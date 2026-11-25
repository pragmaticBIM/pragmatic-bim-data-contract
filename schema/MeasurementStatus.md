---
search:
  boost: 2.0
---


# Enum: MeasurementStatus 




_Outcome of attempting a derived measurement on model entities._



<div data-search-exclude markdown="1">

URI: [pbs:MeasurementStatus](https://schema.pragmaticbim.ch/MeasurementStatus)

**Enum URI:** [pbs:MeasurementStatus](https://schema.pragmaticbim.ch/MeasurementStatus)


## Permissible Values
| Value | Meaning | Description | Additional Info |
| --- | --- | --- | --- |
| measured | pbs:measurement_status_measured | A value was successfully measured from the model. | Title: Measured<br>|
| not_measurable | pbs:measurement_status_not_measurable | The measurement could not be computed from the available model data or geometry. | Title: Not measurable<br>|
| not_applicable | pbs:measurement_status_not_applicable | The measurement does not apply to these subjects in this context. | Title: Not applicable<br>|




## Slots

| Name | Description |
| ---  | --- |
| [measurement_status](measurement_status.md) | Whether the measurement was obtained (measured), could not be computed from the model (not_measurable), or does not apply in this context (not_applicable). |










## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch






## LinkML Source

<details>
```yaml
name: MeasurementStatus
description: Outcome of attempting a derived measurement on model entities.
from_schema: https://schema.pragmaticbim.ch
rank: 1000
enum_uri: pbs:MeasurementStatus
permissible_values:
  measured:
    text: measured
    description: A value was successfully measured from the model.
    meaning: pbs:measurement_status_measured
    alt_descriptions:
      de:
        source: de
        description: Gemessen
    title: Measured
  not_measurable:
    text: not_measurable
    description: The measurement could not be computed from the available model data
      or geometry.
    meaning: pbs:measurement_status_not_measurable
    alt_descriptions:
      de:
        source: de
        description: Nicht messbar
    title: Not measurable
  not_applicable:
    text: not_applicable
    description: The measurement does not apply to these subjects in this context.
    meaning: pbs:measurement_status_not_applicable
    alt_descriptions:
      de:
        source: de
        description: Nicht anwendbar
    title: Not applicable

```
</details>

</div>