"""DerivedMeasurement gives multi-subject quantities their own identity."""

from pragmatic_bim.models import (
    ChangeType,
    DerivedMeasurement,
    Derivation,
    DerivationSourceKind,
    GeometryRepresentation,
    GeometryRepresentationType,
    MeasurementStatus,
    PropertyChange,
    PropertyPathKind,
    QuantityValue,
)


def test_clear_stair_width_measurement():
    measurement = DerivedMeasurement(
        id="meas:stair_clear_width",
        content_kind="measurement",
        name="Stair clear width",
        measurement_status=MeasurementStatus.Measured,
        applies_to_entities=["el:stair_flight", "el:railing_left", "el:railing_right"],
        quantity_values=[
            QuantityValue(
                quantity_type="clear_width",
                quantity_value=1.20,
                quantity_unit="m",
                derivation=Derivation(
                    derivation_source_kind=DerivationSourceKind.IFC_geometry,
                    derivation_method="perpendicular_clear_width",
                    derivation_method_version="0.1",
                    derivation_tolerance=0.005,
                    derivation_tolerance_unit="m",
                ),
            )
        ],
        geometry_representations=[
            GeometryRepresentation(
                geometry_reference="meas:stair_clear_width#line",
                geometry_representation=GeometryRepresentationType.number_3D_Path,
                geometry_format="wkt",
                geometry_wkt="LINESTRING Z (0 0 0, 1.2 0 0)",
            )
        ],
    )
    assert measurement.content_kind == "measurement"
    assert measurement.measurement_status == MeasurementStatus.Measured
    assert set(measurement.applies_to_entities) == {
        "el:stair_flight",
        "el:railing_left",
        "el:railing_right",
    }
    assert measurement.quantity_values[0].derivation.derivation_method == "perpendicular_clear_width"
    assert measurement.geometry_representations[0].geometry_wkt.startswith("LINESTRING Z")


def test_not_measurable_without_quantity():
    record = DerivedMeasurement(
        id="meas:gap_unknown",
        content_kind="measurement",
        name="Clear width unavailable",
        measurement_status=MeasurementStatus.Not_measurable,
        applies_to_entities=["el:railing_a", "el:railing_b"],
    )
    assert record.measurement_status == MeasurementStatus.Not_measurable
    assert record.quantity_values is None


def test_change_can_reference_derived_measurement():
    change = PropertyChange(
        id="chg:1",
        change_type=ChangeType.Property_Change,
        affected_subject="meas:stair_clear_width",
        affected_subject_id="meas:stair_clear_width",
        affected_subject_type="DerivedMeasurement",
        from_revision=1,
        to_revision=2,
        property_path="quantity_values[0].quantity_value",
        property_path_kind=PropertyPathKind.Schema_Slot,
        from_value="1.20",
        to_value="1.15",
    )
    assert change.affected_subject == "meas:stair_clear_width"
    assert change.affected_subject_type == "DerivedMeasurement"
