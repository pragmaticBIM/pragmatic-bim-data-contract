"""Load element definitions from a pragmaticBIM Reference checkout (``elements/*.yaml``)."""

from __future__ import annotations

import os
import subprocess
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import yaml

from pragmatic_bim.ifc2rdf.reference.applicability import (
    ENTITY_ATTRIBUTES,
    Expression,
    clauses,
    entity_classes,
    parse,
)
from pragmatic_bim.ifc2rdf.resources import repo_root

ENV_VAR = "PBS_REFERENCE_PATH"
DEFAULT_RELATIVE_PATH = Path("..") / "elementplan" / "pragmaticBIM-reference"
# Prefix of the pragmaticBIM Elementplan schema (elementplan.linkml.yaml).
PREFIXES = {"pragmaticbim": "https://pragmaticbim.ch/id/"}
INACTIVE_STATUSES = {"deprecated", "inactive", "retired"}


@dataclass(frozen=True)
class ElementDefinition:
    id: str
    """CURIE, for example ``pragmaticbim:element/architecture-railing``."""
    code: str | None
    names: dict[str, str]
    expressions: tuple[Expression, ...]
    """Parsed applicability, one per language variant (identical variants collapsed)."""
    entity_classes: frozenset[str]
    has_ifc4x3_clause: bool = False

    @property
    def uri(self) -> str:
        prefix, _, local = self.id.partition(":")
        return PREFIXES[prefix] + local if prefix in PREFIXES else self.id

    @property
    def label(self) -> str | None:
        return self.names.get("en") or self.names.get("de") or next(iter(self.names.values()), None)


@dataclass
class ReferenceCatalog:
    root: Path
    elements: list[ElementDefinition]
    version: str | None = None
    errors: dict[str, str] = field(default_factory=dict)
    """Element id → reason the applicability could not be parsed."""

    @classmethod
    def load(cls, root: Path | str) -> "ReferenceCatalog":
        root = Path(root)
        folder = root / "elements"
        if not folder.is_dir():
            raise FileNotFoundError(f"{folder} not found (expected a pragmaticBIM Reference checkout)")
        elements: list[ElementDefinition] = []
        errors: dict[str, str] = {}
        for path in sorted(folder.glob("*.yaml")):
            data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
            element_id = data.get("id")
            if not element_id or str(data.get("status", "active")).lower() in INACTIVE_STATUSES:
                continue
            try:
                expressions = _expressions(data.get("applicability"))
            except ValueError as exc:
                errors[element_id] = str(exc)
                continue
            if not expressions:
                continue
            names = {k: str(v) for k, v in (data.get("name") or {}).items() if v}
            all_clauses = [c for e in expressions for c in clauses(e)]
            elements.append(
                ElementDefinition(
                    id=element_id,
                    code=data.get("code"),
                    names=names,
                    expressions=expressions,
                    entity_classes=frozenset(c for e in expressions for c in entity_classes(e)),
                    has_ifc4x3_clause=any(c.attribute == "entity_ifc4_3" for c in all_clauses),
                )
            )
        return cls(root=root, elements=elements, version=_git_version(root), errors=errors)

    def by_id(self) -> dict[str, ElementDefinition]:
        return {e.id: e for e in self.elements}


def _expressions(applicability: Any) -> tuple[Expression, ...]:
    if isinstance(applicability, dict):
        texts = [applicability.get("de"), *(v for k, v in sorted(applicability.items()) if k != "de")]
    else:
        texts = [applicability]
    seen: list[str] = []
    for text in texts:
        text = " ".join(str(text or "").split())
        if text and text != "null" and text not in seen:
            seen.append(text)
    expressions = tuple(parse(text) for text in seen)
    for expression in expressions:
        if not any(c.attribute in ENTITY_ATTRIBUTES for c in clauses(expression)):
            raise ValueError("applicability names no entity_ifc* class")
    return expressions


def _git_version(root: Path) -> str | None:
    """``git describe`` of the checkout; None when ``root`` is not the top of a git work tree."""

    def git(*args: str) -> str | None:
        try:
            result = subprocess.run(
                ["git", *args], cwd=root, capture_output=True, text=True, check=True, timeout=10
            )
        except (OSError, subprocess.SubprocessError):
            return None
        return result.stdout.strip() or None

    top = git("rev-parse", "--show-toplevel")
    if top is None or Path(top).resolve() != root.resolve():
        return None
    return git("describe", "--tags", "--always", "--dirty")


def resolve_reference_path(explicit: Path | str | None = None) -> Path | None:
    """Reference checkout: ``explicit``, then ``$PBS_REFERENCE_PATH``, then the sibling checkout.

    The sibling default is ``../elementplan/pragmaticBIM-reference`` relative to the
    repository root and only applies to source checkouts. Returns None when no
    candidate exists.
    """
    if explicit:
        path = Path(explicit)
        if not (path / "elements").is_dir():
            raise FileNotFoundError(f"{path} is not a pragmaticBIM Reference checkout (no elements/)")
        return path
    env = os.environ.get(ENV_VAR)
    if env:
        return resolve_reference_path(env)
    root = repo_root()
    if root is not None:
        candidate = (root / DEFAULT_RELATIVE_PATH).resolve()
        if (candidate / "elements").is_dir():
            return candidate
    return None
