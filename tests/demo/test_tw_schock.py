"""TW Schock rules on a hand-written shelter graph (the contract lacks the missing: terms they need)."""

from __future__ import annotations

from rdflib import Graph

from demo.app.checks import RULES_DIR, ShaclCheck, run_checks
from pragmatic_bim.ifc2rdf.report import ConversionReport

SHELTER = """
@prefix pbs: <https://schema.pragmaticbim.ch/> .
@prefix missing: <https://schema.pragmaticbim.ch/missing/> .
@prefix ifc: <https://w3id.org/ifc/IFC4_ADD2#> .
@prefix e: <https://example.org/e/> .

e:zone a pbs:ZoneContext ; pbs:ifc_global_id "zone" ;
    pbs:zone_type missing:zone_type_civil_defence_shelter .
e:space a pbs:Space ; pbs:ifc_global_id "space" ; pbs:parent_zone e:zone .

# TW Schock §8.3: 170 kg, 8 anchors, b_x 0.8 m, b_y 1.2 m, h_z 0.6 m -> S_d,shock 6.0 kN.
e:unit a pbs:Equipment ; pbs:ifc_global_id "unit" ; pbs:name "Belüftungsaggregat" ; pbs:parent_space e:space ;
    pbs:quantity_values [ pbs:quantity_type missing:quantity_type_mass ; pbs:quantity_value 1.7e2 ] ;
    pbs:performance_properties
        [ pbs:property_key missing:structural_property_shock_function_category ; pbs:property_value_string "survival" ] ,
        [ pbs:property_key missing:structural_property_shock_fixing_type ; pbs:property_value_string "post_installed_anchor" ] ,
        [ pbs:property_key missing:structural_property_anchor_approval_number ; pbs:property_value_string "BABS D 123" ] ,
        [ pbs:property_key missing:structural_property_anchor_count ; pbs:property_value_number 8.0e0 ] ,
        [ pbs:property_key missing:structural_property_anchor_shock_resistance ; pbs:property_value_number 5.0e0 ] ,
        [ pbs:property_key missing:structural_property_centre_of_gravity_height ; pbs:property_value_number 6.0e-1 ] ,
        [ pbs:property_key missing:structural_property_anchor_spacing_x ; pbs:property_value_number 8.0e-1 ] ,
        [ pbs:property_key missing:structural_property_anchor_spacing_y ; pbs:property_value_number 1.2e0 ] ,
        [ pbs:property_key missing:structural_property_shock_test_required ; pbs:property_value_boolean true ] ,
        [ pbs:property_key missing:structural_property_shock_approval_number ; pbs:property_value_string "BABS 2021-17" ] ;
    pbs:geometry_representations [ pbs:geometry_representation "body_3d" ;
        pbs:bbox_min_x 0.0e0 ; pbs:bbox_max_x 1.0e0 ; pbs:bbox_min_y 0.0e0 ; pbs:bbox_max_y 1.4e0 ;
        pbs:bbox_min_z 0.0e0 ; pbs:bbox_max_z 1.2e0 ] ;
    missing:documented_by e:manual .
e:manual a pbs:Artifact ; pbs:classifications [ pbs:classification_code "B18002" ] .

e:shelf a pbs:Equipment ; pbs:ifc_global_id "shelf" ; pbs:name "Regal" ; pbs:parent_space e:space ;
    pbs:performance_properties
        [ pbs:property_key missing:structural_property_shock_function_category ; pbs:property_value_string "other" ] ,
        [ pbs:property_key missing:structural_property_shock_fixing_type ; pbs:property_value_string "unfixed" ] ;
    missing:within_shock_reach e:unit .

e:ceiling a pbs:Boundary ; pbs:ifc_global_id "ceiling" ;
    pbs:boundary_type ifc:IfcCoveringTypeEnum.CEILING ; pbs:bounded_space e:space .

e:pump a pbs:Equipment ; pbs:ifc_global_id "pump" ; pbs:name "Abwasserpumpe" ; pbs:parent_space e:space ;
    pbs:rests_on e:plinth ;
    pbs:neighbours
        [ pbs:neighbour e:plinth ; pbs:horizontal_clear_distance 0.0e0 ; pbs:vertical_clear_distance 0.0e0 ] ,
        [ pbs:neighbour e:wall ; pbs:horizontal_clear_distance 3.0e-2 ; pbs:vertical_clear_distance 0.0e0 ] ,
        [ pbs:neighbour e:duct ; pbs:horizontal_clear_distance 0.0e0 ; pbs:vertical_clear_distance 8.0e-2 ] ,
        [ pbs:neighbour e:pipe ; pbs:horizontal_clear_distance 3.0e-2 ; pbs:vertical_clear_distance 3.0e-2 ] ;
    pbs:performance_properties
        [ pbs:property_key missing:structural_property_shock_function_category ; pbs:property_value_string "living" ] ,
        [ pbs:property_key missing:structural_property_shock_fixing_type ; pbs:property_value_string "plinth_post_cast" ] ,
        [ pbs:property_key missing:structural_property_shock_deflection ; pbs:property_value_number 5.0e-2 ] ;
    pbs:geometry_representations [ pbs:geometry_representation "body_3d" ;
        pbs:bbox_min_x 3.0e0 ; pbs:bbox_max_x 3.5e0 ; pbs:bbox_min_y 0.0e0 ; pbs:bbox_max_y 5.0e-1 ;
        pbs:bbox_min_z 0.0e0 ; pbs:bbox_max_z 6.0e-1 ] .
e:plinth a pbs:SeparatorSlab ; pbs:ifc_global_id "plinth" ; pbs:name "Sockel" .
e:wall a pbs:SeparatorWall ; pbs:ifc_global_id "wall" ; pbs:name "Wand" .
e:duct a pbs:Equipment ; pbs:ifc_global_id "duct" ; pbs:name "Lüftungskanal" .
e:pipe a pbs:Equipment ; pbs:ifc_global_id "pipe" ; pbs:name "Rohr" .
e:clearance a pbs:ReservedVolume ; pbs:ifc_global_id "clearance" ;
    pbs:reserved_volume_type pbs:reserved_volume_type_movement_clearance ;
    pbs:intersects_elements e:pump , e:shelf .

e:server a pbs:Equipment ; pbs:ifc_global_id "server" ; pbs:parent_space e:space ;
    pbs:performance_properties
        [ pbs:property_key missing:structural_property_shock_function_category ; pbs:property_value_string "facility" ] ,
        [ pbs:property_key missing:structural_property_shock_fixing_type ; pbs:property_value_string "cast_in" ] ,
        [ pbs:property_key missing:structural_property_natural_frequency ; pbs:property_value_number 3.0e1 ] .

e:outside a pbs:Equipment ; pbs:ifc_global_id "outside" .
"""


