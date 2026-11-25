---
search:
  boost: 5.0
---

# Slot: intersects_elements 


_Physical elements whose body overlaps this reserved volume beyond the configured tolerance. Computed from geometry; an empty value means the volume is clear._



<div data-search-exclude markdown="1">



URI: [pbs:intersects_elements](https://schema.pragmaticbim.ch/intersects_elements)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ReservedVolume](ReservedVolume.md) | Volume that must stay clear of building elements (maintenance space, installation path, structural exclusion zone, movement clearance, device space). Modelled as a proxy volume and identified through the pragmaticBIM Reference element definition. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [PhysicalElement](PhysicalElement.md) |
| Domain Of | [ReservedVolume](ReservedVolume.md) |

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
| self | pbs:intersects_elements |
| native | pbs:intersects_elements |




## LinkML Source

<details>
```yaml
name: intersects_elements
description: Physical elements whose body overlaps this reserved volume beyond the
  configured tolerance. Computed from geometry; an empty value means the volume is
  clear.
from_schema: https://schema.pragmaticbim.ch
rank: 1000
domain_of:
- ReservedVolume
range: PhysicalElement
multivalued: true

```
</details></div>