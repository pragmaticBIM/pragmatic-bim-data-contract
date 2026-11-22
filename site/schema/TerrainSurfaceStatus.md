---
search:
  boost: 2.0
---


# Enum: TerrainSurfaceStatus 




_Whether a terrain surface describes the existing or the projected site._



<div data-search-exclude markdown="1">

URI: [pbs:TerrainSurfaceStatus](https://schema.pragmaticbim.ch/TerrainSurfaceStatus)

**Enum URI:** [pbs:TerrainSurfaceStatus](https://schema.pragmaticbim.ch/TerrainSurfaceStatus)


## Permissible Values
| Value | Meaning | Description | Additional Info |
| --- | --- | --- | --- |
| existing | pbs:terrain_surface_status_existing | Existing (as-built or survey) terrain surface. | Title: Existing<br>|
| projected | pbs:terrain_surface_status_projected | Projected (planned or new) terrain surface. | Title: Projected<br>|




## Slots

| Name | Description |
| ---  | --- |
| [terrain_surface_status](terrain_surface_status.md) | Whether the terrain surface represents the existing or the projected site. |










## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch






## LinkML Source

<details>
```yaml
name: TerrainSurfaceStatus
description: Whether a terrain surface describes the existing or the projected site.
from_schema: https://schema.pragmaticbim.ch
rank: 1000
enum_uri: pbs:TerrainSurfaceStatus
permissible_values:
  existing:
    text: existing
    description: Existing (as-built or survey) terrain surface.
    meaning: pbs:terrain_surface_status_existing
    alt_descriptions:
      de:
        source: de
        description: Bestand
    title: Existing
  projected:
    text: projected
    description: Projected (planned or new) terrain surface.
    meaning: pbs:terrain_surface_status_projected
    alt_descriptions:
      de:
        source: de
        description: Neu
    title: Projected

```
</details>

</div>