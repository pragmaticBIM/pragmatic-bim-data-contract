"""Ground-floor flags, height_above_ground_floor, TerrainSurface and height_above_terrain."""

from __future__ import annotations

from pathlib import Path

import ifcopenshell
import ifcopenshell.api.aggregate
import ifcopenshell.api.context
import ifcopenshell.api.geometry
import ifcopenshell.api.project
import ifcopenshell.api.pset
import ifcopenshell.api.root
import ifcopenshell.api.spatial
import ifcopenshell.api.unit
import ifcopenshell.guid
import numpy as np
import pytest
import rdflib
from checks import PBS
from rdflib import RDF, XSD, Literal

from pragmatic_bim.ifc2rdf import convert
from pragmatic_bim.ifc2rdf.geometry import ElementGeometry, terrain_height_at, terrain_mesh_from_geometry

api = ifcopenshell.api
BASE = "https://data.example.org/ground/"

pytest.importorskip("shapely")


def _guid(n: int) -> str:
    return ifcopenshell.guid.compress(f"{n:032x}")


def _building_storeys(path: Path, storeys: list[dict]) -> Path:
    f = api.project.create_file(version="IFC4")
    project = api.root.create_entity(f, ifc_class="IfcProject", name="Ground")
    project.GlobalId = _guid(1)
    api.unit.assign_unit(f)
    api.context.add_context(f, context_type="Model")
    site = api.root.create_entity(f, ifc_class="IfcSite", name="Site")
    site.GlobalId = _guid(2)
    building = api.root.create_entity(f, ifc_class="IfcBuilding", name="Building")
    building.GlobalId = _guid(3)
    api.aggregate.assign_object(f, relating_object=project, products=[site])
    api.aggregate.assign_object(f, relating_object=site, products=[building])
    for index, spec in enumerate(storeys):
        storey = api.root.create_entity(f, ifc_class="IfcBuildingStorey", name=spec["name"])
        storey.GlobalId = spec.get("gid", _guid(10 + index))
        if "elevation" in spec:
            storey.Elevation = float(spec["elevation"])  # project units: mm
        api.aggregate.assign_object(f, relating_object=building, products=[storey])
        if "above_ground" in spec or "entrance" in spec:
            props = []
            if "above_ground" in spec:
                # edit_pset maps Python bool to UNKNOWN for IfcLogical; create NominalValue directly.
                props.append(
                    f.create_entity(
                        "IfcPropertySingleValue",
                        "AboveGround",
                        None,
                        f.create_entity("IfcLogical", bool(spec["above_ground"])),
                        None,
                    )
                )
            if "entrance" in spec:
                props.append(
                    f.create_entity(
                        "IfcPropertySingleValue",
                        "EntranceLevel",
                        None,
                        f.create_entity("IfcBoolean", bool(spec["entrance"])),
                        None,
                    )
                )
            pset = f.create_entity(
                "IfcPropertySet",
                ifcopenshell.guid.new(),
                None,
                "Pset_BuildingStoreyCommon",
                None,
                props,
            )
            f.create_entity(
                "IfcRelDefinesByProperties",
                ifcopenshell.guid.new(),
                None,
                None,
                None,
                [storey],
                pset,
            )
    f.write(str(path))
    return path


def _slot(graph: rdflib.Graph, subject, slot: str):
    return graph.value(subject, PBS[slot])


def _storey_iris(graph: rdflib.Graph) -> dict[str, rdflib.URIRef]:
    return {
        str(graph.value(s, PBS.name)): s
        for s in graph.subjects(RDF.type, PBS.LevelContext)
    }


