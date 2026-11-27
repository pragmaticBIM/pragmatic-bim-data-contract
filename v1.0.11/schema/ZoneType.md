---
search:
  boost: 2.0
---


# Enum: ZoneType 




_Classification of zone purpose and organizational intent._



<div data-search-exclude markdown="1">

URI: [pbs:ZoneType](https://schema.pragmaticbim.ch/ZoneType)

**Enum URI:** [pbs:ZoneType](https://schema.pragmaticbim.ch/ZoneType)


## Permissible Values
| Value | Meaning | Description | Additional Info |
| --- | --- | --- | --- |
| occupancy_unit | pbs:zone_type_occupancy_unit | Occupancy unit zone (for example apartment, office suite, or retail unit). | Title: Occupancy Unit<br>|
| tenant | pbs:zone_type_tenant | Tenant area zone used for leasing and occupancy boundaries. | Title: Tenant<br>|
| functional | pbs:zone_type_functional | Functional grouping zone (for example clinical, retail, office support). | Title: Functional<br>|
| cost | pbs:zone_type_cost | Cost grouping zone for estimation and controlling. | Title: Cost<br>|
| fire | pbs:zone_type_fire | Fire compartment or fire strategy grouping zone. | Title: Fire<br>|
| security | pbs:zone_type_security | Security management zone for access control and surveillance planning. | Title: Security<br>|




## Slots

| Name | Description |
| ---  | --- |
| [zone_type](zone_type.md) | Optional zone classification; intended for SpatialContext nodes where context_type is zone. |










## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch






## LinkML Source

<details>
```yaml
name: ZoneType
description: Classification of zone purpose and organizational intent.
from_schema: https://schema.pragmaticbim.ch
rank: 1000
enum_uri: pbs:ZoneType
permissible_values:
  occupancy_unit:
    text: occupancy_unit
    description: Occupancy unit zone (for example apartment, office suite, or retail
      unit).
    meaning: pbs:zone_type_occupancy_unit
    alt_descriptions:
      de:
        source: de
        description: Nutzungseinheit
    title: Occupancy Unit
  tenant:
    text: tenant
    description: Tenant area zone used for leasing and occupancy boundaries.
    meaning: pbs:zone_type_tenant
    alt_descriptions:
      de:
        source: de
        description: Mieter
    title: Tenant
  functional:
    text: functional
    description: Functional grouping zone (for example clinical, retail, office support).
    meaning: pbs:zone_type_functional
    alt_descriptions:
      de:
        source: de
        description: Funktional
    title: Functional
  cost:
    text: cost
    description: Cost grouping zone for estimation and controlling.
    meaning: pbs:zone_type_cost
    alt_descriptions:
      de:
        source: de
        description: Kosten
    title: Cost
  fire:
    text: fire
    description: Fire compartment or fire strategy grouping zone.
    meaning: pbs:zone_type_fire
    alt_descriptions:
      de:
        source: de
        description: Brandschutz
    title: Fire
  security:
    text: security
    description: Security management zone for access control and surveillance planning.
    meaning: pbs:zone_type_security
    alt_descriptions:
      de:
        source: de
        description: Sicherheit
    title: Security

```
</details>

</div>