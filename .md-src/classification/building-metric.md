# Abstract building metrics

Source: [`building-metrics.skos.ttl`](sources/building-metric.ttl)

## Scheme

- **definition (en):** Semantic definitions for building-level area, volume, and count metrics. Scope variants (above/below ground) are narrower concepts; calculation logic lives in application pipelines.
- **prefLabel (de):** Abstrakte Gebaeudemetriken
- **prefLabel (en):** Abstract building metrics
- **title (en):** Abstract building metrics

## Hierarchy

```mermaid
classDiagram
direction TB
class n_total_circulation_area["total_circulation_area: Total circulation area"]
class n_total_circulation_area_above_ground["total_circulation_area_above_ground: Total circulation area above ground"]
class n_total_circulation_area_below_ground["total_circulation_area_below_ground: Total circulation area below ground"]
class n_total_construction_floor_area["total_construction_floor_area: Total construction floor area"]
class n_total_construction_floor_area_above_ground["total_construction_floor_area_above_ground: Total construction floor area above ground"]
class n_total_construction_floor_area_below_ground["total_construction_floor_area_below_ground: Total construction floor area below ground"]
class n_total_exterior_door_area["total_exterior_door_area: Total exterior door area"]
class n_total_exterior_door_area_above_ground["total_exterior_door_area_above_ground: Total exterior door area above ground"]
class n_total_exterior_door_area_below_ground["total_exterior_door_area_below_ground: Total exterior door area below ground"]
class n_total_exterior_window_area["total_exterior_window_area: Total exterior window area"]
class n_total_exterior_window_area_above_ground["total_exterior_window_area_above_ground: Total exterior window area above ground"]
class n_total_exterior_window_area_below_ground["total_exterior_window_area_below_ground: Total exterior window area below ground"]
class n_total_gross_building_volume["total_gross_building_volume: Total gross building volume"]
class n_total_gross_building_volume_above_ground["total_gross_building_volume_above_ground: Total gross building volume above ground"]
class n_total_gross_building_volume_below_ground["total_gross_building_volume_below_ground: Total gross building volume below ground"]
class n_total_gross_floor_area["total_gross_floor_area: Total gross floor area"]
class n_total_gross_floor_area_above_ground["total_gross_floor_area_above_ground: Total gross floor area above ground"]
class n_total_gross_floor_area_below_ground["total_gross_floor_area_below_ground: Total gross floor area below ground"]
class n_total_main_usable_area["total_main_usable_area: Total main usable area"]
class n_total_main_usable_area_above_ground["total_main_usable_area_above_ground: Total main usable area above ground"]
class n_total_main_usable_area_below_ground["total_main_usable_area_below_ground: Total main usable area below ground"]
class n_total_net_building_volume["total_net_building_volume: Total net building volume"]
class n_total_net_building_volume_above_ground["total_net_building_volume_above_ground: Total net building volume above ground"]
class n_total_net_building_volume_below_ground["total_net_building_volume_below_ground: Total net building volume below ground"]
class n_total_net_floor_area["total_net_floor_area: Total net floor area"]
class n_total_net_floor_area_above_ground["total_net_floor_area_above_ground: Total net floor area above ground"]
class n_total_net_floor_area_below_ground["total_net_floor_area_below_ground: Total net floor area below ground"]
class n_total_roof_area["total_roof_area: Total roof area"]
class n_total_roof_area_above_ground["total_roof_area_above_ground: Total roof area above ground"]
class n_total_roof_area_below_ground["total_roof_area_below_ground: Total roof area below ground"]
class n_total_secondary_usable_area["total_secondary_usable_area: Total secondary usable area"]
class n_total_secondary_usable_area_above_ground["total_secondary_usable_area_above_ground: Total secondary usable area above ground"]
class n_total_secondary_usable_area_below_ground["total_secondary_usable_area_below_ground: Total secondary usable area below ground"]
class n_total_soffit_area["total_soffit_area: Total soffit area"]
class n_total_soffit_area_above_ground["total_soffit_area_above_ground: Total soffit area above ground"]
class n_total_soffit_area_below_ground["total_soffit_area_below_ground: Total soffit area below ground"]
class n_total_storey_count["total_storey_count: Total storey count"]
class n_total_storey_count_above_ground["total_storey_count_above_ground: Total storey count above ground"]
class n_total_storey_count_below_ground["total_storey_count_below_ground: Total storey count below ground"]
class n_total_technical_area["total_technical_area: Total technical area"]
class n_total_technical_area_above_ground["total_technical_area_above_ground: Total technical area above ground"]
class n_total_technical_area_below_ground["total_technical_area_below_ground: Total technical area below ground"]
class n_total_vertical_facade_area["total_vertical_facade_area: Total vertical facade area"]
class n_total_vertical_facade_area_above_ground["total_vertical_facade_area_above_ground: Total vertical facade area above ground"]
class n_total_vertical_facade_area_below_ground["total_vertical_facade_area_below_ground: Total vertical facade area below ground"]
n_total_circulation_area <|-- n_total_circulation_area_above_ground
n_total_circulation_area <|-- n_total_circulation_area_below_ground
n_total_construction_floor_area <|-- n_total_construction_floor_area_above_ground
n_total_construction_floor_area <|-- n_total_construction_floor_area_below_ground
n_total_exterior_door_area <|-- n_total_exterior_door_area_above_ground
n_total_exterior_door_area <|-- n_total_exterior_door_area_below_ground
n_total_exterior_window_area <|-- n_total_exterior_window_area_above_ground
n_total_exterior_window_area <|-- n_total_exterior_window_area_below_ground
n_total_gross_building_volume <|-- n_total_gross_building_volume_above_ground
n_total_gross_building_volume <|-- n_total_gross_building_volume_below_ground
n_total_gross_floor_area <|-- n_total_gross_floor_area_above_ground
n_total_gross_floor_area <|-- n_total_gross_floor_area_below_ground
n_total_main_usable_area <|-- n_total_main_usable_area_above_ground
n_total_main_usable_area <|-- n_total_main_usable_area_below_ground
n_total_net_building_volume <|-- n_total_net_building_volume_above_ground
n_total_net_building_volume <|-- n_total_net_building_volume_below_ground
n_total_net_floor_area <|-- n_total_net_floor_area_above_ground
n_total_net_floor_area <|-- n_total_net_floor_area_below_ground
n_total_roof_area <|-- n_total_roof_area_above_ground
n_total_roof_area <|-- n_total_roof_area_below_ground
n_total_secondary_usable_area <|-- n_total_secondary_usable_area_above_ground
n_total_secondary_usable_area <|-- n_total_secondary_usable_area_below_ground
n_total_soffit_area <|-- n_total_soffit_area_above_ground
n_total_soffit_area <|-- n_total_soffit_area_below_ground
n_total_storey_count <|-- n_total_storey_count_above_ground
n_total_storey_count <|-- n_total_storey_count_below_ground
n_total_technical_area <|-- n_total_technical_area_above_ground
n_total_technical_area <|-- n_total_technical_area_below_ground
n_total_vertical_facade_area <|-- n_total_vertical_facade_area_above_ground
n_total_vertical_facade_area <|-- n_total_vertical_facade_area_below_ground
```

