"""Reference identification, geometry output, and computed relations on the demo model."""

from __future__ import annotations

import json
import struct

import pytest
import rdflib
from checks import PBS, REFERENCE_FIXTURE, shacl_violations
from rdflib import RDF
from synthetic import DEMO_GLOBAL_IDS as GID

from pragmatic_bim.ifc2rdf import convert
from pragmatic_bim.ifc2rdf.reference import resolve_reference_path

shapely = pytest.importorskip("shapely")

BASE = "https://data.example.org/demo/"
REF = "https://pragmaticbim.ch/id/element/"


def iri(role: str) -> rdflib.URIRef:
    return rdflib.URIRef(BASE + GID[role])


def objects(graph: rdflib.Graph, role: str, slot: str) -> set:
    return set(graph.objects(iri(role), PBS[slot]))


def quantities(graph: rdflib.Graph, role: str) -> dict[str, float]:
    return {
        str(graph.value(q, PBS.quantity_type)): graph.value(q, PBS.quantity_value).toPython()
        for q in graph.objects(iri(role), PBS.quantity_values)
    }


def quantity(graph: rdflib.Graph, role: str, quantity_type: str) -> float:
    return quantities(graph, role)[str(PBS[f"quantity_type_{quantity_type}"])]


def reference_uris(graph: rdflib.Graph, role: str) -> set[str]:
    return {
        str(graph.value(c, PBS.classification_uri))
        for c in graph.objects(iri(role), PBS.classifications)
        if str(graph.value(c, PBS.classification_scheme)) == "pragmaticbim-element"
    }


def test_conforms_to_contract_shacl(demo, shacl_graph):
    graph, _, _ = demo
    assert shacl_violations(graph, shacl_graph) == []


# --- identification ------------------------------------------------------------


def test_most_specific_reference_element_wins(demo):
    graph, report, _ = demo
    assert reference_uris(graph, "balcony_slab") == {REF + "architecture-slab-balcony"}
    assert reference_uris(graph, "wall_interior") == {REF + "architecture-wall-interior"}
    assert reference_uris(graph, "wall_exterior") == {REF + "structural-wall"}
    assert reference_uris(graph, "office") == {REF + "spaces-interior"}
    assert reference_uris(graph, "balcony_space") == {REF + "spaces-exterior"}
    assert reference_uris(graph, "railing_front") == {REF + "architecture-railing"}
    assert not report.ambiguous_elements


def test_reference_match_selects_contract_class(demo):
    graph, _, _ = demo
    for role in ("maintenance_overlap", "maintenance_touch"):
        assert (iri(role), RDF.type, PBS.ReservedVolume) in graph
        assert objects(graph, role, "reserved_volume_type") == {PBS.reserved_volume_type_maintenance}
    for role in ("railing_front", "railing_side"):
        assert (iri(role), RDF.type, PBS.SafetyBarrier) in graph


def test_proxies_without_reference_match_are_reported(demo_ifc):
    graph, report = convert(demo_ifc, base_uri=BASE, reference=False, geometry=False)
    assert report.unmatched_reference_entities["IfcBuildingElementProxy"] == 2
    assert not set(graph.subjects(RDF.type, PBS.ReservedVolume))
    assert any("reference identification" in s for s in report.skipped_stages)


# --- geometry ------------------------------------------------------------------


def test_geometry_representations(demo):
    graph, _, glb = demo
    records = {
        str(graph.value(r, PBS.geometry_representation)): r
        for r in graph.objects(iri("wall_interior"), PBS.geometry_representations)
    }
    assert set(records) == {"body_3d", "footprint_2d"}
    body = records["body_3d"]
    assert str(graph.value(body, PBS.geometry_reference)) == f"{glb.name}#{GID['wall_interior']}"
    assert str(graph.value(body, PBS.geometry_format)) == "gltf"
    bbox = [graph.value(body, PBS[f"bbox_{e}_{a}"]).toPython() for e in ("min", "max") for a in "xyz"]
    assert bbox == pytest.approx([0, 4, 0, 5, 4.2, 2.8], abs=1e-3)
    footprint = records["footprint_2d"]
    assert str(graph.value(footprint, PBS.geometry_format)) == "wkt"
    assert str(graph.value(footprint, PBS.geometry_wkt)).startswith("POLYGON")


