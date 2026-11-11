---
search:
  boost: 3.0
---

# Slot: derivation_source_kind 


_Kind of source the value or relation comes from (IFC relationship or property, geometry computation, project parameter, manual entry)._



<div data-search-exclude markdown="1">



URI: [pbs:derivation_source_kind](https://schema.pragmaticbim.ch/derivation_source_kind)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Derivation](Derivation.md) | How a value or relation was obtained. Embedded on the record it describes (for example a QuantityValue measured from geometry, or a ConnectionVirtual computed by a contact test) so that every derived fact carries its source kind, method, method version, tolerance, and input entities. Lets checks distinguish values read from IFC, values computed from geometry, project parameters, and manual entries, and lets results be reproduced or recomputed when a method changes. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [DerivationSourceKind](DerivationSourceKind.md) |
| Domain Of | [Derivation](Derivation.md) |

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
| self | pbs:derivation_source_kind |
| native | pbs:derivation_source_kind |




## LinkML Source

<details>
```yaml
name: derivation_source_kind
description: Kind of source the value or relation comes from (IFC relationship or
  property, geometry computation, project parameter, manual entry).
from_schema: https://schema.pragmaticbim.ch
rank: 1000
domain_of:
- Derivation
range: DerivationSourceKind
required: true

```
</details></div>