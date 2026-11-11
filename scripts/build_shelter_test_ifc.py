#!/usr/bin/env python3
"""Test IFC: civil-defence shelter (Pflichtschutzraum) in a basement, for the TW Schock rules.

Built with the IFC generators of the pragmaticBIM Reference checkout (``generators/``), found
like the converter finds it (``$PBS_REFERENCE_PATH`` or ``../elementplan/pragmaticBIM-reference``).

Layout (UG, floor at -3.00, clear height 2.60, reinforced concrete 0.30):

    Schutzraum  x 0..8      y 0..6     shelter room with ventilation unit, gas filter, pump,
                                       bunks, shelf, cabinet
    Schleuse    x 8.3..12   y 0..2.5   airlock with a suspended ceiling in two elements
    Korridor    x 8.3..12   y 2.8..6   exit corridor with the external door

The TW Schock data the contract cannot carry yet sits in the property set ``PBIM_Schocksicherheit``
(one property per missing structural property key) and ``PBIM_Schutzbau`` on the zone. Each
component and ceiling is set up to pass or fail a specific rule; see ``COMPONENTS`` and ``CEILINGS``.

Usage: python scripts/build_shelter_test_ifc.py [output.ifc]
"""

from __future__ import annotations

import sys
from pathlib import Path
from typing import Any

import ifcopenshell
import ifcopenshell.api.document
import ifcopenshell.api.group
import ifcopenshell.api.root
import ifcopenshell.guid

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from pragmatic_bim.ifc2rdf.reference.catalog import resolve_reference_path  # noqa: E402

REFERENCE = resolve_reference_path()
if REFERENCE is None or not (REFERENCE / "generators").is_dir():
    sys.exit("No pragmaticBIM Reference checkout with generators/ (set PBS_REFERENCE_PATH).")
sys.path.insert(0, str(REFERENCE))

from generators.base import assign_pset, assign_qto, create_multi_storey_shell  # noqa: E402
from generators.covering import add_covering  # noqa: E402
from generators.parts import add_extruded_product, rect_polyline  # noqa: E402
from generators.slab import add_slab  # noqa: E402
from generators.space import _create_space_entity  # noqa: E402
from generators.wall import add_opening_filling, add_opening_in_wall, add_wall  # noqa: E402

UG = -3.0
HEIGHT = 2.6
T = 0.3
SHOCK_PSET = "PBIM_Schocksicherheit"
SHOCK_TYPES = {
    "AnchorCount": "IfcInteger",
    "AnchorShockResistance": "IfcReal",
    "AnchorSpacingX": "IfcLengthMeasure",
    "AnchorSpacingY": "IfcLengthMeasure",
    "CentreOfGravityHeight": "IfcLengthMeasure",
    "Mass": "IfcReal",
    "NaturalFrequency": "IfcReal",
    "ShockDeflection": "IfcLengthMeasure",
    "ShockDamper": "IfcBoolean",
    "ShockTestRequired": "IfcBoolean",
    "PassiveShockSafety": "IfcBoolean",
    "ReinforcementConnection": "IfcBoolean",
}

