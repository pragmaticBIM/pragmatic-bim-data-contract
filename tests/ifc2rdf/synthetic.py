"""Small IFC4 model covering the relations exported by ifc2rdf."""

from __future__ import annotations

from pathlib import Path

import ifcopenshell
import ifcopenshell.api.aggregate
import ifcopenshell.api.context
import ifcopenshell.api.project
import ifcopenshell.api.pset
import ifcopenshell.api.root
import ifcopenshell.api.spatial
import ifcopenshell.api.unit
import ifcopenshell.guid

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
    api.pset.edit_pset(f, pset=pset, properties={"IsExternal": False})
    custom = api.pset.add_pset(f, product=wall, name="Custom_Data")
    api.pset.edit_pset(f, pset=custom, properties={"Note": "synthetic"})

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