def test_ground_floor_from_ifc_property(tmp_path):
    path = _building_storeys(
        tmp_path / "ifc.ifc",
        [
            {"name": "U01", "elevation": -3000, "above_ground": False, "entrance": False, "gid": _guid(21)},
            {"name": "EG", "elevation": 0, "above_ground": True, "entrance": True, "gid": _guid(22)},
            {"name": "01", "elevation": 3000, "above_ground": True, "entrance": False, "gid": _guid(23)},
        ],
    )
    graph, report = convert(path, base_uri=BASE, reference=False, geometry=False)
    storeys = _storey_iris(graph)
    assert _slot(graph, storeys["EG"], "is_ground_floor") == Literal(True, datatype=XSD.boolean)
    assert _slot(graph, storeys["U01"], "is_ground_floor") == Literal(False, datatype=XSD.boolean)
    assert _slot(graph, storeys["EG"], "above_ground") == Literal(True, datatype=XSD.boolean)
    assert _slot(graph, storeys["U01"], "above_ground") == Literal(False, datatype=XSD.boolean)
    assert _slot(graph, storeys["EG"], "ground_reference_source") == PBS.ground_reference_source_ifc_property
    assert report.computed_relations["ground_floor (ifc_property)"] == 1


def test_ground_floor_from_name_convention(tmp_path):
    path = _building_storeys(
        tmp_path / "ifc.ifc",
        [
            {"name": "FD", "elevation": -6000, "gid": _guid(31)},
            {"name": "U01", "elevation": -3000, "gid": _guid(32)},
            {"name": "EG", "elevation": 0, "gid": _guid(33)},
            {"name": "01", "elevation": 3000, "gid": _guid(34)},
            {"name": "01.Z", "elevation": 1500, "gid": _guid(35)},
        ],
    )
    graph, report = convert(path, base_uri=BASE, reference=False, geometry=False)
    storeys = _storey_iris(graph)
    assert _slot(graph, storeys["EG"], "is_ground_floor") == Literal(True, datatype=XSD.boolean)
    assert _slot(graph, storeys["FD"], "above_ground") == Literal(False, datatype=XSD.boolean)
    assert _slot(graph, storeys["U01"], "above_ground") == Literal(False, datatype=XSD.boolean)
    assert _slot(graph, storeys["01"], "above_ground") == Literal(True, datatype=XSD.boolean)
    assert _slot(graph, storeys["01.Z"], "above_ground") == Literal(True, datatype=XSD.boolean)
    assert _slot(graph, storeys["01.Z"], "is_ground_floor") == Literal(False, datatype=XSD.boolean)
    assert _slot(graph, storeys["EG"], "ground_reference_source") == PBS.ground_reference_source_name_convention
    assert report.computed_relations["ground_floor (name_convention)"] == 1


def test_ground_floor_from_elevation_and_ambiguous(tmp_path):
    path = _building_storeys(
        tmp_path / "ifc.ifc",
        [
            {"name": "Basement", "elevation": -3000, "gid": _guid(41)},
            {"name": "Lobby", "elevation": 0, "gid": _guid(42)},
            {"name": "Mezzanine", "elevation": 1500, "gid": _guid(43)},
            {"name": "AlsoEntrance", "elevation": 100, "entrance": True, "above_ground": True, "gid": _guid(44)},
            {"name": "SecondEntrance", "elevation": 500, "entrance": True, "above_ground": True, "gid": _guid(45)},
        ],
    )
    graph, report = convert(path, base_uri=BASE, reference=False, geometry=False)
    storeys = _storey_iris(graph)
    # IFC properties present → ifc_property; two EntranceLevel → lowest elevation wins.
    assert _slot(graph, storeys["AlsoEntrance"], "is_ground_floor") == Literal(True, datatype=XSD.boolean)
    assert _slot(graph, storeys["SecondEntrance"], "is_ground_floor") == Literal(False, datatype=XSD.boolean)
    assert report.computed_relations["ground_floor (ambiguous)"] == 1

    path2 = _building_storeys(
        tmp_path / "elev.ifc",
        [
            {"name": "Basement", "elevation": -3000, "gid": _guid(51)},
            {"name": "Lobby", "elevation": 0, "gid": _guid(52)},
            {"name": "Office", "elevation": 3000, "gid": _guid(53)},
        ],
    )
    graph2, report2 = convert(path2, base_uri=BASE, reference=False, geometry=False)
    storeys2 = _storey_iris(graph2)
    assert _slot(graph2, storeys2["Lobby"], "is_ground_floor") == Literal(True, datatype=XSD.boolean)
    assert _slot(graph2, storeys2["Basement"], "above_ground") == Literal(False, datatype=XSD.boolean)
    assert _slot(graph2, storeys2["Office"], "above_ground") == Literal(True, datatype=XSD.boolean)
    assert _slot(graph2, storeys2["Lobby"], "ground_reference_source") == PBS.ground_reference_source_elevation
    assert report2.computed_relations["ground_floor (elevation)"] == 1


