# KI-Assistent für den Bürgermeister
## Konzept für die Stadt Glashütte

**Erstellt von:** Florian Ziesche — KI-Beratung für Kommunen
**Datum:** Februar 2026
**Version:** 1.0

---

## Executive Summary

Die Stadt Glashütte steht vor den gleichen Herausforderungen wie tausende deutsche Kommunen: Fachkräftemangel, steigende Aufgabenlast, knappe Budgets. Gleichzeitig bietet sich eine einmalige Chance: Mit gezieltem KI-Einsatz kann Glashütte zur **ersten KI-Modellkommune im Osterzgebirge** werden — und dabei konkret Geld sparen, die Verwaltung entlasten und den Bürgerservice verbessern.

Dieses Konzept beschreibt einen **persönlichen KI-Assistenten für den Bürgermeister** als zentralen Einstiegspunkt, der anschließend auf die gesamte Verwaltung ausgeweitet werden kann.

---

## 1. Der KI-Assistent — Was er kann

### Technologie-Stack
| Komponente | Lösung | Warum |
|------------|--------|-------|
| **Wissensdatenbank** | Obsidian | Lokal, DSGVO-konform, kostenlos, vernetzt |
| **KI-Assistent** | OpenClaw + Claude/GPT | Persönlicher Assistent, Telegram/WhatsApp erreichbar |
| **Chatbot (Bürger)** | Neuraflow oder Custom | 24/7 Bürgerservice auf Website |
| **Hosting** | Lokal im Rathaus | Keine Cloud, volle Kontrolle |

### 1.1 Tages-Briefing (automatisch)

**Jeden Morgen um 07:30 Uhr** erhält der Bürgermeister ein personalisiertes Briefing:

- **Termine des Tages** mit allen relevanten Unterlagen, Beschlussvorlagen, Hintergrundinformationen
- **Dringende Vorgänge** mit Handlungsempfehlung und Frist
- **Neue Bürgeranfragen** (zusammengefasst, priorisiert)
- **Relevante Nachrichten** (Förderprogramme, Gesetzesänderungen, Regionalnachrichten)
- **KPI-Übersicht** (offene Vorgänge, Bearbeitungszeiten, Haushaltsstatus)

**Zeitersparnis:** Statt 45-60 Min. morgens Akten sichten → **5 Minuten Briefing lesen**

### 1.2 Vorbereitung Ausschreibungen

| Ohne KI | Mit KI |
|---------|--------|
| Sachbearbeiter recherchiert Vergaberecht | KI prüft automatisch gegen aktuelle Vergabeverordnung |
| Manuelles Erstellen der Leistungsbeschreibung (4-8h) | KI erstellt Entwurf aus Vorlage + Projektdaten (30 Min.) |
| Prüfung auf Vollständigkeit durch Juristen (€800-1.500) | KI-Checkliste prüft 47 Pflichtpunkte automatisch |
| Veröffentlichung manuell auf Vergabeplattform | Automatische Formatierung + Upload-Vorbereitung |

**Einsparung pro Ausschreibung: 6-12 Stunden + €500-1.000 externe Prüfkosten**
**Bei ~20 Ausschreibungen/Jahr: 120-240h + €10.000-20.000 gespart**

### 1.3 Vorbereitung Gästebesuche

Landrat kommt? Delegation aus Partnerstadt? Unternehmer interessiert sich für Ansiedlung?

**KI erstellt automatisch:**
- **Gäste-Dossier:** Wer kommt, Hintergrund, letzte Kontakte, gemeinsame Themen
- **Talking Points:** 5 vorbereitete Gesprächspunkte mit Daten
- **Letzte Beschlüsse** die den Gast betreffen
- **Gastgeschenk-Vorschlag** (z.B. Glashütter Uhren-Buch bei internationalen Gästen)
- **Protokoll-Vorlage** die während des Gesprächs befüllt werden kann

**Zeitersparnis: 2-3 Stunden Vorbereitung → 10 Minuten**

### 1.4 Briefing vor Terminen

