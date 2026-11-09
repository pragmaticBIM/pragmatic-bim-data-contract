---
search:
  boost: 2.0
---


# Enum: EnvironmentalPropertyKey 




_Canonical environmental keys for embodied impacts of an element type, per square metre of element area._



<div data-search-exclude markdown="1">

URI: [pbs:EnvironmentalPropertyKey](https://schema.pragmaticbim.ch/EnvironmentalPropertyKey)

**Enum URI:** [pbs:EnvironmentalPropertyKey](https://schema.pragmaticbim.ch/EnvironmentalPropertyKey)


## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| gwp_embodied | pbs:environmental_property_gwp_embodied | Embodied greenhouse gas emissions in kg CO2-eq/m2 (SIA 2032, KBOB). |
| primary_energy_non_renewable_embodied | pbs:environmental_property_primary_energy_non_renewable_embodied | Embodied non-renewable primary energy in kWh/m2 (SIA 2032, KBOB). |




## Slots

| Name | Description |
| ---  | --- |
| [property_key](property_key.md) |  |










## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch






## LinkML Source

<details>
```yaml
name: EnvironmentalPropertyKey
description: Canonical environmental keys for embodied impacts of an element type,
  per square metre of element area.
from_schema: https://schema.pragmaticbim.ch
rank: 1000
enum_uri: pbs:EnvironmentalPropertyKey
permissible_values:
  gwp_embodied:
    text: gwp_embodied
    description: Embodied greenhouse gas emissions in kg CO2-eq/m2 (SIA 2032, KBOB).
    meaning: pbs:environmental_property_gwp_embodied
  primary_energy_non_renewable_embodied:
    text: primary_energy_non_renewable_embodied
    description: Embodied non-renewable primary energy in kWh/m2 (SIA 2032, KBOB).
    meaning: pbs:environmental_property_primary_energy_non_renewable_embodied

```
</details>

</div>