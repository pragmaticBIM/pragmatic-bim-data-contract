---
search:
  boost: 2.0
---


# Enum: GroundReferenceSource 




_Source used to resolve LevelContext above_ground and is_ground_floor flags._



<div data-search-exclude markdown="1">

URI: [pbs:GroundReferenceSource](https://schema.pragmaticbim.ch/GroundReferenceSource)

**Enum URI:** [pbs:GroundReferenceSource](https://schema.pragmaticbim.ch/GroundReferenceSource)


## Permissible Values
| Value | Meaning | Description | Additional Info |
| --- | --- | --- | --- |
| ifc_property | pbs:ground_reference_source_ifc_property | Flags taken from Pset_BuildingStoreyCommon.AboveGround and EntranceLevel. | Title: IFC property<br>|
| name_convention | pbs:ground_reference_source_name_convention | Flags taken from the storey naming convention (EG/00 ground, U## and FD below, ## above, .Z intermediate inherits the base storey). | Title: Name convention<br>|
| elevation | pbs:ground_reference_source_elevation | Ground floor is the lowest storey with elevation at or above 0; storeys at or above that elevation are above ground. | Title: Elevation<br>|




## Slots

| Name | Description |
| ---  | --- |
| [ground_reference_source](ground_reference_source.md) | Which source was used to resolve above_ground and is_ground_floor for this storey (same source for all storeys of a building). |










## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch






## LinkML Source

<details>
```yaml
name: GroundReferenceSource
description: Source used to resolve LevelContext above_ground and is_ground_floor
  flags.
from_schema: https://schema.pragmaticbim.ch
rank: 1000
enum_uri: pbs:GroundReferenceSource
permissible_values:
  ifc_property:
    text: ifc_property
    description: Flags taken from Pset_BuildingStoreyCommon.AboveGround and EntranceLevel.
    meaning: pbs:ground_reference_source_ifc_property
    alt_descriptions:
      de:
        source: de
        description: IFC-Merkmal
    title: IFC property
  name_convention:
    text: name_convention
    description: 'Flags taken from the storey naming convention (EG/00 ground, U##
      and FD below, ## above, .Z intermediate inherits the base storey).'
    meaning: pbs:ground_reference_source_name_convention
    alt_descriptions:
      de:
        source: de
        description: Namenskonvention
    title: Name convention
  elevation:
    text: elevation
    description: Ground floor is the lowest storey with elevation at or above 0; storeys
      at or above that elevation are above ground.
    meaning: pbs:ground_reference_source_elevation
    alt_descriptions:
      de:
        source: de
        description: Hoehenkote
    title: Elevation

```
</details>

</div>