Für jeden Termin im Kalender:
- Alle zugehörigen **Akten und Dokumente** automatisch zusammengestellt
- **Zusammenfassung** der letzten Entwicklungen zum Thema
- **Beschlussvorlagen** im Entwurf
- **Bürgeranliegen** die zum Termin passen
- **Handlungsoptionen** mit Vor- und Nachteilen

### 1.5 Dashboard & KPI-Übersicht

Echtzeit-Cockpit mit:
- Offene Vorgänge (nach Priorität/Frist)
- Bearbeitungszeiten (Trend)
- Bürgeranfragen (beantwortet vs. offen)
- Haushaltsstatus (Ist vs. Plan)
- Personalauslastung
- Fördermittel-Scanner (neue Programme automatisch erkannt)

---

## 2. Erweiterung: Second Brain für die gesamte Verwaltung

### 2.1 Wissensmanagement mit Obsidian

**Das Problem:**
> "Frau Müller weiß, wie das mit den Baugenehmigungen funktioniert."
> Frau Müller geht 2027 in Rente. Das Wissen geht mit.

**Die Lösung: Obsidian als kommunales Second Brain**

Alle Verwaltungsdokumente, Beschlüsse, Satzungen, Verfahrensanweisungen werden in **Obsidian** — eine lokale, DSGVO-konforme Wissensdatenbank — überführt. Mit KI-Anbindung (OpenClaw + Smart Connections) kann jeder Mitarbeiter fragen: "Wie war das Verfahren beim letzten Bauantrag in Reinhardtsgrimma?" → Sofortige Antwort mit Quellennachweis.

**Warum Obsidian:**
- **100% lokal** — keine Daten verlassen das Rathaus. Kein Cloud-Zwang. DSGVO-konform.
- **Markdown-basiert** — zukunftssicher, kein Vendor Lock-in, lesbar ohne Software
- **Vernetzt** — Dokumente werden automatisch verlinkt (Personen, Projekte, Beschlüsse)
- **KI-fähig** — mit Plugins und OpenClaw als KI-Assistent wird Obsidian zum intelligenten Wissensspeicher
- **Kostenlos** — €0 Lizenzkosten (€50/Jahr für kommerzielle Nutzung)
- **Offline-fähig** — funktioniert auch ohne Internet

**Zahlen:**
- Sachbearbeiter verbringen **20-30% ihrer Arbeitszeit** mit Dokumentensuche (McKinsey)
- Durchschnittliche Suchzeit pro Dokument: **18 Minuten** (IDC)
- Bei 10 Verwaltungsmitarbeitern × 20% × 40h/Woche = **80 Stunden/Woche mit Suchen**
- KI reduziert das auf **10% → 40 Stunden/Woche zurückgewonnen**

### 2.2 Automatische Dokumentenerstellung

**Bescheide, Genehmigungen, Ablehnungen, Einladungen, Protokolle:**

| Dokumenttyp | Ohne KI | Mit KI | Ersparnis |
|-------------|---------|--------|-----------|
| Baugenehmigung | 45 Min. | 10 Min. | 78% |
| Gebührenbescheid | 20 Min. | 3 Min. | 85% |
| Sitzungsprotokoll | 90 Min. | 15 Min. | 83% |
| Bürger-Antwortbrief | 30 Min. | 5 Min. | 83% |
| Ausschreibungstext | 8 Std. | 1,5 Std. | 81% |

**Quelle:** AKDB 2025 — "KI beschleunigt Verwaltungsprozesse um 80%"
**Wohngeldantrag-Bearbeitung: 50% schneller** (Pilot BaWü + Brandenburg)

### 2.3 Automatische Ablage & Klassifikation

- Eingehende Post (physisch gescannt + digital) wird automatisch dem richtigen Vorgang zugeordnet
- E-Mails werden klassifiziert und in die E-Akte überführt
- **Bergheim (NRW):** KI sortiert und verteilt Post vollautomatisch
- **AKDB:** Dokumente automatisch in E-Akte ablegen, ohne manuelle Zuordnung
- Nichts geht mehr verloren, alles ist sofort auffindbar

### 2.4 Bürgerservice-Chatbot (24/7)

