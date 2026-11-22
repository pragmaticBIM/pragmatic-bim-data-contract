"""``space_adjacency``: element↔space relations from geometry when IFC space boundaries are missing.

Fills ``separates_spaces`` / ``connects_spaces`` / ``bounded_by`` / ``adjacent_elements`` the same way
``IfcRelSpaceBoundary`` does. IFC pairs win when both sources exist; disagreements go into the
conversion report. Every kept pair gets a ``ConnectionVirtual`` with ``Derivation`` provenance
(``ifc_explicit`` or ``ifc_geometry``).
"""

from __future__ import annotations

from typing import Any

import shapely

from pragmatic_bim.ifc2rdf.geometry import ElementGeometry, SpatialIndex
from pragmatic_bim.ifc2rdf.model import Node
from pragmatic_bim.ifc2rdf.spatial.context import SpatialContext

_METHOD = "space_adjacency"
_METHOD_VERSION = "0.1"

# Element → (slot on element or space, whether the element is the subject).
# Mirrors contract/mapping/_relationships.yaml IfcRelSpaceBoundary resolutions.
_SLOT_BY_IFC = (
    (("IfcWall", "IfcWallStandardCase", "IfcSlab", "IfcCurtainWall"), "separates_spaces", True),
    (("IfcDoor", "IfcWindow"), "connects_spaces", True),
    (("IfcCovering",), "bounded_by", False),
)


def space_adjacency(ctx: SpatialContext, spec: dict[str, Any]) -> None:
    contact_tolerance = float(spec.get("contact_tolerance", 0.02))
    min_overlap_height = float(spec.get("min_overlap_height", 0.05))
    min_plan_overlap = float(spec.get("min_plan_overlap", 0.01))
    method_version = str(spec.get("method_version", _METHOD_VERSION))

    spaces = ctx.nodes_matching(spec.get("spaces") or {"contract_class": "Space"})
    elements = ctx.nodes_matching(spec.get("elements") or {"contract_class": "PhysicalElement"})
    space_by_iri = {space.iri: space for space in spaces}
    element_by_iri = {element.iri: element for element in elements}

    ifc_pairs = _ifc_pairs(spaces, space_by_iri, element_by_iri)
    ctx.conv.report.spaces_without_ifc_boundaries = sum(
        1 for space in spaces if not any(pair[1] == space.iri for pair in ifc_pairs)
    )

    geometry_pairs: dict[tuple, float] = {}
    for space in spaces:
        space_geo = ctx.geo(space)
        if space_geo is None:
            continue
        search = _search_distance(spec, contact_tolerance)
        for candidate in ctx.index.near(space_geo.plan, search):
            element = ctx.node_of(candidate)
            if element is None or element.iri not in element_by_iri:
                continue
            slot = _slot_for(element)
            if slot is None:
                continue
            tolerance = _pair_tolerance(ctx, element, candidate, contact_tolerance)
            if not _adjacent(space_geo, candidate, tolerance, min_overlap_height, min_plan_overlap):
                continue
            geometry_pairs[(element.iri, space.iri, slot)] = tolerance

    ifc_keys = set(ifc_pairs)
    geometry_keys = set(geometry_pairs)
    # Only compare when both endpoints tessellated; otherwise keep IFC without a disagreement.
    comparable = {
        key
        for key in ifc_keys
        if ctx.geo(element_by_iri[key[0]]) is not None and ctx.geo(space_by_iri[key[1]]) is not None
    }

    for key in sorted(ifc_keys & geometry_keys, key=lambda k: (str(k[0]), str(k[1]), k[2])):
        ctx.conv.report.adjacency_comparison["ifc_and_geometry"] += 1
        element, space = element_by_iri[key[0]], space_by_iri[key[1]]
        ctx.add_adjacency_connection(
            element,
            space,
            source_kind="ifc_explicit",
            method="IfcRelSpaceBoundary",
            method_version=method_version,
            tolerance=geometry_pairs[key],
        )

    for key in sorted((ifc_keys - geometry_keys) & comparable, key=lambda k: (str(k[0]), str(k[1]), k[2])):
        ctx.conv.report.adjacency_comparison["ifc_only"] += 1
        element, space = element_by_iri[key[0]], space_by_iri[key[1]]
        ctx.conv.report.adjacency_disagreements.append(
            f"IFC {key[2]} {element.global_id} ↔ {space.global_id} not found by geometry"
        )
        ctx.add_adjacency_connection(
            element,
            space,
            source_kind="ifc_explicit",
            method="IfcRelSpaceBoundary",
            method_version=method_version,
            tolerance=None,
        )

    for key in sorted((ifc_keys - geometry_keys) - comparable, key=lambda k: (str(k[0]), str(k[1]), k[2])):
        element, space = element_by_iri[key[0]], space_by_iri[key[1]]
        ctx.add_adjacency_connection(
            element,
            space,
            source_kind="ifc_explicit",
            method="IfcRelSpaceBoundary",
            method_version=method_version,
            tolerance=None,
        )

    for key in sorted(geometry_keys - ifc_keys, key=lambda k: (str(k[0]), str(k[1]), k[2])):
        ctx.conv.report.adjacency_comparison["geometry_only"] += 1
        element, space = element_by_iri[key[0]], space_by_iri[key[1]]
        slot, tolerance = key[2], geometry_pairs[key]
        _write_pair(ctx, element, space, slot, "geometry")
        ctx.add_adjacency_connection(
            element,
            space,
            source_kind="ifc_geometry",
            method=_METHOD,
            method_version=method_version,
            tolerance=tolerance,
        )


