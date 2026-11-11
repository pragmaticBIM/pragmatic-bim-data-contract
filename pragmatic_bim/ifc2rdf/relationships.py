"""Turn IFC relationship instances into contract relation slots."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from pragmatic_bim.ifc2rdf.pipeline import Converter


def relate_ifc_relationships(conv: "Converter") -> None:
    for rel in sorted(conv.file.by_type("IfcRelationship"), key=lambda r: r.GlobalId):
        key = conv.mapping.relationship_key(rel)
        if key is None or key == "IfcRelAssociatesClassification":
            continue
        if key == "IfcRelAssignsToGroup":
            group = rel.RelatingGroup
            if group is not None and group.is_a("IfcSystem") and not group.is_a("IfcZone"):
                key = "IfcRelAssignsToSystem"
        for subject, obj, relation_type, owner in _relation_pairs(conv, key, rel):
            _relate(conv, key, subject, obj, relation_type, owner)
    _relate_hosts(conv)


def _relate_hosts(conv: "Converter") -> None:
    """``hosted_by``: filling element → host element, through its opening.

    Chains ``IfcRelFillsElement`` (door → opening) and ``IfcRelVoidsElement``
    (opening → wall) when the mapping lists ``IfcRelVoidsElement`` with
    ``chain_relation_type``.
    """
    spec = conv.mapping.relationships.get("IfcRelVoidsElement") or {}
    relation_type = spec.get("chain_relation_type")
    if not relation_type:
        return
    for node in sorted(conv.nodes.values(), key=lambda n: n.global_id):
        if "IfcRelVoidsElement" not in (node.mapping.block.get("relations") or []):
            continue
        for fills in getattr(node.entity, "FillsVoids", None) or []:
            opening = fills.RelatingOpeningElement
            for voids in getattr(opening, "VoidsElements", None) or []:
                host = conv.nodes.get(voids.RelatingBuildingElement.id())
                if host is not None and conv.writer.set(node, relation_type, host):
                    conv.report.computed_relations[f"{relation_type} (ifc)"] += 1


def _resolve_type(spec: dict[str, Any], entity, condition: str) -> str | None:
    for resolution in spec.get("resolutions") or []:
        classes = resolution.get(condition)
        if classes is None:
            continue
        classes = [classes] if isinstance(classes, str) else classes
        if entity is not None and any(entity.is_a(c) for c in classes):
            return resolution["relation_type"]
    return spec.get("relation_type") if not spec.get("resolutions") else None


def _relation_pairs(conv: "Converter", key: str, rel):
    """Yield ``(a, b, relation_type, owner)``; ``owner`` picks the subject.

    ``owner`` is ``"a"`` when ``a`` is always the subject, or ``"slot"`` when the
    subject is whichever endpoint's contract class declares the slot.
    """
    spec = conv.mapping.relationships[key]
    if key == "IfcRelContainedInSpatialStructure":
        parent = rel.RelatingStructure
        relation_type = _resolve_type(spec, parent, "when_relating_class")
        for child in rel.RelatedElements or []:
            yield child, parent, relation_type, "a"
    elif key == "IfcRelAggregates":
        parent = rel.RelatingObject
        relation_type = _resolve_type(spec, parent, "when_related_class")
        for child in rel.RelatedObjects or []:
            yield child, parent, relation_type, "a"
    elif key == "IfcRelAssignsToGroup":
        group = rel.RelatingGroup
        classes = spec.get("group_classes") or []
        if group is not None and group.is_a() in classes:
            for member in rel.RelatedObjects or []:
                yield group, member, spec["relation_type"], "a"
    elif key == "IfcRelAssignsToSystem":
        system = rel.RelatingGroup
        for member in rel.RelatedObjects or []:
            kind = "system" if member.is_a("IfcSystem") else "element"
            for resolution in spec.get("resolutions") or []:
                if resolution.get("when_related_is") != kind:
                    continue
                if kind == "element":
                    yield member, system, resolution["relation_type"], "a"
                else:
                    yield system, member, resolution["relation_type"], "a"
    elif key == "IfcRelSpaceBoundary":
        space, element = rel.RelatingSpace, rel.RelatedBuildingElement
        if space is None or element is None:
            return
        relation_type = _resolve_type(spec, element, "when_element_class")
        if relation_type:
            yield element, space, relation_type, "slot"
        if spec.get("space_relation_type"):
            yield space, element, spec["space_relation_type"], "a"
    elif key == "IfcRelServicesBuildings":
        system = rel.RelatingSystem
        for related in rel.RelatedBuildings or []:
            relation_type = _resolve_type(spec, related, "when_related_class")
            yield system, related, relation_type, "a"
    else:
        endpoints = {
            "IfcRelConnectsElements": ("RelatingElement", "RelatedElement"),
            "IfcRelConnectsPathElements": ("RelatingElement", "RelatedElement"),
            "IfcRelFillsElement": ("RelatingOpeningElement", "RelatedBuildingElement"),
            "IfcRelCoversBldgElements": ("RelatingBuildingElement", "RelatedCoverings"),
            "IfcRelVoidsElement": ("RelatingBuildingElement", "RelatedOpeningElement"),
        }.get(key)
        if endpoints is None:
            conv.report.unsupported_sources[f"relationship {key}"] += 1
            return
        first = getattr(rel, endpoints[0], None)
        seconds = getattr(rel, endpoints[1], None)
        for second in seconds if isinstance(seconds, (list, tuple)) else [seconds]:
            if first is not None and second is not None:
                yield first, second, spec.get("relation_type"), "slot"


def _relate(conv: "Converter", key: str, a, b, relation_type: str | None, owner: str) -> None:
    if not relation_type:
        return
    node_a, node_b = conv.nodes.get(a.id()), conv.nodes.get(b.id())
    if node_a is None or node_b is None:
        return
    subject, obj = node_a, node_b
    if owner == "slot" and relation_type not in conv.schema.class_slots(node_a.contract_class):
        if relation_type in conv.schema.class_slots(node_b.contract_class):
            subject, obj = node_b, node_a
    if key not in (subject.mapping.block.get("relations") or []):
        conv.report.dropped[f"{subject.contract_class}.{relation_type} ({key} not listed)"] += 1
        return
    conv.writer.set(subject, relation_type, obj)
    if (
        conv.mapping.relationships[key].get("symmetric")
        and relation_type in conv.schema.class_slots(obj.contract_class)
        and key in (obj.mapping.block.get("relations") or [])
    ):
        conv.writer.set(obj, relation_type, subject)