- Bürger fragen online oder telefonisch nach Öffnungszeiten, Formularen, Terminen, Zuständigkeiten
- **Augsburg (CiSA):** 500 häufige Fragen direkt beantwortet
- **Offenburg (OFFI):** So erfolgreich, dass um 1 Jahr verlängert
- **Marburg (Sophia):** Beantwortet Fragen zu KFZ-Zulassung, Gebühren, Verfahren
- **Für Glashütte:** Auch mehrsprachig für internationalen Uhrentourismus!
- **Break-Even: 2-3 Jahre** (BdSt NRW)
- **Entlastet Verwaltung um 30-50% der Routine-Anfragen**

---

## 3. KPIs & Einsparungen — Die harten Zahlen

### 3.1 Direkte Einsparungen (konservativ geschätzt)

| Bereich | Einsparung/Jahr | Berechnung |
|---------|----------------|------------|
| Dokumentenerstellung | **€18.000** | 3h/Tag × 250 Tage × €24/h Personalkosten |
| Dokumentensuche & Ablage | **€24.000** | 4h/Tag × 250 × €24/h |
| Ausschreibungsvorbereitung | **€12.000** | 20 Ausschreibungen × 8h × €75/h (inkl. extern) |
| Bürgeranfragen (Chatbot) | **€15.000** | 50% weniger Telefonanrufe × Sachbearbeiter-Zeit |
| Energiemanagement | **€12.000** | 10-15% auf ~€100K Energiekosten |
| Identifizierte Fördermittel | **€50.000+** | Automatischer Fördermittel-Scanner |
| **GESAMT** | **€131.000+/Jahr** | |

### 3.2 Indirekte Vorteile (nicht bezifferbar aber real)

- **Wissenssicherung:** Kein Wissensverlust bei Pensionierung
- **Mitarbeiterzufriedenheit:** Weniger Routine, mehr sinnvolle Arbeit
- **Attraktivität als Arbeitgeber:** Moderne Verwaltung zieht Bewerber an
- **Bürgervertrauen:** Schnellere Bearbeitung, 24/7 Service
- **Presseaufmerksamkeit:** "KI-Modellkommune" = kostenlose Werbung

### 3.3 Vergleich: Kosten vs. Nutzen

| Investition | Betrag |
|-------------|--------|
| Phase 1: Assessment + Konzept (4 Wochen) | €5.000 |
| Phase 2: Pilot-Implementation (8 Wochen) | €12.000 |
| Phase 3: Laufende Betreuung | €500/Monat |
| KI-API-Kosten (laufend) | ~€200/Monat |
| **Investition Jahr 1** | **~€25.400** |
| **Einsparung Jahr 1** | **€131.000+** |
| **ROI** | **416%** |

### 3.4 Förderung

| Programm | Zuschuss | Für |
|----------|----------|-----|
| Sachsen EFRE | bis 60% | Digitalisierung KMU/Kommunen |
| BMBF KI-Förderung | bis 100% | KI-Forschungsprojekte |
| SAB Sachsen | variabel | Digitalisierungsprojekte |
| KISA (Zweckverband) | Beratung | IT-Dienstleister für sächsische Kommunen |

**Mit 60% EFRE-Förderung: Eigenanteil Phase 1+2 nur ~€6.800**

---

## 4. Was den Bürgermeister gut dastehen lässt

### 4.1 Presse & Aufmerksamkeit

- **"Erste KI-Modellkommune im Osterzgebirge"** → MDR, Sächsische Zeitung, Freie Presse
- **Brandis** wurde als "Innovationskommune Sachsen" vom Innenminister gelobt
- **Großröhrsdorf** hat den ersten InnovationsHub Sachsens → landesweite Beachtung
- **Glashütte + KI = perfekte Story:** "Die Stadt der Präzision wird digital"
- Potenzial für überregionale Medien: Kleine Gemeinde + Innovation = ZEIT/SPIEGEL-Material

### 4.2 Politische Vorteile

- **Bürgerzufriedenheit:** 24/7 Service, schnellere Bearbeitung
- **Haushalt:** Nachweisbare Einsparungen → Geld für andere Projekte (Nahversorgung!)
- **Personalgewinnung:** "Arbeiten in einer modernen Verwaltung"
- **Fördermittel:** KI-Assessment findet automatisch passende Programme → mehr Geld für Glashütte
- **Vorbild-Funktion:** Andere Bürgermeister fragen nach → Netzwerk-Effekt

