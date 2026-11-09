# Abstract use to SIA 380/1 building category mapping

Source: [`abstract-use-to-sia380-1.mapping.ttl`](sources/mapping-use-to-sia380-1.ttl)

External target labels are not shipped in this repository; only codes and IRIs are shown.

## Dataset

- **description (de):** Ordnet jede Nutzung den SIA-380/1-Gebäudekategorien I bis XII für die Berechnung des Heizwärmebedarfs zu. Wohnen ergibt I (MFH) und II (EFH); Sport ergibt XI (Sportbauten) und XII (Hallenbäder). Beherbergung, Labor und Forschung, Rechenzentrum, Personenverkehr und die unterstützenden Nutzungen haben keinen Eintrag; das Projekt legt ihre Kategorie fest.
- **description (en):** Maps each use to the SIA 380/1 building categories I to XII used for the energy demand calculation. Housing maps to both I (multi-family) and II (single-family); sport maps to XI (sports buildings) and XII (indoor pools). Accommodation, laboratory and research, data centre, passenger transport and the support uses have no entry; the project assigns their category.
- **title (de):** Mapping abstrakter Nutzungen zu SIA-380/1-Gebäudekategorien
- **title (en):** Abstract use to SIA 380/1 building category mapping

## Links

| Source | Relation | Targets |
| --- | --- | --- |
| `use:assembly` | `closeMatch` | `sia380:VII` |
| `use:education` | `closeMatch` | `sia380:IV` |
| `use:food-service` | `closeMatch` | `sia380:VI` |
| `use:healthcare` | `closeMatch` | `sia380:VIII` |
| `use:logistics` | `closeMatch` | `sia380:X` |
| `use:office` | `closeMatch` | `sia380:III` |
| `use:production` | `closeMatch` | `sia380:IX` |
| `use:residential` | `closeMatch` | `sia380:I` |
| `use:residential` | `closeMatch` | `sia380:II` |
| `use:retail` | `closeMatch` | `sia380:V` |
| `use:sport` | `closeMatch` | `sia380:XI` |
| `use:sport` | `closeMatch` | `sia380:XII` |
