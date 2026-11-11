"""One conversion job: IFC to contract graph, GLB, graph projection and check results.

Runs inside the worker process; every stage writes its output next to ``model.ifc``.
"""

from __future__ import annotations

import time
import traceback
from dataclasses import asdict
from pathlib import Path
from typing import Any

from pragmatic_bim.ifc2rdf import ConversionReport, convert, to_turtle

from demo.app import checks, graphview
from demo.app.jobs import write_json, write_status


def run_job(directory: Path, *, reference: Path | bool | None = None) -> None:
    """``reference`` is passed to ``convert`` (None: ``$PBS_REFERENCE_PATH`` or the sibling checkout)."""
    directory = Path(directory)
    started = time.monotonic()
    try:
        write_status(directory, "converting")
        graph, report = convert(directory / "model.ifc", reference=reference, geometry_out=directory / "model.glb")
        (directory / "model.ttl").write_text(to_turtle(graph), encoding="utf-8")
        write_json(directory / "report.json", report_dict(report))

        write_status(directory, "projecting")
        view, elements = graphview.project(graph)
        write_json(directory / "graph.json", view)
        write_json(directory / "elements.json", elements)

        write_status(directory, "checking")
        results = checks.run_checks(graph, report)
        write_json(directory / "checks.json", [r.to_dict() for r in results])

        write_status(
            directory,
            "done",
            seconds=round(time.monotonic() - started, 1),
            nodes=len(view["nodes"]),
            edges=len(view["edges"]),
            has_geometry=(directory / "model.glb").is_file(),
        )
    except Exception:
        write_status(directory, "failed", error=traceback.format_exc())


def report_dict(report: ConversionReport) -> dict[str, Any]:
    out: dict[str, Any] = {}
    for key, value in asdict(report).items():
        out[key] = {str(k): v for k, v in value.items()} if isinstance(value, dict) else value
    out["lines"] = report.lines()
    return out
