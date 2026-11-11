"""Checks over the contract graph, reported per IFC GlobalId.

``ShaclCheck`` validates against the rule files in ``rules/`` (one result per node shape that
declares a target; ``na`` when it targets nothing in the model). Contract conformance is left to the converter and IDS.
"""

from __future__ import annotations

import re
from collections import defaultdict
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Any, Protocol

import pyshacl
from rdflib import RDF, RDFS, BNode, Graph, Namespace, URIRef

from pragmatic_bim.ifc2rdf.report import ConversionReport

from demo.app.graphview import compact, entity_ids
from demo.app.i18n import german

SH = Namespace("http://www.w3.org/ns/shacl#")
VIEW = Namespace("https://schema.pragmaticbim.ch/demo/view/")
RULES_DIR = Path(__file__).with_name("rules")
SEVERITY_RANK = {"violation": 0, "warning": 1, "info": 2}
TARGET_PREDICATES = (SH.targetClass, SH.targetNode, SH.targetSubjectsOf, SH.targetObjectsOf, SH.target)


@dataclass
class CheckResult:
    id: str
    title: str
    description: str
    severity: str
    checked: list[str] = field(default_factory=list)
    failed: list[str] = field(default_factory=list)
    items: list[dict[str, Any]] = field(default_factory=list)
    """One row per finding: ``{"guid", "message", "message_de", "path", "severity"}``."""
    title_de: str = ""
    description_de: str = ""
    definition: str = ""
    """The rule as written: the SHACL shape in Turtle."""
    definition_language: str = ""
    view: dict[str, Any] = field(default_factory=dict)
    """Relations to draw when the rule is selected: ``{"relations", "chain", "path"}``."""

    @property
    def status(self) -> str:
        """``na`` (not applicable) when the rule targets no element of the model."""
        if self.failed:
            return "fail"
        return "pass" if self.checked else "na"

    def to_dict(self) -> dict[str, Any]:
        return {**asdict(self), "status": self.status}


@dataclass
class CheckContext:
    graph: Graph
    report: ConversionReport
    owner: dict[Any, str]
    """GlobalId of each entity and of every record (blank node) inlined under it."""


class Check(Protocol):
    def run(self, ctx: CheckContext) -> list[CheckResult]: ...


class ShaclCheck:
    """One result per node shape that declares a target, for one rule file from ``rules/``.

    Validated with SHACL Advanced Features so shapes can use SPARQL targets and constraints.
    """

    def __init__(self, shapes_path: Path) -> None:
        self.shapes_path = shapes_path

    @classmethod
    def rules(cls, directory: Path = RULES_DIR) -> list["ShaclCheck"]:
        return [cls(path) for path in sorted(directory.glob("*.shacl.ttl"))]

    def run(self, ctx: CheckContext) -> list[CheckResult]:
        shapes = Graph().parse(self.shapes_path)
        _, results, _ = pyshacl.validate(
            ctx.graph,
            shacl_graph=shapes,
            inference="none",
            abort_on_first=False,
            allow_warnings=True,
            advanced=True,
        )
        german_messages = [
            _template_pattern(m) for m in shapes.objects(None, SH.message) if getattr(m, "language", None) == "de"
        ]
        node_shape_of: dict[Any, URIRef] = {}
        for node_shape in shapes.subjects(RDF.type, SH.NodeShape):
            node_shape_of[node_shape] = node_shape
            for property_shape in shapes.objects(node_shape, SH.property):
                node_shape_of[property_shape] = node_shape
        targets_of = {
            node_shape: focus_nodes(shapes, node_shape, ctx.graph)
            for node_shape in set(shapes.subjects(RDF.type, SH.NodeShape))
            if any((node_shape, p, None) in shapes for p in TARGET_PREDICATES)
        }

        findings: dict[Any, dict[tuple, dict[str, Any]]] = defaultdict(dict)
        for result in results.subjects(RDF.type, SH.ValidationResult):
            shape = node_shape_of.get(results.value(result, SH.sourceShape))
            focus = results.value(result, SH.focusNode)
            path = results.value(result, SH.resultPath)
            component = str(results.value(result, SH.sourceConstraintComponent)).removeprefix(str(SH))
            messages = _result_messages(results, result, german_messages)
            key = (focus, path, component, results.value(result, SH.value), messages.get("en"))
            findings[shape][key] = {
                "guid": ctx.owner.get(focus),
                "path": compact(path) if path is not None else None,
                "message": _message(ctx.graph, focus, path, component, messages.get("en"), "en"),
                "message_de": _message(ctx.graph, focus, path, component, messages.get("de"), "de"),
                "severity": _severity(results.value(result, SH.resultSeverity)),
            }

        out = []
        for node_shape in sorted(targets_of, key=str):
            targets = targets_of[node_shape]
            items = list(findings.pop(node_shape, {}).values())
            id, title, description, title_de, description_de = self._describe(shapes, node_shape)
            result = _result(
                id=id,
                title=title,
                description=description,
                title_de=title_de,
                description_de=description_de,
                severity=_severity(shapes.value(node_shape, SH.severity)),
                checked={ctx.owner[t] for t in targets if t in ctx.owner},
                items=items,
            )
            result.definition = shape_turtle(shapes, node_shape)
            result.definition_language = "turtle"
            result.view = _view(shapes, node_shape)
            out.append(result)
        leftover = [item for items in findings.values() for item in items.values()]
        if leftover:
            out.append(_result(
                id=f"rule-{self.shapes_path.name}-other",
                title=f"Other findings ({self.shapes_path.name})",
                description="",
                title_de=f"Weitere Befunde ({self.shapes_path.name})",
                description_de="",
                severity="violation",
                checked=set(),
                items=leftover,
            ))
        return out

    def _describe(self, shapes: Graph, node_shape: Any) -> tuple[str, str, str, str, str]:
        """Id, English title and description, German title and description."""
        local = str(node_shape).rstrip("/").rsplit("/", 1)[-1].rsplit("#", 1)[-1]
        title = _text(shapes, node_shape, SH.name) or _text(shapes, node_shape, RDFS.label) or local
        description = _text(shapes, node_shape, SH.description) or _text(shapes, node_shape, RDFS.comment)
        description_de = _text(shapes, node_shape, SH.description, "de")
        file = self.shapes_path.name
        return (
            f"rule-{local}",
            title,
            f"{description} (rule file {file})".strip(),
            _text(shapes, node_shape, SH.name, "de") or title,
            f"{description_de} (Regeldatei {file})".strip() if description_de else "",
        )