# name, IFC class, predefined type, ObjectType, space, (x0, y0, x1, y1), z0, height, TW Schock data, expected
COMPONENTS: list[tuple[str, str, str, str | None, str, tuple[float, float, float, float], float, float, dict[str, Any], str]] = [
    (
        "Belüftungsaggregat VA 150", "IfcUnitaryEquipment", "AIRHANDLER", None, "Schutzraum",
        (0.3, 0.3, 1.1, 1.5), 0.0, 1.2,
        {"FunctionCategory": "survival", "FixingType": "post_installed_anchor", "AnchorApprovalNumber": "BABS-D-21-034",
         "AnchorCount": 8, "AnchorShockResistance": 5.0, "AnchorSpacingX": 0.8, "AnchorSpacingY": 1.2,
         "CentreOfGravityHeight": 0.6, "Mass": 170.0, "ShockTestRequired": True, "ApprovalNumber": "BABS-SR-2021-150",
         "ProofLevel": "basis"},
        "§8 fails: TW Schock worked example, S_d 6.0 kN > R_d 5.0 kN; §7.2 fails: no fixing calculation",
    ),
    (
        "Gasfilter GF 150", "IfcUnitaryEquipment", "USERDEFINED", "Gasfilter", "Schutzraum",
        (1.4, 0.3, 1.9, 0.8), 0.0, 1.0,
        {"FunctionCategory": "survival", "FixingType": "cast_in", "AnchorCount": 4, "AnchorShockResistance": 4.0,
         "Mass": 60.0, "NaturalFrequency": 30.0, "ShockTestRequired": True},
        "§6.3 fails (no ETA), §5.2 fails (no approval), §8 fails (2 · a_max above 16 Hz), §8.1 warns (no damper)",
    ),
    (
        "Abwasserpumpe AP 1", "IfcPump", "SUBMERSIBLEPUMP", None, "Schutzraum",
        (6.6, 0.4, 7.2, 1.0), 0.15, 0.6,
        {"FunctionCategory": "living", "FixingType": "plinth_post_cast", "AnchorCount": 4, "AnchorShockResistance": 6.0,
         "Mass": 45.0, "ShockDeflection": 0.05, "ShockDamper": True},
        "§6.4 fails: plinth without reinforcement connection; §3.2 passes: nearest neighbour besides the plinth is 0.15 m away, swing path 0.05 m",
    ),
    (
        "Liegestelle 1", "IfcFurniture", "BED", None, "Schutzraum",
        (1.0, 5.2, 2.9, 6.0), 0.0, 1.9,
        {"FunctionCategory": "living", "FixingType": "post_installed_anchor", "AnchorApprovalNumber": "BABS-D-19-112",
         "AnchorCount": 4, "AnchorShockResistance": 7.0, "AnchorSpacingX": 1.8, "AnchorSpacingY": 0.7,
         "CentreOfGravityHeight": 0.9, "Mass": 60.0},
        "passes: S_d 6.5 kN <= R_d 7.0 kN",
    ),
    (
        "Liegestelle 2", "IfcFurniture", "BED", None, "Schutzraum",
        (3.2, 5.2, 5.1, 6.0), 0.0, 1.9,
        {"FunctionCategory": "living", "FixingType": "post_installed_anchor", "AnchorApprovalNumber": "BABS-D-19-112",
         "AnchorCount": 4, "AnchorShockResistance": 7.0, "AnchorSpacingX": 1.8, "AnchorSpacingY": 0.7,
         "CentreOfGravityHeight": 0.9, "Mass": 60.0},
        "passes: S_d 6.5 kN <= R_d 7.0 kN",
    ),
    (
        "Regal R1", "IfcFurniture", "SHELF", None, "Schutzraum",
        (0.3, 1.55, 1.3, 1.95), 0.0, 2.0,
        {"FunctionCategory": "other", "FixingType": "unfixed", "Mass": 35.0},
        "§4.3: unfixed, 0.05 m from the ventilation unit (needs the computed within_shock_reach)",
    ),
    (
        "Schrank S1", "IfcFurniture", "FILECABINET", None, "Schutzraum",
        (7.0, 4.5, 7.9, 5.1), 0.0, 2.0,
        {"FunctionCategory": "other", "FixingType": "post_installed_anchor", "Mass": 40.0},
        "§4.3: anchors without approval above 10 kg count as unfixed; nothing vital in reach",
    ),
]

# Suspended ceilings at UG + 2.30: name, space, (x0, y0, x1, y1), TW Schock data, expected
CEILINGS: list[tuple[str, str, tuple[float, float, float, float], dict[str, Any], str]] = [
    (
        "Abgehängte Decke Schleuse 1", "Schleuse", (8.3, 0.0, 10.15, 2.5), {},
        "§4.1 and §4.3.2 fail: no function category, passive shock safety not verified",
    ),
    (
        "Abgehängte Decke Schleuse 2", "Schleuse", (10.15, 0.0, 12.0, 2.5),
        {"FunctionCategory": "other", "PassiveShockSafety": True},
        "§4.1 and §4.3.2 pass",
    ),
]

# name, (x0, y0, x1, y1), long name
SPACES = {
    "Schutzraum": ((0.0, 0.0, 8.0, 6.0), "Pflichtschutzraum SR 01"),
    "Schleuse": ((8.3, 0.0, 12.0, 2.5), "Schleuse"),
    "Korridor": ((8.3, 2.8, 12.0, 6.0), "Korridor UG"),
}


