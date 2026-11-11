"""FastAPI app: ``uvicorn demo.app.main:app --reload`` from the repository root."""

from __future__ import annotations

import json
from collections import defaultdict
from contextlib import asynccontextmanager
from functools import lru_cache
from pathlib import Path
from typing import Any

import shapely
from fastapi import FastAPI, File, HTTPException, Request, UploadFile
from fastapi.responses import FileResponse, HTMLResponse, JSONResponse, RedirectResponse, Response
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from demo.app import i18n, jobs

APP_DIR = Path(__file__).resolve().parent


def _labels(request: Request) -> dict[str, Any]:
    labels = i18n.Labels.from_cookies(request.cookies)
    return {"L": labels, "t": labels.t}


templates = Jinja2Templates(directory=APP_DIR / "templates", context_processors=[_labels])
templates.env.globals["languages"] = i18n.LANGUAGES
DETAIL_ITEM_LIMIT = 500


@asynccontextmanager
async def lifespan(_: FastAPI):
    jobs.DATA_DIR.mkdir(parents=True, exist_ok=True)
    jobs.mark_interrupted()
    yield
    jobs.shutdown()


app = FastAPI(title="Pragmatic BIM check demo", lifespan=lifespan)
app.mount("/static", StaticFiles(directory=APP_DIR / "static"), name="static")


# --- job data -----------------------------------------------------------------


class Job:
    def __init__(self, job_id: str) -> None:
        directory = jobs.job_dir(job_id)
        if directory is None:
            raise HTTPException(404, "Unknown job")
        self.id = job_id
        self.dir = directory
        self.meta = jobs.read_json(directory / "meta.json", {})
        self.status = jobs.status(directory)

    @property
    def done(self) -> bool:
        return self.status.get("stage") == "done"

    def checks(self) -> list[dict[str, Any]]:
        return _load(self.dir / "checks.json")

    def check(self, check_id: str) -> dict[str, Any]:
        for check in self.checks():
            if check["id"] == check_id:
                return check
        raise HTTPException(404, "Unknown check")

    def elements(self) -> dict[str, dict[str, Any]]:
        return _load(self.dir / "elements.json")

    def report(self) -> dict[str, Any]:
        return _load(self.dir / "report.json")


def _load(path: Path) -> Any:
    if not path.is_file():
        raise HTTPException(404, f"{path.name} not available")
    stat = path.stat()
    return _cached_json(str(path), stat.st_mtime_ns)


@lru_cache(maxsize=32)
def _cached_json(path: str, _mtime: int) -> Any:
    return json.loads(Path(path).read_text(encoding="utf-8"))


def _summary(checks: list[dict[str, Any]]) -> dict[str, int]:
    summary = {"fail": 0, "pass": 0, "na": 0}
    for check in checks:
        summary[check["status"]] += 1
    return summary


def _filter(checks: list[dict[str, Any]], show: str) -> list[dict[str, Any]]:
    return [c for c in checks if show == "all" or c["status"] == show]


def _relation_groups(element: dict[str, Any]) -> list[dict[str, Any]]:
    """Links grouped by relation type and direction (outgoing first), in link order."""
    groups: dict[tuple[str, str], list[str]] = {}
    for link in element["links"]:
        groups.setdefault((link["predicate"], link["direction"]), []).append(link["guid"])
    return [{"predicate": p, "direction": d, "guids": guids} for (p, d), guids in groups.items()]


STRUCTURE_CLASSES = {
    "Project", "PerimeterContext", "LegalSiteContext", "BuiltAssetContext",
    "BuildingContext", "CivilStructureContext", "LevelContext",
}


def _structure(elements: dict[str, dict[str, Any]]) -> tuple[list[dict[str, Any]], dict[str, list[str]]]:
    """Spatial tree (project → perimeter → building → level) and the elements each node hides.

    Levels are ordered top down by elevation; an element belongs to its ``parent_level``.
    """
    nodes = {g: e for g, e in elements.items() if e["cls"] in STRUCTURE_CLASSES}
    parent = {}
    for guid, node in nodes.items():
        parent_link = next(
            (
                link["guid"]
                for link in node["links"]
                if link["direction"] == "out" and link["predicate"].startswith("pbs:parent_") and link["guid"] in nodes
            ),
            None,
        )
        if parent_link:
            parent[guid] = parent_link
    children: dict[str, list[str]] = defaultdict(list)
    for guid, parent_guid in parent.items():
        children[parent_guid].append(guid)
    on_level: dict[str, list[str]] = defaultdict(list)
    for guid, element in elements.items():
        if element.get("level") in nodes and guid not in nodes:
            on_level[element["level"]].append(guid)

    def elevation(guid: str) -> float:
        return next((a["value"] for a in nodes[guid]["attributes"] if a["key"] == "pbs:elevation"), 0.0)

    members: dict[str, list[str]] = {}

    def build(guid: str) -> dict[str, Any]:
        kids = sorted(children[guid], key=lambda k: (-elevation(k), nodes[k]["name"]))
        subtree = [build(k) for k in kids]
        members[guid] = [guid, *on_level[guid], *(m for k in kids for m in members[k])]
        return {"guid": guid, "name": nodes[guid]["name"], "cls": nodes[guid]["cls"], "children": subtree,
                "count": len(members[guid]) - 1}

    roots = sorted((g for g in nodes if g not in parent), key=lambda g: nodes[g]["name"])
    return [build(root) for root in roots], members


