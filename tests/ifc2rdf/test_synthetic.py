from __future__ import annotations

import subprocess
import sys

import rdflib
from checks import (
    BOT,
    BOT_ADJACENCY,
    CONTRACT_ADJACENCY,
    PBS,
    global_ids_of,
    metadata,
    performance_properties,
    rows,
    shacl_violations,
)
from rdflib import RDF, Literal, URIRef
from synthetic import GLOBAL_IDS

from pragmatic_bim.ifc2rdf import convert, to_turtle

BASE = "https://data.example.org/model/"


def iri(role: str) -> URIRef:
    return URIRef(BASE + GLOBAL_IDS[role])


def test_conforms_to_contract_shacl(synthetic, shacl_graph):
    graph, _ = synthetic
    assert shacl_violations(graph, shacl_graph) == []


def test_instance_uris_use_base_and_global_id(synthetic):
    graph, _ = synthetic
    for role, global_id in GLOBAL_IDS.items():
        assert (iri(role), PBS.ifc_global_id, Literal(global_id)) in graph, role


def test_contract_classes_and_bot_types(synthetic):
    graph, _ = synthetic
    expected = {
        "kitchen": (PBS.Space, BOT.Space),
        "storey": (PBS.LevelContext, BOT.Storey),
        "building": (PBS.BuildingContext, BOT.Building),
        "wall": (PBS.SeparatorWall, BOT.Element),
        "slab": (PBS.SeparatorSlab, BOT.Element),
        "door": (PBS.ConnectionPhysical, BOT.Element),
        "air_terminal": (PBS.Equipment, BOT.Element),
    }
    for role, types in expected.items():
        for rdf_type in types:
            assert (iri(role), RDF.type, rdf_type) in graph, (role, rdf_type)


def test_relations(synthetic):
    graph, _ = synthetic
    expected = [
        ("wall", PBS.separates_spaces, "kitchen"),
        ("wall", PBS.separates_spaces, "living"),
        ("slab", PBS.separates_spaces, "kitchen"),
        ("door", PBS.connects_spaces, "kitchen"),
        ("door", PBS.connects_spaces, "living"),
        ("kitchen", BOT.adjacentElement, "wall"),
        ("kitchen", BOT.adjacentElement, "slab"),
        ("living", BOT.adjacentElement, "door"),
        ("air_terminal", PBS.parent_space, "kitchen"),
        ("kitchen", PBS.parent_level, "storey"),
        ("wall", PBS.parent_level, "storey"),
        ("door", PBS.parent_level, "storey"),
        ("storey", PBS.parent_building, "building"),
    ]
    for subject, predicate, obj in expected:
        assert (iri(subject), predicate, iri(obj)) in graph, (subject, predicate, obj)


def test_bot_adjacency_matches_contract_relations(synthetic):
    graph, _ = synthetic
    assert rows(graph, BOT_ADJACENCY) == rows(graph, CONTRACT_ADJACENCY)


def test_unpromoted_pset_values_stay_in_metadata(synthetic):
    graph, _ = synthetic
    entries = metadata(graph, iri("wall"))
    assert entries["Custom_Data.Note"] == "synthetic"
    assert entries["Pset_WallCommon.IsExternal"] == "false"


def test_fire_rating_promoted_to_fire_property(synthetic):
    graph, report = synthetic
    fire = performance_properties(graph, iri("wall"))["fire_property_resistance_rating"]
    assert fire["types"] == {PBS.FireProperty, PBS.PerformanceProperty}
    assert fire["property_value_type"] == PBS.performance_property_value_type_string
    assert fire["property_value_string"] == "EI90"
    assert fire["source_pset"] == "Pset_WallCommon"
    assert fire["source_property"] == "FireRating"
    assert fire["source_value_raw"] == "EI 90"
    assert fire["mapping_version"] == report.mapping_version
    assert metadata(graph, iri("wall"))["Pset_WallCommon.FireRating"] == "EI 90"


