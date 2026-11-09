# Abstract cost project types

Source: [`cost-project-types.skos.ttl`](sources/cost-project-type.ttl)

## Scheme

- **definition (de):** Projekt- oder Teilprojektarten als erste Dimension eines Kostenberichts. Gebäude (CPT-01) und Tiefbauwerke (CPT-02 bis CPT-19) teilen dieselben Kostengruppen; Kostenuntergruppen geben an, für welche Projektarten sie gelten. Die Nummerierung entspricht den ICMS-Projektcodes der Ebene 1, sodass ein vollständiger ICMS-Code durch Voranstellen der Projektartnummer gebildet werden kann.
- **definition (en):** Project or sub-project types used as the first dimension of a cost report. Buildings (CPT-01) and civil engineering works (CPT-02 to CPT-19) share the same cost groups; cost sub-groups state the project types they apply to. Numbering is aligned with ICMS Level 1 project codes so that a full ICMS code can be formed by prepending the project type number.
- **prefLabel (de):** Abstrakte Kosten-Projektarten
- **prefLabel (en):** Abstract cost project types
- **title (de):** Abstrakte Kosten-Projektarten
- **title (en):** Abstract cost project types

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
<th class="pbs-lang-col" data-lang="de" data-field="scope_note">Scope note</th>
<th class="pbs-lang-col" data-lang="en" data-field="label">Label</th>
<th class="pbs-lang-col" data-lang="en" data-field="definition">Definition</th>
<th class="pbs-lang-col" data-lang="en" data-field="scope_note">Scope note</th>
</tr>
</thead>
<tbody>
<tr>
<td>CPT-01</td>
<td></td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Gebäude</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Umschlossene Bauwerke, die Personen oder Gütern Schutz bieten, einschliesslich Umgebungsarbeiten.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Buildings</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Enclosed constructions providing shelter for occupants or contents, including their site works.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>CPT-02</td>
<td></td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Strassen und Pisten</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Strassen, Autobahnen sowie Start- und Landebahnen, Rollwege und Vorfelder von Flugplätzen.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Roads and runways</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Road carriageways, highways, airfield runways, taxiways and aprons.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>CPT-03</td>
<td></td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Bahnanlagen</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Eisenbahn-, Stadtbahn-, Tram- und Metrolinien einschliesslich Fahrbahn, Bahnstromversorgung und Sicherungsanlagen.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Railways</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Heavy rail, light rail, tram and metro lines including track, power supply and signalling.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>CPT-04</td>
<td></td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Brücken</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Bauwerke, die einen Verkehrsweg oder eine Leitung über ein Hindernis führen.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Bridges</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Structures carrying a traffic route or utility across an obstacle.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>CPT-05</td>
<td></td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Tunnel</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Unterirdische Bauwerke für Verkehr, Leitungen oder Wasser, im Vortrieb oder im Tagbau erstellt.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Tunnels</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Underground passages for traffic, utilities or water, bored, mined or cut-and-cover.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>CPT-06</td>
<td></td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Abwasserreinigungsanlagen</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Anlagen zur Sammlung, Reinigung und Ableitung von kommunalem und industriellem Abwasser.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Wastewater treatment works</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Plants that collect, treat and discharge sewage and industrial wastewater.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>CPT-07</td>
<td></td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Wasseraufbereitungsanlagen</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Anlagen zur Fassung, Aufbereitung und Speicherung von Trink- oder Brauchwasser.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Water treatment works</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Plants that abstract, treat and store drinking or process water.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>CPT-08</td>
<td></td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Rohrleitungen</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Fern- und Verteilleitungen sowie Kabeltrassen für Wasser, Gas, Öl, Wärme oder Energie.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Pipelines</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Long-distance and distribution pipelines and cable routes for water, gas, oil, heat or energy.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>CPT-09</td>
<td></td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Brunnen und Bohrungen</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Gebohrte oder gegrabene Brunnen und Bohrungen für Wasser, Energie oder Rohstoffe.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Wells and boreholes</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Drilled or dug wells and boreholes for water, energy or resources.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>CPT-10</td>
<td></td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Kraftwerke</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Anlagen zur Erzeugung von Strom oder Wärme aus beliebigen Energieträgern.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Power generation plants</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Plants that generate electricity or heat from any energy source.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>CPT-11</td>
<td></td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Chemieanlagen</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Prozessanlagen zur Herstellung chemischer Stoffe.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Chemical plants</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Process plants producing chemical substances.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>CPT-12</td>
<td></td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Raffinerien</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Prozessanlagen zur Raffination von Rohöl oder anderen Rohstoffen.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Refineries</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Process plants refining crude oil or other raw materials.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>CPT-13</td>
<td></td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Talsperren und Speicherbecken</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Sperrenbauwerke und Becken zum Aufstauen oder Speichern von Wasser.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Dams and reservoirs</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Barriers and basins that impound or store water.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>CPT-14</td>
<td></td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Bergwerke und Steinbrüche</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Ober- oder untertägiger Abbau von Mineralien und Gestein.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Mines and quarries</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Surface or underground extraction of minerals and rock.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>CPT-15</td>
<td></td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Offshore-Bauwerke</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Bauwerke auf offener See wie Plattformen und Fundamente von Windparks.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Offshore works</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Structures in open sea such as platforms and wind farm foundations.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>CPT-16</td>
<td></td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Küstennahe Bauwerke</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Bauwerke im Küstenbereich wie Ufermauern, Wellenbrecher und Auslaufbauwerke.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Near-shore works</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Coastal structures such as seawalls, breakwaters and outfalls.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>CPT-17</td>
<td></td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Häfen</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Hafenanlagen einschliesslich Kais, Liegeplätzen, Terminals und landseitiger Flächen.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Ports</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Harbour facilities including quays, berths, terminals and their land side.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>CPT-18</td>
<td></td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Wasserbau an Gewässern</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Bauwerke an Flüssen, Kanälen und Seen wie Schleusen, Wehre, Uferschutz und Hochwasserschutz.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Waterway works</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Works on rivers, canals and lakes such as locks, weirs, bank protection and flood defence.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>CPT-19</td>
<td></td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Landgewinnung und Geländeaufbau</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Schaffung neuer Landflächen durch Aufschüttung, Baggerung oder Konsolidierung.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Land formation and reclamation</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Creation of new land by filling, dredging or consolidation.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
</tbody>
</table>
</div>