def _measurement_model(path: Path, *, ground_elevation_mm: float = 0.0, include_elements: bool = True) -> dict[str, str]:
    f = api.project.create_file(version="IFC4")
    ids = {}
    project = api.root.create_entity(f, ifc_class="IfcProject", name="Heights")
    project.GlobalId = ids["project"] = _guid(60)
    api.unit.assign_unit(f)
    context = api.context.add_context(f, context_type="Model")
    body = api.context.add_context(f, context_type="Model", context_identifier="Body", target_view="MODEL_VIEW", parent=context)
    site = api.root.create_entity(f, ifc_class="IfcSite", name="Site")
    site.GlobalId = ids["site"] = _guid(61)
    building = api.root.create_entity(f, ifc_class="IfcBuilding", name="Building")
    building.GlobalId = ids["building"] = _guid(62)
    storey = api.root.create_entity(f, ifc_class="IfcBuildingStorey", name="EG")
    storey.GlobalId = ids["storey"] = _guid(63)
    storey.Elevation = ground_elevation_mm
    api.aggregate.assign_object(f, relating_object=project, products=[site])
    api.aggregate.assign_object(f, relating_object=site, products=[building])
    api.aggregate.assign_object(f, relating_object=building, products=[storey])
    if include_elements:
        space = api.root.create_entity(f, ifc_class="IfcSpace", name="Room")
        space.GlobalId = ids["space"] = _guid(64)
        api.aggregate.assign_object(f, relating_object=storey, products=[space])
        representation = api.geometry.add_wall_representation(f, context=body, length=4.0, height=2.8, thickness=4.0)
        api.geometry.assign_representation(f, product=space, representation=representation)
        matrix = np.eye(4)
        matrix[2, 3] = 1.0  # space floor at 1 m (below EG when EG elev is 3 m)
        api.geometry.edit_object_placement(f, product=space, matrix=matrix)

        window = api.root.create_entity(f, ifc_class="IfcWindow", name="Window", predefined_type="WINDOW")
        window.GlobalId = ids["window"] = _guid(65)
        api.spatial.assign_container(f, relating_structure=storey, products=[window])
        win_rep = api.geometry.add_wall_representation(f, context=body, length=1.2, height=1.2, thickness=0.1)
        api.geometry.assign_representation(f, product=window, representation=win_rep)
        win_matrix = np.eye(4)
        win_matrix[0, 3], win_matrix[1, 3], win_matrix[2, 3] = 0.0, 0.0, 1.0
        api.geometry.edit_object_placement(f, product=window, matrix=win_matrix)

        railing = api.root.create_entity(f, ifc_class="IfcRailing", name="Rail", predefined_type="BALUSTRADE")
        railing.GlobalId = ids["railing"] = _guid(66)
        api.spatial.assign_container(f, relating_structure=storey, products=[railing])
        rail_rep = api.geometry.add_wall_representation(f, context=body, length=2.0, height=1.1, thickness=0.05)
        api.geometry.assign_representation(f, product=railing, representation=rail_rep)
        rail_matrix = np.eye(4)
        rail_matrix[0, 3], rail_matrix[1, 3], rail_matrix[2, 3] = 5.0, 0.0, 0.0
        api.geometry.edit_object_placement(f, product=railing, matrix=rail_matrix)
    f.write(str(path))
    return ids


