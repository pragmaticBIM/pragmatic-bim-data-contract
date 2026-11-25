---
search:
  boost: 2.0
---


# Enum: ReservedVolumeType 




_Purpose of a reserved volume that must stay clear of building elements._



<div data-search-exclude markdown="1">

URI: [pbs:ReservedVolumeType](https://schema.pragmaticbim.ch/ReservedVolumeType)

**Enum URI:** [pbs:ReservedVolumeType](https://schema.pragmaticbim.ch/ReservedVolumeType)


## Permissible Values
| Value | Meaning | Description | Additional Info |
| --- | --- | --- | --- |
| maintenance | pbs:reserved_volume_type_maintenance | Clear maintenance space in front of or around equipment. | Title: Maintenance space<br>|
| installation_path | pbs:reserved_volume_type_installation_path | Clear path for bringing in or replacing large equipment. | Title: Installation path<br>|
| exclusion_zone | pbs:reserved_volume_type_exclusion_zone | Zone the structural concept keeps free of penetrations and recesses. | Title: Exclusion zone<br>|
| movement_clearance | pbs:reserved_volume_type_movement_clearance | Clear movement or manoeuvring area (for example turning areas, door swing clearances). | Title: Movement clearance<br>|
| device_space | pbs:reserved_volume_type_device_space | Space reserved for a device chosen late in the design. | Title: Device space<br>|




## Slots

| Name | Description |
| ---  | --- |
| [reserved_volume_type](reserved_volume_type.md) | Purpose of the reserved volume. |










## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch






## LinkML Source

<details>
```yaml
name: ReservedVolumeType
description: Purpose of a reserved volume that must stay clear of building elements.
from_schema: https://schema.pragmaticbim.ch
rank: 1000
enum_uri: pbs:ReservedVolumeType
permissible_values:
  maintenance:
    text: maintenance
    description: Clear maintenance space in front of or around equipment.
    meaning: pbs:reserved_volume_type_maintenance
    alt_descriptions:
      de:
        source: de
        description: Wartungsraum
    title: Maintenance space
  installation_path:
    text: installation_path
    description: Clear path for bringing in or replacing large equipment.
    meaning: pbs:reserved_volume_type_installation_path
    alt_descriptions:
      de:
        source: de
        description: Einbringweg
    title: Installation path
  exclusion_zone:
    text: exclusion_zone
    description: Zone the structural concept keeps free of penetrations and recesses.
    meaning: pbs:reserved_volume_type_exclusion_zone
    alt_descriptions:
      de:
        source: de
        description: Sperrzone
    title: Exclusion zone
  movement_clearance:
    text: movement_clearance
    description: Clear movement or manoeuvring area (for example turning areas, door
      swing clearances).
    meaning: pbs:reserved_volume_type_movement_clearance
    alt_descriptions:
      de:
        source: de
        description: Bewegungsfläche
    title: Movement clearance
  device_space:
    text: device_space
    description: Space reserved for a device chosen late in the design.
    meaning: pbs:reserved_volume_type_device_space
    alt_descriptions:
      de:
        source: de
        description: Geräteplatz
    title: Device space

```
</details>

</div>