"""Acceptance checks on public Revit, ArchiCAD and Vectorworks exports."""

from __future__ import annotations

import hashlib
import os
import subprocess
import sys

import ifcopenshell
from checks import (
    BOT_ADJACENCY,
    BOT_WALLS,
    CONTRACT_ADJACENCY,
    CONTRACT_WALLS,
    PBS,
    global_ids_of,
    metadata,
    performance_properties,
    rows,
    shacl_violations,
)
from rdflib import RDF

from pragmatic_bim.ifc2rdf.mapping import Mapping
from pragmatic_bim.ifc2rdf.resources import default_mapping_path

# IFC classes whose instances map one-to-one onto a contract class.
IFC_ORIGINS = {
    "Space": ["IfcSpace"],
    "LevelContext": ["IfcBuildingStorey"],
    "BuildingContext": ["IfcBuilding"],
    "SeparatorWall": ["IfcWall"],
    "SeparatorSlab": ["IfcSlab"],
}


def test_conforms_to_contract_shacl(sample, shacl_graph):
    _, _, graph, _ = sample
    assert shacl_violations(graph, shacl_graph) == []


def test_source_system_detected(sample):
    expected, _, _, report = sample
    assert report.source_system == expected.source_system


def test_element_counts_match_ifc(sample):
    expected, path, graph, report = sample
    model = ifcopenshell.open(str(path))
    for contract_class, ifc_classes in IFC_ORIGINS.items():
        ifc_ids = {e.GlobalId for ifc_class in ifc_classes for e in model.by_type(ifc_class)}
        assert global_ids_of(graph, contract_class) == ifc_ids, contract_class
    openings = {e.GlobalId for ifc_class in ("IfcDoor", "IfcWindow") for e in model.by_type(ifc_class)}
    assert openings <= global_ids_of(graph, "ConnectionPhysical")

    counts = {cls: len(set(graph.subjects(RDF.type, PBS[cls]))) for cls in expected.counts}
    assert counts == expected.counts
    assert {cls: report.nodes_by_class[cls] for cls in expected.counts} == expected.counts


def test_every_mapped_ifc_entity_is_one_node_with_global_id(sample):
    _, path, graph, report = sample
    model = ifcopenshell.open(str(path))
    mapping = Mapping.load(default_mapping_path())
    mapped = {
        e.GlobalId
        for e in model.by_type("IfcRoot")
        if mapping.entity_key(e) is not None and mapping.resolve(e) is not None
    }
    entities = set(graph.subjects(RDF.type, PBS.Entity))
    assert len(entities) == len(mapped) == sum(report.nodes_by_class.values())
    for node in entities:
        values = list(graph.objects(node, PBS.ifc_global_id))
        assert len(values) == 1, node
        assert str(node).endswith(str(values[0]))
    assert {str(v) for v in graph.objects(None, PBS.ifc_global_id)} == mapped


def test_performance_properties_keep_raw_value_in_metadata(sample):
    expected, _, graph, report = sample
    counts = {}
    for node in set(graph.subjects(PBS.performance_properties, None)):
        entries = metadata(graph, node)
        for key, record in performance_properties(graph, node).items():
            counts[key] = counts.get(key, 0) + 1
            assert record["mapping_version"] == report.mapping_version
            source = f"{record['source_pset']}.{record['source_property']}"
            assert entries[source] == record["source_value_raw"], (node, key)
    assert counts == expected.performance


def test_bot_query_returns_contract_walls(sample):
    _, _, graph, _ = sample
    assert rows(graph, BOT_WALLS) == rows(graph, CONTRACT_WALLS)


def test_bot_adjacency_matches_contract_relations(sample):
    _, path, graph, _ = sample
    adjacency = rows(graph, BOT_ADJACENCY)
    assert adjacency == rows(graph, CONTRACT_ADJACENCY)
    if ifcopenshell.open(str(path)).by_type("IfcRelSpaceBoundary"):
        assert adjacency


def test_output_is_deterministic(sample, tmp_path):
    _, path, _, _ = sample
    digests = set()
    for seed in ("1", "2"):
        out = tmp_path / f"run-{seed}.ttl"
        subprocess.run(
            [sys.executable, "-m", "pragmatic_bim.ifc2rdf", str(path), "-o", str(out), "-q"],
            check=True,
            env={**os.environ, "PYTHONHASHSEED": seed},
        )
        digests.add(hashlib.sha256(out.read_bytes()).hexdigest())
    assert len(digests) == 1
