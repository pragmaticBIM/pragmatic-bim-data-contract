"""One pass over IFC body geometry: world-coordinate meshes per product and an optional GLB."""

from __future__ import annotations

import os
from collections import Counter
from dataclasses import dataclass, field
from functools import cached_property
from pathlib import Path
from typing import Iterable

import ifcopenshell
import ifcopenshell.geom
import numpy as np
import shapely
from shapely.geometry import MultiPolygon, Polygon
from shapely.geometry.base import BaseGeometry

_AREA_EPSILON = 1e-9
_CLEAN_DISTANCE = 1e-6


@dataclass
class ElementGeometry:
    """Triangulated body of one product in project coordinates (metres)."""

    id: int
    global_id: str
    ifc_class: str
    verts: np.ndarray
    """``(n, 3)`` vertex coordinates."""
    faces: np.ndarray
    """``(m, 3)`` vertex indices per triangle."""

    @cached_property
    def bbox_min(self) -> np.ndarray:
        return self.verts.min(axis=0)

    @cached_property
    def bbox_max(self) -> np.ndarray:
        return self.verts.max(axis=0)

    @property
    def z_min(self) -> float:
        return float(self.bbox_min[2])

    @property
    def z_max(self) -> float:
        return float(self.bbox_max[2])

    @property
    def height(self) -> float:
        return self.z_max - self.z_min

    @cached_property
    def footprint(self) -> BaseGeometry | None:
        """Plan outline: union of the triangles projected to XY (None when degenerate)."""
        if not len(self.faces):
            return None
        triangles = shapely.polygons(self.verts[self.faces][:, :, :2])
        triangles = triangles[shapely.area(triangles) > _AREA_EPSILON]
        if not len(triangles):
            return None
        merged = shapely.union_all(triangles).buffer(_CLEAN_DISTANCE).buffer(-_CLEAN_DISTANCE)
        merged = shapely.simplify(merged, 10 * _CLEAN_DISTANCE)
        if merged.is_empty:
            return None
        if isinstance(merged, (Polygon, MultiPolygon)):
            return merged
        polygons = [g for g in getattr(merged, "geoms", []) if isinstance(g, Polygon)]
        return MultiPolygon(polygons) if polygons else None

    @cached_property
    def plan_box(self) -> Polygon:
        """Axis-aligned plan rectangle, a cheap stand-in when the footprint is degenerate."""
        (x0, y0), (x1, y1) = self.bbox_min[:2], self.bbox_max[:2]
        return shapely.box(x0, y0, max(x1, x0 + _CLEAN_DISTANCE), max(y1, y0 + _CLEAN_DISTANCE))

    @property
    def plan(self) -> BaseGeometry:
        return self.footprint if self.footprint is not None else self.plan_box


@dataclass
class GeometryResult:
    geometries: dict[int, ElementGeometry] = field(default_factory=dict)
    failures: Counter = field(default_factory=Counter)
    """IFC class → products with a representation but no tessellated body."""
    glb_path: Path | None = None


def geometry_settings() -> ifcopenshell.geom.settings:
    settings = ifcopenshell.geom.settings()
    settings.set("use-world-coords", True)
    return settings


def run_geometry_pass(
    ifc_file: ifcopenshell.file,
    products: Iterable[ifcopenshell.entity_instance],
    *,
    glb_path: Path | str | None = None,
    threads: int | None = None,
) -> GeometryResult:
    """Tessellate ``products`` once; feed each shape to the GLB serializer and keep its mesh.

    GLB nodes are named after the product GlobalId (``use-element-guids``).
    """
    result = GeometryResult()
    wanted = [p for p in products if getattr(p, "Representation", None) is not None]
    if not wanted:
        return result
    settings = geometry_settings()
    serializer = None
    if glb_path is not None:
        result.glb_path = Path(glb_path)
        result.glb_path.parent.mkdir(parents=True, exist_ok=True)
        serializer_settings = ifcopenshell.geom.serializer_settings()
        serializer_settings.set("use-element-guids", True)
        serializer = ifcopenshell.geom.serializers.gltf(str(result.glb_path), settings, serializer_settings)
        serializer.setFile(ifc_file)
        serializer.setUnitNameAndMagnitude("METER", 1.0)
        serializer.writeHeader()
    iterator = ifcopenshell.geom.iterator(
        settings, ifc_file, threads or os.cpu_count() or 1, include=wanted
    )
    if iterator.initialize():
        while True:
            shape = iterator.get()
            if serializer is not None:
                serializer.write(shape)
            verts = np.asarray(shape.geometry.verts, dtype=float).reshape(-1, 3)
            faces = np.asarray(shape.geometry.faces, dtype=int).reshape(-1, 3)
            if len(verts):
                product = ifc_file.by_id(shape.id)
                result.geometries[shape.id] = ElementGeometry(
                    id=shape.id,
                    global_id=product.GlobalId,
                    ifc_class=product.is_a(),
                    verts=verts,
                    faces=faces,
                )
            if not iterator.next():
                break
    if serializer is not None:
        serializer.finalize()
    for product in wanted:
        if product.id() not in result.geometries:
            result.failures[product.is_a()] += 1
    return result
