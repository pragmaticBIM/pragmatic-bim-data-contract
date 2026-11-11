"""pragmaticBIM Reference applicability parsing, scoring, and catalog loading."""

from __future__ import annotations

import pytest
from checks import REFERENCE_FIXTURE

from pragmatic_bim.ifc2rdf.reference import ReferenceCatalog, resolve_reference_path
from pragmatic_bim.ifc2rdf.reference.applicability import (
    Clause,
    Operation,
    clause_applies_to_schema,
    entity_classes,
    evaluate,
    parse,
)


def test_parse_precedence_and_quotes():
    expr = parse('entity_ifc4=IfcBuildingElementProxy AND ObjectType="Maintenance space" OR entity_ifc2x3=IfcWall')
    assert expr == Operation(
        "OR",
        (
            Operation(
                "AND",
                (Clause("entity_ifc4", "IfcBuildingElementProxy"), Clause("ObjectType", "Maintenance space")),
            ),
            Clause("entity_ifc2x3", "IfcWall"),
        ),
    )
    assert entity_classes(expr) == {"IfcBuildingElementProxy", "IfcWall"}


def test_parse_existence_clause_and_pset_property():
    expr = parse("(entity_ifc4=IfcSpace AND Pset_SpaceCommon.IsExternal=FALSE AND Reference)")
    assert expr.operands[1] == Clause("Pset_SpaceCommon.IsExternal", "FALSE")
    assert expr.operands[2] == Clause("Reference", None)


@pytest.mark.parametrize("text", ["(entity_ifc4=IfcWall", "entity_ifc4=IfcWall )", 'ObjectType="open'])
def test_parse_errors(text):
    with pytest.raises(ValueError):
        parse(text)


def test_score_counts_clauses_of_best_branch():
    expr = parse("(entity_ifc4=IfcSlab AND IsExternal=TRUE AND LoadBearing=TRUE) OR entity_ifc4=IfcSlab")
    facts = {"entity_ifc4": True, "IsExternal": True, "LoadBearing": True}
    assert evaluate(expr, lambda c: facts.get(c.attribute, False)) == (True, 3)
    facts["IsExternal"] = False
    assert evaluate(expr, lambda c: facts.get(c.attribute, False)) == (True, 1)
    assert evaluate(expr, lambda c: False) == (False, 0)


def test_ifc4x3_files_fall_back_to_ifc4_clauses():
    assert clause_applies_to_schema("entity_ifc4", "IFC4X3_ADD2", has_ifc4x3_clause=False)
    assert not clause_applies_to_schema("entity_ifc4", "IFC4X3_ADD2", has_ifc4x3_clause=True)
    assert clause_applies_to_schema("entity_ifc4_3", "IFC4X3_ADD2", has_ifc4x3_clause=True)
    assert not clause_applies_to_schema("entity_ifc2x3", "IFC4", has_ifc4x3_clause=False)


def test_fixture_catalog_loads_every_language_variant():
    catalog = ReferenceCatalog.load(REFERENCE_FIXTURE)
    assert not catalog.errors
    assert catalog.version is None  # the fixture is not a git checkout of its own
    by_id = catalog.by_id()
    maintenance = by_id["pragmaticbim:element/architecture-maintenance-space"]
    assert len(maintenance.expressions) == 4  # de, en, fr, it
    assert maintenance.uri == "https://pragmaticbim.ch/id/element/architecture-maintenance-space"
    assert maintenance.label == "Maintenance space"
    assert by_id["pragmaticbim:element/architecture-railing"].entity_classes == {"IfcRailing"}


def test_resolve_reference_path(tmp_path, monkeypatch):
    assert resolve_reference_path(REFERENCE_FIXTURE) == REFERENCE_FIXTURE
    with pytest.raises(FileNotFoundError):
        resolve_reference_path(tmp_path)
    monkeypatch.setenv("PBS_REFERENCE_PATH", str(REFERENCE_FIXTURE))
    assert resolve_reference_path() == REFERENCE_FIXTURE