def _results(rated: float | None = None) -> dict[str, object]:
    data = SHELTER if rated is None else SHELTER.replace("pbs:property_value_number 5.0e0", f"pbs:property_value_number {rated}e0")
    graph = Graph().parse(data=data, format="turtle")
    report = ConversionReport(source_system="test", contract_version="0", mapping_version="0")
    checks = run_checks(graph, report, [ShaclCheck(RULES_DIR / "tw_schock.shacl.ttl")])
    return {r.id: r for r in checks}


def test_tw_schock_rules():
    results = _results()

    category = results["rule-ShockFunctionCategory"]
    assert set(category.checked) == {"unit", "shelf", "ceiling", "pump", "server"}
    assert category.failed == ["ceiling"]

    calculation = results["rule-FixingCalculation"]
    assert calculation.checked == ["pump", "server", "unit"]
    unit = [i for i in calculation.items if i["guid"] == "unit"]
    assert [i["message"] for i in unit] == ["Anchor force 6.0 kN exceeds R_d,shock 5.0 kN (F = 26.6 kN on 8 anchors)."]
    assert unit[0]["message_de"].startswith("Dübelkraft 6.0 kN")
    assert "unit" not in _results(rated=6.5)["rule-FixingCalculation"].failed

    assert results["rule-ApprovedAnchors"].checked == ["unit"] and results["rule-ApprovedAnchors"].failed == []
    assert results["rule-ComponentApproval"].failed == []
    assert [i["message"] for i in results["rule-ShockDocuments"].items] == ["No fixing calculation (KBOB B07)."]
    assert results["rule-PassiveShockSafety"].failed == ["shelf"]
    assert "Belüftungsaggregat" in results["rule-PassiveShockSafety"].items[0]["message"]
    assert results["rule-SuspendedCeiling"].failed == ["ceiling"]
    assert sorted(i["message"] for i in results["rule-ShockClearance"].items) == [
        "Regal lies in the movement clearance.",
        "Rohr is 0.03 m away horizontally and 0.03 m vertically; swing path 0.05 m.",
        "Wand is 0.03 m away horizontally and 0 m vertically; swing path 0.05 m.",
    ]
    assert [i["message"] for i in results["rule-PostCastPlinth"].items] == [
        "Plinth Sockel has no reinforcement connection to the floor slab."
    ]
    assert results["rule-CastInFixing"].failed == ["server"]
    assert results["rule-StiffComponentDamper"].failed == ["server"]
    assert results["rule-StiffComponentDamper"].severity == "warning"
    assert {i["guid"]: i["message"] for i in calculation.items if i["guid"] != "unit"} == {
        "pump": "Shock proof of the fixing not possible: mass, anchor count or R_d,shock missing.",
        "server": "Shock proof of the fixing not possible: mass, anchor count or R_d,shock missing.",
    }
    assert all("outside" not in r.checked for r in results.values())


def test_tw_schock_rules_not_applicable_without_shelters():
    graph = Graph().parse(data=SHELTER.replace("missing:zone_type_civil_defence_shelter", "pbs:zone_type_fire"), format="turtle")
    report = ConversionReport(source_system="test", contract_version="0", mapping_version="0")
    results = run_checks(graph, report, [ShaclCheck(RULES_DIR / "tw_schock.shacl.ttl")])
    assert len(results) == 11
    assert {r.status for r in results} == {"na"}
