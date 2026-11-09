#!/usr/bin/env python3
"""Generate cost project type and cost group SKOS vocabularies plus code-only ICMS / eBKP mappings."""

from __future__ import annotations

import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "scripts"))

from cost_group_data import (  # noqa: E402
    CATEGORIES,
    CG_NS,
    CPT_NS,
    EBKPH_NS,
    EBKPT_NS,
    GROUPS,
    ICMS_NS,
    PROJECT_TYPES,
    SUBGROUPS,
    WORKS_GROUPS,
    Group,
    SubGroup,
    category_notation,
    group_notation,
    icms_subgroup_codes,
    parse_spec,
    subgroup_notation,
    ttl_escape,
)

OUT_DIR = REPO_ROOT / "classification/abstract-cost-classification"
CPT_OUT = OUT_DIR / "cost-project-types.skos.ttl"
CG_OUT = OUT_DIR / "cost-groups.skos.ttl"
MAP_DIR = REPO_ROOT / "classification/mapping"
ICMS_OUT = MAP_DIR / "abstract-cost-groups-to-icms.mapping.ttl"
EBKPH_OUT = MAP_DIR / "abstract-cost-groups-to-ebkp-h.mapping.ttl"
EBKPT_OUT = MAP_DIR / "abstract-cost-groups-to-ebkp-t.mapping.ttl"

ISSUED = "2026-11-04"
PREDICATES = {
    "exact": "skos:exactMatch",
    "close": "skos:closeMatch",
    "broad": "skos:broadMatch",
    "narrow": "skos:narrowMatch",
    "related": "skos:relatedMatch",
}

COMMON_PREFIXES = [
    "@prefix skos: <http://www.w3.org/2004/02/skos/core#> .",
    "@prefix dcterms: <http://purl.org/dc/terms/> .",
    "@prefix map: <https://example.org/mapping/> .",
]

RENEWAL_MAINTENANCE_PREFIX = {
    "3": ("Renewal", "Erneuerung"),
    "5": ("Maintenance", "Instandhaltung"),
}


def lit(text: str, lang: str) -> str:
    return f'"{ttl_escape(text)}"@{lang}'


def all_groups() -> list[Group]:
    """Explicit groups plus the shared works groups expanded for construction, renewal and maintenance."""
    explicit = {(g.category, g.code): g for g in GROUPS}
    result: list[Group] = [g for g in GROUPS if g.category == "1"]
    for category in ("2", "3", "5"):
        for code, en, de, def_en, def_de in WORKS_GROUPS:
            base = explicit.get((category, code))
            if category in RENEWAL_MAINTENANCE_PREFIX:
                pre_en, pre_de = RENEWAL_MAINTENANCE_PREFIX[category]
                label_en, label_de = f"{pre_en}: {en[0].lower()}{en[1:]}", f"{pre_de}: {de}"
            else:
                label_en, label_de = en, de
            result.append(
                Group(
                    category,
                    code,
                    label_en,
                    label_de,
                    def_en,
                    def_de,
                    ebkph=base.ebkph if base else "",
                    ebkpt=base.ebkpt if base else "",
                )
            )
    result.extend(g for g in GROUPS if g.category in ("4", "6"))
    return result


