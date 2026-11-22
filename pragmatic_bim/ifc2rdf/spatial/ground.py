"""``resolve_ground_floor``: set LevelContext above_ground / is_ground_floor flags per building.

Resolution order (one source per building, recorded on every storey):

1. ``Pset_BuildingStoreyCommon.AboveGround`` / ``EntranceLevel`` (already mapped when present)
2. Storey naming convention (``EG``/``00``, ``U##``, ``FD``, ``##``, ``{base}.Z``)
3. Lowest storey with elevation ≥ 0 as ground floor; storeys at or above it as above ground

Exactly one ground floor per building; when several candidates qualify, the lowest
elevation wins and the conversion report counts the ambiguity.
"""

from __future__ import annotations

import re
from typing import Any

from pragmatic_bim.ifc2rdf.model import Node
from pragmatic_bim.ifc2rdf.spatial.context import SpatialContext

_METHOD = "resolve_ground_floor"
_TOKEN = re.compile(r"^([A-Za-z0-9]+(?:\.[Zz])?)$")
_BASEMENT = re.compile(r"^U\d{2}$", re.I)
_UPPER = re.compile(r"^\d{2}$")
_INTERMEDIATE = re.compile(r"^(.+)\.Z$", re.I)


def resolve_ground_floor(ctx: SpatialContext, spec: dict[str, Any]) -> None:
    selector = spec.get("subject") or {"contract_class": "LevelContext"}
    storeys = ctx.nodes_matching(selector)
    by_building: dict[Any, list[Node]] = {}
    for storey in storeys:
        building = _parent_building(storey)
        by_building.setdefault(building, []).append(storey)

    for building_key, levels in by_building.items():
        levels = sorted(levels, key=lambda n: (_elevation(n) is None, _elevation(n) or 0.0, n.global_id))
        source = _choose_source(ctx, levels)
        if source == "ifc_property":
            _apply_ifc(ctx, levels)
        elif source == "name_convention":
            _apply_names(ctx, levels)
        else:
            _apply_elevation(ctx, levels)
        _ensure_one_ground_floor(ctx, levels)
        for storey in levels:
            _set(ctx, storey, "ground_reference_source", source)
        ctx.conv.report.computed_relations[f"ground_floor ({source})"] += 1


def _choose_source(ctx: SpatialContext, levels: list[Node]) -> str:
    if any(_has_ifc_flags(ctx, level) for level in levels):
        return "ifc_property"
    if any(_name_kind(level)[0] != "unknown" for level in levels):
        return "name_convention"
    return "elevation"


def _has_ifc_flags(ctx: SpatialContext, level: Node) -> bool:
    if _slot_bool(level, "above_ground") is not None or _slot_bool(level, "is_ground_floor") is not None:
        return True
    pset = ctx.psets(level).get("Pset_BuildingStoreyCommon") or {}
    above = pset.get("AboveGround")
    entrance = pset.get("EntranceLevel")
    return _logical_bool(above) is not None or isinstance(entrance, bool) or _logical_bool(entrance) is not None


def _apply_ifc(ctx: SpatialContext, levels: list[Node]) -> None:
    for level in levels:
        pset = ctx.psets(level).get("Pset_BuildingStoreyCommon") or {}
        above = _logical_bool(pset.get("AboveGround"))
        if above is None:
            above = _slot_bool(level, "above_ground")
        if above is not None:
            _set(ctx, level, "above_ground", above)
        entrance = pset.get("EntranceLevel")
        ground = _logical_bool(entrance) if not isinstance(entrance, bool) else entrance
        if ground is None:
            ground = _slot_bool(level, "is_ground_floor")
        if ground is not None:
            _set(ctx, level, "is_ground_floor", ground)


