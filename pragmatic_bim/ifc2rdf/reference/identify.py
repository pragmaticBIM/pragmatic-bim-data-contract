"""Match IFC objects to pragmaticBIM Reference element definitions."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

import ifcopenshell
import ifcopenshell.util.element

from pragmatic_bim.ifc2rdf.mapping import predefined_type
from pragmatic_bim.ifc2rdf.reference.applicability import (
    ENTITY_ATTRIBUTES,
    Clause,
    clause_applies_to_schema,
    evaluate,
)
from pragmatic_bim.ifc2rdf.reference.catalog import ElementDefinition, ReferenceCatalog

CLASSIFICATION_SCHEME = "pragmaticbim-element"
CLASSIFICATION_SOURCE = "pragmaticBIM-reference"

_MISSING = object()


@dataclass(frozen=True)
class ElementMatch:
    element: ElementDefinition
    score: int
    """Clauses satisfied by the matching branch; higher means more specific."""


def best_matches(matches: list[ElementMatch]) -> list[ElementMatch]:
    """Matches sharing the highest score (more than one means the match is ambiguous)."""
    if not matches:
        return []
    top = matches[0].score
    return [m for m in matches if m.score == top]


def identify(ifc_file: ifcopenshell.file, catalog: ReferenceCatalog) -> dict[int, list[ElementMatch]]:
    """Element matches per IFC instance id, best (most specific) first."""
    schema = ifc_file.schema_identifier if hasattr(ifc_file, "schema_identifier") else ifc_file.schema
    result: dict[int, list[ElementMatch]] = {}
    objects = [o for o in ifc_file.by_type("IfcObjectDefinition") if not o.is_a("IfcTypeObject")]
    for product in sorted(objects, key=lambda o: o.GlobalId):
        candidates = [d for d in catalog.elements if any(_is_a(product, c) for c in d.entity_classes)]
        if not candidates:
            continue
        values = _Values(product)
        matches = []
        for definition in candidates:
            score = _score(definition, product, values, schema)
            if score is not None:
                matches.append(ElementMatch(definition, score))
        if matches:
            result[product.id()] = sorted(matches, key=lambda m: (-m.score, m.element.id))
    return result


def classification_entry(match: ElementMatch, version: str | None) -> dict[str, Any]:
    element = match.element
    return {
        "classification_scheme": CLASSIFICATION_SCHEME,
        "classification_code": element.code or element.id.rsplit("/", 1)[-1],
        "classification_label": element.label,
        "classification_uri": element.uri,
        "classification_version": version,
        "classification_source": CLASSIFICATION_SOURCE,
    }


def _score(definition: ElementDefinition, product, values: "_Values", schema: str) -> int | None:
    best: int | None = None

    def holds(clause: Clause) -> bool:
        if clause.attribute in ENTITY_ATTRIBUTES:
            if not clause_applies_to_schema(clause.attribute, schema, definition.has_ifc4x3_clause):
                return False
            return _is_a(product, clause.value or "")
        actual = values.get(clause.attribute)
        if clause.value is None:
            return actual is not _MISSING
        return actual is not _MISSING and _eq(actual, clause.value)

    for expression in definition.expressions:
        matched, score = evaluate(expression, holds)
        if matched and (best is None or score > best):
            best = score
    return best


class _Values:
    """Attribute and property lookup for one product (property sets read once)."""

    def __init__(self, product) -> None:
        self.product = product
        self._psets: dict[str, dict[str, Any]] | None = None

    @property
    def psets(self) -> dict[str, dict[str, Any]]:
        if self._psets is None:
            self._psets = ifcopenshell.util.element.get_psets(self.product)
        return self._psets

    def get(self, name: str) -> Any:
        if "." in name:
            pset, prop = name.split(".", 1)
            return _clean((self.psets.get(pset) or {}).get(prop))
        if name == "PredefinedType":
            return _clean(predefined_type(self.product))
        if hasattr(self.product, name):
            try:
                value = _clean(getattr(self.product, name))
            except (AttributeError, RuntimeError):
                value = _MISSING
            if value is not _MISSING:
                return value
        for props in self.psets.values():
            if name in props and _clean(props[name]) is not _MISSING:
                return _clean(props[name])
        return _MISSING


def _clean(value: Any) -> Any:
    if hasattr(value, "wrappedValue"):
        value = value.wrappedValue
    if value is None or value == "":
        return _MISSING
    return value


def _eq(actual: Any, expected: str) -> bool:
    if expected.upper() in {"TRUE", "FALSE"}:
        return _as_bool(actual) == (expected.upper() == "TRUE")
    return str(actual) == expected


def _as_bool(value: Any) -> bool:
    if isinstance(value, bool):
        return value
    if isinstance(value, (int, float)):
        return bool(value)
    return str(value).strip().upper() in {"TRUE", "1", "YES", "T", ".T."}


def _is_a(product, ifc_class: str) -> bool:
    try:
        return bool(product.is_a(ifc_class))
    except (RuntimeError, ValueError):
        return False
