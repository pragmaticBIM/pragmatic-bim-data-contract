"""Smoke test for the local check demo: worker outputs and the HTMX routes on the synthetic model."""

from __future__ import annotations

import json
import sys
from pathlib import Path

import pytest

pytest.importorskip("ifcopenshell")
pytest.importorskip("pyshacl")
pytest.importorskip("fastapi")
pytest.importorskip("httpx")

REPO_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO_ROOT))
sys.path.insert(0, str(REPO_ROOT / "tests" / "ifc2rdf"))

from checks import REFERENCE_FIXTURE  # noqa: E402
from fastapi.testclient import TestClient  # noqa: E402
from synthetic import DEMO_GLOBAL_IDS, build_demo_model  # noqa: E402

from demo.app import jobs  # noqa: E402
from demo.app.main import app  # noqa: E402
from demo.app.worker import run_job  # noqa: E402

JOB_ID = "0123456789ab"


@pytest.fixture(scope="module")
def job(tmp_path_factory) -> Path:
    data = tmp_path_factory.mktemp("demo-data")
    directory = data / JOB_ID
    directory.mkdir()
    build_demo_model(directory / "model.ifc")
    jobs.write_json(directory / "meta.json", {"name": "demo.ifc", "uploaded_at": "2026-01-01T00:00:00+00:00"})
    run_job(directory, reference=REFERENCE_FIXTURE)
    return directory


@pytest.fixture
def client(job, monkeypatch):
    monkeypatch.setattr(jobs, "DATA_DIR", job.parent)
    with TestClient(app) as client:
        yield client


def test_worker_outputs(job):
    status = json.loads((job / "status.json").read_text())
    assert status["stage"] == "done", status.get("error")
    for name in ("model.ttl", "model.glb", "graph.json", "elements.json", "checks.json", "report.json"):
        assert (job / name).is_file(), name

    graph = json.loads((job / "graph.json").read_text())
    node_ids = {n["id"] for n in graph["nodes"]}
    assert node_ids
    assert all(e["s"] in node_ids and e["t"] in node_ids for e in graph["edges"])

    checks = json.loads((job / "checks.json").read_text())
    assert checks and all(c["id"].startswith("rule-") for c in checks)
    for check in checks:
        assert set(check["failed"]) <= set(check["checked"]) <= node_ids, check["id"]


def test_rules(job):
    checks = {c["id"]: c for c in json.loads((job / "checks.json").read_text())}

    doors = checks["rule-DoorFireRating"]
    assert doors["failed"] == sorted([DEMO_GLOBAL_IDS["door_ifc"], DEMO_GLOBAL_IDS["door_geometry"]])
    assert {i["message"] for i in doors["items"]} == {"Door rated none in a EI60 wall; required at least EI30."}

    guards = checks["rule-GuardHeight"]
    assert guards["status"] == "pass"
    assert {DEMO_GLOBAL_IDS["railing_front"], DEMO_GLOBAL_IDS["railing_side"]} <= set(guards["checked"])


def test_workspace_and_check_detail(client):
    page = client.get(f"/jobs/{JOB_ID}")
    assert page.status_code == 200
    assert 'data-job="0123456789ab"' in page.text

    checks = json.loads((jobs.DATA_DIR / JOB_ID / "checks.json").read_text())
    check = checks[0]
    detail = client.get(f"/jobs/{JOB_ID}/checks/{check['id']}", headers={"HX-Request": "true"})
    assert detail.status_code == 200
    assert json.loads(detail.headers["HX-Trigger"]) == {"pbs:highlight": {"check": check["id"]}}
    ids = client.get(f"/jobs/{JOB_ID}/checks/{check['id']}/ids").json()
    assert ids == {"checked": check["checked"], "failed": check["failed"]}

    cards = client.get(f"/jobs/{JOB_ID}/cards?show=all", headers={"HX-Request": "true"})
    assert cards.status_code == 200 and 'id="cards"' in cards.text


def test_element_and_report(client):
    graph = json.loads((jobs.DATA_DIR / JOB_ID / "graph.json").read_text())
    guid = graph["nodes"][0]["id"]
    element = client.get(f"/jobs/{JOB_ID}/element/{guid}")
    assert element.status_code == 200
    assert json.loads(element.headers["HX-Trigger"]) == {"pbs:select": {"guid": guid}}
    assert guid in element.text

    report = client.get(f"/jobs/{JOB_ID}/report.html")
    assert report.status_code == 200
    assert "attachment" in report.headers["Content-Disposition"]
    assert "Prüfbericht: demo.ifc" in report.text

    assert client.get(f"/jobs/{JOB_ID}/model.glb").status_code == 200
    assert client.get("/jobs/zzz").status_code == 404


def test_language_switch(client):
    door = DEMO_GLOBAL_IDS["door_ifc"]
    german = client.get(f"/jobs/{JOB_ID}/element/{door}").text
    assert "eingesetzt in" in german and "Verbindungsbauteil" in german
    assert "Tür (ohne Feuerwiderstand) in einer EI60-Wand; erforderlich mindestens EI30." in german

    switch = client.get(f"/lang/tech?next=/jobs/{JOB_ID}", follow_redirects=False)
    assert switch.status_code == 303 and switch.headers["location"] == f"/jobs/{JOB_ID}"
    technical = client.get(f"/jobs/{JOB_ID}/element/{door}").text
    assert "hosted_by" in technical and "ConnectionPhysical" in technical
    assert "Door rated none in a EI60 wall; required at least EI30." in technical
    assert client.get("/lang/tech?next=//evil.example", follow_redirects=False).headers["location"] == "/"
