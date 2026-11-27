# Abstract MEP products to DIN 276 mapping

Source: [`abstract-mep-products-to-din276.mapping.ttl`](sources/mapping-mep-products-to-din276.ttl)

External target labels are not shipped in this repository; only codes and IRIs are shown.

## Dataset

- **description (de):** Ordnet abstrakte Gebaeudetechnikprodukte den Kostengruppen der DIN 276:2018 nur per Referenz zu (410 Sanitaer, 420 Waerme, 430 Luft, 440 Elektro, 450 Kommunikation/Sicherheit, 474 Feuerloesch, 480 Automation). Codes nur ueber Notation; DIN 276 wird vom DIN herausgegeben, es werden keine DIN-Bezeichnungen oder -Definitionen wiedergegeben. Lizenznehmende loesen die Codes mit ihrer eigenen Ausgabe auf. closeMatch ist die Leitgruppe; relatedMatch eine sekundaere oder benachbarte Gruppe. Disambiguierung: DIN 276 ist bewusst nicht eindeutig.
- **description (en):** Maps abstract MEP unit and terminal product concepts to DIN 276:2018 Kostengruppen by reference only (410 sanitary, 420 heat, 430 air, 440 electrical, 450 communications/security, 474 fire extinguishing, 480 automation). Codes are referenced by notation; DIN 276 is published by DIN and no DIN titles or definitions are reproduced. Licence holders resolve the codes against their own copy. closeMatch is the leading cost group; relatedMatch marks a secondary or adjacent group. Disambiguation: DIN 276 is deliberately not bijective.
- **title (de):** Mapping abstrakter Gebaeudetechnikprodukte nach DIN 276
- **title (en):** Abstract MEP products to DIN 276 mapping

## Links

