# Abstract site facility products

Source: [`site-setup-products.skos.ttl`](sources/site-facility-product.ttl)

## Scheme

- **definition (de):** Produkttyp-Klassifikation fuer temporaere Baustelleneinrichtung: Geraete, Abschrankungen, Logistikflaechen, Aufenthalt und Baustellenanschluesse. Ein topConcept pro Objekt. Unterscheidet sich von dauerhaften Gebaeudeprodukten.
- **definition (en):** Product-type classification for temporary construction-site facilities: plant, enclosures, logistics surfaces, accommodation, and site services. Assign one top concept per object. Distinct from permanent building products.
- **prefLabel (de):** Abstrakte Baustelleneinrichtungsprodukte
- **prefLabel (en):** Abstract site facility products
- **title (en):** Abstract site facility products

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
<th>Data sheet</th>
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
<td>SFP-BATCH-PLANT</td>
<td></td>
<td><a href="https://github.com/pragmaticBIM/pragmaticbim-reference/blob/main/products/sfp-batch-plant.yaml">Reference</a></td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Betonmischanlage</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Anlage auf der Baustelle, die Beton dosiert und mischt.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note">Mischanlage, nicht die Pumpe. Pumpenstandort und Ausleger sind SFP-PUMP. Schuettgutsilos sind SFP-SILO.</td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Concrete batching plant</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">On-site plant that batches and mixes concrete.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note">Mixing plant, not the pump. Pump position and boom are SFP-PUMP. Bulk silos are SFP-SILO.</td>
</tr>
<tr>
<td>SFP-BREAK-ROOM</td>
<td></td>
<td><a href="https://github.com/pragmaticBIM/pragmaticbim-reference/blob/main/products/sfp-break-room.yaml">Reference</a></td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Aufenthaltsraum</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Temporaerer Raum, in dem Baustellenpersonal isst und pausiert.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note">Nicht SFP-OFFICE und nicht SFP-SANITARY.</td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Break room</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Temporary room where site personnel eat and rest.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note">Not SFP-OFFICE and not SFP-SANITARY.</td>
</tr>
<tr>
<td>SFP-BUFFER</td>
<td></td>
<td><a href="https://github.com/pragmaticBIM/pragmaticbim-reference/blob/main/products/sfp-buffer.yaml">Reference</a></td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Zwischenlager</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Temporaere Flaeche fuer Material zwischen Anlieferung und Einbau oder Weitertransport.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note">Nicht SFP-STORAGE, nicht SFP-STORE und nicht SFP-TRANSFER. Unterscheidet sich vom Raumnamen RN-10-10-04 (Annahmelager), der ein Innenraum am Annahmeort ist.</td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Intermediate storage</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Temporary holding area for material between delivery and installation or onward transport.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note">Not SFP-STORAGE, not SFP-STORE, and not SFP-TRANSFER. Distinct from room name RN-10-10-04 (Annahmelager), which is an indoor space at a delivery point.</td>
</tr>
<tr>
<td>SFP-CANOPY</td>
<td></td>
<td><a href="https://github.com/pragmaticBIM/pragmaticbim-reference/blob/main/products/sfp-canopy.yaml">Reference</a></td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Schutzdach</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Temporaeres Dach ueber oeffentlichem Gehweg oder Nachbarzugang, das Fussgaenger vor herabfallenden Teilen schuetzt.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note">Nicht SFP-SCAFFOLD und nicht SFP-FENCE. Das Schutzdach deckt Fussgaenger auf der oeffentlichen Seite; das Geruest ist eine Arbeitsbuehne; der Zaun ist die Abschrankung.</td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Protective canopy</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Temporary roof over a public footway or neighbouring access, protecting pedestrians from falling objects.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note">Not SFP-SCAFFOLD and not SFP-FENCE. The canopy covers pedestrians on the public side; the scaffold is a work platform; the fence is the enclosure.</td>
</tr>
<tr>
<td>SFP-CONTAINER</td>
<td></td>
<td><a href="https://github.com/pragmaticBIM/pragmaticbim-reference/blob/main/products/sfp-container.yaml">Reference</a></td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Container</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Allgemeiner Baustellencontainer als versetzbare Einheit, ohne genauer bestimmte Aufenthalts- oder Lagerfunktion.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note">Allgemeiner Container, kein abschliessbares Magazin (SFP-STORE). Buero, Aufenthalt und Sanitaer sind SFP-OFFICE, SFP-BREAK-ROOM und SFP-SANITARY.</td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Site container</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Generic site container used as a relocatable unit, without a more specific accommodation or storage function.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note">Generic container, not a lockable store (SFP-STORE). Office, break room, and sanitary units are SFP-OFFICE, SFP-BREAK-ROOM, and SFP-SANITARY.</td>
</tr>
<tr>
<td>SFP-CRANE</td>
<td></td>
<td><a href="https://github.com/pragmaticBIM/pragmaticbim-reference/blob/main/products/sfp-crane.yaml">Reference</a></td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Kran</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Der Kran als Maschine: Turmdrehkran, Mobilkran oder Raupenkran auf der Baustelle.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note">Nur die Maschine. Reichweite und Hoehe sind SFP-CRANE-SWING. Kranstellflaeche und Abstuetzungen sind SFP-CRANE-PAD. Festes Fundament ist SFP-CRANE-FOUNDATION.</td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Crane</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">The crane as a machine: tower crane, mobile crane, or crawler crane stationed on site.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note">Machine only. Reach and height are SFP-CRANE-SWING. Mobile-crane pad and outriggers are SFP-CRANE-PAD. Fixed foundation is SFP-CRANE-FOUNDATION.</td>
</tr>
<tr>
<td>SFP-CRANE-FOUNDATION</td>
<td></td>
<td><a href="https://github.com/pragmaticBIM/pragmaticbim-reference/blob/main/products/sfp-crane-foundation.yaml">Reference</a></td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Kranfundament</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Festes Fundament fuer einen Turmdrehkran, einschliesslich Sockel, Verankerung und Ballast fuer die Einsatzdauer.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note">Festes Fundament, nicht die Kranstellflaeche (SFP-CRANE-PAD) und nicht die Kranmaschine (SFP-CRANE).</td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Crane foundation</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Fixed foundation for a tower crane, including the base, anchors, and ballast that stay in place for the crane&#x27;s service.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note">Fixed foundation, not the mobile-crane pad (SFP-CRANE-PAD) and not the crane machine (SFP-CRANE).</td>
</tr>
<tr>
<td>SFP-CRANE-PAD</td>
<td></td>
<td><a href="https://github.com/pragmaticBIM/pragmaticbim-reference/blob/main/products/sfp-crane-pad.yaml">Reference</a></td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Kranstellfläche</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Vorbereiteter Untergrund, Lastverteilplatten und Abstuetzpositionen fuer einen Mobilkran.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note">Nicht SFP-CRANE und nicht SFP-CRANE-FOUNDATION. Die Stellflaeche ist der temporaere Standplatz mit Abstuetzungen; das Fundament ist ein fester Sockel.</td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Crane set-up pad</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Prepared ground, bearing mats, and outrigger positions for a mobile crane.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note">Not SFP-CRANE and not SFP-CRANE-FOUNDATION. The pad is the temporary set-up surface and outriggers; the foundation is a fixed base.</td>
</tr>
<tr>
<td>SFP-CRANE-SWING</td>
<td></td>
<td><a href="https://github.com/pragmaticBIM/pragmaticbim-reference/blob/main/products/sfp-crane-swing.yaml">Reference</a></td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Schwenkbereich</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Der Raum, den der Kran in Grundriss und Hoehe erreicht, fuer Kollision, Ueberschwenken und Lastwege.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note">Nicht die Kranmaschine (SFP-CRANE). Der Ablauf betrifft den Schwenkbereich, nicht das Geraet.</td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Crane swing envelope</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">The volume the crane can reach in plan and height, used to check collisions, oversailing, and load paths.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note">Not the crane machine (SFP-CRANE). The workflow is about the envelope, not the equipment.</td>
</tr>
<tr>
<td>SFP-FENCE</td>
<td></td>
<td><a href="https://github.com/pragmaticBIM/pragmaticbim-reference/blob/main/products/sfp-fence.yaml">Reference</a></td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Zaun</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Temporaerer Bauzaun, der die Baustelle umschliesst und vom oeffentlichen Raum trennt.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note">Abschrankung, kein Fussgaengerschutz. Ein Schutzdach ueber dem oeffentlichen Gehweg ist SFP-CANOPY. Zugaenge sind SFP-GATE.</td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Site fence</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Temporary site fence that encloses the works and separates them from the public.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note">Enclosure, not a pedestrian cover. A protective roof over a public footway is SFP-CANOPY. Access openings are SFP-GATE.</td>
</tr>
<tr>
<td>SFP-GATE</td>
<td></td>
<td><a href="https://github.com/pragmaticBIM/pragmaticbim-reference/blob/main/products/sfp-gate.yaml">Reference</a></td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Tor</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Fahrzeug- oder Personentor im Bauzaun.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Gate</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Vehicle or pedestrian gate in the site fence.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>SFP-HAUL-ROAD</td>
<td></td>
<td><a href="https://github.com/pragmaticBIM/pragmaticbim-reference/blob/main/products/sfp-haul-road.yaml">Reference</a></td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Baustraße</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Temporaere Strasse auf der Baustelle fuer den Baustellenverkehr.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note">Baustrasse, keine Wendeflaeche. Das Wenden von Lastwagen ist SFP-TURNING. Eine Rampe ist SFP-RAMP.</td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Haul road</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Temporary road on site for construction traffic.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note">Site road, not a turning area. Truck turning is SFP-TURNING. A ramp is SFP-RAMP.</td>
</tr>
<tr>
<td>SFP-HOIST</td>
<td></td>
<td><a href="https://github.com/pragmaticBIM/pragmaticbim-reference/blob/main/products/sfp-hoist.yaml">Reference</a></td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Bauaufzug</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Temporaerer Aufzug fuer Personal oder Material an der Gebaeudefassade.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Construction hoist</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Temporary hoist for personnel or materials on the building face.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>SFP-OFFICE</td>
<td></td>
<td><a href="https://github.com/pragmaticBIM/pragmaticbim-reference/blob/main/products/sfp-office.yaml">Reference</a></td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Baubüro</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Temporaeres Buero fuer Bauleitung, Planung und Besprechungen.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note">Baubuero. Ein Aufenthaltsraum ist SFP-BREAK-ROOM. Sanitaeranlagen sind SFP-SANITARY.</td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Site office</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Temporary office for site management, planning, and meetings.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note">Site office. A break room is SFP-BREAK-ROOM. Sanitary facilities are SFP-SANITARY.</td>
</tr>
<tr>
<td>SFP-OTH</td>
<td></td>
<td><a href="https://github.com/pragmaticBIM/pragmaticbim-reference/blob/main/products/sfp-oth.yaml">Reference</a></td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Sonstige / unbekannte Baustelleneinrichtung</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Baustelleneinrichtung nicht klassifiziert oder noch unbekannt.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note">Fallback fuer fruehe Entwurfsstufen oder fehlende Daten.</td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Other / unknown site facility</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Site facility not classified or not yet known.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note">Fallback for early design stages or missing data.</td>
</tr>
<tr>
<td>SFP-PARKING</td>
<td></td>
<td><a href="https://github.com/pragmaticBIM/pragmaticbim-reference/blob/main/products/sfp-parking.yaml">Reference</a></td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Parkplatz</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Temporaerer Parkplatz fuer Baustellenfahrzeuge und Personal.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Parking area</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Temporary parking for site vehicles and personnel.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>SFP-POWER-DIST</td>
<td></td>
<td><a href="https://github.com/pragmaticBIM/pragmaticbim-reference/blob/main/products/sfp-power-dist.yaml">Reference</a></td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Baustromverteiler</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Temporaerer Elektroverteiler, der die Baustelle ab dem Stromanschluss versorgt.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note">Elektrische Verteilung. Der Bauwasseranschluss ist SFP-WATER-CONN.</td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Site power distribution board</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Temporary electrical distribution board that supplies the site from the power connection.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note">Electrical distribution. The site water connection is SFP-WATER-CONN.</td>
</tr>
<tr>
<td>SFP-PUMP</td>
<td></td>
<td><a href="https://github.com/pragmaticBIM/pragmaticbim-reference/blob/main/products/sfp-pump.yaml">Reference</a></td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Betonpumpe</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Standort und Ausleger einer Betonpumpe, einschliesslich des vom Ausleger ueberstrichenen Raums.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note">Nicht SFP-BATCH-PLANT. Die Pumpe ist die Einbringmaschine mit Ausleger; die Mischanlage mischt den Beton.</td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Concrete pump</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Position and boom of a concrete pump, including the space the boom sweeps.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note">Not SFP-BATCH-PLANT. The pump is the placing machine and its boom; the batching plant mixes the concrete.</td>
</tr>
<tr>
<td>SFP-RAMP</td>
<td></td>
<td><a href="https://github.com/pragmaticBIM/pragmaticbim-reference/blob/main/products/sfp-ramp.yaml">Reference</a></td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Rampe</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Temporaere Rampe, die einen Hoehenunterschied fuer Fahrzeuge oder Personen auf der Baustelle ueberbrueckt.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note">Rampe fuer den Hoehenwechsel. Eine Baustrasse ist SFP-HAUL-ROAD. Das Wenden von Lastwagen ist SFP-TURNING.</td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Ramp</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Temporary ramp that bridges a level difference for vehicles or pedestrians on site.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note">Level-change ramp. A haul road is SFP-HAUL-ROAD. Truck turning is SFP-TURNING.</td>
</tr>
<tr>
<td>SFP-SANITARY</td>
<td></td>
<td><a href="https://github.com/pragmaticBIM/pragmaticbim-reference/blob/main/products/sfp-sanitary.yaml">Reference</a></td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Sanitäranlage</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Temporaere Toiletten, Waschraeume und Duschen fuer die Baustelle.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note">Sanitaeranlage. Ein Aufenthaltsraum ist SFP-BREAK-ROOM. Das Baubuero ist SFP-OFFICE.</td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Sanitary facility</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Temporary toilets, washrooms, and showers for the site.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note">Sanitary facility. A break room is SFP-BREAK-ROOM. The site office is SFP-OFFICE.</td>
</tr>
<tr>
<td>SFP-SCAFFOLD</td>
<td></td>
<td><a href="https://github.com/pragmaticBIM/pragmaticbim-reference/blob/main/products/sfp-scaffold.yaml">Reference</a></td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Gerüst</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Temporaeres Geruest mit Arbeitsbuehnen und Zugang in der Hoehe.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note">Arbeitsbuehne. Eine Fussgaengerabdeckung auf der oeffentlichen Seite ist SFP-CANOPY. Die Baustellenabschrankung ist SFP-FENCE.</td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Scaffold</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Temporary scaffold providing work platforms and access at height.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note">Work platform. A pedestrian cover on the public side is SFP-CANOPY. The site enclosure is SFP-FENCE.</td>
</tr>
<tr>
<td>SFP-SILO</td>
<td></td>
<td><a href="https://github.com/pragmaticBIM/pragmaticbim-reference/blob/main/products/sfp-silo.yaml">Reference</a></td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Silo</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Temporaeres Silo fuer Schuettgut wie Zement, Kalk oder Gips.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Silo</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Temporary silo for bulk material such as cement, lime, or plaster.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>SFP-SKIP-BAY</td>
<td></td>
<td><a href="https://github.com/pragmaticBIM/pragmaticbim-reference/blob/main/products/sfp-skip-bay.yaml">Reference</a></td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Muldenplatz</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Abstellplatz fuer Abfallmulden, die per Lastwagen getauscht werden.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Skip bay</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Set-down place for waste skips that are exchanged by truck.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>SFP-STORAGE</td>
<td></td>
<td><a href="https://github.com/pragmaticBIM/pragmaticbim-reference/blob/main/products/sfp-storage.yaml">Reference</a></td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Lagerfläche</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Offene Flaeche auf der Baustelle fuer Material, das nicht in einem abschliessbaren Magazin liegt.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note">Offene Lagerung. Ein abschliessbares Magazin ist SFP-STORE. Temporaeres Halten zwischen Anlieferung und Verwendung ist SFP-BUFFER. Ein allgemeiner Container ist SFP-CONTAINER.</td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Storage area</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Open area on site for storing materials that are not kept in a lockable store.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note">Open storage. A lockable store is SFP-STORE. Temporary holding between delivery and use is SFP-BUFFER. A generic container is SFP-CONTAINER.</td>
</tr>
<tr>
<td>SFP-STORE</td>
<td></td>
<td><a href="https://github.com/pragmaticBIM/pragmaticbim-reference/blob/main/products/sfp-store.yaml">Reference</a></td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Magazin</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Abschliessbares Magazin fuer Werkzeug, Kleinmaterial und Geraete, die gesichert werden muessen.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note">Nicht SFP-STORAGE, nicht SFP-BUFFER und nicht SFP-CONTAINER. Lagerflaeche ist offene Lagerung; Zwischenlager ist temporaeres Halten; Container ist unspezifisch.</td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Site store</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Lockable store for tools, small materials, and equipment that must be secured.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note">Not SFP-STORAGE, not SFP-BUFFER, and not SFP-CONTAINER. Storage area is open storage; intermediate storage is temporary holding; container is unspecific.</td>
</tr>
<tr>
<td>SFP-TRANSFER</td>
<td></td>
<td><a href="https://github.com/pragmaticBIM/pragmaticbim-reference/blob/main/products/sfp-transfer.yaml">Reference</a></td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Umschlagplatz</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Flaeche, auf der Material zwischen Lieferfahrzeugen, Baustellengeraeten und Lager umgeschlagen wird.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note">Umschlagpunkt, keine Warteflaeche. Material, das vor dem Einbau wartet, ist SFP-BUFFER. Offene Lagerung ist SFP-STORAGE.</td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Transfer area</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Area where materials are transferred between delivery vehicles, site plant, and storage.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note">Handling point, not a holding area. Material that waits before installation is SFP-BUFFER. Open storage is SFP-STORAGE.</td>
</tr>
<tr>
<td>SFP-TURNING</td>
<td></td>
<td><a href="https://github.com/pragmaticBIM/pragmaticbim-reference/blob/main/products/sfp-turning.yaml">Reference</a></td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Wendefläche</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Flaeche, die so bemessen ist, dass Lastwagen auf der Baustelle wenden koennen.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note">Nicht SFP-HAUL-ROAD und nicht SFP-RAMP.</td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Turning area</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Area sized for trucks to turn on site.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note">Not SFP-HAUL-ROAD and not SFP-RAMP.</td>
</tr>
<tr>
<td>SFP-WATER-CONN</td>
<td></td>
<td><a href="https://github.com/pragmaticBIM/pragmaticbim-reference/blob/main/products/sfp-water-conn.yaml">Reference</a></td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Bauwasseranschluss</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Temporaerer Wasseranschluss und die Verteilung, die die Baustelle versorgt.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note">Gegenstueck zu SFP-POWER-DIST. Wasserversorgung, nicht elektrische Verteilung.</td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Site water connection</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Temporary water connection and distribution that supplies the site.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note">Counterpart of SFP-POWER-DIST. Water supply, not electrical distribution.</td>
</tr>
<tr>
<td>SFP-WHEEL-WASH</td>
<td></td>
<td><a href="https://github.com/pragmaticBIM/pragmaticbim-reference/blob/main/products/sfp-wheel-wash.yaml">Reference</a></td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Reifenwaschanlage</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Reifenwasch- oder Durchfahrtsreinigungsanlage am Baustellenausgang.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Wheel wash</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Wheel-wash or drive-through cleaning plant at the site exit.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
</tbody>
</table>
</div>
