"""Geometry stage: tessellate once, export GLB, index footprints (requires the ``geometry`` extra)."""

from __future__ import annotations

from pragmatic_bim.ifc2rdf.geometry.index import SpatialIndex
from pragmatic_bim.ifc2rdf.geometry.shapes import ElementGeometry, GeometryResult, run_geometry_pass

__all__ = ["ElementGeometry", "GeometryResult", "SpatialIndex", "run_geometry_pass"]
