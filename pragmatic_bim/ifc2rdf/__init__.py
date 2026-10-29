"""IFC → RDF export following the Pragmatic BIM data contract.

Requires the ``rdf`` extra (``pip install pragmatic-bim[rdf]``).

    from pragmatic_bim.ifc2rdf import convert, to_turtle

    graph, report = convert("model.ifc", base_uri="https://data.example.org/model/")
    Path("model.ttl").write_text(to_turtle(graph))
"""

from __future__ import annotations

from pragmatic_bim.ifc2rdf.convert import DEFAULT_BASE_URI, ConversionReport, convert, to_turtle

__all__ = ["DEFAULT_BASE_URI", "ConversionReport", "convert", "to_turtle"]
