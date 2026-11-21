"""Contract facts for VKF 16-15 SHACL (issue #13): occupancy, widths, door swing, fire zone."""

from __future__ import annotations

import pytest
import rdflib
from checks import PBS, REFERENCE_FIXTURE, performance_properties, shacl_violations
from synthetic import VKF_GLOBAL_IDS as GID
from synthetic import build_vkf_model

from pragmatic_bim.ifc2rdf import convert

BASE = "https://data.example.org/vkf/"


@pytest.fixture(scope="module")
def vkf(tmp_path_factory):
    path = tmp_path_factory.mktemp("vkf") / "vkf.ifc"
    build_vkf_model(path)
    graph, report = convert(path, base_uri=BASE, reference=REFERENCE_FIXTURE)
    return graph, report


def iri(role: str) -> rdflib.URIRef:
    return rdflib.URIRef(BASE + GID[role])


def quantity(graph: rdflib.Graph, role: str, quantity_type: str) -> float:
    wanted = str(PBS[f"quantity_type_{quantity_type}"])
    for record in graph.objects(iri(role), PBS.quantity_values):
        if str(graph.value(record, PBS.quantity_type)) == wanted:
            return graph.value(record, PBS.quantity_value).toPython()
    raise AssertionError(f"no {quantity_type} on {role}")


def test_vkf_conforms_to_contract_shacl(vkf, shacl_graph):
    graph, _ = vkf
    assert shacl_violations(graph, shacl_graph) == []


def test_peak_occupancy_on_space(vkf):
    graph, report = vkf
    props = performance_properties(graph, iri("room"))
    peak = props["indoor_environment_peak_occupancy"]
    assert peak["types"] == {PBS.IndoorEnvironmentProperty, PBS.PerformanceProperty}
    assert peak["property_value_number"] == 40.0
    assert peak["source_pset"] == "ePset_Space"
    assert peak["source_property"] == "PeakOccupancyActual"
    assert peak["mapping_version"] == report.mapping_version


def test_stair_clear_width_and_winder_inner_tread(vkf):
    graph, _ = vkf
    # Model units are millimetres; values are converted to metres.
    assert quantity(graph, "stair_flight", "clear_width") == pytest.approx(1.25)
    assert quantity(graph, "stair_flight", "tread_length_at_inner_side") == pytest.approx(0.15)
    assert (iri("stair_flight"), rdflib.RDF.type, PBS.PhysicalElement) in graph


def test_escape_route_clear_width_on_space(vkf):
    graph, _ = vkf
    assert quantity(graph, "room", "escape_route_clear_width") == pytest.approx(1.2)
    assert quantity(graph, "corridor", "escape_route_clear_width") == pytest.approx(1.5)


def test_door_opens_in_escape_direction(vkf):
    graph, _ = vkf
    assert set(graph.objects(iri("door_out"), PBS.opens_in_escape_direction)) == {rdflib.Literal(True)}
    assert set(graph.objects(iri("door_in"), PBS.opens_in_escape_direction)) == {rdflib.Literal(False)}
    assert set(graph.objects(iri("exit_door"), PBS.opens_in_escape_direction)) == {rdflib.Literal(True)}


def test_fire_compartment_via_parent_zone(vkf):
    graph, _ = vkf
    zone = iri("fire_zone")
    assert (zone, rdflib.RDF.type, PBS.ZoneContext) in graph
    # ZoneType.fire shares the IFC SpatialZone meaning IRI with other spatial zone kinds.
    assert set(graph.objects(zone, PBS.zone_type)) == {
        rdflib.URIRef("https://w3id.org/ifc/IFC4_ADD2#IfcSpatialZone")
    }
    assert set(graph.objects(iri("room"), PBS.parent_zone)) == {zone}
    assert set(graph.objects(iri("corridor"), PBS.parent_zone)) == {zone}
