---
search:
  boost: 2.0
---


# Enum: IndoorEnvironmentPropertyKey 




_Canonical indoor environment keys for spaces (temperature, humidity, air, light, occupancy)._



<div data-search-exclude markdown="1">

URI: [pbs:IndoorEnvironmentPropertyKey](https://schema.pragmaticbim.ch/IndoorEnvironmentPropertyKey)

**Enum URI:** [pbs:IndoorEnvironmentPropertyKey](https://schema.pragmaticbim.ch/IndoorEnvironmentPropertyKey)


## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| winter_temperature_min | pbs:indoor_environment_winter_temperature_min | Minimum room temperature in winter in degC. |
| winter_temperature_max | pbs:indoor_environment_winter_temperature_max | Maximum room temperature in winter in degC. |
| summer_temperature_min | pbs:indoor_environment_summer_temperature_min | Minimum room temperature in summer in degC. |
| summer_temperature_max | pbs:indoor_environment_summer_temperature_max | Maximum room temperature in summer in degC. |
| relative_humidity_min | pbs:indoor_environment_relative_humidity_min | Minimum relative humidity in percent. |
| relative_humidity_max | pbs:indoor_environment_relative_humidity_max | Maximum relative humidity in percent. |
| outdoor_air_flow_rate | pbs:indoor_environment_outdoor_air_flow_rate | Outdoor air flow rate in m3/h. |
| required_illuminance | pbs:indoor_environment_required_illuminance | Maintained illuminance in lx. |
| peak_occupancy | pbs:indoor_environment_peak_occupancy | Peak number of occupants. |
| daily_operating_hours | pbs:indoor_environment_daily_operating_hours | Daily operating hours in h. |




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
name: IndoorEnvironmentPropertyKey
description: Canonical indoor environment keys for spaces (temperature, humidity,
  air, light, occupancy).
from_schema: https://schema.pragmaticbim.ch
rank: 1000
enum_uri: pbs:IndoorEnvironmentPropertyKey
permissible_values:
  winter_temperature_min:
    text: winter_temperature_min
    description: Minimum room temperature in winter in degC.
    meaning: pbs:indoor_environment_winter_temperature_min
  winter_temperature_max:
    text: winter_temperature_max
    description: Maximum room temperature in winter in degC.
    meaning: pbs:indoor_environment_winter_temperature_max
  summer_temperature_min:
    text: summer_temperature_min
    description: Minimum room temperature in summer in degC.
    meaning: pbs:indoor_environment_summer_temperature_min
  summer_temperature_max:
    text: summer_temperature_max
    description: Maximum room temperature in summer in degC.
    meaning: pbs:indoor_environment_summer_temperature_max
  relative_humidity_min:
    text: relative_humidity_min
    description: Minimum relative humidity in percent.
    meaning: pbs:indoor_environment_relative_humidity_min
  relative_humidity_max:
    text: relative_humidity_max
    description: Maximum relative humidity in percent.
    meaning: pbs:indoor_environment_relative_humidity_max
  outdoor_air_flow_rate:
    text: outdoor_air_flow_rate
    description: Outdoor air flow rate in m3/h.
    meaning: pbs:indoor_environment_outdoor_air_flow_rate
  required_illuminance:
    text: required_illuminance
    description: Maintained illuminance in lx.
    meaning: pbs:indoor_environment_required_illuminance
  peak_occupancy:
    text: peak_occupancy
    description: Peak number of occupants.
    meaning: pbs:indoor_environment_peak_occupancy
  daily_operating_hours:
    text: daily_operating_hours
    description: Daily operating hours in h.
    meaning: pbs:indoor_environment_daily_operating_hours

```
</details>

</div>