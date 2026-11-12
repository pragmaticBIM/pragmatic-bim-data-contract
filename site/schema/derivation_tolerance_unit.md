---
search:
  boost: 3.0
---

# Slot: derivation_tolerance_unit 


_Unit of derivation_tolerance (for example m, mm, deg)._



<div data-search-exclude markdown="1">



URI: [pbs:derivation_tolerance_unit](https://schema.pragmaticbim.ch/derivation_tolerance_unit)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Derivation](Derivation.md) | How a value or relation was obtained. Embedded on the record it describes (for example a QuantityValue measured from geometry, or a ConnectionVirtual computed by a contact test) so that every derived fact carries its source kind, method, method version, tolerance, and input entities. Lets checks distinguish values read from IFC, values computed from geometry, project parameters, and manual entries, and lets results be reproduced or recomputed when a method changes. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Derivation](Derivation.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pbs:derivation_tolerance_unit |
| native | pbs:derivation_tolerance_unit |




## LinkML Source

<details>
```yaml
name: derivation_tolerance_unit
description: Unit of derivation_tolerance (for example m, mm, deg).
from_schema: https://schema.pragmaticbim.ch
rank: 1000
domain_of:
- Derivation
range: string

```
</details></div>