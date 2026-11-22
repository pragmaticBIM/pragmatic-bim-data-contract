"""Conversion report: what was mapped, dropped, identified, and computed."""

from __future__ import annotations

from collections import Counter
from dataclasses import dataclass, field


@dataclass
class ConversionReport:
    source_system: str
    contract_version: str
    mapping_version: str
    nodes_by_class: Counter = field(default_factory=Counter)
    excluded_by_ifc_class: Counter = field(default_factory=Counter)
    dropped: Counter = field(default_factory=Counter)
    missing_required: Counter = field(default_factory=Counter)
    unsupported_sources: Counter = field(default_factory=Counter)
    rejected_values: Counter = field(default_factory=Counter)
    """PropertySet values a ``normalize_*`` rule rejected (they stay in metadata only)."""
    reference_version: str | None = None
    identified_elements: Counter = field(default_factory=Counter)
    ambiguous_elements: Counter = field(default_factory=Counter)
    unmatched_reference_entities: Counter = field(default_factory=Counter)
    computed_relations: Counter = field(default_factory=Counter)
    computed_quantities: Counter = field(default_factory=Counter)
    computed_measurements: Counter = field(default_factory=Counter)
    skipped_stages: list[str] = field(default_factory=list)
    geometry_output: str | None = None
    geometry_failures: Counter = field(default_factory=Counter)
    adjacency_comparison: Counter = field(default_factory=Counter)
    """``ifc_and_geometry`` / ``ifc_only`` / ``geometry_only`` element↔space pairs."""
    adjacency_disagreements: list[str] = field(default_factory=list)
    """Human-readable IFC vs geometry disagreements (IFC kept)."""
    spaces_without_ifc_boundaries: int = 0
    """Spaces that had no ``IfcRelSpaceBoundary`` (geometry may fill them)."""

    def lines(self) -> list[str]:
        out = [
            f"source_system={self.source_system} contract_version={self.contract_version} "
            f"mapping_version={self.mapping_version}"
        ]
        if self.reference_version:
            out.append(f"reference_version={self.reference_version}")
        if self.geometry_output:
            out.append(f"geometry_output={self.geometry_output}")
        out += [f"  {cls}: {n}" for cls, n in sorted(self.nodes_by_class.items())]
        for label, counter in (
            ("excluded", self.excluded_by_ifc_class),
            ("missing required", self.missing_required),
            ("dropped", self.dropped),
            ("unsupported mapping source", self.unsupported_sources),
            ("rejected performance value", self.rejected_values),
            ("identified", self.identified_elements),
            ("ambiguous reference match", self.ambiguous_elements),
            ("no reference match", self.unmatched_reference_entities),
            ("computed relation", self.computed_relations),
            ("computed quantity", self.computed_quantities),
            ("computed measurement", self.computed_measurements),
            ("geometry failed", self.geometry_failures),
            ("space adjacency pair", self.adjacency_comparison),
        ):
            out += [f"  {label}: {key} ×{n}" for key, n in sorted(counter.items())]
        if self.spaces_without_ifc_boundaries:
            out.append(f"  spaces without IFC space boundaries: {self.spaces_without_ifc_boundaries}")
        metrics = self.adjacency_metrics()
        if metrics is not None:
            precision, recall = metrics
            out.append(f"  space adjacency vs IFC: precision={precision:.3f} recall={recall:.3f}")
        out += [f"  space adjacency disagreement: {item}" for item in self.adjacency_disagreements]
        out += [f"  skipped stage: {stage}" for stage in self.skipped_stages]
        return out

    def adjacency_metrics(self) -> tuple[float, float] | None:
        """Precision and recall of geometry pairs against IFC pairs, or None when IFC is empty."""
        both = self.adjacency_comparison.get("ifc_and_geometry", 0)
        ifc_only = self.adjacency_comparison.get("ifc_only", 0)
        geometry_only = self.adjacency_comparison.get("geometry_only", 0)
        ifc_total = both + ifc_only
        geometry_total = both + geometry_only
        if ifc_total == 0:
            return None
        precision = both / geometry_total if geometry_total else 0.0
        recall = both / ifc_total
        return precision, recall

