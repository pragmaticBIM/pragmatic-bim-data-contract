"""Convert an IFC model into an RDF graph that follows the Pragmatic BIM data contract.

The converter interprets ``ifc_mapping.merged.yaml`` (entity blocks, field sources,
relationship resolutions) and the LinkML contract (class hierarchy, slots, enums). It
holds no IFC → contract rules of its own beyond how each mapping source type is read.
"""

from __future__ import annotations

import hashlib
import json
import re
from collections import Counter
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Iterable

import ifcopenshell
import ifcopenshell.util.element
import ifcopenshell.util.unit
from rdflib import RDF, BNode, Graph, Literal, Namespace, URIRef
from rdflib.namespace import DCAT, DCTERMS, XSD

from pragmatic_bim.ifc2rdf.contract import BOT, ContractSchema
from pragmatic_bim.ifc2rdf.mapping import EntityMapping, Mapping
from pragmatic_bim.ifc2rdf.resources import (
    classification_dir,
    default_mapping_path,
    default_schema_path,
)
from pragmatic_bim.ifc2rdf.vocab import Vocabularies

DEFAULT_BASE_URI = "urn:pbs:ifc:{project}/"
SCHEMA_BASE = "https://schema.pragmaticbim.ch/"
_IRI_PATTERN = re.compile(r"^[A-Za-z][A-Za-z0-9+.\-]*:[^\s<>\"{}|\\^`]+$")
_COMPARATORS = {
    "gte": lambda a, b: a >= b,
    "gt": lambda a, b: a > b,
    "lte": lambda a, b: a <= b,
    "lt": lambda a, b: a < b,
    "eq": lambda a, b: a == b,
}
# Hierarchical relationships always point from the contained object to its container.
_SUBJECT_IS_CHILD = {"IfcRelContainedInSpatialStructure", "IfcRelAggregates"}


def _present(value: Any) -> bool:
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

    @property
    def global_id(self) -> str:
        return self.entity.GlobalId

    @property
    def contract_class(self) -> str:
        return self.mapping.contract_class


@dataclass
class ConversionReport:
    source_system: str
    contract_version: str
    mapping_version: str
    nodes_by_class: Counter = field(default_factory=Counter)
    excluded_by_ifc_class: Counter = field(default_factory=Counter)
    dropped: Counter = field(default_factory=Counter)
    missing_required: Counter = field(default_factory=Counter)
    unsupported_sources: Counter = field(default_factory=Counter)

    def lines(self) -> list[str]:
        out = [
            f"source_system={self.source_system} contract_version={self.contract_version} "
            f"mapping_version={self.mapping_version}"
        ]
        out += [f"  {cls}: {n}" for cls, n in sorted(self.nodes_by_class.items())]
        for label, counter in (
            ("excluded", self.excluded_by_ifc_class),
            ("missing required", self.missing_required),
            ("dropped", self.dropped),
            ("unsupported mapping source", self.unsupported_sources),
        ):
            out += [f"  {label}: {key} ×{n}" for key, n in sorted(counter.items())]
        return out


class _Evaluator:
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
            if _present(value):
                return value
        return None

    def _src_ifc_pset_fallback(self, spec, slot, target):
        overrides = (spec.get("source_system_overrides") or {}).get(self.conv.source_system) or []
        for pair in list(overrides) + list(spec.get("fallbacks") or []):
            value = (self.psets.get(pair["pset"]) or {}).get(pair["property"])
            if _present(value):
                self.trace.append((pair["pset"], pair["property"]))
                return value
        return None

    def _src_ifc_attribute_heuristic(self, spec, slot, target):
        value = self.attr(spec["attribute"], target)
        if _present(value):
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
            current = _spatial_parent(current)
            if current is not None and current.is_a(wanted):
                return current
        return None

    def _src_vocabulary_lookup(self, spec, slot, target):
        enum_name = self.conv.schema.slot_range(self.em.contract_class, slot)
        vocab = self.conv.vocab
        for table in spec.get("tables") or []:
            mark = len(self.trace)
            value = self.evaluate(table["match"], slot, target)
            if _present(value):
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