### 4.3 Das Nahversorgungs-Problem lösen

Glashütte hat seit 3 Jahren keinen Lebensmittelmarkt (MDR berichtete). KI kann helfen:
- **Automatisierte Bedarfsanalyse** erstellen (Einwohnerdaten, Altersstruktur, Mobilität)
- **Investoren-Pitch** vorbereiten (Standortanalyse, Kaufkraftdaten)
- **Fördermittel** für Nahversorgung identifizieren
- **Bürgerbefragung** auswerten und aufbereiten

→ "Der Bürgermeister nutzt innovative Werkzeuge, um echte Probleme zu lösen"

---

## 5. Umsetzungsplan

### Phase 1: Assessment & Quick Wins (Wochen 1-4)
- Bestandsaufnahme: Welche Prozesse, welche Software, welche Schmerzpunkte?
- 3 Quick Wins identifizieren und umsetzen (z.B. Chatbot, Briefing, Einfache Sprache)
- DSGVO-Konzept erstellen
- Förderantrag vorbereiten
- **Deliverable:** Machbarkeitsstudie + erste funktionierende KI-Anwendung
- **Kosten:** €5.000

### Phase 2: Pilot-Implementation (Wochen 5-12)
- Bürgerservice-Chatbot live schalten
- KI-Briefing-System für Bürgermeister einrichten
- Second Brain: Erste 500 Dokumente indexieren
- Dokumenten-Vorlagen mit KI-Unterstützung
- Mitarbeiter-Schulung (1 Tag)
- **Deliverable:** 4 funktionierende KI-Anwendungen
- **Kosten:** €12.000

### Phase 3: Vollbetrieb & Erweiterung (ab Monat 4)
- Alle Verwaltungsdokumente im Second Brain
- Automatische Ablage aktiv
- Energiemanagement-Pilot
- Fördermittel-Scanner
- Monatliches Reporting
- **Kosten:** €500/Monat + ~€200/Monat API

### Phase 4: Skalierung (ab Monat 7)
- Erfahrungen dokumentieren als Blaupause für andere Kommunen
- Pressearbeit: "Glashütte zeigt wie es geht"
- Potenzial: Beratung anderer Kommunen (Revenue für Glashütte!)

---

## 6. Über Florian Ziesche

- **5 Jahre als Startup-CEO/COO** (36ZERO Vision, Cloud Computer Vision, München)
- **€5,5 Mio. Kapital eingeworben** (Equity + Grants)
- **KI-Systeme gebaut:** Legal AI mit <0,2% Fehlerrate, Multi-Agent-Architekturen
- **Fertigungsexpertise:** CNC Planer Pro für Maschinenbaubetriebe entwickelt
- **Lokal:** Aufgewachsen in Schlottwitz, kennt die Region und ihre Bedürfnisse

**Kontakt:**
- Email: florian@ziesche.co
- Telefon: +1 347 740 1465

---

## 7. Referenzen & Quellen

| Quelle | Kernaussage |
|--------|-------------|
| McKinsey 2024 | KI senkt Fachkräftelücke um 165.000 Vollzeitstellen |
| dbb Monitor 2025 | 570.000 unbesetzte Stellen im öffentlichen Dienst |
| AKDB 2025 | KI beschleunigt Verwaltungsprozesse um 80% |
| AKDB Pilot BaWü | Wohngeldantrag-Bearbeitung 50% schneller |
| IDC Studie | 50% Produktivitätsplus durch KI-Einsatz |
| BdSt NRW 2025 | Chatbot-Break-Even in 2-3 Jahren |
| Dt. Städtetag 2025 | Beispielsammlung KI in Kommunen (Augsburg, Bochum, Bergheim, etc.) |
| Brandis/Sachsen | "Innovationskommune mit Vorbildcharakter für ganz Sachsen" |

---

*Dieses Konzept ist vertraulich und ausschließlich für die Stadt Glashütte bestimmt.*
*© 2026 Florian Ziesche*
