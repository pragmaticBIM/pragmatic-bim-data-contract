"""Height measurements against the ground floor and against terrain surfaces."""

from __future__ import annotations

from typing import Any

import shapely
from shapely.geometry.base import BaseGeometry

from pragmatic_bim.ifc2rdf.geometry import ElementGeometry
from pragmatic_bim.ifc2rdf.model import Node
from pragmatic_bim.ifc2rdf.spatial.context import SpatialContext
from pragmatic_bim.ifc2rdf.spatial.terrain import TerrainMesh, build_terrain_meshes, pick_terrain

_GROUND_METHOD = "height_above_ground_floor"
_GROUND_VERSION = "0.1"
_TERRAIN_METHOD = "height_above_terrain"
_TERRAIN_VERSION = "0.1"


def height_above_ground_floor(ctx: SpatialContext, spec: dict[str, Any]) -> None:
    """``DerivedMeasurement`` from element reference height minus ground-floor elevation."""
    quantity = (spec.get("quantities") or {}).get("height_above_ground_floor") or {"unit": "m"}
    ground_by_building = _ground_floors(ctx)
    for subject_spec in spec.get("subjects") or []:
        reference = subject_spec.get("reference", "bottom")
        for subject in ctx.nodes_matching(_selector(subject_spec)):
            ground = _ground_for(subject, ground_by_building)
            geo = ctx.geo(subject)
            if ground is None:
                ctx.add_measurement(
                    [subject],
                    quantities=(),
                    method=_GROUND_METHOD,
                    method_version=_GROUND_VERSION,
                    status="not_measurable",
                )
                continue
            if geo is None:
                ctx.add_measurement(
                    [subject, ground],
                    quantities=(),
                    method=_GROUND_METHOD,
                    method_version=_GROUND_VERSION,
                    inputs=[ground],
                    status="not_measurable",
                )
                continue
            elev = _elevation(ground)
            if elev is None:
                ctx.add_measurement(
                    [subject, ground],
                    quantities=(),
                    method=_GROUND_METHOD,
                    method_version=_GROUND_VERSION,
                    inputs=[ground],
                    status="not_measurable",
                )
                continue
            ref_z = geo.z_max if reference == "top" else geo.z_min
            height = ref_z - elev
            point = geo.plan.centroid
            line = shapely.linestrings([[point.x, point.y, elev], [point.x, point.y, ref_z]])
            ctx.add_measurement(
                [subject, ground],
                [("height_above_ground_floor", height, quantity["unit"])],
                method=_GROUND_METHOD,
                method_version=_GROUND_VERSION,
                inputs=[ground],
                line_wkt=shapely.to_wkt(line, rounding_precision=3),
                allow_negative=True,
            )


def height_above_terrain(ctx: SpatialContext, spec: dict[str, Any]) -> None:
    """``DerivedMeasurement`` from element reference height minus sampled terrain height."""
    quantity = (spec.get("quantities") or {}).get("height_above_terrain") or {"unit": "m"}
    buffer = float(spec.get("outside_buffer", 1.0))
    meshes = build_terrain_meshes(ctx)
    terrain_node = pick_terrain(ctx)
    for subject_spec in spec.get("subjects") or []:
        reference = subject_spec.get("reference", "bottom")
        sample = subject_spec.get("sample", "lowest_outside")
        for subject in ctx.nodes_matching(_selector(subject_spec)):
            geo = ctx.geo(subject)
            if terrain_node is None or not meshes or geo is None:
                subjects = [subject] if terrain_node is None else [subject, terrain_node]
                ctx.add_measurement(
                    subjects,
                    quantities=(),
                    method=_TERRAIN_METHOD,
                    method_version=_TERRAIN_VERSION,
                    inputs=[terrain_node] if terrain_node is not None else (),
                    status="not_measurable",
                )
                continue
            mesh = meshes.get(terrain_node.entity.id()) if terrain_node.entity is not None else None
            if mesh is None:
                mesh = next(iter(meshes.values()), None)
            sample_result = _sample_terrain(mesh, geo, sample, buffer) if mesh is not None else None
            if sample_result is None:
                ctx.add_measurement(
                    [subject, terrain_node],
                    quantities=(),
                    method=_TERRAIN_METHOD,
                    method_version=_TERRAIN_VERSION,
                    inputs=[terrain_node],
                    status="not_measurable",
                )
                continue
            sx, sy, sz = sample_result
            ref_z = geo.z_max if reference == "top" else geo.z_min
            height = ref_z - sz
            line = shapely.linestrings([[sx, sy, sz], [sx, sy, ref_z]])
            ctx.add_measurement(
                [subject, terrain_node],
                [("height_above_terrain", height, quantity["unit"])],
                method=_TERRAIN_METHOD,
                method_version=_TERRAIN_VERSION,
                inputs=[terrain_node],
                line_wkt=shapely.to_wkt(line, rounding_precision=3),
                allow_negative=True,
            )


def _selector(subject_spec: dict[str, Any]) -> dict[str, Any]:
    return {k: v for k, v in subject_spec.items() if k in ("contract_class", "ifc_class", "property", "exclude_property")}


def _ground_floors(ctx: SpatialContext) -> dict[Any, Node]:
    result: dict[Any, Node] = {}
    for level in ctx.nodes_matching({"contract_class": "LevelContext"}):
        if _slot_bool(level, "is_ground_floor") is not True:
            continue
        building = _parent_building(level)
        result[building] = level
    return result


def _ground_for(subject: Node, ground_by_building: dict[Any, Node]) -> Node | None:
    building = _parent_building(subject)
    if building in ground_by_building:
        return ground_by_building[building]
    if len(ground_by_building) == 1:
        return next(iter(ground_by_building.values()))
    return None


def _parent_building(node: Node) -> Any:
    parents = node.values.get("parent_building") or []
    return parents[0] if parents else None


def _elevation(level: Node) -> float | None:
    values = level.values.get("elevation") or []
    if not values:
        return None
    return float(values[0].toPython())


def _slot_bool(node: Node, slot: str) -> bool | None:
    values = node.values.get(slot) or []
    if not values:
        return None
    return bool(values[0].toPython())


def _sample_terrain(
    mesh: TerrainMesh, geo: ElementGeometry, sample: str, buffer: float
) -> tuple[float, float, float] | None:
    plan: BaseGeometry = geo.plan
    if sample == "under_footprint":
        point = plan.centroid
        height = mesh.height_at(point.x, point.y)
        if height is None:
            return None
        return float(point.x), float(point.y), height
    # lowest_outside: sample points along the buffered ring and pick the lowest terrain
    ring = plan.buffer(buffer).boundary
    if ring.is_empty:
        return None
    length = float(ring.length)
    if length <= 0:
        return None
    step = max(length / 16.0, 0.25)
    best: tuple[float, float, float] | None = None
    distance = 0.0
    while distance <= length + 1e-9:
        point = ring.interpolate(min(distance, length))
        height = mesh.height_at(point.x, point.y)
        if height is not None and (best is None or height < best[2]):
            best = (float(point.x), float(point.y), height)
        distance += step
    return best


__all__ = ["height_above_ground_floor", "height_above_terrain"]
