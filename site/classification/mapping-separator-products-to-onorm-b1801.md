# Abstract separator products to ÖNORM B 1801 mapping

Source: [`abstract-separator-products-to-onorm-b1801.mapping.ttl`](sources/mapping-separator-products-to-onorm-b1801.ttl)

External target labels are not shipped in this repository; only codes and IRIs are shown.

## Dataset

- **description (de):** Ordnet abstrakte Trennelementprodukte den Codes der Leistungsgliederung Hochbau nach ÖNORM B 1801-1:2022 nur per Referenz zu (z. B. 2.H07, 4.H39). IRI-Lokalnamen mit Unterstrich fuer den Punkt (onorm1801:2_H07 = 2.H07). Codes nur ueber Notation; ÖNORM B 1801 wird von Austrian Standards herausgegeben, es werden keine Bezeichnungen oder Definitionen wiedergegeben. Lizenznehmende loesen die Codes mit ihrer eigenen Ausgabe auf. closeMatch ist die Leit-Leistungsgruppe; relatedMatch eine sekundaere oder benachbarte Position. Disambiguierung: Das Mapping ist bewusst nicht eindeutig.
- **description (en):** Maps abstract separator product concepts to ÖNORM B 1801-1:2022 Leistungsgliederung Hochbau codes by reference only (e.g. 2.H07, 4.H39). IRI local names use underscore for the dot (onorm1801:2_H07 = 2.H07). Codes are referenced by notation; ÖNORM B 1801 is published by Austrian Standards and no titles or definitions are reproduced. Licence holders resolve the codes against their own copy. closeMatch is the leading Leistungsgruppe; relatedMatch marks a secondary or adjacent line. Disambiguation: the mapping is deliberately not bijective.
- **title (de):** Mapping abstrakter Trennelementprodukte nach ÖNORM B 1801
- **title (en):** Abstract separator products to ÖNORM B 1801 mapping

## Links

| Source | Relation | Targets |
| --- | --- | --- |
| `ssp:SSP-CLT` | `closeMatch` | `onorm1801:2-H14` |
| `ssp:SSP-COMPOSITE-BEAM` | `closeMatch` | `onorm1801:2-H15` |
| `ssp:SSP-COMPOSITE-BEAM` | `relatedMatch` | `onorm1801:2-H07` |
| `ssp:SSP-COMPOSITE-DECK` | `closeMatch` | `onorm1801:2-H15` |
| `ssp:SSP-COMPOSITE-DECK` | `relatedMatch` | `onorm1801:2-H07` |
| `ssp:SSP-HBV` | `closeMatch` | `onorm1801:2-H14` |
| `ssp:SSP-HBV` | `relatedMatch` | `onorm1801:2-H07` |
| `ssp:SSP-HBV-INSITU` | `closeMatch` | `onorm1801:2-H14` |
| `ssp:SSP-HBV-INSITU` | `relatedMatch` | `onorm1801:2-H07` |
| `ssp:SSP-HBV-PRECAST` | `closeMatch` | `onorm1801:2-H14` |
| `ssp:SSP-HBV-PRECAST` | `relatedMatch` | `onorm1801:2-H07` |
| `ssp:SSP-HOLZ-LEHM` | `closeMatch` | `onorm1801:2-H14` |
| `ssp:SSP-INSITU` | `closeMatch` | `onorm1801:2-H07` |
| `ssp:SSP-LIGHTWEIGHT` | `closeMatch` | `onorm1801:4-H39` |
| `ssp:SSP-LIGHTWEIGHT` | `relatedMatch` | `onorm1801:2-H14` |
| `ssp:SSP-PREFAB-CONC` | `closeMatch` | `onorm1801:2-H07` |
| `ssp:SSP-STEEL-COMPOSITE` | `closeMatch` | `onorm1801:2-H15` |
| `ssp:SSP-STEEL-COMPOSITE` | `relatedMatch` | `onorm1801:2-H07` |
| `ssp:SSP-TIMBER` | `closeMatch` | `onorm1801:2-H14` |
| `ssp:SSP-TIMBER-CLAY` | `closeMatch` | `onorm1801:2-H14` |
| `ssp:SSP-TIMBER-CONCRETE` | `closeMatch` | `onorm1801:2-H14` |
| `ssp:SSP-TIMBER-CONCRETE` | `relatedMatch` | `onorm1801:2-H07` |
| `ssp:SSP-TIMBER-CONCRETE-INSITU` | `closeMatch` | `onorm1801:2-H14` |
| `ssp:SSP-TIMBER-CONCRETE-INSITU` | `relatedMatch` | `onorm1801:2-H07` |
| `ssp:SSP-TIMBER-CONCRETE-PRECAST` | `closeMatch` | `onorm1801:2-H14` |
| `ssp:SSP-TIMBER-CONCRETE-PRECAST` | `relatedMatch` | `onorm1801:2-H07` |
| `swp:SWP-BLT` | `closeMatch` | `onorm1801:2-H07` |
| `swp:SWP-BLT-PANEL` | `closeMatch` | `onorm1801:2-H07` |
| `swp:SWP-CURTAIN-WALL` | `closeMatch` | `onorm1801:2-H36` |
| `swp:SWP-CURTAIN-WALL` | `relatedMatch` | `onorm1801:4-H39` |
| `swp:SWP-CURTAIN-WALL-STICK` | `closeMatch` | `onorm1801:2-H36` |
| `swp:SWP-CURTAIN-WALL-STICK` | `relatedMatch` | `onorm1801:4-H39` |
| `swp:SWP-CURTAIN-WALL-UNITISED` | `closeMatch` | `onorm1801:2-H36` |
| `swp:SWP-CURTAIN-WALL-UNITISED` | `relatedMatch` | `onorm1801:4-H39` |
| `swp:SWP-DRYWALL` | `closeMatch` | `onorm1801:4-H39` |
| `swp:SWP-ELEMENT-WALL` | `closeMatch` | `onorm1801:4-H39` |
| `swp:SWP-INSITU-CONCRETE` | `closeMatch` | `onorm1801:2-H07` |
| `swp:SWP-LEICHTBAU` | `closeMatch` | `onorm1801:4-H39` |
| `swp:SWP-LEICHTBAU` | `relatedMatch` | `onorm1801:2-H14` |
| `swp:SWP-LIGHTWEIGHT` | `closeMatch` | `onorm1801:4-H39` |
| `swp:SWP-LIGHTWEIGHT` | `relatedMatch` | `onorm1801:2-H14` |
| `swp:SWP-LIGHTWEIGHT-CONCRETE-PANEL` | `closeMatch` | `onorm1801:2-H07` |
| `swp:SWP-MASONRY` | `closeMatch` | `onorm1801:2-H05` |
| `swp:SWP-ORTBETON` | `closeMatch` | `onorm1801:2-H07` |
| `swp:SWP-PREFAB-CONC` | `closeMatch` | `onorm1801:2-H07` |
| `swp:SWP-RAMMED-EARTH` | `closeMatch` | `onorm1801:2-H05` |
| `swp:SWP-RAMMED-EARTH` | `relatedMatch` | `onorm1801:2-H07` |
| `swp:SWP-STEEL` | `closeMatch` | `onorm1801:2-H15` |
| `swp:SWP-SYSTEM-PARTITION` | `closeMatch` | `onorm1801:4-H39` |
| `swp:SWP-TIMBER` | `closeMatch` | `onorm1801:2-H14` |
| `swp:SWP-TIMBER-FRAME` | `closeMatch` | `onorm1801:2-H14` |
| `swp:SWP-TIMBER-SOLID` | `closeMatch` | `onorm1801:2-H14` |
