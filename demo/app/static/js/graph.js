import Graph from "graphology";
import Sigma from "sigma";
import { EdgeArrowProgram } from "sigma/rendering";
import { DEFAULT_EDGE_CURVATURE, EdgeCurvedArrowProgram, indexParallelEdgesIndex } from "@sigma/edge-curve";
import forceAtlas2 from "graphology-layout-forceatlas2";
import FA2Layout from "graphology-layout-forceatlas2/worker";

// Class colours avoid red, green and orange, which mark failing, passing and selected.
const PALETTE = [
  "#0b6bcb", "#8e4ec6", "#0797b9", "#d6409f", "#8d6c3e", "#5b5bd6",
  "#3a5bc7", "#a144af", "#6e56cf", "#00749e", "#7d5e54", "#c2298a",
];
const FAIL = "#e5484d";
const PASS = "#30a46c";
const SELECT = "#f76b15";
const RELATION_PALETTE = [
  "#8da4bf", "#b48ead", "#88b4a8", "#d0a36b", "#9b9bd8", "#c98a8a",
  "#7fb0d0", "#a3b86c", "#c7a2d6", "#8fa39a", "#d49a6a", "#7d93c4",
];
const NEIGHBOR = "#9aa4ae";
const DIM = "#e3e6ea";
const MAX_NEIGHBOR_FOCUS = 2000;

// BOT relations mirror contract relations (e.g. bot:adjacentElement vs separates_spaces).
const HIDDEN_BY_DEFAULT = /^bot:/;


// Spread parallel edges (several relations between the same two nodes) into distinct curves.
function curvature(index, maxIndex) {
  if (index < 0) return -curvature(-index, maxIndex);
  const amplitude = 3.5;
  const maxCurvature = amplitude * (1 - Math.exp(-maxIndex / amplitude)) * DEFAULT_EDGE_CURVATURE;
  return (maxCurvature * index) / maxIndex;
}

function curveParallelEdges(graph) {
  indexParallelEdgesIndex(graph, {
    edgeIndexAttribute: "parallelIndex",
    edgeMinIndexAttribute: "parallelMinIndex",
    edgeMaxIndexAttribute: "parallelMaxIndex",
  });
  graph.forEachEdge((edge, { parallelIndex, parallelMinIndex, parallelMaxIndex }) => {
    if (typeof parallelIndex !== "number" || !parallelMaxIndex) {
      graph.setEdgeAttribute(edge, "type", "straight");
    } else if (typeof parallelMinIndex === "number" && !parallelIndex) {
      graph.setEdgeAttribute(edge, "type", "straight");
    } else {
      graph.mergeEdgeAttributes(edge, { type: "curved", curvature: curvature(parallelIndex, parallelMaxIndex) });
    }
  });
}

export class GraphView {
  constructor(container, url, { onSelect, legend, labels = {} }) {
    this.container = container;
    this.url = url;
    this.onSelect = onSelect;
    this.legend = legend;
    this.labels = { classes: {}, relations: {}, ui: {}, ...labels };
    this.hiddenRelations = new Set();
    this.hiddenNodes = new Set();
    this.hoveredEdge = null;
    this.state = {
      checked: new Set(),
      failed: new Set(),
      neighbors: new Set(),
      selected: null,
      selectedNeighbors: new Set(),
      ruleEdges: null,
      active: false,
    };
  }

  relationLabel(predicate) {
    return this.labels.relations[predicate]?.[0] ?? predicate.replace(/^pbs:/, "");
  }

  classLabel(cls) {
    return this.labels.classes[cls] ?? cls;
  }

  visibleNeighbors(node) {
    const out = new Set();
    this.graph.forEachEdge(node, (_, attrs, source, target) => {
      if (!this.hiddenRelations.has(attrs.relation)) out.add(source === node ? target : source);
    });
    return out;
  }

