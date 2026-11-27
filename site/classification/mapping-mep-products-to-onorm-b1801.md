# Abstract MEP products to ÖNORM B 1801 mapping

Source: [`abstract-mep-products-to-onorm-b1801.mapping.ttl`](sources/mapping-mep-products-to-onorm-b1801.ttl)

External target labels are not shipped in this repository; only codes and IRIs are shown.

## Dataset

- **description (de):** Ordnet abstrakte Gebaeudetechnikprodukte den Codes der Leistungsgliederung Hochbau nach ÖNORM B 1801-1:2022 nur per Referenz zu unter Kostenbereich 3 Bauwerk-Technik (z. B. 3.H40 Sanitaer, 3.H41 Waerme, 3.H43 Lueftung, 3.H51 Elektro). IRI-Lokalnamen mit Unterstrich fuer den Punkt. Codes nur ueber Notation; ÖNORM B 1801 wird von Austrian Standards herausgegeben, es werden keine Bezeichnungen oder Definitionen wiedergegeben. Lizenznehmende loesen die Codes mit ihrer eigenen Ausgabe auf. closeMatch ist die Leit-Leistungsgruppe; relatedMatch eine sekundaere oder benachbarte Position. Disambiguierung: Das Mapping ist bewusst nicht eindeutig.
- **description (en):** Maps abstract MEP unit and terminal product concepts to ÖNORM B 1801-1:2022 Leistungsgliederung Hochbau codes by reference only under Kostenbereich 3 Bauwerk-Technik (e.g. 3.H40 sanitary, 3.H41 heat, 3.H43 ventilation, 3.H51 electrical). IRI local names use underscore for the dot. Codes are referenced by notation; ÖNORM B 1801 is published by Austrian Standards and no titles or definitions are reproduced. Licence holders resolve the codes against their own copy. closeMatch is the leading Leistungsgruppe; relatedMatch marks a secondary or adjacent line. Disambiguation: the mapping is deliberately not bijective.
- **title (de):** Mapping abstrakter Gebaeudetechnikprodukte nach ÖNORM B 1801
- **title (en):** Abstract MEP products to ÖNORM B 1801 mapping

## Links

