"""Plan-view spatial index over element footprints with vertical range filters."""

from __future__ import annotations

from typing import Iterable

import shapely
from shapely.geometry.base import BaseGeometry
from shapely.strtree import STRtree

from pragmatic_bim.ifc2rdf.geometry.shapes import ElementGeometry


class SpatialIndex:
    def __init__(self, geometries: Iterable[ElementGeometry]) -> None:
        self.items = sorted(geometries, key=lambda g: g.global_id)
        self._tree = STRtree([g.plan for g in self.items]) if self.items else None

    def near(self, shape: BaseGeometry, distance: float = 0.0) -> list[ElementGeometry]:
        """Elements whose plan lies within ``distance`` of ``shape`` (ordered by GlobalId)."""
        if self._tree is None:
            return []
        if distance > 0:
            hits = self._tree.query(shape, predicate="dwithin", distance=distance)
        else:
            hits = self._tree.query(shape, predicate="intersects")
        return [self.items[i] for i in sorted(hits)]

    @staticmethod
    def z_overlap(a: ElementGeometry, b: ElementGeometry) -> float:
        return min(a.z_max, b.z_max) - max(a.z_min, b.z_min)

    @staticmethod
    def plan_distance(a: ElementGeometry, b: ElementGeometry) -> float:
        return float(shapely.distance(a.plan, b.plan))
