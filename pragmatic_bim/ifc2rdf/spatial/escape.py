"""``escape_route``: shortest horizontal escape route through the spaces, door to door.

Doors connect the spaces they open into (IFC ``connects_spaces``, else spaces within
``max_door_distance``). A route ends at an exit (an external door on the lowest exit level)
or, on storeys without an exit, at a stair that leaves the storey. Inside a space the walking
distance is the shortest path in plan around the corners of the space outline. Each door gets
the next door or stair on its route and the remaining length; each space gets the door it is
left through and the length from its most remote point on the outline.
"""

from __future__ import annotations

import heapq
import itertools
from dataclasses import dataclass, field
from typing import Any

import ifcopenshell.geom
import numpy as np
import shapely
from shapely.geometry.base import BaseGeometry
from shapely.ops import nearest_points

from pragmatic_bim.ifc2rdf.geometry import ElementGeometry
from pragmatic_bim.ifc2rdf.geometry.shapes import geometry_settings
from pragmatic_bim.ifc2rdf.model import Node
from pragmatic_bim.ifc2rdf.spatial.context import SpatialContext

_SIMPLIFY = 0.02
_STAIR_MIN_AREA = 0.05
_FLOOR_TOLERANCE = 0.3


class PlanRegion:
    """Shortest walking paths inside a plan outline; paths bend only at its corners."""

    def __init__(self, shape: BaseGeometry, tolerance: float = 1e-3) -> None:
        self.shape = shape
        self.region = shape.buffer(tolerance)
        shapely.prepare(self.region)
        rings = [p.exterior for p in _polygons(shape)] + [r for p in _polygons(shape) for r in p.interiors]
        corners = np.unique(np.concatenate([np.asarray(r.coords)[:-1] for r in rings]), axis=0)
        self.corners = corners
        self._corner_paths = self._edges(corners, corners)

    def _edges(self, a: np.ndarray, b: np.ndarray) -> np.ndarray:
        """Straight distance between every point of ``a`` and of ``b``; inf where the segment leaves the region."""
        if not len(a) or not len(b):
            return np.full((len(a), len(b)), np.inf)
        pairs = np.stack(np.broadcast_arrays(a[:, None, :], b[None, :, :]), axis=2)
        distance = np.linalg.norm(pairs[:, :, 0] - pairs[:, :, 1], axis=2)
        lines = shapely.linestrings(pairs.reshape(-1, 2, 2))
        visible = shapely.covers(self.region, lines).reshape(distance.shape) | (distance < 1e-9)
        return np.where(visible, distance, np.inf)

    def _from(self, source: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
        """Walking distance from ``source`` to every corner, and the corner each is reached through (-1: direct)."""
        to_corner = self._edges(source, self.corners)[0]
        previous = np.full(len(self.corners), -1)
        done = np.zeros(len(self.corners), dtype=bool)
        for _ in range(len(self.corners)):
            open_ = np.where(done, np.inf, to_corner)
            nearest = int(np.argmin(open_))
            if not np.isfinite(open_[nearest]):
                break
            done[nearest] = True
            via = to_corner[nearest] + self._corner_paths[nearest]
            shorter = via < to_corner
            to_corner = np.where(shorter, via, to_corner)
            previous[shorter] = nearest
        return to_corner, previous

    def distances(self, source: np.ndarray, points: np.ndarray) -> np.ndarray:
        """Walking distance from ``source`` to each of ``points`` (inf when unreachable)."""
        source = np.asarray(source, dtype=float).reshape(1, 2)
        points = np.asarray(points, dtype=float).reshape(-1, 2)
        to_corner, _ = self._from(source)
        direct = self._edges(source, points)[0]
        via = (to_corner[:, None] + self._edges(self.corners, points)).min(axis=0, initial=np.inf)
        return np.minimum(direct, via)

    def path(self, source: np.ndarray, target: np.ndarray) -> np.ndarray:
        """Points of the shortest walk from ``source`` to ``target`` (a straight line when unreachable)."""
        source = np.asarray(source, dtype=float).reshape(1, 2)
        target = np.asarray(target, dtype=float).reshape(1, 2)
        to_corner, previous = self._from(source)
        direct = self._edges(source, target)[0, 0]
        via = to_corner + self._edges(self.corners, target)[:, 0]
        corner = int(np.argmin(via)) if len(via) else -1
        if corner < 0 or not np.isfinite(via[corner]) or direct <= via[corner]:
            return np.vstack([source, target])
        chain = []
        while corner >= 0:
            chain.append(self.corners[corner])
            corner = int(previous[corner])
        return np.vstack([source, *reversed(chain), target])

    @staticmethod
    def outline_points(shape: BaseGeometry, spacing: float) -> np.ndarray:
        """Corners of the outline plus points every ``spacing`` metres along it."""
        rings = [shapely.segmentize(p.exterior, spacing) for p in _polygons(shape)]
        return np.concatenate([np.asarray(r.coords)[:-1] for r in rings])


@dataclass
class _Portal:
    """A door or stair as seen from one zone: where it is reached and the step from there to the element."""

    key: tuple
    node: Node
    point: np.ndarray
    offset: float
    centre: np.ndarray
    """Plan position of the element itself (door centre, stair landing point)."""
    z: float


@dataclass
class _Zone:
    """Spaces with no wall between them (open plan), walked as one region."""

    spaces: list[Node]
    geometries: list[ElementGeometry]
    outlines: list[BaseGeometry]
    region: PlanRegion
    portals: list[_Portal] = field(default_factory=list)

    @property
    def floor(self) -> float:
        return min(geometry.z_min for geometry in self.geometries)

    @property
    def levels(self) -> set:
        return {level for space in self.spaces for level in space.values.get("parent_level") or ()}


def escape_route(ctx: SpatialContext, spec: dict[str, Any]) -> None:
    slot = spec["target_slot"]
    name = spec.get("name", "escape_route")
    quantity = (spec.get("quantities") or {}).get("escape_route_length")
    spacing = float(spec.get("boundary_sample_spacing", 0.5))

    spaces = [(node, ctx.geo(node)) for node in ctx.nodes_matching(spec["subject"])]
    spaces = [(node, geometry) for node, geometry in spaces if geometry is not None and geometry.footprint is not None]
    if not spaces:
        return
    zones = _open_zones(spaces, float(spec.get("max_open_gap", 0.05)), float(spec.get("min_open_width", 0.6)))
    zone_of = {space.iri: zone for zone in zones for space in zone.spaces}

    exits = _lowest_exits(ctx, spec)
    exit_levels = {level for door in exits for level in door.values.get("parent_level") or ()}
    targets = {("door", door.iri) for door in exits}

    for door in ctx.nodes_matching(spec["doors"]):
        geometry = ctx.geo(door)
        if geometry is None:
            continue
        centre = geometry.plan.centroid
        door_zones = {id(zone_of[iri]): zone_of[iri] for iri in _door_spaces(ctx, door, geometry, zone_of, spec)}
        for zone in door_zones.values():
            point = nearest_points(zone.region.shape.boundary, centre)[0]
            zone.portals.append(
                _Portal(
                    ("door", door.iri), door, np.array(point.coords[0]), point.distance(centre),
                    np.array(centre.coords[0]), geometry.z_min,
                )
            )

    for stair in ctx.nodes_matching(spec["stairs"]):
        geometry = _stair_geometry(ctx, stair)
        if geometry is None:
            continue
        for zone in zones:
            if exit_levels & zone.levels or not any(_leaves_storey(geometry, g) for g in zone.geometries):
                continue
            overlap = geometry.plan.intersection(zone.region.shape)
            if overlap.area < _STAIR_MIN_AREA:
                continue
            key = ("stair", stair.iri, id(zone))
            point = np.array(overlap.representative_point().coords[0])
            zone.portals.append(_Portal(key, stair, point, 0.0, point, zone.floor))
            targets.add(key)

    distance, following = _shortest_routes(zones, targets)
    elements = {p.key: p.node for zone in zones for p in zone.portals}

    for key, length in sorted(distance.items(), key=lambda item: str(item[0])):
        if key[0] != "door":
            continue
        door = elements[key]
        if key in following:
            ctx.relate(door, slot, elements[following[key][0]], "geometry")
        if quantity is not None:
            ctx.add_quantity(door, "escape_route_length", length, quantity["unit"])

    for zone in zones:
        reachable = [p for p in zone.portals if p.key in distance]
        for space, outline in zip(zone.spaces, zone.outlines):
            route = _remote_route(zone.region, outline, reachable, distance, spacing)
            if route is None:
                ctx.conv.report.computed_relations[f"{slot} (no route)"] += 1
                continue
            portal, length, start = route
            ctx.relate(space, slot, portal.node, "geometry")
            if quantity is not None:
                ctx.add_quantity(space, "escape_route_length", length, quantity["unit"])
            if spec.get("path_representation"):
                points = _route_points(zone, start, portal, following)
                ctx.conv.writer.add_inlined(
                    space,
                    "geometry_representations",
                    "GeometryRepresentation",
                    {
                        "geometry_representation": spec["path_representation"],
                        "geometry_reference": f"{name}#{space.global_id}",
                        "geometry_format": "wkt",
                        "geometry_wkt": shapely.to_wkt(shapely.linestrings(points), rounding_precision=3),
                    },
                )


def _remote_route(
    region: PlanRegion, outline: BaseGeometry, portals: list[_Portal], distance: dict, spacing: float
) -> tuple[_Portal, float, np.ndarray] | None:
    """Route length from the most remote outline point of a space, the portal it leaves through, and the point."""
    if not portals:
        return None
    samples = PlanRegion.outline_points(outline, spacing)
    costs = np.stack([region.distances(p.point, samples) + p.offset + distance[p.key] for p in portals])
    best = costs.min(axis=0)
    if not np.isfinite(best).any():
        return None
    remote = int(np.argmax(np.where(np.isfinite(best), best, -np.inf)))
    return portals[int(np.argmin(costs[:, remote]))], float(best[remote]), samples[remote]


def _route_points(zone: _Zone, start: np.ndarray, portal: _Portal, following: dict) -> np.ndarray:
    """3D polyline from ``start`` in ``zone`` through ``portal`` and every following door to the route end."""
    points = _lift(zone.region.path(start, portal.point), zone.floor)
    points.append([*portal.centre, portal.z])
    key = portal.key
    while key in following:
        via, through = following[key]
        here = _portal(through, key)
        there = _portal(through, via)
        points += _lift(through.region.path(here.point, there.point), through.floor)
        points.append([*there.centre, there.z])
        key = via
    clean = [points[0]]
    for point in points[1:]:
        if np.linalg.norm(np.subtract(point, clean[-1])) > 1e-3:
            clean.append(point)
    return np.array(clean, dtype=float)


def _lift(plan: np.ndarray, z: float) -> list[list[float]]:
    return [[x, y, z] for x, y in plan]


def _portal(zone: _Zone, key: tuple) -> _Portal:
    return next(p for p in zone.portals if p.key == key)


def _open_zones(spaces: list[tuple[Node, ElementGeometry]], gap: float, min_width: float) -> list[_Zone]:
    """Group spaces on the same floor whose outlines touch along at least ``min_width``."""
    outlines = [geometry.footprint.simplify(_SIMPLIFY) for _, geometry in spaces]
    parent = list(range(len(spaces)))

    def root(i: int) -> int:
        while parent[i] != i:
            parent[i] = parent[parent[i]]
            i = parent[i]
        return i

    pairs = shapely.STRtree(outlines).query(outlines, predicate="dwithin", distance=gap)
    for i, j in pairs.T:
        if i >= j or abs(spaces[i][1].z_min - spaces[j][1].z_min) > _FLOOR_TOLERANCE:
            continue
        if outlines[i].buffer(gap).intersection(outlines[j].boundary).length >= min_width:
            parent[root(i)] = root(j)

    groups: dict[int, list[int]] = {}
    for i in range(len(spaces)):
        groups.setdefault(root(i), []).append(i)
    zones = []
    for members in groups.values():
        shape = outlines[members[0]]
        if len(members) > 1:
            shape = shapely.union_all([outlines[k].buffer(gap) for k in members]).buffer(-gap).simplify(_SIMPLIFY)
        zones.append(
            _Zone(
                spaces=[spaces[k][0] for k in members],
                geometries=[spaces[k][1] for k in members],
                outlines=[outlines[k] for k in members],
                region=PlanRegion(shape),
            )
        )
    return zones


def _lowest_exits(ctx: SpatialContext, spec: dict[str, Any]) -> list[Node]:
    """External doors on the lowest exit level; higher ones (balcony doors) do not lead outside."""
    candidates = [(door, ctx.geo(door)) for door in ctx.nodes_matching(spec["exits"])]
    candidates = [(door, geometry) for door, geometry in candidates if geometry is not None]
    if not candidates:
        return []
    lowest = min(geometry.z_min for _, geometry in candidates)
    limit = lowest + float(spec.get("max_exit_above_lowest", 1.5))
    return [door for door, geometry in candidates if geometry.z_min <= limit]


def _door_spaces(
    ctx: SpatialContext, door: Node, geometry: ElementGeometry, spaces: dict, spec: dict[str, Any]
) -> list[Any]:
    """Spaces the door opens into: IFC space boundaries, else spaces next to it."""
    stated = [iri for iri in door.values.get("connects_spaces") or () if iri in spaces]
    if stated:
        return stated
    near = []
    for candidate in ctx.index.near(geometry.plan, float(spec.get("max_door_distance", 0.30))):
        node = ctx.node_of(candidate)
        if node is not None and node.iri in spaces and ctx.index.z_overlap(geometry, candidate) > 0:
            near.append(node.iri)
    return sorted(near, key=str)


def _leaves_storey(stair: ElementGeometry, space: ElementGeometry) -> bool:
    """The stair reaches the space floor and continues to another storey."""
    floor = space.z_min
    if not stair.z_min - _FLOOR_TOLERANCE <= floor <= stair.z_max + _FLOOR_TOLERANCE:
        return False
    return stair.z_min < floor - _FLOOR_TOLERANCE or stair.z_max > floor + 1.0


def _stair_geometry(ctx: SpatialContext, stair: Node) -> ElementGeometry | None:
    """The stair body, or its flights and landings when the stair itself has no representation."""
    geometry = ctx.geo(stair)
    if geometry is not None:
        return geometry
    verts, faces = [], []
    settings = geometry_settings()
    for rel in getattr(stair.entity, "IsDecomposedBy", None) or ():
        for part in rel.RelatedObjects:
            if getattr(part, "Representation", None) is None:
                continue
            try:
                shape = ifcopenshell.geom.create_shape(settings, part)
            except RuntimeError:
                continue
            part_verts = np.asarray(shape.geometry.verts, dtype=float).reshape(-1, 3)
            faces.append(np.asarray(shape.geometry.faces, dtype=int).reshape(-1, 3) + sum(len(v) for v in verts))
            verts.append(part_verts)
    if not verts:
        return None
    return ElementGeometry(
        id=stair.entity.id(),
        global_id=stair.global_id,
        ifc_class=stair.entity.is_a(),
        verts=np.concatenate(verts),
        faces=np.concatenate(faces),
    )


def _shortest_routes(
    zones: list[_Zone], targets: set[tuple]
) -> tuple[dict[tuple, float], dict[tuple, tuple[tuple, _Zone]]]:
    """Dijkstra from all targets over portals; edges are walks through a shared zone.

    ``following`` maps a portal to the next portal on its route and the zone walked through.
    """
    edges: dict[tuple, list[tuple[float, tuple, _Zone]]] = {}
    for zone in zones:
        for i, portal in enumerate(zone.portals):
            others = zone.portals[i + 1 :]
            if not others:
                continue
            walks = zone.region.distances(portal.point, np.array([o.point for o in others]))
            for other, walk in zip(others, walks):
                if not np.isfinite(walk) or other.key == portal.key:
                    continue
                cost = float(walk) + portal.offset + other.offset
                edges.setdefault(portal.key, []).append((cost, other.key, zone))
                edges.setdefault(other.key, []).append((cost, portal.key, zone))

    distance: dict[tuple, float] = {}
    following: dict[tuple, tuple[tuple, _Zone]] = {}
    order = itertools.count()
    queue = [(0.0, str(key), next(order), key, None) for key in targets]
    heapq.heapify(queue)
    while queue:
        cost, _, _, key, via = heapq.heappop(queue)
        if key in distance:
            continue
        distance[key] = cost
        if via is not None:
            following[key] = via
        for step, neighbour, zone in edges.get(key, ()):
            if neighbour not in distance:
                heapq.heappush(queue, (cost + step, str(neighbour), next(order), neighbour, (key, zone)))
    return distance, following


def _polygons(shape: BaseGeometry) -> list:
    return list(getattr(shape, "geoms", [shape]))
