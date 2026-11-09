"""Source data for the abstract cost project types, cost groups and their code-only mappings.

Labels and definitions are original wording. ICMS, eBKP-H and eBKP-T are referenced by code only.

Mapping specs use the compact form ``"close:C01 C02|narrow:D05|related:B04"`` where the key is the
SKOS mapping predicate (exact, close, broad, narrow, related) and the values are target notations.
"""

from __future__ import annotations

from dataclasses import dataclass, field

CPT_NS = "https://example.org/abstract/cost-project-type/"
CG_NS = "https://example.org/abstract/cost-group/"
ICMS_NS = "https://example.org/icms/3/"
EBKPH_NS = "https://example.org/ch/ebkp-h/"
EBKPT_NS = "https://example.org/ch/ebkp-t/"

BUILDINGS = "CPT-01"
MAIN_CIVIL = ("CPT-02", "CPT-03", "CPT-04", "CPT-05", "CPT-06", "CPT-07", "CPT-08")
WATER_CIVIL = ("CPT-13", "CPT-16", "CPT-17", "CPT-18", "CPT-19")


@dataclass(frozen=True)
class ProjectType:
    code: str
    label_en: str
    label_de: str
    definition_en: str
    definition_de: str
    civil: bool = True


@dataclass(frozen=True)
class Category:
    digit: str
    label_en: str
    label_de: str
    definition_en: str
    definition_de: str


@dataclass(frozen=True)
class Group:
    category: str
    code: str
    label_en: str
    label_de: str
    definition_en: str
    definition_de: str
    ebkph: str = ""
    ebkpt: str = ""


@dataclass(frozen=True)
class SubGroup:
    category: str
    group: str
    code: str
    label_en: str
    label_de: str
    definition_en: str
    definition_de: str
    project_types: tuple[str, ...] = ()
    ebkph: str = ""
    ebkpt: str = ""
    own: bool = False
    icms_tables: tuple[str, ...] = field(default=())


PROJECT_TYPES: list[ProjectType] = [
    ProjectType("CPT-01", "Buildings", "Gebäude", "Enclosed constructions providing shelter for occupants or contents, including their site works.", "Umschlossene Bauwerke, die Personen oder Gütern Schutz bieten, einschliesslich Umgebungsarbeiten.", civil=False),
    ProjectType("CPT-02", "Roads and runways", "Strassen und Pisten", "Road carriageways, highways, airfield runways, taxiways and aprons.", "Strassen, Autobahnen sowie Start- und Landebahnen, Rollwege und Vorfelder von Flugplätzen."),
    ProjectType("CPT-03", "Railways", "Bahnanlagen", "Heavy rail, light rail, tram and metro lines including track, power supply and signalling.", "Eisenbahn-, Stadtbahn-, Tram- und Metrolinien einschliesslich Fahrbahn, Bahnstromversorgung und Sicherungsanlagen."),
    ProjectType("CPT-04", "Bridges", "Brücken", "Structures carrying a traffic route or utility across an obstacle.", "Bauwerke, die einen Verkehrsweg oder eine Leitung über ein Hindernis führen."),
    ProjectType("CPT-05", "Tunnels", "Tunnel", "Underground passages for traffic, utilities or water, bored, mined or cut-and-cover.", "Unterirdische Bauwerke für Verkehr, Leitungen oder Wasser, im Vortrieb oder im Tagbau erstellt."),
    ProjectType("CPT-06", "Wastewater treatment works", "Abwasserreinigungsanlagen", "Plants that collect, treat and discharge sewage and industrial wastewater.", "Anlagen zur Sammlung, Reinigung und Ableitung von kommunalem und industriellem Abwasser."),
    ProjectType("CPT-07", "Water treatment works", "Wasseraufbereitungsanlagen", "Plants that abstract, treat and store drinking or process water.", "Anlagen zur Fassung, Aufbereitung und Speicherung von Trink- oder Brauchwasser."),
    ProjectType("CPT-08", "Pipelines", "Rohrleitungen", "Long-distance and distribution pipelines and cable routes for water, gas, oil, heat or energy.", "Fern- und Verteilleitungen sowie Kabeltrassen für Wasser, Gas, Öl, Wärme oder Energie."),
    ProjectType("CPT-09", "Wells and boreholes", "Brunnen und Bohrungen", "Drilled or dug wells and boreholes for water, energy or resources.", "Gebohrte oder gegrabene Brunnen und Bohrungen für Wasser, Energie oder Rohstoffe."),
    ProjectType("CPT-10", "Power generation plants", "Kraftwerke", "Plants that generate electricity or heat from any energy source.", "Anlagen zur Erzeugung von Strom oder Wärme aus beliebigen Energieträgern."),
    ProjectType("CPT-11", "Chemical plants", "Chemieanlagen", "Process plants producing chemical substances.", "Prozessanlagen zur Herstellung chemischer Stoffe."),
    ProjectType("CPT-12", "Refineries", "Raffinerien", "Process plants refining crude oil or other raw materials.", "Prozessanlagen zur Raffination von Rohöl oder anderen Rohstoffen."),
    ProjectType("CPT-13", "Dams and reservoirs", "Talsperren und Speicherbecken", "Barriers and basins that impound or store water.", "Sperrenbauwerke und Becken zum Aufstauen oder Speichern von Wasser."),
    ProjectType("CPT-14", "Mines and quarries", "Bergwerke und Steinbrüche", "Surface or underground extraction of minerals and rock.", "Ober- oder untertägiger Abbau von Mineralien und Gestein."),
    ProjectType("CPT-15", "Offshore works", "Offshore-Bauwerke", "Structures in open sea such as platforms and wind farm foundations.", "Bauwerke auf offener See wie Plattformen und Fundamente von Windparks."),
    ProjectType("CPT-16", "Near-shore works", "Küstennahe Bauwerke", "Coastal structures such as seawalls, breakwaters and outfalls.", "Bauwerke im Küstenbereich wie Ufermauern, Wellenbrecher und Auslaufbauwerke."),
    ProjectType("CPT-17", "Ports", "Häfen", "Harbour facilities including quays, berths, terminals and their land side.", "Hafenanlagen einschliesslich Kais, Liegeplätzen, Terminals und landseitiger Flächen."),
    ProjectType("CPT-18", "Waterway works", "Wasserbau an Gewässern", "Works on rivers, canals and lakes such as locks, weirs, bank protection and flood defence.", "Bauwerke an Flüssen, Kanälen und Seen wie Schleusen, Wehre, Uferschutz und Hochwasserschutz."),
    ProjectType("CPT-19", "Land formation and reclamation", "Landgewinnung und Geländeaufbau", "Creation of new land by filling, dredging or consolidation.", "Schaffung neuer Landflächen durch Aufschüttung, Baggerung oder Konsolidierung."),
]

CATEGORIES: list[Category] = [
    Category("1", "Acquisition", "Erwerb", "Costs of securing the site and of the client's administration, finance, legal and marketing activities.", "Kosten für die Sicherung des Grundstücks sowie für Verwaltung, Finanzierung, Recht und Vermarktung durch die Bauherrschaft."),
    Category("2", "Construction", "Erstellung", "Costs of creating the constructed asset from site preparation to handover, including design and supervision.", "Kosten für die Erstellung des Bauwerks von der Baustellenvorbereitung bis zur Übergabe, einschliesslich Planung und Bauleitung."),
    Category("3", "Renewal", "Erneuerung", "Costs of replacing major components at the end of their service life after handover.", "Kosten für den Ersatz wesentlicher Bauteile am Ende ihrer Nutzungsdauer nach der Übergabe."),
    Category("4", "Operation", "Betrieb", "Recurring costs of running the asset during use.", "Wiederkehrende Kosten für den Betrieb des Bauwerks während der Nutzung."),
    Category("5", "Maintenance", "Instandhaltung", "Costs of keeping the asset in working condition through inspection, servicing and repair.", "Kosten für den Erhalt der Funktionsfähigkeit durch Inspektion, Wartung und Reparatur."),
    Category("6", "End of life", "Lebensende", "Costs of decommissioning, demolishing and reinstating at the end of the asset's life.", "Kosten für Ausserbetriebnahme, Rückbau und Wiederherstellung am Ende der Lebensdauer."),
]