def render_project_types() -> str:
    lines = [
        f"@prefix : <{CPT_NS}> .",
        *COMMON_PREFIXES,
        "",
        ":scheme a skos:ConceptScheme ;",
        '  skos:prefLabel "Abstract cost project types"@en ;',
        '  skos:prefLabel "Abstrakte Kosten-Projektarten"@de ;',
        '  dcterms:title "Abstract cost project types"@en ;',
        '  dcterms:title "Abstrakte Kosten-Projektarten"@de ;',
        '  dcterms:identifier "AbstractCostProjectType" ;',
        '  dcterms:creator "pragmatic-bim-public-rules" ;',
        f'  dcterms:issued "{ISSUED}" ;',
        "  dcterms:license <https://creativecommons.org/licenses/by/4.0/> ;",
        "  dcterms:source <https://github.com/simondilhas/pragmatic-bim-public-rules> ;",
        "  dcterms:references map:abstractCostGroupsToIcmsMapping ;",
        '  skos:definition "Project or sub-project types used as the first dimension of a cost report. Buildings (CPT-01) and civil engineering works (CPT-02 to CPT-19) share the same cost groups; cost sub-groups state the project types they apply to. Numbering is aligned with ICMS Level 1 project codes so that a full ICMS code can be formed by prepending the project type number."@en ;',
        '  skos:definition "Projekt- oder Teilprojektarten als erste Dimension eines Kostenberichts. Gebäude (CPT-01) und Tiefbauwerke (CPT-02 bis CPT-19) teilen dieselben Kostengruppen; Kostenuntergruppen geben an, für welche Projektarten sie gelten. Die Nummerierung entspricht den ICMS-Projektcodes der Ebene 1, sodass ein vollständiger ICMS-Code durch Voranstellen der Projektartnummer gebildet werden kann."@de ;',
        '  skos:scopeNote "Own wording. ICMS is referenced by code only through the cost groups to ICMS mapping bridge; no ICMS text is reproduced."@en ;',
        '  skos:scopeNote "Eigene Formulierung. ICMS wird nur über Codes in der Mapping-Brücke Kostengruppen zu ICMS referenziert; es wird kein ICMS-Text wiedergegeben."@de ;',
        "  skos:hasTopConcept",
        "    " + ",\n    ".join(f":{pt.code}" for pt in PROJECT_TYPES) + " .",
        "",
    ]
    for pt in PROJECT_TYPES:
        lines += [
            f":{pt.code} a skos:Concept ;",
            "  skos:inScheme :scheme ;",
            "  skos:topConceptOf :scheme ;",
            f'  skos:notation "{pt.code}" ;',
            f"  skos:prefLabel {lit(pt.label_en, 'en')} ;",
            f"  skos:prefLabel {lit(pt.label_de, 'de')} ;",
            f"  skos:definition {lit(pt.definition_en, 'en')} ;",
            f"  skos:definition {lit(pt.definition_de, 'de')} .",
            "",
        ]
    return "\n".join(lines)


