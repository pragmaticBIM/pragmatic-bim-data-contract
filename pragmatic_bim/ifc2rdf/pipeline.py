"""Convert an IFC model into an RDF graph that follows the Pragmatic BIM data contract.

The converter interprets ``ifc_mapping.merged.yaml`` (entity blocks, field sources,
relationship resolutions) and the LinkML contract (class hierarchy, slots, enums). It
holds no IFC → contract rules of its own beyond how each mapping source type is read.

Stages: identify (pragmaticBIM Reference) → build nodes → populate → IFC relationships →
geometry and computed relations → derivations → emit.
"""

from __future__ import annotations

import hashlib
from pathlib import Path
from typing import Any

import ifcopenshell
import ifcopenshell.util.unit
from rdflib import Graph, URIRef

from pragmatic_bim.ifc2rdf.contract import ContractSchema
from pragmatic_bim.ifc2rdf.emit import build_graph
from pragmatic_bim.ifc2rdf.evaluator import Evaluator
from pragmatic_bim.ifc2rdf.mapping import Mapping
from pragmatic_bim.ifc2rdf.model import Node
from pragmatic_bim.ifc2rdf.populate import derive, populate
from pragmatic_bim.ifc2rdf.reference import (
    ElementMatch,
    ReferenceCatalog,
    best_matches,
    classification_entry,
    identify,
    resolve_reference_path,
)
from pragmatic_bim.ifc2rdf.relationships import relate_ifc_relationships
from pragmatic_bim.ifc2rdf.report import ConversionReport
from pragmatic_bim.ifc2rdf.resources import (
    classification_dir,
    default_mapping_path,
    default_schema_path,
)
from pragmatic_bim.ifc2rdf.vocab import Vocabularies
from pragmatic_bim.ifc2rdf.writer import SlotWriter

DEFAULT_BASE_URI = "urn:pbs:ifc:{project}/"


class Converter:
    def __init__(
        self,
        ifc_file: ifcopenshell.file,
        *,
        mapping: Mapping,
        schema: ContractSchema,
        vocab: Vocabularies,
        base_uri: str = DEFAULT_BASE_URI,
        contract_version: str | None = None,
        source_system: str | None = None,
        source_digest: str | None = None,
        catalog: ReferenceCatalog | None = None,
        geometry: bool = True,
        geometry_out: Path | str | None = None,
        source_name: str = "model.ifc",
    ) -> None:
        self.file = ifc_file
        self.catalog = catalog
        self.geometry_enabled = geometry
        self.geometry_out = Path(geometry_out) if geometry_out else None
        self.source_name = source_name
        self.reference_matches: dict[int, list[ElementMatch]] = {}
        self.mapping = mapping
        self.schema = schema
        self.vocab = vocab
        self.contract_version = contract_version or mapping.canonical_type_version
        self.source_system = source_system or detect_source_system(ifc_file, mapping.conventions)
        self.source_digest = source_digest
        projects = sorted(ifc_file.by_type("IfcProject"), key=lambda p: p.GlobalId)
        project_id = projects[0].GlobalId if projects else "model"
        self.base_uri = base_uri.replace("{project}", project_id)
        self.length_scale = ifcopenshell.util.unit.calculate_unit_scale(ifc_file)
        self.report = ConversionReport(self.source_system, self.contract_version, mapping.version)
        self.writer = SlotWriter(schema, self.report)
        self.nodes: dict[int, Node] = {}
        self._by_iri: dict[URIRef, Node] = {}
        self._disciplines: dict[int, Any] = {}

    # --- helpers --------------------------------------------------------------

    def iri(self, global_id: str) -> URIRef:
        return URIRef(self.base_uri + global_id)

    @property
    def by_iri(self) -> dict[URIRef, Node]:
        if len(self._by_iri) != len(self.nodes):
            self._by_iri = {n.iri: n for n in self.nodes.values()}
        return self._by_iri

    def systems_of(self, entity: ifcopenshell.entity_instance) -> list:
        systems = []
        for rel in getattr(entity, "HasAssignments", None) or []:
            group = getattr(rel, "RelatingGroup", None)
            if group is not None and group.is_a("IfcSystem") and not group.is_a("IfcZone"):
                systems.append(group)
        return systems

    def system_discipline(self, system: ifcopenshell.entity_instance) -> Any:
        if system.id() not in self._disciplines:
            em = self.mapping.resolve(system)
            spec = (em.block.get("attributes") or {}).get("system_discipline") if em else None
            value = Evaluator(self, system, em).evaluate(spec, "system_discipline") if spec else None
            self._disciplines[system.id()] = value
        return self._disciplines[system.id()]

    def sorted_nodes(self) -> list[Node]:
        return sorted(self.nodes.values(), key=lambda n: n.global_id)

    # --- stages ---------------------------------------------------------------

    def identify(self) -> None:
        if self.catalog is None:
            self.report.skipped_stages.append("reference identification (disabled or no pragmaticBIM-reference checkout)")
            return
        self.report.reference_version = self.catalog.version
        self.reference_matches = identify(self.file, self.catalog)

    def build_nodes(self) -> None:
        candidates = sorted(self.file.by_type("IfcRoot"), key=lambda e: e.GlobalId)
        for entity in candidates:
            key = self.mapping.entity_key(entity)
            if key is None:
                continue
            matches = self.reference_matches.get(entity.id(), [])
            em = self.mapping.resolve(entity, [m.element.id for m in matches])
            if em is None:
                if key not in self.mapping.excluded and self.mapping.needs_reference_match(key):
                    self.report.unmatched_reference_entities[entity.is_a()] += 1
                else:
                    self.report.excluded_by_ifc_class[entity.is_a()] += 1
                continue
            self.nodes[entity.id()] = Node(
                entity=entity,
                mapping=em,
                iri=self.iri(entity.GlobalId),
                types=self.schema.rdf_types(em.contract_class),
                reference_elements=tuple(m.element.id for m in matches),
            )

    def classify(self, node: Node) -> None:
        """Add the best pragmaticBIM Reference match(es) as classifications."""
        best = best_matches(self.reference_matches.get(node.entity.id(), []))
        if not best:
            return
        version = self.catalog.version if self.catalog else None
        self.writer.classifications(node, [classification_entry(m, version) for m in best])
        for match in best:
            self.report.identified_elements[match.element.id] += 1
        if len(best) > 1:
            self.report.ambiguous_elements[" | ".join(m.element.id for m in best)] += 1

    def compute_geometry(self) -> None:
        if not self.geometry_enabled:
            self.report.skipped_stages.append("geometry (disabled)")
            return
        try:
            from pragmatic_bim.ifc2rdf.geometry import run_geometry_pass
            from pragmatic_bim.ifc2rdf.spatial import compute
        except ImportError as exc:
            self.report.skipped_stages.append(f"geometry (install pragmatic-bim[geometry]: {exc.name})")
            return
        products = [n.entity for n in self.sorted_nodes() if n.entity.is_a("IfcProduct")]
        result = run_geometry_pass(self.file, products, glb_path=self.geometry_out)
        self.report.geometry_failures.update(result.failures)
        if result.glb_path is not None:
            self.report.geometry_output = str(result.glb_path)
        compute(self, result, self.source_name)

    def run(self) -> Graph:
        self.identify()
        self.build_nodes()
        nodes = self.sorted_nodes()
        for node in nodes:
            populate(self, node)
            self.classify(node)
        relate_ifc_relationships(self)
        self.compute_geometry()
        for node in nodes:
            derive(self, node)
        return build_graph(self, nodes)


