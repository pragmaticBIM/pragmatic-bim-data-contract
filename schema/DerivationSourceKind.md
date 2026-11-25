---
search:
  boost: 2.0
---


# Enum: DerivationSourceKind 




_Kind of source a derived value or relation comes from. Used by Derivation.derivation_source_kind._



<div data-search-exclude markdown="1">

URI: [pbs:DerivationSourceKind](https://schema.pragmaticbim.ch/DerivationSourceKind)

**Enum URI:** [pbs:DerivationSourceKind](https://schema.pragmaticbim.ch/DerivationSourceKind)


## Permissible Values
| Value | Meaning | Description | Additional Info |
| --- | --- | --- | --- |
| ifc_explicit | pbs:derivation_source_kind_ifc_explicit | Read directly from an explicit IFC relationship object or property set, without computation. | Title: IFC explicit<br>|
| ifc_geometry | pbs:derivation_source_kind_ifc_geometry | Computed from IFC geometry (for example contact, containment in a void, height above a reference surface, spacing along an axis, surface slope). | Title: IFC geometry<br>|
| project_parameter | pbs:derivation_source_kind_project_parameter | Taken from project-level parameters outside the model (for example traffic volumes from the project basis). | Title: Project parameter<br>|
| manual | pbs:derivation_source_kind_manual | Entered or confirmed manually by a person. | Title: Manual<br>|




## Slots

| Name | Description |
| ---  | --- |
| [derivation_source_kind](derivation_source_kind.md) | Kind of source the value or relation comes from (IFC relationship or property, geometry computation, project parameter, manual entry). |










## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch






## LinkML Source

<details>
```yaml
name: DerivationSourceKind
description: Kind of source a derived value or relation comes from. Used by Derivation.derivation_source_kind.
from_schema: https://schema.pragmaticbim.ch
rank: 1000
enum_uri: pbs:DerivationSourceKind
permissible_values:
  ifc_explicit:
    text: ifc_explicit
    description: Read directly from an explicit IFC relationship object or property
      set, without computation.
    meaning: pbs:derivation_source_kind_ifc_explicit
    alt_descriptions:
      de:
        source: de
        description: Direkt aus dem IFC
    title: IFC explicit
  ifc_geometry:
    text: ifc_geometry
    description: Computed from IFC geometry (for example contact, containment in a
      void, height above a reference surface, spacing along an axis, surface slope).
    meaning: pbs:derivation_source_kind_ifc_geometry
    alt_descriptions:
      de:
        source: de
        description: Aus der IFC-Geometrie berechnet
    title: IFC geometry
  project_parameter:
    text: project_parameter
    description: Taken from project-level parameters outside the model (for example
      traffic volumes from the project basis).
    meaning: pbs:derivation_source_kind_project_parameter
    alt_descriptions:
      de:
        source: de
        description: Projektparameter
    title: Project parameter
  manual:
    text: manual
    description: Entered or confirmed manually by a person.
    meaning: pbs:derivation_source_kind_manual
    alt_descriptions:
      de:
        source: de
        description: Manuell erfasst
    title: Manual

```
</details>

</div>