def render_cost_groups() -> str:
    groups = all_groups()
    lines = [
        f"@prefix : <{CG_NS}> .",
        f"@prefix cpt: <{CPT_NS}> .",
        "@prefix pbs: <https://schema.pragmaticbim.ch/> .",
        *COMMON_PREFIXES,
        "",
        ":scheme a skos:ConceptScheme ;",
        '  skos:prefLabel "Abstract cost groups"@en ;',
        '  skos:prefLabel "Abstrakte Kostengruppen"@de ;',
        '  dcterms:title "Abstract cost groups"@en ;',
        '  dcterms:title "Abstrakte Kostengruppen"@de ;',
        '  dcterms:identifier "AbstractCostGroup" ;',
        '  dcterms:creator "pragmatic-bim-public-rules" ;',
        f'  dcterms:issued "{ISSUED}" ;',
        "  dcterms:license <https://creativecommons.org/licenses/by/4.0/> ;",
        "  dcterms:source <https://github.com/simondilhas/pragmatic-bim-public-rules> ;",
        "  dcterms:references map:abstractCostGroupsToIcmsMapping, map:abstractCostGroupsToEbkpHMapping, map:abstractCostGroupsToEbkpTMapping ;",
        '  skos:definition "Open life-cycle cost structure for buildings and civil engineering works. Level 2 categories (CG-1 acquisition to CG-6 end of life), Level 3 groups (CG-{C}-{GG}) and Level 4 sub-groups (CG-{C}-{GG}-{SSS}). Construction, renewal and maintenance share the same thirteen groups. Sub-groups with a B prefix apply to buildings, those with a C prefix to civil engineering works (see pbs:projectType); sub-groups without a letter apply to all project types. Codes 800 and above are own extensions without an ICMS sub-group equivalent."@en ;',
        '  skos:definition "Offene Lebenszyklus-Kostengliederung für Hochbau und Tiefbau. Kategorien der Ebene 2 (CG-1 Erwerb bis CG-6 Lebensende), Gruppen der Ebene 3 (CG-{C}-{GG}) und Untergruppen der Ebene 4 (CG-{C}-{GG}-{SSS}). Erstellung, Erneuerung und Instandhaltung teilen dieselben dreizehn Gruppen. Untergruppen mit Präfix B gelten für Gebäude, mit Präfix C für Tiefbauwerke (siehe pbs:projectType); Untergruppen ohne Buchstaben gelten für alle Projektarten. Codes ab 800 sind eigene Erweiterungen ohne ICMS-Untergruppe."@de ;',
        '  skos:scopeNote "Own wording; group and sub-group numbering is aligned with ICMS 3 so that matches are exact by design. ICMS, eBKP-H and eBKP-T are referenced by code only in the mapping bridges; no third-party titles or definitions are reproduced. Level 4 sub-groups are provided for construction and acquisition; renewal and maintenance reuse the construction sub-group codes, operation and end of life stop at Level 3."@en ;',
        '  skos:scopeNote "Eigene Formulierung; die Nummerierung von Gruppen und Untergruppen ist auf ICMS 3 abgestimmt, sodass die Entsprechungen per Konstruktion exakt sind. ICMS, eBKP-H und eBKP-T werden in den Mapping-Brücken nur über Codes referenziert; es werden keine fremden Bezeichnungen oder Definitionen wiedergegeben. Untergruppen der Ebene 4 bestehen für Erstellung und Erwerb; Erneuerung und Instandhaltung verwenden die Untergruppencodes der Erstellung, Betrieb und Lebensende enden auf Ebene 3."@de ;',
        "  skos:hasTopConcept",
        "    " + ",\n    ".join(f":{category_notation(c.digit)}" for c in CATEGORIES) + " .",
        "",
    ]

    for cat in CATEGORIES:
        children = [group_notation(g.category, g.code) for g in groups if g.category == cat.digit]
        notation = category_notation(cat.digit)
        lines += [
            f":{notation} a skos:Concept ;",
            "  skos:inScheme :scheme ;",
            "  skos:topConceptOf :scheme ;",
            f'  skos:notation "{notation}" ;',
            f"  skos:prefLabel {lit(cat.label_en, 'en')} ;",
            f"  skos:prefLabel {lit(cat.label_de, 'de')} ;",
            f"  skos:definition {lit(cat.definition_en, 'en')} ;",
            f"  skos:definition {lit(cat.definition_de, 'de')} ;",
            "  skos:narrower " + ", ".join(f":{c}" for c in children) + " .",
            "",
        ]

    for grp in groups:
        notation = group_notation(grp.category, grp.code)
        children = [subgroup_notation(sg) for sg in SUBGROUPS if sg.category == grp.category and sg.group == grp.code]
        tail = [
            f"  skos:definition {lit(grp.definition_en, 'en')} ;",
            f"  skos:definition {lit(grp.definition_de, 'de')}",
        ]
        if children:
            tail[-1] += " ;"
            tail.append("  skos:narrower " + ", ".join(f":{c}" for c in children))
        tail[-1] += " ."
        lines += [
            f":{notation} a skos:Concept ;",
            "  skos:inScheme :scheme ;",
            f"  skos:broader :{category_notation(grp.category)} ;",
            f'  skos:notation "{notation}" ;',
            f"  skos:prefLabel {lit(grp.label_en, 'en')} ;",
            f"  skos:prefLabel {lit(grp.label_de, 'de')} ;",
            *tail,
            "",
        ]

    for sg in SUBGROUPS:
        notation = subgroup_notation(sg)
        body = [
            f":{notation} a skos:Concept ;",
            "  skos:inScheme :scheme ;",
            f"  skos:broader :{group_notation(sg.category, sg.group)} ;",
            f'  skos:notation "{notation}" ;',
            f"  skos:prefLabel {lit(sg.label_en, 'en')} ;",
            f"  skos:prefLabel {lit(sg.label_de, 'de')} ;",
            f"  skos:definition {lit(sg.definition_en, 'en')} ;",
            f"  skos:definition {lit(sg.definition_de, 'de')}",
        ]
        if sg.project_types:
            body[-1] += " ;"
            body.append("  pbs:projectType " + ", ".join(f"cpt:{pt}" for pt in sg.project_types))
        body[-1] += " ."
        lines += body + [""]
    return "\n".join(lines)


