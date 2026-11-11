---
search:
  boost: 5.0
---

# Slot: rests_on 


_Elements this element sits on: its underside bears on their top (for example wall on slab, column on slab, slab on wall or column). Computed from geometric contact; it records contact, not a structural analysis result. The inverse (supports) is read by querying the slot from the other side._



<div data-search-exclude markdown="1">



URI: [pbs:rests_on](https://schema.pragmaticbim.ch/rests_on)
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
| Range | [PhysicalElement](PhysicalElement.md) |
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
| self | pbs:rests_on |
| native | pbs:rests_on |




## LinkML Source

<details>
```yaml
name: rests_on
description: 'Elements this element sits on: its underside bears on their top (for
  example wall on slab, column on slab, slab on wall or column). Computed from geometric
  contact; it records contact, not a structural analysis result. The inverse (supports)
  is read by querying the slot from the other side.'
from_schema: https://schema.pragmaticbim.ch
rank: 1000
domain_of:
- PhysicalElement
range: PhysicalElement
multivalued: true

```
</details></div>