# Level 3 groups shared by construction, renewal and maintenance.
WORKS_GROUPS: list[tuple[str, str, str, str, str]] = [
    ("01", "Demolition, site preparation and formation", "Rückbau, Baustellenvorbereitung und Geländeformung", "Investigation, clearance, demolition, remediation and forming of the site before the permanent works.", "Untersuchung, Räumung, Rückbau, Sanierung und Formung des Geländes vor den dauerhaften Arbeiten."),
    ("02", "Substructure", "Unterbau", "Ground-related works that transfer loads into the ground, up to the top of the lowest floor or formation level.", "Erdberührte Arbeiten, die Lasten in den Baugrund abtragen, bis Oberkante der untersten Bodenplatte bzw. des Planums."),
    ("03", "Structure", "Tragwerk", "Load-bearing construction above the substructure.", "Tragende Konstruktion oberhalb des Unterbaus."),
    ("04", "Architectural and non-structural works", "Ausbau und nichttragende Arbeiten", "Envelope, partitions, finishes, fittings and other non-load-bearing construction.", "Gebäudehülle, Trennwände, Beläge, Einbauten und weitere nichttragende Konstruktionen."),
    ("05", "Services and equipment", "Technische Anlagen und Ausrüstung", "Mechanical, electrical, plumbing, transport and specialist installations.", "Haustechnische, elektrische, sanitäre, fördertechnische und spezielle Anlagen."),
    ("06", "Surface and underground drainage", "Oberflächen- und Untergrundentwässerung", "Drainage of surface, storm and foul water outside the structure, including connections.", "Ableitung von Oberflächen-, Regen- und Schmutzwasser ausserhalb des Bauwerks, einschliesslich Anschlüssen."),
    ("07", "External and ancillary works", "Umgebungs- und Nebenarbeiten", "Retaining structures, enclosures, paving, landscaping and services within the site but outside the main structure.", "Stützbauwerke, Einfriedungen, Beläge, Begrünung und Werkleitungen auf dem Grundstück ausserhalb des Hauptbauwerks."),
    ("08", "Preliminaries and site overheads", "Baustellengemeinkosten", "Constructor's site management, temporary facilities, shared plant and general obligations not allocated to elements.", "Baustellenführung, provisorische Einrichtungen, gemeinsame Geräte und allgemeine Pflichten des Unternehmers, die keinem Element zugeordnet sind."),
    ("09", "Risk allowances", "Reserven und Teuerung", "Allowances for design development, contingencies, price level and exchange rate changes.", "Reserven für Projektentwicklung, Unvorhergesehenes, Teuerung und Wechselkursänderungen."),
    ("10", "Taxes and levies", "Steuern und Abgaben", "Taxes and levies on construction payments.", "Steuern und Abgaben auf Zahlungen für die Erstellung."),
    ("11", "Off-site works and utilities", "Arbeiten und Werkleitungen ausserhalb des Grundstücks", "Utility connections and public access works outside the site boundary.", "Werkleitungsanschlüsse und öffentliche Zufahrten ausserhalb der Grundstücksgrenze."),
    ("12", "Production equipment, furniture and loose fittings", "Betriebseinrichtungen, Mobiliar und Ausstattung", "Production and process equipment, furniture and loose items supplied for the use of the asset.", "Produktions- und Prozesseinrichtungen, Mobiliar und lose Ausstattung für die Nutzung des Bauwerks."),
    ("13", "Consultancy and supervision", "Planung, Beratung und Bauleitung", "Fees of designers and advisers, statutory approval charges, site supervision and testing authorities.", "Honorare von Planenden und Beratenden, behördliche Bewilligungsgebühren, Bauleitung und Prüfstellen."),
]

GROUPS: list[Group] = [
    Group("1", "01", "Site acquisition", "Grundstückserwerb", "Price and associated costs of securing land, building rights or existing property.", "Preis und Nebenkosten für den Erwerb von Land, Baurechten oder bestehenden Liegenschaften.", ebkph="close:A01|related:A02", ebkpt="close:A01|related:A02"),
    Group("1", "02", "Client administration, finance, legal and marketing", "Verwaltung, Finanzierung, Recht und Vermarktung der Bauherrschaft", "Client-side overheads, interest, legal, accounting, sales and leasing costs.", "Gemeinkosten der Bauherrschaft, Zinsen, Rechts-, Buchhaltungs-, Verkaufs- und Vermietungskosten.", ebkph="related:W03 W06", ebkpt="related:W03 W06"),
    Group("2", "01", "", "", "", "", ebkph="narrow:B01 B05 B06", ebkpt="narrow:L01 L04 M01"),
    Group("2", "02", "", "", "", "", ebkph="narrow:C01 B07 E01", ebkpt="narrow:M O01"),
    Group("2", "03", "", "", "", "", ebkph="narrow:C02 C03 C04", ebkpt="narrow:N O"),
    Group("2", "04", "", "", "", "", ebkph="narrow:E02 E03 F G", ebkpt="narrow:P R"),
    Group("2", "05", "", "", "", "", ebkph="narrow:D H", ebkpt="narrow:S T"),
    Group("2", "06", "", "", "", "", ebkph="related:B04 I01.02 I05.06", ebkpt="narrow:Q01 Q02"),
    Group("2", "07", "", "", "", "", ebkph="close:I", ebkpt="related:M08 R08"),
    Group("2", "08", "", "", "", "", ebkph="related:B02 B03 B08", ebkpt="narrow:L02 L03 L06"),
    Group("2", "09", "", "", "", "", ebkph="close:Y", ebkpt="close:Y"),
    Group("2", "10", "", "", "", "", ebkph="related:Z", ebkpt="related:Z"),
    Group("2", "11", "", "", "", "", ebkph="related:B04 B09.03", ebkpt="related:Q"),
    Group("2", "12", "", "", "", "", ebkph="narrow:J H01", ebkpt="related:T R08"),
    Group("2", "13", "", "", "", "", ebkph="close:V|related:W01", ebkpt="close:V|related:W01"),
    Group("4", "01", "Cleaning", "Reinigung", "Routine and periodic cleaning of the asset.", "Unterhalts- und periodische Reinigung des Bauwerks."),
    Group("4", "02", "Utilities", "Ver- und Entsorgungsmedien", "Energy, water and other supplied media consumed in use.", "Im Betrieb bezogene Energie, Wasser und weitere Medien."),
    Group("4", "03", "Waste management", "Abfallentsorgung", "Collection, sorting and disposal of operational waste.", "Sammlung, Trennung und Entsorgung von Betriebsabfällen."),
    Group("4", "04", "Security", "Sicherheit und Bewachung", "Guarding, access control and security services in use.", "Bewachung, Zutrittskontrolle und Sicherheitsdienste im Betrieb."),
    Group("4", "05", "Information and communication technology", "Informations- und Kommunikationstechnik", "Running costs of ICT services and networks.", "Betriebskosten von IKT-Diensten und Netzwerken."),
    Group("4", "06", "Operator overheads", "Betreibergemeinkosten", "Operator's management, staff and general obligations.", "Führung, Personal und allgemeine Pflichten der Betreiberin."),
    Group("4", "07", "Operation risk allowances", "Reserven Betrieb", "Allowances for uncertainty in operation costs.", "Reserven für Unsicherheiten der Betriebskosten."),
    Group("4", "08", "Operation taxes and levies", "Steuern und Abgaben Betrieb", "Taxes and levies on operation.", "Steuern und Abgaben auf den Betrieb."),
    Group("6", "01", "Disposal inspection", "Zustandsaufnahme vor Rückbau", "Survey of the asset and hazardous materials before disposal.", "Aufnahme des Bauwerks und der Schadstoffe vor dem Rückbau."),
    Group("6", "02", "Decommissioning and decontamination", "Ausserbetriebnahme und Dekontamination", "Taking the asset out of service and removing contaminants.", "Ausserbetriebnahme des Bauwerks und Entfernen von Schadstoffen."),
    Group("6", "03", "Demolition and material recovery", "Rückbau und Materialrückgewinnung", "Demolition, dismantling and recovery of reusable or recyclable material.", "Abbruch, Demontage und Rückgewinnung wiederverwendbarer oder rezyklierbarer Materialien."),
    Group("6", "04", "Reinstatement", "Wiederherstellung", "Restoring the site after demolition.", "Wiederherstellung des Geländes nach dem Rückbau."),
    Group("6", "05", "End-of-life site overheads", "Baustellengemeinkosten Rückbau", "Constructor's site overheads for end-of-life works.", "Baustellengemeinkosten des Unternehmers für Rückbauarbeiten."),
    Group("6", "06", "End-of-life risk allowances", "Reserven Rückbau", "Allowances for uncertainty in end-of-life costs.", "Reserven für Unsicherheiten der Rückbaukosten."),
    Group("6", "07", "End-of-life taxes and levies", "Steuern und Abgaben Rückbau", "Taxes and levies on end-of-life works.", "Steuern und Abgaben auf Rückbauarbeiten."),
]

B = (BUILDINGS,)
C = MAIN_CIVIL
CW = WATER_CIVIL


def _sg(group: str, code: str, en: str, de: str, def_en: str, def_de: str, *, pt: tuple[str, ...] = (), h: str = "", t: str = "", own: bool = False, category: str = "2") -> SubGroup:
    if code.startswith("B"):
        tables = ("B",)
    elif code.startswith("C"):
        tables = ("C",)
    elif category == "1":
        tables = ("A",)
    else:
        tables = ("B", "C")
    return SubGroup(category, group, code, en, de, def_en, def_de, pt, h, t, own, tables)


