# Building space name classification

Source: [`building-space-name-classification.skos.ttl`](sources/room-name.ttl)

## Scheme

- **definition (de):** Normalisierte abstrakte Raumbezeichnungen für allgemeinen Gebäudegebrauch auf IfcSpace.
- **definition (en):** Normalized abstract room name types for general building use on IfcSpace.
- **prefLabel (de):** Gebäude-Raumbezeichnungsklassifikation
- **prefLabel (en):** Building Space Name Classification
- **title (en):** Building Space Name Classification

## Hierarchy

Hierarchy diagram omitted (190 concepts; Mermaid render limit is 80 nodes). See the Concepts table below or the source TTL.

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
<td>RN-01</td>
<td></td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Wohnen</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Normalisierte Raumbezeichnungen für Wohnnutzungen.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Residential</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Normalized room names for residential living spaces.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-01-10</td>
<td>RN-01</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Wohnen und Schlafen</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Räume für Wohnen, Schlafen und Essen.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Living and sleeping</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Rooms for daily living, sleeping, and dining.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-01-10-01</td>
<td>RN-01-10</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Schlafzimmer</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Raum primär für Schlafen.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Bedroom</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Room primarily used for sleeping.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-01-10-02</td>
<td>RN-01-10</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Wohnzimmer</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Raum für Wohnen und Entspannung.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Living Room</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Room for daily living and relaxation.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-01-10-03</td>
<td>RN-01-10</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Esszimmer</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Raum für Mahlzeiten.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Dining Room</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Room for eating meals.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-01-10-04</td>
<td>RN-01-10</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Arbeitszimmer</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Wohnlicher Raum für Arbeit oder Studium.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Home Study</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Residential room for study or home office work.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-01-10-05</td>
<td>RN-01-10</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Gästezimmer</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Raum für über Nacht bleibende Gäste.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Guest Room</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Room for overnight guests.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-01-10-06</td>
<td>RN-01-10</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Wintergarten</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Geschlossener verglaster Wohnraum, im Unterschied zu offenen Aussenplattformen wie Balkon, Terrasse und Innenhof.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Winter Garden</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Closed glazed living room, distinct from open outdoor platforms such as balcony, terrace, and patio.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-01-20</td>
<td>RN-01</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Wohnliche Dienste</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Küche, Bad, Wäsche, Trocknung, Hauswirtschaft, Gang, Wohnungseingang, Abstellraum, Kellerabteil und Entree in Wohneinheiten.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Residential services</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Kitchen, bathroom, laundry, drying, utility, hallway, entry, storage, cellar, and entrance spaces within dwellings.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-01-20-01</td>
<td>RN-01-20</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Küche</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Raum für Speisezubereitung.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Kitchen</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Room for food preparation.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-01-20-02</td>
<td>RN-01-20</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Badezimmer</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Raum mit Bad, Dusche oder Körperpflege.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Bathroom</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Room with bath, shower, or personal hygiene fixtures.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-01-20-03</td>
<td>RN-01-20</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Waschküche</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Waschküche innerhalb einer Wohneinheit.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Laundry Room</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Laundry room inside a single dwelling.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-01-20-04</td>
<td>RN-01-20</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Hauswirtschaftsraum</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Raum für haushaltstechnische Einrichtungen.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Utility Room</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Room for domestic utilities and equipment.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-01-20-05</td>
<td>RN-01-20</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Gang</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Erschliessungsgang innerhalb einer Wohneinheit.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Hallway</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Circulation passage within a dwelling unit.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-01-20-06</td>
<td>RN-01-20</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Wohnungseingang</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Eingangsbereich innerhalb einer Wohneinheit.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Residential Entry</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Entry space within a dwelling unit.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-01-20-07</td>
<td>RN-01-20</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Abstellraum Wohnen</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Kleiner Abstellraum innerhalb einer Wohneinheit.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Residential Closet</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Small storage within a dwelling unit.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-01-20-08</td>
<td>RN-01-20</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Kellerabteil</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Zugeordnetes Kellerabteil einer Wohneinheit.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Cellar Compartment</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Assigned cellar storage compartment for a dwelling.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-01-20-09</td>
<td>RN-01-20</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Entree</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Eingangs-Übergangsraum im Wohnkontext.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Entrance Hall</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Residential entrance transition space within a dwelling context.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-01-20-10</td>
<td>RN-01-20</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Gemeinschaftswaschküche</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Gemeinsame Waschküche mehrerer Wohneinheiten, im Unterschied zur Waschküche innerhalb einer Wohnung.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Communal Laundry</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Shared laundry for several dwellings, distinct from the laundry inside one dwelling.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-01-20-11</td>
<td>RN-01-20</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Trocknungsraum</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Raum zum Trocknen der Wäsche, im Unterschied zum Waschraum.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Drying Room</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Room for drying laundry, distinct from the wash room.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-01-30</td>
<td>RN-01</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Wohneinheitsebene</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Gesamtwohnflächen ohne weitere Unterteilung.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Dwelling unit level</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Whole-unit spaces when not subdivided further.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-01-30-03</td>
<td>RN-01-30</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Wohneinheit</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Generische Wohneinheit ohne weitere Unterteilung.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Apartment Unit</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Generic residential unit space when not subdivided further.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-02</td>
<td></td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Arbeit</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Normalisierte Raumbezeichnungen für Büro- und Wissensarbeit.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Work</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Normalized room names for office and knowledge work.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-02-10</td>
<td>RN-02</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Einzelarbeit</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Einzel- und Grossraumbüros.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Individual work</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Enclosed and open-plan workspaces.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-02-10-01</td>
<td>RN-02-10</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Büro</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Büro für Einzel- oder Gruppenarbeit.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Office</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Enclosed office for individual or shared desk work.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-02-10-02</td>
<td>RN-02-10</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Grossraumbüro</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Offene Bürolandschaft ohne geschlossene Zellbüros.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Open-Plan Office</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Open office landscape without full-height partitions.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-02-20</td>
<td>RN-02</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Zusammenarbeit</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Besprechungs- und informelle Teamräume.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Collaboration</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Meeting and informal collaboration spaces.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-02-20-01</td>
<td>RN-02-20</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Besprechungsraum</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Raum für kleine Besprechungen.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Meeting Room</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Room for small group meetings.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-02-20-02</td>
<td>RN-02-20</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Konferenzraum</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Raum für formelle Sitzungen und Präsentationen.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Conference Room</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Room for formal meetings and presentations.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-02-20-03</td>
<td>RN-02-20</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Pausenraum</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Informeller Raum für Pausen.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Break Room</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Informal staff rest and refreshment space.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-02-20-04</td>
<td>RN-02-20</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Gemeinschaftsbüro</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Gemeinsam genutzter Arbeitsraum für Bewohnende ausserhalb der Wohnung.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Community Office</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Shared office for residents working outside their dwelling.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-02-30</td>
<td>RN-02</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Empfangsbereich</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Empfang und Wartebereich für Besucher.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Reception area</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Visitor reception and waiting area.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-02-30-01</td>
<td>RN-02-30</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Empfang</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Empfang und Wartebereich für Besucher.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Reception</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Visitor reception and waiting area.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-03</td>
<td></td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Erschliessung</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Normalisierte Raumbezeichnungen für Erschliessungsräume.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Circulation</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Normalized room names for circulation and access spaces.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-03-10</td>
<td>RN-03</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Horizontale Erschliessung</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Flure, Hallen, Vorräume, Schleusen und horizontale Zugänge.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Horizontal circulation</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Corridors, lobbies, vestibules, airlocks, and horizontal access routes.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-03-10-01</td>
<td>RN-03-10</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Flur</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Horizontaler Verbindungsflur, einschliesslich schmaler Durchgänge zwischen Reihen oder Funktionen.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Corridor</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Horizontal circulation passage, including narrow aisles between rows or functions.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-03-10-02</td>
<td>RN-03-10</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Eingangshalle</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Eingangshalle oder Empfoyer.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Lobby</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Main entrance lobby or reception hall.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-03-10-04</td>
<td>RN-03-10</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Vorraum</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Übergangsraum zwischen Aussen und Innen.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Vestibule</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Transition space between exterior and interior.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-03-10-05</td>
<td>RN-03-10</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Schleuse</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Geschlossene Schleuse für kontrollierten Übergang zwischen Bereichen.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Airlock</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Enclosed lock or airlock for controlled passage between zones.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-03-20</td>
<td>RN-03</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Vertikale Erschliessung</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Treppen, Rampen und Aufzüge.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Vertical circulation</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Stairs, ramps, and lifts.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-03-20-01</td>
<td>RN-03-20</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Treppenhaus</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Treppenhaus mit Podesten.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Stairwell</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Enclosed stair and landing volume.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-03-20-02</td>
<td>RN-03-20</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Aufzugszone</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Wartebereich an Aufzugshaltestellen.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Elevator Lobby</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Waiting area at elevator stops.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-03-20-03</td>
<td>RN-03-20</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Rampe</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Geneigte barrierefreie Erschliessung.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Ramp</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Inclined accessible circulation route.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-04</td>
<td></td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Hygiene</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Normalisierte Raumbezeichnungen für Hygiene- und Sanitärräume.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Hygiene</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Normalized room names for sanitary and changing spaces.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-04-10</td>
<td>RN-04</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Toiletten</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">WC-Räume nach Barrierefreiheit und Geschlechterausstattung.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Toilets</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Toilet rooms by accessibility and gender provision.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-04-10-01</td>
<td>RN-04-10</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Herren-WC</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">WC für Männer.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Male Toilet</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Toilet room for male use.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-04-10-02</td>
<td>RN-04-10</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Damen-WC</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">WC für Frauen.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Female Toilet</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Toilet room for female use.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-04-10-03</td>
<td>RN-04-10</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Barrierefreies WC</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Rollstuhlgängiges WC.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Accessible Toilet</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Wheelchair-accessible toilet room.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-04-10-04</td>
<td>RN-04-10</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Allgemeines WC</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">WC für gemischte oder all-gender Nutzung.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Unisex Toilet</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Toilet room for mixed or all-gender use.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-04-20</td>
<td>RN-04</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Waschen und Umziehen</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Duschen, Umziehen und Schliessfächer.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Wash and change</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Shower, changing, and locker spaces.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-04-20-01</td>
<td>RN-04-20</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Duschraum</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Raum mit Duscheinrichtungen.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Shower Room</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Room with shower facilities.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-04-20-02</td>
<td>RN-04-20</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Umkleideraum</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Raum zum Umziehen.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Changing Room</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Room for changing clothes.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-04-20-03</td>
<td>RN-04-20</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Schliessfachraum</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Raum mit persönlichen Schliessfächern.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Locker Room</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Room with personal lockers.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-05</td>
<td></td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Gesundheit</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Normalisierte Raumbezeichnungen für medizinische und pflegerische Räume.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Healthcare</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Normalized room names for medical and care spaces.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-05-10</td>
<td>RN-05</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Stationäre Pflege</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Räume für stationären Aufenthalt und Erholung.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Inpatient care</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Rooms for inpatient stay and recovery.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-05-10-01</td>
<td>RN-05-10</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Patientenzimmer</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Raum für stationäre Pflege.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Patient Room</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Room for inpatient care and recovery.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-05-10-02</td>
<td>RN-05-10</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Aufwachraum</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Raum für postoperative Überwachung.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Recovery Room</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Room for post-procedure recovery.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-05-20</td>
<td>RN-05</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Klinische Behandlung</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Behandlungs-, Operations- und Eingriffsräume.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Clinical treatment</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Treatment, surgery, and procedure spaces.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-05-20-01</td>
<td>RN-05-20</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Behandlungsraum</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Raum für ambulante Behandlung.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Treatment Room</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Room for outpatient treatment.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-05-20-02</td>
<td>RN-05-20</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Operationssaal</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Raum für operative Eingriffe.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Operating Room</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Room for surgical procedures.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-05-20-03</td>
<td>RN-05-20</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Eingriffsraum</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Raum für kleinere medizinische Eingriffe.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Procedure Room</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Room for minor medical procedures.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-05-20-04</td>
<td>RN-05-20</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Untersuchungsraum</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Raum für ärztliche Untersuchung.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Examination Room</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Room for clinical examination.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-05-30</td>
<td>RN-05</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Diagnostik und Support</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Bildgebung, Labor, Warten und Pflegestation.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Diagnostics and support</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Imaging, laboratory, waiting, and nursing support spaces.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-05-30-01</td>
<td>RN-05-30</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Bildgebungsraum</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Raum für diagnostische Bildgebung.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Imaging Room</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Room for diagnostic imaging.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-05-30-02</td>
<td>RN-05-30</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Medizinisches Labor</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Labor für medizinische Analysen.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Medical Laboratory</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Laboratory for medical analysis.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-05-30-03</td>
<td>RN-05-30</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Wartezimmer</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Raum für wartende Patienten und Besucher.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Waiting Room</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Room for patients and visitors to wait.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-05-30-04</td>
<td>RN-05-30</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Pflegestationszimmer</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Zentrale Pflegestation.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Nurses Station</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Central nursing and monitoring workspace.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-06</td>
<td></td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Bildung</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Normalisierte Raumbezeichnungen für Bildungs- und Lernräume.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Education</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Normalized room names for teaching and learning spaces.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-06-10</td>
<td>RN-06</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Unterricht</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Klassenzimmer, Hörsäle und Seminarräume.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Instruction</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Classrooms, lecture halls, and seminar spaces.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-06-10-01</td>
<td>RN-06-10</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Klassenzimmer</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Raum für Schul- oder Gruppenunterricht.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Classroom</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Room for school or group instruction.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-06-10-02</td>
<td>RN-06-10</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Hörsaal</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Raum mit festem Gestühl für Vorlesungen.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Lecture Hall</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Room with fixed seating for lectures.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-06-10-03</td>
<td>RN-06-10</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Seminarraum</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Raum für Seminare und Workshops.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Seminar Room</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Room for seminars and workshops.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-06-10-04</td>
<td>RN-06-10</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Computerraum</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Raum mit Computerarbeitsplätzen für Unterricht.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Computer Lab</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Room with computer workstations for teaching.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-06-20</td>
<td>RN-06</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Selbstgesteuertes Lernen</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Bibliothek, Lernräume und Ausbildungswerkstätten.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Self-directed learning</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Library, study, and training workshop spaces.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-06-20-01</td>
<td>RN-06-20</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Bibliotheksraum</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Raum für Lesen und Bibliotheksnutzung.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Library Room</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Room for reading and library use.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-06-20-02</td>
<td>RN-06-20</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Lernraum</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Raum für selbstständiges Lernen.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Study Room</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Room for self-directed study.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-06-20-03</td>
<td>RN-06-20</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Ausbildungswerkstatt</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Raum für praktische Ausbildung.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Training Workshop</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Room for practical skills training.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-06-30</td>
<td>RN-06</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Versammlung und Fachräume</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Aula, Ateliers und naturwissenschaftliche Laboratorien.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Assembly and special subjects</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Auditoria, art studios, and science laboratories.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-06-30-01</td>
<td>RN-06-30</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Aula</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Grosse Versammlungshalle für Veranstaltungen.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Auditorium</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Large assembly hall for events.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-06-30-02</td>
<td>RN-06-30</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Kunstatelier</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Raum für bildnerischen Unterricht.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Art Studio</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Room for visual arts instruction and practice.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-06-30-03</td>
<td>RN-06-30</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Naturwissenschaftslabor</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Labor für naturwissenschaftlichen Unterricht.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Science Lab</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Laboratory for science teaching.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-07</td>
<td></td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Gewerbe</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Normalisierte Raumbezeichnungen für Gastronomie- und Verkaufsräume.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Commercial</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Normalized room names for hospitality and retail spaces.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-07-10</td>
<td>RN-07</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Gastronomie</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Cafeterias, Restaurants, Bars und Food-Courts.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Dining and beverage</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Cafeterias, restaurants, bars, and food courts.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-07-10-01</td>
<td>RN-07-10</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Cafeteria</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Selbstbedienungsgastronomie.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Cafeteria</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Self-service dining space.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-07-10-02</td>
<td>RN-07-10</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Restaurant</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Bediente Gastronomie.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Restaurant</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Full-service dining space.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-07-10-03</td>
<td>RN-07-10</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Bar</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Raum für Getränkeausschank.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Bar</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Room for beverage service.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-07-10-04</td>
<td>RN-07-10</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Food-Court</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Gemeinsame Gastronomiefläche mit mehreren Anbietern.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Food Court</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Shared dining area with multiple vendors.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-07-20</td>
<td>RN-07</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Verkauf und Ausstellung</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Verkaufs-, Ausstellungs- und Kioskbereiche.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Retail and exhibition</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Retail, sales, kiosk, and exhibition spaces.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-07-20-01</td>
<td>RN-07-20</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Verkaufsraum</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Raum für Warenpräsentation und Verkauf.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Retail Space</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Room for displaying and selling goods.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-07-20-02</td>
<td>RN-07-20</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Verkaufsfläche</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Offene Verkaufsfläche.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Sales Floor</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Open retail sales area.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-07-20-03</td>
<td>RN-07-20</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Kiosk</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Kleiner Verkaufs- oder Servicebereich.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Kiosk</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Small retail or service counter space.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-07-20-04</td>
<td>RN-07-20</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Kundenbetreuungsbereich</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Bereich für Kundenbetreuung.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Customer Service Area</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Area for customer assistance and service.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-07-20-05</td>
<td>RN-07-20</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Ausstellungsraum</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Raum für Ausstellungen.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Exhibition Space</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Room for displays and exhibitions.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-07-30</td>
<td>RN-07</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Beherbergung</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Hotel- und Gästezimmer.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Hospitality</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Hotel and guest accommodation rooms.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-07-30-01</td>
<td>RN-07-30</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Hotelzimmer</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Übernachtungszimmer für Gäste.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Hotel Room</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Guest accommodation room.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-08</td>
<td></td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Industrie</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Normalisierte Raumbezeichnungen für Produktions- und Werkräume.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Industrial</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Normalized room names for production and workshop spaces.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-08-10</td>
<td>RN-08</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Produktion</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Werkstätten, Produktionshallen, Montage und Reinräume.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Production</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Workshops, production halls, assembly, and clean rooms.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-08-10-01</td>
<td>RN-08-10</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Werkstatt</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Raum für manuelle Fertigung und Reparatur.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Workshop</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Room for manual fabrication and repair.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-08-10-02</td>
<td>RN-08-10</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Produktionshalle</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Halle für Produktionsprozesse.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Production Hall</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Hall for manufacturing processes.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-08-10-03</td>
<td>RN-08-10</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Montagebereich</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Bereich für Montage.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Assembly Area</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Area for product assembly.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-08-10-04</td>
<td>RN-08-10</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Verpackungsbereich</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Bereich für Verpackung.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Packaging Area</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Area for packaging goods.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-08-10-05</td>
<td>RN-08-10</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Reinraum</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Produktionsraum mit kontrollierter Umgebung.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Clean Room</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Controlled-environment production room.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-08-20</td>
<td>RN-08</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Logistik</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Lagerung, Be-/Entladung, Qualitätskontrolle und Wartung.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Logistics</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Warehousing, loading, quality control, and maintenance.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-08-20-01</td>
<td>RN-08-20</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Lagerhalle</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Halle oder Raum für Warenlagerung.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Warehouse</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Room or hall for goods storage.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-08-20-02</td>
<td>RN-08-20</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Laderampe</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Bereich für Be- und Entladung.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Loading Dock</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Area for loading and unloading goods.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-08-20-03</td>
<td>RN-08-20</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Qualitätskontrollraum</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Raum für Prüfung und Qualitätskontrolle.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Quality Control Room</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Room for inspection and quality testing.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-08-20-04</td>
<td>RN-08-20</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Wartungsbucht</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Bucht für Gerätewartung.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Maintenance Bay</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Bay for equipment maintenance.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-08-30</td>
<td>RN-08</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Spezielle Industrie</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Überdeckte Höfe und spezielle Industrieräume.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Special industrial</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Covered yards and special industrial spaces.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-08-30-01</td>
<td>RN-08-30</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Überdachter Hof</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Überdachter Aussenarbeits- oder Lagerhof als Raum modelliert.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Covered Yard</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Covered exterior work or storage yard modeled as space.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-09</td>
<td></td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Technik</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Normalisierte Raumbezeichnungen für Technik- und Anlagenräume.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Technical</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Normalized room names for building services and plant rooms.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-09-10</td>
<td>RN-09</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">HLK und Sanitärtechnik</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Heizungs-, Kälte-, Pumpen- und Sprinklerzentralen.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">HVAC and plumbing plant</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Heating, cooling, pumping, and fire suppression plant rooms.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-09-10-01</td>
<td>RN-09-10</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">HLK-Zentralraum</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Raum für Heizungs-, Lüftungs- und Klimaanlagen.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">HVAC Plant Room</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Room for heating, ventilation, and cooling plant.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-09-10-02</td>
<td>RN-09-10</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Pumpenraum</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Raum für Pumpen und Flüssigkeitstechnik.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Pump Room</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Room for pumps and fluid handling.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-09-10-03</td>
<td>RN-09-10</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Heizungsraum</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Raum für Heizkessel und Wärmeerzeugung.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Boiler Room</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Room for boilers and heat generation.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-09-10-04</td>
<td>RN-09-10</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Kälteraum</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Raum für Kälteanlagen.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Chiller Room</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Room for chillers and cooling plant.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-09-10-05</td>
<td>RN-09-10</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Sprinklerraum</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Raum für Sprinkler- und Löschanlagen.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Sprinkler Room</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Room for fire suppression equipment.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-09-20</td>
<td>RN-09</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Elektro- und IT-Technik</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Elektro-, Generator-, Transformator-, Server- und Kommunikationsräume.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Electrical and IT plant</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Electrical, generator, transformer, server, and telecom rooms.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-09-20-01</td>
<td>RN-09-20</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Elektroraum</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Raum für elektrische Verteilung.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Electrical Room</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Room for electrical distribution equipment.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-09-20-02</td>
<td>RN-09-20</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Serverraum</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Raum für IT- und Netzwerktechnik.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Server Room</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Room for IT and network equipment.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-09-20-03</td>
<td>RN-09-20</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Generatorraum</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Raum für Notstromaggregate.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Generator Room</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Room for backup power generation.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-09-20-04</td>
<td>RN-09-20</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Transformatorenraum</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Raum für Transformatoren.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Transformer Room</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Room for electrical transformers.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-09-20-05</td>
<td>RN-09-20</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Kommunikationsraum</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Raum für Telekommunikations- und Schwachstromanlagen.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Communications Room</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Room for telecom and low-voltage systems.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-09-30</td>
<td>RN-09</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Zähler und Entsorgung</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Zählerräume und Abfallräume.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Metering and waste</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Meter rooms and waste handling spaces.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-09-30-01</td>
<td>RN-09-30</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Zählerraum</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Raum für Verbrauchszähler.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Meter Room</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Room for utility metering equipment.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-09-30-02</td>
<td>RN-09-30</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Abfallraum</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Raum für Abfallsammlung.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Waste Room</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Room for waste collection and handling.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-09-30-03</td>
<td>RN-09-30</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Abfallschacht</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Vertikaler Schacht für den Transport von Siedlungsabfall zu einer zentralen Sammelstelle.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Waste Chute</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Vertical chute for transferring household waste to a central collection point.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-10</td>
<td></td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Lager</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Normalisierte Raumbezeichnungen für Lager- und Nebenräume.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Storage</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Normalized room names for storage and ancillary spaces.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-10-10</td>
<td>RN-10</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Allgemeine Lagertypen</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Allgemeine, Material-, Geräte-, Hauswart- und Kinderwagenlager.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">General storage types</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">General, supply, equipment, janitor, and stroller storage.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-10-10-01</td>
<td>RN-10-10</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Allgemeiner Lagerraum</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Raum für allgemeine Materiallagerung.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">General Storage</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Room for general material storage.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-10-10-02</td>
<td>RN-10-10</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Materialraum</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Raum für Verbrauchsmaterial.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Supply Room</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Room for consumable supplies.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-10-10-03</td>
<td>RN-10-10</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Gerätelager</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Lager für Geräte und Werkzeuge.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Equipment Storage</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Storage for tools and equipment.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-10-10-04</td>
<td>RN-10-10</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Annahmelager</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Zwischenlager am Annahmeort.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Unloading Storage</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Temporary storage at delivery point.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-10-10-05</td>
<td>RN-10-10</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Hauswarteschrank</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Kleiner Raum für Reinigungsmaterial.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Janitor Closet</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Small room for cleaning supplies and equipment.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-10-10-06</td>
<td>RN-10-10</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Kinderwagenraum</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Abstellraum für Kinderwagen und Mobilitätshilfen an der Eingangshalle, ausserhalb des Fluchtwegs.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Stroller Room</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Store for strollers and mobility aids off the lobby, off the escape route.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-10-10-07</td>
<td>RN-10-10</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Gartenhaus</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Geschlossener Abstellraum im Aussenbereich für Gartengeräte und Haushaltsgüter.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Garden Shed</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Enclosed outdoor storage room for garden tools and household goods.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-10-20</td>
<td>RN-10</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Speziallager</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Archive, Post- und Paketräume, Kühllager sowie Labor-, Chemikalien-, Gefahrstoff- und Probenlager.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Specialized storage</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Archives, mail rooms, parcel rooms, cold storage, and laboratory, chemical, hazardous, and sample storage.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-10-20-01</td>
<td>RN-10-20</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Archivraum</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Raum für Dokumenten- und Aktenarchive.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Archive Room</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Room for document and record archives.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-10-20-02</td>
<td>RN-10-20</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Postraum</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Raum für Postein- und -ausgang.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Mail Room</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Room for incoming and outgoing mail.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-10-20-03</td>
<td>RN-10-20</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Kühlraum</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Gekühlter Lagerraum.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Cold Storage</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Refrigerated storage room.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-10-20-04</td>
<td>RN-10-20</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Laborlager</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Lager für Labormaterial und Verbrauchsgüter.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Laboratory Storage</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Storage for laboratory materials and consumables.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-10-20-05</td>
<td>RN-10-20</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Chemikalienlager</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Lager für Chemikalien.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Chemical Storage</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Storage for chemicals.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-10-20-06</td>
<td>RN-10-20</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Gefahrstofflager</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Lager für Gefahrstoffe.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Hazardous Material Storage</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Storage for hazardous materials.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-10-20-07</td>
<td>RN-10-20</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Probenlager</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Lager für Labor- oder Materialproben.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Sample Storage</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Storage for laboratory or material samples.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-10-20-08</td>
<td>RN-10-20</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Paketraum</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Raum für Paketfächer, im Unterschied zum Postraum und zu persönlichen Schliessfächern.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Parcel Room</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Parcel locker room, distinct from the mail room and from personal lockers.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-11</td>
<td></td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Aussen</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Normalisierte Raumbezeichnungen für als IfcSpace modellierte Aussenräume.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Outdoor</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Normalized room names for exterior spaces modeled as IfcSpace.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-11-10</td>
<td>RN-11</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Aussenplattformen</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Balkone, Loggien, Fluchtbalkone, Terrassen, Dachterrassen, Wartungsdächer, Technikaufstellflächen, Gründächer und Innenhöfe.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Exterior platforms</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Balconies, loggias, escape balconies, terraces, roof terraces, maintenance roofs, technical plant pads, green roofs, and patios.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-11-10-01</td>
<td>RN-11-10</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Balkon</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Vom Innern erschlossene Aussenplattform.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Balcony</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Exterior projecting platform accessed from inside.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-11-10-02</td>
<td>RN-11-10</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Terrasse</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Aussenliegende Terrassenfläche.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Terrace</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Exterior paved or decked platform.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-11-10-03</td>
<td>RN-11-10</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Innenhof</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Innenhof oder Patio.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Patio</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Enclosed or semi-enclosed outdoor sitting area.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-11-10-04</td>
<td>RN-11-10</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Fluchtbalkon</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Aussenliegender Balkon als Fluchtweg.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Escape Balcony</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Exterior balcony serving as an escape route.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-11-10-05</td>
<td>RN-11-10</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Dachterrasse</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Begehbares und nutzbares Flachdach als Aussenfläche.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Roof Terrace</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Occupiable flat-roof area intended for outdoor use.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-11-10-06</td>
<td>RN-11-10</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Wartungsdach</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Begehbares Flachdach nur für Betrieb, Wartung und Inspektion.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Maintenance Roof</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Walkable flat-roof area accessible only for facility management and inspection.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-11-10-07</td>
<td>RN-11-10</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Technikaufstellfläche</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Flachdach- oder Aussenfläche für die Aufstellung haustechnischer Anlagen und Geräte.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Technical Plant Pad</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Flat-roof or outdoor pad reserved for building-services equipment and plant.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-11-10-08</td>
<td>RN-11-10</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Gründach</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Begrünte Flachdachfläche als Aussenraum modelliert.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Green Roof</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Vegetated flat-roof area modeled as outdoor space.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-11-10-09</td>
<td>RN-11-10</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Loggia</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Zurückgesetzter offener Aussenraum im Gebäudevolumen, im Unterschied zum auskragenden Balkon.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Loggia</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Recessed open outdoor room inside the building volume, distinct from a projecting balcony.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-11-20</td>
<td>RN-11</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Landschaft und Freizeit</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Gärten, Spielplätze, Beckenflächen und Retentionsflächen.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Landscape and recreation</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Gardens, playgrounds, pool areas, and retention areas.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-11-20-01</td>
<td>RN-11-20</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Gartenfläche</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Als Raum modellierte Gartenfläche.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Garden Area</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Landscaped outdoor area as space.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-11-20-02</td>
<td>RN-11-20</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Spielplatz</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Aussenliegender Spielbereich.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Playground</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Outdoor play area.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-11-20-03</td>
<td>RN-11-20</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Beckenfläche</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Aussenliegende Becken- oder Wasserfläche.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Pool Area</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Outdoor pool or water feature area.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-11-20-04</td>
<td>RN-11-20</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Retentionsfläche</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Mehrzweckfläche mit temporärer, geplanter Wasserrückhaltung bei Starkregen.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Retention Area</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Multi-purpose area with temporary, planned water retention during heavy rainfall.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-11-30</td>
<td>RN-11</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Überdachte Aussenwege</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Überdachte Fusswege und Portiken.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Covered exterior routes</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Covered walkways and porticos.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-11-30-01</td>
<td>RN-11-30</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Überdachter Fussweg</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Überdachter Aussenweg für Fussgänger.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Covered Walkway</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Covered exterior pedestrian route.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-11-30-02</td>
<td>RN-11-30</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Portikus</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Überdachter Aussenanbau am Eingang.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Portico</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Covered exterior entrance structure.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-11-40</td>
<td>RN-11</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Aussenerschliessung</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Aussentreppen, Strassen und aussenliegende Erschliessungswege.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Exterior circulation</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Exterior stairs, streets, and outdoor access routes.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-11-40-01</td>
<td>RN-11-40</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Aussentreppe</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Aussenliegende Treppe zur vertikalen Erschliessung.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Exterior Stair</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Open or external stair for outdoor vertical circulation.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-11-40-02</td>
<td>RN-11-40</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Strasse</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Als Raum modellierte äussere Fahrerschliessung, einschliesslich Zufahrts-, Betriebs- und Erschliessungsstrassen.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Street</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Outdoor vehicular circulation route as space, including access roads, driveways, and service roads.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-11-50</td>
<td>RN-11</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Abfallsammlung Aussen</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Aussenflächen für das Sammeln und Bereitstellen von Siedlungsabfall.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Exterior waste collection</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Outdoor areas for collecting and presenting household waste.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-11-50-01</td>
<td>RN-11-50</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Abfallsammelplatz Aussen</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Aussenfläche für das Sammeln und Bereitstellen von Siedlungsabfall in Säcken.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Exterior Waste Collection Area</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Outdoor area for collecting and presenting bagged household waste.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-11-50-02</td>
<td>RN-11-50</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Unterflurcontainer</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Aussenfläche für einen unterirdischen Sammelcontainer für Siedlungsabfall.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Underground Waste Container</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Outdoor space allocated to an underground household-waste collection container.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-11-60</td>
<td>RN-11</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Zustellanlagen Aussen</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Aussenflächen für Briefkasten- und Paketfachanlagen.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Exterior delivery facilities</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Outdoor areas allocated to mailboxes and parcel lockers.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-11-60-01</td>
<td>RN-11-60</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Briefkasten- und Paketfachanlage Aussen</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Aussenfläche für Briefkästen und Paketfächer.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Exterior Mailbox and Parcel Locker Area</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Outdoor area allocated to mailboxes and parcel lockers.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-12</td>
<td></td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Hohlraum</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Normalisierte Raumbezeichnungen für nicht nutzbare Hohlräume.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Void</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Normalized room names for non-occupiable void spaces.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-12-10</td>
<td>RN-12</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Vertikale Hohlräume</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Schächte und Steigzonen.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Vertical voids</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Shafts and service risers.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-12-10-01</td>
<td>RN-12-10</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Schacht</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Vertikaler Technik- oder Erschliessungsschacht.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Shaft</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Vertical service or circulation shaft.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-12-10-02</td>
<td>RN-12-10</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Steigzone</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Vertikale Gebäudetechnik-Steigzone.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Riser</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Vertical building services riser.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-12-20</td>
<td>RN-12</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Installations- und Lufträume</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Installationshohlräume und modellierter Luftraum.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Plenums and air volumes</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Plenums, mechanical voids, and modeled air spaces.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-12-20-01</td>
<td>RN-12-20</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Installationszwischenraum</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Installationshohlraum in Decke oder Boden.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Plenum</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Ceiling or floor service void.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-12-20-02</td>
<td>RN-12-20</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Technikhohlraum</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Nicht begehbarer Technikhohlraum.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Mechanical Void</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Non-accessible mechanical void.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-12-20-03</td>
<td>RN-12-20</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Luftraum</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Nicht nutzbarer Luftraum im Modell.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Air Space</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Non-occupiable air volume in the model.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-13</td>
<td></td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Parkierung</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Normalisierte Raumbezeichnungen für Innen- und Aussenparkierung.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Parking</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Normalized room names for interior and exterior parking spaces.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-13-10</td>
<td>RN-13</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Innenparkierung</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Parkplätze in einem Gebäude oder einer Anlage.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Interior parking</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Parking spaces within a building or structure.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-13-10-01</td>
<td>RN-13-10</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Parkplatz PKW Innen</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Innenparkplatz für Personenwagen.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Interior Car Parking</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Interior parking space for passenger cars.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-13-10-02</td>
<td>RN-13-10</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Parkplatz LKW Innen</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Innenparkplatz für Lastwagen.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Interior Truck Parking</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Interior parking space for trucks.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-13-10-03</td>
<td>RN-13-10</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Parkplatz Velo Innen</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Innenparkplatz für Velos.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Interior Bicycle Parking</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Interior parking space for bicycles.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-13-10-04</td>
<td>RN-13-10</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Parkplatz Motorrad Innen</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Innenparkplatz für Motorräder.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Interior Motorcycle Parking</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Interior parking space for motorcycles.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-13-20</td>
<td>RN-13</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Aussenparkierung</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Parkplätze im Aussenbereich.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Exterior parking</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Parking spaces in outdoor areas.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-13-20-01</td>
<td>RN-13-20</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Parkplatz PKW Aussen</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Aussenparkplatz für Personenwagen.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Exterior Car Parking</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Exterior parking space for passenger cars.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-13-20-02</td>
<td>RN-13-20</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Parkplatz LKW Aussen</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Aussenparkplatz für Lastwagen.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Exterior Truck Parking</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Exterior parking space for trucks.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-13-20-03</td>
<td>RN-13-20</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Parkplatz Velo Aussen</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Aussenparkplatz für Velos.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Exterior Bicycle Parking</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Exterior parking space for bicycles.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-13-20-04</td>
<td>RN-13-20</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Parkplatz Motorrad Aussen</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Aussenparkplatz für Motorräder.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Exterior Motorcycle Parking</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Exterior parking space for motorcycles.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
</tbody>
</table>
</div>