def _statement(subject: str, links: list[tuple[str, list[str]]]) -> list[str]:
    parts = [f"{PREDICATES[key]} {', '.join(targets)}" for key, targets in links if targets]
    if not parts:
        return []
    out = [f"{subject} {parts[0]}"]
    for part in parts[1:]:
        out[-1] += " ;"
        out.append(f"  {part}")
    out[-1] += " ."
    return out


def _mapping_header(dataset: str, title_en: str, title_de: str, refs: str, desc_en: str, desc_de: str) -> list[str]:
    return [
        f"map:{dataset} a dcterms:Dataset ;",
        f"  dcterms:title {lit(title_en, 'en')} ;",
        f"  dcterms:title {lit(title_de, 'de')} ;",
        f"  dcterms:references {refs} ;",
        f'  dcterms:issued "{ISSUED}" ;',
        f"  dcterms:description {lit(desc_en, 'en')} ;",
        f"  dcterms:description {lit(desc_de, 'de')} .",
        "",
    ]


def render_icms_mapping() -> str:
    lines = [
        f"@prefix cg: <{CG_NS}> .",
        f"@prefix cpt: <{CPT_NS}> .",
        f"@prefix icms: <{ICMS_NS}> .",
        *COMMON_PREFIXES,
        "",
        *_mapping_header(
            "abstractCostGroupsToIcmsMapping",
            "Abstract cost groups to ICMS mapping",
            "Mapping abstrakter Kostengruppen nach ICMS",
            "cg:scheme, cpt:scheme, icms:scheme",
            "Maps abstract cost project types and cost groups to International Cost Management Standard (ICMS, 3rd edition) codes by reference only; ICMS is copyright of the ICMS Coalition and no ICMS titles or definitions are reproduced. Project types map with skos:exactMatch to ICMS Level 1 project codes (icms:01 to icms:19). Categories and groups map with skos:exactMatch to project-independent codes (icms:2, icms:2.03). Sub-groups map with skos:closeMatch; their target local names carry the ICMS table: A. for Table A-1 acquisition, B. for Table B-1 buildings and C. for Table C-1 civil engineering works (e.g. icms:B.2.03.030). To form a full ICMS code, prepend the Level 1 project code (e.g. 01.2.03.030). Own extensions (codes 800 and above) map with skos:broadMatch to their ICMS group.",
            "Ordnet abstrakte Kosten-Projektarten und Kostengruppen den Codes des International Cost Management Standard (ICMS, 3. Ausgabe) nur per Referenz zu; ICMS ist urheberrechtlich durch die ICMS Coalition geschützt, es werden keine ICMS-Bezeichnungen oder -Definitionen wiedergegeben. Projektarten mit skos:exactMatch auf ICMS-Projektcodes der Ebene 1 (icms:01 bis icms:19). Kategorien und Gruppen mit skos:exactMatch auf projektunabhängige Codes (icms:2, icms:2.03). Untergruppen mit skos:closeMatch; der lokale Name des Ziels trägt die ICMS-Tabelle: A. für Tabelle A-1 Erwerb, B. für Tabelle B-1 Gebäude und C. für Tabelle C-1 Tiefbau (z. B. icms:B.2.03.030). Der vollständige ICMS-Code entsteht durch Voranstellen des Projektcodes (z. B. 01.2.03.030). Eigene Erweiterungen (Codes ab 800) mit skos:broadMatch auf ihre ICMS-Gruppe.",
        ),
        "# --- Project types (ICMS Level 1) ---",
        "",
    ]
    for pt in PROJECT_TYPES:
        lines.append(f"cpt:{pt.code} skos:exactMatch icms:{pt.code.removeprefix('CPT-')} .")
    lines += ["", "# --- Categories and groups (ICMS Levels 2 and 3) ---", ""]
    for cat in CATEGORIES:
        lines.append(f"cg:{category_notation(cat.digit)} skos:exactMatch icms:{cat.digit} .")
    for grp in all_groups():
        lines.append(f"cg:{group_notation(grp.category, grp.code)} skos:exactMatch icms:{grp.category}.{grp.code} .")
    lines += ["", "# --- Sub-groups (ICMS Level 4) ---", ""]
    for sg in SUBGROUPS:
        subject = f"cg:{subgroup_notation(sg)}"
        if sg.own:
            lines.append(f"{subject} skos:broadMatch icms:{sg.category}.{sg.group} .")
        else:
            targets = ", ".join(f"icms:{code}" for code in icms_subgroup_codes(sg))
            lines.append(f"{subject} skos:closeMatch {targets} .")
    return "\n".join(lines) + "\n"


