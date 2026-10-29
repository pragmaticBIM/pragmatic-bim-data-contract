"""Normalization rules declared in the mapping, applied to value variants.

Variants marked "sample" occur in the pinned public exports (tests/ifc2rdf/samples.py).
"""

from __future__ import annotations

import pytest

from pragmatic_bim.ifc2rdf.mapping import Mapping
from pragmatic_bim.ifc2rdf.normalize import normalize
from pragmatic_bim.ifc2rdf.resources import default_mapping_path

RULES = Mapping.load(default_mapping_path()).conventions


@pytest.mark.parametrize(
    ("raw", "expected"),
    [
        ("EI 90", [(None, "EI90")]),
        ("EI90", [(None, "EI90")]),
        ("ei 90", [(None, "EI90")]),
        (" EI 90 ", [(None, "EI90")]),
        ("EI 90-RF1", [(None, "EI90"), ("reaction_to_fire", "RF1")]),
        ("EI90-RF1", [(None, "EI90"), ("reaction_to_fire", "RF1")]),
        ("EI 90 - RF1", [(None, "EI90"), ("reaction_to_fire", "RF1")]),
        ("REI 60-RF2(cr)", [(None, "REI60"), ("reaction_to_fire", "RF2(CR)")]),
        ("EI 30-Sa", [(None, "EI30"), ("smoke_rating", "SA")]),
        ("EI 30-C", [(None, "EI30")]),
        ("REI 120", [(None, "REI120")]),
        ("F90", [(None, "F90")]),
        ("T30", [(None, "T30")]),
        ("Fire Rating", []),  # sample: Revit Duplex, Pset_DoorCommon / PSet_Revit_Type_Identity Data
        ("FireRating", []),  # sample: Revit Duplex, Pset_WindowCommon / PSet_Revit_Type_Other
        ("耐火等級レベル1", []),  # sample: Vectorworks unicode, Pset_ColumnCommon
        ("耐火等級レベル", []),  # sample: Vectorworks unicode, Pset_ColumnCommon
        ("-RF1", []),
        ("", []),
    ],
)
def test_fire_rating(raw, expected):
    assert normalize(RULES["normalize_fire_rating"], raw) == expected


@pytest.mark.parametrize(
    ("raw", "expected"),
    [
        ("Rw 52 dB", 52.0),
        ("52", 52.0),
        (52, 52.0),
        ("R'w = 45 (-1;-3)", 45.0),
        ("52,5 dB", 52.5),
        ("AcousticRating", None),
        ("SSK 2", None),
    ],
)
def test_acoustic_rating_db(raw, expected):
    assert normalize(RULES["normalize_acoustic_rating_db"], raw) == ([] if expected is None else [(None, expected)])


@pytest.mark.parametrize(
    ("raw", "expected"),
    [
        (0.3, 0.3),  # sample: ArchiCAD FZK-Haus, Pset_SlabCommon
        (0.4, 0.4),  # sample: ArchiCAD FZK-Haus, Pset_WallCommon / Pset_SlabCommon
        (1.4, 1.4),  # sample: ArchiCAD FZK-Haus, Pset_WindowCommon / Pset_DoorCommon
        (1.5, 1.5),  # sample: ArchiCAD FZK-Haus, Pset_WallCommon
        (2.0, 2.0),  # sample: ArchiCAD FZK-Haus, Pset_DoorCommon
        ("0,25 W/m2K", 0.25),
        (0, None),
        (True, None),
        ("n/a", None),
    ],
)
def test_thermal_transmittance(raw, expected):
    rule = RULES["normalize_thermal_transmittance"]
    assert normalize(rule, raw) == ([] if expected is None else [(None, expected)])


@pytest.mark.parametrize(
    ("raw", "expected"),
    [
        (True, True),  # sample: IsExternal / LoadBearing in all Revit and ArchiCAD exports
        (False, False),
        ("TRUE", True),
        (".F.", False),
        ("UNKNOWN", None),
        ("Exterior", None),
    ],
)
def test_boolean(raw, expected):
    assert normalize(RULES["normalize_boolean"], raw) == ([] if expected is None else [(None, expected)])
