"""Terrain surface mesh helpers: triangulated lookup ``terrain_height_at(x, y)``."""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np

from pragmatic_bim.ifc2rdf.geometry.shapes import ElementGeometry


@dataclass
class TerrainMesh:
    """Triangulated terrain surface with XY height lookup."""

    geometry: ElementGeometry
    triangles: np.ndarray
    """``(m, 3, 3)`` triangle vertices."""

    def height_at(self, x: float, y: float) -> float | None:
        """Interpolate Z on the first triangle that contains ``(x, y)``; else None."""
        point = np.array([x, y], dtype=float)
        for tri in self.triangles:
            height = _triangle_height(tri, point)
            if height is not None:
                return float(height)
        return None


def terrain_mesh_from_geometry(geometry: ElementGeometry) -> TerrainMesh | None:
    """Build a ``TerrainMesh`` from an element body; None when there are no faces."""
    if not len(geometry.faces):
        return None
    return TerrainMesh(geometry=geometry, triangles=geometry.verts[geometry.faces])


def terrain_height_at(mesh: TerrainMesh, x: float, y: float) -> float | None:
    """Height of ``mesh`` at a plan point, or None outside the surface."""
    return mesh.height_at(x, y)


def _triangle_height(tri: np.ndarray, point: np.ndarray) -> float | None:
    """Barycentric interpolation; None when the point is outside the triangle."""
    a, b, c = tri[:, :2]
    v0 = c - a
    v1 = b - a
    v2 = point - a
    dot00 = float(np.dot(v0, v0))
    dot01 = float(np.dot(v0, v1))
    dot02 = float(np.dot(v0, v2))
    dot11 = float(np.dot(v1, v1))
    dot12 = float(np.dot(v1, v2))
    denom = dot00 * dot11 - dot01 * dot01
    if abs(denom) < 1e-18:
        return None
    u = (dot11 * dot02 - dot01 * dot12) / denom
    v = (dot00 * dot12 - dot01 * dot02) / denom
    if u < -1e-9 or v < -1e-9 or u + v > 1.0 + 1e-9:
        return None
    w = 1.0 - u - v
    return float(w * tri[0, 2] + v * tri[1, 2] + u * tri[2, 2])


__all__ = ["TerrainMesh", "terrain_mesh_from_geometry", "terrain_height_at"]