## Concepts

<div class="pbs-vocab-concepts" data-default-lang="en" data-active-lang="en">
<div class="pbs-lang-switcher" role="group" aria-label="Language">
<button type="button" class="pbs-lang-btn" data-lang="de">DE</button>
<button type="button" class="pbs-lang-btn" data-lang="en">EN</button>
</div>
<table>
<thead>
<tr>
<th>Notation</th>
<th>Broader</th>
<th class="pbs-lang-col" data-lang="de" data-field="label">Label</th>
<th class="pbs-lang-col" data-lang="de" data-field="definition">Definition</th>
<th class="pbs-lang-col" data-lang="de" data-field="description">Description</th>
<th class="pbs-lang-col" data-lang="de" data-field="scope_note">Scope note</th>
<th class="pbs-lang-col" data-lang="en" data-field="label">Label</th>
<th class="pbs-lang-col" data-lang="en" data-field="definition">Definition</th>
<th class="pbs-lang-col" data-lang="en" data-field="description">Description</th>
<th class="pbs-lang-col" data-lang="en" data-field="scope_note">Scope note</th>
</tr>
</thead>
<tbody>
<tr>
<td>total_circulation_area</td>
<td></td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Gesamte Verkehrsflaeche</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition"></td>
<td class="pbs-lang-col" data-lang="de" data-field="description"></td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Total circulation area</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Sum of circulation area (Verkehrsflaeche, VF per SIA 416) derived from spaces classified as circulation area: floor area for horizontal and vertical access such as corridors, stairs, and lift shafts.</td>
<td class="pbs-lang-col" data-lang="en" data-field="description">Equals SIA 416 VF. Derived from spaces by SIA 416 class; calculation logic lives in application pipelines.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>total_circulation_area_above_ground</td>
<td>total_circulation_area</td>
<td class="pbs-lang-col" data-lang="de" data-field="label"></td>
<td class="pbs-lang-col" data-lang="de" data-field="definition"></td>
<td class="pbs-lang-col" data-lang="de" data-field="description"></td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Total circulation area above ground</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Circulation area (SIA 416 VF) of spaces above ground level.</td>
<td class="pbs-lang-col" data-lang="en" data-field="description"></td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>total_circulation_area_below_ground</td>
<td>total_circulation_area</td>
<td class="pbs-lang-col" data-lang="de" data-field="label"></td>
<td class="pbs-lang-col" data-lang="de" data-field="definition"></td>
<td class="pbs-lang-col" data-lang="de" data-field="description"></td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Total circulation area below ground</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Circulation area (SIA 416 VF) of spaces below ground level.</td>
<td class="pbs-lang-col" data-lang="en" data-field="description"></td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>total_construction_floor_area</td>
<td></td>
<td class="pbs-lang-col" data-lang="de" data-field="label"></td>
<td class="pbs-lang-col" data-lang="de" data-field="definition"></td>
<td class="pbs-lang-col" data-lang="de" data-field="description"></td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Total construction floor area</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Floor area occupied by enclosing and internal construction elements (shell zone between gross and net).</td>
<td class="pbs-lang-col" data-lang="en" data-field="description">Semantic composite; close to SIA 416 KF (Konstruktionsflaeche) and DIN 277 KGF.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>total_construction_floor_area_above_ground</td>
<td>total_construction_floor_area</td>
<td class="pbs-lang-col" data-lang="de" data-field="label"></td>
<td class="pbs-lang-col" data-lang="de" data-field="definition"></td>
<td class="pbs-lang-col" data-lang="de" data-field="description"></td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Total construction floor area above ground</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition"></td>
<td class="pbs-lang-col" data-lang="en" data-field="description"></td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>total_construction_floor_area_below_ground</td>
<td>total_construction_floor_area</td>
<td class="pbs-lang-col" data-lang="de" data-field="label"></td>
<td class="pbs-lang-col" data-lang="de" data-field="definition"></td>
<td class="pbs-lang-col" data-lang="de" data-field="description"></td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Total construction floor area below ground</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition"></td>
<td class="pbs-lang-col" data-lang="en" data-field="description"></td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>total_envelope_area</td>
<td></td>
<td class="pbs-lang-col" data-lang="de" data-field="label"></td>
<td class="pbs-lang-col" data-lang="de" data-field="definition"></td>
<td class="pbs-lang-col" data-lang="de" data-field="description"></td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Total envelope area</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Semantic composite of opaque facade, windows, doors, roof, and soffit areas forming the thermal envelope.</td>
<td class="pbs-lang-col" data-lang="en" data-field="description"></td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>total_exterior_door_area</td>
<td></td>
<td class="pbs-lang-col" data-lang="de" data-field="label"></td>
<td class="pbs-lang-col" data-lang="de" data-field="definition"></td>
<td class="pbs-lang-col" data-lang="de" data-field="description"></td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Total exterior door area</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Total area of exterior doors.</td>
<td class="pbs-lang-col" data-lang="en" data-field="description"></td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>total_exterior_door_area_above_ground</td>
<td>total_exterior_door_area</td>
<td class="pbs-lang-col" data-lang="de" data-field="label"></td>
<td class="pbs-lang-col" data-lang="de" data-field="definition"></td>
<td class="pbs-lang-col" data-lang="de" data-field="description"></td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Total exterior door area above ground</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition"></td>
<td class="pbs-lang-col" data-lang="en" data-field="description"></td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>total_exterior_door_area_below_ground</td>
<td>total_exterior_door_area</td>
<td class="pbs-lang-col" data-lang="de" data-field="label"></td>
<td class="pbs-lang-col" data-lang="de" data-field="definition"></td>
<td class="pbs-lang-col" data-lang="de" data-field="description"></td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Total exterior door area below ground</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition"></td>
<td class="pbs-lang-col" data-lang="en" data-field="description"></td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>total_exterior_floor_area</td>
<td></td>
<td class="pbs-lang-col" data-lang="de" data-field="label"></td>
<td class="pbs-lang-col" data-lang="de" data-field="definition"></td>
<td class="pbs-lang-col" data-lang="de" data-field="description"></td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Total exterior floor area</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Horizontal floor area of exterior or open covered spaces.</td>
<td class="pbs-lang-col" data-lang="en" data-field="description">Close to SIA 416 AGF (Aussen-Geschossflaeche).</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>total_exterior_window_area</td>
<td></td>
<td class="pbs-lang-col" data-lang="de" data-field="label"></td>
<td class="pbs-lang-col" data-lang="de" data-field="definition"></td>
<td class="pbs-lang-col" data-lang="de" data-field="description"></td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Total exterior window area</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Total glazed area of exterior windows.</td>
<td class="pbs-lang-col" data-lang="en" data-field="description"></td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>total_exterior_window_area_above_ground</td>
<td>total_exterior_window_area</td>
<td class="pbs-lang-col" data-lang="de" data-field="label"></td>
<td class="pbs-lang-col" data-lang="de" data-field="definition"></td>
<td class="pbs-lang-col" data-lang="de" data-field="description"></td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Total exterior window area above ground</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition"></td>
<td class="pbs-lang-col" data-lang="en" data-field="description"></td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>total_exterior_window_area_below_ground</td>
<td>total_exterior_window_area</td>
<td class="pbs-lang-col" data-lang="de" data-field="label"></td>
<td class="pbs-lang-col" data-lang="de" data-field="definition"></td>
<td class="pbs-lang-col" data-lang="de" data-field="description"></td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Total exterior window area below ground</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition"></td>
<td class="pbs-lang-col" data-lang="en" data-field="description"></td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>total_gross_building_volume</td>
<td></td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Gesamtes Gebaeudevolumen</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition"></td>
<td class="pbs-lang-col" data-lang="de" data-field="description"></td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Total gross building volume</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Gross enclosed building volume measured to outer boundaries of enclosing elements.</td>
<td class="pbs-lang-col" data-lang="en" data-field="description">Close to SIA 416 GV (Gebaeudevolumen).</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>total_gross_building_volume_above_ground</td>
<td>total_gross_building_volume</td>
<td class="pbs-lang-col" data-lang="de" data-field="label"></td>
<td class="pbs-lang-col" data-lang="de" data-field="definition"></td>
<td class="pbs-lang-col" data-lang="de" data-field="description"></td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Total gross building volume above ground</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition"></td>
<td class="pbs-lang-col" data-lang="en" data-field="description"></td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>total_gross_building_volume_below_ground</td>
<td>total_gross_building_volume</td>
<td class="pbs-lang-col" data-lang="de" data-field="label"></td>
<td class="pbs-lang-col" data-lang="de" data-field="definition"></td>
<td class="pbs-lang-col" data-lang="de" data-field="description"></td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Total gross building volume below ground</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition"></td>
<td class="pbs-lang-col" data-lang="en" data-field="description"></td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>total_gross_floor_area</td>
<td></td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Gesamte Bruttogeschossflaeche</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition"></td>
<td class="pbs-lang-col" data-lang="de" data-field="description"></td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Total gross floor area</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">All-side enclosed and covered floor area of accessible storeys including construction areas, measured to outer boundaries.</td>
<td class="pbs-lang-col" data-lang="en" data-field="description">Close to SIA 416 GF (Geschossflaeche) and DIN 277 BGF.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>total_gross_floor_area_above_ground</td>
<td>total_gross_floor_area</td>
<td class="pbs-lang-col" data-lang="de" data-field="label"></td>
<td class="pbs-lang-col" data-lang="de" data-field="definition"></td>
<td class="pbs-lang-col" data-lang="de" data-field="description"></td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Total gross floor area above ground</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Gross floor area of storeys above ground level.</td>
<td class="pbs-lang-col" data-lang="en" data-field="description"></td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>total_gross_floor_area_below_ground</td>
<td>total_gross_floor_area</td>
<td class="pbs-lang-col" data-lang="de" data-field="label"></td>
<td class="pbs-lang-col" data-lang="de" data-field="definition"></td>
<td class="pbs-lang-col" data-lang="de" data-field="description"></td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Total gross floor area below ground</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Gross floor area of storeys below ground level.</td>
<td class="pbs-lang-col" data-lang="en" data-field="description"></td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>total_main_usable_area</td>
<td></td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Gesamte Hauptnutzflaeche</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition"></td>
<td class="pbs-lang-col" data-lang="de" data-field="description"></td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Total main usable area</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Sum of main usable area (Hauptnutzflaeche, HNF per SIA 416) derived from spaces classified as main usable area: floor area serving the primary purpose of use of the building.</td>
<td class="pbs-lang-col" data-lang="en" data-field="description">Equals SIA 416 HNF. Derived from spaces by SIA 416 class; calculation logic lives in application pipelines.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>total_main_usable_area_above_ground</td>
<td>total_main_usable_area</td>
<td class="pbs-lang-col" data-lang="de" data-field="label"></td>
<td class="pbs-lang-col" data-lang="de" data-field="definition"></td>
<td class="pbs-lang-col" data-lang="de" data-field="description"></td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Total main usable area above ground</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Main usable area (SIA 416 HNF) of spaces above ground level.</td>
<td class="pbs-lang-col" data-lang="en" data-field="description"></td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>total_main_usable_area_below_ground</td>
<td>total_main_usable_area</td>
<td class="pbs-lang-col" data-lang="de" data-field="label"></td>
<td class="pbs-lang-col" data-lang="de" data-field="definition"></td>
<td class="pbs-lang-col" data-lang="de" data-field="description"></td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Total main usable area below ground</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Main usable area (SIA 416 HNF) of spaces below ground level.</td>
<td class="pbs-lang-col" data-lang="en" data-field="description"></td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>total_net_building_volume</td>
<td></td>
<td class="pbs-lang-col" data-lang="de" data-field="label"></td>
<td class="pbs-lang-col" data-lang="de" data-field="definition"></td>
<td class="pbs-lang-col" data-lang="de" data-field="description"></td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Total net building volume</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Net enclosed volume between internal faces of enclosing construction elements.</td>
<td class="pbs-lang-col" data-lang="en" data-field="description">Close to DIN 277 net volume / ISO 9836 net volume concepts.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>total_net_building_volume_above_ground</td>
<td>total_net_building_volume</td>
<td class="pbs-lang-col" data-lang="de" data-field="label"></td>
<td class="pbs-lang-col" data-lang="de" data-field="definition"></td>
<td class="pbs-lang-col" data-lang="de" data-field="description"></td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Total net building volume above ground</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition"></td>
<td class="pbs-lang-col" data-lang="en" data-field="description"></td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>total_net_building_volume_below_ground</td>
<td>total_net_building_volume</td>
<td class="pbs-lang-col" data-lang="de" data-field="label"></td>
<td class="pbs-lang-col" data-lang="de" data-field="definition"></td>
<td class="pbs-lang-col" data-lang="de" data-field="description"></td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Total net building volume below ground</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition"></td>
<td class="pbs-lang-col" data-lang="en" data-field="description"></td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>total_net_floor_area</td>
<td></td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Gesamte Nettogeschossflaeche</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition"></td>
<td class="pbs-lang-col" data-lang="de" data-field="description"></td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Total net floor area</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Net floor area between enclosing construction elements, excluding construction thickness.</td>
<td class="pbs-lang-col" data-lang="en" data-field="description">Close to SIA 416 NGF and DIN 277 NRF.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>total_net_floor_area_above_ground</td>
<td>total_net_floor_area</td>
<td class="pbs-lang-col" data-lang="de" data-field="label"></td>
<td class="pbs-lang-col" data-lang="de" data-field="definition"></td>
<td class="pbs-lang-col" data-lang="de" data-field="description"></td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Total net floor area above ground</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Net floor area above ground level.</td>
<td class="pbs-lang-col" data-lang="en" data-field="description"></td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>total_net_floor_area_below_ground</td>
<td>total_net_floor_area</td>
<td class="pbs-lang-col" data-lang="de" data-field="label"></td>
<td class="pbs-lang-col" data-lang="de" data-field="definition"></td>
<td class="pbs-lang-col" data-lang="de" data-field="description"></td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Total net floor area below ground</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Net floor area below ground level.</td>
<td class="pbs-lang-col" data-lang="en" data-field="description"></td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>total_roof_area</td>
<td></td>
<td class="pbs-lang-col" data-lang="de" data-field="label"></td>
<td class="pbs-lang-col" data-lang="de" data-field="definition"></td>
<td class="pbs-lang-col" data-lang="de" data-field="description"></td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Total roof area</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Horizontal projection or net area of roof surfaces.</td>
<td class="pbs-lang-col" data-lang="en" data-field="description"></td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>total_roof_area_above_ground</td>
<td>total_roof_area</td>
<td class="pbs-lang-col" data-lang="de" data-field="label"></td>
<td class="pbs-lang-col" data-lang="de" data-field="definition"></td>
<td class="pbs-lang-col" data-lang="de" data-field="description"></td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Total roof area above ground</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition"></td>
<td class="pbs-lang-col" data-lang="en" data-field="description"></td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>total_roof_area_below_ground</td>
<td>total_roof_area</td>
<td class="pbs-lang-col" data-lang="de" data-field="label"></td>
<td class="pbs-lang-col" data-lang="de" data-field="definition"></td>
<td class="pbs-lang-col" data-lang="de" data-field="description"></td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Total roof area below ground</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition"></td>
<td class="pbs-lang-col" data-lang="en" data-field="description"></td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>total_secondary_usable_area</td>
<td></td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Gesamte Nebennutzflaeche</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition"></td>
<td class="pbs-lang-col" data-lang="de" data-field="description"></td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Total secondary usable area</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Sum of secondary usable area (Nebennutzflaeche, NNF per SIA 416) derived from spaces classified as secondary usable area: floor area supporting but not serving the primary purpose of use, such as storage, cellar, and bicycle rooms.</td>
<td class="pbs-lang-col" data-lang="en" data-field="description">Equals SIA 416 NNF. Derived from spaces by SIA 416 class; calculation logic lives in application pipelines.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>total_secondary_usable_area_above_ground</td>
<td>total_secondary_usable_area</td>
<td class="pbs-lang-col" data-lang="de" data-field="label"></td>
<td class="pbs-lang-col" data-lang="de" data-field="definition"></td>
<td class="pbs-lang-col" data-lang="de" data-field="description"></td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Total secondary usable area above ground</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Secondary usable area (SIA 416 NNF) of spaces above ground level.</td>
<td class="pbs-lang-col" data-lang="en" data-field="description"></td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>total_secondary_usable_area_below_ground</td>
<td>total_secondary_usable_area</td>
<td class="pbs-lang-col" data-lang="de" data-field="label"></td>
<td class="pbs-lang-col" data-lang="de" data-field="definition"></td>
<td class="pbs-lang-col" data-lang="de" data-field="description"></td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Total secondary usable area below ground</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Secondary usable area (SIA 416 NNF) of spaces below ground level.</td>
<td class="pbs-lang-col" data-lang="en" data-field="description"></td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>total_soffit_area</td>
<td></td>
<td class="pbs-lang-col" data-lang="de" data-field="label"></td>
<td class="pbs-lang-col" data-lang="de" data-field="definition"></td>
<td class="pbs-lang-col" data-lang="de" data-field="description"></td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Total soffit area</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Area of underside / soffit surfaces forming part of the building envelope.</td>
<td class="pbs-lang-col" data-lang="en" data-field="description"></td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>total_soffit_area_above_ground</td>
<td>total_soffit_area</td>
<td class="pbs-lang-col" data-lang="de" data-field="label"></td>
<td class="pbs-lang-col" data-lang="de" data-field="definition"></td>
<td class="pbs-lang-col" data-lang="de" data-field="description"></td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Total soffit area above ground</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition"></td>
<td class="pbs-lang-col" data-lang="en" data-field="description"></td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>total_soffit_area_below_ground</td>
<td>total_soffit_area</td>
<td class="pbs-lang-col" data-lang="de" data-field="label"></td>
<td class="pbs-lang-col" data-lang="de" data-field="definition"></td>
<td class="pbs-lang-col" data-lang="de" data-field="description"></td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Total soffit area below ground</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition"></td>
<td class="pbs-lang-col" data-lang="en" data-field="description"></td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>total_storey_count</td>
<td></td>
<td class="pbs-lang-col" data-lang="de" data-field="label"></td>
<td class="pbs-lang-col" data-lang="de" data-field="definition"></td>
<td class="pbs-lang-col" data-lang="de" data-field="description"></td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Total storey count</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Count of building storeys included in the measured scope.</td>
<td class="pbs-lang-col" data-lang="en" data-field="description"></td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>total_storey_count_above_ground</td>
<td>total_storey_count</td>
<td class="pbs-lang-col" data-lang="de" data-field="label"></td>
<td class="pbs-lang-col" data-lang="de" data-field="definition"></td>
<td class="pbs-lang-col" data-lang="de" data-field="description"></td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Total storey count above ground</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition"></td>
<td class="pbs-lang-col" data-lang="en" data-field="description"></td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>total_storey_count_below_ground</td>
<td>total_storey_count</td>
<td class="pbs-lang-col" data-lang="de" data-field="label"></td>
<td class="pbs-lang-col" data-lang="de" data-field="definition"></td>
<td class="pbs-lang-col" data-lang="de" data-field="description"></td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Total storey count below ground</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition"></td>
<td class="pbs-lang-col" data-lang="en" data-field="description"></td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>total_technical_area</td>
<td></td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Gesamte Funktionsflaeche</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition"></td>
<td class="pbs-lang-col" data-lang="de" data-field="description"></td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Total technical area</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Sum of technical area (Funktionsflaeche, FF per SIA 416) derived from spaces classified as technical area: floor area for building services installations and plant rooms.</td>
<td class="pbs-lang-col" data-lang="en" data-field="description">Equals SIA 416 FF. Derived from spaces by SIA 416 class; calculation logic lives in application pipelines.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>total_technical_area_above_ground</td>
<td>total_technical_area</td>
<td class="pbs-lang-col" data-lang="de" data-field="label"></td>
<td class="pbs-lang-col" data-lang="de" data-field="definition"></td>
<td class="pbs-lang-col" data-lang="de" data-field="description"></td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Total technical area above ground</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Technical area (SIA 416 FF) of spaces above ground level.</td>
<td class="pbs-lang-col" data-lang="en" data-field="description"></td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>total_technical_area_below_ground</td>
<td>total_technical_area</td>
<td class="pbs-lang-col" data-lang="de" data-field="label"></td>
<td class="pbs-lang-col" data-lang="de" data-field="definition"></td>
<td class="pbs-lang-col" data-lang="de" data-field="description"></td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Total technical area below ground</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Technical area (SIA 416 FF) of spaces below ground level.</td>
<td class="pbs-lang-col" data-lang="en" data-field="description"></td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>total_vertical_facade_area</td>
<td></td>
<td class="pbs-lang-col" data-lang="de" data-field="label"></td>
<td class="pbs-lang-col" data-lang="de" data-field="definition"></td>
<td class="pbs-lang-col" data-lang="de" data-field="description"></td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Total vertical facade area</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Net vertical area of exterior cladding and opaque facade surfaces.</td>
<td class="pbs-lang-col" data-lang="en" data-field="description"></td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>total_vertical_facade_area_above_ground</td>
<td>total_vertical_facade_area</td>
<td class="pbs-lang-col" data-lang="de" data-field="label"></td>
<td class="pbs-lang-col" data-lang="de" data-field="definition"></td>
<td class="pbs-lang-col" data-lang="de" data-field="description"></td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Total vertical facade area above ground</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition"></td>
<td class="pbs-lang-col" data-lang="en" data-field="description"></td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>total_vertical_facade_area_below_ground</td>
<td>total_vertical_facade_area</td>
<td class="pbs-lang-col" data-lang="de" data-field="label"></td>
<td class="pbs-lang-col" data-lang="de" data-field="definition"></td>
<td class="pbs-lang-col" data-lang="de" data-field="description"></td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Total vertical facade area below ground</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition"></td>
<td class="pbs-lang-col" data-lang="en" data-field="description"></td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
</tbody>
</table>
</div>