def _rule_connections(
    check: dict[str, Any], elements: dict[str, dict[str, Any]]
) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    """Edges ``{s, t, p, failed}`` of the rule's relations around its checked elements, and their 3D paths."""
    view = check.get("view") or {}
    relations = set(view.get("relations") or ())
    if not relations:
        return [], []
    failed = set(check["failed"])
    quantity = view.get("quantity")
    edges: dict[tuple[str, str, str], bool] = {}
    paths = []
    for guid in check["checked"]:
        if guid not in elements:
            continue
        bad = guid in failed
        frontier, seen = [guid], {guid}
        while frontier:
            current = frontier.pop()
            for link in elements[current]["links"]:
                if link["predicate"] not in relations or (view.get("chain") and link["direction"] != "out"):
                    continue
                other = link["guid"]
                source, target = (current, other) if link["direction"] == "out" else (other, current)
                key = (source, target, link["predicate"])
                edges[key] = edges.get(key, False) or bad
                if view.get("chain") and other not in seen and other in elements:
                    seen.add(other)
                    frontier.append(other)
        points = _path_points(elements[guid], view["path"]) if view.get("path") else None
        if points:
            paths.append({"guid": guid, "points": points, "failed": bad, "label": _label(elements[guid], quantity)})
    edge_list = [
        {"s": s, "t": t, "p": p, "failed": bad, "label": _label(elements[s], quantity)}
        for (s, t, p), bad in sorted(edges.items())
    ]
    return edge_list, paths


def _label(element: dict[str, Any], quantity: str | None) -> str | None:
    """``"12.3 m"`` for the element's ``quantity`` record, if it has one."""
    for record in element["records"].get("pbs:quantity_values", []) if quantity else ():
        if record.get("pbs:quantity_type") == quantity:
            return f'{record["pbs:quantity_value"]:.1f} {record.get("pbs:quantity_unit", "")}'.strip()
    return None


def _path_points(element: dict[str, Any], representation: str) -> list[list[float]] | None:
    for record in element["records"].get("pbs:geometry_representations", []):
        if record.get("pbs:geometry_representation") == representation and record.get("pbs:geometry_wkt"):
            return [list(c) for c in shapely.from_wkt(record["pbs:geometry_wkt"]).coords]
    return None


def _route_length(element: dict[str, Any]) -> float | None:
    for record in element["records"].get("pbs:quantity_values", []):
        if record.get("pbs:quantity_type") == "pbs:quantity_type_escape_route_length":
            return record.get("pbs:quantity_value")
    return None


