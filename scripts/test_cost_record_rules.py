#!/usr/bin/env python3
"""Cost-stage and amount rules on CostRecord (generated models + pragmatic_bim.rules)."""

from __future__ import annotations

import json
import sys
import unittest
import warnings
from decimal import Decimal
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT))

from pragmatic_bim import rules  # noqa: E402
from pragmatic_bim.models import Classification, CostRecord, CostRequirement  # noqa: E402

JSON_SCHEMA = REPO_ROOT / "site" / "schema" / "pragmatic-bim.schema.json"

try:
    import jsonschema
except ImportError:  # pragma: no cover - optional dependency
    jsonschema = None


def stage(code: str) -> dict:
    return {"classification_scheme": rules.COST_STAGES, "classification_code": code}


def cost_record(**overrides) -> dict:
    payload = {
        "id": "cr-1",
        "name": "Rohbau",
        "content_kind": "virtual",
        "cost_record_role": "estimate",
        "currency": "CHF",
    }
    payload.update(overrides)
    return payload


D1 = cost_record(unit_cost=120.5, classifications=[stage("approved_budget")])
D3 = cost_record(amount="1250000.00")


class CostRecordRuleTests(unittest.TestCase):
    def test_d1_estimate_with_one_cost_stage_is_valid(self) -> None:
        record = rules.validate(CostRecord(**D1))
        self.assertEqual(rules.cost_stage_codes(record), ["approved_budget"])

    def test_d2_two_cost_stages_are_invalid(self) -> None:
        record = CostRecord(**cost_record(
            unit_cost=10,
            classifications=[stage("early_estimate"), stage("approved_budget")],
        ))
        with self.assertRaises(rules.ContractRuleError) as ctx:
            rules.validate(record)
        self.assertIn("at most one 'cost-stages'", str(ctx.exception))

    def test_two_cost_stages_allowed_outside_estimate_role(self) -> None:
        record = CostRecord(**cost_record(
            cost_record_role="actual",
            unit_cost=10,
            classifications=[stage("contract_amendment"), stage("expectation")],
        ))
        self.assertEqual(rules.issues(record), [])

    def test_other_schemes_do_not_count_as_cost_stages(self) -> None:
        record = CostRecord(**cost_record(
            unit_cost=10,
            classifications=[
                stage("approved_budget"),
                {"classification_scheme": "ebkp-h", "classification_code": "C"},
            ],
        ))
        self.assertEqual(rules.issues(record), [])

    def test_d3_amount_only_is_valid(self) -> None:
        record = rules.validate(CostRecord(**D3))
        self.assertEqual(record.amount, Decimal("1250000.00"))
        self.assertIsNone(record.unit_cost)

    def test_amount_must_be_non_negative(self) -> None:
        with self.assertRaises(ValueError):
            CostRecord(**cost_record(amount="-1"))

    def test_d4_neither_amount_nor_unit_cost_is_invalid(self) -> None:
        with self.assertRaises(rules.ContractRuleError) as ctx:
            rules.validate(CostRecord(**cost_record()))
        self.assertIn("either amount or unit_cost is required", str(ctx.exception))

    def test_d4_dict_payload_requires_model_name(self) -> None:
        self.assertEqual(rules.issues(cost_record()), [])
        self.assertEqual(
            rules.issues(cost_record(), "CostRecord"),
            ["either amount or unit_cost is required"],
        )

    def test_d5_legacy_cost_category_is_valid_with_deprecation_warning(self) -> None:
        record = CostRecord(**cost_record(unit_cost=10, cost_category="Rohbau"))
        with self.assertWarns(DeprecationWarning) as ctx:
            rules.validate(record)
        self.assertIn("CostRecord.cost_category is deprecated", str(ctx.warning))
        self.assertEqual(record.cost_category, "Rohbau")

    def test_cost_requirement_cost_category_warns(self) -> None:
        requirement = CostRequirement(
            id="req-1",
            name="Budget cap",
            content_kind="requirement",
            currency="CHF",
            cost_category="Rohbau",
        )
        with self.assertWarns(DeprecationWarning):
            rules.validate(requirement)

    def test_no_warning_without_cost_category(self) -> None:
        with warnings.catch_warnings():
            warnings.simplefilter("error")
            rules.validate(CostRecord(**D1))

    def test_d6_generated_models_round_trip(self) -> None:
        for payload in (D1, D3):
            with self.subTest(payload=payload):
                record = CostRecord(**payload)
                dumped = record.model_dump(mode="json", exclude_none=True)
                self.assertEqual(dumped, payload)
                again = CostRecord.model_validate_json(record.model_dump_json())
                self.assertEqual(again, record)

    def test_cost_stage_classification_is_a_plain_classification(self) -> None:
        entry = Classification(**stage("expectation"))
        self.assertEqual(entry.classification_scheme, "cost-stages")


@unittest.skipIf(jsonschema is None, "jsonschema not installed")
class CostRecordJsonSchemaTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        schema = json.loads(JSON_SCHEMA.read_text(encoding="utf-8"))
        cost_record_schema = {**schema["$defs"]["CostRecord"], "$defs": schema["$defs"]}
        cls.validator = jsonschema.Draft202012Validator(cost_record_schema)

    def test_amount_or_unit_cost_required(self) -> None:
        self.assertTrue(self.validator.is_valid(cost_record(amount=100)))
        self.assertTrue(self.validator.is_valid(cost_record(unit_cost=1.5)))
        self.assertFalse(self.validator.is_valid(cost_record()))

    def test_cost_category_still_accepted(self) -> None:
        self.assertTrue(self.validator.is_valid(cost_record(unit_cost=1, cost_category="Rohbau")))


if __name__ == "__main__":
    unittest.main()
