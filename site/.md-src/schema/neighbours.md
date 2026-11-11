---
search:
  boost: 5.0
---

# Slot: neighbours 


_Clear distances to the neighbouring physical elements within the measurement range configured for the conversion. Computed from geometry; elements farther away have no record._



<div data-search-exclude markdown="1">



URI: [pbs:neighbours](https://schema.pragmaticbim.ch/neighbours)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [PhysicalElement](PhysicalElement.md) | Base class for physical elements that can be placed in built asset/level context. |  no  |
| [Separator](Separator.md) | Abstract base class for elements that separate spaces or zones. |  no  |
| [SeparatorWall](SeparatorWall.md) | Wall-based separating element. |  no  |
| [SeparatorSlab](SeparatorSlab.md) | Slab-based separating element (for example floor/roof/base slab separators). |  no  |
| [ConnectionPhysical](ConnectionPhysical.md) | Physical connector providing functional connection between spaces (for example door, window, duct, pipe, cable) or carrying loads between elements (column, beam). |  no  |
| [SafetyBarrier](SafetyBarrier.md) | Linear fall protection or guiding element (balustrade, guardrail, handrail) along slab, balcony, roof, landing, stair, or ramp edges. |  no  |
| [Boundary](Boundary.md) | Physical element acting as a boundary treatment (for example covering). |  no  |
| [Equipment](Equipment.md) | Endpoint or device element (for example terminal, unit, control device, sensor) located in a space and assigned to a system. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [NeighbourDistance](NeighbourDistance.md) |
| Domain Of | [PhysicalElement](PhysicalElement.md) |

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
| self | pbs:neighbours |
| native | pbs:neighbours |




## LinkML Source

<details>
```yaml
name: neighbours
description: Clear distances to the neighbouring physical elements within the measurement
  range configured for the conversion. Computed from geometry; elements farther away
  have no record.
from_schema: https://schema.pragmaticbim.ch
rank: 1000
domain_of:
- PhysicalElement
range: NeighbourDistance
multivalued: true
inlined: true

```
</details></div>