def _render_ebkp_mapping(variant: str, ns: str, prefix: str, dataset: str, attr: str, desc_en: str, desc_de: str) -> str:
    lines = [
        f"@prefix cg: <{CG_NS}> .",
        f"@prefix {prefix}: <{ns}> .",
        *COMMON_PREFIXES,
        "",
        *_mapping_header(
            dataset,
            f"Abstract cost groups to {variant} mapping",
            f"Mapping abstrakter Kostengruppen nach {variant}",
            f"cg:scheme, {prefix}:scheme",
            desc_en,
            desc_de,
        ),
    ]
    sections = [
        ("Groups (Level 3)", [(f"cg:{group_notation(g.category, g.code)}", getattr(g, attr)) for g in all_groups()]),
        ("Sub-groups (Level 4)", [(f"cg:{subgroup_notation(sg)}", getattr(sg, attr)) for sg in SUBGROUPS]),
    ]
    for title, rows in sections:
        lines += [f"# --- {title} ---", ""]
        for subject, spec in rows:
            links = [(key, [f"{prefix}:{code}" for code in codes]) for key, codes in parse_spec(spec)]
            stmt = _statement(subject, links)
            if stmt:
                lines += stmt + [""]
    return "\n".join(lines)


EBKP_DESC_COMMON_EN = (
    "Codes are referenced by notation only (main group letter, element group e.g. {eg}, element e.g. {el}); "
    "{variant} is published by CRB and no CRB titles, definitions or reference quantities are reproduced. "
    "Licence holders resolve the codes against their own copy. "
    "Predicates: skos:exactMatch only for identical scope; skos:closeMatch for near-equivalent scope; "
    "skos:broadMatch where the {variant} code is broader; skos:narrowMatch where the {variant} codes are parts of the cost group; "
    "skos:relatedMatch marks an adjacent or partial line, not an equal alternative. "
    "Disambiguation: the mapping is deliberately not bijective. ICMS-shaped groups bundle by work type and life-cycle stage, "
    "{variant} by element, so one cost group can spread over several codes and vice versa. "
    "Renewal (CG-3) and maintenance (CG-5) works use the same {variant} codes as the corresponding construction (CG-2) groups. "
    "Operation (CG-4) and end of life (CG-6) have no {variant} equivalent. Unmapped sub-groups are spread across element rates in {variant}."
)
EBKP_DESC_COMMON_DE = (
    "Codes werden nur über die Notation referenziert (Hauptgruppe als Buchstabe, Elementgruppe z. B. {eg}, Element z. B. {el}); "
    "{variant} wird von CRB herausgegeben, es werden keine CRB-Bezeichnungen, Definitionen oder Bezugsgrössen wiedergegeben. "
    "Lizenznehmende lösen die Codes mit ihrer eigenen Ausgabe auf. "
    "Prädikate: skos:exactMatch nur bei identischem Umfang; skos:closeMatch bei nahezu gleichem Umfang; "
    "skos:broadMatch, wenn der {variant}-Code umfassender ist; skos:narrowMatch, wenn die {variant}-Codes Teile der Kostengruppe sind; "
    "skos:relatedMatch bezeichnet eine benachbarte oder teilweise Position, keine gleichwertige Alternative. "
    "Disambiguierung: Das Mapping ist bewusst nicht eindeutig. Die ICMS-orientierten Gruppen gliedern nach Leistungsart und Lebenszyklusphase, "
    "{variant} nach Elementen; eine Kostengruppe kann sich daher auf mehrere Codes verteilen und umgekehrt. "
    "Erneuerung (CG-3) und Instandhaltung (CG-5) verwenden dieselben {variant}-Codes wie die entsprechenden Gruppen der Erstellung (CG-2). "
    "Betrieb (CG-4) und Lebensende (CG-6) haben keine {variant}-Entsprechung. Nicht zugeordnete Untergruppen sind in {variant} auf die Elementkosten verteilt."
)