def _wall(f, ctx, storey, name, rect, *, external, doors=()):
    """Wall over plan rectangle ``rect``; ``doors`` are ``(name, start, width, height, external)``."""
    x0, y0, x1, y1 = rect
    along_x = (x1 - x0) >= (y1 - y0)
    origin = (x0, y0, UG) if along_x else (x1, y0, UG)
    direction = (1.0, 0.0) if along_x else (0.0, 1.0)
    length, thickness = (x1 - x0, y1 - y0) if along_x else (y1 - y0, x1 - x0)
    start = x0 if along_x else y0
    wall = add_wall(
        f, name=name, body_context=ctx, storey=storey, origin=origin, length=length, height=HEIGHT,
        thickness=thickness, direction_xy=direction, predefined_type="SOLIDWALL",
        openings=[{"along": s - start, "sill": 0.0, "width": w, "height": h} for _, s, w, h, _ in doors],
    )
    assign_pset(f, wall, "Pset_WallCommon", {"IsExternal": external, "LoadBearing": True},
                datatypes={"IsExternal": "IfcBoolean", "LoadBearing": "IfcBoolean"})
    for door_name, s, w, h, door_external in doors:
        common = dict(body_context=ctx, along=s - start, sill=0.0, clear_width=w, clear_height=h,
                      wall_thickness=thickness, wall_origin=origin, direction_xy=direction)
        opening = add_opening_in_wall(f, host=wall, name=f"{door_name}-Öffnung", **common)
        door = add_opening_filling(f, opening=opening, name=door_name, storey=storey, ifc_class="IfcDoor",
                                   predefined_type="DOOR", frame_width=0.10, exterior_protrusion=0.0, **common)
        assign_pset(f, door, "Pset_DoorCommon", {"IsExternal": door_external}, datatypes={"IsExternal": "IfcBoolean"})
    return wall


