"""Geometry stage: tessellate once, export GLB, index footprints (requires the ``geometry`` extra)."""

from __future__ import annotations

from pragmatic_bim.ifc2rdf.geometry.index import SpatialIndex
from pragmatic_bim.ifc2rdf.geometry.shapes import ElementGeometry, GeometryResult, run_geometry_pass
from pragmatic_bim.ifc2rdf.geometry.terrain import TerrainMesh, terrain_height_at, terrain_mesh_from_geometry

__all__ = [
    "ElementGeometry",
    "GeometryResult",
    "SpatialIndex",
    "TerrainMesh",
    "run_geometry_pass",
    "terrain_height_at",
    "terrain_mesh_from_geometry",
]