| Source | Relation | Targets |
| --- | --- | --- |
| `mtp:MTP-COOL-CEILING-PANEL` | `closeMatch` | `onorm1801:3-H44` |
| `mtp:MTP-COOL-CEILING-PANEL` | `relatedMatch` | `onorm1801:4-H39` |
| `mtp:MTP-COOL-CHILLED-BEAM` | `closeMatch` | `onorm1801:3-H44` |
| `mtp:MTP-COOL-CHILLED-BEAM` | `relatedMatch` | `onorm1801:4-H39` |
| `mtp:MTP-COOL-CHILLED-CEILING` | `closeMatch` | `onorm1801:3-H44` |
| `mtp:MTP-COOL-CHILLED-CEILING` | `relatedMatch` | `onorm1801:4-H39` |
| `mtp:MTP-COOL-FAN-COIL` | `closeMatch` | `onorm1801:3-H44` |
| `mtp:MTP-COOL-FAN-COIL` | `relatedMatch` | `onorm1801:3-H41` |
| `mtp:MTP-DATA-DATA-OUTLET` | `closeMatch` | `onorm1801:3-H52` |
| `mtp:MTP-DATA-SENSOR-ACTUATOR` | `closeMatch` | `onorm1801:3-H52` |
| `mtp:MTP-DATA-SENSOR-ACTUATOR` | `relatedMatch` | `onorm1801:3-H48` |
| `mtp:MTP-DATA-WIFI-AP` | `closeMatch` | `onorm1801:3-H52` |
| `mtp:MTP-ELEC-LIGHT` | `closeMatch` | `onorm1801:3-H51` |
| `mtp:MTP-ELEC-SOCKET` | `closeMatch` | `onorm1801:3-H51` |
| `mtp:MTP-ELEC-SWITCH` | `closeMatch` | `onorm1801:3-H51` |
| `mtp:MTP-FIRE-FIRE-DAMPER` | `closeMatch` | `onorm1801:3-H43` |
| `mtp:MTP-FIRE-FIRE-DAMPER` | `relatedMatch` | `onorm1801:3-H45` |
| `mtp:MTP-FIRE-FIRE-DAMPER-ACTUATOR` | `closeMatch` | `onorm1801:3-H43` |
| `mtp:MTP-FIRE-FIRE-DAMPER-ACTUATOR` | `relatedMatch` | `onorm1801:3-H52` |
| `mtp:MTP-FIRE-SMOKE-DETECTOR` | `closeMatch` | `onorm1801:3-H52` |
| `mtp:MTP-FIRE-SMOKE-DETECTOR` | `relatedMatch` | `onorm1801:3-H45` |
| `mtp:MTP-FW-SHOWER` | `closeMatch` | `onorm1801:3-H40` |
| `mtp:MTP-FW-TAP` | `closeMatch` | `onorm1801:3-H40` |
| `mtp:MTP-FW-WC-FLUSH` | `closeMatch` | `onorm1801:3-H40` |
| `mtp:MTP-HEAT-FAN-COIL` | `closeMatch` | `onorm1801:3-H41` |
| `mtp:MTP-HEAT-FAN-COIL` | `relatedMatch` | `onorm1801:3-H44` |
| `mtp:MTP-HEAT-RADIATOR` | `closeMatch` | `onorm1801:3-H41` |
| `mtp:MTP-HEAT-UFH-MANIFOLD` | `closeMatch` | `onorm1801:3-H41` |
| `mtp:MTP-SM-GAS-OUTLET` | `closeMatch` | `onorm1801:3-H40` |
| `mtp:MTP-SM-HOSE-REEL` | `closeMatch` | `onorm1801:3-H45` |
| `mtp:MTP-SM-SPRINKLER-HEAD` | `closeMatch` | `onorm1801:3-H45` |
| `mtp:MTP-VENT-AIR-VALVE` | `closeMatch` | `onorm1801:3-H43` |
| `mtp:MTP-VENT-GRILLE` | `closeMatch` | `onorm1801:3-H43` |
| `mtp:MTP-WW-FLOOR-DRAIN` | `closeMatch` | `onorm1801:3-H40` |
| `mtp:MTP-WW-SINK-DRAIN` | `closeMatch` | `onorm1801:3-H40` |
| `mtp:MTP-WW-WC-OUTLET` | `closeMatch` | `onorm1801:3-H40` |
| `mup:MUP-COOL-CHILLER` | `closeMatch` | `onorm1801:3-H44` |
| `mup:MUP-COOL-CHILLER` | `relatedMatch` | `onorm1801:3-H43` |
| `mup:MUP-COOL-FREE-COOLER` | `closeMatch` | `onorm1801:3-H44` |
| `mup:MUP-DATA-NETWORK-SWITCH` | `closeMatch` | `onorm1801:3-H52` |
| `mup:MUP-DATA-NETWORK-SWITCH` | `relatedMatch` | `onorm1801:3-H51` |
| `mup:MUP-DATA-PATCH-PANEL` | `closeMatch` | `onorm1801:3-H52` |
| `mup:MUP-DATA-PATCH-PANEL` | `relatedMatch` | `onorm1801:3-H51` |
| `mup:MUP-DATA-SERVER` | `closeMatch` | `onorm1801:3-H52` |
| `mup:MUP-DATA-SERVER` | `relatedMatch` | `onorm1801:3-H51` |
| `mup:MUP-ELEC-GENERATOR` | `closeMatch` | `onorm1801:3-H51` |
| `mup:MUP-ELEC-MAIN-DIST-BOARD` | `closeMatch` | `onorm1801:3-H51` |
| `mup:MUP-ELEC-SUB-DIST-BOARD` | `closeMatch` | `onorm1801:3-H51` |
| `mup:MUP-ELEC-TRANSFORMER` | `closeMatch` | `onorm1801:3-H51` |
| `mup:MUP-ELEC-UPS` | `closeMatch` | `onorm1801:3-H51` |
| `mup:MUP-FW-PRESSURE-BOOSTER` | `closeMatch` | `onorm1801:3-H40` |
| `mup:MUP-FW-WATER-HEATER` | `closeMatch` | `onorm1801:3-H40` |
| `mup:MUP-FW-WATER-HEATER` | `relatedMatch` | `onorm1801:3-H41` |
| `mup:MUP-HEAT-BOILER` | `closeMatch` | `onorm1801:3-H41` |
| `mup:MUP-HEAT-DISTRICT-HEAT-SUBSTATION` | `closeMatch` | `onorm1801:3-H41` |
| `mup:MUP-HEAT-HEAT-PUMP` | `closeMatch` | `onorm1801:3-H41` |
| `mup:MUP-HEAT-HP-AIR` | `closeMatch` | `onorm1801:3-H41` |
| `mup:MUP-HEAT-HP-GROUND` | `closeMatch` | `onorm1801:3-H41` |
| `mup:MUP-HEAT-HP-WATER` | `closeMatch` | `onorm1801:3-H41` |
| `mup:MUP-SM-COMPRESSOR` | `closeMatch` | `onorm1801:3-H40` |
| `mup:MUP-SM-COMPRESSOR` | `relatedMatch` | `onorm1801:3-H41` |
| `mup:MUP-SM-FIRE-PUMP` | `closeMatch` | `onorm1801:3-H45` |
| `mup:MUP-SM-FIRE-PUMP` | `relatedMatch` | `onorm1801:3-H40` |
| `mup:MUP-SM-GAS-REGULATOR` | `closeMatch` | `onorm1801:3-H40` |
| `mup:MUP-VENT-AHU` | `closeMatch` | `onorm1801:3-H43` |
| `mup:MUP-VENT-AHU` | `relatedMatch` | `onorm1801:3-H44` |
| `mup:MUP-VENT-FAN` | `closeMatch` | `onorm1801:3-H43` |
| `mup:MUP-WW-GREASE-SEPARATOR` | `closeMatch` | `onorm1801:3-H40` |
| `mup:MUP-WW-LIFTING-STATION` | `closeMatch` | `onorm1801:3-H40` |