def test_height_quantity(demo):
    graph, _, _ = demo
    heights = [v for k, v in quantities(graph, "wall_interior").items() if k.endswith("IfcQuantityLength")]
    assert heights == pytest.approx([2.8])


def test_glb_nodes_are_named_by_global_id(demo):
    _, report, glb = demo
    assert report.geometry_output == str(glb)
    data = glb.read_bytes()
    assert data[:4] == b"glTF"
    length, kind = struct.unpack_from("<I4s", data, 12)
    assert kind == b"JSON"
    names = {n.get("name") for n in json.loads(data[20 : 20 + length])["nodes"]}
    expected = set(GID.values()) - {GID[r] for r in ("project", "site", "building", "storey", "opening")}
    assert expected <= names


def test_no_geometry_keeps_ifc_relations(demo_ifc):
    graph, report = convert(demo_ifc, base_uri=BASE, reference=REFERENCE_FIXTURE, geometry=False)
    assert "geometry (disabled)" in report.skipped_stages
    assert not set(graph.objects(None, PBS.geometry_representations))
    assert objects(graph, "door_ifc", "hosted_by") == {iri("wall_interior")}
    assert not objects(graph, "door_geometry", "hosted_by")


# --- computed relations ------------------------------------------------------------


def test_hosted_by_from_ifc_and_geometry(demo):
    graph, report, _ = demo
    assert objects(graph, "door_ifc", "hosted_by") == {iri("wall_interior")}
    assert objects(graph, "door_geometry", "hosted_by") == {iri("wall_interior")}
    assert objects(graph, "window", "hosted_by") == {iri("wall_exterior")}
    assert objects(graph, "exit_door", "hosted_by") == {iri("exit_wall")}
    assert report.computed_relations["hosted_by (ifc)"] == 1
    assert report.computed_relations["hosted_by (geometry)"] == 3


def test_reserved_volume_intersections(demo):
    graph, _, _ = demo
    assert objects(graph, "maintenance_overlap", "intersects_elements") == {iri("wall_interior")}
    assert not objects(graph, "maintenance_touch", "intersects_elements")


def test_barrier_guards_space_and_height(demo):
    graph, _, _ = demo
    for role, height in (("railing_front", 1.10), ("railing_side", 1.00)):
        assert objects(graph, role, "guards_space") == {iri("balcony_space")}
        assert quantity(graph, role, "height_above_walking_surface") == pytest.approx(height, abs=1e-3)


def test_rests_on_slab_column_slab(demo):
    graph, _, _ = demo
    assert (iri("column"), RDF.type, PBS.ConnectionPhysical) in graph
    assert objects(graph, "column", "rests_on") == {iri("floor_slab")}
    assert objects(graph, "ceiling_slab", "rests_on") == {
        iri("column"), iri("wall_interior"), iri("wall_exterior")
    }
    for wall in ("wall_interior", "wall_exterior", "wall_short"):
        assert objects(graph, wall, "rests_on") == {iri("floor_slab")}
    assert not objects(graph, "floor_slab", "rests_on")


def test_equipment_rests_on_slab(demo):
    graph, _, _ = demo
    assert objects(graph, "air_handler", "rests_on") == {iri("floor_slab")}


