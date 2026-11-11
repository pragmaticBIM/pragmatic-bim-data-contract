---
search:
  boost: 3.0
---

# Slot: horizontal_clear_distance 


_Horizontal clear distance in metres between the plan outlines; 0 where they overlap or touch._



<div data-search-exclude markdown="1">



URI: [pbs:horizontal_clear_distance](https://schema.pragmaticbim.ch/horizontal_clear_distance)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [NeighbourDistance](NeighbourDistance.md) | Clear distance from an element to a neighbouring physical element, measured from geometry: the horizontal gap between their plan outlines and the vertical gap between their height ranges. Both are 0 where the elements overlap in that direction, so 0 and 0 means touching or intersecting. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Double](Double.md) |
| Domain Of | [NeighbourDistance](NeighbourDistance.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Value Constraints

| Property | Value |
| --- | --- |
| Minimum Value | 0 |












## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pbs:horizontal_clear_distance |
| native | pbs:horizontal_clear_distance |




## LinkML Source

<details>
```yaml
name: horizontal_clear_distance
description: Horizontal clear distance in metres between the plan outlines; 0 where
  they overlap or touch.
from_schema: https://schema.pragmaticbim.ch
rank: 1000
domain_of:
- NeighbourDistance
range: double
required: true
minimum_value: 0

```
</details></div>