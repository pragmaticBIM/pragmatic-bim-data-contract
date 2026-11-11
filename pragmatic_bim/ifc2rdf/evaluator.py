"""Read mapping field sources (``source: ...``) for one IFC instance."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Iterable

import ifcopenshell
import ifcopenshell.util.element

from pragmatic_bim.ifc2rdf.mapping import EntityMapping
from pragmatic_bim.ifc2rdf.model import present

if TYPE_CHECKING:
    from pragmatic_bim.ifc2rdf.pipeline import Converter


class Evaluator:
    """Evaluate mapping field sources for one IFC instance."""

    def __init__(self, converter: "Converter", entity: ifcopenshell.entity_instance, em: EntityMapping):
        self.conv = converter
        self.entity = entity
        self.em = em
        self._psets: dict[str, dict[str, Any]] | None = None
        self.trace: list[tuple[str, str]] = []

    @property
    def psets(self) -> dict[str, dict[str, Any]]:
        if self._psets is None:
            self._psets = ifcopenshell.util.element.get_psets(self.entity, psets_only=True)
        return self._psets

    def attr(self, path: str, target: ifcopenshell.entity_instance | None = None) -> Any:
        value: Any = self.entity if target is None else target
        for part in path.split("."):
            if not isinstance(value, ifcopenshell.entity_instance):
                return None
            value = getattr(value, part, None)
        if isinstance(value, ifcopenshell.entity_instance) and value.id() == 0:
            value = getattr(value, "wrappedValue", value)
        return value

    def evaluate(self, spec: Any, slot: str | None = None, target=None) -> Any:
        if not isinstance(spec, dict):
            return spec
        source = spec.get("source", "constant" if "value" in spec else None)
        handler = getattr(self, f"_src_{source}", None)
        if handler is None:
            self.conv.report.unsupported_sources[str(source)] += 1
            return None
        return handler(spec, slot, target)

    def _src_constant(self, spec, slot, target):
        return spec.get("value")

    def _src_ifc_attribute(self, spec, slot, target):
        value = self.attr(spec["attribute"], target)
        if spec.get("convert_length_to") == "m" and isinstance(value, (int, float)):
            value = float(value) * self.conv.length_scale
        return value

    def _src_ifc_attribute_fallback(self, spec, slot, target):
        for fallback in spec.get("fallbacks") or []:
            if "constant" in fallback:
                return fallback["constant"]
            value = self.attr(fallback["attribute"], target)
            if present(value):
                return value
        return None

    def pset_candidates(self, spec: dict[str, Any]) -> Iterable[tuple[str, str, Any]]:
        """Present ``(pset, property, value)`` in lookup order: overrides, fallbacks, tool fallbacks."""
        system = self.conv.source_system
        pairs = list((spec.get("source_system_overrides") or {}).get(system) or [])
        pairs += list(spec.get("fallbacks") or [])
        pairs += list((spec.get("source_system_fallbacks") or {}).get(system) or [])
        for pair in pairs:
            value = (self.psets.get(pair["pset"]) or {}).get(pair["property"])
            if present(value):
                yield pair["pset"], pair["property"], value

    def _src_ifc_pset_fallback(self, spec, slot, target):
        for pset, prop, value in self.pset_candidates(spec):
            self.trace.append((pset, prop))
            return value
        return None

    def _src_ifc_attribute_heuristic(self, spec, slot, target):
        value = self.attr(spec["attribute"], target)
        if present(value):
            text = str(value).casefold()
            for rule in spec.get("map") or []:
                if any(str(keyword).casefold() in text for keyword in rule["match"]):
                    return rule["value"]
        return spec.get("default")

    def _src_ifc_relation_heuristic(self, spec, slot, target):
        entity = self.entity if target is None else target
        for rule in spec.get("rules") or []:
            if "when_name_match" in rule:
                name = str(getattr(entity, "Name", None) or "").casefold()
                if any(str(k).casefold() in name for k in rule["when_name_match"]):
                    return rule["value"]
            if "when_assigned_to_system_predefined_type" in rule:
                wanted = set(rule["when_assigned_to_system_predefined_type"])
                if any(getattr(s, "PredefinedType", None) in wanted for s in self.conv.systems_of(entity)):
                    return rule["value"]
            if "when_assigned_to_system_discipline" in rule:
                wanted = rule["when_assigned_to_system_discipline"]
                if any(self.conv.system_discipline(s) == wanted for s in self.conv.systems_of(entity)):
                    return rule["value"]
        return spec.get("default")

    def _src_predefined_type_map(self, spec, slot, target):
        return self.em.predefined.get(spec["attribute"])

    def _src_ifc_relation(self, spec, slot, target):
        wanted = (spec.get("resolve") or {}).get("walk_up_to_class")
        current = self.entity if target is None else target
        seen: set[int] = set()
        while current is not None and current.id() not in seen:
            seen.add(current.id())
            current = spatial_parent(current)
            if current is not None and current.is_a(wanted):
                return current
        return None

    def _src_vocabulary_lookup(self, spec, slot, target):
        enum_name = self.conv.schema.slot_range(self.em.contract_class, slot)
        vocab = self.conv.vocab
        for table in spec.get("tables") or []:
            mark = len(self.trace)
            value = self.evaluate(table["match"], slot, target)
            if present(value):
                if "bridge" in table:
                    candidates = vocab.bridge_lookup(table["bridge"], str(value))
                else:
                    candidates = vocab.label_lookup(
                        table["vocabulary"], str(value), table.get("match_property", "prefLabel")
                    )
                for iri in candidates:
                    enum_value = self.conv.schema.enum_value_for_meaning(enum_name, iri)
                    if enum_value is not None:
                        return enum_value
            del self.trace[mark:]
        return spec.get("default")

    def _src_ifc_classification(self, spec, slot, target):
        entity = self.entity if target is None else target
        entries = []
        for rel in getattr(entity, "HasAssociations", None) or []:
            if not rel.is_a("IfcRelAssociatesClassification"):
                continue
            reference = rel.RelatingClassification
            entry = {
                key: self.evaluate(sub_spec, key, reference)
                for key, sub_spec in (spec.get("map") or {}).items()
            }
            entries.append(entry)
        return entries

    def _src_metadata_merge(self, spec, slot, target):
        return None


def spatial_parent(entity: ifcopenshell.entity_instance) -> ifcopenshell.entity_instance | None:
    for inverse, attribute in (
        ("ContainedInStructure", "RelatingStructure"),
        ("Decomposes", "RelatingObject"),
        ("FillsVoids", "RelatingOpeningElement"),
        ("VoidsElements", "RelatingBuildingElement"),
    ):
        for rel in getattr(entity, inverse, None) or []:
            return getattr(rel, attribute)
    return None


def spec_attributes(spec: Any) -> set[str]:
    """IFC attribute names an entity-level field spec reads (top-level path segment)."""
    names: set[str] = set()
    if isinstance(spec, dict):
        if spec.get("source") == "ifc_classification":
            return names
        if isinstance(spec.get("attribute"), str) and spec.get("source") != "predefined_type_map":
            names.add(spec["attribute"].split(".")[0])
        for value in spec.values():
            names |= spec_attributes(value)
    elif isinstance(spec, list):
        for value in spec:
            names |= spec_attributes(value)
    return names