def _view(shapes: Graph, node_shape: Any) -> dict[str, Any]:
    """Demo annotations on a shape: ``view:relation`` (repeatable), ``view:chain``, ``view:path``, ``view:quantity``.

    ``chain`` follows the relations onward from each checked element (a route); ``path`` names the
    ``geometry_representation`` drawn in 3D instead of straight lines between the elements;
    ``quantity`` labels each line with that quantity of the element it starts from.
    """
    relations = sorted(compact(r) for r in shapes.objects(node_shape, VIEW.relation))
    if not relations:
        return {}
    chain = shapes.value(node_shape, VIEW.chain)
    path = shapes.value(node_shape, VIEW.path)
    quantity = shapes.value(node_shape, VIEW.quantity)
    return {
        "relations": relations,
        "chain": bool(chain.toPython()) if chain is not None else False,
        "path": str(path) if path is not None else None,
        "quantity": compact(quantity) if quantity is not None else None,
    }


def default_checks() -> list[Check]:
    return list(ShaclCheck.rules())


def run_checks(graph: Graph, report: ConversionReport, checks: list[Check] | None = None) -> list[CheckResult]:
    ctx = CheckContext(graph=graph, report=report, owner=record_owners(graph))
    results = [r for check in (checks if checks is not None else default_checks()) for r in check.run(ctx)]
    return sorted(results, key=lambda r: (
        {"fail": 0, "pass": 1, "na": 2}[r.status],
        SEVERITY_RANK.get(r.severity, 9),
        r.title,
    ))


def focus_nodes(shapes: Graph, node_shape: Any, data: Graph) -> set[Any]:
    """Focus nodes of ``node_shape`` in ``data`` (core targets and SPARQL-based targets)."""
    nodes: set[Any] = set()
    for cls in shapes.objects(node_shape, SH.targetClass):
        nodes.update(data.subjects(RDF.type, cls))
    nodes.update(shapes.objects(node_shape, SH.targetNode))
    for predicate in shapes.objects(node_shape, SH.targetSubjectsOf):
        nodes.update(data.subjects(predicate, None))
    for predicate in shapes.objects(node_shape, SH.targetObjectsOf):
        nodes.update(data.objects(None, predicate))
    for target in shapes.objects(node_shape, SH.target):
        select = shapes.value(target, SH.select)
        if select is not None:
            nodes.update(row[0] for row in data.query(_declared_prefixes(shapes, target) + str(select)))
    return nodes


def shape_turtle(shapes: Graph, node_shape: Any) -> str:
    """``node_shape`` with its nested blank nodes (property shapes, targets, constraints) as Turtle."""
    description = shapes.cbd(node_shape)
    for prefix, namespace in shapes.namespaces():
        description.bind(prefix, namespace, override=True)
    text = description.serialize(format="turtle")
    return "\n".join(line for line in text.splitlines() if not line.startswith("@prefix")).strip()


