---
search:
  boost: 3.0
---

# Slot: neighbour 


_The neighbouring element the distances are measured to._



<div data-search-exclude markdown="1">



URI: [pbs:neighbour](https://schema.pragmaticbim.ch/neighbour)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [NeighbourDistance](NeighbourDistance.md) | Clear distance from an element to a neighbouring physical element, measured from geometry: the horizontal gap between their plan outlines and the vertical gap between their height ranges. Both are 0 where the elements overlap in that direction, so 0 and 0 means touching or intersecting. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [PhysicalElement](PhysicalElement.md) |
| Domain Of | [NeighbourDistance](NeighbourDistance.md) |

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
| self | pbs:neighbour |
| native | pbs:neighbour |




## LinkML Source

<details>
```yaml
name: neighbour
description: The neighbouring element the distances are measured to.
from_schema: https://schema.pragmaticbim.ch
rank: 1000
domain_of:
- NeighbourDistance
range: PhysicalElement
required: true

```
</details></div>