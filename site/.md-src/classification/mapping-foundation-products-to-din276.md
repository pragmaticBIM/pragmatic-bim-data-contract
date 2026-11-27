# Abstract foundation products to DIN 276 mapping

Source: [`abstract-foundation-products-to-din276.mapping.ttl`](sources/mapping-foundation-products-to-din276.ttl)

External target labels are not shipped in this repository; only codes and IRIs are shown.

## Dataset

- **description (de):** Ordnet abstrakte Fundamentprodukte den Kostengruppen der DIN 276:2018 nur per Referenz zu: Flachgruendungen 322, Tiefgruendungen 323, Baugrundverbesserung 321, Abdichtungen 325, Draenagen 326, Baugrubenverbau related 312. Codes nur ueber Notation; DIN 276 wird vom DIN herausgegeben, es werden keine DIN-Bezeichnungen oder -Definitionen wiedergegeben. Lizenznehmende loesen die Codes mit ihrer eigenen Ausgabe auf. closeMatch ist die Leitgruppe; relatedMatch eine sekundaere oder benachbarte Gruppe. Disambiguierung: DIN 276 ist bewusst nicht eindeutig.
- **description (en):** Maps abstract foundation product concepts to DIN 276:2018 Kostengruppen by reference only: shallow foundations 322, deep foundations 323, ground improvement 321, waterproofing 325, drainage 326, excavation support related 312. Codes are referenced by notation; DIN 276 is published by DIN and no DIN titles or definitions are reproduced. Licence holders resolve the codes against their own copy. closeMatch is the leading cost group; relatedMatch marks a secondary or adjacent group. Disambiguation: DIN 276 is deliberately not bijective.
- **title (de):** Mapping abstrakter Fundamentprodukte nach DIN 276
- **title (en):** Abstract foundation products to DIN 276 mapping

## Links

| Source | Relation | Targets |
| --- | --- | --- |
| `fdp:FDP-DRAINAGE` | `closeMatch` | `din276:326` |
| `fdp:FDP-DRAINAGE` | `relatedMatch` | `din276:325` |
| `fdp:FDP-GROUND-INJECTION` | `closeMatch` | `din276:321` |
| `fdp:FDP-MICRO-PILE` | `closeMatch` | `din276:323` |
| `fdp:FDP-MICRO-PILE` | `relatedMatch` | `din276:321` |
| `fdp:FDP-MICRO-PILE-GROUTED` | `closeMatch` | `din276:323` |
| `fdp:FDP-MICRO-PILE-GROUTED` | `relatedMatch` | `din276:321` |
| `fdp:FDP-PAD` | `closeMatch` | `din276:322` |
| `fdp:FDP-PILE` | `closeMatch` | `din276:323` |
| `fdp:FDP-PILE-BORED` | `closeMatch` | `din276:323` |
| `fdp:FDP-PILE-DRIVEN` | `closeMatch` | `din276:323` |
| `fdp:FDP-RAFT` | `closeMatch` | `din276:322` |
| `fdp:FDP-RAFT-INS` | `closeMatch` | `din276:325` |
| `fdp:FDP-RAFT-INS` | `relatedMatch` | `din276:322` |
| `fdp:FDP-RETAINING` | `closeMatch` | `din276:312` |
| `fdp:FDP-RETAINING` | `closeMatch` | `din276:322` |
| `fdp:FDP-RETAINING-INS` | `closeMatch` | `din276:325` |
| `fdp:FDP-RETAINING-INS` | `relatedMatch` | `din276:312` |
| `fdp:FDP-RETAINING-INSITU` | `closeMatch` | `din276:312` |
| `fdp:FDP-RETAINING-INSITU` | `closeMatch` | `din276:322` |
| `fdp:FDP-RETAINING-PRECAST` | `closeMatch` | `din276:312` |
| `fdp:FDP-RETAINING-PRECAST` | `closeMatch` | `din276:322` |
| `fdp:FDP-RETAINING-SHORING` | `closeMatch` | `din276:312` |
| `fdp:FDP-RETAINING-SHORING` | `relatedMatch` | `din276:322` |
| `fdp:FDP-SOIL-REPLACEMENT` | `closeMatch` | `din276:321` |
| `fdp:FDP-STRIP` | `closeMatch` | `din276:322` |
| `fdp:FDP-WATERPROOF` | `closeMatch` | `din276:325` |
| `fdp:FDP-WATERPROOF-CONCRETE` | `closeMatch` | `din276:325` |
| `fdp:FDP-WATERPROOF-CONCRETE` | `relatedMatch` | `din276:322` |
| `fdp:FDP-WATERPROOF-MEMBRANE` | `closeMatch` | `din276:325` |