def _apply_names(ctx: SpatialContext, levels: list[Node]) -> None:
    by_token: dict[str, Node] = {}
    parsed: list[tuple[Node, str, str | None]] = []
    for level in levels:
        kind, base = _name_kind(level)
        parsed.append((level, kind, base))
        token = _name_token(level)
        if token and kind != "intermediate":
            by_token[token.upper()] = level

    for level, kind, base in parsed:
        if kind == "intermediate":
            continue
        if kind == "ground":
            _set(ctx, level, "is_ground_floor", True)
            _set(ctx, level, "above_ground", True)
        elif kind == "below":
            _set(ctx, level, "is_ground_floor", False)
            _set(ctx, level, "above_ground", False)
        elif kind == "above":
            _set(ctx, level, "is_ground_floor", False)
            _set(ctx, level, "above_ground", True)

    for level, kind, base in parsed:
        if kind != "intermediate" or base is None:
            continue
        parent = by_token.get(base.upper())
        if parent is None:
            continue
        above = _slot_bool(parent, "above_ground")
        ground = _slot_bool(parent, "is_ground_floor")
        if above is not None:
            _set(ctx, level, "above_ground", above)
        if ground is not None:
            _set(ctx, level, "is_ground_floor", False)


def _apply_elevation(ctx: SpatialContext, levels: list[Node]) -> None:
    candidates = [level for level in levels if (_elevation(level) is not None and _elevation(level) >= 0)]
    ground = min(candidates, key=lambda n: (_elevation(n), n.global_id)) if candidates else None
    ground_elev = _elevation(ground) if ground is not None else None
    for level in levels:
        elev = _elevation(level)
        is_ground = ground is not None and level is ground
        _set(ctx, level, "is_ground_floor", is_ground)
        if elev is None or ground_elev is None:
            continue
        _set(ctx, level, "above_ground", elev >= ground_elev)


def _ensure_one_ground_floor(ctx: SpatialContext, levels: list[Node]) -> None:
    grounds = [level for level in levels if _slot_bool(level, "is_ground_floor") is True]
    if len(grounds) <= 1:
        if len(grounds) == 1:
            for level in levels:
                if level is not grounds[0]:
                    _set(ctx, level, "is_ground_floor", False)
        return
    chosen = min(grounds, key=lambda n: (_elevation(n) is None, _elevation(n) or 0.0, n.global_id))
    ctx.conv.report.computed_relations["ground_floor (ambiguous)"] += 1
    for level in levels:
        _set(ctx, level, "is_ground_floor", level is chosen)


def _name_kind(level: Node) -> tuple[str, str | None]:
    token = _name_token(level)
    if not token:
        return "unknown", None
    match = _INTERMEDIATE.fullmatch(token)
    if match:
        return "intermediate", match.group(1)
    upper = token.upper()
    if upper in ("EG", "00"):
        return "ground", None
    if upper == "FD" or _BASEMENT.fullmatch(upper):
        return "below", None
    if _UPPER.fullmatch(upper):
        return "above", None
    return "unknown", None


def _name_token(level: Node) -> str:
    raw = None
    if level.entity is not None:
        raw = level.entity.Name or level.entity.LongName
    if raw is None:
        values = level.values.get("name") or []
        raw = values[0].toPython() if values else None
    text = str(raw or "").strip()
    if not text:
        return ""
    token = text.split()[0]
    return token if _TOKEN.fullmatch(token) else token


def _parent_building(level: Node) -> Any:
    parents = level.values.get("parent_building") or []
    return parents[0] if parents else None


def _elevation(level: Node) -> float | None:
    values = level.values.get("elevation") or []
    if not values:
        return None
    return float(values[0].toPython())


def _slot_bool(level: Node, slot: str) -> bool | None:
    values = level.values.get(slot) or []
    if not values:
        return None
    return bool(values[0].toPython())


def _logical_bool(raw: Any) -> bool | None:
    if isinstance(raw, bool):
        return raw
    if raw is None:
        return None
    text = str(raw).strip().upper()
    if text in ("TRUE", "T", ".T.", "1"):
        return True
    if text in ("FALSE", "F", ".F.", "0"):
        return False
    return None


def _set(ctx: SpatialContext, node: Node, slot: str, value: Any) -> None:
    node.values.pop(slot, None)
    ctx.conv.writer.set(node, slot, value)


__all__ = ["resolve_ground_floor"]