def _ifc_pairs(
    spaces: list[Node],
    space_by_iri: dict,
    element_by_iri: dict,
) -> set[tuple]:
    """Element↔space pairs already stated by ``IfcRelSpaceBoundary`` (any of the four slots)."""
    pairs: set[tuple] = set()
    for space in spaces:
        for element_iri in space.values.get("adjacent_elements") or ():
            element = element_by_iri.get(element_iri)
            if element is None:
                continue
            slot = _slot_for(element)
            if slot is None:
                continue
            pairs.add((element.iri, space.iri, slot))
        for element_iri in space.values.get("bounded_by") or ():
            element = element_by_iri.get(element_iri)
            if element is not None:
                pairs.add((element.iri, space.iri, "bounded_by"))
    for element in element_by_iri.values():
        for slot in ("separates_spaces", "connects_spaces"):
            for space_iri in element.values.get(slot) or ():
                if space_iri in space_by_iri:
                    pairs.add((element.iri, space_iri, slot))
        space_iri = (element.values.get("bounded_space") or [None])[0]
        if space_iri in space_by_iri:
            pairs.add((element.iri, space_iri, "bounded_by"))
    return pairs


def _write_pair(ctx: SpatialContext, element: Node, space: Node, slot: str, method: str) -> None:
    if slot == "bounded_by":
        ctx.relate(space, "bounded_by", element, method)
        if "bounded_space" in ctx.conv.schema.class_slots(element.contract_class):
            ctx.relate(element, "bounded_space", space, method)
    else:
        ctx.relate(element, slot, space, method)
    ctx.relate(space, "adjacent_elements", element, method)


def _slot_for(element: Node) -> str | None:
    if element.entity is None:
        return None
    for classes, slot, _ in _SLOT_BY_IFC:
        if any(element.entity.is_a(c) for c in classes):
            return slot
    return None


def _search_distance(spec: dict[str, Any], contact_tolerance: float) -> float:
    """Upper bound for the spatial index query (half thickness is applied per pair)."""
    return float(spec.get("max_half_thickness", 0.50)) + contact_tolerance


def _pair_tolerance(
    ctx: SpatialContext, element: Node, geometry: ElementGeometry, contact_tolerance: float
) -> float:
    """Wall-thickness/2 + contact_tolerance; slabs and thin elements fall back to contact_tolerance."""
    half = _half_thickness(geometry)
    if element.entity is not None and element.entity.is_a("IfcSlab"):
        return contact_tolerance
    return half + contact_tolerance


def _half_thickness(geometry: ElementGeometry) -> float:
    """Shorter plan extent of the oriented envelope, halved (wall thickness proxy)."""
    envelope = shapely.oriented_envelope(geometry.plan)
    if envelope.is_empty:
        return 0.0
    coords = list(envelope.exterior.coords)
    edges = [
        ((coords[i][0] - coords[i + 1][0]) ** 2 + (coords[i][1] - coords[i + 1][1]) ** 2) ** 0.5
        for i in range(4)
    ]
    return 0.5 * min(edges) if edges else 0.0


def _adjacent(
    space: ElementGeometry,
    element: ElementGeometry,
    tolerance: float,
    min_overlap_height: float,
    min_plan_overlap: float,
) -> bool:
    """Element body meets the space volume within ``tolerance`` (plan gap or vertical bearing)."""
    if element.ifc_class == "IfcSlab" or element.ifc_class.endswith("Slab"):
        return _slab_adjacent(space, element, tolerance, min_plan_overlap)
    if SpatialIndex.z_overlap(space, element) < min_overlap_height:
        return False
    return float(shapely.distance(space.plan, element.plan)) <= tolerance + 1e-9


def _slab_adjacent(
    space: ElementGeometry, slab: ElementGeometry, tolerance: float, min_plan_overlap: float
) -> bool:
    """Space floor on the slab top, or space ceiling against the slab bottom, with plan overlap."""
    overlap = float(shapely.area(shapely.intersection(space.plan, slab.plan)))
    if overlap < min_plan_overlap:
        return False
    floor_on_top = abs(space.z_min - slab.z_max) <= tolerance
    ceiling_on_bottom = abs(space.z_max - slab.z_min) <= tolerance
    return floor_on_top or ceiling_on_bottom
