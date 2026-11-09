---
search:
  boost: 2.0
---


# Enum: StructuralPropertyKey 




_Canonical structural-related keys derived from IFC PropertySets._



<div data-search-exclude markdown="1">

URI: [pbs:StructuralPropertyKey](https://schema.pragmaticbim.ch/StructuralPropertyKey)

**Enum URI:** [pbs:StructuralPropertyKey](https://schema.pragmaticbim.ch/StructuralPropertyKey)


## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| load_bearing | pbs:structural_property_load_bearing |  |
| stiffness_class | pbs:structural_property_stiffness_class |  |
| strength_class | pbs:structural_property_strength_class |  |
| design_area_load | pbs:structural_property_design_area_load | Imposed design area load in kN/m2. |
| design_point_load | pbs:structural_property_design_point_load | Imposed design point load in kN. |
| vibration_class | pbs:structural_property_vibration_class | Vibration criterion class, for example ISO Residential (Night). |
| seismic_structure_class | pbs:structural_property_seismic_structure_class | Seismic structure class (Bauwerksklasse) I, II, or III under SIA 261. |




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
name: StructuralPropertyKey
description: Canonical structural-related keys derived from IFC PropertySets.
from_schema: https://schema.pragmaticbim.ch
rank: 1000
enum_uri: pbs:StructuralPropertyKey
permissible_values:
  load_bearing:
    text: load_bearing
    meaning: pbs:structural_property_load_bearing
  stiffness_class:
    text: stiffness_class
    meaning: pbs:structural_property_stiffness_class
  strength_class:
    text: strength_class
    meaning: pbs:structural_property_strength_class
  design_area_load:
    text: design_area_load
    description: Imposed design area load in kN/m2.
    meaning: pbs:structural_property_design_area_load
  design_point_load:
    text: design_point_load
    description: Imposed design point load in kN.
    meaning: pbs:structural_property_design_point_load
  vibration_class:
    text: vibration_class
    description: Vibration criterion class, for example ISO Residential (Night).
    meaning: pbs:structural_property_vibration_class
  seismic_structure_class:
    text: seismic_structure_class
    description: Seismic structure class (Bauwerksklasse) I, II, or III under SIA
      261.
    meaning: pbs:structural_property_seismic_structure_class

```
</details>

</div>