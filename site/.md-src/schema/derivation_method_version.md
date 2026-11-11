---
search:
  boost: 3.0
---

# Slot: derivation_method_version 


_Version of the method implementation, so results can be reproduced and recomputed when the method changes._



<div data-search-exclude markdown="1">



URI: [pbs:derivation_method_version](https://schema.pragmaticbim.ch/derivation_method_version)
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
| self | pbs:derivation_method_version |
| native | pbs:derivation_method_version |




## LinkML Source

<details>
```yaml
name: derivation_method_version
description: Version of the method implementation, so results can be reproduced and
  recomputed when the method changes.
from_schema: https://schema.pragmaticbim.ch
rank: 1000
domain_of:
- Derivation
range: string

```
</details></div>