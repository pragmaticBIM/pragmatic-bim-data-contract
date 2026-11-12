---
search:
  boost: 5.0
---

# Slot: connects_physical_elements 


_Physical elements connected to this one side by side (for example wall-wall junction, beam framing into a column). On a physical element the relation is symmetric and stated on both elements. From IfcRelConnectsElements / IfcRelConnectsPathElements, or computed from geometric contact. Bearing contact is rests_on._



<div data-search-exclude markdown="1">



URI: [pbs:connects_physical_elements](https://schema.pragmaticbim.ch/connects_physical_elements)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [PhysicalElement](PhysicalElement.md) | Base class for physical elements that can be placed in built asset/level context. |  no  |
| [ConnectionVirtual](ConnectionVirtual.md) | Logical or topological connection between spaces and/or physical elements. Connections read from IFC relationships and connections computed from geometry (for example a contact test) use the same class; derivation records which of the two applies and how the connection was computed. |  no  |
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
| Domain Of | [PhysicalElement](PhysicalElement.md), [ConnectionVirtual](ConnectionVirtual.md) |

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
| self | pbs:connects_physical_elements |
| native | pbs:connects_physical_elements |




## LinkML Source

<details>
```yaml
name: connects_physical_elements
description: Physical elements connected to this one side by side (for example wall-wall
  junction, beam framing into a column). On a physical element the relation is symmetric
  and stated on both elements. From IfcRelConnectsElements / IfcRelConnectsPathElements,
  or computed from geometric contact. Bearing contact is rests_on.
from_schema: https://schema.pragmaticbim.ch
rank: 1000
domain_of:
- PhysicalElement
- ConnectionVirtual
range: PhysicalElement
multivalued: true

```
</details></div>