def _declared_prefixes(shapes: Graph, node: Any) -> str:
    lines = []
    for declarations in shapes.objects(node, SH.prefixes):
        for declare in shapes.objects(declarations, SH.declare):
            lines.append(f"PREFIX {shapes.value(declare, SH.prefix)}: <{shapes.value(declare, SH.namespace)}>")
    return "\n".join(lines) + "\n"


def record_owners(graph: Graph) -> dict[Any, str]:
    owner: dict[Any, str] = dict(entity_ids(graph))
    pending = [o for o in owner]
    while pending:
        parent = pending.pop()
        for obj in graph.objects(parent):
            if isinstance(obj, BNode) and obj not in owner:
                owner[obj] = owner[parent]
                pending.append(obj)
    return owner


_COMPONENT_MESSAGES = {
    "en": {
        "MinCountConstraintComponent": "Missing {path}",
        "MaxCountConstraintComponent": "Too many values for {path}",
        "InConstraintComponent": "{path}: value not in the allowed list",
        "DatatypeConstraintComponent": "{path}: wrong datatype",
        "ClassConstraintComponent": "{path}: target has the wrong class",
        "NodeKindConstraintComponent": "{path}: wrong node kind",
        "ClosedConstraintComponent": "Property {path} is not part of the contract",
        "PatternConstraintComponent": "{path}: value does not match the pattern",
    },
    "de": {
        "MinCountConstraintComponent": "{path} fehlt",
        "MaxCountConstraintComponent": "Zu viele Werte für {path}",
        "InConstraintComponent": "{path}: Wert nicht in der erlaubten Liste",
        "DatatypeConstraintComponent": "{path}: falscher Datentyp",
        "ClassConstraintComponent": "{path}: verknüpftes Objekt hat die falsche Klasse",
        "NodeKindConstraintComponent": "{path}: falsche Knotenart",
        "ClosedConstraintComponent": "Eigenschaft {path} ist nicht Teil des Datenvertrags",
        "PatternConstraintComponent": "{path}: Wert entspricht nicht dem Muster",
    },
}


def _text(graph: Graph, subject: Any, predicate: Any, lang: str | None = None) -> str:
    """Literal in ``lang``; ``None`` picks an English or untagged literal."""
    accepted = {lang} if lang else {None, "en"}
    return next((str(v) for v in graph.objects(subject, predicate) if getattr(v, "language", None) in accepted), "")


def _template_pattern(template: Any) -> re.Pattern[str]:
    return re.compile(re.sub(r"\\\{\\[?$]\w+\\\}", ".*", re.escape(str(template))), re.DOTALL)


def _result_messages(results: Graph, result: Any, german: list[re.Pattern[str]]) -> dict[str, str]:
    """Result messages by language. pyshacl drops the language tag of SPARQL constraint
    messages after substituting variables, so German ones are recognized by their template."""
    out: dict[str, str] = {}
    for message in results.objects(result, SH.resultMessage):
        lang = getattr(message, "language", None)
        if lang is None and any(p.fullmatch(str(message)) for p in german):
            lang = "de"
        out["de" if lang == "de" else "en"] = str(message)
    return out


def _message(graph: Graph, focus: Any, path: Any, component: str, raw: str | None, lang: str) -> str:
    template = _COMPONENT_MESSAGES[lang].get(component)
    if template and path is not None:
        label = compact(path) if lang == "en" else german().slots.get(compact(path), compact(path))
        text = template.format(path=label)
    elif raw is None and lang == "de":
        return ""
    else:
        text = str(raw or component)[:200]
    if isinstance(focus, BNode):
        record = sorted(compact(t).removeprefix("pbs:") for t in graph.objects(focus, RDF.type))
        if record:
            text = f"{record[-1]} record: {text}" if lang == "en" else f"{german().classes.get(record[-1], record[-1])}: {text}"
    return text


def _severity(term: Any) -> str:
    return str(term).removeprefix(str(SH)).lower() if term is not None else "violation"


def _result(
    *,
    id: str,
    title: str,
    description: str,
    severity: str,
    checked: set[str],
    items: list[dict[str, Any]],
    title_de: str = "",
    description_de: str = "",
) -> CheckResult:
    items = sorted(items, key=lambda i: (str(i["guid"]), str(i["path"]), i["message"]))
    failed = {i["guid"] for i in items if i["guid"]}
    severities = [i["severity"] for i in items] or [severity]
    return CheckResult(
        id=id,
        title=title,
        description=description,
        title_de=title_de,
        description_de=description_de,
        severity=min(severities, key=lambda s: SEVERITY_RANK.get(s, 9)),
        checked=sorted(checked | failed),
        failed=sorted(failed),
        items=items,
    )
