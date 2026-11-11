"""Converter node and value helpers shared by the pipeline stages."""

from __future__ import annotations

import json
import re
from dataclasses import dataclass, field
from typing import Any

import ifcopenshell
from rdflib import URIRef

from pragmatic_bim.ifc2rdf.mapping import EntityMapping

IRI_PATTERN = re.compile(r"^[A-Za-z][A-Za-z0-9+.\-]*:[^\s<>\"{}|\\^`]+$")


def present(value: Any) -> bool:
    return value is not None and value != "" and value != () and value != []


def serialize_value(value: Any) -> str | None:
    """IFC attribute or property value as ``MetadataEntry.metadata_value`` text."""
    if value is None:
        return None
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, str):
        return value or None
    if isinstance(value, (int, float)):
        return str(value)
    if isinstance(value, ifcopenshell.entity_instance):
        if value.id() == 0 and hasattr(value, "wrappedValue"):
            return serialize_value(value.wrappedValue)
        global_id = getattr(value, "GlobalId", None) if value.is_a("IfcRoot") else None
        return global_id
    if isinstance(value, dict):
        items = {k: serialize_value(v) for k, v in sorted(value.items()) if k != "id"}
        return json.dumps(items, ensure_ascii=False, sort_keys=True)
    if isinstance(value, (list, tuple)):
        items = [serialize_value(v) for v in value]
        if any(item is None for item in items):
            return None
        return json.dumps(items, ensure_ascii=False)
    return str(value)


@dataclass
class Node:
    entity: ifcopenshell.entity_instance
    mapping: EntityMapping
    iri: URIRef
    types: tuple[URIRef, ...]
    values: dict[str, list[Any]] = field(default_factory=dict)
    inlined: dict[str, list[tuple[str, dict[str, Any]]]] = field(default_factory=dict)
    reference_elements: tuple[Any, ...] = ()
    """pragmaticBIM Reference element definitions the entity matches (best match first)."""

    @property
    def global_id(self) -> str:
        return self.entity.GlobalId

    @property
    def contract_class(self) -> str:
        return self.mapping.contract_class
