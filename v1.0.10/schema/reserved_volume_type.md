---
search:
  boost: 5.0
---

# Slot: reserved_volume_type 


_Purpose of the reserved volume._



<div data-search-exclude markdown="1">



URI: [pbs:reserved_volume_type](https://schema.pragmaticbim.ch/reserved_volume_type)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ReservedVolume](ReservedVolume.md) | Volume that must stay clear of building elements (maintenance space, installation path, structural exclusion zone, movement clearance, device space). Modelled as a proxy volume and identified through the pragmaticBIM Reference element definition. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [ReservedVolumeType](ReservedVolumeType.md) |
| Domain Of | [ReservedVolume](ReservedVolume.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pbs:reserved_volume_type |
| native | pbs:reserved_volume_type |




## LinkML Source

<details>
```yaml
name: reserved_volume_type
description: Purpose of the reserved volume.
from_schema: https://schema.pragmaticbim.ch
rank: 1000
domain_of:
- ReservedVolume
range: ReservedVolumeType
required: true

```
</details></div>