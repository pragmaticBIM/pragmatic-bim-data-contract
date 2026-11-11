"""``prism_overlap``: reserved volume → physical elements that intrude into it.

2.5D test: plan overlap area above ``min_overlap_area`` and vertical overlap above
``min_overlap_height``. Elements that only touch the volume do not count.
"""

from __future__ import annotations

from typing import Any

import shapely

from pragmatic_bim.ifc2rdf.spatial.context import SpatialContext


def prism_overlap(ctx: SpatialContext, spec: dict[str, Any]) -> None:
    slot = spec["target_slot"]
    min_area = float(spec.get("min_overlap_area", 0.01))
    min_height = float(spec.get("min_overlap_height", 0.01))
    for subject in ctx.nodes_matching(spec["subject"]):
        geometry = ctx.geo(subject)
        if geometry is None:
            continue
        skip = _related_products(subject.entity) if spec.get("exclude_related_products") else set()
        for candidate in ctx.index.near(geometry.plan):
            node = ctx.node_of(candidate)
            if node is None or node is subject or candidate.id in skip:
                continue
            if not ctx.matches(node, spec["object"]):
                continue
            if ctx.index.z_overlap(geometry, candidate) < min_height:
                continue
            if float(shapely.area(shapely.intersection(geometry.plan, candidate.plan))) < min_area:
                continue
            ctx.relate(subject, slot, node, "geometry")


def _related_products(entity) -> set[int]:
    """Products the volume is part of, nested in, or assigned to."""
    related: set[int] = set()
    for inverse, attribute in (("Decomposes", "RelatingObject"), ("Nests", "RelatingObject")):
        for rel in getattr(entity, inverse, None) or []:
            target = getattr(rel, attribute, None)
            if target is not None:
                related.add(target.id())
    for rel in getattr(entity, "HasAssignments", None) or []:
        if rel.is_a("IfcRelAssignsToProduct") and rel.RelatingProduct is not None:
            related.add(rel.RelatingProduct.id())
    for rel in getattr(entity, "ReferencedBy", None) or []:
        if rel.is_a("IfcRelAssignsToProduct"):
            related.update(o.id() for o in rel.RelatedObjects or [])
    return related
