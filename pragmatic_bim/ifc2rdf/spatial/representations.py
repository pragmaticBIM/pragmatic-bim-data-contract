"""Geometry records per node: ``geometry_representations`` and the bounding-box height."""

from __future__ import annotations

import shapely

from pragmatic_bim.ifc2rdf.geometry import ElementGeometry
from pragmatic_bim.ifc2rdf.spatial.context import SpatialContext


def add_geometry_records(ctx: SpatialContext, source_name: str) -> None:
    """Write one record per representation kind the entity block asks for (``geometry``).

    ``body_3d`` points at the GLB node (or the IFC product when no GLB is written);
    ``footprint_2d`` carries the plan outline as WKT. Both carry the bounding box.
    """
    config = ctx.conv.mapping.computed_relations.get("geometry") or {}
    formats = config.get("representations") or {}
    height = (config.get("quantities") or {}).get("height")
    glb = ctx.geometry.glb_path.name if ctx.geometry.glb_path else None
    for node in ctx.conv.sorted_nodes():
        geometry = ctx.geo(node)
        if geometry is None:
            continue
        spec = node.mapping.block.get("geometry") or {}
        for kind in (spec.get("primary"), spec.get("secondary")):
            entry = _entry(kind, geometry, formats, glb, source_name)
            if entry is not None:
                ctx.conv.writer.add_inlined(node, "geometry_representations", "GeometryRepresentation", entry)
        if height is not None:
            ctx.add_quantity(node, "height", geometry.height, height["unit"])


def _entry(kind, geometry: ElementGeometry, formats: dict, glb: str | None, source_name: str) -> dict | None:
    pointer = f"#{geometry.global_id}"
    if kind == "body_3d" and formats.get("body_3d"):
        entry = {
            "geometry_representation": "body_3d",
            "geometry_reference": (glb or source_name) + pointer,
            "geometry_format": formats["body_3d"] if glb else "ifc",
        }
    elif kind == "footprint_2d" and formats.get("footprint_2d") and geometry.footprint is not None:
        entry = {
            "geometry_representation": "footprint_2d",
            "geometry_reference": source_name + pointer,
            "geometry_format": formats["footprint_2d"],
            "geometry_wkt": shapely.to_wkt(geometry.footprint, rounding_precision=4),
        }
    else:
        return None
    for axis, low, high in zip("xyz", geometry.bbox_min, geometry.bbox_max):
        entry[f"bbox_min_{axis}"] = round(float(low), 4)
        entry[f"bbox_max_{axis}"] = round(float(high), 4)
    return entry
