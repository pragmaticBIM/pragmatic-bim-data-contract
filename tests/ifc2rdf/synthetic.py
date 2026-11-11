"""Small IFC4 model covering the relations exported by ifc2rdf."""

from __future__ import annotations

from pathlib import Path

import ifcopenshell
import ifcopenshell.api.aggregate
import ifcopenshell.api.context
import ifcopenshell.api.feature
import ifcopenshell.api.geometry
import ifcopenshell.api.project
import ifcopenshell.api.pset
import ifcopenshell.api.root
import ifcopenshell.api.spatial
import ifcopenshell.api.unit
import ifcopenshell.guid
import numpy as np

api = ifcopenshell.api

GLOBAL_IDS = {
    "project": "0_GnOvDvLFvh8OAMIIfyZK",
    "site": "2S7MK3ekP1sBqBvntVpVbO",
    "building": "2sTR9pWRL7cukE4OiK_291",
    "storey": "0heBVqALjAQRx5h7xgLFpP",
    "kitchen": "0tZ3YpNO1FBfo0OXVZ2CcQ",
    "living": "0r3HfCNkz60B2Gj1FVKZDs",
    "wall": "1NBmyYQHjELQyrC2t3Q8ib",
    "slab": "3C2OZFrAz2ABM0OIF92CZ2",
    "door": "06ghllMnv4cfLS8IxzDThn",
    "air_terminal": "2Yw3MqzGb0ZOwGrDOO8sXK",
}


def build_model(path: Path) -> dict[str, str]:
    """Write the model to ``path`` and return the GlobalIds by role."""
    f = api.project.create_file(version="IFC4")
    entities = {}

    def create(role: str, ifc_class: str, name: str, **kwargs):
        entity = api.root.create_entity(f, ifc_class=ifc_class, name=name, **kwargs)
        entity.GlobalId = GLOBAL_IDS[role]
        entities[role] = entity
        return entity

    project = create("project", "IfcProject", "Synthetic")
    api.unit.assign_unit(f)  # millimetres
    api.context.add_context(f, context_type="Model")
    site = create("site", "IfcSite", "Site")
    building = create("building", "IfcBuilding", "Building A")
    storey = create("storey", "IfcBuildingStorey", "EG")
    storey.Elevation = 3000.0
    api.aggregate.assign_object(f, relating_object=project, products=[site])
    api.aggregate.assign_object(f, relating_object=site, products=[building])
    api.aggregate.assign_object(f, relating_object=building, products=[storey])

    kitchen = create("kitchen", "IfcSpace", "Küche")
    living = create("living", "IfcSpace", "Wohnen")
    api.aggregate.assign_object(f, relating_object=storey, products=[kitchen, living])

    wall = create("wall", "IfcWall", "Wall 1", predefined_type="STANDARD")
    slab = create("slab", "IfcSlab", "Slab 1", predefined_type="FLOOR")
    door = create("door", "IfcDoor", "Door 1", predefined_type="DOOR")
    api.spatial.assign_container(f, relating_structure=storey, products=[wall, slab, door])
    air_terminal = create("air_terminal", "IfcAirTerminal", "Supply 1", predefined_type="DIFFUSER")
    api.spatial.assign_container(f, relating_structure=kitchen, products=[air_terminal])

    pset = api.pset.add_pset(f, product=wall, name="Pset_WallCommon")
    api.pset.edit_pset(
        f,
        pset=pset,
        properties={
            "IsExternal": False,
            "LoadBearing": True,
            "FireRating": "EI 90",
            "AcousticRating": "Rw 52 dB",
            "ThermalTransmittance": 0.25,
        },
    )
    custom = api.pset.add_pset(f, product=wall, name="Custom_Data")
    api.pset.edit_pset(f, pset=custom, properties={"Note": "synthetic"})
    slab_common = api.pset.add_pset(f, product=slab, name="Pset_SlabCommon")
    api.pset.edit_pset(f, pset=slab_common, properties={"FireRating": "REI 60-RF1"})
    # Revit placeholder in the standard pset; the rating itself is in the Revit type pset.
    door_common = api.pset.add_pset(f, product=door, name="Pset_DoorCommon")
    api.pset.edit_pset(f, pset=door_common, properties={"FireRating": "Fire Rating"})
    door_revit = api.pset.add_pset(f, product=door, name="PSet_Revit_Type_Other")
    api.pset.edit_pset(f, pset=door_revit, properties={"FireRating": "EI 30-C"})

    boundaries = [(kitchen, wall), (living, wall), (kitchen, door), (living, door), (kitchen, slab)]
    for index, (space, element) in enumerate(boundaries):
        f.create_entity(
            "IfcRelSpaceBoundary",
            GlobalId=ifcopenshell.guid.compress(f"{index + 1:032x}"),
            RelatingSpace=space,
            RelatedBuildingElement=element,
            PhysicalOrVirtualBoundary="PHYSICAL",
            InternalOrExternalBoundary="INTERNAL",
        )
    f.write(str(path))
    return dict(GLOBAL_IDS)


