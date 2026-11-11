"""Demo-only stand-in for TW Schock terms the contract lacks (``missing:`` in ``rules/tw_schock.shacl.ttl``).

The converter keeps the shelter data as metadata entries (``PBIM_Schutzbau.*`` on the zone,
``PBIM_Schocksicherheit.*`` on components) and drops IFC document references. This adds the
``missing:`` terms the rules read, so the rules can run before the contract carries them:

- zone with ``PBIM_Schutzbau.Schutzbautyp``: ``zone_type_civil_defence_shelter``; ``Schutzgrad``:
  ``shock_protection_level``
- ``PBIM_Schocksicherheit.<Key>``: performance property ``structural_property_<key>``; ``Mass``:
  quantity ``quantity_type_mass``
- ``IfcRelAssociatesDocument``: ``documented_by`` an Artifact classified with the document's
  Identification (KBOB code)
"""

from __future__ import annotations

from pathlib import Path

from rdflib import RDF, BNode, Graph, Literal, Namespace, URIRef

PBS = Namespace("https://schema.pragmaticbim.ch/")
MISSING = Namespace("https://schema.pragmaticbim.ch/missing/")
SHELTER_PSET = "PBIM_Schutzbau"
SHOCK_PSET = "PBIM_Schocksicherheit"

STRING, NUMBER, BOOLEAN = "string", "number", "boolean"
SHOCK_PROPERTIES = {
    "FunctionCategory": ("shock_function_category", STRING),
    "ShockTestRequired": ("shock_test_required", BOOLEAN),
    "ApprovalNumber": ("shock_approval_number", STRING),
    "ProofLevel": ("shock_proof_level", STRING),
    "FixingType": ("shock_fixing_type", STRING),
    "AnchorApprovalNumber": ("anchor_approval_number", STRING),
    "AnchorEta": ("anchor_eta", STRING),
    "AnchorCount": ("anchor_count", NUMBER),
    "AnchorShockResistance": ("anchor_shock_resistance", NUMBER),
    "AnchorSpacingX": ("anchor_spacing_x", NUMBER),
    "AnchorSpacingY": ("anchor_spacing_y", NUMBER),
    "CentreOfGravityHeight": ("centre_of_gravity_height", NUMBER),
    "NaturalFrequency": ("natural_frequency", NUMBER),
    "ShockDeflection": ("shock_deflection", NUMBER),
    "ShockDamper": ("shock_damper", BOOLEAN),
    "PassiveShockSafety": ("passive_shock_safety", BOOLEAN),
    "ReinforcementConnection": ("reinforcement_connection", BOOLEAN),
}
PROTECTION_LEVELS = {"basis": "basis", "1 bar": "basis", "3 bar": "3_bar", "3_bar": "3_bar", "3bar": "3_bar"}


def add_missing_terms(graph: Graph, ifc_path: Path | None = None) -> int:
    """Add the ``missing:`` terms to ``graph`` in place; returns the number of triples added."""
    before = len(graph)
    for entity, key, value in list(_metadata(graph)):
        pset, _, prop = key.partition(".")
        if pset == SHELTER_PSET:
            _shelter(graph, entity, prop, value)
        elif pset == SHOCK_PSET:
            _shock(graph, entity, prop, value)
    if ifc_path is not None and Path(ifc_path).is_file():
        _documents(graph, Path(ifc_path))
    return len(graph) - before


def _metadata(graph: Graph):
    for entity, entry in graph.subject_objects(PBS.metadata):
        key, value = graph.value(entry, PBS.metadata_key), graph.value(entry, PBS.metadata_value)
        if key is not None and value is not None:
            yield entity, str(key), str(value)


def _shelter(graph: Graph, zone: URIRef, prop: str, value: str) -> None:
    if prop == "Schutzbautyp" and value.strip():
        graph.add((zone, PBS.zone_type, MISSING.zone_type_civil_defence_shelter))
    elif prop == "Schutzgrad" and (level := PROTECTION_LEVELS.get(value.strip().lower())):
        graph.add((zone, MISSING.shock_protection_level, MISSING[f"shock_protection_level_{level}"]))


def _shock(graph: Graph, entity: URIRef, prop: str, value: str) -> None:
    if prop == "Mass":
        record = BNode()
        graph.add((entity, PBS.quantity_values, record))
        graph.add((record, RDF.type, PBS.QuantityValue))
        graph.add((record, PBS.quantity_type, MISSING.quantity_type_mass))
        graph.add((record, PBS.quantity_unit, Literal("kg")))
        graph.add((record, PBS.quantity_value, Literal(float(value))))
        return
    if prop not in SHOCK_PROPERTIES:
        return
    name, kind = SHOCK_PROPERTIES[prop]
    if kind == NUMBER:
        literal = Literal(float(value))
    elif kind == BOOLEAN:
        literal = Literal(value.strip().lower() == "true")
    else:
        literal = Literal(value)
    record = BNode()
    graph.add((entity, PBS.performance_properties, record))
    graph.add((record, RDF.type, PBS.PerformanceProperty))
    graph.add((record, RDF.type, PBS.StructuralProperty))
    graph.add((record, PBS.property_key, MISSING[f"structural_property_{name}"]))
    graph.add((record, PBS[f"property_value_{kind}"], literal))
    graph.add((record, PBS.source_pset, Literal(SHOCK_PSET)))
    graph.add((record, PBS.source_property, Literal(prop)))
    graph.add((record, PBS.source_value_raw, Literal(value)))


def _documents(graph: Graph, ifc_path: Path) -> None:
    import ifcopenshell

    entities = {str(g): s for s, g in graph.subject_objects(PBS.ifc_global_id) if isinstance(s, URIRef)}
    model = ifcopenshell.open(str(ifc_path))
    for rel in model.by_type("IfcRelAssociatesDocument"):
        document = rel.RelatingDocument
        info = getattr(document, "ReferencedDocument", None) if document.is_a("IfcDocumentReference") else document
        code = document.Identification or (info.Identification if info else None)
        if not code:
            continue
        artifact = URIRef(f"urn:pbs:demo:document:{code}")
        if (artifact, RDF.type, PBS.Artifact) not in graph:
            classification = BNode()
            graph.add((artifact, RDF.type, PBS.Artifact))
            graph.add((artifact, RDF.type, PBS.Entity))
            graph.add((artifact, PBS.name, Literal(document.Name or (info.Name if info else None) or code)))
            graph.add((artifact, PBS.classifications, classification))
            graph.add((classification, RDF.type, PBS.Classification))
            graph.add((classification, PBS.classification_code, Literal(code)))
            graph.add((classification, PBS.classification_scheme, Literal("KBOB")))
        for product in rel.RelatedObjects:
            entity = entities.get(getattr(product, "GlobalId", None))
            if entity is not None:
                graph.add((entity, MISSING.documented_by, artifact))