def _escape_route(element: dict[str, Any], elements: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    """Elements along ``escape_route_next`` from ``element``, each with its remaining route length."""
    hops: list[dict[str, Any]] = []
    guid: str | None = element["guid"]
    while guid in elements and all(hop["guid"] != guid for hop in hops):
        current = elements[guid]
        hops.append({"guid": guid, "element": current, "length": _route_length(current)})
        guid = next(
            (
                link["guid"]
                for link in current["links"]
                if link["predicate"] == "pbs:escape_route_next" and link["direction"] == "out"
            ),
            None,
        )
    return hops if len(hops) > 1 else []


def _trigger(response: Response, event: str, detail: dict[str, Any]) -> Response:
    response.headers["HX-Trigger"] = json.dumps({event: detail})
    return response


# --- pages --------------------------------------------------------------------


@app.get("/", response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse(request, "index.html", {"jobs": jobs.list_jobs()})


@app.get("/lang/{lang}")
def set_language(lang: str, next: str = "/"):
    if lang not in i18n.LANGUAGES:
        raise HTTPException(404, "Unknown language")
    target = next if next.startswith("/") and not next.startswith("//") else "/"
    response = RedirectResponse(target, status_code=303)
    response.set_cookie(i18n.COOKIE, lang, max_age=365 * 24 * 3600, samesite="lax")
    return response


@app.post("/jobs")
async def upload(request: Request, file: UploadFile = File(...)):
    name = Path(file.filename or "model.ifc").name
    if not name.lower().endswith(".ifc"):
        raise HTTPException(400, "Upload an .ifc file")
    job_id = jobs.create_job(name, await file.read())
    jobs.submit(job_id)
    url = f"/jobs/{job_id}"
    if request.headers.get("HX-Request"):
        return Response(status_code=204, headers={"HX-Redirect": url})
    return RedirectResponse(url, status_code=303)


@app.get("/jobs/{job_id}", response_class=HTMLResponse)
def workspace(request: Request, job_id: str):
    job = Job(job_id)
    if not job.done:
        return templates.TemplateResponse(request, "processing.html", {"job": job})
    checks = job.checks()
    context = {
        "job": job,
        "checks": _filter(checks, "fail"),
        "summary": _summary(checks),
        "show": "fail",
        "has_geometry": (job.dir / "model.glb").is_file(),
    }
    context["structure"], context["structure_members"] = _structure(job.elements())
    return templates.TemplateResponse(request, "job.html", context)


@app.get("/jobs/{job_id}/status", response_class=HTMLResponse)
def job_status(request: Request, job_id: str):
    job = Job(job_id)
    response = templates.TemplateResponse(request, "partials/status.html", {"job": job})
    if job.done:
        response.headers["HX-Refresh"] = "true"
    return response


@app.get("/jobs/{job_id}/cards", response_class=HTMLResponse)
def cards(request: Request, job_id: str, show: str = "fail"):
    job = Job(job_id)
    context = {"job": job, "checks": _filter(job.checks(), show), "show": show}
    return templates.TemplateResponse(request, "partials/cards.html", context)


@app.get("/jobs/{job_id}/checks/{check_id}", response_class=HTMLResponse)
def check_detail(request: Request, job_id: str, check_id: str):
    job = Job(job_id)
    check = job.check(check_id)
    context = {
        "job": job,
        "check": check,
        "elements": job.elements(),
        "items": check["items"][:DETAIL_ITEM_LIMIT],
        "limit": DETAIL_ITEM_LIMIT,
    }
    response = templates.TemplateResponse(request, "partials/check_detail.html", context)
    return _trigger(response, "pbs:highlight", {"check": check_id})


@app.get("/jobs/{job_id}/checks/{check_id}/ids")
def check_ids(job_id: str, check_id: str):
    """Highlight sets for both viewers; fetched by ``bridge.js`` (too large for a header)."""
    job = Job(job_id)
    check = job.check(check_id)
    edges, paths = _rule_connections(check, job.elements())
    return JSONResponse({"checked": check["checked"], "failed": check["failed"], "edges": edges, "paths": paths})


@app.get("/jobs/{job_id}/element/{guid}", response_class=HTMLResponse)
def element(request: Request, job_id: str, guid: str):
    job = Job(job_id)
    elements = job.elements()
    findings = [
        {"check": c, "items": [i for i in c["items"] if i["guid"] == guid]}
        for c in job.checks()
        if guid in c["failed"]
    ]
    element = elements.get(guid)
    context = {
        "job": job,
        "guid": guid,
        "element": element,
        "elements": elements,
        "findings": findings,
        "relations": _relation_groups(element) if element else [],
        "route": _escape_route(element, elements) if element else [],
        "route_path": _path_points(element, "path_3d") if element else None,
    }
    response = templates.TemplateResponse(request, "partials/element.html", context)
    return _trigger(response, "pbs:select", {"guid": guid})


@app.get("/jobs/{job_id}/graph.json")
def graph_json(job_id: str):
    return FileResponse(Job(job_id).dir / "graph.json", media_type="application/json")


@app.get("/jobs/{job_id}/model.glb")
def model_glb(job_id: str):
    path = Job(job_id).dir / "model.glb"
    if not path.is_file():
        raise HTTPException(404, "No geometry")
    return FileResponse(path, media_type="model/gltf-binary")


@app.get("/jobs/{job_id}/report.html", response_class=HTMLResponse)
def report(request: Request, job_id: str):
    job = Job(job_id)
    checks = job.checks()
    context = {
        "job": job,
        "checks": checks,
        "summary": _summary(checks),
        "conversion": job.report(),
        "elements": job.elements(),
        "css": (APP_DIR / "static" / "css" / "report.css").read_text(encoding="utf-8"),
    }
    response = templates.TemplateResponse(request, "report.html", context)
    stem = Path(job.meta.get("name", "model.ifc")).stem
    response.headers["Content-Disposition"] = f'attachment; filename="{stem}-check-report.html"'
    return response
