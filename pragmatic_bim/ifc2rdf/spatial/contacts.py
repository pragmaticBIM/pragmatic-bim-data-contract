"""Element-to-element contact: ``vertical_contact`` (rests_on) and ``side_contact``."""

from __future__ import annotations

from typing import Any

import shapely

from pragmatic_bim.ifc2rdf.geometry import ElementGeometry
from pragmatic_bim.ifc2rdf.spatial.context import SpatialContext


def vertical_contact(ctx: SpatialContext, spec: dict[str, Any]) -> None:
    """Subject rests on object: its bottom bears on the object's upper part."""
    slot = spec["target_slot"]
    tolerance = float(spec.get("contact_tolerance", 0.02))
    min_area = float(spec.get("min_contact_area", 0.01))
    for subject in ctx.nodes_matching(spec["subject"]):
        upper = ctx.geo(subject)
        if upper is None:
            continue
        for candidate in ctx.index.near(upper.plan):
            node = ctx.node_of(candidate)
            if node is None or node is subject or not ctx.matches(node, spec["object"]):
                continue
            if bears_on(upper, candidate, tolerance) and _plan_overlap(upper, candidate) >= min_area:
                ctx.relate(subject, slot, node, "geometry")


def side_contact(ctx: SpatialContext, spec: dict[str, Any]) -> None:
    """Symmetric contact between elements standing side by side."""
    slot = spec["target_slot"]
    max_distance = float(spec.get("max_plan_distance", 0.01))
    min_height = float(spec.get("min_overlap_height", 0.10))
    for subject in ctx.nodes_matching(spec["subject"]):
        geometry = ctx.geo(subject)
        if geometry is None:
            continue
        bearing = set(subject.values.get("rests_on") or [])
        for candidate in ctx.index.near(geometry.plan, max_distance):
            node = ctx.node_of(candidate)
            if node is None or node is subject or not ctx.matches(node, spec["object"]):
                continue
            if node.iri in bearing or subject.iri in (node.values.get("rests_on") or []):
                continue
            if ctx.index.z_overlap(geometry, candidate) < min_height:
                continue
            ctx.relate(subject, slot, node, "geometry")
            ctx.relate(node, slot, subject, "geometry")


def bears_on(upper: ElementGeometry, lower: ElementGeometry, tolerance: float) -> bool:
    return (
        lower.z_min + tolerance <= upper.z_min <= lower.z_max + tolerance
        and upper.z_max > lower.z_max + tolerance
    )


def _plan_overlap(a: ElementGeometry, b: ElementGeometry) -> float:
    return float(shapely.area(shapely.intersection(a.plan, b.plan)))
