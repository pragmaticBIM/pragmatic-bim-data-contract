---
search:
  boost: 5.0
---

# Slot: lit_space 


_Interior spaces that receive daylight through this window. From space boundaries or computed from geometry (adjacent or nearest interior space)._



<div data-search-exclude markdown="1">



URI: [pbs:lit_space](https://schema.pragmaticbim.ch/lit_space)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ConnectionPhysical](ConnectionPhysical.md) | Physical connector providing functional connection between spaces (for example door, window, duct, pipe, cable) or carrying loads between elements (column, beam). |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Space](Space.md) |
| Domain Of | [ConnectionPhysical](ConnectionPhysical.md) |

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
| self | pbs:lit_space |
| native | pbs:lit_space |




## LinkML Source

<details>
```yaml
name: lit_space
description: Interior spaces that receive daylight through this window. From space
  boundaries or computed from geometry (adjacent or nearest interior space).
from_schema: https://schema.pragmaticbim.ch
rank: 1000
domain_of:
- ConnectionPhysical
range: Space
multivalued: true

```
</details></div>