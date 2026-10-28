"""SKOS vocabulary and mapping-bridge lookups referenced by the IFC mapping."""

from __future__ import annotations

from pathlib import Path

from rdflib import DCTERMS, RDF, SKOS, Graph, Literal, URIRef

_MATCH_PREDICATES = (
    SKOS.exactMatch,
    SKOS.closeMatch,
    SKOS.broadMatch,
    SKOS.narrowMatch,
    SKOS.relatedMatch,
)
_NON_TARGET_PREDICATES = {
    RDF.type,
    SKOS.prefLabel,
    SKOS.altLabel,
    SKOS.notation,
    SKOS.definition,
    SKOS.inScheme,
    DCTERMS.title,
    DCTERMS.description,
}


def _norm(text: str) -> str:
    return " ".join(str(text).split()).casefold()


class Vocabularies:
    def __init__(self, classification_dir: Path) -> None:
        self.root = Path(classification_dir)
        self._graphs: dict[Path, Graph] = {}
        self._label_index: dict[tuple[Path, str], dict[str, list[str]]] = {}
        self._scheme_files: dict[str, Path | None] = {}

    def _graph(self, path: Path) -> Graph:
        if path not in self._graphs:
            self._graphs[path] = Graph().parse(path, format="turtle")
        return self._graphs[path]

    def _find(self, filename: str) -> Path:
        matches = sorted(self.root.rglob(filename))
        if not matches:
            raise FileNotFoundError(f"{filename} not found under {self.root}")
        return matches[0]

    def _labels(self, path: Path, prop: str) -> dict[str, list[str]]:
        key = (path, prop)
        if key not in self._label_index:
            predicate = SKOS[prop]
            index: dict[str, list[str]] = {}
            for subject, label in self._graph(path).subject_objects(predicate):
                if isinstance(subject, URIRef) and isinstance(label, Literal):
                    index.setdefault(_norm(label), []).append(str(subject))
            self._label_index[key] = {k: sorted(set(v)) for k, v in index.items()}
        return self._label_index[key]

    def label_lookup(self, vocabulary: str, value: str, prop: str = "prefLabel") -> list[str]:
        """Concept IRIs in ``{vocabulary}.skos.ttl`` whose ``prop`` label equals ``value``."""
        path = self._find(f"{vocabulary}.skos.ttl")
        return self._labels(path, prop).get(_norm(value), [])

    def bridge_lookup(self, bridge: str, value: str) -> list[str]:
        """Targets of bridge concepts whose prefLabel equals ``value``."""
        path = self._find(f"{bridge}.mapping.ttl")
        graph = self._graph(path)
        targets: set[str] = set()
        for subject in self._labels(path, "prefLabel").get(_norm(value), []):
            for predicate in _MATCH_PREDICATES:
                targets.update(str(o) for o in graph.objects(URIRef(subject), predicate))
        return sorted(targets)

    def bridge_targets(self, bridge: str, subject: str) -> list[str]:
        """IRIs a bridge maps ``subject`` to, through any non-descriptive predicate."""
        graph = self._graph(self._find(f"{bridge}.mapping.ttl"))
        return sorted(
            str(o)
            for p, o in graph.predicate_objects(URIRef(subject))
            if isinstance(o, URIRef) and p not in _NON_TARGET_PREDICATES
        )

    def _scheme_file(self, scheme_identifier: str) -> Path | None:
        if scheme_identifier not in self._scheme_files:
            needle = f'dcterms:identifier "{scheme_identifier}"'
            found = None
            for path in sorted(self.root.rglob("*.skos.ttl")):
                if needle in path.read_text(encoding="utf-8"):
                    found = path
                    break
            self._scheme_files[scheme_identifier] = found
        return self._scheme_files[scheme_identifier]

    def concept(self, scheme_identifier: str, iri: str) -> dict[str, str] | None:
        """Notation and English label of ``iri`` in the scheme with ``scheme_identifier``."""
        path = self._scheme_file(scheme_identifier)
        if path is None:
            return None
        graph = self._graph(path)
        subject = URIRef(iri)
        notation = graph.value(subject, SKOS.notation)
        if notation is None:
            return None
        labels = {lit.language: str(lit) for lit in graph.objects(subject, SKOS.prefLabel)}
        return {
            "notation": str(notation),
            "label": labels.get("en") or next(iter(sorted(labels.values())), ""),
        }