SUBGROUPS: list[SubGroup] = [
    # --- Acquisition (project independent) ---
    _sg("01", "010", "Land and rights purchase", "Kauf von Land und Rechten", "Price paid for land, building rights or existing property.", "Preis für Land, Baurechte oder bestehende Liegenschaften.", category="1", h="close:A01", t="close:A01"),
    _sg("01", "020", "Compensation to occupiers", "Entschädigung von Nutzenden", "Payments to existing occupiers or holders of rights.", "Zahlungen an bisherige Nutzende oder Berechtigte.", category="1", h="close:A02.06", t="close:A02.06"),
    _sg("01", "030", "Payment in lieu of site works", "Abgeltung statt Bauleistung", "Payments to previous owners for demolition or modification instead of carrying out the work.", "Zahlungen an Voreigentümer für Rückbau oder Anpassungen anstelle der Ausführung.", category="1", h="related:A01.03", t="related:A01.03"),
    _sg("01", "040", "Heritage and environment contributions", "Beiträge an Denkmal- und Umweltschutz", "Contributions required to preserve heritage, culture or environment.", "Beiträge zur Erhaltung von Denkmälern, Kultur oder Umwelt.", category="1"),
    _sg("01", "050", "Acquisition fees", "Nebenkosten Erwerb", "Agent, notary, land registry, survey and legal fees for the acquisition.", "Vermittlungs-, Notariats-, Grundbuch-, Vermessungs- und Anwaltskosten für den Erwerb.", category="1", h="narrow:A02.02 A02.03 A02.04 A02.05 A02.07", t="narrow:A02.02 A02.03 A02.04 A02.05 A02.07"),
    _sg("01", "060", "Acquisition taxes", "Steuern Erwerb", "Transfer and gains taxes and statutory charges on the acquisition.", "Handänderungs- und Gewinnsteuern sowie Abgaben auf den Erwerb.", category="1", h="close:A02.01", t="close:A02.01"),
    _sg("02", "010", "Client general overheads", "Allgemeine Gemeinkosten Bauherrschaft", "Share of the client's general office costs.", "Anteil der allgemeinen Bürokosten der Bauherrschaft.", category="1"),
    _sg("02", "020", "Client project administration", "Projektadministration Bauherrschaft", "Client's in-house project team, project office and related expenses.", "Internes Projektteam, Projektbüro und zugehörige Aufwendungen der Bauherrschaft.", category="1", h="related:V03.02", t="related:V03.02"),
    _sg("02", "030", "Interest and finance", "Zinsen und Finanzierung", "Interest and financing charges during the project.", "Zinsen und Finanzierungskosten während des Projekts.", category="1", h="close:W03", t="close:W03"),
    _sg("02", "040", "Client legal expenses", "Rechtskosten Bauherrschaft", "Legal costs not related to the acquisition.", "Rechtskosten, die nicht den Erwerb betreffen.", category="1", h="related:V03.06", t="related:V03.06"),
    _sg("02", "050", "Accounting", "Buchhaltung", "Accounting and audit costs of the project.", "Buchhaltungs- und Revisionskosten des Projekts.", category="1"),
    _sg("02", "060", "Sales, leasing and marketing", "Verkauf, Vermietung und Vermarktung", "Costs of selling, letting, advertising and promoting the asset.", "Kosten für Verkauf, Vermietung, Werbung und Vermarktung des Bauwerks.", category="1", h="close:W06|related:W04.02", t="close:W06|related:W04.02"),
    _sg("02", "070", "Sales and leasing taxes", "Steuern auf Verkauf und Vermietung", "Taxes and charges on sale or lease.", "Steuern und Abgaben auf Verkauf oder Vermietung.", category="1"),
    _sg("02", "080", "Operating licences and permits", "Betriebsbewilligungen", "Licences and permits required to use or operate the asset.", "Bewilligungen für Nutzung oder Betrieb des Bauwerks.", category="1", h="broad:W01", t="broad:W01"),

    # --- Construction: buildings, group 01 ---
    _sg("01", "B010", "Site investigation and survey", "Baugrunduntersuchung und Bestandsaufnahme", "Ground investigation, topographic and condition surveys.", "Baugrunduntersuchungen, Geländeaufnahmen und Zustandsaufnahmen.", pt=B, h="narrow:B01.01 B01.02"),
    _sg("01", "B020", "Environmental remediation", "Altlastensanierung", "Treatment or removal of contaminated ground.", "Behandlung oder Entfernung von belastetem Untergrund.", pt=B, h="close:B06.02|related:B05.03"),
    _sg("01", "B030", "Hazardous material sampling", "Schadstoffbeprobung", "Sampling and testing for hazardous or useful materials.", "Beprobung und Prüfung auf Schadstoffe oder verwertbare Materialien.", pt=B, h="close:B01.03"),
    _sg("01", "B040", "Temporary site fencing", "Provisorische Bauabschrankung", "Temporary fencing and hoarding before the main works.", "Provisorische Abschrankungen vor den Hauptarbeiten.", pt=B, h="broad:B02.07"),
    _sg("01", "B050", "Demolition and support of adjacent structures", "Rückbau und Sicherung angrenzender Bauwerke", "Demolition of existing buildings and temporary support to neighbours.", "Rückbau bestehender Gebäude und Sicherung angrenzender Bauwerke.", pt=B, h="narrow:B05.02 B05.03 B09.02"),
    _sg("01", "B060", "Site clearance", "Baufeldräumung", "Clearing, grubbing, topsoil stripping and tree felling.", "Räumen, Roden, Oberbodenabtrag und Baumfällung.", pt=B, h="close:B05.01"),
    _sg("01", "B070", "Tree transplanting", "Baumverpflanzung", "Lifting and replanting existing trees.", "Ausheben und Verpflanzen bestehender Bäume.", pt=B, h="broad:B05.01"),
    _sg("01", "B080", "Site formation and slope treatment", "Geländeformung und Böschungssicherung", "Shaping of the site and stabilisation of slopes.", "Formung des Geländes und Sicherung von Böschungen.", pt=B, h="narrow:I01.01 B06.03"),
    _sg("01", "B090", "Temporary drainage and dewatering", "Provisorische Entwässerung und Wasserhaltung", "Temporary surface drainage and groundwater control.", "Provisorische Oberflächenentwässerung und Wasserhaltung.", pt=B, h="close:B06.06"),
    _sg("01", "B100", "Temporary utility protection and diversion", "Provisorische Sicherung und Umlegung von Werkleitungen", "Protecting, diverting or relocating existing utilities.", "Sichern, Umlegen oder Verlegen bestehender Werkleitungen.", pt=B, h="close:B03.02"),
    _sg("01", "B110", "Erosion control", "Erosionsschutz", "Measures preventing soil erosion during works.", "Massnahmen gegen Bodenerosion während der Arbeiten.", pt=B, h="broad:B06|related:I03.08"),

    # --- Construction: buildings, group 02 ---
    _sg("02", "B010", "Piling and underpinning", "Pfählung und Unterfangung", "Piles, caissons, pile testing and underpinning of the building.", "Pfähle, Senkkästen, Pfahlprüfungen und Unterfangungen des Gebäudes.", pt=B, h="narrow:B07.02 B07.03"),
    _sg("02", "B020", "Foundations and lowest floor", "Fundamente und unterste Bodenplatte", "Footings, pile caps, ground beams, lowest floor slab and lift pits, including excavation.", "Fundamente, Pfahlkopfbalken, Fundamentbalken, unterste Bodenplatte und Liftunterfahrten, einschliesslich Aushub.", pt=B, h="narrow:C01.01 C01.02 C01.03 C01.04 C01.05|related:B06.01 B06.04"),
    _sg("02", "B030", "Basement walls and bottom", "Untergeschosswände und -boden", "Basement retaining walls, bottom slabs, tanking, drainage blanket and insulation.", "Erdberührte Untergeschosswände, Bodenplatten, Abdichtung, Sickerschicht und Wärmedämmung.", pt=B, h="narrow:C02.01 C01.03 E01.01 E01.02 E01.03|related:B06.04"),

    # --- Construction: buildings, group 03 ---
    _sg("03", "B010", "Structural alterations", "Tragwerksanpassungen", "Removal and alteration of existing load-bearing construction.", "Rückbau und Anpassung bestehender tragender Konstruktion.", pt=B, h="related:C05.01 B05.02"),
    _sg("03", "B020", "Below-ground suspended structure", "Tragwerk unter Terrain", "Walls, columns, suspended slabs and stairs between lowest floor and ground floor.", "Wände, Stützen, Decken und Treppen zwischen unterster Bodenplatte und Erdgeschoss.", pt=B, h="broad:C02 C03 C04"),
    _sg("03", "B030", "Frame and floors above ground", "Tragwerk über Terrain", "Load-bearing walls, columns, floors, roof structure and stairs above ground floor.", "Tragende Wände, Stützen, Decken, Dachkonstruktion und Treppen oberhalb des Erdgeschosses.", pt=B, h="narrow:C02.01 C02.02 C03.01 C03.02 C04.01 C04.02 C04.03 C04.04 C04.05 C04.06 C04.07 C04.08"),
    _sg("03", "B040", "Structural tanks, pools and sundries", "Tragende Becken und Ergänzungen", "Structural tanks, pools, plinths and minor structural items.", "Tragende Becken, Sockel und kleinere tragende Bauteile.", pt=B, h="related:C05.02"),
    _sg("03", "B050", "Prefabricated or composite structure", "Vorgefertigtes oder Verbundtragwerk", "Structure supplied as prefabricated or composite systems.", "Tragwerk als vorgefertigtes oder Verbundsystem geliefert.", pt=B, h="broad:C"),

    # --- Construction: buildings, group 04 ---
    _sg("04", "B010", "Non-structural alterations", "Anpassungen nichttragender Bauteile", "Removal and alteration of existing non-load-bearing construction.", "Rückbau und Anpassung bestehender nichttragender Bauteile.", pt=B, h="related:B05.02 G06.01"),
    _sg("04", "B020", "External envelope", "Gebäudehülle Fassade", "External wall finishes, cladding, curtain walls, windows, external doors and shutters.", "Äussere Wandbekleidungen, Fassadenbekleidungen, Vorhangfassaden, Fenster, Aussentüren und Abschlüsse.", pt=B, h="narrow:E02 E03"),
    _sg("04", "B030", "Roof coverings and rooflights", "Bedachung und Oblichter", "Roof finishes, waterproofing, insulation, skylights and roof landscaping.", "Dachhaut, Abdichtung, Dämmung, Oblichter und Dachbegrünung.", pt=B, h="narrow:F01 F02"),
    _sg("04", "B040", "Internal divisions", "Innenwände und Innentüren", "Non-load-bearing partitions, internal doors, windows and shutters.", "Nichttragende Trennwände, Innentüren, Innenfenster und Abschlüsse.", pt=B, h="close:G01"),
    _sg("04", "B050", "Fittings and sundries", "Einbauten und Ergänzungen", "Balustrades, built-in cabinets, signs and other fixed fittings.", "Geländer, Einbauschränke, Beschriftungen und weitere feste Einbauten.", pt=B, h="close:G05|related:J01.04 E03.05"),
    _sg("04", "B060", "Internal finishes", "Innenbeläge und -bekleidungen", "Floor, wall and ceiling finishes under cover.", "Boden-, Wand- und Deckenbeläge in überdeckten Bereichen.", pt=B, h="narrow:G02 G03 G04"),
    _sg("04", "B070", "Builder's work for services", "Baumeisterarbeiten für Installationen", "Plinths, openings, sleeves, enclosures and fire stopping for services.", "Sockel, Durchbrüche, Hülsen, Verkleidungen und Abschottungen für Installationen.", pt=B, h="narrow:C05.01 C05.02 G06.01 G06.02"),
    _sg("04", "B080", "Prefabricated or composite non-structural work", "Vorgefertigte nichttragende Systeme", "Envelope or fit-out supplied as prefabricated systems.", "Hülle oder Ausbau als vorgefertigte Systeme geliefert.", pt=B, h="related:E02.04 F01.04"),

    # --- Construction: buildings, group 05 ---
    _sg("05", "B010", "Heating, ventilation and air conditioning", "Heizung, Lüftung und Klima", "Heat and cold generation, distribution and emission, and air handling.", "Wärme- und Kälteerzeugung, -verteilung und -abgabe sowie Lufttechnik.", pt=B, h="narrow:D05 D06 D07"),
    _sg("05", "B020", "Electrical power", "Starkstromanlagen", "Incoming supply, transformation, storage, distribution and power outlets.", "Einspeisung, Transformierung, Speicherung, Verteilung und Anschlüsse Starkstrom.", pt=B, h="narrow:D01.01 D01.02 D01.03 D01.04 D01.06"),
    _sg("05", "B030", "Lighting fittings", "Leuchten", "Supply and installation of light fittings.", "Lieferung und Montage von Leuchten.", pt=B, h="close:D01.05"),
    _sg("05", "B040", "Low-voltage, communication and automation", "Schwachstrom, Kommunikation und Automation", "ICT cabling, building automation, security and alarm systems.", "IKT-Verkabelung, Gebäudeautomation, Sicherheits- und Alarmanlagen.", pt=B, h="narrow:D01.07 D01.08 D01.09 D01.10 D01.11 D02 D03"),
    _sg("05", "B050", "Water supply and drainage in the building", "Wasserversorgung und Entwässerung im Gebäude", "Cold and hot water, grey water and internal waste and rainwater drainage.", "Kalt- und Warmwasser, Grauwasser sowie interne Schmutz- und Regenwasserableitung.", pt=B, h="narrow:D08 D09"),
    _sg("05", "B060", "Sanitary fittings", "Sanitärapparate", "Supply of sanitary appliances and fixtures.", "Lieferung von Sanitärapparaten und -ausstattung.", pt=B, h="close:D08.05|related:D08.06"),
    _sg("05", "B070", "Waste disposal systems", "Abfallentsorgungsanlagen", "Refuse, laboratory and industrial waste systems.", "Anlagen für Kehricht-, Labor- und Industrieabfälle.", pt=B, h="broad:H09|related:D09.01"),
    _sg("05", "B080", "Fire protection systems", "Brandschutzanlagen", "Sprinklers, hydrants, extinguishing, detection and alarm systems.", "Sprinkler, Hydranten, Löschanlagen, Brandmelde- und Alarmanlagen.", pt=B, h="close:D04"),
    _sg("05", "B090", "Gas and special media", "Gas und Spezialmedien", "Fuel gas, medical, laboratory and industrial gases, compressed air and vacuum.", "Brenngas, medizinische, Labor- und Industriegase, Druckluft und Vakuum.", pt=B, h="narrow:D10 D11"),
    _sg("05", "B100", "Lifts and conveyors", "Aufzüge und Förderanlagen", "Lifts, platform lifts, escalators, moving walks and conveyors.", "Aufzüge, Plattformlifte, Fahrtreppen, Fahrsteige und Förderanlagen.", pt=B, h="close:D12"),
    _sg("05", "B110", "Facade access equipment", "Fassadenbefahranlagen", "Gondolas and building maintenance units.", "Fassadenbefahranlagen und Gondeln.", pt=B, h="related:D12.03"),
    _sg("05", "B120", "Turntables", "Drehscheiben", "Vehicle and stage turntables.", "Drehscheiben für Fahrzeuge und Bühnen.", pt=B, h="related:H09.06"),
    _sg("05", "B130", "Generators", "Notstromaggregate", "Standby and emergency generators.", "Ersatz- und Notstromaggregate.", pt=B, h="broad:D01.01"),
    _sg("05", "B140", "Energy-saving and renewable systems", "Energiesparende und erneuerbare Anlagen", "Photovoltaics, heat recovery and similar energy-saving features.", "Photovoltaik, Wärmerückgewinnung und ähnliche energiesparende Anlagen.", pt=B, h="related:D01.01 D05.02"),
    _sg("05", "B150", "Water and wastewater treatment equipment", "Wasser- und Abwasserbehandlungsanlagen", "Treatment plant serving the building.", "Behandlungsanlagen für das Gebäude.", pt=B, h="narrow:D08.02 D09.02"),
    _sg("05", "B160", "Fountains and pool plant", "Brunnen- und Beckentechnik", "Filtration and plant for fountains and pools.", "Filtration und Technik für Brunnen und Becken.", pt=B, h="broad:H07|related:I03.07"),
    _sg("05", "B170", "Powered signage", "Elektrische Beschriftung", "Illuminated and electronic signs.", "Beleuchtete und elektronische Beschriftungen.", pt=B, h="related:J01.04 D01.06"),
    _sg("05", "B175", "Audio-visual systems", "Audiovisuelle Anlagen", "Audio-visual and entertainment systems.", "Audiovisuelle und Unterhaltungsanlagen.", pt=B, h="broad:H06"),
    _sg("05", "B180", "Commercial kitchen equipment", "Grossküchenanlagen", "Catering kitchen plant and appliances.", "Grossküchentechnik und -geräte.", pt=B, h="close:H03"),
    _sg("05", "B190", "Cold room equipment", "Kühlzellen", "Cold and freezer rooms.", "Kühl- und Tiefkühlzellen.", pt=B, h="close:H09.08"),
    _sg("05", "B200", "Laboratory equipment", "Laboreinrichtungen", "Fixed laboratory installations.", "Feste Laborinstallationen.", pt=B, h="close:H02"),
    _sg("05", "B210", "Medical equipment", "Medizinische Einrichtungen", "Fixed medical installations.", "Feste medizinische Installationen.", pt=B, h="close:H05"),
    _sg("05", "B220", "Hotel equipment", "Hoteleinrichtungen", "Fixed hotel-specific equipment.", "Feste hotelspezifische Einrichtungen.", pt=B, h="broad:H09"),
    _sg("05", "B230", "Parking and entrance access control", "Park- und Zutrittskontrolle", "Barrier, ticketing and entrance control systems.", "Schranken-, Ticket- und Zutrittskontrollsysteme.", pt=B, h="related:D03.02 H09.06"),
    _sg("05", "B240", "Domestic appliances", "Haushaltgeräte", "Built-in household appliances.", "Eingebaute Haushaltgeräte.", pt=B, h="related:G05.02 D01.06"),
    _sg("05", "B250", "Other specialist installations", "Weitere Spezialanlagen", "Use-specific installations not listed elsewhere.", "Nutzungsspezifische Anlagen, die nicht anderweitig erfasst sind.", pt=B, h="broad:H"),
    _sg("05", "B260", "Main contractor attendance on services", "Unternehmerleistungen für Installationen", "Main contractor's profit and attendance on services trades.", "Zuschläge und Hilfeleistungen des Hauptunternehmers für Installationsgewerke.", pt=B),

    # --- Construction: buildings, group 06 ---
    _sg("06", "B010", "Surface water drainage", "Oberflächenentwässerung", "Drainage of paved and landscaped surfaces.", "Entwässerung befestigter und begrünter Flächen.", pt=B, h="close:I05.06"),
    _sg("06", "B020", "Storm water drainage", "Regenwasserableitung", "Below-ground storm water pipes and structures.", "Erdverlegte Regenwasserleitungen und -bauwerke.", pt=B, h="narrow:B04.07|related:I01.02"),
    _sg("06", "B030", "Foul and wastewater drainage", "Schmutzwasserableitung", "Below-ground foul water pipes and structures.", "Erdverlegte Schmutzwasserleitungen und -bauwerke.", pt=B, h="close:B04.06|related:I01.02"),
    _sg("06", "B040", "Drainage connections", "Kanalisationsanschlüsse", "Disconnections and connections to drains.", "Trennungen und Anschlüsse an die Kanalisation.", pt=B, h="broad:B04"),
    _sg("06", "B050", "Drain inspection", "Kanalinspektion", "Camera inspection of existing or new drains.", "Kamerainspektion bestehender oder neuer Leitungen.", pt=B, h="related:B01.04"),
    _sg("06", "B060", "Buried process pipes", "Erdverlegte Prozessleitungen", "Buried pipework for process media.", "Erdverlegte Leitungen für Prozessmedien.", pt=B, h="related:H01.04 D11.04"),

    # --- Construction: buildings, group 07 ---
    _sg("07", "B010", "Retaining structures", "Stützbauwerke", "Permanent retaining walls and slope protection in the site.", "Dauerhafte Stützmauern und Böschungsverbau auf dem Grundstück.", pt=B, h="narrow:I02.01 I02.02"),
    _sg("07", "B020", "Site enclosures and divisions", "Einfriedungen", "Fences, walls and gates around and within the site.", "Zäune, Mauern und Tore um und auf dem Grundstück.", pt=B, h="close:I02.08|related:I02.03"),
    _sg("07", "B030", "Ancillary structures", "Nebenbauten", "Small detached and underground structures in the site.", "Kleinbauten und unterirdische Bauwerke auf dem Grundstück.", pt=B, h="narrow:I02.05 I02.06"),
    _sg("07", "B040", "Roads and paving", "Verkehrsflächen und Beläge", "Hard surfaces, paths and site roads.", "Hartflächen, Wege und Zufahrten auf dem Grundstück.", pt=B, h="close:I04"),
    _sg("07", "B050", "Landscaping", "Begrünung und Geländegestaltung", "Soft and hard landscaping and ground modelling.", "Grünflächen, Gestaltung und Geländemodellierung.", pt=B, h="narrow:I01.01 I03"),
    _sg("07", "B060", "External fittings and equipment", "Ausstattung Umgebung", "Furniture, play equipment and waste stations outside.", "Mobiliar, Spielgeräte und Entsorgungsstellen im Aussenraum.", pt=B, h="close:I06"),
    _sg("07", "B070", "External services", "Werkleitungen Umgebung", "Water, gas, power, communications and lighting in the site.", "Wasser, Gas, Strom, Kommunikation und Beleuchtung auf dem Grundstück.", pt=B, h="close:I05|related:B04"),

    # --- Construction: civil works, group 01 ---
    _sg("01", "C010", "Site investigation and survey", "Untersuchung und Vermessung", "Ground investigation, surveys and condition records.", "Baugrunduntersuchung, Vermessung und Zustandsaufnahmen.", pt=C, t="close:L01"),
    _sg("01", "C020", "Environmental remediation", "Altlastensanierung", "Treatment or removal of contaminated ground.", "Behandlung oder Entfernung von belastetem Untergrund.", pt=C, t="close:M04"),
    _sg("01", "C030", "Hazardous material sampling", "Schadstoffbeprobung", "Sampling and testing for hazardous or useful materials.", "Beprobung und Prüfung auf Schadstoffe oder verwertbare Materialien.", pt=C, t="broad:L01"),
    _sg("01", "C040", "Temporary fencing", "Provisorische Abschrankung", "Temporary fencing before the main works.", "Provisorische Abschrankungen vor den Hauptarbeiten.", pt=C, t="broad:L02"),
    _sg("01", "C050", "Demolition of existing structures", "Rückbau bestehender Bauwerke", "Demolition and support to adjacent structures.", "Rückbau und Sicherung angrenzender Bauwerke.", pt=C, t="close:L04"),
    _sg("01", "C060", "Site clearance", "Baufeldräumung", "Clearing, grubbing, topsoil stripping and tree felling.", "Räumen, Roden, Oberbodenabtrag und Baumfällung.", pt=C, t="narrow:M01.01 M01.02"),
    _sg("01", "C070", "Tree transplanting", "Baumverpflanzung", "Lifting and replanting existing trees.", "Ausheben und Verpflanzen bestehender Bäume.", pt=C, t="broad:M01.01"),
    _sg("01", "C080", "General earthworks and slope treatment", "Allgemeine Erdarbeiten und Böschungssicherung", "Cut, fill and slope treatment serving more than one sub-project.", "Abtrag, Schüttung und Böschungssicherung für mehrere Teilprojekte.", pt=C, t="narrow:M01.03 M01.05 M05"),
    _sg("01", "C090", "Temporary drainage and dewatering", "Provisorische Entwässerung und Wasserhaltung", "Temporary surface drainage and groundwater control.", "Provisorische Oberflächenentwässerung und Wasserhaltung.", pt=C, t="close:M01.08"),
    _sg("01", "C100", "Temporary access roads and storage areas", "Provisorische Zufahrten und Lagerflächen", "Temporary roads and laydown areas let under an advance contract.", "Provisorische Zufahrten und Lagerflächen aus einem Vorabvertrag.", pt=C, t="broad:L03"),
    _sg("01", "C110", "Temporary utility protection and diversion", "Provisorische Sicherung und Umlegung von Werkleitungen", "Protecting, diverting or relocating existing utilities.", "Sichern, Umlegen oder Verlegen bestehender Werkleitungen.", pt=C, t="broad:L03"),
    _sg("01", "C120", "Erosion control", "Erosionsschutz", "Measures preventing soil erosion during works.", "Massnahmen gegen Bodenerosion während der Arbeiten.", pt=C, t="broad:M05|related:M08"),
    _sg("01", "C650", "Dredging", "Nassbaggerung", "Dredging of sediments and rock including transport and disposal.", "Baggerung von Sedimenten und Fels einschliesslich Transport und Ablagerung.", pt=CW, t="broad:M01"),

    # --- Construction: civil works, group 02 ---
    _sg("02", "C010", "Embankments and cuttings", "Dämme und Einschnitte", "Earthworks forming the route of a specific sub-project.", "Erdarbeiten zur Ausbildung des Trassees eines Teilprojekts.", pt=("CPT-02", "CPT-03", "CPT-08", "CPT-13"), t="narrow:M01.03 M01.05"),
    _sg("02", "C020", "Excavation and lateral support", "Aushub und Baugrubensicherung", "Excavation, disposal and temporary support to receive structures.", "Aushub, Abtransport und Baugrubensicherung für Bauwerke.", pt=C, t="narrow:M01.03 M07"),
    _sg("02", "C025", "Geotextiles and geomembranes", "Geotextilien und Geomembranen", "Separation, filter and sealing layers in the ground.", "Trenn-, Filter- und Dichtungslagen im Baugrund.", pt=C, t="broad:M05"),
    _sg("02", "C030", "Trenches", "Gräben", "Utility and common trenches including backfill.", "Leitungs- und Sammelgräben einschliesslich Verfüllung.", pt=C, t="narrow:M01.04 M01.07"),
    _sg("02", "C040", "Drilling and boring", "Bohrungen", "Drilled and bored works including trenchless installation.", "Bohrarbeiten einschliesslich grabenlosem Leitungsbau.", pt=C, t="related:M02"),
    _sg("02", "C050", "Piling and anchoring", "Pfählung und Verankerung", "Piles, ground anchors and their testing.", "Pfähle, Anker und deren Prüfung.", pt=C, t="related:O01 M07"),
    _sg("02", "C060", "Structural backfill and ground improvement", "Hinterfüllung und Baugrundverbesserung", "Backfill to structures and improvement of the ground.", "Hinterfüllung von Bauwerken und Verbesserung des Baugrunds.", pt=C, t="narrow:M01.06 M06"),
    _sg("02", "C070", "Earth-retaining structures", "Stützbauwerke", "Permanent retaining walls and slope securing.", "Dauerhafte Stützmauern und Hangsicherungen.", pt=C, t="close:M07"),
    _sg("02", "C080", "Abutments and wing walls", "Widerlager und Flügelmauern", "End supports and wing walls of bridges.", "Endauflager und Flügelmauern von Brücken.", pt=("CPT-04",), t="broad:O04"),
    _sg("02", "C090", "Footings and pile caps", "Fundamente und Pfahlkopfplatten", "Foundations nearest to ground or water level.", "Fundamente nahe der Gelände- oder Wasseroberfläche.", pt=C, t="close:O01"),
    _sg("02", "C100", "Sub-base to pavements and track", "Fundationsschicht Fahrbahn", "Unbound or bound layers beneath road pavements and rail track.", "Ungebundene oder gebundene Schichten unter Strassenbelägen und Gleisen.", pt=("CPT-02", "CPT-03"), t="broad:R01 R03"),
    _sg("02", "C110", "Bases for tanks, pipes and wells", "Fundamente für Behälter, Rohre und Brunnen", "Foundation bases for tanks, pipe supports and wells.", "Fundamente für Behälter, Rohrauflager und Brunnen.", pt=("CPT-06", "CPT-07", "CPT-08", "CPT-09"), t="broad:O01"),
    _sg("02", "C120", "Beds and surrounds to buried pipes", "Bettung und Umhüllung erdverlegter Leitungen", "Bedding, haunching and surround to buried pipes and cables.", "Bettung, Auflager und Umhüllung erdverlegter Rohre und Kabel.", pt=("CPT-06", "CPT-07", "CPT-08"), t="broad:Q"),
    _sg("02", "C660", "Rock revetments and gabions", "Blockwurf und Drahtschotterkörbe", "Rock armour, riprap and gabion protection.", "Blockwurf, Steinschüttungen und Drahtschotterkörbe.", pt=CW, t="broad:M07"),
    _sg("02", "C680", "Bank protection", "Uferschutz", "Protection of river and lake banks.", "Schutz von Fluss- und Seeufern.", pt=("CPT-13", "CPT-18"), t="broad:M07|related:M08"),

    # --- Construction: civil works, group 03 ---
    _sg("03", "C010", "Piers and pylons", "Pfeiler und Pylone", "Intermediate supports and towers of bridges.", "Zwischenstützen und Pylone von Brücken.", pt=("CPT-04",), t="broad:O04|related:O02"),
    _sg("03", "C020", "Suspension and cable systems", "Seil- und Hängesysteme", "Main cables, stays and hangers.", "Tragseile, Schrägseile und Hänger.", pt=("CPT-04",), t="broad:O05|related:O07"),
    _sg("03", "C030", "Bridge decks", "Brückenüberbau", "Deck structure spanning between supports.", "Überbau zwischen den Auflagern.", pt=("CPT-04",), t="close:O05"),
    _sg("03", "C040", "Bearings", "Brückenlager", "Bearings transferring deck loads to supports.", "Lager zur Übertragung der Überbaulasten auf die Stützen.", pt=("CPT-04",), t="broad:O06"),
    _sg("03", "C050", "Tunnel support and lining", "Tunnelsicherung und -ausbau", "Primary support and final lining of underground excavations.", "Sicherung und Ausbau von Hohlräumen im Untertagbau.", pt=("CPT-05",), t="narrow:N02 N03|related:N01"),
    _sg("03", "C060", "Road and track bases", "Tragschichten Strasse und Gleis", "Structural base layers of roads and track.", "Tragschichten von Strassen und Gleisen.", pt=("CPT-02", "CPT-03"), t="broad:R01 R03"),
    _sg("03", "C070", "Structural pavements", "Tragende Beläge", "Structural pavement layers of roads and runways.", "Tragende Belagsschichten von Strassen und Pisten.", pt=("CPT-02",), t="broad:R01"),
    _sg("03", "C080", "Service roads and approaches", "Nebenstrassen und Zufahrten", "Approach roads and service roads to the structure.", "Zufahrten und Dienststrassen zum Bauwerk.", pt=("CPT-02", "CPT-04", "CPT-05"), t="broad:R01"),
    _sg("03", "C090", "Parapets and edge details", "Brüstungen und Randabschlüsse", "Edge beams, parapets and edge treatment.", "Randbalken, Brüstungen und Randabschlüsse.", pt=("CPT-02", "CPT-04"), t="broad:O08|related:R06"),
    _sg("03", "C100", "Main structures", "Hauptbauwerke", "Primary walls, slabs, frames and special structures.", "Primäre Wände, Platten, Rahmen und Spezialkonstruktionen.", pt=C, t="narrow:O02 O03 O07"),
    _sg("03", "C105", "Utility service buildings", "Betriebsgebäude für Werkleitungen", "Small buildings housing utility plant.", "Kleinbauten für Werkleitungsanlagen.", pt=("CPT-06", "CPT-07", "CPT-08", "CPT-10"), t="related:P"),
    _sg("03", "C110", "Tanks and storage structures", "Behälter und Speicherbauwerke", "Tanks, basins and storage containers.", "Behälter, Becken und Speicherbauwerke.", pt=("CPT-06", "CPT-07", "CPT-13"), t="broad:O07"),
    _sg("03", "C120", "Supports for tanks and pipes", "Auflager für Behälter und Rohre", "Structural supports for tanks and pipework.", "Tragende Auflager für Behälter und Rohrleitungen.", pt=("CPT-06", "CPT-07", "CPT-08"), t="broad:O07"),
    _sg("03", "C130", "Civil pipework", "Rohrleitungen", "Pipework forming the main asset.", "Rohrleitungen als Hauptbestandteil der Anlage.", pt=("CPT-06", "CPT-07", "CPT-08"), t="narrow:Q02 Q03 Q04 Q05 Q09"),
    _sg("03", "C140", "Valves and fittings", "Armaturen und Formstücke", "Valves and fittings in pipework.", "Armaturen und Formstücke in Rohrleitungen.", pt=("CPT-06", "CPT-07", "CPT-08"), t="broad:Q"),
    _sg("03", "C700", "Locks and guide structures", "Schleusen und Leitwerke", "Navigation locks and guiding structures.", "Schiffsschleusen und Leitwerke.", pt=("CPT-18",), t="broad:O07"),
    _sg("03", "C720", "Flood defences", "Hochwasserschutzbauten", "Dykes, flood walls and barriers.", "Dämme, Hochwasserschutzmauern und Sperrwerke.", pt=("CPT-13", "CPT-16", "CPT-18"), t="broad:M07|related:O07"),
    _sg("03", "C750", "Weirs", "Wehre", "Fixed and movable weirs.", "Feste und bewegliche Wehre.", pt=("CPT-13", "CPT-18"), t="broad:O07"),

    # --- Construction: civil works, group 04 ---
    _sg("04", "C010", "Non-structural alterations", "Anpassungen nichttragender Bauteile", "Removal and alteration of existing non-structural parts.", "Rückbau und Anpassung bestehender nichttragender Bauteile.", pt=C, t="broad:L04"),
    _sg("04", "C020", "Non-structural construction and finishes", "Nichttragende Bauteile und Oberflächen", "Coatings, linings, cladding and built-in parts.", "Beschichtungen, Verkleidungen, Bekleidungen und Einbauten.", pt=C, t="close:P"),
    _sg("04", "C030", "Running surface", "Fahrbahnoberfläche", "Wearing course of roads and running surface of track.", "Deckschicht von Strassen und Fahrfläche von Gleisen.", pt=("CPT-02", "CPT-03", "CPT-04", "CPT-05"), t="narrow:R01 R03"),
    _sg("04", "C040", "Signs and markings", "Signalisation und Markierung", "Road signs, markings and similar.", "Signale, Markierungen und dergleichen.", pt=("CPT-02", "CPT-04", "CPT-05"), t="close:R02"),
    _sg("04", "C050", "Gantries", "Signalportale", "Sign and equipment gantries.", "Signal- und Ausrüstungsportale.", pt=("CPT-02", "CPT-03"), t="related:S04 R02"),
    _sg("04", "C060", "Safety facilities", "Sicherheitseinrichtungen", "Safety installations for users and staff.", "Sicherheitseinrichtungen für Nutzende und Personal.", pt=C, t="broad:S07|related:R05"),
    _sg("04", "C070", "Barriers, rails and access", "Rückhaltesysteme und Zugänge", "Vehicle restraint, handrails, ladders and walkways.", "Fahrzeugrückhaltesysteme, Handläufe, Leitern und Stege.", pt=C, t="close:R06"),
    _sg("04", "C080", "Special equipment and fittings", "Spezielle Ausrüstung", "Route-specific fittings not covered elsewhere.", "Trassenspezifische Ausrüstung, die nicht anderweitig erfasst ist.", pt=C, t="broad:R07|related:R08"),
    _sg("04", "C090", "Interior landscaping", "Innenbegrünung", "Planting within enclosed civil structures.", "Begrünung innerhalb geschlossener Tiefbauwerke.", pt=C, t="related:M08"),
    _sg("04", "C100", "Builder's work for services", "Baumeisterarbeiten für Installationen", "Openings, plinths and enclosures for equipment.", "Durchbrüche, Sockel und Verkleidungen für Ausrüstung.", pt=C, t="broad:P05|related:N04"),

    # --- Construction: civil works, group 05 ---
    _sg("05", "C005", "District heating and cooling", "Fernwärme und Fernkälte", "District heating and cooling networks.", "Fernwärme- und Fernkältenetze.", pt=("CPT-08",), t="close:Q05|related:T02 T03"),
    _sg("05", "C010", "Mechanical systems", "Mechanische Anlagen", "Ventilation, heating, cooling and pumping plant.", "Lüftungs-, Heiz-, Kühl- und Pumpanlagen.", pt=C, t="narrow:S03 T04|related:T02 T03"),
    _sg("05", "C020", "Lighting systems", "Beleuchtung", "Route, tunnel and area lighting.", "Strassen-, Tunnel- und Flächenbeleuchtung.", pt=C, t="close:S02"),
    _sg("05", "C030", "Feature lighting", "Effektbeleuchtung", "Decorative and architectural illumination.", "Dekorative und architektonische Beleuchtung.", pt=C, t="broad:S02"),
    _sg("05", "C040", "Low-voltage power supply", "Energieversorgung", "Power supply and distribution for equipment.", "Energieversorgung und -verteilung für Ausrüstung.", pt=C, t="close:S01|related:T01"),
    _sg("05", "C050", "Cables and cable routes", "Kabel und Kabelanlagen", "Cables, cable trays, duct banks and cable chambers.", "Kabel, Kabeltrassen, Rohrblöcke und Kabelschächte.", pt=C, t="narrow:Q06 Q07 Q08|related:N04"),
    _sg("05", "C060", "Other electrical services", "Weitere elektrische Anlagen", "Electrical installations not listed elsewhere.", "Elektrische Anlagen, die nicht anderweitig erfasst sind.", pt=C, t="broad:T01"),
    _sg("05", "C070", "Control and instrumentation", "Steuerung und Messtechnik", "Automation, communication and control systems.", "Automations-, Kommunikations- und Leitsysteme.", pt=C, t="close:S06|related:S05"),
    _sg("05", "C080", "Pipe racks", "Rohrbrücken", "Local supports for service pipes.", "Lokale Auflager für Leitungen.", pt=("CPT-06", "CPT-07", "CPT-10", "CPT-11", "CPT-12"), t="broad:Q09"),
    _sg("05", "C090", "Water supply and drainage in structures", "Wasser und Entwässerung im Bauwerk", "Water and drainage installations inside civil structures.", "Wasser- und Entwässerungsinstallationen in Tiefbauwerken.", pt=C, t="narrow:T05 T06"),
    _sg("05", "C100", "Refuse disposal systems", "Abfallentsorgungsanlagen", "Systems for collecting and removing refuse.", "Anlagen zur Sammlung und Entsorgung von Abfällen.", pt=C, t="related:T06"),
    _sg("05", "C110", "Fire services", "Brandschutzanlagen", "Detection, alarm and extinguishing systems.", "Melde-, Alarm- und Löschanlagen.", pt=C, t="close:S08"),
    _sg("05", "C115", "Gas services", "Gasanlagen", "Gas installations within structures.", "Gasinstallationen in Bauwerken.", pt=C, t="narrow:T07|related:Q04"),
    _sg("05", "C120", "Lifts and escalators", "Aufzüge und Fahrtreppen", "Lifts, escalators and moving walks.", "Aufzüge, Fahrtreppen und Fahrsteige.", pt=C, t="close:S09"),
    _sg("05", "C800", "Traction power and overhead line", "Bahnstrom und Fahrleitung", "Overhead contact line and traction power supply.", "Fahrleitung und Bahnstromversorgung.", pt=("CPT-03",), t="close:R04", own=True),
    _sg("05", "C810", "Rail signalling and train control", "Bahnsicherungsanlagen", "Interlocking, signalling and train protection.", "Stellwerke, Signale und Zugbeeinflussung.", pt=("CPT-03",), t="close:R05", own=True),

    # --- Construction: civil works, group 06 ---
    _sg("06", "C010", "Surface water drainage", "Oberflächenentwässerung", "Drainage of route and site surfaces.", "Entwässerung von Fahrbahn- und Geländeoberflächen.", pt=C, t="close:Q01"),
    _sg("06", "C020", "Storm water drainage", "Regenwasserableitung", "Storm water pipes, retention and outfalls.", "Regenwasserleitungen, Retention und Einleitungen.", pt=C, t="broad:Q01|related:Q02"),
    _sg("06", "C030", "Foul and wastewater drainage", "Schmutzwasserableitung", "Foul sewers and wastewater pipes.", "Schmutzwasserkanäle und Abwasserleitungen.", pt=C, t="close:Q02"),
    _sg("06", "C040", "Pumping systems", "Pumpanlagen", "Drainage pumping stations.", "Entwässerungspumpwerke.", pt=C, t="related:Q02 T06"),
    _sg("06", "C050", "Drainage connections", "Kanalisationsanschlüsse", "Connections to existing drainage.", "Anschlüsse an bestehende Kanalisation.", pt=C, t="broad:Q02"),

    # --- Construction: civil works, group 07 ---
    _sg("07", "C010", "Site enclosures and divisions", "Einfriedungen", "Fences, walls and gates along the route or site.", "Zäune, Mauern und Tore entlang der Trasse oder des Areals.", pt=C, t="broad:R08"),
    _sg("07", "C020", "Ancillary structures", "Nebenbauwerke", "Minor structures supporting the main asset.", "Kleinere Bauwerke zur Ergänzung der Hauptanlage.", pt=C, t="broad:O07"),
    _sg("07", "C030", "Minor roads and paving", "Kleinere Verkehrsflächen", "Paving not forming a separate sub-project.", "Beläge, die kein eigenes Teilprojekt bilden.", pt=C, t="broad:R01"),
    _sg("07", "C040", "Landscaping", "Landschaftsgestaltung", "Soft and hard landscaping.", "Grünflächen und Gestaltung.", pt=C, t="close:M08"),
    _sg("07", "C050", "External fittings and equipment", "Ausstattung Umgebung", "Furniture and equipment along the route.", "Mobiliar und Ausstattung entlang der Trasse.", pt=C, t="close:R08"),
    _sg("07", "C800", "Art in public works", "Kunst am Bau", "Artworks commissioned for the asset.", "Für das Bauwerk beauftragte Kunstwerke.", pt=C, t="close:R09", own=True),

    # --- Construction: all project types, group 08 ---
    _sg("08", "010", "Site management", "Bauführung", "Constructor's site management staff and support labour.", "Bauführungspersonal und Hilfskräfte des Unternehmers.", h="broad:B02.07", t="broad:L02"),
    _sg("08", "020", "Temporary access and storage areas", "Provisorische Zufahrten und Lagerflächen", "Temporary access, storage and traffic management at the constructor's discretion.", "Provisorische Zufahrten, Lagerflächen und Verkehrsführung nach Wahl des Unternehmers.", h="narrow:B02.01 B03.04", t="broad:L02|related:L03"),
    _sg("08", "030", "Site fencing and security", "Bauabschrankung und Bewachung", "Fencing and security of the site during works.", "Abschrankung und Bewachung der Baustelle während der Arbeiten.", h="broad:B02.07|related:B02.08", t="broad:L02"),
    _sg("08", "040", "Shared construction plant", "Gemeinsame Baugeräte", "Cranes, hoists and other plant shared between trades.", "Krane, Bauaufzüge und weitere gemeinsam genutzte Geräte.", h="close:B02.04", t="broad:L02"),
    _sg("08", "050", "Shared scaffolding", "Gemeinsame Gerüste", "Scaffolding shared between trades.", "Gemeinsam genutzte Gerüste.", h="close:B08", t="close:L06"),
    _sg("08", "060", "Other temporary facilities and services", "Weitere provisorische Einrichtungen", "Site accommodation, temporary supplies and processing facilities.", "Unterkünfte, provisorische Versorgung und Aufbereitungseinrichtungen.", h="narrow:B02.02 B02.03 B02.05 B03.03 B03.05", t="broad:L02|related:L03"),
    _sg("08", "070", "Site technology and communications", "Baustellen-IT und Kommunikation", "Telephone, network, hardware and software on site.", "Telefon, Netzwerk, Hard- und Software auf der Baustelle.", h="broad:B02.02", t="broad:L02"),
    _sg("08", "080", "Constructor's documentation", "Dokumentation des Unternehmers", "Submissions, reports and as-built records.", "Eingaben, Berichte und Revisionsunterlagen.", h="related:V02.02", t="related:V02.02"),
    _sg("08", "090", "Quality monitoring and inspection", "Qualitätsüberwachung und Prüfungen", "Monitoring, recording and inspections during works.", "Überwachung, Aufzeichnung und Prüfungen während der Arbeiten.", h="related:B01.04", t="related:L01"),
    _sg("08", "100", "Health, safety and environment", "Arbeitssicherheit und Umweltschutz", "Safety, health and environmental management on site.", "Arbeitssicherheit, Gesundheitsschutz und Umweltmanagement auf der Baustelle.", h="broad:B02.07|related:B02.08", t="broad:L02"),
    _sg("08", "110", "Constructor's insurances and guarantees", "Versicherungen und Garantien des Unternehmers", "Insurances, bonds, guarantees and warranties of the constructor.", "Versicherungen, Bürgschaften und Garantien des Unternehmers.", h="related:W02", t="related:W02"),
    _sg("08", "120", "Constructor's statutory fees", "Gebühren des Unternehmers", "Statutory fees and charges borne by the constructor.", "Gebühren und Abgaben zulasten des Unternehmers.", h="related:W01.02", t="related:W01.02"),
    _sg("08", "130", "Testing and commissioning", "Prüfung und Inbetriebnahme", "Testing and commissioning of the completed works.", "Prüfung und Inbetriebnahme der fertiggestellten Arbeiten.", h="close:W05", t="close:W05"),
    _sg("08", "140", "Extreme climate and working conditions", "Erschwerte Witterungs- und Arbeitsbedingungen", "Extra measures for extreme weather or working conditions.", "Zusätzliche Massnahmen bei extremer Witterung oder erschwerten Bedingungen.", h="close:B02.06", t="broad:L02"),
    _sg("08", "C025", "Temporary batching and processing plant", "Provisorische Misch- und Aufbereitungsanlagen", "Temporary concrete batching and material processing yards.", "Provisorische Betonmischanlagen und Aufbereitungsplätze.", pt=C, t="broad:L02"),
    _sg("08", "C045", "Marine plant and equipment", "Schwimmende Geräte", "Floating and marine plant for waterborne works.", "Schwimmende Geräte für Arbeiten auf dem Wasser.", pt=CW, t="broad:L02"),
    _sg("08", "C055", "Workforce accommodation", "Unterkünfte für Arbeitskräfte", "Living accommodation for the workforce.", "Wohnunterkünfte für Arbeitskräfte.", pt=C, t="broad:L02"),
    _sg("08", "C065", "Mobilisation and demobilisation", "Installation und Räumung", "Mobilisation and demobilisation of major plant.", "Installation und Räumung von Grossgeräten.", pt=C, t="broad:L02"),

    # --- Construction: all project types, groups 09-13 ---
    _sg("09", "010", "Design development allowance", "Reserve Projektentwicklung", "Allowance for changes as the design develops.", "Reserve für Änderungen im Zuge der Projektentwicklung.", h="broad:Y01", t="broad:Y01"),
    _sg("09", "020", "Construction contingency", "Reserve Unvorhergesehenes", "Allowance for unforeseen events during construction.", "Reserve für unvorhergesehene Ereignisse während der Ausführung.", h="broad:Y01", t="broad:Y01"),
    _sg("09", "030", "Price level adjustment", "Teuerung", "Price changes until tender and during construction.", "Preisänderungen bis zur Ausschreibung und während der Ausführung.", h="close:Y02", t="close:Y02"),
    _sg("09", "040", "Exchange rate adjustment", "Wechselkursänderungen", "Effect of currency fluctuation on costs.", "Auswirkung von Wechselkursschwankungen auf die Kosten.", h="related:Y02", t="related:Y02"),
    _sg("10", "010", "Taxes paid by the constructor", "Steuern zulasten Unternehmer", "Taxes and levies borne by the constructor.", "Steuern und Abgaben zulasten des Unternehmers.", h="related:Z01", t="related:Z01"),
    _sg("10", "020", "Taxes on contract payments", "Steuern auf Vertragszahlungen", "Value added tax and levies paid by the client on contract payments.", "Mehrwertsteuer und Abgaben der Bauherrschaft auf Vertragszahlungen.", h="close:Z01", t="close:Z01"),
    _sg("11", "010", "Off-site utility connections", "Werkleitungsanschlüsse ausserhalb", "Connections, diversions and capacity upgrades of public utilities up to the site.", "Anschlüsse, Umlegungen und Kapazitätserweiterungen öffentlicher Werkleitungen bis zum Grundstück.", h="close:B04", t="broad:Q"),
    _sg("11", "020", "Public access roads and footpaths", "Öffentliche Zufahrten und Fusswege", "Public roads and footpaths outside the site.", "Öffentliche Strassen und Fusswege ausserhalb des Grundstücks.", h="close:B09.03", t="related:R01"),
    _sg("12", "010", "Loose furniture, fittings and equipment", "Mobiliar und lose Ausstattung", "Loose items normally supplied after completion.", "Lose Ausstattung, die üblicherweise nach Fertigstellung geliefert wird.", h="narrow:J01 J02 J03", t="related:R08"),
    _sg("12", "020", "Fixed production and process equipment", "Feste Produktions- und Prozesseinrichtungen", "Production and process plant installed before completion.", "Vor Fertigstellung installierte Produktions- und Prozessanlagen.", h="close:H01|related:H04", t="related:T08"),
    _sg("12", "800", "Art in architecture", "Kunst am Bau", "Artworks and artistically designed building parts.", "Kunstwerke und künstlerisch gestaltete Bauteile.", pt=B, h="close:J04", own=True),
    _sg("13", "010", "Design and consultancy fees", "Planungs- und Beratungshonorare", "Fees and expenses of architects, engineers, surveyors and specialists.", "Honorare und Nebenkosten von Architektur, Ingenieurwesen, Vermessung und Fachplanung.", h="close:V01|related:V02.01", t="close:V01|related:V02.01"),
    _sg("13", "020", "Statutory approval charges", "Bewilligungsgebühren", "Charges payable to authorities for approvals and inspections.", "Gebühren an Behörden für Bewilligungen und Abnahmen.", h="close:W01", t="close:W01"),
    _sg("13", "030", "Site supervision", "Bauleitung", "Site supervision including accommodation and travel.", "Bauleitung einschliesslich Unterkunft und Reisen.", h="broad:V01", t="broad:V01"),
    _sg("13", "040", "Testing authorities", "Prüfstellen", "Payments to testing authorities and laboratories.", "Zahlungen an Prüfstellen und Labore.", h="related:V01.05", t="related:V01.05"),
    _sg("13", "800", "Client-side advisers and project platforms", "Beratung und Projektplattformen der Bauherrschaft", "Competitions, owner, operator and user representatives, advisers and project platforms.", "Auswahlverfahren, Vertretung von Eigentümer, Betreiber und Nutzenden, Beratung und Projektplattformen.", h="close:V03", t="close:V03", own=True),
]


def category_notation(digit: str) -> str:
    return f"CG-{digit}"


def group_notation(category: str, code: str) -> str:
    return f"CG-{category}-{code}"


def subgroup_notation(sg: SubGroup) -> str:
    return f"CG-{sg.category}-{sg.group}-{sg.code}"


def icms_subgroup_codes(sg: SubGroup) -> list[str]:
    """ICMS reference codes; B. and C. prefixes denote ICMS Tables B-1 and C-1."""
    digits = sg.code.lstrip("BC")
    base = f"{sg.category}.{sg.group}.{digits}"
    if sg.icms_tables == ("A",):
        return [base]
    return [f"{table}.{base}" for table in sg.icms_tables]


def parse_spec(spec: str) -> list[tuple[str, list[str]]]:
    result: list[tuple[str, list[str]]] = []
    if not spec:
        return result
    for part in spec.split("|"):
        key, _, values = part.partition(":")
        result.append((key.strip(), values.split()))
    return result


def ttl_escape(text: str) -> str:
    return text.replace("\\", "\\\\").replace('"', '\\"')
