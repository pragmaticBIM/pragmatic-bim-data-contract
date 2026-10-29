"""Apply the value normalization rules declared in the mapping (``normalize_*`` conventions)."""

from __future__ import annotations

import re
from typing import Any

COMPARATORS = {
    "gte": lambda a, b: a >= b,
    "gt": lambda a, b: a > b,
    "lte": lambda a, b: a <= b,
    "lt": lambda a, b: a < b,
    "eq": lambda a, b: a == b,
}


def normalize(spec: dict[str, Any], raw: Any) -> list[tuple[str | None, str | float | bool]]:
    """Normalized ``(property_key, value)`` pairs for ``raw``; empty when the value is rejected.

    The first pair carries the declared key (``None``); further pairs come from
    ``suffix_routes`` and name their own key.
    """
    value_type = spec.get("value_type", "string")
    if value_type == "boolean":
        flag = _boolean(spec, raw)
        return [] if flag is None else [(None, flag)]
    if value_type == "number":
        number = _number(spec, raw)
        return [] if number is None else [(None, number)]
    return _string(spec, raw)


def _boolean(spec: dict[str, Any], raw: Any) -> bool | None:
    if isinstance(raw, bool):
        return raw
    text = str(raw).strip().casefold()
    if text in {str(v).casefold() for v in spec.get("true_values") or []}:
        return True
    if text in {str(v).casefold() for v in spec.get("false_values") or []}:
        return False
    return None


def _number(spec: dict[str, Any], raw: Any) -> float | None:
    if isinstance(raw, bool):
        return None
    if isinstance(raw, (int, float)):
        value = float(raw)
    else:
        match = re.search(spec.get("number_pattern", r"[0-9]+(?:\.[0-9]+)?"), str(raw))
        if match is None:
            return None
        value = float(match.group(0).replace(",", "."))
    for operator, bound in (spec.get("accept_range") or {}).items():
        if not COMPARATORS[operator](value, bound):
            return None
    return value


def _string(spec: dict[str, Any], raw: Any) -> list[tuple[str | None, str | float | bool]]:
    text = str(raw)
    text = "".join(text.split()) if spec.get("remove_whitespace") else text.strip()
    if spec.get("upper_case"):
        text = text.upper()
    separator = spec.get("suffix_separator")
    head, *suffixes = text.split(separator) if separator else [text]
    pattern = spec.get("accept_pattern")
    if not head or (pattern and re.fullmatch(pattern, head) is None):
        return []
    values: list[tuple[str | None, str | float | bool]] = [(None, head)]
    for suffix in suffixes:
        for route in spec.get("suffix_routes") or []:
            if re.fullmatch(route["pattern"], suffix):
                values.append((route["property_key"], suffix))
                break
    return values
