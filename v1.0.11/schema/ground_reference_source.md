---
search:
  boost: 5.0
---

# Slot: ground_reference_source 


_Which source was used to resolve above_ground and is_ground_floor for this storey (same source for all storeys of a building)._



<div data-search-exclude markdown="1">



URI: [pbs:ground_reference_source](https://schema.pragmaticbim.ch/ground_reference_source)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [LevelContext](LevelContext.md) | Spatial context node constrained to level/storey semantics. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [GroundReferenceSource](GroundReferenceSource.md) |
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
| self | pbs:ground_reference_source |
| native | pbs:ground_reference_source |




## LinkML Source

<details>
```yaml
name: ground_reference_source
description: Which source was used to resolve above_ground and is_ground_floor for
  this storey (same source for all storeys of a building).
from_schema: https://schema.pragmaticbim.ch
rank: 1000
domain_of:
- LevelContext
range: GroundReferenceSource

```
</details></div>