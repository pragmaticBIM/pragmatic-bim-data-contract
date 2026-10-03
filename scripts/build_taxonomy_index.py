#!/usr/bin/env python3
"""Build pragmatic_bim/taxonomies.json from the SKOS classification turtle files.

The index lets consumers resolve and validate Classification.classification_code
values without parsing turtle or depending on rdflib at runtime.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from rdflib import Graph
from rdflib.namespace import DCTERMS, RDF, SKOS

REPO_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_CLASSIFICATION_DIR = REPO_ROOT / "classification"
DEFAULT_OUT = REPO_ROOT / "pragmatic_bim" / "taxonomies.json"


def localized(graph: Graph, subject, predicate) -> dict[str, str]:
    return {
        (literal.language or "en"): str(literal)
        for literal in graph.objects(subject, predicate)
    }


def read_scheme(path: Path) -> tuple[str, dict] | None:
    graph = Graph()
    graph.parse(path, format="turtle")

    scheme = next(graph.subjects(RDF.type, SKOS.ConceptScheme), None)
    if scheme is None:
        return None

    identifier = next(graph.objects(scheme, DCTERMS.identifier), None)
    if identifier is None:
        return None

    concepts: dict[str, dict] = {}
    for concept in graph.subjects(RDF.type, SKOS.Concept):
        notation = next(graph.objects(concept, SKOS.notation), None)
        if notation is None:
            continue
        broader = next(graph.objects(concept, SKOS.broader), None)
        broader_code = next(graph.objects(broader, SKOS.notation), None) if broader else None
        concepts[str(notation)] = {
            "labels": localized(graph, concept, SKOS.prefLabel),
            "definition": localized(graph, concept, SKOS.definition),
            "broader": str(broader_code) if broader_code else None,
        }

    return str(identifier), {
        "labels": localized(graph, scheme, SKOS.prefLabel),
        "description": localized(graph, scheme, DCTERMS.description),
        "source": path.relative_to(REPO_ROOT).as_posix(),
        "concepts": dict(sorted(concepts.items())),
    }


def build(classification_dir: Path, out_path: Path) -> dict:
    index: dict[str, dict] = {}
    for path in sorted(classification_dir.rglob("*.skos.ttl")):
        result = read_scheme(path)
        if result is None:
            print(f"  skipped (no dcterms:identifier): {path.name}")
            continue
        identifier, payload = result
        if identifier in index:
            index[identifier]["concepts"].update(payload["concepts"])
        else:
            index[identifier] = payload
        print(f"  {identifier:48s} {len(payload['concepts']):5d} concepts  {path.name}")

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(index, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return index


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--classification-dir", type=Path, default=DEFAULT_CLASSIFICATION_DIR)
    parser.add_argument("--out", type=Path, default=DEFAULT_OUT)
    args = parser.parse_args()

    index = build(args.classification_dir, args.out)
    total = sum(len(scheme["concepts"]) for scheme in index.values())
    print(f"\n{len(index)} schemes, {total} concepts -> {args.out.relative_to(REPO_ROOT)}")


if __name__ == "__main__":
    main()
