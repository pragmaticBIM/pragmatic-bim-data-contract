import * as THREE from "three";
import { OrbitControls } from "three/addons/controls/OrbitControls.js";
import { GLTFLoader } from "three/addons/loaders/GLTFLoader.js";
import { Line2 } from "three/addons/lines/Line2.js";
import { LineGeometry } from "three/addons/lines/LineGeometry.js";
import { LineMaterial } from "three/addons/lines/LineMaterial.js";

const GLOBAL_ID = /^[0-9A-Za-z_$]{22}$/;
const CLICK_TOLERANCE = 4;

// The IfcOpenShell GLB has no vertex normals; lit materials need flat shading.
const material = (color, extra = {}) =>
  new THREE.MeshLambertMaterial({ color, side: THREE.DoubleSide, flatShading: true, ...extra });
const seeThrough = (color, opacity) => material(color, { transparent: true, opacity, depthWrite: false });
const MATERIALS = {
  fail: material(0xe5484d),
  pass: material(0x30a46c),
  select: material(0xf76b15),
  ghost: seeThrough(0xb8c2cc, 0.08),
  space: seeThrough(0x7fb3e6, 0.15),
};
const TRANSLUCENT = {
  fail: seeThrough(0xe5484d, 0.35),
  pass: seeThrough(0x30a46c, 0.25),
  select: seeThrough(0xf76b15, 0.5),
};
const SEE_THROUGH = new Set([MATERIALS.ghost, MATERIALS.space, ...Object.values(TRANSLUCENT)]);
const LINE_COLORS = { fail: 0xe5484d, pass: 0x30a46c };
// Paths are stored at floor level; lift them so the floor slab does not hide them.
const PATH_LIFT = 0.15;
// Closer than this, a line to the related element's surface would vanish; aim at its centre instead.
const MIN_LINE_LENGTH = 0.3;

// IFC project coordinates (Z up) to the scene of the IfcOpenShell GLB (Y up).
const fromIfc = ([x, y, z]) => new THREE.Vector3(x, z, -y);

/** Point halfway along a polyline, measured by length. */
function midpoint(points) {
  const lengths = points.slice(1).map((p, i) => p.distanceTo(points[i]));
  let rest = lengths.reduce((a, b) => a + b, 0) / 2;
  for (let i = 0; i < lengths.length; i++) {
    if (rest <= lengths[i]) return points[i].clone().lerp(points[i + 1], lengths[i] ? rest / lengths[i] : 0);
    rest -= lengths[i];
  }
  return points[points.length - 1].clone();
}

export class Viewer3D {
  constructor(container, url, { onSelect }) {
    this.container = container;
    this.url = url;
    this.onSelect = onSelect;
    this.meshesByGuid = new Map();
    this.meshes = [];
    this.state = { checked: new Set(), failed: new Set(), selected: null, active: false };
    this.translucent = new Set();
    this.boxes = new Map();
    this.hidden = new Set();
    this.drawn = {};
    this.lineMaterials = Object.fromEntries(
      Object.entries(LINE_COLORS).map(([k, color]) => [
        k,
        new LineMaterial({ color, linewidth: 3, depthTest: false, transparent: true, opacity: 0.95 }),
      ]),
    );
    this.dotMaterials = Object.fromEntries(
      Object.entries(LINE_COLORS).map(([k, color]) => [k, new THREE.MeshBasicMaterial({ color, depthTest: false })]),
    );
  }

  /** Volumes such as spaces would hide the building elements; draw them see-through. */
  setTranslucent(guids) {
    this.translucent = new Set(guids);
    if (this.model) this.applyState();
  }