def _measurements(graph: rdflib.Graph, method: str) -> list[rdflib.URIRef]:
    return [
        s
        for s in graph.subjects(RDF.type, PBS.DerivedMeasurement)
        if str(graph.value(s, PBS.name)) == method
    ]


def _quantity(graph: rdflib.Graph, measurement, quantity_type: str) -> float | None:
    wanted = str(PBS[f"quantity_type_{quantity_type}"])
    for q in graph.objects(measurement, PBS.quantity_values):
        if str(graph.value(q, PBS.quantity_type)) == wanted:
            return graph.value(q, PBS.quantity_value).toPython()
    return None


def test_height_above_ground_floor_positive_and_negative(tmp_path):
    # EG at 0 mm → elevations 0 m; window sill ~1 m → positive; space floor at 1 m.
    ids = _measurement_model(tmp_path / "pos.ifc", ground_elevation_mm=0.0)
    graph, report = convert(tmp_path / "pos.ifc", base_uri=BASE, reference=False)
    measured = _measurements(graph, "height_above_ground_floor")
    assert measured
    by_subject = {}
    for m in measured:
        subjects = set(graph.objects(m, PBS.applies_to_entities))
        for role, gid in ids.items():
            iri = rdflib.URIRef(BASE + gid)
            if iri in subjects and role in ("window", "space", "railing"):
                by_subject[role] = m
    assert set(by_subject) == {"window", "space", "railing"}
    assert _quantity(graph, by_subject["window"], "height_above_ground_floor") == pytest.approx(1.0, abs=0.05)
    assert _quantity(graph, by_subject["railing"], "height_above_ground_floor") == pytest.approx(1.1, abs=0.05)
    assert (by_subject["window"], PBS.measurement_status, PBS.measurement_status_measured) in graph
    assert report.computed_measurements["height_above_ground_floor"] >= 3

    # EG at 3000 mm = 3 m; space/window sill at 1 m → negative height kept.
    ids2 = _measurement_model(tmp_path / "neg.ifc", ground_elevation_mm=3000.0)
    graph2, _ = convert(tmp_path / "neg.ifc", base_uri=BASE, reference=False)
    for m in _measurements(graph2, "height_above_ground_floor"):
        subjects = set(graph2.objects(m, PBS.applies_to_entities))
        if rdflib.URIRef(BASE + ids2["window"]) in subjects:
            value = _quantity(graph2, m, "height_above_ground_floor")
            assert value is not None and value < 0


def test_height_above_ground_floor_not_measurable_without_ground(tmp_path):
    path = tmp_path / "none.ifc"
    f = api.project.create_file(version="IFC4")
    project = api.root.create_entity(f, ifc_class="IfcProject", name="None")
    project.GlobalId = _guid(70)
    api.unit.assign_unit(f)
    context = api.context.add_context(f, context_type="Model")
    body = api.context.add_context(f, context_type="Model", context_identifier="Body", target_view="MODEL_VIEW", parent=context)
    site = api.root.create_entity(f, ifc_class="IfcSite", name="Site")
    site.GlobalId = _guid(71)
    building = api.root.create_entity(f, ifc_class="IfcBuilding", name="Building")
    building.GlobalId = _guid(72)
    storey = api.root.create_entity(f, ifc_class="IfcBuildingStorey", name="BasementOnly")
    storey.GlobalId = _guid(73)
    storey.Elevation = -3000.0
    api.aggregate.assign_object(f, relating_object=project, products=[site])
    api.aggregate.assign_object(f, relating_object=site, products=[building])
    api.aggregate.assign_object(f, relating_object=building, products=[storey])
    window = api.root.create_entity(f, ifc_class="IfcWindow", name="Window", predefined_type="WINDOW")
    window.GlobalId = _guid(74)
    api.spatial.assign_container(f, relating_structure=storey, products=[window])
    win_rep = api.geometry.add_wall_representation(f, context=body, length=1.0, height=1.0, thickness=0.1)
    api.geometry.assign_representation(f, product=window, representation=win_rep)
    f.write(str(path))
    graph, _ = convert(path, base_uri=BASE, reference=False)
    measured = _measurements(graph, "height_above_ground_floor")
    assert measured
    assert all(
        (m, PBS.measurement_status, PBS.measurement_status_not_measurable) in graph for m in measured
    )


