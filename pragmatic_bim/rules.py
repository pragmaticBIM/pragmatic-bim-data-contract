"""Cross-slot contract rules that the generated Pydantic models do not enforce.

gen-pydantic keeps class-level ``any_of`` and similar constraints only as
``linkml_meta``; it does not emit validators for them. Per-scheme cardinality on
``classifications`` cannot be expressed in LinkML at all. Call :func:`validate`
after constructing a model (or on a plain payload dict) to apply these rules.

This module imports nothing from the package so consumers that generate their
own models from the contract YAML can vendor it unchanged.

    from pragmatic_bim import rules
    from pragmatic_bim.models import Classification, CostRecord

    record = rules.validate(CostRecord(
        id="cr-1", content_kind="virtual", cost_record_role="estimate",
        amount="1250000", currency="CHF",
        classifications=[Classification(classification_scheme=rules.COST_STAGES,
                                        classification_code="approved_budget")]))
"""

from __future__ import annotations

import warnings
from enum import Enum
from typing import Any, Callable

COST_STAGES = "cost-stages"
COST_STAGE_CODES = (
    "early_estimate",
    "approved_budget",
    "contract_amendment",
    "expectation",
)

DEPRECATED_SLOTS: dict[str, dict[str, str]] = {
    "CostRecord": {
        "cost_category": "use a classifications entry with classification_scheme 'cost-stages'",
    },
    "CostRequirement": {
        "cost_category": "use a classifications entry with classification_scheme 'cost-stages'",
    },
}


class ContractRuleError(ValueError):
    """Raised when an instance violates one or more contract rules."""

    def __init__(self, model_name: str, issues: list[str]) -> None:
        """Store the model name and a copy of its contract rule violations."""
        self.model_name = model_name
        self.issues = list(issues)
        super().__init__(f"{model_name} violates contract rules: " + "; ".join(self.issues))


def _get(instance: Any, slot: str) -> Any:
    """Read a dict key or object attribute, returning None when absent."""
    if isinstance(instance, dict):
        return instance.get(slot)
    return getattr(instance, slot, None)


def _text(value: Any) -> Any:
    """Unwrap Enum members to their values, leaving other values unchanged."""
    return value.value if isinstance(value, Enum) else value


def _is_set(value: Any) -> bool:
    """Return whether a value is neither None nor an empty string."""
    return value is not None and value != ""


def cost_stage_codes(instance: Any) -> list[str]:
    """``classification_code`` values of every ``cost-stages`` classification on the instance."""
    return [
        _get(entry, "classification_code")
        for entry in _get(instance, "classifications") or []
        if _get(entry, "classification_scheme") == COST_STAGES
    ]


def cost_record_issues(instance: Any) -> list[str]:
    """Return violations of cost presence and estimate stage cardinality rules."""
    issues: list[str] = []
    if not _is_set(_get(instance, "amount")) and not _is_set(_get(instance, "unit_cost")):
        issues.append("either amount or unit_cost is required")
    stages = cost_stage_codes(instance)
    if _text(_get(instance, "cost_record_role")) == "estimate" and len(stages) > 1:
        issues.append(
            f"cost_record_role 'estimate' allows at most one '{COST_STAGES}' classification, "
            f"got {len(stages)} ({', '.join(map(str, stages))})"
        )
    return issues


RULES: dict[str, Callable[[Any], list[str]]] = {
    "CostRecord": cost_record_issues,
}


def _resolve_model_name(instance: Any, model_name: str | None) -> str | None:
    """Use an explicit model name or find a known class in the instance's MRO."""
    if model_name is not None:
        return model_name
    if isinstance(instance, dict):
        return None
    known = RULES.keys() | DEPRECATED_SLOTS.keys()
    for cls in type(instance).__mro__:
        if cls.__name__ in known:
            return cls.__name__
    return None


def issues(instance: Any, model_name: str | None = None) -> list[str]:
    """Rule violations for ``instance``; empty when valid or when no rules apply.

    ``model_name`` is required for plain dict payloads and otherwise inferred from
    the instance class (or its nearest ancestor with rules).
    """
    name = _resolve_model_name(instance, model_name)
    check = RULES.get(name) if name else None
    return check(instance) if check else []


def deprecated_slots_in_use(instance: Any, model_name: str | None = None) -> dict[str, str]:
    """Deprecated slots populated on ``instance``, mapped to their replacement hint."""
    name = _resolve_model_name(instance, model_name)
    return {
        slot: hint
        for slot, hint in DEPRECATED_SLOTS.get(name or "", {}).items()
        if _is_set(_get(instance, slot))
    }


def validate(instance: Any, model_name: str | None = None) -> Any:
    """Apply contract rules to ``instance`` and return it unchanged.

    Emits ``DeprecationWarning`` for populated deprecated slots and raises
    :class:`ContractRuleError` when a rule is violated.
    """
    name = _resolve_model_name(instance, model_name) or type(instance).__name__
    for slot, hint in deprecated_slots_in_use(instance, name).items():
        warnings.warn(f"{name}.{slot} is deprecated; {hint}", DeprecationWarning, stacklevel=2)
    found = issues(instance, name)
    if found:
        raise ContractRuleError(name, found)
    return instance
