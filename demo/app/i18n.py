"""German labels for the demo UI; the technical mode shows the contract identifiers.

``labels.de.yaml`` holds the UI strings and the labels for classes, relations and slots.
Enum values take their German label from the contract (``alt_descriptions.de``), resolved
through the range of the slot that carries them, since several enums share IFC meanings.
"""

from __future__ import annotations

from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path
from typing import Any

import yaml

LANGUAGES = {"de": "Deutsch", "tech": "Technisch"}
DEFAULT_LANGUAGE = "de"
COOKIE = "pbs_lang"
LABELS_PATH = Path(__file__).with_name("labels.de.yaml")
CONTRACT_DIR = Path(__file__).resolve().parents[2] / "contract"
CONTRACT_PREFIXES = {"ifcowl:": "ifc:"}


@dataclass(frozen=True)
class Vocabulary:
    ui: dict[str, str]
    classes: dict[str, str]
    relations: dict[str, list[str]]
    """Predicate -> [label read from the subject, label read from the object]."""
    slots: dict[str, str]
    values: dict[str, str]
    slot_values: dict[str, dict[str, str]]


def _compact(meaning: str) -> str:
    for prefix, replacement in CONTRACT_PREFIXES.items():
        if meaning.startswith(prefix):
            return replacement + meaning.removeprefix(prefix)
    return meaning


@lru_cache(maxsize=1)
def german() -> Vocabulary:
    labels = yaml.safe_load(LABELS_PATH.read_text(encoding="utf-8"))
    ranges: dict[str, str] = {}
    enums: dict[str, dict[str, set[str]]] = {}
    for path in sorted(CONTRACT_DIR.glob("*.yaml")):
        schema = yaml.safe_load(path.read_text(encoding="utf-8"))
        if not isinstance(schema, dict):
            continue
        for slot, spec in (schema.get("slots") or {}).items():
            if spec and spec.get("range"):
                ranges[slot] = spec["range"]
        for enum, spec in (schema.get("enums") or {}).items():
            for value in ((spec or {}).get("permissible_values") or {}).values():
                value = value or {}
                de = ((value.get("alt_descriptions") or {}).get("de") or {}).get("description")
                if value.get("meaning") and de:
                    enums.setdefault(enum, {}).setdefault(_compact(value["meaning"]), set()).add(de)

    # The graph stores the meaning, not the enum value; meanings shared by several values
    # (all SeparatorWallType values are ifc:IfcWall) get no label.
    by_meaning: dict[str, set[str]] = {}
    for values in enums.values():
        for meaning, de in values.items():
            by_meaning.setdefault(meaning, set()).update(de)

    def unique(values: dict[str, set[str]]) -> dict[str, str]:
        return {meaning: next(iter(de)) for meaning, de in values.items() if len(de) == 1}

    return Vocabulary(
        ui=labels["ui"],
        classes=labels["classes"],
        relations=labels["relations"],
        slots=labels["slots"],
        values={**unique(by_meaning), **labels["values"]},
        slot_values={f"pbs:{slot}": unique(enums[enum]) for slot, enum in ranges.items() if enum in enums},
    )


class Labels:
    """Display labels for one language; ``tech`` returns the identifiers unchanged."""

    def __init__(self, lang: str) -> None:
        self.lang = lang if lang in LANGUAGES else DEFAULT_LANGUAGE
        self.vocab = german() if self.lang == "de" else None

    @classmethod
    def from_cookies(cls, cookies: dict[str, str]) -> "Labels":
        return cls(cookies.get(COOKIE, DEFAULT_LANGUAGE))

    @property
    def html_lang(self) -> str:
        return "de" if self.vocab else "en"

    def t(self, text: str) -> str:
        return self.vocab.ui.get(text, text) if self.vocab else text

    def cls(self, name: str) -> str:
        local = name.removeprefix("pbs:")
        return self.vocab.classes.get(local, local) if self.vocab else name

    def relation(self, predicate: str, direction: str = "out") -> str:
        if not self.vocab:
            return predicate.removeprefix("pbs:")
        labels = self.vocab.relations.get(predicate)
        if not labels:
            return predicate.removeprefix("pbs:")
        return labels[0] if direction == "out" else labels[1]

    def slot(self, key: str) -> str:
        return self.vocab.slots.get(key, key) if self.vocab else key

    def value(self, key: str, value: Any) -> Any:
        if not self.vocab:
            return value
        if isinstance(value, bool):
            return "ja" if value else "nein"
        if not isinstance(value, str):
            return value
        return self.vocab.slot_values.get(key, {}).get(value) or self.vocab.values.get(value, value)

    def title(self, check: dict[str, Any]) -> str:
        return (self.vocab and check.get("title_de")) or check["title"]

    def description(self, check: dict[str, Any]) -> str:
        return (self.vocab and check.get("description_de")) or check.get("description", "")

    def message(self, item: dict[str, Any]) -> str:
        return (self.vocab and item.get("message_de")) or item["message"]

    def client(self) -> dict[str, Any]:
        """Labels for ``graph.js`` and ``bridge.js``."""
        if not self.vocab:
            return {"classes": {}, "relations": {}, "ui": {}}
        ui = ("Relations", "All", "Could not load")
        return {
            "classes": self.vocab.classes,
            "relations": self.vocab.relations,
            "ui": {text: self.t(text) for text in ui},
        }
