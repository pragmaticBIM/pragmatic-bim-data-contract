"""Contract facts for VKF 17-15 (Reference #128): escape-route role, safety lighting, escape sign."""

from __future__ import annotations

import rdflib
from checks import PBS, REFERENCE_FIXTURE, performance_properties, shacl_violations
from synthetic import VKF_17_GLOBAL_IDS as GID
from synthetic import build_vkf_17_15_model

from pragmatic_bim.ifc2rdf import convert

BASE = "https://data.example.org/vkf17/"
IFC = rdflib.Namespace("https://w3id.org/ifc/IFC4_ADD2#")


def iri(role: str) -> rdflib.URIRef:
    return rdflib.URIRef(BASE + GID[role])


def test_vkf_17_15_facts(tmp_path, shacl_graph):
    path = tmp_path / "vkf17.ifc"
    build_vkf_17_15_model(path)
    graph, report = convert(path, base_uri=BASE, reference=REFERENCE_FIXTURE)

    assert shacl_violations(graph, shacl_graph) == []

    assert set(graph.objects(iri("corridor"), PBS.escape_route_role)) == {
        PBS.escape_route_role_horizontal
    }

    light_props = performance_properties(graph, iri("light"))
    assert light_props["fire_property_safety_rated_duration"]["property_value_number"] == 30.0
    assert light_props["fire_property_safety_start_up_time"]["property_value_number"] == 15.0
    assert light_props["fire_property_safety_supply_type"]["property_value_string"] == "SINGLE_BATTERY"
    assert light_props["fire_property_safety_floor_illuminance"]["property_value_number"] == 1.0
    assert light_props["fire_property_safety_not_switchable"]["property_value_boolean"] is True
    assert light_props["fire_property_safety_rated_duration"]["types"] == {
        PBS.FireProperty,
        PBS.PerformanceProperty,
    }
    assert (iri("light"), rdflib.RDF.type, PBS.Equipment) in graph
    assert set(graph.objects(iri("light"), PBS.equipment_type)) == {IFC.IfcElectricalElement}

    sign_props = performance_properties(graph, iri("escape_sign"))
    assert sign_props["fire_property_escape_sign_lighting_type"]["property_value_string"] == "BACKLIT"
    assert sign_props["fire_property_escape_sign_supply_type"]["property_value_string"] == "CENTRAL_BATTERY"
    assert sign_props["fire_property_escape_sign_mounting_height"]["property_value_number"] == 2.1
    assert (iri("escape_sign"), rdflib.RDF.type, PBS.Equipment) in graph
    assert set(graph.objects(iri("escape_sign"), PBS.equipment_type)) == {
        IFC.IfcFireSuppressionTerminal
    }
    assert set(graph.objects(iri("escape_sign"), PBS.content_kind)) == {
        rdflib.Literal("physical")
    }
    assert report.mapping_version
