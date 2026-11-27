# Abstract connector products to ÖNORM B 1801 mapping

Source: [`abstract-connector-products-to-onorm-b1801.mapping.ttl`](sources/mapping-connector-products-to-onorm-b1801.ttl)

External target labels are not shipped in this repository; only codes and IRIs are shown.

## Dataset

- **description (de):** Ordnet abstrakte Tuer- und Fenster-Verbindungsprodukte den Codes der Leistungsgliederung Hochbau nach ÖNORM B 1801-1:2022 nur per Referenz zu (z. B. 2.H36, 4.H37). IRI-Lokalnamen mit Unterstrich fuer den Punkt. Codes nur ueber Notation; ÖNORM B 1801 wird von Austrian Standards herausgegeben, es werden keine Bezeichnungen oder Definitionen wiedergegeben. Lizenznehmende loesen die Codes mit ihrer eigenen Ausgabe auf. closeMatch ist die Leit-Leistungsgruppe; relatedMatch eine sekundaere oder benachbarte Position. Disambiguierung: Das Mapping ist bewusst nicht eindeutig.
- **description (en):** Maps abstract door and window connector product concepts to ÖNORM B 1801-1:2022 Leistungsgliederung Hochbau codes by reference only (e.g. 2.H36, 4.H37). IRI local names use underscore for the dot. Codes are referenced by notation; ÖNORM B 1801 is published by Austrian Standards and no titles or definitions are reproduced. Licence holders resolve the codes against their own copy. closeMatch is the leading Leistungsgruppe; relatedMatch marks a secondary or adjacent line (e.g. interior vs exterior). Disambiguation: the mapping is deliberately not bijective.
- **title (de):** Mapping abstrakter Verbindungsprodukte nach ÖNORM B 1801
- **title (en):** Abstract connector products to ÖNORM B 1801 mapping

## Links

| Source | Relation | Targets |
| --- | --- | --- |
| `dcp:DCP-GATE` | `closeMatch` | `onorm1801:2-H37` |
| `dcp:DCP-GATE-FOLDING` | `closeMatch` | `onorm1801:2-H37` |
| `dcp:DCP-GATE-ROLLING` | `closeMatch` | `onorm1801:2-H37` |
| `dcp:DCP-GATE-SECTIONAL` | `closeMatch` | `onorm1801:2-H37` |
| `dcp:DCP-GATE-SLIDING` | `closeMatch` | `onorm1801:2-H37` |
| `dcp:DCP-GATE-UP-OVER` | `closeMatch` | `onorm1801:2-H37` |
| `dcp:DCP-GLASS` | `closeMatch` | `onorm1801:2-H36` |
| `dcp:DCP-GLASS` | `relatedMatch` | `onorm1801:2-H37` |
| `dcp:DCP-GLASS-AUTOMATIC` | `closeMatch` | `onorm1801:2-H37` |
| `dcp:DCP-GLASS-AUTOMATIC` | `relatedMatch` | `onorm1801:2-H36` |
| `dcp:DCP-GLASS-FRAMED` | `closeMatch` | `onorm1801:2-H36` |
| `dcp:DCP-GLASS-FRAMED` | `relatedMatch` | `onorm1801:2-H37` |
| `dcp:DCP-GLASS-FRAMELESS` | `closeMatch` | `onorm1801:2-H36` |
| `dcp:DCP-GLASS-FRAMELESS` | `relatedMatch` | `onorm1801:2-H37` |
| `dcp:DCP-METAL` | `closeMatch` | `onorm1801:2-H37` |
| `dcp:DCP-METAL` | `relatedMatch` | `onorm1801:4-H37` |
| `dcp:DCP-PVC` | `closeMatch` | `onorm1801:2-H37` |
| `dcp:DCP-PVC` | `relatedMatch` | `onorm1801:4-H37` |
| `dcp:DCP-SPECIAL` | `closeMatch` | `onorm1801:2-H37` |
| `dcp:DCP-SPECIAL` | `relatedMatch` | `onorm1801:4-H37` |
| `dcp:DCP-WOOD` | `closeMatch` | `onorm1801:2-H37` |
| `dcp:DCP-WOOD` | `relatedMatch` | `onorm1801:4-H37` |
| `dcp:DCP-WOOD-ENTRANCE` | `closeMatch` | `onorm1801:2-H37` |
| `dcp:DCP-WOOD-ENTRANCE` | `relatedMatch` | `onorm1801:4-H37` |
| `dcp:DCP-WOOD-INTERIOR` | `closeMatch` | `onorm1801:4-H37` |
| `dcp:DCP-WOOD-INTERIOR` | `relatedMatch` | `onorm1801:2-H37` |
| `dcp:DCP-WOOD-METAL` | `closeMatch` | `onorm1801:2-H37` |
| `dcp:DCP-WOOD-METAL` | `relatedMatch` | `onorm1801:4-H37` |
| `dcp:DCP-WOOD-RATED` | `closeMatch` | `onorm1801:2-H37` |
| `dcp:DCP-WOOD-RATED` | `relatedMatch` | `onorm1801:4-H37` |
| `wicp:WICP-ALUMINIUM` | `closeMatch` | `onorm1801:2-H36` |
| `wicp:WICP-ALUMINIUM` | `relatedMatch` | `onorm1801:4-H36` |
| `wicp:WICP-FACADE-UNIT` | `closeMatch` | `onorm1801:2-H36` |
| `wicp:WICP-PVC` | `closeMatch` | `onorm1801:2-H36` |
| `wicp:WICP-PVC` | `relatedMatch` | `onorm1801:4-H36` |
| `wicp:WICP-ROOF-DOME` | `closeMatch` | `onorm1801:2-H09` |
| `wicp:WICP-ROOF-DOME` | `relatedMatch` | `onorm1801:2-H36` |
| `wicp:WICP-ROOF-WINDOW` | `closeMatch` | `onorm1801:2-H09` |
| `wicp:WICP-ROOF-WINDOW` | `relatedMatch` | `onorm1801:2-H36` |
| `wicp:WICP-ROOFLIGHT-BAND` | `closeMatch` | `onorm1801:2-H09` |
| `wicp:WICP-ROOFLIGHT-BAND` | `relatedMatch` | `onorm1801:2-H36` |
| `wicp:WICP-SKYLIGHT` | `closeMatch` | `onorm1801:2-H09` |
| `wicp:WICP-SKYLIGHT` | `relatedMatch` | `onorm1801:2-H36` |
| `wicp:WICP-SPECIAL` | `closeMatch` | `onorm1801:2-H36` |
| `wicp:WICP-SPECIAL` | `relatedMatch` | `onorm1801:4-H36` |
| `wicp:WICP-STEEL` | `closeMatch` | `onorm1801:2-H36` |
| `wicp:WICP-STEEL` | `relatedMatch` | `onorm1801:4-H36` |
| `wicp:WICP-WOOD` | `closeMatch` | `onorm1801:2-H36` |
| `wicp:WICP-WOOD` | `relatedMatch` | `onorm1801:4-H36` |
| `wicp:WICP-WOOD-METAL` | `closeMatch` | `onorm1801:2-H36` |
| `wicp:WICP-WOOD-METAL` | `relatedMatch` | `onorm1801:4-H36` |
