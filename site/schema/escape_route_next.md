---
search:
  boost: 5.0
---

# Slot: escape_route_next 


_Next element on the shortest horizontal escape route: the door a space is left through, or the door or stair a door leads on to. The route ends at an exit to the outside or at a stair leaving the storey; follow the slot repeatedly to read the whole route. Computed from geometry; the remaining length is the escape_route_length quantity._



<div data-search-exclude markdown="1">



URI: [pbs:escape_route_next](https://schema.pragmaticbim.ch/escape_route_next)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ConnectionPhysical](ConnectionPhysical.md) | Physical connector providing functional connection between spaces (for example door, window, duct, pipe, cable) or carrying loads between elements (column, beam). |  no  |
| [Space](Space.md) | Spatial container used for occupancy, circulation, service, or analysis. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [PhysicalElement](PhysicalElement.md) |
| Domain Of | [ConnectionPhysical](ConnectionPhysical.md), [Space](Space.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pbs:escape_route_next |
| native | pbs:escape_route_next |




## LinkML Source

<details>
```yaml
name: escape_route_next
description: 'Next element on the shortest horizontal escape route: the door a space
  is left through, or the door or stair a door leads on to. The route ends at an exit
  to the outside or at a stair leaving the storey; follow the slot repeatedly to read
  the whole route. Computed from geometry; the remaining length is the escape_route_length
  quantity.'
from_schema: https://schema.pragmaticbim.ch
rank: 1000
domain_of:
- ConnectionPhysical
- Space
range: PhysicalElement

```
</details></div>