---
search:
  boost: 5.0
---

# Slot: above_ground 


_Whether this storey is fully above ground. Resolved from IFC properties, the storey naming convention, or elevation (see ground_reference_source)._



<div data-search-exclude markdown="1">



URI: [pbs:above_ground](https://schema.pragmaticbim.ch/above_ground)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [LevelContext](LevelContext.md) | Spatial context node constrained to level/storey semantics. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Boolean](Boolean.md) |
| Domain Of | [LevelContext](LevelContext.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pbs:above_ground |
| native | pbs:above_ground |




## LinkML Source

<details>
```yaml
name: above_ground
description: Whether this storey is fully above ground. Resolved from IFC properties,
  the storey naming convention, or elevation (see ground_reference_source).
from_schema: https://schema.pragmaticbim.ch
rank: 1000
domain_of:
- LevelContext
range: boolean

```
</details></div>