def test_neighbour_distances(demo):
    graph, _, _ = demo
    records = {
        graph.value(r, PBS.neighbour): (
            graph.value(r, PBS.horizontal_clear_distance).toPython(),
            graph.value(r, PBS.vertical_clear_distance).toPython(),
        )
        for r in objects(graph, "air_handler", "neighbours")
    }
    assert set(records) == {iri("floor_slab"), iri("wall_exterior"), iri("balcony_slab")}
    assert records[iri("floor_slab")] == pytest.approx((0.0, 0.0), abs=1e-3)
    assert records[iri("wall_exterior")] == pytest.approx((0.1, 0.0), abs=1e-3)
    assert records[iri("balcony_slab")] == pytest.approx((0.4, 0.0), abs=1e-3)


def test_side_contact_is_symmetric(demo):
    graph, _, _ = demo
    assert objects(graph, "wall_short", "connects_physical_elements") == {iri("wall_interior")}
    assert objects(graph, "wall_interior", "connects_physical_elements") == {iri("wall_short")}
    # Bearing contact is not repeated as side contact.
    assert not objects(graph, "column", "connects_physical_elements")


def test_window_lights_interior_space(demo):
    graph, _, _ = demo
    assert objects(graph, "window", "lit_space") == {iri("office")}
    assert quantity(graph, "window", "area_glazed") == pytest.approx(2.0 * 1.2 * 0.75)
    assert quantity(graph, "office", "glazing_ratio") == pytest.approx(1.8 / 20.0)
    assert str(PBS.quantity_type_glazing_ratio) not in quantities(graph, "balcony_space")


def test_escape_route_through_doors_to_exit(demo):
    graph, _, _ = demo
    assert objects(graph, "exit_door", "escape_route_next") == set()
    assert quantity(graph, "exit_door", "escape_route_length") == 0
    # Door centre to corridor edge (0.1), across the corridor, corridor edge to exit centre (0.15).
    for door, x in (("door_geometry", 3.5), ("door_ifc", 1.5)):
        assert objects(graph, door, "escape_route_next") == {iri("exit_door")}
        expected = 0.1 + ((8 - x) ** 2 + 1) ** 0.5 + 0.15
        assert quantity(graph, door, "escape_route_length") == pytest.approx(expected, abs=1e-3)
    assert objects(graph, "corridor", "escape_route_next") == {iri("exit_door")}
    assert quantity(graph, "corridor", "escape_route_length") == pytest.approx(65**0.5 + 0.15, abs=1e-3)
    # Most remote office corner (0, 0), through the nearer door_geometry.
    assert objects(graph, "office", "escape_route_next") == {iri("door_geometry")}
    office = 28.25**0.5 + 0.1 + quantity(graph, "door_geometry", "escape_route_length")
    assert quantity(graph, "office", "escape_route_length") == pytest.approx(office, abs=1e-3)
    assert not objects(graph, "balcony_space", "escape_route_next")


def test_escape_route_path_geometry(demo):
    graph, _, _ = demo
    paths = [
        str(graph.value(r, PBS.geometry_wkt))
        for r in graph.objects(iri("office"), PBS.geometry_representations)
        if str(graph.value(r, PBS.geometry_representation)) == "path_3d"
    ]
    assert len(paths) == 1
    points = shapely.from_wkt(paths[0]).coords
    # Remote corner, door_geometry (office side, centre, corridor side), exit door centre.
    expected = [(0, 0, 0), (3.5, 4.0, 0), (3.5, 4.1, 0), (3.5, 4.2, 0), (8.0, 5.2, 0), (8.15, 5.2, 0)]
    assert [tuple(p) for p in points] == [pytest.approx(p, abs=1e-3) for p in expected]


def test_plan_region_walks_around_corners():
    from shapely.geometry import Polygon

    from pragmatic_bim.ifc2rdf.spatial.escape import PlanRegion

    l_shape = PlanRegion(Polygon([(0, 0), (4, 0), (4, 1), (1, 1), (1, 4), (0, 4)]))
    walks = l_shape.distances([3.5, 0.5], [[0.5, 3.5], [2.0, 0.5], [3.0, 3.0]])
    around = (2.5**2 + 0.5**2) ** 0.5 + (0.5**2 + 2.5**2) ** 0.5
    assert walks[0] == pytest.approx(around)
    assert walks[1] == pytest.approx(1.5)
    assert walks[2] == float("inf")
    assert l_shape.path([3.5, 0.5], [0.5, 3.5]).tolist() == [[3.5, 0.5], [1, 1], [0.5, 3.5]]
    assert l_shape.path([3.5, 0.5], [2.0, 0.5]).tolist() == [[3.5, 0.5], [2.0, 0.5]]


