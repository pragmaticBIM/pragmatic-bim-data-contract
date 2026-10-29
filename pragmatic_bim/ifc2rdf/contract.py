"""Read the LinkML contract schema: class hierarchy, slots, enums, and URIs.

Only the parts needed to serialize instance data are interpreted. The RDF terms follow
LinkML conventions: ``class_uri`` / ``slot_uri`` (default prefix ``pbs``) and enum
permissible values serialized as their ``meaning`` IRI when one is declared.
"""

from __future__ import annotations

from functools import lru_cache
from pathlib import Path
from typing import Any

import yaml
from rdflib import XSD, Literal, URIRef

BOT = "https://w3id.org/bot#"

_LITERAL_DATATYPES = {
    "string": None,
    "integer": XSD.integer,
    "double": XSD.double,
    "float": XSD.double,
    "decimal": XSD.decimal,
    "boolean": XSD.boolean,
    "date": XSD.date,
    "datetime": XSD.dateTime,
}
_IRI_TYPES = {"uriorcurie", "uri", "curie"}


class ContractSchema:
    def __init__(self, root: Path) -> None:
        self.root = Path(root)
        self.prefixes: dict[str, str] = {}
        self.classes: dict[str, dict[str, Any]] = {}
        self.slots: dict[str, dict[str, Any]] = {}
        self.enums: dict[str, dict[str, Any]] = {}
        self.default_prefix = "pbs"
        self._load(self.root, set())
        self._meaning_index: dict[str, dict[str, str]] = {}

    def _load(self, path: Path, seen: set[Path]) -> None:
        path = path.resolve()
        if path in seen:
            return
        seen.add(path)
        data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
        for name, value in (data.get("prefixes") or {}).items():
            self.prefixes.setdefault(name, value if isinstance(value, str) else value["prefix_reference"])
        if path == self.root.resolve():
            self.default_prefix = data.get("default_prefix", self.default_prefix)
        for imported in data.get("imports") or []:
            if imported.startswith("linkml:"):
                continue
            self._load(path.parent / f"{imported}.yaml", seen)
        self.classes.update(data.get("classes") or {})
        self.slots.update(data.get("slots") or {})
        self.enums.update(data.get("enums") or {})

    # --- URIs -----------------------------------------------------------------

    def expand(self, curie: str) -> str:
        if "://" in curie or curie.startswith("urn:"):
            return curie
        prefix, sep, local = curie.partition(":")
        if sep and prefix in self.prefixes:
            return self.prefixes[prefix] + local
        return self.prefixes[self.default_prefix] + curie

    def class_uri(self, name: str) -> URIRef:
        return URIRef(self.expand(self.classes[name].get("class_uri") or name))

    def slot_uri(self, name: str) -> URIRef:
        return URIRef(self.expand(self.slots.get(name, {}).get("slot_uri") or name))

    # --- Classes --------------------------------------------------------------

    @lru_cache(maxsize=None)
    def ancestors(self, name: str) -> tuple[str, ...]:
        """``name`` followed by its ``is_a`` chain."""
        chain = []
        current: str | None = name
        while current:
            chain.append(current)
            current = self.classes[current].get("is_a")
        return tuple(chain)

    @lru_cache(maxsize=None)
    def class_slots(self, name: str) -> frozenset[str]:
        slots: set[str] = set()
        for cls in self.ancestors(name):
            definition = self.classes[cls]
            slots.update(definition.get("slots") or [])
            slots.update((definition.get("attributes") or {}).keys())
        return frozenset(slots)

    def _slot_usage(self, class_name: str, slot: str, key: str) -> Any:
        for cls in self.ancestors(class_name):
            usage = (self.classes[cls].get("slot_usage") or {}).get(slot) or {}
            if key in usage:
                return usage[key]
        return None

    def slot_property(self, class_name: str, slot: str, key: str, default: Any = None) -> Any:
        value = self._slot_usage(class_name, slot, key)
        if value is not None:
            return value
        return self.slots.get(slot, {}).get(key, default)

    def slot_range(self, class_name: str, slot: str) -> str:
        return self.slot_property(class_name, slot, "range") or "string"

    def is_multivalued(self, class_name: str, slot: str) -> bool:
        return bool(self.slot_property(class_name, slot, "multivalued", False))

    def required_slots(self, class_name: str) -> list[str]:
        return sorted(
            slot
            for slot in self.class_slots(class_name)
            if self.slot_property(class_name, slot, "required", False) and slot != "id"
        )

    def content_kind(self, class_name: str) -> str | None:
        return self._slot_usage(class_name, "content_kind", "equals_string")

    @lru_cache(maxsize=None)
    def rdf_types(self, class_name: str) -> tuple[URIRef, ...]:
        """Contract types plus BOT exact mappings asserted on an instance of ``class_name``.

        Ancestors are included so that ``sh:class`` constraints on abstract ranges
        (for example ``parent_building`` → ``BuiltAssetContext``) hold without RDFS
        inference. Ancestors that pin a different ``content_kind`` than the class
        (``VirtualEntity`` above ``SpatialContext``) are skipped because their
        generated shape would reject the instance.
        """
        kind = self.content_kind(class_name)
        types: list[URIRef] = []
        bot_types: list[URIRef] = []
        for cls in self.ancestors(class_name):
            pinned = self.content_kind(cls)
            if pinned is not None and pinned != kind:
                continue
            types.append(self.class_uri(cls))
            for mapped in self.classes[cls].get("exact_mappings") or []:
                uri = URIRef(self.expand(mapped))
                if str(uri).startswith(BOT) and uri not in bot_types:
                    bot_types.append(uri)
        return tuple(types + bot_types)

    # --- Values ---------------------------------------------------------------

    def is_class(self, name: str) -> bool:
        return name in self.classes

    def is_enum(self, name: str) -> bool:
        return name in self.enums

    def enum_term(self, enum_name: str, value: str) -> URIRef | Literal:
        values = self.enums[enum_name].get("permissible_values") or {}
        if value not in values:
            raise ValueError(f"{value!r} is not a permissible value of {enum_name}")
        meaning = (values[value] or {}).get("meaning")
        return URIRef(self.expand(meaning)) if meaning else Literal(value)

    def enum_value_for_meaning(self, enum_name: str, iri: str) -> str | None:
        index = self._meaning_index.get(enum_name)
        if index is None:
            index = {}
            for value, spec in (self.enums[enum_name].get("permissible_values") or {}).items():
                meaning = (spec or {}).get("meaning")
                if meaning:
                    index.setdefault(self.expand(meaning), value)
            self._meaning_index[enum_name] = index
        return index.get(iri)

    def literal(self, range_name: str, value: Any) -> URIRef | Literal:
        if range_name in _IRI_TYPES:
            return URIRef(str(value))
        datatype = _LITERAL_DATATYPES.get(range_name)
        if range_name == "boolean":
            return Literal(bool(value), datatype=XSD.boolean)
        if datatype in (XSD.double, XSD.decimal):
            return Literal(float(value), datatype=datatype)
        if datatype == XSD.integer:
            return Literal(int(value), datatype=datatype)
        if datatype is None:
            return Literal(str(value))
        return Literal(value, datatype=datatype)
