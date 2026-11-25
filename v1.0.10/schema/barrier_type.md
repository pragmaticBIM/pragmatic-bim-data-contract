---
search:
  boost: 5.0
---

# Slot: barrier_type 


_Classification of the safety barrier (balustrade, guardrail, handrail)._



<div data-search-exclude markdown="1">



URI: [pbs:barrier_type](https://schema.pragmaticbim.ch/barrier_type)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SafetyBarrier](SafetyBarrier.md) | Linear fall protection or guiding element (balustrade, guardrail, handrail) along slab, balcony, roof, landing, stair, or ramp edges. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [BarrierType](BarrierType.md) |
| Domain Of | [SafetyBarrier](SafetyBarrier.md) |

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
| self | pbs:barrier_type |
| native | pbs:barrier_type |




## LinkML Source

<details>
```yaml
name: barrier_type
description: Classification of the safety barrier (balustrade, guardrail, handrail).
from_schema: https://schema.pragmaticbim.ch
rank: 1000
domain_of:
- SafetyBarrier
range: BarrierType
required: true

```
</details></div>