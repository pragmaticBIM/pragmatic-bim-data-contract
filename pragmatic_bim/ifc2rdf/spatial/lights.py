"""``window_daylight``: exterior window → interior space it lights, glazed area, glazing ratio.

The space comes from the window's ``connects_spaces`` (IFC space boundaries) when one
matches the object selector, otherwise from the nearest matching space within
``max_plan_distance`` that overlaps the window vertically.
"""

from __future__ import annotations

from collections import defaultdict
from typing import Any

import shapely

from pragmatic_bim.ifc2rdf.model import Node
from pragmatic_bim.ifc2rdf.spatial.context import SpatialContext


def window_daylight(ctx: SpatialContext, spec: dict[str, Any]) -> None:
    slot = spec["target_slot"]
    max_distance = float(spec.get("max_plan_distance", 0.60))
    quantities = spec.get("quantities") or {}
    area_spec = quantities.get("area_glazed")
    ratio_spec = quantities.get("glazing_ratio")
    glazed_by_space: dict[int, float] = defaultdict(float)
    spaces = ctx.nodes_matching(spec["object"])
    space_by_iri = {n.iri: n for n in spaces}

    for window in ctx.nodes_matching(spec["subject"]):
        lit = [space_by_iri[iri] for iri in window.values.get("connects_spaces") or [] if iri in space_by_iri]
        method = "ifc"
        if not lit:
            lit = _nearest_space(ctx, window, spec["object"], max_distance)
            method = "geometry"
        for space in lit:
            ctx.relate(window, slot, space, method)
        if area_spec is None:
            continue
        area = glazed_area(ctx, window, area_spec)
        if area is None:
            continue
        ctx.add_quantity(window, "area_glazed", area, area_spec["unit"])
        for space in lit:
            glazed_by_space[space.entity.id()] += area / len(lit)

    if ratio_spec is None:
        return
    for space in spaces:
        floor_area = _floor_area(ctx, space, ratio_spec)
        if floor_area:
            ctx.add_quantity(space, "glazing_ratio", glazed_by_space[space.entity.id()] / floor_area, ratio_spec["unit"])


def _nearest_space(ctx: SpatialContext, window: Node, selector: dict[str, Any], max_distance: float) -> list[Node]:
    geometry = ctx.geo(window)
    if geometry is None:
        return []
    best: tuple[float, str] | None = None
    found = None
    for candidate in ctx.index.near(geometry.plan, max_distance):
        node = ctx.node_of(candidate)
        if node is None or node is window or not ctx.matches(node, selector):
            continue
        if ctx.index.z_overlap(geometry, candidate) <= 0:
            continue
        key = (float(shapely.distance(geometry.plan, candidate.plan)), candidate.global_id)
        if best is None or key < best:
            best, found = key, node
    return [found] if found is not None else []


def glazed_area(ctx: SpatialContext, window: Node, spec: dict[str, Any]) -> float | None:
    """Window area (quantity set, then overall dimensions, then geometry) × glazing fraction."""
    area = ctx.pset_value(window, spec.get("area_sources"))
    if isinstance(area, (int, float)):
        area = float(area) * ctx.area_scale
    else:
        dimensions = [getattr(window.entity, a, None) for a in spec.get("dimension_attributes") or ()]
        if dimensions and all(isinstance(d, (int, float)) and d > 0 for d in dimensions):
            area = 1.0
            for dimension in dimensions:
                area *= float(dimension) * ctx.conv.length_scale
        else:
            geometry = ctx.geo(window)
            if geometry is None:
                return None
            envelope = shapely.oriented_envelope(geometry.plan)
            coords = list(envelope.exterior.coords) if envelope.geom_type == "Polygon" else []
            sides = [shapely.Point(a).distance(shapely.Point(b)) for a, b in zip(coords, coords[1:])]
            area = (max(sides) if sides else 0.0) * geometry.height
    fraction = ctx.pset_value(window, spec.get("glazing_fraction"))
    if isinstance(fraction, (int, float)) and 0 < fraction <= 1:
        area *= float(fraction)
    return area


def _floor_area(ctx: SpatialContext, space: Node, spec: dict[str, Any]) -> float | None:
    area = ctx.pset_value(space, spec.get("floor_area_sources"))
    if isinstance(area, (int, float)) and area > 0:
        return float(area) * ctx.area_scale
    geometry = ctx.geo(space)
    if geometry is None or geometry.footprint is None:
        return None
    return float(geometry.footprint.area) or None
