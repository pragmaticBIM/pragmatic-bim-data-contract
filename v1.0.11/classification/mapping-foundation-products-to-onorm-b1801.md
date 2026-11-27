# Abstract foundation products to ÖNORM B 1801 mapping

Source: [`abstract-foundation-products-to-onorm-b1801.mapping.ttl`](sources/mapping-foundation-products-to-onorm-b1801.ttl)

External target labels are not shipped in this repository; only codes and IRIs are shown.

## Dataset

- **description (de):** Ordnet abstrakte Fundamentprodukte den Codes der Leistungsgliederung Hochbau nach ÖNORM B 1801-1:2022 nur per Referenz zu (z. B. 2.H07, 2.H04, 2.H08). IRI-Lokalnamen mit Unterstrich fuer den Punkt. Codes nur ueber Notation; ÖNORM B 1801 wird von Austrian Standards herausgegeben, es werden keine Bezeichnungen oder Definitionen wiedergegeben. Lizenznehmende loesen die Codes mit ihrer eigenen Ausgabe auf. closeMatch ist die Leit-Leistungsgruppe; relatedMatch eine sekundaere oder benachbarte Position. Disambiguierung: Das Mapping ist bewusst nicht eindeutig.
- **description (en):** Maps abstract foundation product concepts to ÖNORM B 1801-1:2022 Leistungsgliederung Hochbau codes by reference only (e.g. 2.H07, 2.H04, 2.H08). IRI local names use underscore for the dot. Codes are referenced by notation; ÖNORM B 1801 is published by Austrian Standards and no titles or definitions are reproduced. Licence holders resolve the codes against their own copy. closeMatch is the leading Leistungsgruppe; relatedMatch marks a secondary or adjacent line. Disambiguation: the mapping is deliberately not bijective.
- **title (de):** Mapping abstrakter Fundamentprodukte nach ÖNORM B 1801
- **title (en):** Abstract foundation products to ÖNORM B 1801 mapping

## Links

| Source | Relation | Targets |
| --- | --- | --- |
| `fdp:FDP-DRAINAGE` | `closeMatch` | `onorm1801:2-H03` |
| `fdp:FDP-DRAINAGE` | `relatedMatch` | `onorm1801:2-H08` |
| `fdp:FDP-GROUND-INJECTION` | `closeMatch` | `onorm1801:2-H04` |
| `fdp:FDP-MICRO-PILE` | `closeMatch` | `onorm1801:2-H04` |
| `fdp:FDP-MICRO-PILE-GROUTED` | `closeMatch` | `onorm1801:2-H04` |
| `fdp:FDP-PAD` | `closeMatch` | `onorm1801:2-H07` |
| `fdp:FDP-PILE` | `closeMatch` | `onorm1801:2-H04` |
| `fdp:FDP-PILE` | `relatedMatch` | `onorm1801:2-H07` |
| `fdp:FDP-PILE-BORED` | `closeMatch` | `onorm1801:2-H04` |
| `fdp:FDP-PILE-BORED` | `relatedMatch` | `onorm1801:2-H07` |
| `fdp:FDP-PILE-DRIVEN` | `closeMatch` | `onorm1801:2-H04` |
| `fdp:FDP-PILE-DRIVEN` | `relatedMatch` | `onorm1801:2-H07` |
| `fdp:FDP-RAFT` | `closeMatch` | `onorm1801:2-H07` |
| `fdp:FDP-RAFT-INS` | `closeMatch` | `onorm1801:2-H08` |
| `fdp:FDP-RAFT-INS` | `relatedMatch` | `onorm1801:2-H07` |
| `fdp:FDP-RETAINING` | `closeMatch` | `onorm1801:2-H07` |
| `fdp:FDP-RETAINING` | `relatedMatch` | `onorm1801:2-H04` |
| `fdp:FDP-RETAINING-INS` | `closeMatch` | `onorm1801:2-H08` |
| `fdp:FDP-RETAINING-INS` | `relatedMatch` | `onorm1801:2-H04` |
| `fdp:FDP-RETAINING-INSITU` | `closeMatch` | `onorm1801:2-H07` |
| `fdp:FDP-RETAINING-INSITU` | `relatedMatch` | `onorm1801:2-H04` |
| `fdp:FDP-RETAINING-PRECAST` | `closeMatch` | `onorm1801:2-H07` |
| `fdp:FDP-RETAINING-PRECAST` | `relatedMatch` | `onorm1801:2-H04` |
| `fdp:FDP-RETAINING-SHORING` | `closeMatch` | `onorm1801:2-H04` |
| `fdp:FDP-RETAINING-SHORING` | `relatedMatch` | `onorm1801:2-H07` |
| `fdp:FDP-SOIL-REPLACEMENT` | `closeMatch` | `onorm1801:2-H03` |
| `fdp:FDP-SOIL-REPLACEMENT` | `relatedMatch` | `onorm1801:2-H04` |
| `fdp:FDP-STRIP` | `closeMatch` | `onorm1801:2-H07` |
| `fdp:FDP-WATERPROOF` | `closeMatch` | `onorm1801:2-H08` |
| `fdp:FDP-WATERPROOF-CONCRETE` | `closeMatch` | `onorm1801:2-H08` |
| `fdp:FDP-WATERPROOF-CONCRETE` | `relatedMatch` | `onorm1801:2-H07` |
| `fdp:FDP-WATERPROOF-MEMBRANE` | `closeMatch` | `onorm1801:2-H08` |