def detect_source_system(ifc_file: ifcopenshell.file, conventions: dict[str, Any]) -> str:
    config = conventions.get("source_system") or {}
    texts: list[str] = []
    for app in ifc_file.by_type("IfcApplication"):
        texts += [app.ApplicationFullName or "", app.ApplicationIdentifier or ""]
    header = ifc_file.header.file_name
    texts += [header.originating_system or "", header.preprocessor_version or ""]
    blob = " ".join(texts).casefold()
    for system, keywords in (config.get("detect") or {}).items():
        if any(str(keyword).casefold() in blob for keyword in keywords):
            return system
    return config.get("default", "ifc")


def convert(
    ifc_path: Path | str,
    *,
    base_uri: str = DEFAULT_BASE_URI,
    contract_version: str | None = None,
    source_system: str | None = None,
    mapping_path: Path | str | None = None,
    schema_path: Path | str | None = None,
    reference: Path | str | bool | None = None,
    geometry: bool = True,
    geometry_out: Path | str | None = None,
) -> tuple[Graph, ConversionReport]:
    """Convert ``ifc_path`` into a contract RDF graph and a conversion report.

    ``reference`` is a pragmaticBIM Reference checkout; None looks it up
    (``$PBS_REFERENCE_PATH``, then the sibling checkout) and False disables identification.
    ``geometry_out`` writes the GLB mesh (node names are GlobalIds); ``geometry=False``
    skips geometry and the computed relations.
    """
    ifc_path = Path(ifc_path)
    digest = hashlib.sha256(ifc_path.read_bytes()).hexdigest()
    reference_path = None if reference is False else resolve_reference_path(
        None if reference is True else reference
    )
    converter = Converter(
        ifcopenshell.open(str(ifc_path)),
        mapping=Mapping.load(Path(mapping_path) if mapping_path else default_mapping_path()),
        schema=ContractSchema(Path(schema_path) if schema_path else default_schema_path()),
        vocab=Vocabularies(classification_dir()),
        base_uri=base_uri,
        contract_version=contract_version,
        source_system=source_system,
        source_digest=digest,
        catalog=ReferenceCatalog.load(reference_path) if reference_path else None,
        geometry=geometry,
        geometry_out=geometry_out,
        source_name=ifc_path.name,
    )
    graph = converter.run()
    return graph, converter.report
