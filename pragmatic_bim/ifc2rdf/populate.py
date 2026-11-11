"""Populate node slots from mapping fields, attributes, metadata, and derivations."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

import ifcopenshell
from rdflib import URIRef

from pragmatic_bim.ifc2rdf.evaluator import Evaluator, spec_attributes
from pragmatic_bim.ifc2rdf.model import Node, present, serialize_value
from pragmatic_bim.ifc2rdf.normalize import COMPARATORS, normalize

if TYPE_CHECKING:
    from pragmatic_bim.ifc2rdf.pipeline import Converter


def populate(conv: "Converter", node: Node) -> None:
    em = node.mapping
    block = em.block
    ev = Evaluator(conv, node.entity, em)
    used_psets: set[tuple[str, str]] = set()
    promoted_attrs: set[str] = set()

    fields = block.get("fields") or {}
    for field_name, slot in conv.mapping.field_slots.items():
        spec = fields.get(field_name)
        if spec is None:
            continue
        promoted_attrs |= spec_attributes(spec)
        ev.trace.clear()
        value = ev.evaluate(spec, slot)
        if slot == "classifications":
            conv.writer.classifications(node, value or [])
        elif isinstance(value, ifcopenshell.entity_instance):
            target = conv.nodes.get(value.id())
            if target is not None:
                conv.writer.set(node, slot, target)
        elif present(value):
            conv.writer.set(node, slot, value)
            used_psets.update(ev.trace)

    conv.writer.set(node, "content_kind", block["content_kind"])
    attributes = block.get("attributes") or {}
    performance_psets: set[tuple[str, str]] = set()
    for slot, spec in attributes.items():
        if slot == "metadata":
            continue
        if isinstance(spec, dict) and spec.get("source") == "ifc_pset_performance":
            performance_psets |= _performance_properties(conv, node, ev, slot, spec)
            continue
        promoted_attrs |= spec_attributes(spec)
        ev.trace.clear()
        value = ev.evaluate(spec, slot)
        if present(value):
            before = len(node.values.get(slot, []))
            conv.writer.set(node, slot, value)
            if len(node.values.get(slot, [])) > before:
                used_psets.update(ev.trace)
    if em.predefined:
        promoted_attrs.add("PredefinedType")

    metadata_spec = attributes.get("metadata")
    if metadata_spec:
        _metadata(conv, node, ev, metadata_spec, used_psets, promoted_attrs, performance_psets)


def _performance_properties(
    conv: "Converter", node: Node, ev: Evaluator, slot: str, spec: dict[str, Any]
) -> set[tuple[str, str]]:
    """Add normalized PerformanceProperty records; return the ``(pset, property)`` pairs used."""
    used: set[tuple[str, str]] = set()
    if slot not in conv.schema.class_slots(node.contract_class):
        conv.report.dropped[f"{node.contract_class}.{slot} (slot not on class)"] += 1
        return used
    for prop in spec.get("properties") or []:
        rule = prop.get("normalize") or {}
        label = f"{prop['property_class']}.{prop['property_key']}"
        for pset, name, raw in ev.pset_candidates(prop["lookup"]):
            values = normalize(rule, raw)
            if not values:
                conv.report.rejected_values[f"{label} {pset}.{name}={raw!r}"] += 1
                continue
            value_type = rule.get("value_type", "string")
            for key, value in values:
                entry = {
                    "property_key": key or prop["property_key"],
                    "property_value_type": value_type,
                    f"property_value_{value_type}": value,
                    "source_pset": pset,
                    "source_property": name,
                    "source_value_raw": serialize_value(raw),
                    "mapping_version": conv.mapping.version,
                }
                if key is None:
                    entry["property_unit"] = rule.get("unit")
                    entry["property_unit_uri"] = rule.get("unit_uri")
                conv.writer.add_inlined(node, slot, prop["property_class"], entry)
            used.add((pset, name))
            break
    return used


def _metadata(conv, node, ev, spec, used_psets, promoted_attrs, performance_psets) -> None:
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
            skip = set(used_psets)
            if "attributes.performance_properties" not in (part.get("keep_used_in") or []):
                skip |= performance_psets
            for pset, properties in ev.psets.items():
                for prop, value in properties.items():
                    if prop == "id" or (pset, prop) in skip:
                        continue
                    text = serialize_value(value)
                    if text is not None:
                        entries[key_format.format(pset=pset, property=prop)] = text
        else:
            conv.report.unsupported_sources[str(part.get("source"))] += 1
    for key in sorted(entries):
        conv.writer.add_inlined(node, "metadata", "MetadataEntry", {"metadata_key": key, "metadata_value": entries[key]})


def derive(conv: "Converter", node: Node) -> None:
    for spec in node.mapping.block.get("derivations") or []:
        source = spec.get("source")
        if source == "vocabulary_derived_classification":
            _derive_classification(conv, node, spec)
        elif source == "attribute_derivation":
            _derive_attribute(conv, node, spec)
        else:
            conv.report.unsupported_sources[str(source)] += 1


def _derive_classification(conv: "Converter", node: Node, spec: dict[str, Any]) -> None:
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
        for target in conv.vocab.bridge_targets(spec["bridge"], str(term)):
            concept = conv.vocab.concept(scheme, target)
            if concept is None:
                conv.report.dropped[f"{cls}.classifications ({target} not in {scheme})"] += 1
                continue
            conv.writer.add_inlined(
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


def _derive_attribute(conv: "Converter", node: Node, spec: dict[str, Any]) -> None:
    target_slot = spec["target_attribute"]
    if spec.get("when_target_unset") and node.values.get(target_slot):
        return
    related = node.values.get(spec["from_relation"]) or []
    source_nodes = [conv.by_iri[iri] for iri in related if iri in conv.by_iri]
    for source in sorted(source_nodes, key=lambda n: n.global_id):
        attr_spec = (source.mapping.block.get("attributes") or {}).get(spec["from_attribute"])
        value = Evaluator(conv, source.entity, source.mapping).evaluate(attr_spec, spec["from_attribute"])
        if not isinstance(value, (int, float)):
            continue
        rule = spec["rule"]
        conv.writer.set(node, target_slot, COMPARATORS[rule["operator"]](value, rule["threshold"]))
        return
