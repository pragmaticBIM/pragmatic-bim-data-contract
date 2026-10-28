"""Graph assertions shared by the synthetic and sample tests."""

from __future__ import annotations

import pyshacl
import rdflib
from rdflib import RDF, Namespace

PBS = Namespace("https://schema.pragmaticbim.ch/")
BOT = Namespace("https://w3id.org/bot#")
SH = Namespace("http://www.w3.org/ns/shacl#")

PREFIXES = """PREFIX pbs: <https://schema.pragmaticbim.ch/>
PREFIX bot: <https://w3id.org/bot#>
"""

BOT_WALLS = PREFIXES + """
SELECT DISTINCT ?wall WHERE {
  ?space a bot:Space ; bot:adjacentElement ?wall .
  ?wall a bot:Element , pbs:SeparatorWall .
}"""

CONTRACT_WALLS = PREFIXES + """
SELECT DISTINCT ?wall WHERE {
  ?wall a pbs:SeparatorWall ; pbs:separates_spaces ?space .
  ?space a pbs:Space .
}"""

BOT_ADJACENCY = PREFIXES + "SELECT ?space ?element WHERE { ?space bot:adjacentElement ?element }"

CONTRACT_ADJACENCY = PREFIXES + """
SELECT ?space ?element WHERE {
  { ?element pbs:separates_spaces ?space }
  UNION { ?element pbs:connects_spaces ?space . ?element a pbs:ConnectionPhysical }
  UNION { ?space pbs:bounded_by ?element }
  ?space a pbs:Space .
}"""


def shacl_violations(graph: rdflib.Graph, shacl: rdflib.Graph) -> list[str]:
    conforms, report, _ = pyshacl.validate(
        graph, shacl_graph=shacl, inference="none", abort_on_first=False, allow_warnings=True
    )
    if conforms:
        return []
    messages = []
    for result in report.subjects(RDF.type, SH.ValidationResult):
        messages.append(
            f"{report.value(result, SH.focusNode)} {report.value(result, SH.resultPath)}: "
            f"{report.value(result, SH.resultMessage)}"
        )
    return sorted(messages)


def nodes_of(graph: rdflib.Graph, contract_class: str) -> set[rdflib.term.Node]:
    return set(graph.subjects(RDF.type, PBS[contract_class]))


def global_ids_of(graph: rdflib.Graph, contract_class: str) -> set[str]:
    return {str(graph.value(node, PBS.ifc_global_id)) for node in nodes_of(graph, contract_class)}


def rows(graph: rdflib.Graph, query: str) -> set[tuple]:
    return {tuple(row) for row in graph.query(query)}
