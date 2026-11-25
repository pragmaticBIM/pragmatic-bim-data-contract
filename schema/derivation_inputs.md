---
search:
  boost: 3.0
---

# Slot: derivation_inputs 


_Entities whose data or geometry were used, beyond the subject itself. For a height measured above a reference surface this includes the reference element (for example the pavement course)._



<div data-search-exclude markdown="1">



URI: [pbs:derivation_inputs](https://schema.pragmaticbim.ch/derivation_inputs)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Derivation](Derivation.md) | How a value or relation was obtained. Embedded on the record it describes (for example a QuantityValue measured from geometry, or a ConnectionVirtual computed by a contact test) so that every derived fact carries its source kind, method, method version, tolerance, and input entities. Lets checks distinguish values read from IFC, values computed from geometry, project parameters, and manual entries, and lets results be reproduced or recomputed when a method changes. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Entity](Entity.md) |
| Domain Of | [Derivation](Derivation.md) |

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
| self | pbs:derivation_inputs |
| native | pbs:derivation_inputs |




## LinkML Source

<details>
```yaml
name: derivation_inputs
description: Entities whose data or geometry were used, beyond the subject itself.
  For a height measured above a reference surface this includes the reference element
  (for example the pavement course).
from_schema: https://schema.pragmaticbim.ch
rank: 1000
domain_of:
- Derivation
range: Entity
multivalued: true
inlined: false

```
</details></div>