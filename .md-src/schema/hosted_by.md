---
search:
  boost: 5.0
---

# Slot: hosted_by 


_Host element whose opening this connector fills (for example the wall a door or window sits in). From IfcRelFillsElement and IfcRelVoidsElement, or computed from geometry when the IFC chain is missing._



<div data-search-exclude markdown="1">



URI: [pbs:hosted_by](https://schema.pragmaticbim.ch/hosted_by)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ConnectionPhysical](ConnectionPhysical.md) | Physical connector providing functional connection between spaces (for example door, window, duct, pipe, cable) or carrying loads between elements (column, beam). |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [PhysicalElement](PhysicalElement.md) |
| Domain Of | [ConnectionPhysical](ConnectionPhysical.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pbs:hosted_by |
| native | pbs:hosted_by |




## LinkML Source

<details>
```yaml
name: hosted_by
description: Host element whose opening this connector fills (for example the wall
  a door or window sits in). From IfcRelFillsElement and IfcRelVoidsElement, or computed
  from geometry when the IFC chain is missing.
from_schema: https://schema.pragmaticbim.ch
rank: 1000
domain_of:
- ConnectionPhysical
range: PhysicalElement

```
</details></div>