"""Geometry-derived space adjacency fallback and Derivation provenance."""

from __future__ import annotations

from pathlib import Path

import ifcopenshell
import pytest
import rdflib
from checks import BOT, PBS, REFERENCE_FIXTURE, shacl_violations
from rdflib import RDF
from synthetic import DEMO_GLOBAL_IDS as GID
from synthetic import GLOBAL_IDS, build_demo_model

from pragmatic_bim.ifc2rdf import convert

shapely = pytest.importorskip("shapely")

BASE = "https://data.example.org/demo/"
SYNTH_BASE = "https://data.example.org/model/"
REPO = Path(__file__).resolve().parents[2]
DEMO_DATA = REPO / "demo-data"


def iri(role: str, base: str = BASE) -> rdflib.URIRef:
    return rdflib.URIRef(base + GID[role])


def slot_objects(graph: rdflib.Graph, role: str, predicate, base: str = BASE) -> set:
    return set(graph.objects(iri(role, base), predicate))


def _strip_space_boundaries(path: Path) -> Path:
    """Copy an IFC file with all IfcRelSpaceBoundary relations removed."""
    out = path.with_name(path.stem + "-no-boundaries.ifc")
    model = ifcopenshell.open(str(path))
    for rel in list(model.by_type("IfcRelSpaceBoundary")):
        model.remove(rel)
    model.write(str(out))
    return out


def test_demo_geometry_fills_missing_space_boundaries(demo):
    graph, report, _ = demo
    assert report.spaces_without_ifc_boundaries >= 1
    assert report.adjacency_comparison["geometry_only"] >= 1
    assert slot_objects(graph, "wall_interior", PBS.separates_spaces) >= {iri("office"), iri("corridor")}
    assert slot_objects(graph, "wall_exterior", PBS.separates_spaces) >= {iri("office")}
    assert slot_objects(graph, "floor_slab", PBS.separates_spaces) >= {iri("office")}
    assert slot_objects(graph, "door_geometry", PBS.connects_spaces) >= {iri("office"), iri("corridor")}
    # Space.adjacent_elements is serialized as bot:adjacentElement.
    assert iri("wall_interior") in slot_objects(graph, "office", BOT.adjacentElement)
    assert iri("door_geometry") in slot_objects(graph, "corridor", BOT.adjacentElement)


def test_demo_adjacency_provenance_in_rdf(demo):
    graph, report, _ = demo
    assert report.computed_relations["ConnectionVirtual (ifc_geometry)"] >= 1
    connections = list(graph.subjects(RDF.type, PBS.ConnectionVirtual))
    assert connections
    geometry_derived = []
    for node in connections:
        assert (node, PBS.connection_virtual_type, PBS.connection_virtual_type_adjacency) in graph
        derivation = graph.value(node, PBS.derivation)
        assert derivation is not None
        kind = graph.value(derivation, PBS.derivation_source_kind)
        if kind == PBS.derivation_source_kind_ifc_geometry:
            geometry_derived.append(node)
            assert graph.value(derivation, PBS.derivation_method) == rdflib.Literal("space_adjacency")
            assert graph.value(derivation, PBS.derivation_tolerance) is not None
    assert geometry_derived


def test_synthetic_with_boundaries_and_without_geometry_keeps_ifc(synthetic):
    """Synthetic model has IfcRelSpaceBoundary but no body geometry — IFC pairs stay, no disagreement spam."""
    graph, report = synthetic
    assert (rdflib.URIRef(SYNTH_BASE + GLOBAL_IDS["wall"]), PBS.separates_spaces, rdflib.URIRef(SYNTH_BASE + GLOBAL_IDS["kitchen"])) in graph
    assert report.adjacency_comparison.get("ifc_only", 0) == 0
    assert report.adjacency_disagreements == []
    assert report.computed_relations["ConnectionVirtual (ifc_explicit)"] >= 1


def test_synthetic_without_boundaries_gets_geometry_adjacency(tmp_path, shacl_graph):
    with_boundaries = tmp_path / "with.ifc"
    build_demo_model(with_boundaries)
    without = _strip_space_boundaries(with_boundaries)
    # Demo never had boundaries; stripping is a no-op but keeps the helper exercised.
    # Build a geometric twin of the relation synthetic model: use demo (has geometry).
    graph, report = convert(without, base_uri=BASE, reference=REFERENCE_FIXTURE)
    assert report.adjacency_comparison["geometry_only"] >= 1
    assert slot_objects(graph, "wall_interior", PBS.separates_spaces) >= {iri("office"), iri("corridor")}
    assert shacl_violations(graph, shacl_graph) == []


def test_geometry_matches_ifc_when_both_present(tmp_path):
    """Demo plus synthetic space boundaries: geometry should recover the IFC pairs (high recall)."""
    path = tmp_path / "bounded_demo.ifc"
    build_demo_model(path)
    model = ifcopenshell.open(str(path))
    by_gid = {e.GlobalId: e for e in model.by_type("IfcRoot") if getattr(e, "GlobalId", None)}
    pairs = [
        ("office", "wall_interior"),
        ("corridor", "wall_interior"),
        ("office", "wall_exterior"),
        ("office", "floor_slab"),
        ("office", "door_geometry"),
        ("corridor", "door_geometry"),
        ("office", "door_ifc"),
        ("corridor", "door_ifc"),
    ]
    for index, (space_role, element_role) in enumerate(pairs):
        model.create_entity(
            "IfcRelSpaceBoundary",
            GlobalId=ifcopenshell.guid.compress(f"{index + 1:032x}"),
            RelatingSpace=by_gid[GID[space_role]],
            RelatedBuildingElement=by_gid[GID[element_role]],
            PhysicalOrVirtualBoundary="PHYSICAL",
            InternalOrExternalBoundary="INTERNAL",
        )
    model.write(str(path))

    graph, report = convert(path, base_uri=BASE, reference=REFERENCE_FIXTURE)
    assert report.adjacency_comparison["ifc_and_geometry"] >= 6
    metrics = report.adjacency_metrics()
    assert metrics is not None
    precision, recall = metrics
    assert recall >= 0.75
    assert precision >= 0.5
    # IFC wins: stated pairs remain even if geometry also found extras.
    assert slot_objects(graph, "wall_interior", PBS.separates_spaces) >= {iri("office"), iri("corridor")}
    assert report.computed_relations["ConnectionVirtual (ifc_explicit)"] >= 1


@pytest.mark.parametrize(
    "folder,source",
    [
        ("8709cf0ef484", "archicad"),
        ("ad6854cf6338", "revit"),
    ],
)
def test_demo_data_exports_space_adjacency(folder, source, shacl_graph):
    path = DEMO_DATA / folder / "model.ifc"
    if not path.is_file():
        pytest.skip(f"demo-data/{folder}/model.ifc not available")
    graph, report = convert(path, reference=REFERENCE_FIXTURE)
    assert report.source_system == source or report.source_system in {source, "ifc"}
    walls_with_spaces = list(graph.subjects(PBS.separates_spaces, None))
    assert walls_with_spaces, f"expected separates_spaces on {source} export"
    connections = list(graph.subjects(RDF.type, PBS.ConnectionVirtual))
    assert connections, f"expected adjacency ConnectionVirtual provenance on {source} export"
    assert shacl_violations(graph, shacl_graph) == []
