---
search:
  boost: 5.0
---

# Slot: derivation 


_How this value or relation was obtained (source kind, method, version, tolerance, inputs). Omit only when the record is copied unchanged from its source and no further traceability is needed._



<div data-search-exclude markdown="1">



URI: [pbs:derivation](https://schema.pragmaticbim.ch/derivation)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [QuantityValue](QuantityValue.md) | Minimal quantity record for costing and analysis. |  no  |
| [ConnectionVirtual](ConnectionVirtual.md) | Logical or topological connection between spaces and/or physical elements. Connections read from IFC relationships and connections computed from geometry (for example a contact test) use the same class; derivation records which of the two applies and how the connection was computed. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Derivation](Derivation.md) |
| Domain Of | [QuantityValue](QuantityValue.md), [ConnectionVirtual](ConnectionVirtual.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pbs:derivation |
| native | pbs:derivation |




## LinkML Source

<details>
```yaml
name: derivation
description: How this value or relation was obtained (source kind, method, version,
  tolerance, inputs). Omit only when the record is copied unchanged from its source
  and no further traceability is needed.
from_schema: https://schema.pragmaticbim.ch
rank: 1000
domain_of:
- QuantityValue
- ConnectionVirtual
range: Derivation
inlined: true

```
</details></div>