"""Load ``ifc_mapping.merged.yaml`` and resolve entity blocks for IFC instances."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any

import ifcopenshell
import yaml


@dataclass(frozen=True)
class EntityMapping:
    key: str
    """Mapping entity key, for example ``IfcWall``."""
    block: dict[str, Any]
    """Entity block with ``inherits`` resolved."""
    contract_class: str
    """LinkML class name (``canonical_type`` without the variant suffix)."""
    canonical_type: str
    predefined: dict[str, Any]
    """Selected ``predefined_type_map`` entry (empty when the entity has none)."""


class Mapping:
    def __init__(self, data: dict[str, Any], path: Path | None = None) -> None:
        self.data = data
        self.path = path
        self.version = str(data["mapping_version"])
        self.canonical_type_version = str(data["canonical_type_version"])
        self.conventions = data.get("conventions") or {}
        self.relationships = data.get("relationships") or {}
        self.entities = data.get("entities") or {}
        self.templates = data.get("templates") or {}
        projection = self.conventions.get("rdf_projection") or {}
        self.field_slots: dict[str, str] = projection.get("field_slots") or {}
        self.excluded: set[str] = set((projection.get("exclude_entities") or {}).keys())
        self._resolved: dict[str, dict[str, Any]] = {}
        self._chains: dict[tuple[str, str], tuple[str, ...]] = {}

    @classmethod
    def load(cls, path: Path) -> "Mapping":
        return cls(yaml.safe_load(Path(path).read_text(encoding="utf-8")), Path(path))

    def block(self, key: str) -> dict[str, Any]:
        """Entity or template block with ``inherits`` merged (entity keys take precedence)."""
        if key not in self._resolved:
            own = self.entities.get(key) or self.templates.get(key)
            if own is None:
                raise KeyError(f"Mapping has no entity or template {key!r}")
            merged: dict[str, Any] = {}
            parent = own.get("inherits")
            if parent:
                merged.update(self.block(parent))
            merged.update({k: v for k, v in own.items() if k != "inherits"})
            self._resolved[key] = merged
        return self._resolved[key]

    def supertype_chain(self, schema: str, ifc_class: str) -> tuple[str, ...]:
        key = (schema, ifc_class)
        if key not in self._chains:
            chain = []
            decl = ifcopenshell.schema_by_name(schema).declaration_by_name(ifc_class)
            while decl is not None:
                chain.append(decl.name())
                decl = decl.supertype()
            self._chains[key] = tuple(chain)
        return self._chains[key]

    def entity_key(self, entity: ifcopenshell.entity_instance) -> str | None:
        """Nearest mapped IFC class of ``entity`` (exact class first, then supertypes)."""
        schema = entity.is_a(True).split(".")[0]
        for name in self.supertype_chain(schema, entity.is_a()):
            if name in self.entities:
                return name
        return None

    def resolve(self, entity: ifcopenshell.entity_instance) -> EntityMapping | None:
        key = self.entity_key(entity)
        if key is None or key in self.excluded:
            return None
        block = self.block(key)
        predefined: dict[str, Any] = {}
        if block.get("canonical_type_from") == "predefined_type_map":
            table = block["predefined_type_map"]
            predefined = table.get(predefined_type(entity) or "", table["default"])
            canonical = predefined["canonical_type"]
        else:
            canonical = block["canonical_type"]
        return EntityMapping(
            key=key,
            block=block,
            contract_class=canonical.split(".")[0],
            canonical_type=canonical,
            predefined=predefined,
        )

    def relationship_key(self, rel: ifcopenshell.entity_instance) -> str | None:
        schema = rel.is_a(True).split(".")[0]
        for name in self.supertype_chain(schema, rel.is_a()):
            if name in self.relationships:
                return name
        return None


def predefined_type(entity: ifcopenshell.entity_instance) -> str | None:
    """Occurrence ``PredefinedType``, falling back to the type object when not defined."""
    value = getattr(entity, "PredefinedType", None)
    if value in (None, "NOTDEFINED"):
        for rel in getattr(entity, "IsTypedBy", None) or getattr(entity, "IsDefinedBy", None) or []:
            type_object = getattr(rel, "RelatingType", None)
            if type_object is not None and hasattr(type_object, "PredefinedType"):
                type_value = type_object.PredefinedType
                if type_value not in (None, "NOTDEFINED"):
                    return type_value
    return value
