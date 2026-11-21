---
search:
  boost: 5.0
---

# Slot: opens_in_escape_direction 


_Whether a swing door leaf opens in the direction of the shortest horizontal escape route through the door. Computed from door OperationType and local placement against escape_route_next; unset when the door is not on a route or the operation type is not a swing._



<div data-search-exclude markdown="1">



URI: [pbs:opens_in_escape_direction](https://schema.pragmaticbim.ch/opens_in_escape_direction)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ConnectionPhysical](ConnectionPhysical.md) | Physical connector providing functional connection between spaces (for example door, window, duct, pipe, cable) or carrying loads between elements (column, beam). |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Boolean](Boolean.md) |
| Domain Of | [ConnectionPhysical](ConnectionPhysical.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pbs:opens_in_escape_direction |
| native | pbs:opens_in_escape_direction |




## LinkML Source

<details>
```yaml
name: opens_in_escape_direction
description: Whether a swing door leaf opens in the direction of the shortest horizontal
  escape route through the door. Computed from door OperationType and local placement
  against escape_route_next; unset when the door is not on a route or the operation
  type is not a swing.
from_schema: https://schema.pragmaticbim.ch
rank: 1000
domain_of:
- ConnectionPhysical
range: boolean

```
</details></div>