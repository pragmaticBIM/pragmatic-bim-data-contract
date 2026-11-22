---
search:
  boost: 5.0
---

# Slot: terrain_surface_status 


_Whether the terrain surface represents the existing or the projected site._



<div data-search-exclude markdown="1">



URI: [pbs:terrain_surface_status](https://schema.pragmaticbim.ch/terrain_surface_status)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [TerrainSurface](TerrainSurface.md) | Existing or projected terrain surface (survey surface) as a geographic element. Converted from IfcGeographicElement (IFC4+); IFC2x3 proxies stay generic. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [TerrainSurfaceStatus](TerrainSurfaceStatus.md) |
| Domain Of | [TerrainSurface](TerrainSurface.md) |

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
| self | pbs:terrain_surface_status |
| native | pbs:terrain_surface_status |




## LinkML Source

<details>
```yaml
name: terrain_surface_status
description: Whether the terrain surface represents the existing or the projected
  site.
from_schema: https://schema.pragmaticbim.ch
rank: 1000
domain_of:
- TerrainSurface
range: TerrainSurfaceStatus
required: true

```
</details></div>