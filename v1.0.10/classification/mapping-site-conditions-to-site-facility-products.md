# Site conditions to site facility products mapping

Source: [`abstract-site-conditions-to-site-facility-products.mapping.ttl`](sources/mapping-site-conditions-to-site-facility-products.ttl)

External target labels are not shipped in this repository; only codes and IRIs are shown.

## Dataset

- **description (de):** Verknüpft Standortbedingungen des Bauablaufs (SC-CON-*) mit den Baustelleneinrichtungsprodukten (SFP), die darin typischerweise platziert werden. skos:relatedMatch: eine Baustellenzufahrt oder Installationsfläche ist eine in der Bestellung festgelegte Planungszone; die Einrichtungen darin werden separat klassifiziert, sobald die Baustelleneinrichtung geplant ist. Nicht bijektiv.
- **description (en):** Links construction site conditions (SC-CON-*) to the site facility products (SFP) typically placed in them. Uses skos:relatedMatch: a construction access or logistics area is a planning zone fixed in the brief; the facilities in it are classified separately once the site set-up is planned. Not bijective.
- **title (de):** Mapping Standortbedingungen zu Baustelleneinrichtungsprodukten
- **title (en):** Site conditions to site facility products mapping

## Links

| Source | Relation | Targets |
| --- | --- | --- |
| `sc:SC-CON-ACCESS` | `relatedMatch` | `sfp:SFP-GATE` |
| `sc:SC-CON-ACCESS` | `relatedMatch` | `sfp:SFP-HAUL-ROAD` |
| `sc:SC-CON-ACCESS` | `relatedMatch` | `sfp:SFP-RAMP` |
| `sc:SC-CON-ACCESS` | `relatedMatch` | `sfp:SFP-TURNING` |
| `sc:SC-CON-ACCESS` | `relatedMatch` | `sfp:SFP-WHEEL-WASH` |
| `sc:SC-CON-LOGISTICS` | `relatedMatch` | `sfp:SFP-BREAK-ROOM` |
| `sc:SC-CON-LOGISTICS` | `relatedMatch` | `sfp:SFP-BUFFER` |
| `sc:SC-CON-LOGISTICS` | `relatedMatch` | `sfp:SFP-CONTAINER` |
| `sc:SC-CON-LOGISTICS` | `relatedMatch` | `sfp:SFP-CRANE-PAD` |
| `sc:SC-CON-LOGISTICS` | `relatedMatch` | `sfp:SFP-OFFICE` |
| `sc:SC-CON-LOGISTICS` | `relatedMatch` | `sfp:SFP-PARKING` |
| `sc:SC-CON-LOGISTICS` | `relatedMatch` | `sfp:SFP-SANITARY` |
| `sc:SC-CON-LOGISTICS` | `relatedMatch` | `sfp:SFP-SKIP-BAY` |
| `sc:SC-CON-LOGISTICS` | `relatedMatch` | `sfp:SFP-STORAGE` |
| `sc:SC-CON-LOGISTICS` | `relatedMatch` | `sfp:SFP-STORE` |
| `sc:SC-CON-LOGISTICS` | `relatedMatch` | `sfp:SFP-TRANSFER` |
