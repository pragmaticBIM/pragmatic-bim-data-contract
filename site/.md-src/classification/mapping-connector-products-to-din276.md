# Abstract connector products to DIN 276 mapping

Source: [`abstract-connector-products-to-din276.mapping.ttl`](sources/mapping-connector-products-to-din276.ttl)

External target labels are not shipped in this repository; only codes and IRIs are shown.

## Dataset

- **description (de):** Ordnet abstrakte Tuer- und Fenster-Verbindungsprodukte den Kostengruppen der DIN 276:2018 nur per Referenz zu: Aussenwand oeffnungen 334, Innenwand oeffnungen 344, Dachoeffnungen 362. Codes nur ueber Notation; DIN 276 wird vom DIN herausgegeben, es werden keine DIN-Bezeichnungen oder -Definitionen wiedergegeben. Lizenznehmende loesen die Codes mit ihrer eigenen Ausgabe auf. closeMatch ist die Leitgruppe aussen; relatedMatch die Innen-Alternative. Disambiguierung: DIN 276 ist bewusst nicht eindeutig.
- **description (en):** Maps abstract door and window connector product concepts to DIN 276:2018 Kostengruppen by reference only: exterior openings 334, interior openings 344, roof openings 362. Codes are referenced by notation; DIN 276 is published by DIN and no DIN titles or definitions are reproduced. Licence holders resolve the codes against their own copy. closeMatch is the leading exterior cost group; relatedMatch marks the interior alternative where the product may be booked under either. Disambiguation: DIN 276 is deliberately not bijective.
- **title (de):** Mapping abstrakter Verbindungsprodukte nach DIN 276
- **title (en):** Abstract connector products to DIN 276 mapping

## Links

| Source | Relation | Targets |
| --- | --- | --- |
| `dcp:DCP-GATE` | `closeMatch` | `din276:334` |
| `dcp:DCP-GATE` | `relatedMatch` | `din276:344` |
| `dcp:DCP-GATE-FOLDING` | `closeMatch` | `din276:334` |
| `dcp:DCP-GATE-FOLDING` | `relatedMatch` | `din276:344` |
| `dcp:DCP-GATE-ROLLING` | `closeMatch` | `din276:334` |
| `dcp:DCP-GATE-ROLLING` | `relatedMatch` | `din276:344` |
| `dcp:DCP-GATE-SECTIONAL` | `closeMatch` | `din276:334` |
| `dcp:DCP-GATE-SECTIONAL` | `relatedMatch` | `din276:344` |
| `dcp:DCP-GATE-SLIDING` | `closeMatch` | `din276:334` |
| `dcp:DCP-GATE-SLIDING` | `relatedMatch` | `din276:344` |
| `dcp:DCP-GATE-UP-OVER` | `closeMatch` | `din276:334` |
| `dcp:DCP-GATE-UP-OVER` | `relatedMatch` | `din276:344` |
| `dcp:DCP-GLASS` | `closeMatch` | `din276:334` |
| `dcp:DCP-GLASS` | `relatedMatch` | `din276:344` |
| `dcp:DCP-GLASS-AUTOMATIC` | `closeMatch` | `din276:334` |
| `dcp:DCP-GLASS-AUTOMATIC` | `relatedMatch` | `din276:344` |
| `dcp:DCP-GLASS-FRAMED` | `closeMatch` | `din276:334` |
| `dcp:DCP-GLASS-FRAMED` | `relatedMatch` | `din276:344` |
| `dcp:DCP-GLASS-FRAMELESS` | `closeMatch` | `din276:334` |
| `dcp:DCP-GLASS-FRAMELESS` | `relatedMatch` | `din276:344` |
| `dcp:DCP-METAL` | `closeMatch` | `din276:334` |
| `dcp:DCP-METAL` | `relatedMatch` | `din276:344` |
| `dcp:DCP-PVC` | `closeMatch` | `din276:334` |
| `dcp:DCP-PVC` | `relatedMatch` | `din276:344` |
| `dcp:DCP-SPECIAL` | `closeMatch` | `din276:334` |
| `dcp:DCP-SPECIAL` | `relatedMatch` | `din276:344` |
| `dcp:DCP-WOOD` | `closeMatch` | `din276:334` |
| `dcp:DCP-WOOD` | `relatedMatch` | `din276:344` |
| `dcp:DCP-WOOD-ENTRANCE` | `closeMatch` | `din276:334` |
| `dcp:DCP-WOOD-ENTRANCE` | `relatedMatch` | `din276:344` |
| `dcp:DCP-WOOD-INTERIOR` | `closeMatch` | `din276:344` |
| `dcp:DCP-WOOD-INTERIOR` | `relatedMatch` | `din276:334` |
| `dcp:DCP-WOOD-METAL` | `closeMatch` | `din276:334` |
| `dcp:DCP-WOOD-METAL` | `relatedMatch` | `din276:344` |
| `dcp:DCP-WOOD-RATED` | `closeMatch` | `din276:334` |
| `dcp:DCP-WOOD-RATED` | `relatedMatch` | `din276:344` |
| `wicp:WICP-ALUMINIUM` | `closeMatch` | `din276:334` |
| `wicp:WICP-ALUMINIUM` | `relatedMatch` | `din276:344` |
| `wicp:WICP-FACADE-UNIT` | `closeMatch` | `din276:334` |
| `wicp:WICP-FACADE-UNIT` | `relatedMatch` | `din276:337` |
| `wicp:WICP-PVC` | `closeMatch` | `din276:334` |
| `wicp:WICP-PVC` | `relatedMatch` | `din276:344` |
| `wicp:WICP-ROOF-DOME` | `closeMatch` | `din276:362` |
| `wicp:WICP-ROOF-DOME` | `relatedMatch` | `din276:334` |
| `wicp:WICP-ROOF-WINDOW` | `closeMatch` | `din276:362` |
| `wicp:WICP-ROOF-WINDOW` | `relatedMatch` | `din276:334` |
| `wicp:WICP-ROOFLIGHT-BAND` | `closeMatch` | `din276:362` |
| `wicp:WICP-ROOFLIGHT-BAND` | `relatedMatch` | `din276:334` |
| `wicp:WICP-SKYLIGHT` | `closeMatch` | `din276:362` |
| `wicp:WICP-SKYLIGHT` | `relatedMatch` | `din276:334` |
| `wicp:WICP-SPECIAL` | `closeMatch` | `din276:334` |
| `wicp:WICP-SPECIAL` | `relatedMatch` | `din276:344` |
| `wicp:WICP-STEEL` | `closeMatch` | `din276:334` |
| `wicp:WICP-STEEL` | `relatedMatch` | `din276:344` |
| `wicp:WICP-WOOD` | `closeMatch` | `din276:334` |
| `wicp:WICP-WOOD` | `relatedMatch` | `din276:344` |
| `wicp:WICP-WOOD-METAL` | `closeMatch` | `din276:334` |
| `wicp:WICP-WOOD-METAL` | `relatedMatch` | `din276:344` |
