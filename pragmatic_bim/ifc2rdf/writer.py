"""Write values onto converter nodes, checked against the contract slot ranges."""

from __future__ import annotations

from typing import Any, Iterable

from pragmatic_bim.ifc2rdf.contract import ContractSchema
from pragmatic_bim.ifc2rdf.model import IRI_PATTERN, Node, present, serialize_value
from pragmatic_bim.ifc2rdf.report import ConversionReport


class SlotWriter:
    def __init__(self, schema: ContractSchema, report: ConversionReport) -> None:
        self.schema = schema
        self.report = report

    def set(self, node: Node, slot: str, value: Any) -> bool:
        """Add ``value`` (or each item of a list) to ``slot``; return whether anything was added."""
        cls = node.contract_class
        if slot not in self.schema.class_slots(cls):
            self.report.dropped[f"{cls}.{slot} (slot not on class)"] += 1
            return False
        range_name = self.schema.slot_range(cls, slot)
        added = False
        for item in value if isinstance(value, list) else [value]:
            term = self.term(node, slot, range_name, item)
            if term is None:
                continue
            existing = node.values.setdefault(slot, [])
            if term in existing:
                continue
            if existing and not self.schema.is_multivalued(cls, slot):
                self.report.dropped[f"{cls}.{slot} (second value for single-valued slot)"] += 1
                continue
            existing.append(term)
            added = True
        return added

    def term(self, node: Node, slot: str, range_name: str, value: Any):
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
        if range_name in ("uriorcurie", "uri") and not IRI_PATTERN.match(str(value)):
            self.report.dropped[f"{cls}.{slot} (not an IRI)"] += 1
            return None
        try:
            return self.schema.literal(range_name, value)
        except (TypeError, ValueError):
            self.report.dropped[f"{cls}.{slot}={value!r} (not {range_name})"] += 1
            return None

    def classifications(self, node: Node, entries: Iterable[dict[str, Any]]) -> None:
        if "classifications" not in self.schema.class_slots(node.contract_class):
            return
        for entry in entries:
            self.add_inlined(node, "classifications", "Classification", entry)

    def add_inlined(self, node: Node, slot: str, class_name: str, entry: dict[str, Any]) -> bool:
        """Add an inlined record; return whether it was added."""
        if slot not in self.schema.class_slots(node.contract_class):
            self.report.dropped[f"{node.contract_class}.{slot} (slot not on class)"] += 1
            return False
        clean = {k: v for k, v in entry.items() if present(v)}
        for key in list(clean):
            if key not in self.schema.class_slots(class_name):
                del clean[key]
            elif self.schema.is_enum(range_name := self.schema.slot_range(class_name, key)):
                try:
                    self.schema.enum_term(range_name, str(clean[key]))
                except ValueError:
                    reason = f"{class_name}.{key}={clean[key]!r} (not in {range_name})"
                    self.report.dropped[f"{node.contract_class}.{slot} {reason}"] += 1
                    return False
            elif range_name in ("uriorcurie", "uri") and not IRI_PATTERN.match(str(clean[key])):
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
            return False
        bucket = node.inlined.setdefault(slot, [])
        if (class_name, clean) in bucket:
            return False
        bucket.append((class_name, clean))
        return True
