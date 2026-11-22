"""Select TerrainSurface nodes and build meshes for height measurements."""

from __future__ import annotations

from typing import TYPE_CHECKING

from pragmatic_bim.ifc2rdf.geometry.terrain import TerrainMesh, terrain_mesh_from_geometry
from pragmatic_bim.ifc2rdf.model import Node

if TYPE_CHECKING:
    from pragmatic_bim.ifc2rdf.spatial.context import SpatialContext


def build_terrain_meshes(ctx: "SpatialContext") -> dict[int, TerrainMesh]:
    """Build terrain meshes for every ``TerrainSurface`` that has geometry."""
    meshes: dict[int, TerrainMesh] = {}
    for node in ctx.nodes_matching({"contract_class": "TerrainSurface"}):
        geo = ctx.geo(node)
        if geo is None or node.entity is None:
            continue
        mesh = terrain_mesh_from_geometry(geo)
        if mesh is not None:
            meshes[node.entity.id()] = mesh
    return meshes


def pick_terrain(ctx: "SpatialContext") -> Node | None:
    """Prefer a projected terrain surface; otherwise the first existing one."""
    nodes = ctx.nodes_matching({"contract_class": "TerrainSurface"})
    projected = [n for n in nodes if _status(n) == "projected"]
    if projected:
        return sorted(projected, key=lambda n: n.global_id)[0]
    existing = [n for n in nodes if _status(n) == "existing"]
    if existing:
        return sorted(existing, key=lambda n: n.global_id)[0]
    return sorted(nodes, key=lambda n: n.global_id)[0] if nodes else None


def _status(node: Node) -> str | None:
    values = node.values.get("terrain_surface_status") or []
    if not values:
        return None
    text = str(values[0])
    if text.endswith("projected"):
        return "projected"
    if text.endswith("existing"):
        return "existing"
    return None


__all__ = ["TerrainMesh", "build_terrain_meshes", "pick_terrain"]
