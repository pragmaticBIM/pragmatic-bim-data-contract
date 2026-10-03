"""Lookup helpers for the SKOS classification schemes shipped with the contract.

Codes are `skos:notation` values (for example ``SEC-BAU-CLI-GC``) and schemes are
``dcterms:identifier`` values (for example ``AbstractCompanySectorClassification``),
matching ``Classification.classification_code`` / ``classification_scheme``.
"""

from __future__ import annotations

import json
from functools import lru_cache
from importlib import resources

COMPANY_SECTOR = "AbstractCompanySectorClassification"
PERSON_RELATIONSHIP = "AbstractPersonRelationshipType"
TOPIC = "AbstractTopicClassification"
ROLES = "AbstractRoles"


@lru_cache(maxsize=1)
def _index() -> dict:
    with resources.files(__package__).joinpath("taxonomies.json").open(encoding="utf-8") as fh:
        return json.load(fh)


def schemes() -> list[str]:
    """Identifiers of every scheme in the index."""
    return sorted(_index())


def concepts(scheme: str) -> dict[str, dict]:
    """All concepts of a scheme, keyed by notation."""
    try:
        return _index()[scheme]["concepts"]
    except KeyError:
        raise KeyError(f"unknown scheme {scheme!r}; known: {', '.join(schemes())}") from None


def codes(scheme: str, *, under: str | None = None) -> list[str]:
    """Notations of a scheme, optionally only those at or below ``under``."""
    all_codes = sorted(concepts(scheme))
    if under is None:
        return all_codes
    return [code for code in all_codes if code == under or under in ancestors(scheme, code)]


def label(scheme: str, code: str, lang: str = "en") -> str:
    labels = concepts(scheme)[code]["labels"]
    return labels.get(lang) or labels.get("en") or next(iter(labels.values()), code)


def is_valid(scheme: str, code: str) -> bool:
    return code in concepts(scheme)


def ancestors(scheme: str, code: str) -> list[str]:
    """Broader codes from the immediate parent up to the top concept."""
    chain: list[str] = []
    current = concepts(scheme).get(code, {}).get("broader")
    while current and current not in chain:
        chain.append(current)
        current = concepts(scheme).get(current, {}).get("broader")
    return chain


def choices(scheme: str, *, under: str | None = None, lang: str = "en") -> dict[str, str]:
    """Code to label mapping, for prompts and select inputs."""
    return {code: label(scheme, code, lang) for code in codes(scheme, under=under)}


def describe(scheme: str, *, under: str | None = None, lang: str = "en") -> str:
    """Indented ``CODE — Label`` outline, compact enough to paste into a prompt."""
    lines = []
    for code in codes(scheme, under=under):
        depth = len(ancestors(scheme, code))
        if under is not None:
            depth -= len(ancestors(scheme, under))
        lines.append(f"{'  ' * max(depth, 0)}{code} — {label(scheme, code, lang)}")
    return "\n".join(lines)
