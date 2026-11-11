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
    skipped_stages: list[str] = field(default_factory=list)
    geometry_output: str | None = None
    geometry_failures: Counter = field(default_factory=Counter)

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
            ("geometry failed", self.geometry_failures),
        ):
            out += [f"  {label}: {key} ×{n}" for key, n in sorted(counter.items())]
        out += [f"  skipped stage: {stage}" for stage in self.skipped_stages]
        return out
