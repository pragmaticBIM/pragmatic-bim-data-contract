"""``neighbour_distance``: clear horizontal and vertical distance to nearby physical elements."""

from __future__ import annotations

from typing import Any

import shapely
from shapely.ops import nearest_points

from pragmatic_bim.ifc2rdf.geometry import ElementGeometry
from pragmatic_bim.ifc2rdf.spatial.context import SpatialContext

_METHOD = "neighbour_distance"
_METHOD_VERSION = "0.1"


def neighbour_distance(ctx: SpatialContext, spec: dict[str, Any]) -> None:
    """One ``DerivedMeasurement`` per subject–object pair within both distance limits."""
    max_horizontal = float(spec.get("max_horizontal_distance", 1.0))
    max_vertical = float(spec.get("max_vertical_distance", 1.0))
    for subject in ctx.nodes_matching(spec["subject"]):
        geometry = ctx.geo(subject)
        if geometry is None:
            continue
        for candidate in ctx.index.near(geometry.plan, max_horizontal):
            node = ctx.node_of(candidate)
            if node is None or node is subject or not ctx.matches(node, spec["object"]):
                continue
            vertical = vertical_gap(geometry, candidate)
            if vertical > max_vertical:
                continue
            horizontal = ctx.index.plan_distance(geometry, candidate)
            p1, p2 = nearest_points(geometry.plan, candidate.plan)
            z1 = (geometry.z_min + geometry.z_max) / 2.0
            z2 = (candidate.z_min + candidate.z_max) / 2.0
            line = shapely.linestrings([[p1.x, p1.y, z1], [p2.x, p2.y, z2]])
            ctx.add_measurement(
                [subject, node],
                [
                    ("horizontal_clear_distance", round(horizontal, 3), "m"),
                    ("vertical_clear_distance", round(vertical, 3), "m"),
                ],
                method=_METHOD,
                method_version=_METHOD_VERSION,
                line_wkt=shapely.to_wkt(line, rounding_precision=3),
            )


def vertical_gap(a: ElementGeometry, b: ElementGeometry) -> float:
    return max(0.0, b.z_min - a.z_max, a.z_min - b.z_max)
