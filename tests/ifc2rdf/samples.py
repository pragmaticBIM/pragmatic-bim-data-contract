"""Public IFC exports used by the ifc2rdf tests.

The files are not redistributed with this repository (their source repositories do not
declare a license). They are downloaded from a pinned commit and verified by sha256.
"""

from __future__ import annotations

import hashlib
import os
import urllib.request
from dataclasses import dataclass, field
from pathlib import Path


@dataclass(frozen=True)
class Sample:
    id: str
    url: str
    sha256: str
    source_system: str
    # Contract class -> node count expected from the IFC content.
    counts: dict[str, int] = field(default_factory=dict)


SAMPLES = [
    Sample(
        id="revit-duplex",
        url="https://raw.githubusercontent.com/youshengCode/IfcSampleFiles/"
        "7e6927982d7e57b29409bb631ef93d6770ef0665/Ifc2x3_Duplex_Architecture.ifc",
        sha256="b347a2c8aa8fff6db896a4417a9c50c22ac0ccd7c5cfc22b99b8d29336c606ed",
        source_system="revit",
        counts={
            "Space": 21,
            "LevelContext": 4,
            "BuildingContext": 1,
            "SeparatorWall": 57,
            "SeparatorSlab": 21,
            "ConnectionPhysical": 38,
        },
    ),
    Sample(
        id="archicad-fzk-haus",
        url="https://raw.githubusercontent.com/opensourceBIM/TestFiles/"
        "df9bb50f549b29b01f04d5481859971c864ef388/TestData/data/AC11-FZK-Haus-IFC.ifc",
        sha256="c89069da241e149166e0551128aaf088def582a48c267e67a08ca88c3f1319a0",
        source_system="archicad",
        counts={
            "Space": 7,
            "LevelContext": 2,
            "BuildingContext": 1,
            "SeparatorWall": 13,
            "SeparatorSlab": 4,
            "ConnectionPhysical": 16,
        },
    ),
    Sample(
        id="vectorworks-nvw-dcr",
        url="https://raw.githubusercontent.com/giofox96/Graph_ML-Giovanni_Carlo_Volpe/"
        "3bf70d9764d7f919bd964a319659baef1e1c71b2/Graph%20ML%20--%20NOTEBOOKS/"
        "Supporting%20Files/NVW_DCR-LOD100_Arch.ifc",
        sha256="c5daf00dd22eebcf05cc19c13ad5ab14f1954f6733f43ac5f04c6d7e949140f8",
        source_system="vectorworks",
        counts={"Space": 48, "LevelContext": 8, "BuildingContext": 1, "SeparatorSlab": 11},
    ),
    Sample(
        id="vectorworks-unicode",
        url="https://raw.githubusercontent.com/opensourceBIM/TestFiles/"
        "baf434036eec2f8e7f5b313629faba4cef8c6ec5/TestData/data/japanesechars/vectorworks_unicode.ifc",
        sha256="1f37720aed7ba65376a1ea144c9f62b6db4197829bb1562d57398cbd2caea084",
        source_system="vectorworks",
        counts={
            "LevelContext": 3,
            "BuildingContext": 1,
            "SeparatorWall": 8,
            "SeparatorSlab": 4,
            "ConnectionPhysical": 2,
        },
    ),
]


def cache_dir() -> Path:
    override = os.environ.get("PBS_IFC_SAMPLES_DIR")
    if override:
        return Path(override)
    base = Path(os.environ.get("XDG_CACHE_HOME") or Path.home() / ".cache")
    return base / "pragmatic-bim" / "ifc-samples"


def fetch(sample: Sample) -> Path:
    """Return a verified local copy of ``sample``, downloading it when missing."""
    target = cache_dir() / f"{sample.id}.ifc"
    if target.is_file() and hashlib.sha256(target.read_bytes()).hexdigest() == sample.sha256:
        return target
    with urllib.request.urlopen(sample.url, timeout=60) as response:
        data = response.read()
    digest = hashlib.sha256(data).hexdigest()
    if digest != sample.sha256:
        raise ValueError(f"{sample.id}: sha256 mismatch ({digest} != {sample.sha256})")
    target.parent.mkdir(parents=True, exist_ok=True)
    tmp = target.with_suffix(".part")
    tmp.write_bytes(data)
    tmp.replace(target)
    return target
