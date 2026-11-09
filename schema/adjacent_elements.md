---
search:
  boost: 5.0
---

# Slot: adjacent_elements 


_Physical elements adjacent to the space through an IFC space boundary (walls, slabs, doors, windows, coverings). Space-side view of separates_spaces, connects_spaces, and bounded_by, serialized as bot:adjacentElement._



<div data-search-exclude markdown="1">



URI: [bot:adjacentElement](https://w3id.org/bot#adjacentElement)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Space](Space.md) | Spatial container used for occupancy, circulation, service, or analysis. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [PhysicalElement](PhysicalElement.md) |
| Domain Of | [Space](Space.md) |
| Slot URI | [bot:adjacentElement](https://w3id.org/bot#adjacentElement) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | bot:adjacentElement |
| native | pbs:adjacent_elements |




## LinkML Source

<details>
```yaml
name: adjacent_elements
description: Physical elements adjacent to the space through an IFC space boundary
  (walls, slabs, doors, windows, coverings). Space-side view of separates_spaces,
  connects_spaces, and bounded_by, serialized as bot:adjacentElement.
from_schema: https://schema.pragmaticbim.ch
rank: 1000
slot_uri: bot:adjacentElement
domain_of:
- Space
range: PhysicalElement
multivalued: true

```
</details></div>