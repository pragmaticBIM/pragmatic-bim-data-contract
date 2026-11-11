---
search:
  boost: 3.0
---

# Slot: vertical_clear_distance 


_Vertical clear distance in metres between the height ranges; 0 where they overlap or touch._



<div data-search-exclude markdown="1">



URI: [pbs:vertical_clear_distance](https://schema.pragmaticbim.ch/vertical_clear_distance)
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
| self | pbs:vertical_clear_distance |
| native | pbs:vertical_clear_distance |




## LinkML Source

<details>
```yaml
name: vertical_clear_distance
description: Vertical clear distance in metres between the height ranges; 0 where
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