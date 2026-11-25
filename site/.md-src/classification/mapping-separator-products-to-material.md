# Abstract separator products to material mapping

Source: [`abstract-separator-products-to-material.mapping.ttl`](sources/mapping-separator-products-to-material.ttl)

External target labels are not shipped in this repository; only codes and IRIs are shown.

## Dataset

- **description (de):** Ordnet abstrakte Wand- und Deckenplatten-Trennelementprodukte dominanten Materialklassen zu. skos:closeMatch fuer primaere Substanz; skos:relatedMatch bei Verbund oder Variabilitaet.
- **description (en):** Maps abstract wall and slab separator product concepts to dominant-substance material classes. Uses skos:closeMatch for primary substance; skos:relatedMatch where composite or variable.
- **title (de):** Mapping abstrakter Trennelementprodukte nach Material
- **title (en):** Abstract separator products to material mapping

## Links

| Source | Relation | Targets |
| --- | --- | --- |
| `ssp:SSP-CLT` | `closeMatch` | `mat:MAT-WOD` |
| `ssp:SSP-CLT` | `relatedMatch` | `mat:MAT-CMP` |
| `ssp:SSP-COMPOSITE-BEAM` | `closeMatch` | `mat:MAT-MET-STL` |
| `ssp:SSP-COMPOSITE-BEAM` | `relatedMatch` | `mat:MAT-CONC` |
| `ssp:SSP-COMPOSITE-DECK` | `closeMatch` | `mat:MAT-MET-STL` |
| `ssp:SSP-COMPOSITE-DECK` | `relatedMatch` | `mat:MAT-CONC` |
| `ssp:SSP-HBV` | `closeMatch` | `mat:MAT-CMP` |
| `ssp:SSP-HBV` | `relatedMatch` | `mat:MAT-CONC` |
| `ssp:SSP-HBV` | `relatedMatch` | `mat:MAT-WOD` |
| `ssp:SSP-HBV-CONC` | `closeMatch` | `mat:MAT-CONC` |
| `ssp:SSP-HBV-INSITU` | `closeMatch` | `mat:MAT-CMP` |
| `ssp:SSP-HBV-INSITU` | `relatedMatch` | `mat:MAT-CONC` |
| `ssp:SSP-HBV-INSITU` | `relatedMatch` | `mat:MAT-WOD` |
| `ssp:SSP-HBV-PRECAST` | `closeMatch` | `mat:MAT-CMP` |
| `ssp:SSP-HBV-PRECAST` | `relatedMatch` | `mat:MAT-CONC` |
| `ssp:SSP-HBV-PRECAST` | `relatedMatch` | `mat:MAT-WOD` |
| `ssp:SSP-HBV-WOD` | `closeMatch` | `mat:MAT-WOD` |
| `ssp:SSP-HOLZ-LEHM` | `closeMatch` | `mat:MAT-WOD` |
| `ssp:SSP-HOLZ-LEHM` | `relatedMatch` | `mat:MAT-CMP` |
| `ssp:SSP-HOLZ-LEHM` | `relatedMatch` | `mat:MAT-MSN` |
| `ssp:SSP-HOLZ-LEHM-MSN` | `closeMatch` | `mat:MAT-MSN` |
| `ssp:SSP-HOLZ-LEHM-WOD` | `closeMatch` | `mat:MAT-WOD` |
| `ssp:SSP-INSITU` | `closeMatch` | `mat:MAT-CONC` |
| `ssp:SSP-LIGHTWEIGHT` | `closeMatch` | `mat:MAT-CMP` |
| `ssp:SSP-LIGHTWEIGHT` | `relatedMatch` | `mat:MAT-INS` |
| `ssp:SSP-OTH` | `closeMatch` | `mat:MAT-OTH` |
| `ssp:SSP-PREFAB-CONC` | `closeMatch` | `mat:MAT-CONC` |
| `ssp:SSP-PREFAB-CONC` | `relatedMatch` | `mat:MAT-CMP` |
| `ssp:SSP-STEEL-COMPOSITE` | `closeMatch` | `mat:MAT-MET-STL` |
| `ssp:SSP-STEEL-COMPOSITE` | `relatedMatch` | `mat:MAT-CONC` |
| `ssp:SSP-STEEL-COMPOSITE-CONC` | `closeMatch` | `mat:MAT-CONC` |
| `ssp:SSP-STEEL-COMPOSITE-STL` | `closeMatch` | `mat:MAT-MET-STL` |
| `ssp:SSP-TIMBER` | `closeMatch` | `mat:MAT-WOD` |
| `ssp:SSP-TIMBER` | `relatedMatch` | `mat:MAT-CMP` |
| `swp:SWP-BLT` | `closeMatch` | `mat:MAT-CONC` |
| `swp:SWP-BLT` | `relatedMatch` | `mat:MAT-CMP` |
| `swp:SWP-BLT-PANEL` | `closeMatch` | `mat:MAT-CONC` |
| `swp:SWP-BLT-PANEL` | `relatedMatch` | `mat:MAT-CMP` |
| `swp:SWP-CURTAIN-WALL` | `closeMatch` | `mat:MAT-MET-ALU` |
| `swp:SWP-CURTAIN-WALL` | `relatedMatch` | `mat:MAT-GLS` |
| `swp:SWP-CURTAIN-WALL` | `relatedMatch` | `mat:MAT-PLA` |
| `swp:SWP-CURTAIN-WALL-STICK` | `closeMatch` | `mat:MAT-MET-ALU` |
| `swp:SWP-CURTAIN-WALL-STICK` | `relatedMatch` | `mat:MAT-GLS` |
| `swp:SWP-CURTAIN-WALL-STICK` | `relatedMatch` | `mat:MAT-PLA` |
| `swp:SWP-CURTAIN-WALL-UNITISED` | `closeMatch` | `mat:MAT-MET-ALU` |
| `swp:SWP-CURTAIN-WALL-UNITISED` | `relatedMatch` | `mat:MAT-GLS` |
| `swp:SWP-CURTAIN-WALL-UNITISED` | `relatedMatch` | `mat:MAT-PLA` |
| `swp:SWP-DRYWALL` | `closeMatch` | `mat:MAT-GYP` |
| `swp:SWP-DRYWALL` | `relatedMatch` | `mat:MAT-CMP` |
| `swp:SWP-DRYWALL` | `relatedMatch` | `mat:MAT-MET-STL` |
| `swp:SWP-ELEMENT-WALL` | `closeMatch` | `mat:MAT-GYP` |
| `swp:SWP-ELEMENT-WALL` | `relatedMatch` | `mat:MAT-CMP` |
| `swp:SWP-ELEMENT-WALL` | `relatedMatch` | `mat:MAT-MET-STL` |
| `swp:SWP-LEICHTBAU` | `closeMatch` | `mat:MAT-CMP` |
| `swp:SWP-LEICHTBAU` | `relatedMatch` | `mat:MAT-GYP` |
| `swp:SWP-LEICHTBAU` | `relatedMatch` | `mat:MAT-PLA` |
| `swp:SWP-MASONRY` | `closeMatch` | `mat:MAT-MSN` |
| `swp:SWP-MASONRY` | `relatedMatch` | `mat:MAT-CONC` |
| `swp:SWP-ORTBETON` | `closeMatch` | `mat:MAT-CONC` |
| `swp:SWP-OTH` | `closeMatch` | `mat:MAT-OTH` |
| `swp:SWP-PREFAB-CONC` | `closeMatch` | `mat:MAT-CONC` |
| `swp:SWP-PREFAB-CONC` | `relatedMatch` | `mat:MAT-CMP` |
| `swp:SWP-RAMMED-EARTH` | `closeMatch` | `mat:MAT-MSN` |
| `swp:SWP-RAMMED-EARTH` | `relatedMatch` | `mat:MAT-CMP` |
| `swp:SWP-STEEL` | `closeMatch` | `mat:MAT-MET-STL` |
| `swp:SWP-SYSTEM-PARTITION` | `closeMatch` | `mat:MAT-GYP` |
| `swp:SWP-SYSTEM-PARTITION` | `relatedMatch` | `mat:MAT-CMP` |
| `swp:SWP-SYSTEM-PARTITION` | `relatedMatch` | `mat:MAT-MET-STL` |
| `swp:SWP-TIMBER` | `closeMatch` | `mat:MAT-WOD` |
| `swp:SWP-TIMBER` | `relatedMatch` | `mat:MAT-CMP` |
| `swp:SWP-TIMBER-FRAME` | `closeMatch` | `mat:MAT-WOD` |
| `swp:SWP-TIMBER-FRAME` | `relatedMatch` | `mat:MAT-CMP` |
| `swp:SWP-TIMBER-SOLID` | `closeMatch` | `mat:MAT-WOD` |
| `swp:SWP-TIMBER-SOLID` | `relatedMatch` | `mat:MAT-CMP` |
