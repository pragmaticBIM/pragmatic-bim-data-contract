"""Demo stand-in that lifts the TW Schock metadata of the converter onto the missing: terms."""

from __future__ import annotations

from rdflib import Graph, Literal, URIRef

from demo.app.checks import RULES_DIR, ShaclCheck, run_checks
from demo.app.tw_schock_data import MISSING, PBS, add_missing_terms
from pragmatic_bim.ifc2rdf.report import ConversionReport

CONVERTED = """
@prefix pbs: <https://schema.pragmaticbim.ch/> .
@prefix ifcowl: <https://w3id.org/ifc/IFC4_ADD2#> .
@prefix e: <https://example.org/e/> .

e:zone a pbs:ZoneContext ; pbs:ifc_global_id "zone" ; pbs:zone_type ifcowl:IfcSpatialZone ;
    pbs:group_members e:space ;
    pbs:metadata [ pbs:metadata_key "PBIM_Schutzbau.Schutzbautyp" ; pbs:metadata_value "Pflichtschutzraum" ] ,
        [ pbs:metadata_key "PBIM_Schutzbau.Schutzgrad" ; pbs:metadata_value "Basis" ] .
e:space a pbs:Space ; pbs:ifc_global_id "space" .
e:unit a pbs:Equipment ; pbs:ifc_global_id "unit" ; pbs:parent_space e:space ;
    pbs:geometry_representations [ pbs:geometry_representation "body_3d" ;
        pbs:bbox_min_x 0.0e0 ; pbs:bbox_max_x 1.0e0 ; pbs:bbox_min_y 0.0e0 ; pbs:bbox_max_y 1.4e0 ;
        pbs:bbox_min_z 0.0e0 ; pbs:bbox_max_z 1.2e0 ] ;
    pbs:metadata
        [ pbs:metadata_key "PBIM_Schocksicherheit.FunctionCategory" ; pbs:metadata_value "survival" ] ,
        [ pbs:metadata_key "PBIM_Schocksicherheit.FixingType" ; pbs:metadata_value "post_installed_anchor" ] ,
        [ pbs:metadata_key "PBIM_Schocksicherheit.AnchorApprovalNumber" ; pbs:metadata_value "BABS-D-21-034" ] ,
        [ pbs:metadata_key "PBIM_Schocksicherheit.AnchorCount" ; pbs:metadata_value "8" ] ,
        [ pbs:metadata_key "PBIM_Schocksicherheit.AnchorShockResistance" ; pbs:metadata_value "5.0" ] ,
        [ pbs:metadata_key "PBIM_Schocksicherheit.AnchorSpacingX" ; pbs:metadata_value "0.8" ] ,
        [ pbs:metadata_key "PBIM_Schocksicherheit.AnchorSpacingY" ; pbs:metadata_value "1.2" ] ,
        [ pbs:metadata_key "PBIM_Schocksicherheit.CentreOfGravityHeight" ; pbs:metadata_value "0.6" ] ,
        [ pbs:metadata_key "PBIM_Schocksicherheit.Mass" ; pbs:metadata_value "170.0" ] ,
        [ pbs:metadata_key "PBIM_Schocksicherheit.ShockTestRequired" ; pbs:metadata_value "false" ] .
"""


def test_add_missing_terms():
    graph = Graph().parse(data=CONVERTED, format="turtle")
    zone, unit = URIRef("https://example.org/e/zone"), URIRef("https://example.org/e/unit")
    assert add_missing_terms(graph) > 0
    assert (zone, PBS.zone_type, MISSING.zone_type_civil_defence_shelter) in graph
    assert (zone, MISSING.shock_protection_level, MISSING.shock_protection_level_basis) in graph
    values = {graph.value(r, PBS.property_key): r for r in graph.objects(unit, PBS.performance_properties)}
    count = graph.value(values[MISSING.structural_property_anchor_count], PBS.property_value_number)
    assert count == Literal(8.0)
    test_required = graph.value(values[MISSING.structural_property_shock_test_required], PBS.property_value_boolean)
    assert test_required == Literal(False)
    mass = next(r for r in graph.objects(unit, PBS.quantity_values))
    assert graph.value(mass, PBS.quantity_type) == MISSING.quantity_type_mass

    report = ConversionReport(source_system="test", contract_version="0", mapping_version="0")
    results = {r.id: r for r in run_checks(graph, report, [ShaclCheck(RULES_DIR / "tw_schock.shacl.ttl")])}
    assert [i["message"] for i in results["rule-FixingCalculation"].items] == [
        "Anchor force 6.0 kN exceeds R_d,shock 5.0 kN (F = 26.6 kN on 8 anchors)."
    ]
