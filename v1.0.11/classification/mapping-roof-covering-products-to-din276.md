# Abstract roof covering products to DIN 276 mapping

Source: [`abstract-roof-covering-products-to-din276.mapping.ttl`](sources/mapping-roof-covering-products-to-din276.ttl)

External target labels are not shipped in this repository; only codes and IRIs are shown.

## Dataset

- **description (de):** Ordnet abstrakte Dachbekleidungsprodukte den Kostengruppen der DIN 276:2018 nur per Referenz zu: Dachbelaege 363, konstruktionsnahe related 361, Dachoeffnungen related 362, Photovoltaik 442. Codes nur ueber Notation; DIN 276 wird vom DIN herausgegeben, es werden keine DIN-Bezeichnungen oder -Definitionen wiedergegeben. Lizenznehmende loesen die Codes mit ihrer eigenen Ausgabe auf. closeMatch ist die Leitgruppe; relatedMatch eine sekundaere oder benachbarte Gruppe. Disambiguierung: DIN 276 ist bewusst nicht eindeutig.
- **description (en):** Maps abstract roof covering product concepts to DIN 276:2018 Kostengruppen by reference only: roof coverings 363, structure-heavy related 361, roof openings related 362, photovoltaics 442. Codes are referenced by notation; DIN 276 is published by DIN and no DIN titles or definitions are reproduced. Licence holders resolve the codes against their own copy. closeMatch is the leading cost group; relatedMatch marks a secondary or adjacent group. Disambiguation: DIN 276 is deliberately not bijective.
- **title (de):** Mapping abstrakter Dachbekleidungsprodukte nach DIN 276
- **title (en):** Abstract roof covering products to DIN 276 mapping

## Links

| Source | Relation | Targets |
| --- | --- | --- |
| `rcp:RCP-FLAT-BITUMEN` | `closeMatch` | `din276:363` |
| `rcp:RCP-FLAT-LIQUID` | `closeMatch` | `din276:363` |
| `rcp:RCP-FLAT-SINGLE-PLY` | `closeMatch` | `din276:363` |
| `rcp:RCP-GREEN-EXTENSIVE` | `closeMatch` | `din276:363` |
| `rcp:RCP-GREEN-INTENSIVE` | `closeMatch` | `din276:363` |
| `rcp:RCP-METAL-SHEET` | `closeMatch` | `din276:363` |
| `rcp:RCP-PV-INTEGRATED` | `closeMatch` | `din276:363` |
| `rcp:RCP-PV-INTEGRATED` | `closeMatch` | `din276:442` |
| `rcp:RCP-PV-MOUNTED` | `closeMatch` | `din276:442` |
| `rcp:RCP-PV-MOUNTED` | `relatedMatch` | `din276:363` |
| `rcp:RCP-PV-ROOF` | `closeMatch` | `din276:442` |
| `rcp:RCP-PV-ROOF` | `relatedMatch` | `din276:363` |
| `rcp:RCP-SLATE` | `closeMatch` | `din276:363` |
| `rcp:RCP-TILE-CLAY` | `closeMatch` | `din276:363` |
| `rcp:RCP-TILE-CONCRETE` | `closeMatch` | `din276:363` |
| `rcp:RCP-WOOD-SHINGLE` | `closeMatch` | `din276:363` |
| `rcp:RCP-WOOD-SHINGLE` | `relatedMatch` | `din276:361` |
