"""Serialize converter nodes into an RDF graph."""

from __future__ import annotations

import hashlib
import json
from typing import TYPE_CHECKING

from rdflib import RDF, BNode, Graph, Literal, Namespace, URIRef
from rdflib.namespace import DCAT, DCTERMS, XSD

from pragmatic_bim.ifc2rdf.contract import BOT
from pragmatic_bim.ifc2rdf.model import Node

if TYPE_CHECKING:
    from pragmatic_bim.ifc2rdf.pipeline import Converter

SCHEMA_BASE = "https://schema.pragmaticbim.ch/"


def build_graph(conv: "Converter", nodes: list[Node]) -> Graph:
    schema = conv.schema
    graph = Graph(bind_namespaces="none")
    pbs = Namespace(schema.prefixes.get("pbs", SCHEMA_BASE))
    graph.bind("pbs", pbs)
    graph.bind("bot", Namespace(BOT))
    graph.bind("ifcowl", Namespace(schema.prefixes["ifcowl"]))
    graph.bind("rdf", RDF)
    graph.bind("xsd", XSD)
    graph.bind("dcterms", DCTERMS)
    graph.bind("dcat", DCAT)
    graph.bind("inst", Namespace(conv.base_uri))

    dataset = URIRef(conv.base_uri)
    graph.add((dataset, RDF.type, DCAT.Dataset))
    graph.add((dataset, DCTERMS.conformsTo, URIRef(f"{SCHEMA_BASE}{conv.contract_version}/")))
    graph.add((dataset, pbs.contract_version, Literal(conv.contract_version)))
    graph.add((dataset, pbs.mapping_version, Literal(conv.mapping.version)))
    if conv.source_digest:
        graph.add((dataset, DCTERMS.source, Literal(f"sha256:{conv.source_digest}")))

    for node in nodes:
        cls = node.contract_class
        conv.report.nodes_by_class[cls] += 1
        node.values.setdefault("ifc_global_id", [Literal(node.global_id)])
        for rdf_type in node.types:
            graph.add((node.iri, RDF.type, rdf_type))
        for slot, terms in node.values.items():
            predicate = schema.slot_uri(slot)
            for term in terms:
                graph.add((node.iri, predicate, term))
        digest = hashlib.sha1(node.global_id.encode()).hexdigest()[:12]
        for slot, entries in sorted(node.inlined.items()):
            ordered = sorted(entries, key=lambda e: json.dumps(e[1], sort_keys=True, ensure_ascii=False))
            for index, (class_name, entry) in enumerate(ordered):
                blank = BNode(f"{digest}{slot[:2]}{index:05d}")
                graph.add((node.iri, schema.slot_uri(slot), blank))
                for rdf_type in schema.rdf_types(class_name):
                    graph.add((blank, RDF.type, rdf_type))
                for key, value in sorted(entry.items()):
                    range_name = schema.slot_range(class_name, key)
                    if schema.is_enum(range_name):
                        term = schema.enum_term(range_name, str(value))
                    elif schema.is_class(range_name):
                        term = URIRef(str(value))
                    else:
                        term = schema.literal(range_name, value)
                    graph.add((blank, schema.slot_uri(key), term))
        present = set(node.values) | set(node.inlined)
        for slot in schema.required_slots(cls):
            if slot not in present:
                conv.report.missing_required[f"{cls}.{slot}"] += 1
    return graph


def to_turtle(graph: Graph) -> str:
    return graph.serialize(format="turtle")
