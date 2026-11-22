"""Shared state for computed relations: geometry, spatial index, selectors, quantity output."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Iterable, Sequence

import ifcopenshell.util.element
import ifcopenshell.util.unit

from pragmatic_bim.ifc2rdf.geometry import ElementGeometry, GeometryResult, SpatialIndex
from pragmatic_bim.ifc2rdf.mapping import EntityMapping
from pragmatic_bim.ifc2rdf.model import Node

if TYPE_CHECKING:
    from pragmatic_bim.ifc2rdf.pipeline import Converter

UNIT_URIS = {
    "m": "http://qudt.org/vocab/unit/M",
    "m2": "http://qudt.org/vocab/unit/M2",
    "m3": "http://qudt.org/vocab/unit/M3",
    "1": "http://qudt.org/vocab/unit/UNITLESS",
}

_MEASUREMENT_MAPPING = EntityMapping(
    key="DerivedMeasurement",
    block={"content_kind": "measurement", "canonical_type": "DerivedMeasurement"},
    contract_class="DerivedMeasurement",
    canonical_type="DerivedMeasurement",
    predefined={},
)
_CONNECTION_VIRTUAL_MAPPING = EntityMapping(
    key="ConnectionVirtual",
    block={"content_kind": "virtual", "canonical_type": "ConnectionVirtual"},
    contract_class="ConnectionVirtual",
    canonical_type="ConnectionVirtual",
    predefined={},
)


class SpatialContext:
    def __init__(self, conv: "Converter", geometry: GeometryResult) -> None:
        self.conv = conv
        self.geometry = geometry
        # Terrain meshes stay out of the plan-outline index used for other elements.
        indexed = [
            geo
            for geo in geometry.geometries.values()
            if not _is_terrain(conv, geo.id)
        ]
        self.index = SpatialIndex(indexed)
        self.area_scale = ifcopenshell.util.unit.calculate_unit_scale(conv.file, "AREAUNIT")
        self._psets: dict[int, dict[str, dict[str, Any]]] = {}

    def geo(self, node: Node) -> ElementGeometry | None:
        if node.entity is None:
            return None
        return self.geometry.geometries.get(node.entity.id())

    def node_of(self, geometry: ElementGeometry) -> Node | None:
        return self.conv.nodes.get(geometry.id)

    def psets(self, node: Node) -> dict[str, dict[str, Any]]:
        if node.entity is None:
            return {}
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
            if node.entity is None:
                return False
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

    def add_measurement(
        self,
        subjects: Sequence[Node],
        quantities: Sequence[tuple[str, float, str]],
        method: str,
        method_version: str,
        inputs: Iterable[Node | str] = (),
        tolerance: float | None = None,
        line_wkt: str | None = None,
        status: str = "measured",
        allow_negative: bool = False,
    ) -> Node | None:
        """Write a top-level ``DerivedMeasurement``; id is deterministic from method + subjects."""
        subject_list = list(subjects)
        if not subject_list:
            self.conv.report.dropped[f"DerivedMeasurement ({method}) (no subjects)"] += 1
            return None
        local_id = _measurement_id(method, subject_list)
        existing = self.conv.extra_nodes.get(local_id)
        if existing is not None:
            return existing

        node = Node(
            entity=None,
            mapping=_MEASUREMENT_MAPPING,
            iri=self.conv.iri(local_id),
            types=self.conv.schema.rdf_types("DerivedMeasurement"),
            local_id=local_id,
        )
        self.conv.extra_nodes[local_id] = node
        self.conv._by_iri = {}

        self.conv.writer.set(node, "content_kind", "measurement")
        self.conv.writer.set(node, "name", method)
        self.conv.writer.set(node, "measurement_status", status)
        self.conv.writer.set(node, "applies_to_entities", subject_list)

        input_refs = [str(item.iri) if isinstance(item, Node) else str(item) for item in inputs]
        derivation = {
            "_class": "Derivation",
            "derivation_source_kind": "ifc_geometry",
            "derivation_method": method,
            "derivation_method_version": method_version,
            "derivation_tolerance": tolerance,
            "derivation_tolerance_unit": "m" if tolerance is not None else None,
            "derivation_inputs": input_refs or None,
        }
        for quantity_type, value, unit in quantities:
            if value < 0 and not allow_negative:
                self.conv.report.dropped[f"DerivedMeasurement.quantity_values {quantity_type} (negative)"] += 1
                continue
            self.conv.writer.add_inlined(
                node,
                "quantity_values",
                "QuantityValue",
                {
                    "quantity_type": quantity_type,
                    "quantity_value": round(float(value), 4),
                    "quantity_unit": unit,
                    "quantity_unit_uri": UNIT_URIS.get(unit),
                    "derivation": derivation,
                },
            )
        if line_wkt:
            self.conv.writer.add_inlined(
                node,
                "geometry_representations",
                "GeometryRepresentation",
                {
                    "geometry_representation": "path_3d",
                    "geometry_reference": f"measurement#{local_id}",
                    "geometry_format": "wkt",
                    "geometry_wkt": line_wkt,
                },
            )
        self.conv.report.computed_measurements[method] += 1
        return node

    def relate(self, subject: Node, slot: str, obj: Node, method: str) -> bool:
        added = self.conv.writer.set(subject, slot, obj)
        if added:
            self.conv.report.computed_relations[f"{slot} ({method})"] += 1
        return added

    def add_adjacency_connection(
        self,
        element: Node,
        space: Node,
        *,
        source_kind: str,
        method: str,
        method_version: str,
        tolerance: float | None,
    ) -> Node | None:
        """Emit a ``ConnectionVirtual`` that carries Derivation for one element↔space adjacency."""
        local_id = f"space_adjacency__{element.global_id}__{space.global_id}"
        existing = self.conv.extra_nodes.get(local_id)
        if existing is not None:
            return existing

        node = Node(
            entity=None,
            mapping=_CONNECTION_VIRTUAL_MAPPING,
            iri=self.conv.iri(local_id),
            types=self.conv.schema.rdf_types("ConnectionVirtual"),
            local_id=local_id,
        )
        self.conv.extra_nodes[local_id] = node
        self.conv._by_iri = {}

        self.conv.writer.set(node, "content_kind", "virtual")
        self.conv.writer.set(node, "name", f"space adjacency {element.global_id} {space.global_id}")
        self.conv.writer.set(node, "connection_virtual_type", "adjacency")
        self.conv.writer.set(node, "connects_physical_elements", element)
        self.conv.writer.set(node, "connects_spaces", space)
        self.conv.writer.add_inlined(
            node,
            "derivation",
            "Derivation",
            {
                "derivation_source_kind": source_kind,
                "derivation_method": method,
                "derivation_method_version": method_version,
                "derivation_tolerance": tolerance,
                "derivation_tolerance_unit": "m" if tolerance is not None else None,
            },
        )
        self.conv.report.computed_relations[f"ConnectionVirtual ({source_kind})"] += 1
        return node


def _measurement_id(method: str, subjects: Sequence[Node]) -> str:
    subject_ids = sorted(node.global_id for node in subjects)
    return f"{method}__{'__'.join(subject_ids)}"


def _is_terrain(conv: "Converter", entity_id: int) -> bool:
    node = conv.nodes.get(entity_id)
    return node is not None and node.contract_class == "TerrainSurface"


def _equal(actual: Any, expected: Any) -> bool:
    if actual is None:
        return False
    if isinstance(expected, bool):
        if isinstance(actual, bool):
            return actual == expected
        return str(actual).strip().upper() in ({"TRUE", "T", ".T.", "1"} if expected else {"FALSE", "F", ".F.", "0"})
    return str(actual) == str(expected)