def build(path: Path) -> Path:
    f, _project, _site, _building, (ug, eg), ctx = create_multi_storey_shell(
        "Schutzraum TW Schock Test", storey_names=("UG", "EG"), storey_elevations=(UG, 0.0)
    )

    spaces = {}
    for name, ((x0, y0, x1, y1), long_name) in SPACES.items():
        spaces[name] = _create_space_entity(
            f, storey=ug, body_context=ctx, name=name, long_name=long_name, predefined_type="SPACE",
            polyline=rect_polyline(x0, y0, x1, y1), height=HEIGHT,
            quantities={"NetFloorArea": (x1 - x0) * (y1 - y0), "Height": HEIGHT},
            properties={"Pset_SpaceCommon": {"IsExternal": False}},
            properties_datatypes={"Pset_SpaceCommon": {"IsExternal": "IfcBoolean"}},
        )

    _wall(f, ctx, ug, "Aussenwand Süd", (-T, -T, 12.0 + T, 0.0), external=True)
    _wall(f, ctx, ug, "Aussenwand Nord", (-T, 6.0, 12.0 + T, 6.0 + T), external=True)
    _wall(f, ctx, ug, "Aussenwand West", (-T, 0.0, 0.0, 6.0), external=True)
    _wall(f, ctx, ug, "Aussenwand Ost", (12.0, 0.0, 12.0 + T, 6.0), external=True,
          doors=[("Ausgang UG", 4.0, 1.0, 2.1, True)])
    _wall(f, ctx, ug, "Schutzraumwand", (8.0, 0.0, 8.3, 6.0), external=False,
          doors=[("Panzertür PT 1", 0.9, 0.8, 1.85, False)])
    _wall(f, ctx, ug, "Schleusenwand", (8.3, 2.5, 12.0, 2.8), external=False,
          doors=[("Panzertür PT 2", 10.6, 0.8, 1.85, False)])

    for slab, storey, z, predefined in (("Bodenplatte UG", ug, UG - 0.4, "BASESLAB"), ("Decke über UG", eg, -0.4, "FLOOR")):
        product = add_slab(f, name=slab, body_context=ctx, storey=storey,
                           polyline=rect_polyline(-T, -T, 12.0 + T, 6.0 + T), thickness=0.4, z_bottom=z,
                           predefined_type=predefined)
        assign_pset(f, product, "Pset_SlabCommon", {"LoadBearing": True, "IsExternal": predefined == "BASESLAB"},
                    datatypes={"LoadBearing": "IfcBoolean", "IsExternal": "IfcBoolean"})

    plinth = add_slab(f, name="Betonsockel Pumpe", body_context=ctx, storey=ug,
                      polyline=rect_polyline(6.5, 0.3, 7.3, 1.1), thickness=0.15, z_bottom=UG,
                      predefined_type="USERDEFINED")
    plinth.ObjectType = "Betonsockel"
    assign_pset(f, plinth, SHOCK_PSET, {"ReinforcementConnection": False}, datatypes=SHOCK_TYPES)

    for name, space, (x0, y0, x1, y1), shock, _ in CEILINGS:
        ceiling = add_covering(f, name=name, body_context=ctx, storey=ug,
                               polyline=rect_polyline(x0, y0, x1, y1), thickness=0.05, z_bottom=UG + 2.3,
                               predefined_type="CEILING")
        f.create_entity(
            "IfcRelSpaceBoundary", GlobalId=ifcopenshell.guid.new(), RelatingSpace=spaces[space],
            RelatedBuildingElement=ceiling, PhysicalOrVirtualBoundary="PHYSICAL", InternalOrExternalBoundary="INTERNAL",
        )
        if shock:
            assign_pset(f, ceiling, SHOCK_PSET, shock, datatypes=SHOCK_TYPES)

    elements = {}
    for name, ifc_class, predefined, object_type, space, (x0, y0, x1, y1), z0, h, shock, _ in COMPONENTS:
        element = add_extruded_product(f, ifc_class=ifc_class, name=name, body_context=ctx, storey=spaces[space],
                                       polyline=rect_polyline(x0, y0, x1, y1), thickness=h, z_bottom=UG + z0,
                                       predefined_type=predefined)
        if object_type:
            element.ObjectType = object_type
        assign_pset(f, element, SHOCK_PSET, shock, datatypes=SHOCK_TYPES)
        qto = {"IfcUnitaryEquipment": "Qto_UnitaryEquipmentBaseQuantities", "IfcPump": "Qto_PumpBaseQuantities"}.get(ifc_class)
        if qto:
            assign_qto(f, element, qto, {"GrossWeight": shock["Mass"]})
        elements[name] = element

    clearance = add_extruded_product(f, ifc_class="IfcBuildingElementProxy", name="Schwingraum Pumpe",
                                     body_context=ctx, storey=ug, polyline=rect_polyline(6.55, 0.35, 7.25, 1.05),
                                     thickness=0.75, z_bottom=UG + 0.15, predefined_type="USERDEFINED")
    clearance.ObjectType = "Bewegungsfläche"

    zone = ifcopenshell.api.root.create_entity(f, ifc_class="IfcZone", name="Schutzraum SR 01")
    zone.ObjectType = "Schutzbau"
    ifcopenshell.api.group.assign_group(f, products=[spaces["Schutzraum"], spaces["Schleuse"]], group=zone)
    assign_pset(f, zone, "PBIM_Schutzbau", {"Schutzbautyp": "Pflichtschutzraum", "Schutzgrad": "Basis", "Schutzplaetze": 40},
                datatypes={"Schutzplaetze": "IfcInteger"})

    information = ifcopenshell.api.document.add_information(f)
    ifcopenshell.api.document.edit_information(
        f, information=information, attributes={"Identification": "B18002", "Name": "Montageanleitung VA 150"})
    reference = ifcopenshell.api.document.add_reference(f, information=information)
    ifcopenshell.api.document.edit_reference(
        f, reference=reference, attributes={"Identification": "B18002", "Location": "montageanleitung-va150.pdf"})
    ifcopenshell.api.document.assign_document(f, products=[elements["Belüftungsaggregat VA 150"]], document=reference)

    path.parent.mkdir(parents=True, exist_ok=True)
    f.write(str(path))
    return path


if __name__ == "__main__":
    out = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "temp" / "schutzraum-tw-schock.ifc"
    print(build(out))
    for name, *_, expected in (*COMPONENTS, *CEILINGS):
        print(f"  {name}: {expected}")
