"""``door_opens_in_escape_direction``: swing leaf opens with escape travel through the door.

Runs after ``escape_route``. For each swing door on a route, compares the travel
direction (door centre → next portal, or from the upstream space through an exit)
with the door's local +Y from ``ObjectPlacement``. IFC swing doors open into the
local +Y half-space.
"""

from __future__ import annotations

from typing import Any

import ifcopenshell.util.placement
import numpy as np

from pragmatic_bim.ifc2rdf.model import Node
from pragmatic_bim.ifc2rdf.spatial.context import SpatialContext


def door_opens_in_escape_direction(ctx: SpatialContext, spec: dict[str, Any]) -> None:
    slot = spec["target_slot"]
    swing_types = {str(t).upper() for t in spec.get("swing_operation_types") or ()}
    doors = ctx.nodes_matching(spec["subject"])
    upstream = _upstream_spaces(ctx, doors)

    for door in doors:
        operation = getattr(door.entity, "OperationType", None)
        if operation is None or str(operation).upper() not in swing_types:
            continue
        if door.iri not in upstream and not (door.values.get("escape_route_next") or ()):
            continue
        travel = _travel_direction(ctx, door, upstream)
        local_y = _local_y(door)
        if travel is None or local_y is None:
            continue
        opens = bool(np.dot(travel, local_y) > 0)
        if ctx.conv.writer.set(door, slot, opens):
            ctx.conv.report.computed_relations[f"{slot} ({spec['method']})"] += 1


def _upstream_spaces(ctx: SpatialContext, doors: list[Node]) -> dict[Any, list[Node]]:
    """Spaces (and doors) whose ``escape_route_next`` points at each door."""
    door_iris = {door.iri for door in doors}
    result: dict[Any, list[Node]] = {door.iri: [] for door in doors}
    for node in ctx.conv.sorted_nodes():
        for nxt in node.values.get("escape_route_next") or ():
            if nxt in door_iris:
                result[nxt].append(node)
    return result


def _travel_direction(ctx: SpatialContext, door: Node, upstream: dict) -> np.ndarray | None:
    """Unit plan vector of escape travel through the door."""
    geometry = ctx.geo(door)
    if geometry is None:
        return None
    origin = np.array(geometry.plan.centroid.coords[0], dtype=float)
    next_iris = door.values.get("escape_route_next") or ()
    if next_iris:
        nxt = ctx.conv.by_iri.get(next_iris[0])
        nxt_geo = ctx.geo(nxt) if nxt is not None else None
        if nxt_geo is None:
            return None
        target = np.array(nxt_geo.plan.centroid.coords[0], dtype=float)
    else:
        sources = upstream.get(door.iri) or []
        if not sources:
            return None
        # Exit: leave through the door away from the upstream space/door.
        source_geo = ctx.geo(sources[0])
        if source_geo is None:
            return None
        source = np.array(source_geo.plan.centroid.coords[0], dtype=float)
        target = origin + (origin - source)
    delta = target[:2] - origin[:2]
    norm = np.linalg.norm(delta)
    if norm < 1e-9:
        return None
    return delta / norm


def _local_y(door: Node) -> np.ndarray | None:
    """Unit plan vector of the door's local +Y (opening side) in project coordinates."""
    placement = getattr(door.entity, "ObjectPlacement", None)
    if placement is None:
        return None
    matrix = ifcopenshell.util.placement.get_local_placement(placement)
    axis = np.array(matrix[:2, 1], dtype=float)
    norm = np.linalg.norm(axis)
    if norm < 1e-9:
        return None
    return axis / norm