| Source | Relation | Targets |
| --- | --- | --- |
| `mtp:MTP-COOL-CEILING-PANEL` | `closeMatch` | `din276:434` |
| `mtp:MTP-COOL-CEILING-PANEL` | `relatedMatch` | `din276:439` |
| `mtp:MTP-COOL-CHILLED-BEAM` | `closeMatch` | `din276:434` |
| `mtp:MTP-COOL-CHILLED-BEAM` | `relatedMatch` | `din276:439` |
| `mtp:MTP-COOL-CHILLED-CEILING` | `closeMatch` | `din276:434` |
| `mtp:MTP-COOL-CHILLED-CEILING` | `relatedMatch` | `din276:439` |
| `mtp:MTP-COOL-FAN-COIL` | `closeMatch` | `din276:434` |
| `mtp:MTP-COOL-FAN-COIL` | `relatedMatch` | `din276:423` |
| `mtp:MTP-DATA-DATA-OUTLET` | `closeMatch` | `din276:457` |
| `mtp:MTP-DATA-SENSOR-ACTUATOR` | `closeMatch` | `din276:480` |
| `mtp:MTP-DATA-SENSOR-ACTUATOR` | `relatedMatch` | `din276:457` |
| `mtp:MTP-DATA-WIFI-AP` | `closeMatch` | `din276:457` |
| `mtp:MTP-DATA-WIFI-AP` | `relatedMatch` | `din276:451` |
| `mtp:MTP-ELEC-LIGHT` | `closeMatch` | `din276:445` |
| `mtp:MTP-ELEC-LIGHT` | `relatedMatch` | `din276:444` |
| `mtp:MTP-ELEC-SOCKET` | `closeMatch` | `din276:444` |
| `mtp:MTP-ELEC-SWITCH` | `closeMatch` | `din276:444` |
| `mtp:MTP-FIRE-FIRE-DAMPER` | `closeMatch` | `din276:431` |
| `mtp:MTP-FIRE-FIRE-DAMPER` | `relatedMatch` | `din276:456` |
| `mtp:MTP-FIRE-FIRE-DAMPER-ACTUATOR` | `closeMatch` | `din276:431` |
| `mtp:MTP-FIRE-FIRE-DAMPER-ACTUATOR` | `closeMatch` | `din276:480` |
| `mtp:MTP-FIRE-SMOKE-DETECTOR` | `closeMatch` | `din276:456` |
| `mtp:MTP-FW-SHOWER` | `closeMatch` | `din276:412` |
| `mtp:MTP-FW-TAP` | `closeMatch` | `din276:412` |
| `mtp:MTP-FW-WC-FLUSH` | `closeMatch` | `din276:412` |
| `mtp:MTP-HEAT-FAN-COIL` | `closeMatch` | `din276:423` |
| `mtp:MTP-HEAT-FAN-COIL` | `relatedMatch` | `din276:434` |
| `mtp:MTP-HEAT-RADIATOR` | `closeMatch` | `din276:423` |
| `mtp:MTP-HEAT-UFH-MANIFOLD` | `closeMatch` | `din276:423` |
| `mtp:MTP-HEAT-UFH-MANIFOLD` | `relatedMatch` | `din276:422` |
| `mtp:MTP-SM-GAS-OUTLET` | `closeMatch` | `din276:413` |
| `mtp:MTP-SM-GAS-OUTLET` | `relatedMatch` | `din276:412` |
| `mtp:MTP-SM-HOSE-REEL` | `closeMatch` | `din276:474` |
| `mtp:MTP-SM-SPRINKLER-HEAD` | `closeMatch` | `din276:474` |
| `mtp:MTP-VENT-AIR-VALVE` | `closeMatch` | `din276:431` |
| `mtp:MTP-VENT-GRILLE` | `closeMatch` | `din276:431` |
| `mtp:MTP-WW-FLOOR-DRAIN` | `closeMatch` | `din276:411` |
| `mtp:MTP-WW-SINK-DRAIN` | `closeMatch` | `din276:411` |
| `mtp:MTP-WW-WC-OUTLET` | `closeMatch` | `din276:411` |
| `mtp:MTP-WW-WC-OUTLET` | `relatedMatch` | `din276:412` |
| `mup:MUP-COOL-CHILLER` | `closeMatch` | `din276:434` |
| `mup:MUP-COOL-FREE-COOLER` | `closeMatch` | `din276:434` |
| `mup:MUP-DATA-NETWORK-SWITCH` | `closeMatch` | `din276:457` |
| `mup:MUP-DATA-NETWORK-SWITCH` | `relatedMatch` | `din276:451` |
| `mup:MUP-DATA-PATCH-PANEL` | `closeMatch` | `din276:457` |
| `mup:MUP-DATA-PATCH-PANEL` | `relatedMatch` | `din276:451` |
| `mup:MUP-DATA-SERVER` | `closeMatch` | `din276:457` |
| `mup:MUP-DATA-SERVER` | `relatedMatch` | `din276:451` |
| `mup:MUP-ELEC-GENERATOR` | `closeMatch` | `din276:442` |
| `mup:MUP-ELEC-MAIN-DIST-BOARD` | `closeMatch` | `din276:443` |
| `mup:MUP-ELEC-MAIN-DIST-BOARD` | `relatedMatch` | `din276:444` |
| `mup:MUP-ELEC-SUB-DIST-BOARD` | `closeMatch` | `din276:444` |
| `mup:MUP-ELEC-SUB-DIST-BOARD` | `relatedMatch` | `din276:443` |
| `mup:MUP-ELEC-TRANSFORMER` | `closeMatch` | `din276:441` |
| `mup:MUP-ELEC-UPS` | `closeMatch` | `din276:442` |
| `mup:MUP-FW-PRESSURE-BOOSTER` | `closeMatch` | `din276:412` |
| `mup:MUP-FW-WATER-HEATER` | `closeMatch` | `din276:412` |
| `mup:MUP-FW-WATER-HEATER` | `relatedMatch` | `din276:421` |
| `mup:MUP-HEAT-BOILER` | `closeMatch` | `din276:421` |
| `mup:MUP-HEAT-DISTRICT-HEAT-SUBSTATION` | `closeMatch` | `din276:421` |
| `mup:MUP-HEAT-DISTRICT-HEAT-SUBSTATION` | `relatedMatch` | `din276:422` |
| `mup:MUP-HEAT-HEAT-PUMP` | `closeMatch` | `din276:421` |
| `mup:MUP-HEAT-HP-AIR` | `closeMatch` | `din276:421` |
| `mup:MUP-HEAT-HP-GROUND` | `closeMatch` | `din276:421` |
| `mup:MUP-HEAT-HP-WATER` | `closeMatch` | `din276:421` |
| `mup:MUP-SM-COMPRESSOR` | `closeMatch` | `din276:473` |
| `mup:MUP-SM-COMPRESSOR` | `relatedMatch` | `din276:413` |
| `mup:MUP-SM-FIRE-PUMP` | `closeMatch` | `din276:474` |
| `mup:MUP-SM-FIRE-PUMP` | `relatedMatch` | `din276:412` |
| `mup:MUP-SM-GAS-REGULATOR` | `closeMatch` | `din276:413` |
| `mup:MUP-SM-GAS-REGULATOR` | `relatedMatch` | `din276:412` |
| `mup:MUP-VENT-AHU` | `closeMatch` | `din276:431` |
| `mup:MUP-VENT-AHU` | `relatedMatch` | `din276:433` |
| `mup:MUP-VENT-FAN` | `closeMatch` | `din276:431` |
| `mup:MUP-WW-GREASE-SEPARATOR` | `closeMatch` | `din276:411` |
| `mup:MUP-WW-LIFTING-STATION` | `closeMatch` | `din276:411` |
