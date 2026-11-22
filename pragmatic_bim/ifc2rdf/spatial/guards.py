"""``barrier_walking_surface``: safety barrier → spaces whose floor it protects, plus its height.

A space qualifies when its plan lies within ``max_plan_distance`` of the barrier and its
floor (space bottom) lies between ``barrier base - max_floor_below_base`` and
``barrier base + floor_tolerance``. The barrier height above the walking surface is
measured against the highest qualifying floor (worst case) and written as a
``DerivedMeasurement``.
"""

from __future__ import annotations

from typing import Any

import shapely

from pragmatic_bim.ifc2rdf.spatial.context import SpatialContext

_METHOD = "barrier_walking_surface"
_METHOD_VERSION = "0.1"


def barrier_walking_surface(ctx: SpatialContext, spec: dict[str, Any]) -> None:
    slot = spec["target_slot"]
    max_distance = float(spec.get("max_plan_distance", 0.30))
    tolerance = float(spec.get("floor_tolerance", 0.05))
    below = float(spec.get("max_floor_below_base", 1.0))
    quantities = spec.get("quantities") or {}
    quantity = quantities.get("height_above_walking_surface")
    for subject in ctx.nodes_matching(spec["subject"]):
        barrier = ctx.geo(subject)
        if barrier is None:
            continue
        floors: list[tuple[Any, float]] = []
        for candidate in ctx.index.near(barrier.plan, max_distance):
            node = ctx.node_of(candidate)
            if node is None or node is subject or not ctx.matches(node, spec["object"]):
                continue
            floor = candidate.z_min
            if not barrier.z_min - below <= floor <= barrier.z_min + tolerance:
                continue
            if candidate.z_max <= barrier.z_min + tolerance:
                continue
            ctx.relate(subject, slot, node, "geometry")
            floors.append((node, floor))
        if not floors or quantity is None:
            continue
        worst_space, worst_floor = max(floors, key=lambda item: item[1])
        height = barrier.z_max - worst_floor
        point = barrier.plan.centroid
        line = shapely.linestrings(
            [[point.x, point.y, worst_floor], [point.x, point.y, barrier.z_max]]
        )
        ctx.add_measurement(
            [subject, worst_space],
            [("height_above_walking_surface", height, quantity["unit"])],
            method=_METHOD,
            method_version=_METHOD_VERSION,
            inputs=[space for space, _ in floors],
            line_wkt=shapely.to_wkt(line, rounding_precision=3),
        )
