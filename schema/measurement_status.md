---
search:
  boost: 5.0
---

# Slot: measurement_status 


_Whether the measurement was obtained (measured), could not be computed from the model (not_measurable), or does not apply in this context (not_applicable)._



<div data-search-exclude markdown="1">



URI: [pbs:measurement_status](https://schema.pragmaticbim.ch/measurement_status)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [DerivedMeasurement](DerivedMeasurement.md) | Measurement entity with its own identity for values that involve more than one subject (for example clear width between a stair and two railings). Subjects are listed in applies_to_entities; the value and its Derivation live in quantity_values; an optional display line uses geometry_representations (typically WKT LINESTRING Z). Use measurement_status to distinguish a successful measure from not_measurable or not_applicable. |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [MeasurementStatus](MeasurementStatus.md) |
| Domain Of | [DerivedMeasurement](DerivedMeasurement.md) |

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
| self | pbs:measurement_status |
| native | pbs:measurement_status |




## LinkML Source

<details>
```yaml
name: measurement_status
description: Whether the measurement was obtained (measured), could not be computed
  from the model (not_measurable), or does not apply in this context (not_applicable).
from_schema: https://schema.pragmaticbim.ch
rank: 1000
domain_of:
- DerivedMeasurement
range: MeasurementStatus
required: true

```
</details></div>