  async load() {
    const data = await (await fetch(this.url)).json();
    const graph = new Graph({ type: "directed", multi: true, allowSelfLoops: false });
    const classes = [...new Set(data.nodes.map((n) => n.cls))].sort();
    this.colors = Object.fromEntries(classes.map((c, i) => [c, PALETTE[i % PALETTE.length]]));
    for (const n of data.nodes) {
      graph.addNode(n.id, {
        label: n.label,
        cls: n.cls,
        color: this.colors[n.cls],
        x: Math.random() * 100,
        y: Math.random() * 100,
        size: 2,
      });
    }
    const counts = new Map();
    for (const e of data.edges) {
      if (!graph.hasNode(e.s) || !graph.hasNode(e.t)) continue;
      for (const p of e.p) {
        graph.addEdge(e.s, e.t, { relation: p, label: this.relationLabel(p), size: 1 });
        counts.set(p, (counts.get(p) || 0) + 1);
      }
    }
    this.relations = [...counts.entries()].sort((a, b) => b[1] - a[1]);
    this.relationColors = Object.fromEntries(
      this.relations.map(([p], i) => [p, RELATION_PALETTE[i % RELATION_PALETTE.length]]),
    );
    for (const [p] of this.relations) if (HIDDEN_BY_DEFAULT.test(p)) this.hiddenRelations.add(p);
    graph.forEachEdge((edge, attrs) => graph.setEdgeAttribute(edge, "color", this.relationColors[attrs.relation]));
    graph.forEachNode((node) => graph.setNodeAttribute(node, "size", 2.5 + Math.sqrt(graph.degree(node))));
    curveParallelEdges(graph);
    this.graph = graph;

    this.container.querySelector(".view-status")?.remove();
    this.renderer = new Sigma(graph, this.container, {
      defaultEdgeType: "straight",
      edgeProgramClasses: { straight: EdgeArrowProgram, curved: EdgeCurvedArrowProgram },
      labelRenderedSizeThreshold: 9,
      labelSize: 11,
      renderEdgeLabels: true,
      edgeLabelSize: 10,
      edgeLabelColor: { color: "#4b5560" },
      enableEdgeEvents: true,
      zIndex: true,
      nodeReducer: (node, attrs) => this.reduceNode(node, attrs),
      edgeReducer: (edge, attrs) => this.reduceEdge(edge, attrs),
    });
    this.renderer.on("clickNode", ({ node }) => this.onSelect(node));
    this.renderer.on("clickStage", () => this.onSelect(null));
    this.renderer.on("enterEdge", ({ edge }) => {
      this.hoveredEdge = edge;
      this.renderer.refresh({ skipIndexation: true });
    });
    this.renderer.on("leaveEdge", () => {
      this.hoveredEdge = null;
      this.renderer.refresh({ skipIndexation: true });
    });
    new ResizeObserver(() => {
      this.renderer.resize?.();
      this.renderer.refresh();
    }).observe(this.container);
    this.renderLegend(classes);
    this.renderRelations();
    this.runLayout();
  }

  /** Relation legend inside the graph view; each relation type can be switched off. */
  renderRelations() {
    const panel = document.createElement("div");
    panel.className = "relations-panel";
    const ui = this.labels.ui;
    panel.innerHTML = `
      <div class="relations-head">${ui.Relations ?? "Relations"}</div>
      <label class="relations-all"><input type="checkbox" data-all><span>${ui.All ?? "All"}</span></label>` + this.relations
      .map(([p, n]) => `
        <label title="${p}">
          <input type="checkbox" value="${p}" ${this.hiddenRelations.has(p) ? "" : "checked"}>
          <i style="background:${this.relationColors[p]}"></i>
          <span>${this.relationLabel(p)}</span><span class="n">${n}</span>
        </label>`)
      .join("");
    const all = panel.querySelector("[data-all]");
    const boxes = [...panel.querySelectorAll("input[value]")];
    const syncAll = () => {
      const shown = boxes.filter((box) => box.checked).length;
      all.checked = shown === boxes.length;
      all.indeterminate = shown > 0 && shown < boxes.length;
    };
    panel.addEventListener("change", (event) => {
      const changed = event.target === all ? boxes : [event.target];
      if (event.target === all) boxes.forEach((box) => (box.checked = all.checked));
      for (const { value, checked } of changed) {
        if (checked) this.hiddenRelations.delete(value);
        else this.hiddenRelations.add(value);
      }
      syncAll();
      if (this.state.selected) this.state.selectedNeighbors = this.visibleNeighbors(this.state.selected);
      this.renderer.refresh({ skipIndexation: true });
    });
    syncAll();
    this.container.appendChild(panel);
  }

  /** Nodes (and their edges) left out of the drawing, e.g. hidden storeys. */
  setHidden(guids) {
    this.hiddenNodes = new Set(guids);
    this.renderer?.refresh({ skipIndexation: true });
  }

  nodesOfClass(cls) {
    return this.graph.filterNodes((_, attrs) => attrs.cls === cls);
  }

  runLayout() {
    const settings = { ...forceAtlas2.inferSettings(this.graph), barnesHutOptimize: this.graph.order > 500 };
    const duration = Math.min(2500 + this.graph.order * 2, 15000);
    try {
      const layout = new FA2Layout(this.graph, { settings });
      layout.start();
      setTimeout(() => layout.kill(), duration);
    } catch (error) {
      console.warn("ForceAtlas2 worker unavailable, running synchronously", error);
      forceAtlas2.assign(this.graph, { settings, iterations: this.graph.order > 5000 ? 50 : 200 });
    }
  }

  renderLegend(classes) {
    if (!this.legend) return;
    this.legend.innerHTML = classes
      .map((c) => `<span title="${c}"><i style="background:${this.colors[c]}"></i>${this.classLabel(c)}</span>`)
      .join("");
  }

