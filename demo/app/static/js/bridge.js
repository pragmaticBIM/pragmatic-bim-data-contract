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

views.querySelectorAll("[data-layout]").forEach((button) =>
  button.addEventListener("click", () => {
    views.classList.remove("graph", "split", "model");
    views.classList.add(button.dataset.layout);
    views.querySelectorAll("[data-layout]").forEach((b) => b.classList.toggle("active", b === button));
  }),
);
