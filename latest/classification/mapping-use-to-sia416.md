# Abstract use to SIA 416 mapping

Source: [`abstract-use-to-sia416.mapping.ttl`](sources/mapping-use-to-sia416.ttl)

External target labels are not shipped in this repository; only codes and IRIs are shown.

## Dataset

- **description (de):** Ordnet jede Nutzung der SIA-416-Flächenart zu, die ihr Bruttovolumen prägt. Nutzungen, für die gebaut wird, ergeben Hauptnutzfläche (HNF); Keller, Parkierung und Technik behalten ihre eigene Flächenart. Einzelne Räume innerhalb eines Volumens werden über das Mapping der Raumaktivität eingeteilt.
- **description (en):** Maps each use to the SIA 416 area class that dominates its gross volume. Uses that are the purpose of the building map to main usable area (HNF); storage, parking and building services keep their own class. Individual spaces inside a volume are classified through the space activity mapping.
- **title (de):** Mapping abstrakter Nutzungen zu SIA 416
- **title (en):** Abstract use to SIA 416 mapping

## Links

| Source | Relation | Targets |
| --- | --- | --- |
| `use:accommodation` | `closeMatch` | `sia:HNF` |
| `use:assembly` | `closeMatch` | `sia:HNF` |
| `use:building-services` | `closeMatch` | `sia:FF` |
| `use:data-centre` | `closeMatch` | `sia:HNF` |
| `use:education` | `closeMatch` | `sia:HNF` |
| `use:food-service` | `closeMatch` | `sia:HNF` |
| `use:healthcare` | `closeMatch` | `sia:HNF` |
| `use:laboratory` | `closeMatch` | `sia:HNF` |
| `use:logistics` | `closeMatch` | `sia:HNF` |
| `use:office` | `closeMatch` | `sia:HNF` |
| `use:parking` | `closeMatch` | `sia:NNF` |
| `use:passenger-transport` | `closeMatch` | `sia:HNF` |
| `use:production` | `closeMatch` | `sia:HNF` |
| `use:residential` | `closeMatch` | `sia:HNF` |
| `use:retail` | `closeMatch` | `sia:HNF` |
| `use:sport` | `closeMatch` | `sia:HNF` |
| `use:storage` | `closeMatch` | `sia:NNF` |