def _spatial_parent(entity: ifcopenshell.entity_instance) -> ifcopenshell.entity_instance | None:
    for inverse, attribute in (
        ("ContainedInStructure", "RelatingStructure"),
        ("Decomposes", "RelatingObject"),
        ("FillsVoids", "RelatingOpeningElement"),
        ("VoidsElements", "RelatingBuildingElement"),
    ):
        for rel in getattr(entity, inverse, None) or []:
            return getattr(rel, attribute)
    return None


def _spec_attributes(spec: Any) -> set[str]:
    """IFC attribute names an entity-level field spec reads (top-level path segment)."""
    names: set[str] = set()
    if isinstance(spec, dict):
        if spec.get("source") == "ifc_classification":
            return names
        if isinstance(spec.get("attribute"), str) and spec.get("source") != "predefined_type_map":
            names.add(spec["attribute"].split(".")[0])
        for value in spec.values():
            names |= _spec_attributes(value)
    elif isinstance(spec, list):
        for value in spec:
            names |= _spec_attributes(value)
    return names


class Converter:
    def __init__(
        self,
        ifc_file: ifcopenshell.file,
        *,
        mapping: Mapping,
        schema: ContractSchema,
        vocab: Vocabularies,
        base_uri: str = DEFAULT_BASE_URI,
        contract_version: str | None = None,
        source_system: str | None = None,
        source_digest: str | None = None,
    ) -> None:
        self.file = ifc_file
        self.mapping = mapping
        self.schema = schema
        self.vocab = vocab
        self.contract_version = contract_version or mapping.canonical_type_version
        self.source_system = source_system or detect_source_system(ifc_file, mapping.conventions)
        self.source_digest = source_digest
        projects = sorted(ifc_file.by_type("IfcProject"), key=lambda p: p.GlobalId)
        project_id = projects[0].GlobalId if projects else "model"
        self.base_uri = base_uri.replace("{project}", project_id)
        self.length_scale = ifcopenshell.util.unit.calculate_unit_scale(ifc_file)
        self.report = ConversionReport(self.source_system, self.contract_version, mapping.version)
        self.nodes: dict[int, Node] = {}
        self._by_iri: dict[URIRef, Node] = {}
        self._disciplines: dict[int, Any] = {}

    # --- helpers --------------------------------------------------------------

    def iri(self, global_id: str) -> URIRef:
        return URIRef(self.base_uri + global_id)

    def systems_of(self, entity: ifcopenshell.entity_instance) -> list:
        systems = []
        for rel in getattr(entity, "HasAssignments", None) or []:
            group = getattr(rel, "RelatingGroup", None)
            if group is not None and group.is_a("IfcSystem") and not group.is_a("IfcZone"):
                systems.append(group)
        return systems

    def system_discipline(self, system: ifcopenshell.entity_instance) -> Any:
        if system.id() not in self._disciplines:
            em = self.mapping.resolve(system)
            spec = (em.block.get("attributes") or {}).get("system_discipline") if em else None
            value = _Evaluator(self, system, em).evaluate(spec, "system_discipline") if spec else None
            self._disciplines[system.id()] = value
        return self._disciplines[system.id()]

    # --- conversion -----------------------------------------------------------

    def run(self) -> Graph:
        candidates = sorted(self.file.by_type("IfcRoot"), key=lambda e: e.GlobalId)
        for entity in candidates:
            key = self.mapping.entity_key(entity)
            if key is None:
                continue
            em = self.mapping.resolve(entity)
            if em is None:
                self.report.excluded_by_ifc_class[entity.is_a()] += 1
                continue
            self.nodes[entity.id()] = Node(
                entity=entity,
                mapping=em,
                iri=self.iri(entity.GlobalId),
                types=self.schema.rdf_types(em.contract_class),
            )
        nodes = sorted(self.nodes.values(), key=lambda n: n.global_id)
        for node in nodes:
            self._populate(node)
        self._relationships()
        for node in nodes:
            self._derive(node)
        return self._graph(nodes)

    def _set(self, node: Node, slot: str, value: Any) -> None:
        cls = node.contract_class
        if slot not in self.schema.class_slots(cls):
            self.report.dropped[f"{cls}.{slot} (slot not on class)"] += 1
            return
        range_name = self.schema.slot_range(cls, slot)
        for item in value if isinstance(value, list) else [value]:
            term = self._term(node, slot, range_name, item)
            if term is None:
                continue
            existing = node.values.setdefault(slot, [])
            if term in existing:
                continue
            if existing and not self.schema.is_multivalued(cls, slot):
                self.report.dropped[f"{cls}.{slot} (second value for single-valued slot)"] += 1
                continue
            existing.append(term)

    def _term(self, node: Node, slot: str, range_name: str, value: Any):
        cls = node.contract_class
        if isinstance(value, Node):
            if not self.schema.is_class(range_name) or self.schema.class_uri(range_name) not in value.types:
                self.report.dropped[f"{cls}.{slot} → {value.contract_class} (outside range {range_name})"] += 1
                return None
            return value.iri
        if self.schema.is_enum(range_name):
            try:
                return self.schema.enum_term(range_name, str(value))
            except ValueError:
                self.report.dropped[f"{cls}.{slot}={value!r} (not in {range_name})"] += 1
                return None
        if range_name == "boolean" and not isinstance(value, bool):
            text = str(value).strip().casefold()
            if text not in ("true", "false", ".t.", ".f."):
                self.report.dropped[f"{cls}.{slot}={value!r} (not boolean)"] += 1
                return None
            value = text in ("true", ".t.")
        if range_name in ("uriorcurie", "uri") and not _IRI_PATTERN.match(str(value)):
            self.report.dropped[f"{cls}.{slot} (not an IRI)"] += 1
            return None
        try:
            return self.schema.literal(range_name, value)
        except (TypeError, ValueError):
            self.report.dropped[f"{cls}.{slot}={value!r} (not {range_name})"] += 1
            return None

    def _populate(self, node: Node) -> None:
        em = node.mapping
        block = em.block
        ev = _Evaluator(self, node.entity, em)
        used_psets: set[tuple[str, str]] = set()
        promoted_attrs: set[str] = set()

        fields = block.get("fields") or {}
        for field_name, slot in self.mapping.field_slots.items():
            spec = fields.get(field_name)
            if spec is None:
                continue
            promoted_attrs |= _spec_attributes(spec)
            ev.trace.clear()
            value = ev.evaluate(spec, slot)
            if slot == "classifications":
                self._classifications(node, value or [])
            elif isinstance(value, ifcopenshell.entity_instance):
                target = self.nodes.get(value.id())
                if target is not None:
                    self._set(node, slot, target)
            elif _present(value):
                self._set(node, slot, value)
                used_psets.update(ev.trace)

        self._set(node, "content_kind", block["content_kind"])
        attributes = block.get("attributes") or {}
        for slot, spec in attributes.items():
            if slot == "metadata":
                continue
            promoted_attrs |= _spec_attributes(spec)
            ev.trace.clear()
            value = ev.evaluate(spec, slot)
            if _present(value):
                before = len(node.values.get(slot, []))
                self._set(node, slot, value)
                if len(node.values.get(slot, [])) > before:
                    used_psets.update(ev.trace)
        if em.predefined:
            promoted_attrs.add("PredefinedType")

        metadata_spec = attributes.get("metadata")
        if metadata_spec:
            self._metadata(node, ev, metadata_spec, used_psets, promoted_attrs)

    def _classifications(self, node: Node, entries: Iterable[dict[str, Any]]) -> None:
        if "classifications" not in self.schema.class_slots(node.contract_class):
            return
        for entry in entries:
            self._add_inlined(node, "classifications", "Classification", entry)

    def _add_inlined(self, node: Node, slot: str, class_name: str, entry: dict[str, Any]) -> None:
        clean = {k: v for k, v in entry.items() if _present(v)}
        for key in list(clean):
            if key not in self.schema.class_slots(class_name):
                del clean[key]
            elif self.schema.slot_range(class_name, key) in ("uriorcurie", "uri") and not _IRI_PATTERN.match(
                str(clean[key])
            ):
                del clean[key]
            elif not isinstance(clean[key], (str, int, float, bool)):
                serialized = serialize_value(clean[key])
                if serialized is None:
                    del clean[key]
                else:
                    clean[key] = serialized
        missing = [s for s in self.schema.required_slots(class_name) if s not in clean]
        if missing:
            self.report.dropped[f"{node.contract_class}.{slot} entry (missing {', '.join(missing)})"] += 1
            return
        bucket = node.inlined.setdefault(slot, [])
        if (class_name, clean) not in bucket:
            bucket.append((class_name, clean))

    def _metadata(self, node, ev, spec, used_psets, promoted_attrs) -> None:
        entries: dict[str, str] = {}
        for part in spec.get("parts") or []:
            key_format = (part.get("entry_format") or {}).get("metadata_key", "")
            if part.get("source") == "ifc_attribute_all":
                excluded = set(part.get("exclude_attributes") or [])
                if part.get("exclude_when_mapped_to_typed_slot"):
                    excluded |= promoted_attrs
                info = node.entity.get_info(include_identifier=False, recursive=False)
                for name, value in info.items():
                    if name in ("type", "id") or name in excluded:
                        continue
                    text = serialize_value(value)
                    if text is not None:
                        entries[key_format.format(ifc_class=node.entity.is_a(), attribute=name)] = text
            elif part.get("source") == "ifc_pset_all":
                for pset, properties in ev.psets.items():
                    for prop, value in properties.items():
                        if prop == "id" or (pset, prop) in used_psets:
                            continue
                        text = serialize_value(value)
                        if text is not None:
                            entries[key_format.format(pset=pset, property=prop)] = text
            else:
                self.report.unsupported_sources[str(part.get("source"))] += 1
        for key in sorted(entries):
            self._add_inlined(
                node, "metadata", "MetadataEntry", {"metadata_key": key, "metadata_value": entries[key]}
            )

    def _derive(self, node: Node) -> None:
        for spec in node.mapping.block.get("derivations") or []:
            source = spec.get("source")
            if source == "vocabulary_derived_classification":
                self._derive_classification(node, spec)
            elif source == "attribute_derivation":
                self._derive_attribute(node, spec)
            else:
                self.report.unsupported_sources[str(source)] += 1

    def _derive_classification(self, node: Node, spec: dict[str, Any]) -> None:
        cls = node.contract_class
        slot = spec["from_attribute"]
        terms = node.values.get(slot) or []
        scheme = spec["classification_scheme"]
        existing = {entry.get("classification_scheme") for _, entry in node.inlined.get("classifications", [])}
        if not terms or (spec.get("append_if_scheme_missing") and scheme in existing):
            return
        for term in terms:
            if not isinstance(term, URIRef):
                continue
            for target in self.vocab.bridge_targets(spec["bridge"], str(term)):
                concept = self.vocab.concept(scheme, target)
                if concept is None:
                    self.report.dropped[f"{cls}.classifications ({target} not in {scheme})"] += 1
                    continue
                self._add_inlined(
                    node,
                    "classifications",
                    "Classification",
                    {
                        "classification_scheme": scheme,
                        "classification_code": concept["notation"],
                        "classification_label": concept["label"],
                        "classification_uri": target,
                        "classification_source": spec.get("classification_source"),
                    },
                )

    def _derive_attribute(self, node: Node, spec: dict[str, Any]) -> None:
        target_slot = spec["target_attribute"]
        if spec.get("when_target_unset") and node.values.get(target_slot):
            return
        if not self._by_iri:
            self._by_iri = {n.iri: n for n in self.nodes.values()}
        related = node.values.get(spec["from_relation"]) or []
        source_nodes = [self._by_iri[iri] for iri in related if iri in self._by_iri]
        for source in sorted(source_nodes, key=lambda n: n.global_id):
            attr_spec = (source.mapping.block.get("attributes") or {}).get(spec["from_attribute"])
            value = _Evaluator(self, source.entity, source.mapping).evaluate(attr_spec, spec["from_attribute"])
            if not isinstance(value, (int, float)):
                continue
            rule = spec["rule"]
            self._set(node, target_slot, _COMPARATORS[rule["operator"]](value, rule["threshold"]))
            return

    # --- relationships --------------------------------------------------------

    def _relationships(self) -> None:
        for rel in sorted(self.file.by_type("IfcRelationship"), key=lambda r: r.GlobalId):
            key = self.mapping.relationship_key(rel)
            if key is None or key == "IfcRelAssociatesClassification":
                continue
            if key == "IfcRelAssignsToGroup":
                group = rel.RelatingGroup
                if group is not None and group.is_a("IfcSystem") and not group.is_a("IfcZone"):
                    key = "IfcRelAssignsToSystem"
            for subject, obj, relation_type, owner in self._relation_pairs(key, rel):
                self._relate(key, subject, obj, relation_type, owner)

    def _resolve_type(self, spec: dict[str, Any], entity, condition: str) -> str | None:
        for resolution in spec.get("resolutions") or []:
            classes = resolution.get(condition)
            if classes is None:
                continue
            classes = [classes] if isinstance(classes, str) else classes
            if entity is not None and any(entity.is_a(c) for c in classes):
                return resolution["relation_type"]
        return spec.get("relation_type") if not spec.get("resolutions") else None

    def _relation_pairs(self, key: str, rel):
        """Yield ``(a, b, relation_type, owner)``; ``owner`` picks the subject.

        ``owner`` is ``"a"`` when ``a`` is always the subject, or ``"slot"`` when the
        subject is whichever endpoint's contract class declares the slot.
        """
        spec = self.mapping.relationships[key]
        if key == "IfcRelContainedInSpatialStructure":
            parent = rel.RelatingStructure
            relation_type = self._resolve_type(spec, parent, "when_relating_class")
            for child in rel.RelatedElements or []:
                yield child, parent, relation_type, "a"
        elif key == "IfcRelAggregates":
            parent = rel.RelatingObject
            relation_type = self._resolve_type(spec, parent, "when_related_class")
            for child in rel.RelatedObjects or []:
                yield child, parent, relation_type, "a"
        elif key == "IfcRelAssignsToGroup":
            group = rel.RelatingGroup
            classes = spec.get("group_classes") or []
            if group is not None and group.is_a() in classes:
                for member in rel.RelatedObjects or []:
                    yield group, member, spec["relation_type"], "a"
        elif key == "IfcRelAssignsToSystem":
            system = rel.RelatingGroup
            for member in rel.RelatedObjects or []:
                kind = "system" if member.is_a("IfcSystem") else "element"
                for resolution in spec.get("resolutions") or []:
                    if resolution.get("when_related_is") != kind:
                        continue
                    if kind == "element":
                        yield member, system, resolution["relation_type"], "a"
                    else:
                        yield system, member, resolution["relation_type"], "a"
        elif key == "IfcRelSpaceBoundary":
            space, element = rel.RelatingSpace, rel.RelatedBuildingElement
            if space is None or element is None:
                return
            relation_type = self._resolve_type(spec, element, "when_element_class")
            if relation_type:
                yield element, space, relation_type, "slot"
            if spec.get("space_relation_type"):
                yield space, element, spec["space_relation_type"], "a"
        elif key == "IfcRelServicesBuildings":
            system = rel.RelatingSystem
            for related in rel.RelatedBuildings or []:
                relation_type = self._resolve_type(spec, related, "when_related_class")
                yield system, related, relation_type, "a"
        else:
            endpoints = {
                "IfcRelConnectsElements": ("RelatingElement", "RelatedElement"),
                "IfcRelConnectsPathElements": ("RelatingElement", "RelatedElement"),
                "IfcRelFillsElement": ("RelatingOpeningElement", "RelatedBuildingElement"),
                "IfcRelCoversBldgElements": ("RelatingBuildingElement", "RelatedCoverings"),
            }.get(key)
            if endpoints is None:
                self.report.unsupported_sources[f"relationship {key}"] += 1
                return
            first = getattr(rel, endpoints[0], None)
            seconds = getattr(rel, endpoints[1], None)
            for second in seconds if isinstance(seconds, (list, tuple)) else [seconds]:
                if first is not None and second is not None:
                    yield first, second, spec.get("relation_type"), "slot"

    def _relate(self, key: str, a, b, relation_type: str | None, owner: str) -> None:
        if not relation_type:
            return
        node_a, node_b = self.nodes.get(a.id()), self.nodes.get(b.id())
        if node_a is None or node_b is None:
            return
        subject, obj = node_a, node_b
        if owner == "slot" and relation_type not in self.schema.class_slots(node_a.contract_class):
            if relation_type in self.schema.class_slots(node_b.contract_class):
                subject, obj = node_b, node_a
        if key not in (subject.mapping.block.get("relations") or []):
            self.report.dropped[f"{subject.contract_class}.{relation_type} ({key} not listed)"] += 1
            return
        self._set(subject, relation_type, obj)

    # --- graph ------------------------------------------------------------------

    def _graph(self, nodes: list[Node]) -> Graph:
        schema = self.schema
        graph = Graph(bind_namespaces="none")
        pbs = Namespace(schema.prefixes.get("pbs", SCHEMA_BASE))
        graph.bind("pbs", pbs)
        graph.bind("bot", Namespace(BOT))
        graph.bind("ifcowl", Namespace(schema.prefixes["ifcowl"]))
        graph.bind("rdf", RDF)
        graph.bind("xsd", XSD)
        graph.bind("dcterms", DCTERMS)
        graph.bind("dcat", DCAT)
        graph.bind("inst", Namespace(self.base_uri))

        dataset = URIRef(self.base_uri)
        graph.add((dataset, RDF.type, DCAT.Dataset))
        graph.add((dataset, DCTERMS.conformsTo, URIRef(f"{SCHEMA_BASE}{self.contract_version}/")))
        graph.add((dataset, pbs.contract_version, Literal(self.contract_version)))
        graph.add((dataset, pbs.mapping_version, Literal(self.mapping.version)))
        if self.source_digest:
            graph.add((dataset, DCTERMS.source, Literal(f"sha256:{self.source_digest}")))

        for node in nodes:
            cls = node.contract_class
            self.report.nodes_by_class[cls] += 1
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
                    graph.add((blank, RDF.type, schema.class_uri(class_name)))
                    for key, value in sorted(entry.items()):
                        graph.add(
                            (blank, schema.slot_uri(key), schema.literal(schema.slot_range(class_name, key), value))
                        )
            present = set(node.values) | set(node.inlined)
            for slot in schema.required_slots(cls):
                if slot not in present:
                    self.report.missing_required[f"{cls}.{slot}"] += 1
        return graph


