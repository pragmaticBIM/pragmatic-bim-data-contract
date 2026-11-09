# Site conditions to connection functional type mapping

Source: [`abstract-site-conditions-to-connection-functional-type.mapping.ttl`](sources/mapping-site-conditions-to-connection-functional-type.ttl)

External target labels are not shipped in this repository; only codes and IRIs are shown.

## Dataset

- **description (de):** Verknüpft Werkanschlüsse eines Grundstücks (SC-UTL-*) mit dem funktionellen Verbindungstyp des transportierten Mediums. skos:relatedMatch: SC-UTL klassifiziert den Anschluss des Grundstücks an ein Netz, ConnectionFunctionalType klassifiziert Verbindungen zwischen Räumen nach Medium. Das Medium ist dasselbe, der Geltungsbereich verschieden.
- **description (en):** Links utility connections of a site (SC-UTL-*) to the connection functional type of the medium they carry. Uses skos:relatedMatch: SC-UTL classifies the connection of the site to a network, ConnectionFunctionalType classifies connections between spaces by medium. The medium is the same; the scope differs.
- **title (de):** Mapping Standortbedingungen zu funktionellem Verbindungstyp
- **title (en):** Site conditions to connection functional type mapping

## Links

| Source | Relation | Targets |
| --- | --- | --- |
| `sc:SC-UTL-ELECTRICITY` | `relatedMatch` | `cft:electrical` |
| `sc:SC-UTL-GAS` | `relatedMatch` | `cft:special-media` |
| `sc:SC-UTL-STORMWATER` | `relatedMatch` | `cft:waste-water` |
| `sc:SC-UTL-TELECOM` | `relatedMatch` | `cft:data` |
| `sc:SC-UTL-THERMAL` | `relatedMatch` | `cft:cooling` |
| `sc:SC-UTL-THERMAL` | `relatedMatch` | `cft:heating` |
| `sc:SC-UTL-WASTEWATER` | `relatedMatch` | `cft:waste-water` |
| `sc:SC-UTL-WATER` | `relatedMatch` | `cft:fresh-water` |
