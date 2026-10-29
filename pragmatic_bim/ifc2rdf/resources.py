"""Locate the contract, mapping, and classification files shipped with the package or repo."""

from __future__ import annotations

from pathlib import Path

_PACKAGE_DIR = Path(__file__).resolve().parent.parent


def data_root() -> Path:
    """Directory that contains ``contract/`` and ``classification/``.

    Wheels bundle both under ``pragmatic_bim/_data``; a source checkout uses the repo root.
    """
    for candidate in (_PACKAGE_DIR / "_data", _PACKAGE_DIR.parent):
        if (candidate / "contract" / "mapping").is_dir():
            return candidate
    raise FileNotFoundError("Cannot locate contract/ data directory for pragmatic_bim.ifc2rdf")


def default_mapping_path() -> Path:
    return data_root() / "contract" / "mapping" / "ifc_mapping.merged.yaml"


def default_schema_path() -> Path:
    return data_root() / "contract" / "00_pragmatic_bim_data_contract.yaml"


def classification_dir() -> Path:
    return data_root() / "classification"
