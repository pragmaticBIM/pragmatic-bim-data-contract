# Abstract covering products to DIN 276 mapping

Source: [`abstract-covering-products-to-din276.mapping.ttl`](sources/mapping-covering-products-to-din276.ttl)

External target labels are not shipped in this repository; only codes and IRIs are shown.

## Dataset

- **description (de):** Ordnet abstrakte Bekleidungsprodukte den Kostengruppen der DIN 276:2018 nur per Referenz zu: Bodenbelaege 353, Innenwandbekleidungen 345, Deckenbekleidungen 354, Fassadenbekleidungen 335. Codes nur ueber Notation; DIN 276 wird vom DIN herausgegeben, es werden keine DIN-Bezeichnungen oder -Definitionen wiedergegeben. Lizenznehmende loesen die Codes mit ihrer eigenen Ausgabe auf. closeMatch ist die Leitgruppe; relatedMatch eine sekundaere oder benachbarte Gruppe. Disambiguierung: DIN 276 ist bewusst nicht eindeutig.
- **description (en):** Maps abstract covering product concepts to DIN 276:2018 Kostengruppen by reference only: floor finishes 353, interior wall finishes 345, ceiling finishes 354, facade cladding 335. Codes are referenced by notation; DIN 276 is published by DIN and no DIN titles or definitions are reproduced. Licence holders resolve the codes against their own copy. closeMatch is the leading cost group; relatedMatch marks a secondary or adjacent group. Disambiguation: DIN 276 is deliberately not bijective.
- **title (de):** Mapping abstrakter Bekleidungsprodukte nach DIN 276
- **title (en):** Abstract covering products to DIN 276 mapping

## Links