  reduceNode(node, attrs) {
    if (this.hiddenNodes.has(node)) return { ...attrs, hidden: true };
    const s = this.state;
    const res = { ...attrs };
    if (s.selected && s.selected !== node && !s.selectedNeighbors.has(node)) {
      return { ...attrs, color: DIM, label: "", zIndex: 0 };
    }
    if (s.active) {
      if (s.failed.has(node)) {
        res.color = FAIL;
        res.zIndex = 2;
      } else if (s.checked.has(node)) {
        res.color = PASS;
        res.zIndex = 1;
      } else if (s.neighbors.has(node)) {
        res.color = NEIGHBOR;
      } else {
        res.color = DIM;
        res.label = "";
        res.zIndex = 0;
      }
    }
    if (s.selected === node) {
      res.color = SELECT;
      res.highlighted = true;
      res.forceLabel = true;
      res.size = attrs.size * 1.6;
      res.zIndex = 3;
    }
    return res;
  }

  reduceEdge(edge, attrs) {
    const s = this.state;
    const [source, target] = this.graph.extremities(edge);
    if (this.hiddenNodes.has(source) || this.hiddenNodes.has(target)) return { ...attrs, hidden: true };
    if (s.active && s.ruleEdges && !s.selected) {
      const rule = s.ruleEdges.get(`${source}|${target}|${attrs.relation}`);
      if (!rule) return { ...attrs, hidden: true };
      const hovered = edge === this.hoveredEdge;
      const label = rule.label ? `${attrs.label} · ${rule.label}` : attrs.label;
      return {
        ...attrs, label, color: rule.failed ? FAIL : PASS, size: hovered ? 3 : 2, forceLabel: hovered || Boolean(rule.label), zIndex: 2,
      };
    }
    if (this.hiddenRelations.has(attrs.relation)) return { ...attrs, hidden: true };
    if (edge === this.hoveredEdge) return { ...attrs, size: 2.5, forceLabel: true, zIndex: 3 };
    if (s.selected) {
      if (source === s.selected || target === s.selected) return { ...attrs, size: 2, forceLabel: true, zIndex: 2 };
      return { ...attrs, hidden: true };
    }
    if (!s.active) return attrs;
    const focus = s.failed.size ? s.failed : s.checked;
    if (focus.has(source) || focus.has(target)) return attrs;
    return { ...attrs, hidden: true };
  }

  /** ``edges`` (``{s, t, p, failed}``) replaces all other edges while the highlight is active. */
  highlight({ checked, failed, edges = [] }) {
    if (!this.graph) return;
    const s = this.state;
    s.failed = new Set(failed.filter((n) => this.graph.hasNode(n)));
    s.checked = new Set(checked.filter((n) => this.graph.hasNode(n) && !s.failed.has(n)));
    s.active = true;
    const focus = s.failed.size ? s.failed : s.checked;
    s.neighbors = new Set();
    s.ruleEdges = edges.length ? new Map(edges.map((e) => [`${e.s}|${e.t}|${e.p}`, e])) : null;
    if (s.ruleEdges) {
      for (const e of edges) for (const n of [e.s, e.t]) if (this.graph.hasNode(n)) s.neighbors.add(n);
    } else if (focus.size <= MAX_NEIGHBOR_FOCUS) {
      for (const n of focus) for (const m of this.visibleNeighbors(n)) s.neighbors.add(m);
    }
    this.renderer.refresh();
    this.focusOn(s.ruleEdges ? [...focus, ...s.checked, ...s.neighbors] : [...focus]);
  }

  /** Selected node with its related nodes stays visible, everything else fades; null clears. */
  select(guid) {
    if (!this.graph) return;
    const s = this.state;
    s.selected = guid && this.graph.hasNode(guid) ? guid : null;
    s.selectedNeighbors = s.selected ? this.visibleNeighbors(s.selected) : new Set();
    this.renderer.refresh({ skipIndexation: true });
    if (s.selected) this.focusOn([s.selected, ...s.selectedNeighbors], 0.25);
  }

  clear() {
    if (!this.graph) return;
    Object.assign(this.state, {
      checked: new Set(),
      failed: new Set(),
      neighbors: new Set(),
      selected: null,
      selectedNeighbors: new Set(),
      ruleEdges: null,
      active: false,
    });
    this.renderer.refresh();
    this.renderer.getCamera().animate({ x: 0.5, y: 0.5, ratio: 1 }, { duration: 400 });
  }

  focusOn(nodes, minRatio = 0.3) {
    const points = nodes.map((n) => this.renderer.getNodeDisplayData(n)).filter(Boolean);
    if (!points.length) return;
    const xs = points.map((p) => p.x);
    const ys = points.map((p) => p.y);
    const [minX, maxX, minY, maxY] = [Math.min(...xs), Math.max(...xs), Math.min(...ys), Math.max(...ys)];
    const ratio = Math.min(1.2, Math.max(minRatio, Math.max(maxX - minX, maxY - minY) * 1.3));
    this.renderer.getCamera().animate({ x: (minX + maxX) / 2, y: (minY + maxY) / 2, ratio }, { duration: 500 });
  }
}