  async load() {
    const { clientWidth: w, clientHeight: h } = this.container;
    this.renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true });
    this.renderer.setPixelRatio(window.devicePixelRatio);
    this.renderer.setSize(w || 1, h || 1);
    for (const m of Object.values(this.lineMaterials)) m.resolution.set(w || 1, h || 1);
    this.container.appendChild(this.renderer.domElement);

    this.scene = new THREE.Scene();
    this.scene.add(new THREE.HemisphereLight(0xffffff, 0x8d99a6, 2.2));
    const sun = new THREE.DirectionalLight(0xffffff, 1.6);
    sun.position.set(1, 2, 1.5);
    this.scene.add(sun);

    this.camera = new THREE.PerspectiveCamera(45, (w || 1) / (h || 1), 0.05, 5000);
    this.controls = new OrbitControls(this.camera, this.renderer.domElement);
    this.controls.addEventListener("change", () => this.render());
    this.controls.enableDamping = false;

    new ResizeObserver(() => this.resize()).observe(this.container);
    this.bindPicking();

    const gltf = await new GLTFLoader().loadAsync(this.url);
    this.model = gltf.scene;
    this.scene.add(this.model);
    this.connections = new THREE.Group();
    this.scene.add(this.connections);
    this.index();
    this.applyState();
    this.container.querySelector(".view-status")?.remove();
    this.fit(this.meshes);
  }

  index() {
    this.model.traverse((object) => {
      if (!object.isMesh) return;
      let node = object;
      while (node && !GLOBAL_ID.test(node.name)) node = node.parent;
      if (!node) return;
      object.userData.guid = node.name;
      object.userData.original = object.material;
      this.meshes.push(object);
      if (!this.meshesByGuid.has(node.name)) this.meshesByGuid.set(node.name, []);
      this.meshesByGuid.get(node.name).push(object);
    });
  }

  applyState() {
    const s = this.state;
    for (const mesh of this.meshes) {
      const guid = mesh.userData.guid;
      const volume = this.translucent.has(guid);
      // With a selection, everything except the selected element is drawn see-through.
      const palette = volume || s.selected ? TRANSLUCENT : MATERIALS;
      let next = volume ? MATERIALS.space : mesh.userData.original;
      if (guid === s.selected) next = volume ? TRANSLUCENT.select : MATERIALS.select;
      else if (s.active && s.failed.has(guid)) next = palette.fail;
      else if (s.active && s.checked.has(guid)) next = palette.pass;
      else if (s.active || s.selected) next = MATERIALS.ghost;
      mesh.material = next;
      mesh.renderOrder = SEE_THROUGH.has(next) ? 1 : 0;
      mesh.visible = !this.hidden.has(guid);
    }
    this.render();
  }

  /** ``paths`` (``{points, failed}``, IFC coordinates) are drawn when given, else ``edges`` (``{s, t, failed}``). */
  highlight({ checked, failed, edges = [], paths = [] }) {
    const s = this.state;
    s.failed = new Set(failed);
    s.checked = new Set(checked.filter((g) => !s.failed.has(g)));
    s.active = true;
    this.setConnections(paths.length ? { paths } : { edges });
    this.applyState();
    const drawn = paths.length || edges.length;
    const related = [...s.failed, ...s.checked].flatMap((g) => this.meshesByGuid.get(g) || []).filter((m) => m.visible);
    this.fit(drawn && related.length ? related : this.focusMeshes());
  }

  /** Elements left out of the model, e.g. hidden storeys; their connection lines go too. */
  setHidden(guids) {
    this.hidden = new Set(guids);
    if (!this.model) return;
    this.setConnections(this.drawn);
    this.applyState();
  }

  setConnections({ edges = [], paths = [] }) {
    if (!this.connections) return;
    this.drawn = { edges, paths };
    paths = paths.filter((p) => !this.hidden.has(p.guid));
    edges = edges.filter((e) => !this.hidden.has(e.s) && !this.hidden.has(e.t));
    for (const child of [...this.connections.children]) {
      this.connections.remove(child);
      if (child.isSprite) {
        child.material.map.dispose();
        child.material.dispose();
      } else {
        child.geometry?.dispose();
      }
    }
    for (const path of paths) {
      const points = path.points.map((p) => fromIfc(p).add(new THREE.Vector3(0, PATH_LIFT, 0)));
      this.addLine(points, path.failed);
      this.addDot(points[0], path.failed);
      if (path.label) this.addLabel(midpoint(points), path.label, path.failed);
    }
    for (const edge of edges) {
      const from = this.box(edge.s)?.getCenter(new THREE.Vector3());
      const target = this.box(edge.t);
      if (!from || !target) continue;
      let to = target.clampPoint(from, new THREE.Vector3());
      if (to.distanceTo(from) < MIN_LINE_LENGTH) to = target.getCenter(new THREE.Vector3());
      this.addLine([from, to], edge.failed);
      this.addDot(from, edge.failed);
    }
    this.render();
  }

  addLine(points, failed) {
    if (points.length < 2) return;
    const geometry = new LineGeometry();
    geometry.setPositions(points.flatMap((p) => [p.x, p.y, p.z]));
    const line = new Line2(geometry, this.lineMaterials[failed ? "fail" : "pass"]);
    line.computeLineDistances();
    line.renderOrder = 10;
    this.connections.add(line);
  }

  addDot(point, failed) {
    const dot = new THREE.Mesh(new THREE.SphereGeometry(0.12, 12, 8), this.dotMaterials[failed ? "fail" : "pass"]);
    dot.position.copy(point);
    dot.renderOrder = 10;
    this.connections.add(dot);
  }

  addLabel(point, text, failed) {
    const canvas = document.createElement("canvas");
    const ctx = canvas.getContext("2d");
    const font = "600 36px system-ui, sans-serif";
    ctx.font = font;
    canvas.width = Math.ceil(ctx.measureText(text).width) + 24;
    canvas.height = 52;
    ctx.font = font;
    ctx.fillStyle = failed ? "#e5484d" : "#30a46c";
    ctx.beginPath();
    ctx.roundRect(0, 0, canvas.width, canvas.height, 10);
    ctx.fill();
    ctx.fillStyle = "#fff";
    ctx.textBaseline = "middle";
    ctx.fillText(text, 12, canvas.height / 2 + 1);
    const texture = new THREE.CanvasTexture(canvas);
    texture.colorSpace = THREE.SRGBColorSpace;
    const sprite = new THREE.Sprite(new THREE.SpriteMaterial({ map: texture, depthTest: false, sizeAttenuation: false }));
    const height = 0.022;
    sprite.scale.set((height * canvas.width) / canvas.height, height, 1);
    sprite.center.set(0.5, -0.4);
    sprite.position.copy(point);
    sprite.renderOrder = 11;
    this.connections.add(sprite);
  }

  box(guid) {
    if (!this.boxes.has(guid)) {
      const meshes = this.meshesByGuid.get(guid);
      const box = new THREE.Box3();
      for (const mesh of meshes || []) box.expandByObject(mesh);
      this.boxes.set(guid, box.isEmpty() ? null : box);
    }
    return this.boxes.get(guid);
  }

  /** null clears the selection. */
  select(guid) {
    const hadSelection = Boolean(this.state.selected);
    this.state.selected = guid && this.meshesByGuid.has(guid) ? guid : null;
    this.applyState();
    if (this.state.selected) this.fit(this.meshesByGuid.get(guid), 3);
    else if (hadSelection) this.fit(this.focusMeshes());
  }

  focusMeshes() {
    const s = this.state;
    const focus = s.active ? [...(s.failed.size ? s.failed : s.checked)].flatMap((g) => this.meshesByGuid.get(g) || []) : [];
    const shown = (meshes) => meshes.filter((m) => m.visible);
    return shown(focus).length ? shown(focus) : shown(this.meshes);
  }

  clear() {
    Object.assign(this.state, { checked: new Set(), failed: new Set(), selected: null, active: false });
    this.setConnections({});
    this.applyState();
    this.fit(this.meshes);
  }

  fit(meshes, padding = 1.3) {
    if (!meshes?.length || !this.camera) return;
    const box = new THREE.Box3();
    for (const mesh of meshes) box.expandByObject(mesh);
    if (box.isEmpty()) return;
    const center = box.getCenter(new THREE.Vector3());
    const radius = Math.max(box.getSize(new THREE.Vector3()).length() / 2, 0.5);
    const distance = (radius * padding) / Math.sin(THREE.MathUtils.degToRad(this.camera.fov / 2));
    const direction = this.camera.position.clone().sub(this.controls.target);
    if (direction.lengthSq() < 1e-6) direction.set(1, 0.8, 1.2);
    direction.normalize();
    this.controls.target.copy(center);
    this.camera.position.copy(center).addScaledVector(direction, distance);
    this.camera.near = Math.max(distance / 1000, 0.01);
    this.camera.far = distance * 100;
    this.camera.updateProjectionMatrix();
    this.controls.update();
    this.render();
  }

  bindPicking() {
    const raycaster = new THREE.Raycaster();
    const canvas = this.renderer.domElement;
    let down = null;
    canvas.addEventListener("pointerdown", (e) => (down = [e.clientX, e.clientY]));
    canvas.addEventListener("pointerup", (e) => {
      if (!down || Math.hypot(e.clientX - down[0], e.clientY - down[1]) > CLICK_TOLERANCE) return;
      const rect = canvas.getBoundingClientRect();
      const pointer = new THREE.Vector2(
        ((e.clientX - rect.left) / rect.width) * 2 - 1,
        -((e.clientY - rect.top) / rect.height) * 2 + 1,
      );
      raycaster.setFromCamera(pointer, this.camera);
      const hits = raycaster.intersectObjects(this.meshes.filter((m) => m.visible), false);
      const hit = hits.find((h) => !SEE_THROUGH.has(h.object.material)) || hits[0];
      this.onSelect(hit ? hit.object.userData.guid : null);
    });
  }

  resize() {
    const { clientWidth: w, clientHeight: h } = this.container;
    if (!w || !h || !this.camera) return;
    this.camera.aspect = w / h;
    this.camera.updateProjectionMatrix();
    this.renderer.setSize(w, h);
    for (const m of Object.values(this.lineMaterials)) m.resolution.set(w, h);
    this.render();
  }

  render() {
    if (this.renderer && this.scene && this.camera) this.renderer.render(this.scene, this.camera);
  }
}
