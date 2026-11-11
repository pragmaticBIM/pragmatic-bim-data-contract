"""``opening_in_host``: door or window → wall it sits in, when IFC states no opening chain."""

from __future__ import annotations

from typing import Any

import shapely

from pragmatic_bim.ifc2rdf.spatial.context import SpatialContext


def opening_in_host(ctx: SpatialContext, spec: dict[str, Any]) -> None:
    slot = spec["target_slot"]
    max_distance = float(spec.get("max_plan_distance", 0.05))
    for subject in ctx.nodes_matching(spec["subject"]):
        if spec.get("only_when_unset") and subject.values.get(slot):
            continue
        geometry = ctx.geo(subject)
        if geometry is None:
            continue
        centre = geometry.plan_box.centroid
        best: tuple[int, float, str] | None = None
        host_node = None
        for candidate in ctx.index.near(geometry.plan, max_distance):
            node = ctx.node_of(candidate)
            if node is None or node is subject or not ctx.matches(node, spec["object"]):
                continue
            if ctx.index.z_overlap(geometry, candidate) <= 0:
                continue
            # A straight wall's oriented envelope spans its openings; prefer the host that contains the centre.
            contains = int(not shapely.oriented_envelope(candidate.plan).buffer(max_distance).contains(centre))
            distance = float(shapely.distance(candidate.plan, centre))
            key = (contains, distance, candidate.global_id)
            if best is None or key < best:
                best, host_node = key, node
        if host_node is not None:
            ctx.relate(subject, slot, host_node, "geometry")
