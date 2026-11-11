"""Relations and quantities computed from geometry, configured in ``_computed_relations.yaml``.

Each entry under ``computed_relations`` names a ``method``; entries run in file order
after the IFC relationships, so geometric fallbacks see what IFC already stated.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Callable

from pragmatic_bim.ifc2rdf.geometry import GeometryResult
from pragmatic_bim.ifc2rdf.spatial.contacts import side_contact, vertical_contact
from pragmatic_bim.ifc2rdf.spatial.context import SpatialContext
from pragmatic_bim.ifc2rdf.spatial.escape import escape_route
from pragmatic_bim.ifc2rdf.spatial.guards import barrier_walking_surface
from pragmatic_bim.ifc2rdf.spatial.hosted_by import opening_in_host
from pragmatic_bim.ifc2rdf.spatial.intersects import prism_overlap
from pragmatic_bim.ifc2rdf.spatial.lights import window_daylight
from pragmatic_bim.ifc2rdf.spatial.neighbours import neighbour_distance
from pragmatic_bim.ifc2rdf.spatial.representations import add_geometry_records

if TYPE_CHECKING:
    from pragmatic_bim.ifc2rdf.pipeline import Converter

METHODS: dict[str, Callable[[SpatialContext, dict], None]] = {
    "opening_in_host": opening_in_host,
    "vertical_contact": vertical_contact,
    "side_contact": side_contact,
    "prism_overlap": prism_overlap,
    "barrier_walking_surface": barrier_walking_surface,
    "window_daylight": window_daylight,
    "escape_route": escape_route,
    "neighbour_distance": neighbour_distance,
}


def compute(conv: "Converter", geometry: GeometryResult, source_name: str) -> None:
    """Write geometry records, then every configured computed relation."""
    ctx = SpatialContext(conv, geometry)
    add_geometry_records(ctx, source_name)
    for name, spec in conv.mapping.computed_relations.items():
        if not isinstance(spec, dict) or "method" not in spec:
            continue
        method = METHODS.get(spec["method"])
        if method is None:
            conv.report.unsupported_sources[f"computed relation {name}: {spec['method']}"] += 1
            continue
        method(ctx, spec)


__all__ = ["METHODS", "SpatialContext", "compute"]
