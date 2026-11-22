"""SpatialContext.add_measurement emits deterministic DerivedMeasurement entities."""

from __future__ import annotations

import ifcopenshell
import rdflib
from checks import PBS
from rdflib import RDF
from synthetic import GLOBAL_IDS

from pragmatic_bim.ifc2rdf.emit import build_graph
from pragmatic_bim.ifc2rdf.geometry import GeometryResult
from pragmatic_bim.ifc2rdf.mapping import Mapping
from pragmatic_bim.ifc2rdf.pipeline import Converter
from pragmatic_bim.ifc2rdf.contract import ContractSchema
from pragmatic_bim.ifc2rdf.resources import classification_dir, default_mapping_path, default_schema_path
from pragmatic_bim.ifc2rdf.spatial.context import SpatialContext
from pragmatic_bim.ifc2rdf.vocab import Vocabularies

BASE = "https://data.example.org/model/"


def _converter(ifc_path) -> Converter:
    return Converter(
        ifcopenshell.open(str(ifc_path)),
        mapping=Mapping.load(default_mapping_path()),
        schema=ContractSchema(default_schema_path()),
        vocab=Vocabularies(classification_dir()),
        base_uri=BASE,
        source_system="test",
        source_name=str(ifc_path.name),
    )


def _subjects(conv: Converter) -> tuple:
    wall = next(n for n in conv.sorted_nodes() if n.global_id == GLOBAL_IDS["wall"])
    slab = next(n for n in conv.sorted_nodes() if n.global_id == GLOBAL_IDS["slab"])
    return wall, slab


def test_add_measurement_twice_yields_one_entity(synthetic_ifc):
    conv = _converter(synthetic_ifc)
    conv.build_nodes()
    ctx = SpatialContext(conv, GeometryResult())
    wall, slab = _subjects(conv)
    first = ctx.add_measurement(
        [wall, slab],
        [("clear_width", 1.2, "m")],
        method="perpendicular_clear_width",
        method_version="0.1",
        tolerance=0.005,
        line_wkt="LINESTRING Z (0 0 0, 1.2 0 0)",
    )
    second = ctx.add_measurement(
        [slab, wall],
        [("clear_width", 9.9, "m")],
        method="perpendicular_clear_width",
        method_version="0.1",
    )
    assert first is not None and first is second
    assert len(conv.extra_nodes) == 1
    assert conv.report.computed_measurements["perpendicular_clear_width"] == 1

    graph = build_graph(conv, conv.all_nodes())
    measurements = list(graph.subjects(RDF.type, PBS.DerivedMeasurement))
    assert len(measurements) == 1
    subject = measurements[0]
    assert (subject, PBS.content_kind, rdflib.Literal("measurement")) in graph
    assert (subject, PBS.measurement_status, PBS.measurement_status_measured) in graph
    assert set(graph.objects(subject, PBS.applies_to_entities)) == {
        rdflib.URIRef(BASE + GLOBAL_IDS["wall"]),
        rdflib.URIRef(BASE + GLOBAL_IDS["slab"]),
    }
    quantities = list(graph.objects(subject, PBS.quantity_values))
    assert len(quantities) == 1
    assert graph.value(quantities[0], PBS.quantity_value).toPython() == 1.2
    derivation = graph.value(quantities[0], PBS.derivation)
    assert graph.value(derivation, PBS.derivation_method) == rdflib.Literal("perpendicular_clear_width")
    assert graph.value(derivation, PBS.derivation_source_kind) == PBS.derivation_source_kind_ifc_geometry
    geom = next(graph.objects(subject, PBS.geometry_representations))
    assert str(graph.value(geom, PBS.geometry_wkt)).startswith("LINESTRING Z")


def test_not_measurable_without_quantity(synthetic_ifc):
    conv = _converter(synthetic_ifc)
    conv.build_nodes()
    ctx = SpatialContext(conv, GeometryResult())
    wall, slab = _subjects(conv)
    node = ctx.add_measurement(
        [wall, slab],
        quantities=(),
        method="perpendicular_clear_width",
        method_version="0.1",
        status="not_measurable",
    )
    assert node is not None
    graph = build_graph(conv, conv.all_nodes())
    subject = next(graph.subjects(RDF.type, PBS.DerivedMeasurement))
    assert (subject, PBS.measurement_status, PBS.measurement_status_not_measurable) in graph
    assert list(graph.objects(subject, PBS.quantity_values)) == []
    assert conv.report.computed_measurements["perpendicular_clear_width"] == 1
