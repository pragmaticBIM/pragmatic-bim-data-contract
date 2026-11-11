"""``barrier_walking_surface``: safety barrier → spaces whose floor it protects, plus its height.

A space qualifies when its plan lies within ``max_plan_distance`` of the barrier and its
floor (space bottom) lies between ``barrier base - max_floor_below_base`` and
``barrier base + floor_tolerance``. The barrier height above the walking surface is
measured against the highest qualifying floor (worst case).
"""

from __future__ import annotations

from typing import Any

from pragmatic_bim.ifc2rdf.spatial.context import SpatialContext


def barrier_walking_surface(ctx: SpatialContext, spec: dict[str, Any]) -> None:
    slot = spec["target_slot"]
    max_distance = float(spec.get("max_plan_distance", 0.30))
    tolerance = float(spec.get("floor_tolerance", 0.05))
    below = float(spec.get("max_floor_below_base", 1.0))
    quantities = spec.get("quantities") or {}
    for subject in ctx.nodes_matching(spec["subject"]):
        barrier = ctx.geo(subject)
        if barrier is None:
            continue
        floors = []
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
            floors.append(floor)
        quantity = quantities.get("height_above_walking_surface")
        if floors and quantity is not None:
            ctx.add_quantity(subject, "height_above_walking_surface", barrier.z_max - max(floors), quantity["unit"])
