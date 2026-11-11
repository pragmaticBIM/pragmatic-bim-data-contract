"""Project the contract RDF graph onto a property graph keyed by IFC GlobalId.

Entities (subjects with ``pbs:ifc_global_id``) become nodes, object properties between two
entities become edges. Literals, enum IRIs and inlined records (metadata, performance
properties, classifications, ...) stay on the entity as properties for the side panel.
"""

from __future__ import annotations

from collections import defaultdict
from typing import Any

from rdflib import RDF, BNode, Graph, Literal, Namespace, URIRef

from pragmatic_bim.ifc2rdf.contract import ContractSchema
from pragmatic_bim.ifc2rdf.emit import SCHEMA_BASE
from pragmatic_bim.ifc2rdf.resources import default_schema_path

PBS = Namespace(SCHEMA_BASE)
PREFIXES = {
    SCHEMA_BASE: "pbs:",
    "https://w3id.org/bot#": "bot:",
    "https://w3id.org/ifc/IFC4_ADD2#": "ifc:",
    str(RDF): "rdf:",
}


def compact(term: Any) -> str:
    text = str(term)
    for base, prefix in PREFIXES.items():
        if text.startswith(base):
            return prefix + text[len(base):]
    return text


def plain(term: Any) -> Any:
    """JSON value for an RDF term (numbers and booleans stay typed)."""
    if isinstance(term, Literal):
        value = term.toPython()
        return value if isinstance(value, (str, int, float, bool)) else str(term)
    if isinstance(term, URIRef):
        return compact(term)
    return str(term)


def entity_ids(graph: Graph) -> dict[URIRef, str]:
    return {s: str(g) for s, g in graph.subject_objects(PBS.ifc_global_id) if isinstance(s, URIRef)}


def primary_class(graph: Graph, node: URIRef, schema: ContractSchema) -> str:
    """Most specific contract class of ``node`` (longest ``is_a`` chain)."""
    names = [str(t)[len(SCHEMA_BASE):] for t in graph.objects(node, RDF.type) if str(t).startswith(SCHEMA_BASE)]
    known = [n for n in names if schema.is_class(n)]
    if known:
        return max(sorted(known), key=lambda n: len(schema.ancestors(n)))
    return sorted(names)[0] if names else "Entity"


def project(graph: Graph, schema: ContractSchema | None = None) -> tuple[dict, dict]:
    """``(graph_view, elements)``: nodes/edges for the graph viewer and per-GlobalId detail."""
    schema = schema or ContractSchema(default_schema_path())
    ids = entity_ids(graph)
    elements: dict[str, dict[str, Any]] = {}
    for node, guid in ids.items():
        elements[guid] = {
            "guid": guid,
            "iri": str(node),
            "name": str(graph.value(node, PBS.name) or guid),
            "cls": primary_class(graph, node, schema),
            "types": sorted(compact(t) for t in graph.objects(node, RDF.type)),
            "level": None,
            "attributes": [],
            "records": defaultdict(list),
            "links": [],
        }

    edges: dict[tuple[str, str], list[str]] = defaultdict(list)
    for node, guid in ids.items():
        element = elements[guid]
        for predicate, obj in sorted(graph.predicate_objects(node), key=lambda po: (str(po[0]), str(po[1]))):
            if predicate == RDF.type:
                continue
            key = compact(predicate)
            if obj in ids:
                target = ids[obj]
                if target != guid:
                    edges[(guid, target)].append(key)
                    element["links"].append({"predicate": key, "guid": target, "direction": "out"})
                    elements[target]["links"].append({"predicate": key, "guid": guid, "direction": "in"})
                if predicate == PBS.parent_level:
                    element["level"] = target
            elif isinstance(obj, BNode):
                record = {compact(p): plain(o) for p, o in graph.predicate_objects(obj) if p != RDF.type}
                element["records"][key].append(record)
            else:
                element["attributes"].append({"key": key, "value": plain(obj)})

    for element in elements.values():
        element["records"] = {slot: sorted(rows, key=_record_order) for slot, rows in sorted(element["records"].items())}
        element["links"].sort(key=lambda link: (link["direction"], link["predicate"], elements[link["guid"]]["name"]))

    nodes = [
        {"id": e["guid"], "label": e["name"], "cls": e["cls"], "level": e["level"]}
        for e in sorted(elements.values(), key=lambda e: e["guid"])
    ]
    view = {
        "nodes": nodes,
        "edges": [{"s": s, "t": t, "p": sorted(set(p))} for (s, t), p in sorted(edges.items())],
    }
    return view, elements


def _record_order(record: dict[str, Any]) -> str:
    return str(record.get("pbs:metadata_key") or record.get("pbs:property_key") or sorted(record.items()))