| Source | Relation | Targets |
| --- | --- | --- |
| `ccp:CCP-GYPSUM-BOARD` | `closeMatch` | `din276:354` |
| `ccp:CCP-GYPSUM-DIRECT` | `closeMatch` | `din276:354` |
| `ccp:CCP-GYPSUM-SUSPENDED` | `closeMatch` | `din276:354` |
| `ccp:CCP-METAL-GRID` | `closeMatch` | `din276:354` |
| `ccp:CCP-METAL-PANEL` | `closeMatch` | `din276:354` |
| `ccp:CCP-METAL-SHEET` | `closeMatch` | `din276:354` |
| `ccp:CCP-MINERAL-FIBRE` | `closeMatch` | `din276:354` |
| `ccp:CCP-STRETCH-MEMBRANE` | `closeMatch` | `din276:354` |
| `ccp:CCP-SYNTHETIC` | `closeMatch` | `din276:354` |
| `ccp:CCP-SYNTHETIC-PANEL` | `closeMatch` | `din276:354` |
| `ccp:CCP-WOOD` | `closeMatch` | `din276:354` |
| `fcp:FCP-ACCESS-FLOOR` | `closeMatch` | `din276:353` |
| `fcp:FCP-ACCESS-FLOOR` | `relatedMatch` | `din276:439` |
| `fcp:FCP-ARTIFICIAL-STONE` | `closeMatch` | `din276:353` |
| `fcp:FCP-CARPET` | `closeMatch` | `din276:353` |
| `fcp:FCP-CAVITY-FLOOR` | `closeMatch` | `din276:353` |
| `fcp:FCP-CAVITY-FLOOR` | `relatedMatch` | `din276:439` |
| `fcp:FCP-CERAMIC-TILE` | `closeMatch` | `din276:353` |
| `fcp:FCP-LAMINATE` | `closeMatch` | `din276:353` |
| `fcp:FCP-LINOLIUM` | `closeMatch` | `din276:353` |
| `fcp:FCP-LVT` | `closeMatch` | `din276:353` |
| `fcp:FCP-NATURAL-STONE` | `closeMatch` | `din276:353` |
| `fcp:FCP-PARQUET` | `closeMatch` | `din276:353` |
| `fcp:FCP-RAISED-FLOOR` | `closeMatch` | `din276:353` |
| `fcp:FCP-RAISED-FLOOR` | `relatedMatch` | `din276:439` |
| `fcp:FCP-SCREED-BONDED` | `closeMatch` | `din276:353` |
| `fcp:FCP-SCREED-FLOATING` | `closeMatch` | `din276:353` |
| `fcp:FCP-SCREED-HEATED` | `closeMatch` | `din276:353` |
| `fcp:FCP-SCREED-HEATED` | `relatedMatch` | `din276:423` |
| `fcp:FCP-SEAMLESS-RESIN` | `closeMatch` | `din276:353` |
| `fcp:FCP-SUBFLOOR` | `closeMatch` | `din276:353` |
| `facp:FaCP-BIPV-INTEGRATED` | `closeMatch` | `din276:335` |
| `facp:FaCP-BIPV-INTEGRATED` | `closeMatch` | `din276:442` |
| `facp:FaCP-BRICK-SLIP` | `closeMatch` | `din276:335` |
| `facp:FaCP-BRICK-SLIP-BONDED` | `closeMatch` | `din276:335` |
| `facp:FaCP-BRICK-SLIP-VENTILATED` | `closeMatch` | `din276:335` |
| `facp:FaCP-CERAMIC-VENTILATED` | `closeMatch` | `din276:335` |
| `facp:FaCP-EXTERIOR-PAINT-COATING` | `closeMatch` | `din276:335` |
| `facp:FaCP-EXTERIOR-PAINT-COATING` | `relatedMatch` | `din276:336` |
| `facp:FaCP-FIBER-CEMENT-BOARD` | `closeMatch` | `din276:335` |
| `facp:FaCP-HPL-PANEL` | `closeMatch` | `din276:335` |
| `facp:FaCP-METAL-COMPOSITE-PANEL` | `closeMatch` | `din276:335` |
| `facp:FaCP-METAL-SHEET-STANDING-SEAM` | `closeMatch` | `din276:335` |
| `facp:FaCP-NATURAL-STONE-VENTILATED` | `closeMatch` | `din276:335` |
| `facp:FaCP-PREFAB-MODULAR-METAL` | `closeMatch` | `din276:337` |
| `facp:FaCP-PREFAB-MODULAR-METAL` | `relatedMatch` | `din276:335` |
| `facp:FaCP-PREFAB-MODULAR-TIMBER` | `closeMatch` | `din276:337` |
| `facp:FaCP-PREFAB-MODULAR-TIMBER` | `relatedMatch` | `din276:335` |
| `facp:FaCP-RENDER-ETICS` | `closeMatch` | `din276:335` |
| `facp:FaCP-RENDER-ETICS-WDVS` | `closeMatch` | `din276:335` |
| `facp:FaCP-RETROFIT-OVERCLADDING` | `closeMatch` | `din276:335` |
| `facp:FaCP-SYNTHETIC-VENTILATED` | `closeMatch` | `din276:335` |
| `facp:FaCP-TIMBER-VENTILATED` | `closeMatch` | `din276:335` |
| `wcp:WCP-ARTIFICIAL-STONE` | `closeMatch` | `din276:345` |
| `wcp:WCP-ARTIFICIAL-STONE-ANCHORED` | `closeMatch` | `din276:345` |
| `wcp:WCP-ARTIFICIAL-STONE-BONDED` | `closeMatch` | `din276:345` |
| `wcp:WCP-CERAMIC-TILE` | `closeMatch` | `din276:345` |
| `wcp:WCP-FABRIC-STRETCHED` | `closeMatch` | `din276:345` |
| `wcp:WCP-NATURAL-STONE` | `closeMatch` | `din276:345` |
| `wcp:WCP-NATURAL-STONE-ANCHORED` | `closeMatch` | `din276:345` |
| `wcp:WCP-NATURAL-STONE-BONDED` | `closeMatch` | `din276:345` |
| `wcp:WCP-PAINT` | `closeMatch` | `din276:345` |
| `wcp:WCP-PAINT` | `relatedMatch` | `din276:336` |
| `wcp:WCP-SEAMLESS-COATING` | `closeMatch` | `din276:345` |
| `wcp:WCP-SYNTHETIC-PANEL` | `closeMatch` | `din276:345` |
| `wcp:WCP-TEXTILE` | `closeMatch` | `din276:345` |
| `wcp:WCP-TEXTILE-BONDED` | `closeMatch` | `din276:345` |
| `wcp:WCP-WALLPAPER` | `closeMatch` | `din276:345` |
| `wcp:WCP-WOOD-PANEL` | `closeMatch` | `din276:345` |
