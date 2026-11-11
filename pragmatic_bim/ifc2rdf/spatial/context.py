"""Shared state for computed relations: geometry, spatial index, selectors, quantity output."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

import ifcopenshell.util.element
import ifcopenshell.util.unit

from pragmatic_bim.ifc2rdf.geometry import ElementGeometry, GeometryResult, SpatialIndex
from pragmatic_bim.ifc2rdf.model import Node

if TYPE_CHECKING:
    from pragmatic_bim.ifc2rdf.pipeline import Converter

UNIT_URIS = {
    "m": "http://qudt.org/vocab/unit/M",
    "m2": "http://qudt.org/vocab/unit/M2",
    "m3": "http://qudt.org/vocab/unit/M3",
    "1": "http://qudt.org/vocab/unit/UNITLESS",
}


class SpatialContext:
    def __init__(self, conv: "Converter", geometry: GeometryResult) -> None:
        self.conv = conv
        self.geometry = geometry
        self.index = SpatialIndex(geometry.geometries.values())
        self.area_scale = ifcopenshell.util.unit.calculate_unit_scale(conv.file, "AREAUNIT")
        self._psets: dict[int, dict[str, dict[str, Any]]] = {}

    def geo(self, node: Node) -> ElementGeometry | None:
        return self.geometry.geometries.get(node.entity.id())

    def node_of(self, geometry: ElementGeometry) -> Node | None:
        return self.conv.nodes.get(geometry.id)

    def psets(self, node: Node) -> dict[str, dict[str, Any]]:
        if node.entity.id() not in self._psets:
            self._psets[node.entity.id()] = ifcopenshell.util.element.get_psets(node.entity)
        return self._psets[node.entity.id()]

    def pset_value(self, node: Node, sources: list[dict[str, str]]) -> Any:
        """First present ``{pset, property}`` value."""
        for source in sources or []:
            value = (self.psets(node).get(source["pset"]) or {}).get(source["property"])
            if value not in (None, ""):
                return value
        return None

    def matches(self, node: Node, selector: dict[str, Any]) -> bool:
        """Selector keys combine with AND: contract_class, ifc_class, property, exclude_property."""
        contract_class = selector.get("contract_class")
        if contract_class and contract_class not in self.conv.schema.ancestors(node.contract_class):
            return False
        ifc_classes = selector.get("ifc_class")
        if ifc_classes:
            ifc_classes = [ifc_classes] if isinstance(ifc_classes, str) else ifc_classes
            if not any(node.entity.is_a(c) for c in ifc_classes):
                return False
        for path, expected in (selector.get("property") or {}).items():
            if not _equal(self._property(node, path), expected):
                return False
        for path, excluded in (selector.get("exclude_property") or {}).items():
            if _equal(self._property(node, path), excluded):
                return False
        return True

    def nodes_matching(self, selector: dict[str, Any]) -> list[Node]:
        return [n for n in self.conv.sorted_nodes() if self.matches(n, selector)]

    def _property(self, node: Node, path: str) -> Any:
        pset, _, prop = path.partition(".")
        return (self.psets(node).get(pset) or {}).get(prop)

    def add_quantity(self, node: Node, quantity_type: str, value: float, unit: str) -> bool:
        if value < 0:
            self.conv.report.dropped[f"{node.contract_class}.quantity_values {quantity_type} (negative)"] += 1
            return False
        added = self.conv.writer.add_inlined(
            node,
            "quantity_values",
            "QuantityValue",
            {
                "quantity_type": quantity_type,
                "quantity_value": round(float(value), 4),
                "quantity_unit": unit,
                "quantity_unit_uri": UNIT_URIS.get(unit),
            },
        )
        if added:
            self.conv.report.computed_quantities[quantity_type] += 1
        return added

    def relate(self, subject: Node, slot: str, obj: Node, method: str) -> bool:
        added = self.conv.writer.set(subject, slot, obj)
        if added:
            self.conv.report.computed_relations[f"{slot} ({method})"] += 1
        return added


def _equal(actual: Any, expected: Any) -> bool:
    if actual is None:
        return False
    if isinstance(expected, bool):
        if isinstance(actual, bool):
            return actual == expected
        return str(actual).strip().upper() in ({"TRUE", "T", ".T.", "1"} if expected else {"FALSE", "F", ".F.", "0"})
    return str(actual) == str(expected)