def test_fire_rating_suffix_kept_separately(synthetic):
    graph, _ = synthetic
    props = performance_properties(graph, iri("slab"))
    assert props["fire_property_resistance_rating"]["property_value_string"] == "REI60"
    reaction = props["fire_property_reaction_to_fire"]
    assert reaction["property_value_string"] == "RF1"
    assert reaction["source_value_raw"] == "REI 60-RF1"
    assert metadata(graph, iri("slab"))["Pset_SlabCommon.FireRating"] == "REI 60-RF1"


def test_numeric_and_boolean_performance_properties(synthetic):
    graph, _ = synthetic
    props = performance_properties(graph, iri("wall"))
    acoustic = props["acoustic_property_rating_db"]
    assert acoustic["types"] == {PBS.AcousticProperty, PBS.PerformanceProperty}
    assert (acoustic["property_value_number"], acoustic["property_unit"]) == (52.0, "dB")
    assert acoustic["source_value_raw"] == "Rw 52 dB"
    thermal = props["thermal_property_thermal_transmittance"]
    assert (thermal["property_value_number"], thermal["property_unit"]) == (0.25, "W/m2K")
    assert thermal["property_unit_uri"] == URIRef("http://qudt.org/vocab/unit/W-PER-M2-K")
    assert props["thermal_property_is_external"]["property_value_boolean"] is False
    load_bearing = props["structural_property_load_bearing"]
    assert load_bearing["types"] == {PBS.StructuralProperty, PBS.PerformanceProperty}
    assert load_bearing["property_value_boolean"] is True


def test_rejected_value_falls_through_to_tool_pset(synthetic, synthetic_ifc, shacl_graph):
    graph, report = synthetic
    assert "fire_property_resistance_rating" not in performance_properties(graph, iri("door"))
    assert report.rejected_values["FireProperty.resistance_rating Pset_DoorCommon.FireRating='Fire Rating'"] == 1

    revit, _ = convert(synthetic_ifc, base_uri=BASE, source_system="revit")
    fire = performance_properties(revit, iri("door"))["fire_property_resistance_rating"]
    assert fire["property_value_string"] == "EI30"
    assert (fire["source_pset"], fire["source_value_raw"]) == ("PSet_Revit_Type_Other", "EI 30-C")
    assert metadata(revit, iri("door"))["Pset_DoorCommon.FireRating"] == "Fire Rating"
    assert shacl_violations(revit, shacl_graph) == []


def test_storey_elevation_in_metres(synthetic):
    graph, _ = synthetic
    assert graph.value(iri("storey"), PBS.elevation).toPython() == 3.0
    assert str(graph.value(iri("storey"), PBS.elevation_unit)) == "m"


def test_space_name_vocabulary_lookup(synthetic):
    graph, _ = synthetic
    name_type = graph.value(iri("kitchen"), PBS.space_name_type)
    assert name_type is not None and str(name_type).endswith("RN_RES_KIT")


def test_versions_recorded(synthetic_ifc):
    graph, report = convert(synthetic_ifc, base_uri=BASE, contract_version="v9.9.9")
    dataset = URIRef(BASE)
    assert graph.value(dataset, PBS.contract_version) == Literal("v9.9.9")
    assert graph.value(dataset, PBS.mapping_version) == Literal(report.mapping_version)
    assert report.mapping_version


def test_every_node_has_global_id(synthetic):
    graph, _ = synthetic
    entities = set(graph.subjects(RDF.type, PBS.Entity))
    assert entities
    assert all(graph.value(node, PBS.ifc_global_id) is not None for node in entities)
    assert global_ids_of(graph, "Entity") == set(GLOBAL_IDS.values())


def test_cli_writes_identical_turtle(synthetic_ifc, tmp_path):
    out = tmp_path / "model.ttl"
    result = subprocess.run(
        [sys.executable, "-m", "pragmatic_bim.ifc2rdf", str(synthetic_ifc), "-o", str(out), "--base-uri", BASE],
        capture_output=True,
        text=True,
        check=True,
    )
    assert "mapping_version=" in result.stderr
    graph, _ = convert(synthetic_ifc, base_uri=BASE)
    assert out.read_text(encoding="utf-8") == to_turtle(graph)
    assert len(rdflib.Graph().parse(out)) == len(graph)
