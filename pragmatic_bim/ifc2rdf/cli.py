"""``ifc2rdf model.ifc -o model.ttl [--contract-version vX.Y.Z]``"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from pragmatic_bim.ifc2rdf.convert import DEFAULT_BASE_URI, convert, to_turtle


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="ifc2rdf",
        description="Convert an IFC model into Turtle that follows the Pragmatic BIM data contract.",
    )
    parser.add_argument("ifc", type=Path, help="Input IFC file")
    parser.add_argument("-o", "--output", type=Path, help="Output Turtle file (default: stdout)")
    parser.add_argument(
        "--contract-version",
        help="Contract version recorded in the graph (default: canonical_type_version of the mapping)",
    )
    parser.add_argument(
        "--base-uri",
        default=DEFAULT_BASE_URI,
        help="Instance URI prefix; the IFC GlobalId is appended. "
        "'{project}' is replaced by the IfcProject GlobalId (default: %(default)s)",
    )
    parser.add_argument(
        "--source-system",
        help="Authoring tool for PropertySet overrides (revit, archicad, vectorworks, ifc). "
        "Detected from IfcApplication when omitted.",
    )
    parser.add_argument("--mapping", type=Path, help="Override ifc_mapping.merged.yaml")
    parser.add_argument("--schema", type=Path, help="Override the contract root schema YAML")
    parser.add_argument("-q", "--quiet", action="store_true", help="Do not print the conversion report")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    graph, report = convert(
        args.ifc,
        base_uri=args.base_uri,
        contract_version=args.contract_version,
        source_system=args.source_system,
        mapping_path=args.mapping,
        schema_path=args.schema,
    )
    turtle = to_turtle(graph)
    if args.output:
        args.output.write_text(turtle, encoding="utf-8")
    else:
        sys.stdout.write(turtle)
    if not args.quiet:
        print("\n".join(report.lines()), file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
