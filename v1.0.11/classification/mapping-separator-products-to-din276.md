# Abstract separator products to DIN 276 mapping

Source: [`abstract-separator-products-to-din276.mapping.ttl`](sources/mapping-separator-products-to-din276.ttl)

External target labels are not shipped in this repository; only codes and IRIs are shown.

## Dataset

- **description (de):** Ordnet abstrakte Trennelementprodukte den Kostengruppen der DIN 276:2018 nur per Referenz zu (z. B. 331, 341, 351). Codes nur ueber Notation; DIN 276 wird vom DIN herausgegeben, es werden keine DIN-Bezeichnungen oder -Definitionen wiedergegeben. Lizenznehmende loesen die Codes mit ihrer eigenen Ausgabe auf. closeMatch ist die Leitgruppe; wo Aussen- vs Innenlage am Produkt nicht kodiert ist, stehen 331 und 341 (bzw. 330er und 340er) als gleichwertige closeMatch-Alternativen — Building Separator Wall Role entscheidet bei der Zuweisung. relatedMatch bezeichnet eine sekundaere oder benachbarte Gruppe. Disambiguierung: DIN 276 ist bewusst nicht eindeutig; Bauweisen fallen oft unter dieselbe Kostengruppe.
- **description (en):** Maps abstract separator product concepts to DIN 276:2018 Kostengruppen by reference only (e.g. 331, 341, 351). Codes are referenced by notation; DIN 276 is published by DIN and no DIN titles or definitions are reproduced. Licence holders resolve the codes against their own copy. closeMatch is the leading cost group; where exterior vs interior is not encoded on the product, both 331 and 341 (or both 330-series and 340-series) are listed as equal closeMatch alternatives — Building Separator Wall Role chooses at assignment time. relatedMatch marks a secondary or adjacent group. Disambiguation: DIN 276 is deliberately not bijective; construction method often collapses under the same Kostengruppe.
- **title (de):** Mapping abstrakter Trennelementprodukte nach DIN 276
- **title (en):** Abstract separator products to DIN 276 mapping

## Links