DEMO_ROLES = [
    "project", "site", "building", "storey",
    "office", "balcony_space",
    "wall_interior", "wall_exterior", "balcony_slab",
    "door_ifc", "opening", "door_geometry", "window",
    "maintenance_overlap", "maintenance_touch",
    "railing_front", "railing_side",
    "floor_slab", "ceiling_slab", "column", "wall_short",
]
DEMO_GLOBAL_IDS = {role: ifcopenshell.guid.compress(f"{0xD000 + i:032x}") for i, role in enumerate(DEMO_ROLES)}


def build_demo_model(path: Path) -> dict[str, str]:
    """Write the geometry demo model (millimetre lengths, m² areas) and return GlobalIds by role.

    Plan (metres), storey at z = 0:

    - office: interior space x 0..5, y 0..4, NetFloorArea 20 m².
    - wall_interior: EI 60 wall x 0..5, y 4..4.2; door_ifc fills ``opening`` (x 1..2);
      door_geometry (x 3..4) sits in the wall without opening relations.
    - maintenance_overlap: Wartungsraum x 4..5, y 3.5..4.5 (cuts the wall);
      maintenance_touch: Wartungsraum x 0..0.5, y 3..4 (only touches it).
    - wall_exterior: x 0..5, y -0.3..0; window: exterior, 2.0 × 1.2 m, glazing fraction 0.75,
      in that wall without opening relations.
    - balcony_slab y -2.3..-0.3 with exterior balcony_space on top; railing_front
      (1.10 m, y -2.3..-2.25) and railing_side (1.00 m, x 0..0.05, y -2.25..-0.5).
    - floor_slab (z -0.2..0) and ceiling_slab (z 2.8..3.0) over x 0..5, y -0.3..4.2, with
      column (x 2.4..2.6, y 1.9..2.1) between them; both full-height walls carry the ceiling.
    - wall_short: EI 30 partition x 2.0..2.1, y 2.1..4.0, 2.5 m high (stops below the
      ceiling slab), abutting wall_interior.
    """
    f = api.project.create_file(version="IFC4")
    entities = {}

    def create(role: str, ifc_class: str, name: str, **kwargs):
        entity = api.root.create_entity(f, ifc_class=ifc_class, name=name, **kwargs)
        entity.GlobalId = DEMO_GLOBAL_IDS[role]
        entities[role] = entity
        return entity

    def pset(product, name: str, properties: dict) -> None:
        api.pset.edit_pset(f, pset=api.pset.add_pset(f, product=product, name=name), properties=properties)

    project = create("project", "IfcProject", "Demo")
    api.unit.assign_unit(f)
    model = api.context.add_context(f, context_type="Model")
    body = api.context.add_context(
        f, context_type="Model", context_identifier="Body", target_view="MODEL_VIEW", parent=model
    )

    def box(product, x0: float, y0: float, z0: float, x1: float, y1: float, z1: float) -> None:
        matrix = np.eye(4)
        matrix[:3, 3] = (x0, y0, z0)
        api.geometry.edit_object_placement(f, product=product, matrix=matrix)
        representation = api.geometry.add_wall_representation(
            f, context=body, length=x1 - x0, height=z1 - z0, thickness=y1 - y0
        )
        api.geometry.assign_representation(f, product=product, representation=representation)

    site = create("site", "IfcSite", "Site")
    building = create("building", "IfcBuilding", "Building A")
    storey = create("storey", "IfcBuildingStorey", "EG")
    storey.Elevation = 0.0
    api.aggregate.assign_object(f, relating_object=project, products=[site])
    api.aggregate.assign_object(f, relating_object=site, products=[building])
    api.aggregate.assign_object(f, relating_object=building, products=[storey])

    office = create("office", "IfcSpace", "Büro", predefined_type="SPACE")
    balcony_space = create("balcony_space", "IfcSpace", "Balkon", predefined_type="SPACE")
    api.aggregate.assign_object(f, relating_object=storey, products=[office, balcony_space])
    box(office, 0, 0, 0, 5, 4, 2.8)
    box(balcony_space, 0, -2.3, 0, 5, -0.3, 2.5)
    pset(office, "Pset_SpaceCommon", {"IsExternal": False})
    pset(balcony_space, "Pset_SpaceCommon", {"IsExternal": True})
    qto = api.pset.add_qto(f, product=office, name="Qto_SpaceBaseQuantities")
    api.pset.edit_qto(f, qto=qto, properties={"NetFloorArea": 20.0})

    wall_interior = create("wall_interior", "IfcWall", "Wand EI60", predefined_type="STANDARD")
    wall_exterior = create("wall_exterior", "IfcWall", "Aussenwand", predefined_type="STANDARD")
    balcony_slab = create("balcony_slab", "IfcSlab", "Balkonplatte", predefined_type="FLOOR")
    box(wall_interior, 0, 4, 0, 5, 4.2, 2.8)
    box(wall_exterior, 0, -0.3, 0, 5, 0, 2.8)
    box(balcony_slab, 0, -2.3, -0.2, 5, -0.3, 0)
    pset(wall_interior, "Pset_WallCommon", {"IsExternal": False, "LoadBearing": False, "FireRating": "EI 60"})
    pset(wall_exterior, "Pset_WallCommon", {"IsExternal": True, "LoadBearing": True})
    pset(balcony_slab, "Pset_SlabCommon", {"IsExternal": True, "LoadBearing": True})

    opening = create("opening", "IfcOpeningElement", "Öffnung", predefined_type="OPENING")
    box(opening, 1, 4, 0, 2, 4.2, 2.1)
    api.feature.add_feature(f, feature=opening, element=wall_interior)
    door_ifc = create("door_ifc", "IfcDoor", "Tür 1", predefined_type="DOOR")
    door_geometry = create("door_geometry", "IfcDoor", "Tür 2", predefined_type="DOOR")
    box(door_ifc, 1, 4.05, 0, 2, 4.15, 2.1)
    box(door_geometry, 3, 4.05, 0, 4, 4.15, 2.1)
    api.feature.add_filling(f, opening=opening, element=door_ifc)
    for door in (door_ifc, door_geometry):
        pset(door, "Pset_DoorCommon", {"IsExternal": False})

    window = create("window", "IfcWindow", "Fenster", predefined_type="WINDOW")
    window.OverallWidth, window.OverallHeight = 2000.0, 1200.0
    box(window, 1, -0.3, 0.9, 3, 0, 2.1)
    pset(window, "Pset_WindowCommon", {"IsExternal": True, "GlazingAreaFraction": 0.75})

    maintenance = []
    for role, bounds in (
        ("maintenance_overlap", (4, 3.5, 0, 5, 4.5, 2)),
        ("maintenance_touch", (0, 3, 0, 0.5, 4, 2)),
    ):
        proxy = create(role, "IfcBuildingElementProxy", "WR", predefined_type="USERDEFINED")
        proxy.ObjectType = "Wartungsraum"
        box(proxy, *bounds)
        maintenance.append(proxy)

    railing_front = create("railing_front", "IfcRailing", "Geländer vorne", predefined_type="GUARDRAIL")
    railing_side = create("railing_side", "IfcRailing", "Geländer seitlich", predefined_type="GUARDRAIL")
    box(railing_front, 0, -2.3, 0, 5, -2.25, 1.10)
    box(railing_side, 0, -2.25, 0, 0.05, -0.5, 1.00)

    floor_slab = create("floor_slab", "IfcSlab", "Bodenplatte", predefined_type="FLOOR")
    ceiling_slab = create("ceiling_slab", "IfcSlab", "Decke", predefined_type="FLOOR")
    box(floor_slab, 0, -0.3, -0.2, 5, 4.2, 0)
    box(ceiling_slab, 0, -0.3, 2.8, 5, 4.2, 3.0)
    for slab in (floor_slab, ceiling_slab):
        pset(slab, "Pset_SlabCommon", {"IsExternal": False, "LoadBearing": True})
    column = create("column", "IfcColumn", "Stütze", predefined_type="COLUMN")
    box(column, 2.4, 1.9, 0, 2.6, 2.1, 2.8)
    wall_short = create("wall_short", "IfcWall", "Trennwand EI30", predefined_type="STANDARD")
    box(wall_short, 2.0, 2.1, 0, 2.1, 4.0, 2.5)
    pset(wall_short, "Pset_WallCommon", {"IsExternal": False, "LoadBearing": False, "FireRating": "EI 30"})

    api.spatial.assign_container(
        f,
        relating_structure=storey,
        products=[
            wall_interior, wall_exterior, balcony_slab, door_ifc, door_geometry, window,
            *maintenance, railing_front, railing_side, floor_slab, ceiling_slab, column, wall_short,
        ],
    )
    f.write(str(path))
    return dict(DEMO_GLOBAL_IDS)
