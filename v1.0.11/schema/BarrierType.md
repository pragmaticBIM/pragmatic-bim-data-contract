---
search:
  boost: 2.0
---


# Enum: BarrierType 




_Classification of safety barriers (fall protection and guiding elements)._



<div data-search-exclude markdown="1">

URI: [pbs:BarrierType](https://schema.pragmaticbim.ch/BarrierType)

**Enum URI:** [pbs:BarrierType](https://schema.pragmaticbim.ch/BarrierType)


## Permissible Values
| Value | Meaning | Description | Additional Info |
| --- | --- | --- | --- |
| balustrade | ifcowl:IfcRailingTypeEnum.BALUSTRADE | Fall protection at a slab, balcony, or roof edge. | Title: Balustrade<br>|
| guardrail | ifcowl:IfcRailingTypeEnum.GUARDRAIL | Fall protection along a stair, ramp, or landing. | Title: Guardrail<br>|
| handrail | ifcowl:IfcRailingTypeEnum.HANDRAIL | Handrail for guidance and support. | Title: Handrail<br>|
| other | pbs:barrier_type_other | User-defined or unspecified barrier. | Title: Other<br>|




## Slots

| Name | Description |
| ---  | --- |
| [barrier_type](barrier_type.md) | Classification of the safety barrier (balustrade, guardrail, handrail). |










## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch






## LinkML Source

<details>
```yaml
name: BarrierType
description: Classification of safety barriers (fall protection and guiding elements).
from_schema: https://schema.pragmaticbim.ch
rank: 1000
enum_uri: pbs:BarrierType
permissible_values:
  balustrade:
    text: balustrade
    description: Fall protection at a slab, balcony, or roof edge.
    meaning: ifcowl:IfcRailingTypeEnum.BALUSTRADE
    alt_descriptions:
      de:
        source: de
        description: Brüstungsgeländer
    title: Balustrade
  guardrail:
    text: guardrail
    description: Fall protection along a stair, ramp, or landing.
    meaning: ifcowl:IfcRailingTypeEnum.GUARDRAIL
    alt_descriptions:
      de:
        source: de
        description: Absturzsicherung
    title: Guardrail
  handrail:
    text: handrail
    description: Handrail for guidance and support.
    meaning: ifcowl:IfcRailingTypeEnum.HANDRAIL
    alt_descriptions:
      de:
        source: de
        description: Handlauf
    title: Handrail
  other:
    text: other
    description: User-defined or unspecified barrier.
    meaning: pbs:barrier_type_other
    alt_descriptions:
      de:
        source: de
        description: Andere
    title: Other

```
</details>

</div>