def detect_source_system(ifc_file: ifcopenshell.file, conventions: dict[str, Any]) -> str:
    config = conventions.get("source_system") or {}
    texts: list[str] = []
    for app in ifc_file.by_type("IfcApplication"):
        texts += [app.ApplicationFullName or "", app.ApplicationIdentifier or ""]
    header = ifc_file.header.file_name
    texts += [header.originating_system or "", header.preprocessor_version or ""]
    blob = " ".join(texts).casefold()
    for system, keywords in (config.get("detect") or {}).items():
        if any(str(keyword).casefold() in blob for keyword in keywords):
            return system
    return config.get("default", "ifc")


def convert(
    ifc_path: Path | str,
    *,
    base_uri: str = DEFAULT_BASE_URI,
    contract_version: str | None = None,
    source_system: str | None = None,
    mapping_path: Path | str | None = None,
    schema_path: Path | str | None = None,
) -> tuple[Graph, ConversionReport]:
    """Convert ``ifc_path`` into a contract RDF graph and a conversion report."""
    ifc_path = Path(ifc_path)
    digest = hashlib.sha256(ifc_path.read_bytes()).hexdigest()
    converter = Converter(
        ifcopenshell.open(str(ifc_path)),
        mapping=Mapping.load(Path(mapping_path) if mapping_path else default_mapping_path()),
        schema=ContractSchema(Path(schema_path) if schema_path else default_schema_path()),
        vocab=Vocabularies(classification_dir()),
        base_uri=base_uri,
        contract_version=contract_version,
        source_system=source_system,
        source_digest=digest,
    )
    graph = converter.run()
    return graph, converter.report


def to_turtle(graph: Graph) -> str:
    return graph.serialize(format="turtle")
