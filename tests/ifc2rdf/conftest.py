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

from samples import SAMPLES, Sample, fetch  # noqa: E402
from synthetic import build_model  # noqa: E402

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
    graph, report = convert(synthetic_ifc, base_uri="https://data.example.org/model/")
    return graph, report


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
        _converted[sample.id] = convert(path)
    graph, report = _converted[sample.id]
    return sample, path, graph, report