# --- demo rules (what an external SHACL/SPARQL checker would evaluate) --------------

BARRIERS_BELOW_MINIMUM = """
PREFIX pbs: <https://schema.pragmaticbim.ch/>
SELECT ?barrier WHERE {
  ?barrier a pbs:SafetyBarrier ; pbs:guards_space ?space ;
           pbs:quantity_values [ pbs:quantity_type pbs:quantity_type_height_above_walking_surface ;
                                 pbs:quantity_value ?height ] .
  FILTER (?height < 1.1 - 0.001)
}"""

FIRE_DOORS_IN_RATED_WALLS = """
PREFIX pbs: <https://schema.pragmaticbim.ch/>
SELECT DISTINCT ?door WHERE {
  ?door pbs:hosted_by ?wall .
  ?wall pbs:performance_properties [ a pbs:FireProperty ] .
  FILTER NOT EXISTS { ?door pbs:performance_properties [ a pbs:FireProperty ] }
}"""


FIRE_WALLS_NOT_REACHING_SLAB = """
PREFIX pbs: <https://schema.pragmaticbim.ch/>
SELECT ?wall WHERE {
  ?wall a pbs:SeparatorWall ; pbs:performance_properties [ a pbs:FireProperty ] .
  FILTER NOT EXISTS { ?slab a pbs:SeparatorSlab ; pbs:rests_on ?wall }
}"""

LOAD_PATH = """
PREFIX pbs: <https://schema.pragmaticbim.ch/>
SELECT ?upper ?member ?lower WHERE {
  ?upper a pbs:SeparatorSlab ; pbs:rests_on ?member .
  ?member pbs:connection_physical_type ?type ; pbs:rests_on ?lower .
  ?lower a pbs:SeparatorSlab .
}"""


def test_demo_rule_fire_walls_reach_slab_above(demo):
    graph, _, _ = demo
    assert {row.wall for row in graph.query(FIRE_WALLS_NOT_REACHING_SLAB)} == {iri("wall_short")}


def test_demo_rule_load_path(demo):
    graph, _, _ = demo
    assert {tuple(row) for row in graph.query(LOAD_PATH)} == {
        (iri("ceiling_slab"), iri("column"), iri("floor_slab"))
    }


def test_demo_rule_barrier_height(demo):
    graph, _, _ = demo
    assert {row.barrier for row in graph.query(BARRIERS_BELOW_MINIMUM)} == {iri("railing_side")}


def test_demo_rule_doors_in_fire_rated_walls(demo):
    graph, _, _ = demo
    assert {row.door for row in graph.query(FIRE_DOORS_IN_RATED_WALLS)} == {iri("door_ifc"), iri("door_geometry")}


# --- pragmaticBIM-reference example models (local checkout only) -------------------

REFERENCE_MEDIA = [
    "architecture-railing",
    "architecture-maintenance-space",
    "architecture-door-interior",
    "architecture-window-exterior",
    "architecture-slab-balcony",
]


@pytest.mark.parametrize("element", REFERENCE_MEDIA)
def test_reference_media_model(element, shacl_graph):
    checkout = resolve_reference_path()
    path = checkout / "media" / "attachments" / f"{element}.ifc" if checkout else None
    if path is None or not path.is_file():
        pytest.skip("pragmaticBIM-reference checkout with media/attachments not available")
    graph, report = convert(path, reference=checkout)
    assert report.identified_elements[f"pragmaticbim:element/{element}"] >= 1
    assert shacl_violations(graph, shacl_graph) == []
