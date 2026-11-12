---
search:
  boost: 3.0
---

# Slot: derived_at 


_Timestamp when the value or relation was derived._



<div data-search-exclude markdown="1">



URI: [pbs:derived_at](https://schema.pragmaticbim.ch/derived_at)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Derivation](Derivation.md) | How a value or relation was obtained. Embedded on the record it describes (for example a QuantityValue measured from geometry, or a ConnectionVirtual computed by a contact test) so that every derived fact carries its source kind, method, method version, tolerance, and input entities. Lets checks distinguish values read from IFC, values computed from geometry, project parameters, and manual entries, and lets results be reproduced or recomputed when a method changes. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Datetime](Datetime.md) |
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
| self | pbs:derived_at |
| native | pbs:derived_at |




## LinkML Source

<details>
```yaml
name: derived_at
description: Timestamp when the value or relation was derived.
from_schema: https://schema.pragmaticbim.ch
rank: 1000
domain_of:
- Derivation
range: datetime

```
</details></div>