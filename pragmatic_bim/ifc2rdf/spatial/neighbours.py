"""``neighbour_distance``: clear horizontal and vertical distance to nearby physical elements."""

from __future__ import annotations

from typing import Any

from pragmatic_bim.ifc2rdf.geometry import ElementGeometry
from pragmatic_bim.ifc2rdf.spatial.context import SpatialContext


def neighbour_distance(ctx: SpatialContext, spec: dict[str, Any]) -> None:
    """One ``NeighbourDistance`` record per object within both distance limits, on the subject."""
    slot = spec["target_slot"]
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
            added = ctx.conv.writer.add_inlined(subject, slot, "NeighbourDistance", {
                "neighbour": str(node.iri),
                "horizontal_clear_distance": round(ctx.index.plan_distance(geometry, candidate), 3),
                "vertical_clear_distance": round(vertical, 3),
            })
            if added:
                ctx.conv.report.computed_relations[f"{slot} (geometry)"] += 1


def vertical_gap(a: ElementGeometry, b: ElementGeometry) -> float:
    return max(0.0, b.z_min - a.z_max, a.z_min - b.z_max)
