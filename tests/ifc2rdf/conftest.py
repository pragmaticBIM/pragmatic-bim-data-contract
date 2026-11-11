from __future__ import annotations

import os
import sys
from pathlib import Path

import pytest

pytest.importorskip("ifcopenshell")
pytest.importorskip("rdflib")
pytest.importorskip("pyshacl")

import rdflib  # noqa: E402

sys.path.insert(0, str(Path(__file__).parent))

from checks import REFERENCE_FIXTURE  # noqa: E402
from samples import SAMPLES, Sample, fetch  # noqa: E402
from synthetic import build_demo_model, build_model  # noqa: E402

from pragmatic_bim.ifc2rdf import convert  # noqa: E402

REPO_ROOT = Path(__file__).resolve().parents[2]
SHACL_PATH = REPO_ROOT / "site" / "schema" / "pragmatic-bim.shacl.ttl"


@pytest.fixture(scope="session")
def shacl_graph() -> rdflib.Graph:
    return rdflib.Graph().parse(SHACL_PATH)


@pytest.fixture(scope="session")
def synthetic_ifc(tmp_path_factory) -> Path:
    path = tmp_path_factory.mktemp("synthetic") / "synthetic.ifc"
    build_model(path)
    return path


@pytest.fixture(scope="session")
def synthetic(synthetic_ifc):
    graph, report = convert(
        synthetic_ifc, base_uri="https://data.example.org/model/", reference=REFERENCE_FIXTURE
    )
    return graph, report


@pytest.fixture(scope="session")
def demo_ifc(tmp_path_factory) -> Path:
    path = tmp_path_factory.mktemp("demo") / "demo.ifc"
    build_demo_model(path)
    return path


@pytest.fixture(scope="session")
def demo(demo_ifc):
    """``(graph, report, glb_path)`` for the geometry demo model."""
    glb = demo_ifc.with_suffix(".glb")
    graph, report = convert(
        demo_ifc, base_uri="https://data.example.org/demo/", reference=REFERENCE_FIXTURE, geometry_out=glb
    )
    return graph, report, glb


def _sample_path(sample: Sample) -> Path:
    try:
        return fetch(sample)
    except Exception as exc:  # network or checksum failure
        if os.environ.get("PBS_REQUIRE_IFC_SAMPLES") == "1":
            raise
        pytest.skip(f"IFC sample {sample.id} unavailable: {exc}")


_converted: dict[str, tuple] = {}


@pytest.fixture(scope="session", params=SAMPLES, ids=[s.id for s in SAMPLES])
def sample(request):
    """``(sample, ifc_path, graph, report)`` for each pinned public IFC export."""
    sample: Sample = request.param
    path = _sample_path(sample)
    if sample.id not in _converted:
        _converted[sample.id] = convert(path, reference=REFERENCE_FIXTURE)
    graph, report = _converted[sample.id]
    return sample, path, graph, report
