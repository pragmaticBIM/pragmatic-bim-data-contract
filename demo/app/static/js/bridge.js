// Connects HTMX responses to the two viewers: the server announces what to show via
// HX-Trigger events (pbs:highlight, pbs:select); viewer clicks load the element partial.
import { GraphView } from "./graph.js";
import { Viewer3D } from "./viewer3d.js";

const workspace = document.getElementById("workspace");
const job = workspace.dataset.job;
const views = document.getElementById("views");

const labels = JSON.parse(document.getElementById("labels").textContent);
const props = document.getElementById("props");
const propsPlaceholder = props.innerHTML;

const markSelectedRow = (guid) =>
  document.querySelectorAll(".findings tr[data-guid]").forEach((row) => row.classList.toggle("selected", row.dataset.guid === guid));

const clearSelection = () => {
  graph.select(null);
  viewer.select(null);
  markSelectedRow(null);
  props.innerHTML = propsPlaceholder;
};

const showElement = (guid) => {
  if (!guid) return clearSelection();
  htmx.ajax("GET", `/jobs/${job}/element/${encodeURIComponent(guid)}`, { target: "#props", swap: "innerHTML" });
};

const graph = new GraphView(document.getElementById("graph-view"), `/jobs/${job}/graph.json`, {
  onSelect: showElement,
  legend: document.getElementById("legend"),
  labels,
});
const viewer = new Viewer3D(document.getElementById("model-view"), `/jobs/${job}/model.glb`, { onSelect: showElement });

const fail = (view, error) => {
  console.error(error);
  const status = view.querySelector(".view-status") || view.appendChild(document.createElement("div"));
  status.className = "view-status";
  status.textContent = `${labels.ui["Could not load"] ?? "Could not load"}: ${error.message || error}`;
};

graph
  .load()
  .then(() => viewer.setTranslucent(graph.nodesOfClass("Space")))
  .catch((e) => fail(document.getElementById("graph-view"), e));
if (workspace.dataset.hasGeometry === "true") {
  viewer.load().catch((e) => fail(document.getElementById("model-view"), e));
}

let activeCheck = null;
const markActiveCard = () =>
  document.querySelectorAll(".card").forEach((c) => c.classList.toggle("active", c.dataset.check === activeCheck));

document.body.addEventListener("pbs:highlight", async (event) => {
  activeCheck = event.detail.check;
  markActiveCard();
  const ids = await (await fetch(`/jobs/${job}/checks/${activeCheck}/ids`)).json();
  graph.highlight(ids);
  viewer.highlight(ids);
});

props.addEventListener("click", (event) => {
  const button = event.target.closest("[data-route]");
  if (!button) return;
  activeCheck = null;
  markActiveCard();
  const guids = button.dataset.route.split(" ");
  const edges = guids.slice(1).map((t, i) => ({ s: guids[i], t, p: "pbs:escape_route_next", failed: false }));
  const paths = button.dataset.path
    ? [{ points: JSON.parse(button.dataset.path), failed: false, label: button.dataset.length }]
    : [];
  graph.highlight({ checked: guids, failed: [], edges });
  viewer.highlight({ checked: guids, failed: [], edges, paths });
});

document.body.addEventListener("htmx:afterSettle", (event) => {
  if (event.target.id === "cards") markActiveCard();
});

document.body.addEventListener("pbs:select", (event) => {
  const { guid } = event.detail;
  graph.select(guid);
  viewer.select(guid);
  markSelectedRow(guid);
});

document.addEventListener("keydown", (event) => {
  if (event.key === "Escape") clearSelection();
});

document.getElementById("clear-highlight").addEventListener("click", () => {
  activeCheck = null;
  markActiveCard();
  graph.clear();
  viewer.clear();
  markSelectedRow(null);
  props.innerHTML = propsPlaceholder;
});

const structure = document.querySelector(".structure-tree");
if (structure) {
  const members = JSON.parse(document.getElementById("structure-members").textContent);
  const boxes = [...structure.querySelectorAll("input[data-structure]")];
  const own = (li) => li.querySelector(":scope > label > input");
  structure.addEventListener("change", (event) => {
    const item = event.target.closest("li");
    for (const box of item.querySelectorAll("input[data-structure]")) {
      box.checked = event.target.checked;
      box.indeterminate = false;
    }
    // A parent stays shown while any child is; unticking a single storey keeps its building.
    for (let li = item.parentElement.closest("li"); li; li = li.parentElement.closest("li")) {
      const kids = [...li.querySelectorAll(":scope > ul > li")].map(own);
      own(li).checked = kids.some((k) => k.checked || k.indeterminate);
      own(li).indeterminate = own(li).checked && !kids.every((k) => k.checked && !k.indeterminate);
    }
    const hidden = boxes.filter((box) => !box.checked).flatMap((box) => members[box.dataset.structure] || []);
    graph.setHidden(hidden);
    viewer.setHidden(hidden);
  });
}

views.querySelectorAll("[data-layout]").forEach((button) =>
  button.addEventListener("click", () => {
    views.classList.remove("graph", "split", "model");
    views.classList.add(button.dataset.layout);
    views.querySelectorAll("[data-layout]").forEach((b) => b.classList.toggle("active", b === button));
  }),
);
