---
search:
  boost: 5.0
---

# Slot: requirement_property_key 


_Canonical performance key for the target (for example u_value, resistance_rating, airborne_sound_rating_db, seismic_structure_class, gwp_embodied). Either a permissible value of a PerformanceProperty key enum, matched against Entity.performance_properties property_key, or an entity slot name such as is_heated._

__



<div data-search-exclude markdown="1">



URI: [pbs:requirement_property_key](https://schema.pragmaticbim.ch/requirement_property_key)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [PerformanceRequirement](PerformanceRequirement.md) | Performance target requirement (U-value, fire rating, airflow, acoustic, etc.). Boolean targets use target_value_boolean with requirement_property_key aligned to entity slot names where applicable (for example is_heated on Space). Numeric and textual targets use a permissible value of a PerformanceProperty key enum (FirePropertyKey, AcousticPropertyKey, ThermalPropertyKey, StructuralPropertyKey, IndoorEnvironmentPropertyKey, EnvironmentalPropertyKey, SecurityPropertyKey, MaterialPropertyKey) as requirement_property_key. Application pipelines compare the subject entity slot, or the performance_properties entry with the same property_key, to the requirement target and record the outcome as MatchChange (match_status met, unmet, or unknown; unknown when the subject has no value). |  no  |
| [IdentificationRequirement](IdentificationRequirement.md) | Identification or classification value the subject must carry (predefined type, long name, area category, interior or exterior). States what the subject is, not how it performs (PerformanceRequirement) or what it is made of (MaterialRequirement). |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [PerformanceRequirement](PerformanceRequirement.md), [IdentificationRequirement](IdentificationRequirement.md) |

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
| self | pbs:requirement_property_key |
| native | pbs:requirement_property_key |




## LinkML Source

<details>
```yaml
name: requirement_property_key
description: 'Canonical performance key for the target (for example u_value, resistance_rating,
  airborne_sound_rating_db, seismic_structure_class, gwp_embodied). Either a permissible
  value of a PerformanceProperty key enum, matched against Entity.performance_properties
  property_key, or an entity slot name such as is_heated.

  '
from_schema: https://schema.pragmaticbim.ch
rank: 1000
domain_of:
- PerformanceRequirement
- IdentificationRequirement
range: string
required: true

```
</details></div>