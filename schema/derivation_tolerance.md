---
search:
  boost: 3.0
---

# Slot: derivation_tolerance 


_Geometric or numeric tolerance applied by the method (for example the maximum gap still counted as contact)._



<div data-search-exclude markdown="1">



URI: [pbs:derivation_tolerance](https://schema.pragmaticbim.ch/derivation_tolerance)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Derivation](Derivation.md) | How a value or relation was obtained. Embedded on the record it describes (for example a QuantityValue measured from geometry, or a ConnectionVirtual computed by a contact test) so that every derived fact carries its source kind, method, method version, tolerance, and input entities. Lets checks distinguish values read from IFC, values computed from geometry, project parameters, and manual entries, and lets results be reproduced or recomputed when a method changes. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Double](Double.md) |
| Domain Of | [Derivation](Derivation.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Value Constraints

| Property | Value |
| --- | --- |
| Minimum Value | 0 |












## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pbs:derivation_tolerance |
| native | pbs:derivation_tolerance |




## LinkML Source

<details>
```yaml
name: derivation_tolerance
description: Geometric or numeric tolerance applied by the method (for example the
  maximum gap still counted as contact).
from_schema: https://schema.pragmaticbim.ch
rank: 1000
domain_of:
- Derivation
range: double
minimum_value: 0

```
</details></div>