def test_terrain_height_at_on_synthetic_slope():
    # Two triangles forming a 2×2 square sloping from z=0 at (0,0) to z=2 at (2,2).
    verts = np.array(
        [
            [0.0, 0.0, 0.0],
            [2.0, 0.0, 1.0],
            [0.0, 2.0, 1.0],
            [2.0, 2.0, 2.0],
        ],
        dtype=float,
    )
    faces = np.array([[0, 1, 2], [1, 3, 2]], dtype=int)
    geo = ElementGeometry(id=1, global_id="T", ifc_class="IfcGeographicElement", verts=verts, faces=faces)
    mesh = terrain_mesh_from_geometry(geo)
    assert mesh is not None
    assert terrain_height_at(mesh, 0.0, 0.0) == pytest.approx(0.0, abs=1e-6)
    assert terrain_height_at(mesh, 2.0, 2.0) == pytest.approx(2.0, abs=1e-6)
    assert terrain_height_at(mesh, 1.0, 1.0) == pytest.approx(1.0, abs=1e-6)
    assert terrain_height_at(mesh, 5.0, 5.0) is None


def _terrain_model(path: Path, *, projected: bool = False, with_elements: bool = True) -> dict[str, str]:
    f = api.project.create_file(version="IFC4")
    ids = {}
    project = api.root.create_entity(f, ifc_class="IfcProject", name="Terrain")
    project.GlobalId = ids["project"] = _guid(80)
    api.unit.assign_unit(f)
    context = api.context.add_context(f, context_type="Model")
    body = api.context.add_context(f, context_type="Model", context_identifier="Body", target_view="MODEL_VIEW", parent=context)
    site = api.root.create_entity(f, ifc_class="IfcSite", name="Site")
    site.GlobalId = ids["site"] = _guid(81)
    building = api.root.create_entity(f, ifc_class="IfcBuilding", name="Building")
    building.GlobalId = ids["building"] = _guid(82)
    storey = api.root.create_entity(f, ifc_class="IfcBuildingStorey", name="EG")
    storey.GlobalId = ids["storey"] = _guid(83)
    storey.Elevation = 0.0
    api.aggregate.assign_object(f, relating_object=project, products=[site])
    api.aggregate.assign_object(f, relating_object=site, products=[building])
    api.aggregate.assign_object(f, relating_object=building, products=[storey])

    terrain = api.root.create_entity(f, ifc_class="IfcGeographicElement", name="Terrain", predefined_type="TERRAIN")
    terrain.GlobalId = ids["terrain"] = _guid(84)
    terrain.ObjectType = "projected" if projected else "existing"
    api.spatial.assign_container(f, relating_structure=site, products=[terrain])
    # Flat-ish slab representation covering 0..10 m in plan at z≈0
    terr_rep = api.geometry.add_wall_representation(f, context=body, length=10.0, height=0.05, thickness=10.0)
    api.geometry.assign_representation(f, product=terrain, representation=terr_rep)
    terr_matrix = np.eye(4)
    terr_matrix[2, 3] = 0.0
    api.geometry.edit_object_placement(f, product=terrain, matrix=terr_matrix)

    if with_elements:
        window = api.root.create_entity(f, ifc_class="IfcWindow", name="Window", predefined_type="WINDOW")
        window.GlobalId = ids["window"] = _guid(85)
        api.spatial.assign_container(f, relating_structure=storey, products=[window])
        win_rep = api.geometry.add_wall_representation(f, context=body, length=1.0, height=1.0, thickness=0.1)
        api.geometry.assign_representation(f, product=window, representation=win_rep)
        win_matrix = np.eye(4)
        win_matrix[0, 3], win_matrix[1, 3], win_matrix[2, 3] = 2.0, 2.0, 1.5
        api.geometry.edit_object_placement(f, product=window, matrix=win_matrix)

        space = api.root.create_entity(f, ifc_class="IfcSpace", name="Room")
        space.GlobalId = ids["space"] = _guid(86)
        api.aggregate.assign_object(f, relating_object=storey, products=[space])
        space_rep = api.geometry.add_wall_representation(f, context=body, length=3.0, height=2.5, thickness=3.0)
        api.geometry.assign_representation(f, product=space, representation=space_rep)
        space_matrix = np.eye(4)
        space_matrix[0, 3], space_matrix[1, 3], space_matrix[2, 3] = 1.0, 1.0, 0.5
        api.geometry.edit_object_placement(f, product=space, matrix=space_matrix)

        railing = api.root.create_entity(f, ifc_class="IfcRailing", name="Rail", predefined_type="GUARDRAIL")
        railing.GlobalId = ids["railing"] = _guid(87)
        api.spatial.assign_container(f, relating_structure=storey, products=[railing])
        rail_rep = api.geometry.add_wall_representation(f, context=body, length=2.0, height=1.0, thickness=0.05)
        api.geometry.assign_representation(f, product=railing, representation=rail_rep)
        rail_matrix = np.eye(4)
        rail_matrix[0, 3], rail_matrix[1, 3], rail_matrix[2, 3] = 3.0, 3.0, 0.2
        api.geometry.edit_object_placement(f, product=railing, matrix=rail_matrix)

    f.write(str(path))
    return ids


