---
search:
  boost: 5.0
---

# Slot: is_ground_floor 


_Whether this storey is the building's ground floor (entrance level). Exactly one storey per building should be true after resolution._



<div data-search-exclude markdown="1">



URI: [pbs:is_ground_floor](https://schema.pragmaticbim.ch/is_ground_floor)
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
| self | pbs:is_ground_floor |
| native | pbs:is_ground_floor |




## LinkML Source

<details>
```yaml
name: is_ground_floor
description: Whether this storey is the building's ground floor (entrance level).
  Exactly one storey per building should be true after resolution.
from_schema: https://schema.pragmaticbim.ch
rank: 1000
domain_of:
- LevelContext
range: boolean

```
</details></div>