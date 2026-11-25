---
search:
  boost: 2.0
---


# Enum: EscapeRouteRole 




_Role of a space on an escape route (VKF 16-15 / 17-15): horizontal route, vertical route, or exit to the open air. Set only on spaces that belong to an escape route._



<div data-search-exclude markdown="1">

URI: [pbs:EscapeRouteRole](https://schema.pragmaticbim.ch/EscapeRouteRole)

**Enum URI:** [pbs:EscapeRouteRole](https://schema.pragmaticbim.ch/EscapeRouteRole)


## Permissible Values
| Value | Meaning | Description | Additional Info |
| --- | --- | --- | --- |
| HORIZONTAL | pbs:escape_route_role_horizontal | Horizontal escape route (for example a corridor or lobby on the escape path). | Title: Horizontal<br>|
| VERTICAL | pbs:escape_route_role_vertical | Vertical escape route (for example a stairwell). | Title: Vertical<br>|
| EXIT | pbs:escape_route_role_exit | Exit to the open air or equivalent end of the escape route. | Title: Exit<br>|




## Slots

| Name | Description |
| ---  | --- |
| [escape_route_role](escape_route_role.md) | Role of this space on an escape route: horizontal, vertical, or exit to the open air. Unset when the space is not part of an escape route. From ePset_Space.EscapeRouteRole; shared by VKF 16-15 and 17-15 checks. |










## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch






## LinkML Source

<details>
```yaml
name: EscapeRouteRole
description: 'Role of a space on an escape route (VKF 16-15 / 17-15): horizontal route,
  vertical route, or exit to the open air. Set only on spaces that belong to an escape
  route.'
from_schema: https://schema.pragmaticbim.ch
rank: 1000
enum_uri: pbs:EscapeRouteRole
permissible_values:
  HORIZONTAL:
    text: HORIZONTAL
    description: Horizontal escape route (for example a corridor or lobby on the escape
      path).
    meaning: pbs:escape_route_role_horizontal
    alt_descriptions:
      de:
        source: de
        description: Horizontal
    title: Horizontal
  VERTICAL:
    text: VERTICAL
    description: Vertical escape route (for example a stairwell).
    meaning: pbs:escape_route_role_vertical
    alt_descriptions:
      de:
        source: de
        description: Vertikal
    title: Vertical
  EXIT:
    text: EXIT
    description: Exit to the open air or equivalent end of the escape route.
    meaning: pbs:escape_route_role_exit
    alt_descriptions:
      de:
        source: de
        description: Ausgang
    title: Exit

```
</details>

</div>