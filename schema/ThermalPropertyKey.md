---
search:
  boost: 2.0
---


# Enum: ThermalPropertyKey 




_Canonical thermal-related keys derived from IFC PropertySets._



<div data-search-exclude markdown="1">

URI: [pbs:ThermalPropertyKey](https://schema.pragmaticbim.ch/ThermalPropertyKey)

**Enum URI:** [pbs:ThermalPropertyKey](https://schema.pragmaticbim.ch/ThermalPropertyKey)


## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| u_value | pbs:thermal_property_u_value |  |
| r_value | pbs:thermal_property_r_value |  |
| thermal_transmittance | pbs:thermal_property_thermal_transmittance |  |
| is_external | pbs:thermal_property_is_external | Element faces the outside of the building (IFC IsExternal); marks thermal envelope elements. |
| air_tightness_n50 | pbs:thermal_property_air_tightness_n50 | Air change rate at 50 Pa pressure difference in 1/h (building envelope). |




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
name: ThermalPropertyKey
description: Canonical thermal-related keys derived from IFC PropertySets.
from_schema: https://schema.pragmaticbim.ch
rank: 1000
enum_uri: pbs:ThermalPropertyKey
permissible_values:
  u_value:
    text: u_value
    meaning: pbs:thermal_property_u_value
  r_value:
    text: r_value
    meaning: pbs:thermal_property_r_value
  thermal_transmittance:
    text: thermal_transmittance
    meaning: pbs:thermal_property_thermal_transmittance
  is_external:
    text: is_external
    description: Element faces the outside of the building (IFC IsExternal); marks
      thermal envelope elements.
    meaning: pbs:thermal_property_is_external
  air_tightness_n50:
    text: air_tightness_n50
    description: Air change rate at 50 Pa pressure difference in 1/h (building envelope).
    meaning: pbs:thermal_property_air_tightness_n50

```
</details>

</div>