def render_ebkph_mapping() -> str:
    return _render_ebkp_mapping(
        "eBKP-H",
        EBKPH_NS,
        "ebkph",
        "abstractCostGroupsToEbkpHMapping",
        "ebkph",
        "Maps abstract cost groups to eBKP-H (SN 506 511, Hochbau) codes for buildings (CPT-01) and for the project-independent groups. "
        + EBKP_DESC_COMMON_EN.format(variant="eBKP-H", eg="C01", el="C01.01"),
        "Ordnet abstrakte Kostengruppen den Codes des eBKP-H (SN 506 511, Hochbau) für Gebäude (CPT-01) und für die projektunabhängigen Gruppen zu. "
        + EBKP_DESC_COMMON_DE.format(variant="eBKP-H", eg="C01", el="C01.01"),
    )


def render_ebkpt_mapping() -> str:
    return _render_ebkp_mapping(
        "eBKP-T",
        EBKPT_NS,
        "ebkpt",
        "abstractCostGroupsToEbkpTMapping",
        "ebkpt",
        "Maps abstract cost groups to eBKP-T (SN 506 512, Tiefbau) codes for civil engineering works (CPT-02 to CPT-19) and for the project-independent groups. Main groups A and V to Z are identical in eBKP-H and eBKP-T. Most links target element groups because element-level codes are only partly public. "
        + EBKP_DESC_COMMON_EN.format(variant="eBKP-T", eg="M01", el="M01.03"),
        "Ordnet abstrakte Kostengruppen den Codes des eBKP-T (SN 506 512, Tiefbau) für Tiefbauwerke (CPT-02 bis CPT-19) und für die projektunabhängigen Gruppen zu. Die Hauptgruppen A sowie V bis Z sind in eBKP-H und eBKP-T identisch. Die meisten Verweise zielen auf Elementgruppen, da die Elementcodes nur teilweise öffentlich sind. "
        + EBKP_DESC_COMMON_DE.format(variant="eBKP-T", eg="M01", el="M01.03"),
    )


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    outputs = {
        CPT_OUT: render_project_types(),
        CG_OUT: render_cost_groups(),
        ICMS_OUT: render_icms_mapping(),
        EBKPH_OUT: render_ebkph_mapping(),
        EBKPT_OUT: render_ebkpt_mapping(),
    }
    for path, text in outputs.items():
        path.write_text(text, encoding="utf-8")
        print(f"Wrote {path.relative_to(REPO_ROOT)}")


if __name__ == "__main__":
    main()