| Source | Relation | Targets |
| --- | --- | --- |
| `ssp:SSP-CLT` | `closeMatch` | `din276:351` |
| `ssp:SSP-COMPOSITE-BEAM` | `closeMatch` | `din276:351` |
| `ssp:SSP-COMPOSITE-DECK` | `closeMatch` | `din276:351` |
| `ssp:SSP-COMPOSITE-DECK` | `relatedMatch` | `din276:355` |
| `ssp:SSP-HBV` | `closeMatch` | `din276:351` |
| `ssp:SSP-HBV` | `relatedMatch` | `din276:355` |
| `ssp:SSP-HBV-INSITU` | `closeMatch` | `din276:351` |
| `ssp:SSP-HBV-PRECAST` | `closeMatch` | `din276:355` |
| `ssp:SSP-HBV-PRECAST` | `relatedMatch` | `din276:351` |
| `ssp:SSP-HOLZ-LEHM` | `closeMatch` | `din276:351` |
| `ssp:SSP-INSITU` | `closeMatch` | `din276:351` |
| `ssp:SSP-LIGHTWEIGHT` | `closeMatch` | `din276:351` |
| `ssp:SSP-LIGHTWEIGHT` | `relatedMatch` | `din276:355` |
| `ssp:SSP-PREFAB-CONC` | `closeMatch` | `din276:355` |
| `ssp:SSP-PREFAB-CONC` | `relatedMatch` | `din276:351` |
| `ssp:SSP-STEEL-COMPOSITE` | `closeMatch` | `din276:351` |
| `ssp:SSP-STEEL-COMPOSITE` | `relatedMatch` | `din276:355` |
| `ssp:SSP-TIMBER` | `closeMatch` | `din276:351` |
| `ssp:SSP-TIMBER-CLAY` | `closeMatch` | `din276:351` |
| `ssp:SSP-TIMBER-CONCRETE` | `closeMatch` | `din276:351` |
| `ssp:SSP-TIMBER-CONCRETE` | `relatedMatch` | `din276:355` |
| `ssp:SSP-TIMBER-CONCRETE-INSITU` | `closeMatch` | `din276:351` |
| `ssp:SSP-TIMBER-CONCRETE-PRECAST` | `closeMatch` | `din276:355` |
| `ssp:SSP-TIMBER-CONCRETE-PRECAST` | `relatedMatch` | `din276:351` |
| `swp:SWP-BLT` | `closeMatch` | `din276:337` |
| `swp:SWP-BLT` | `closeMatch` | `din276:346` |
| `swp:SWP-BLT` | `relatedMatch` | `din276:331` |
| `swp:SWP-BLT` | `relatedMatch` | `din276:341` |
| `swp:SWP-BLT-PANEL` | `closeMatch` | `din276:337` |
| `swp:SWP-BLT-PANEL` | `closeMatch` | `din276:346` |
| `swp:SWP-BLT-PANEL` | `relatedMatch` | `din276:331` |
| `swp:SWP-BLT-PANEL` | `relatedMatch` | `din276:341` |
| `swp:SWP-CURTAIN-WALL` | `closeMatch` | `din276:334` |
| `swp:SWP-CURTAIN-WALL` | `closeMatch` | `din276:337` |
| `swp:SWP-CURTAIN-WALL-STICK` | `closeMatch` | `din276:334` |
| `swp:SWP-CURTAIN-WALL-STICK` | `closeMatch` | `din276:337` |
| `swp:SWP-CURTAIN-WALL-UNITISED` | `closeMatch` | `din276:337` |
| `swp:SWP-CURTAIN-WALL-UNITISED` | `relatedMatch` | `din276:334` |
| `swp:SWP-DRYWALL` | `closeMatch` | `din276:342` |
| `swp:SWP-DRYWALL` | `relatedMatch` | `din276:346` |
| `swp:SWP-ELEMENT-WALL` | `closeMatch` | `din276:346` |
| `swp:SWP-ELEMENT-WALL` | `relatedMatch` | `din276:342` |
| `swp:SWP-INSITU-CONCRETE` | `closeMatch` | `din276:331` |
| `swp:SWP-INSITU-CONCRETE` | `closeMatch` | `din276:341` |
| `swp:SWP-LEICHTBAU` | `closeMatch` | `din276:332` |
| `swp:SWP-LEICHTBAU` | `closeMatch` | `din276:342` |
| `swp:SWP-LEICHTBAU` | `relatedMatch` | `din276:337` |
| `swp:SWP-LEICHTBAU` | `relatedMatch` | `din276:346` |
| `swp:SWP-LIGHTWEIGHT` | `closeMatch` | `din276:332` |
| `swp:SWP-LIGHTWEIGHT` | `closeMatch` | `din276:342` |
| `swp:SWP-LIGHTWEIGHT` | `relatedMatch` | `din276:337` |
| `swp:SWP-LIGHTWEIGHT` | `relatedMatch` | `din276:346` |
| `swp:SWP-LIGHTWEIGHT-CONCRETE-PANEL` | `closeMatch` | `din276:337` |
| `swp:SWP-LIGHTWEIGHT-CONCRETE-PANEL` | `closeMatch` | `din276:346` |
| `swp:SWP-LIGHTWEIGHT-CONCRETE-PANEL` | `relatedMatch` | `din276:331` |
| `swp:SWP-LIGHTWEIGHT-CONCRETE-PANEL` | `relatedMatch` | `din276:341` |
| `swp:SWP-MASONRY` | `closeMatch` | `din276:331` |
| `swp:SWP-MASONRY` | `closeMatch` | `din276:341` |
| `swp:SWP-ORTBETON` | `closeMatch` | `din276:331` |
| `swp:SWP-ORTBETON` | `closeMatch` | `din276:341` |
| `swp:SWP-PREFAB-CONC` | `closeMatch` | `din276:337` |
| `swp:SWP-PREFAB-CONC` | `closeMatch` | `din276:346` |
| `swp:SWP-PREFAB-CONC` | `relatedMatch` | `din276:331` |
| `swp:SWP-PREFAB-CONC` | `relatedMatch` | `din276:341` |
| `swp:SWP-RAMMED-EARTH` | `closeMatch` | `din276:331` |
| `swp:SWP-RAMMED-EARTH` | `closeMatch` | `din276:341` |
| `swp:SWP-STEEL` | `closeMatch` | `din276:331` |
| `swp:SWP-STEEL` | `closeMatch` | `din276:341` |
| `swp:SWP-STEEL` | `relatedMatch` | `din276:333` |
| `swp:SWP-STEEL` | `relatedMatch` | `din276:343` |
| `swp:SWP-SYSTEM-PARTITION` | `closeMatch` | `din276:346` |
| `swp:SWP-SYSTEM-PARTITION` | `relatedMatch` | `din276:342` |
| `swp:SWP-TIMBER` | `closeMatch` | `din276:331` |
| `swp:SWP-TIMBER` | `closeMatch` | `din276:341` |
| `swp:SWP-TIMBER-FRAME` | `closeMatch` | `din276:331` |
| `swp:SWP-TIMBER-FRAME` | `closeMatch` | `din276:341` |
| `swp:SWP-TIMBER-SOLID` | `closeMatch` | `din276:331` |
| `swp:SWP-TIMBER-SOLID` | `closeMatch` | `din276:341` |