def test_terrain_surface_mapping_and_height_above_terrain(tmp_path):
    ids = _terrain_model(tmp_path / "terrain.ifc", projected=False)
    graph, report = convert(tmp_path / "terrain.ifc", base_uri=BASE, reference=False)
    terrain_iri = rdflib.URIRef(BASE + ids["terrain"])
    assert (terrain_iri, RDF.type, PBS.TerrainSurface) in graph
    assert (terrain_iri, PBS.terrain_surface_status, PBS.terrain_surface_status_existing) in graph

    measured = _measurements(graph, "height_above_terrain")
    assert measured
    roles = {}
    for m in measured:
        subjects = set(graph.objects(m, PBS.applies_to_entities))
        for role in ("window", "space", "railing"):
            if rdflib.URIRef(BASE + ids[role]) in subjects:
                roles[role] = m
                assert terrain_iri in subjects
                assert (m, PBS.measurement_status, PBS.measurement_status_measured) in graph
                assert _quantity(graph, m, "height_above_terrain") is not None
    assert set(roles) == {"window", "space", "railing"}
    assert report.computed_measurements["height_above_terrain"] >= 3

    ids2 = _terrain_model(tmp_path / "projected.ifc", projected=True)
    graph2, _ = convert(tmp_path / "projected.ifc", base_uri=BASE, reference=False)
    assert (
        rdflib.URIRef(BASE + ids2["terrain"]),
        PBS.terrain_surface_status,
        PBS.terrain_surface_status_projected,
    ) in graph2


def test_height_above_terrain_not_measurable_without_terrain(tmp_path):
    _measurement_model(tmp_path / "no_terrain.ifc")
    graph, _ = convert(tmp_path / "no_terrain.ifc", base_uri=BASE, reference=False)
    measured = _measurements(graph, "height_above_terrain")
    assert measured
    assert all(
        (m, PBS.measurement_status, PBS.measurement_status_not_measurable) in graph for m in measured
    )
    for m in measured:
        assert _quantity(graph, m, "height_above_terrain") is None
