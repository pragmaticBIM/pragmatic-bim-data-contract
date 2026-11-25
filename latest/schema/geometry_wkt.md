---
search:
  boost: 3.0
---

# Slot: geometry_wkt 


_Inline WKT payload for small representations (for example a footprint_2d polygon or a path_3d line in project coordinates, metres)._



<div data-search-exclude markdown="1">



URI: [pbs:geometry_wkt](https://schema.pragmaticbim.ch/geometry_wkt)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [GeometryRepresentation](GeometryRepresentation.md) | Minimal geometry reference for an entity, separating representation from encoding format. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [GeometryRepresentation](GeometryRepresentation.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pbs:geometry_wkt |
| native | pbs:geometry_wkt |




## LinkML Source

<details>
```yaml
name: geometry_wkt
description: Inline WKT payload for small representations (for example a footprint_2d
  polygon or a path_3d line in project coordinates, metres).
from_schema: https://schema.pragmaticbim.ch
rank: 1000
domain_of:
- GeometryRepresentation
range: string

```
</details></div>