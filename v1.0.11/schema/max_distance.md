---
search:
  boost: 5.0
---

# Slot: max_distance 


_Maximum walking distance in metres when adjacency_kind is max_distance._



<div data-search-exclude markdown="1">



URI: [pbs:max_distance](https://schema.pragmaticbim.ch/max_distance)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SpatialRequirement](SpatialRequirement.md) | Spatial constraint requirement (min area, min height, adjacency, distance, etc.). |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Double](Double.md) |
| Domain Of | [SpatialRequirement](SpatialRequirement.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
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
| self | pbs:max_distance |
| native | pbs:max_distance |




## LinkML Source

<details>
```yaml
name: max_distance
description: Maximum walking distance in metres when adjacency_kind is max_distance.
from_schema: https://schema.pragmaticbim.ch
rank: 1000
domain_of:
- SpatialRequirement
range: double
minimum_value: 0

```
</details></div>