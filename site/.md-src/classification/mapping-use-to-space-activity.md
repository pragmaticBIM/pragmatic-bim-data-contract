# Abstract use to space activity mapping

Source: [`abstract-use-to-space-activity.mapping.ttl`](sources/mapping-use-to-space-activity.ttl)

External target labels are not shipped in this repository; only codes and IRIs are shown.

## Dataset

- **description (de):** Ordnet jede Nutzung der Raumaktivität zu, unter die ihr Bruttovolumen fällt. closeMatch ist die spezifischste Klasse, die die ganze Nutzung abdeckt. Nutzungen ohne passende Klasse haben keinen Eintrag: Versammlung und Kultur, Lager und Logistik, Sport sowie Rechenzentrum.
- **description (en):** Maps each use to the space activity class that its gross volume falls under. closeMatch is the most specific class that covers the whole use. Uses without a fitting class have no entry: assembly and culture, warehousing and logistics, sport, and data centre.
- **title (de):** Mapping abstrakter Nutzungen zu Raumaktivitäten
- **title (en):** Abstract use to space activity mapping

## Links

| Source | Relation | Targets |
| --- | --- | --- |
| `use:accommodation` | `closeMatch` | `abs:M-COM` |
| `use:building-services` | `closeMatch` | `abs:S-TEC` |
| `use:education` | `closeMatch` | `abs:M-LRN` |
| `use:food-service` | `closeMatch` | `abs:M-COM` |
| `use:healthcare` | `closeMatch` | `abs:M-HEL` |
| `use:laboratory` | `closeMatch` | `abs:M-WRK` |
| `use:office` | `closeMatch` | `abs:M-WRK-KNW` |
| `use:parking` | `closeMatch` | `abs:S-PRK` |
| `use:passenger-transport` | `closeMatch` | `abs:M-CIR` |
| `use:production` | `closeMatch` | `abs:M-WRK-PRD` |
| `use:residential` | `closeMatch` | `abs:M-RES` |
| `use:retail` | `closeMatch` | `abs:M-COM` |
| `use:storage` | `closeMatch` | `abs:S-STO` |
