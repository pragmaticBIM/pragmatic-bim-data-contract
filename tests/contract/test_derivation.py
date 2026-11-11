"""Derivation records how a value or relation was obtained."""

import pytest
from pydantic import ValidationError

from pragmatic_bim.models import (
    ConnectionVirtual,
    Derivation,
    DerivationSourceKind,
    QuantityValue,
)


def test_quantity_measured_from_geometry_carries_method_and_reference():
    height = QuantityValue(
        quantity_type="height",
        quantity_value=1.20,
        quantity_unit="m",
        derivation=Derivation(
            derivation_source_kind=DerivationSourceKind.IFC_geometry,
            derivation_method="height_above_reference_surface",
            derivation_method_version="0.1",
            derivation_tolerance=0.005,
            derivation_tolerance_unit="m",
            derivation_inputs=["el:pavement_course"],
        ),
    )
    assert height.derivation.derivation_source_kind == DerivationSourceKind.IFC_geometry
    assert height.derivation.derivation_inputs == ["el:pavement_course"]


def test_connection_from_contact_test():
    contact = ConnectionVirtual(
        id="el:contact_railing_edge_beam",
        content_kind="virtual",
        name="Railing on edge beam",
        connection_virtual_type="structural_joint",
        connects_physical_elements=["el:railing_north", "el:edge_beam_north"],
        derivation=Derivation(
            derivation_source_kind="ifc_geometry",
            derivation_method="contact_test",
            derivation_tolerance=0.005,
            derivation_tolerance_unit="m",
        ),
    )
    assert contact.derivation.derivation_method == "contact_test"


def test_source_kind_is_required():
    with pytest.raises(ValidationError):
        Derivation(derivation_method="contact_test")


def test_tolerance_must_not_be_negative():
    with pytest.raises(ValidationError):
        Derivation(derivation_source_kind="ifc_geometry", derivation_tolerance=-0.001)
