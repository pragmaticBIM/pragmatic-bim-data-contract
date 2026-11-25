---
search:
  boost: 5.0
---

# Slot: guards_space 


_Spaces whose walking surface this barrier protects against falls. Computed from geometry: the barrier footprint lies within a tolerance of the space footprint and the space floor is at or below the barrier base._



<div data-search-exclude markdown="1">



URI: [pbs:guards_space](https://schema.pragmaticbim.ch/guards_space)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SafetyBarrier](SafetyBarrier.md) | Linear fall protection or guiding element (balustrade, guardrail, handrail) along slab, balcony, roof, landing, stair, or ramp edges. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Space](Space.md) |
| Domain Of | [SafetyBarrier](SafetyBarrier.md) |

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
| self | pbs:guards_space |
| native | pbs:guards_space |




## LinkML Source

<details>
```yaml
name: guards_space
description: 'Spaces whose walking surface this barrier protects against falls. Computed
  from geometry: the barrier footprint lies within a tolerance of the space footprint
  and the space floor is at or below the barrier base.'
from_schema: https://schema.pragmaticbim.ch
rank: 1000
domain_of:
- SafetyBarrier
range: Space
multivalued: true

```
</details></div>