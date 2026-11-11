import * as THREE from "three";
import { OrbitControls } from "three/addons/controls/OrbitControls.js";
import { GLTFLoader } from "three/addons/loaders/GLTFLoader.js";

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

export class Viewer3D {
  constructor(container, url, { onSelect }) {
    this.container = container;
    this.url = url;
    this.onSelect = onSelect;
    this.meshesByGuid = new Map();
    this.meshes = [];
    this.state = { checked: new Set(), failed: new Set(), selected: null, active: false };
    this.translucent = new Set();
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
    }
    this.render();
  }

  highlight({ checked, failed }) {
    const s = this.state;
    s.failed = new Set(failed);
    s.checked = new Set(checked.filter((g) => !s.failed.has(g)));
    s.active = true;
    this.applyState();
    this.fit(this.focusMeshes());
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
    return focus.length ? focus : this.meshes;
  }

  clear() {
    Object.assign(this.state, { checked: new Set(), failed: new Set(), selected: null, active: false });
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
      const hits = raycaster.intersectObjects(this.meshes, false);
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
    this.render();
  }

  render() {
    if (this.renderer && this.scene && this.camera) this.renderer.render(this.scene, this.camera);
  }
}
