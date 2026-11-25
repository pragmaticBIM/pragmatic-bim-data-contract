---
search:
  boost: 2.0
---


# Enum: FirePropertyKey 




_Canonical fire-related keys derived from IFC PropertySets._



<div data-search-exclude markdown="1">

URI: [pbs:FirePropertyKey](https://schema.pragmaticbim.ch/FirePropertyKey)

**Enum URI:** [pbs:FirePropertyKey](https://schema.pragmaticbim.ch/FirePropertyKey)


## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| resistance_rating | pbs:fire_property_resistance_rating |  |
| smoke_rating | pbs:fire_property_smoke_rating |  |
| reaction_to_fire | pbs:fire_property_reaction_to_fire |  |
| safety_rated_duration | pbs:fire_property_safety_rated_duration | Rated operating time of safety lighting when normal lighting fails, in minutes (VKF 17-15). |
| safety_start_up_time | pbs:fire_property_safety_start_up_time | Time until safety lighting operates after general power supply failure, in seconds (VKF 17-15). |
| safety_supply_type | pbs:fire_property_safety_supply_type | Safety power source type (SINGLE_BATTERY, CENTRAL_BATTERY, GENERATOR). |
| safety_floor_illuminance | pbs:fire_property_safety_floor_illuminance | Planned illuminance of safety lighting at floor level of the escape route, in lx. |
| safety_not_switchable | pbs:fire_property_safety_not_switchable | Whether the safety luminaire cannot be switched off by a main or room lighting switch. |
| escape_sign_lighting_type | pbs:fire_property_escape_sign_lighting_type | Lighting type of an escape sign (ILLUMINATED, BACKLIT, AFTERGLOW). |
| escape_sign_supply_type | pbs:fire_property_escape_sign_supply_type | Safety power source of a lit or backlit escape sign (SINGLE_BATTERY, CENTRAL_BATTERY, GENERATOR). |
| escape_sign_mounting_height | pbs:fire_property_escape_sign_mounting_height | Mounting height of the lower edge of an escape sign above the finished floor, in metres. |




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
name: FirePropertyKey
description: Canonical fire-related keys derived from IFC PropertySets.
from_schema: https://schema.pragmaticbim.ch
rank: 1000
enum_uri: pbs:FirePropertyKey
permissible_values:
  resistance_rating:
    text: resistance_rating
    meaning: pbs:fire_property_resistance_rating
  smoke_rating:
    text: smoke_rating
    meaning: pbs:fire_property_smoke_rating
  reaction_to_fire:
    text: reaction_to_fire
    meaning: pbs:fire_property_reaction_to_fire
  safety_rated_duration:
    text: safety_rated_duration
    description: Rated operating time of safety lighting when normal lighting fails,
      in minutes (VKF 17-15).
    meaning: pbs:fire_property_safety_rated_duration
  safety_start_up_time:
    text: safety_start_up_time
    description: Time until safety lighting operates after general power supply failure,
      in seconds (VKF 17-15).
    meaning: pbs:fire_property_safety_start_up_time
  safety_supply_type:
    text: safety_supply_type
    description: Safety power source type (SINGLE_BATTERY, CENTRAL_BATTERY, GENERATOR).
    meaning: pbs:fire_property_safety_supply_type
  safety_floor_illuminance:
    text: safety_floor_illuminance
    description: Planned illuminance of safety lighting at floor level of the escape
      route, in lx.
    meaning: pbs:fire_property_safety_floor_illuminance
  safety_not_switchable:
    text: safety_not_switchable
    description: Whether the safety luminaire cannot be switched off by a main or
      room lighting switch.
    meaning: pbs:fire_property_safety_not_switchable
  escape_sign_lighting_type:
    text: escape_sign_lighting_type
    description: Lighting type of an escape sign (ILLUMINATED, BACKLIT, AFTERGLOW).
    meaning: pbs:fire_property_escape_sign_lighting_type
  escape_sign_supply_type:
    text: escape_sign_supply_type
    description: Safety power source of a lit or backlit escape sign (SINGLE_BATTERY,
      CENTRAL_BATTERY, GENERATOR).
    meaning: pbs:fire_property_escape_sign_supply_type
  escape_sign_mounting_height:
    text: escape_sign_mounting_height
    description: Mounting height of the lower edge of an escape sign above the finished
      floor, in metres.
    meaning: pbs:fire_property_escape_sign_mounting_height

```
</details>

</div>