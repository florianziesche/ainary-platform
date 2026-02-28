# Ainary Outreach Engine v1

## ICP (Ideal Customer Profile)
- **Region:** Dresden + 50km (Sächsische Schweiz, Erzgebirge, Meißen, Freital, Pirna, Dippoldiswalde, Glashütte, Freiberg)
- **Größe:** 10-100 Mitarbeiter (Mittelstand)
- **Budget:** €15.000+ verfügbar (oder förderbar — Sachsen Digital = 50% Zuschuss auf bis zu €100K)
- **Pain:** Manuelle Verwaltungsarbeit, Fachkräftemangel, Digitalisierungsrückstand
- **Entscheider:** Geschäftsführer, Inhaber, Verwaltungsleiter, Bürgermeister

## Target Segments (nach Priorität)

### Segment 1: Kommunale Verwaltungen (HÖCHSTE Prio)
- Warum: OZG-Druck, Fachkräftemangel, Förderung verfügbar, BM Glashütte als Referenz
- Targets: Alle Gemeinden/Städte im Landkreis Sächsische Schweiz-Osterzgebirge
- Pain: Bürgeranfragen, Bescheide, Digitalisierung, OZG-Umsetzung
- Outreach: Persönlich via BM-Netzwerk + direkte Email an Bürgermeister

### Segment 2: Maschinenbau / Fertigung
- Warum: CNC-Planung, Angebotswesen, Fachkräftemangel — Andreas als Pilot-Referenz
- Targets: IHK Dresden Mitglieder, Mittelstandspreis-Nominierte, Silicon Saxony
- Pain: Belegungsplanung, manuelle Kalkulation, Meisterwissen nicht dokumentiert
- Outreach: Email + LinkedIn

### Segment 3: Forschung / Hochschulen / Institute
- Warum: Forschungsanträge schreiben = hochmanuell, zeitintensiv, perfekter KI-Use-Case
- Targets: TU Dresden Institute, Fraunhofer Dresden, Helmholtz-Zentrum, HTW Dresden
- Pain: ZIM-Anträge, EU-Anträge, BMBF-Anträge — jeder Antrag 40-80h manuelle Arbeit
- Outreach: LinkedIn + direkte Email an Institutsleiter/Projektleiter

### Segment 4: Fördermittelberater
- Warum: Die schreiben SELBST Anträge für andere — maximaler Hebel
- Targets: subventcon.de, malburg-fleischer.de, foerderung-sachsen.de, deutsche-foerdermittelberatung.de
- Pain: Jeder Antrag = 20-60h. Mit KI: 5-10h + Review.
- Outreach: "Ich automatisiere 70% Ihrer Antragsarbeit"

### Segment 5: Handwerk / Bau
- Warum: Massiver Fachkräftemangel, null Digitalisierung, aber Geld vorhanden
- Targets: Kreishandwerkerschaft, Innungen, einzelne Betriebe
- Pain: Angebote manuell, keine CRM, Zettelwirtschaft
- Outreach: Über Innungen/HWK als Multiplikatoren

## Nachricht-Kalibrierung

### Florians Stil (aus Session-Analyse)
- Direkt, kein Smalltalk
- Führt mit konkretem Nutzen, nicht mit Feature
- Zahlen wenn möglich
- Kurz (max 5 Sätze cold outreach)
- Deutsch, Sie-Form für Erstontakt
- Kein Marketing-Sprech, kein "KI-Revolution"
- Stattdessen: "Ich habe X gebaut und bei Y eingesetzt. Ergebnis: Z. Passt das zu Ihrem Problem?"

### Email-Template (Segment 1: Verwaltung)
```
Betreff: KI für [Gemeinde] — Bürgeranfragen automatisieren

Sehr geehrter Herr/Frau [Name],

ich arbeite gerade mit der Stadtverwaltung Glashütte an einem KI-Pilotprojekt für die Automatisierung von Bürgeranfragen und Verwaltungsprozessen.

Ergebnis bei vergleichbaren Verwaltungen: 60% weniger Bearbeitungszeit bei Standardanfragen, 24/7 Bürgerservice ohne Mehrpersonal.

Hätten Sie Interesse an einem 30-Minuten-Gespräch, ob das auch für [Gemeinde] Sinn macht? Kein Verkaufsgespräch — nur eine ehrliche Einschätzung.

Mit freundlichen Grüßen
Florian Ziesche
Ainary · KI-Systeme für den Mittelstand
florian@ainaryventures.com
```

### Email-Template (Segment 2: Maschinenbau)
```
Betreff: 6h Planungszeit → 45 Minuten — KI für [Firma]

Sehr geehrter Herr/Frau [Name],

ich habe für einen Maschinenbaubetrieb in Sachsen (25 MA, 3 CNC-Maschinen) die Belegungsplanung automatisiert. Ergebnis: 87% weniger Planungszeit, ~€18K Ersparnis pro Jahr.

Vorher habe ich als CEO eine KI-Firma aufgebaut (BMW, Siemens, Bosch als Kunden). Jetzt bringe ich diese Technologie in den Mittelstand.

Lohnt sich ein kurzes Gespräch? 30 Minuten, keine Verpflichtung.

Florian Ziesche
Ainary · florian@ainaryventures.com
```

### Email-Template (Segment 3: Forschungsanträge)
```
Betreff: Forschungsanträge in halber Zeit — KI-Unterstützung

Sehr geehrter Herr/Frau Prof. [Name],

ein ZIM-Antrag kostet 40-80 Arbeitsstunden. Ich baue KI-Systeme die 70% davon automatisieren: Literaturrecherche, Textbausteine, Budgetplanung, Formatierung — Sie reviewen und finalisieren.

Hintergrund: TUM-Absolvent, ex-CEO einer KI-Firma (€5M Funding), jetzt spezialisiert auf KI-Automatisierung für den Mittelstand und die Wissenschaft.

Hätten Sie 20 Minuten für einen kurzen Austausch?

Florian Ziesche
florian@ainaryventures.com
```

### LinkedIn-Template (kurz, alle Segmente)
```
Hallo Herr/Frau [Name],

ich automatisiere manuelle Verwaltungsarbeit für Mittelständler in Sachsen mit KI. Nicht ChatGPT — spezialisierte Systeme für Ihren konkreten Anwendungsfall.

Aktueller Pilot: [relevantes Beispiel]. Ergebnis: [Zahl].

Passt ein kurzer Austausch?

Florian Ziesche
```

## Pipeline-Workflow

### Täglicher Agent-Run (automatisch)
1. Suche 3-5 neue Leads (Web Search, IHK, Handelsregister)
2. Recherche pro Lead (Website, News, Größe, Pain-Hypothese)
3. Match-Score berechnen (ICP-Fit 0-100%)
4. Nachricht generieren (Template + Personalisierung)
5. → Florian via Telegram: [✅ Senden] [❌ Skip]

### Follow-up Regeln
- Tag 5: Keine Antwort → Follow-up vorschlagen
- Tag 14: Keine Antwort → 2. Follow-up oder Skip
- Antwort erhalten → in Pipeline verschieben, Termin vorschlagen

## Lead-Datenbank (erste Batch)

### Sofort kontaktierbar (aus Recherche)
| # | Firma/Organisation | Segment | Ort | Kontakt | Pain-Hypothese |
|---|---|---|---|---|---|
| 1 | Gemeinden Landkreis SOE | Verwaltung | Region | Bürgermeister | OZG, Bürgeranfragen |
| 2 | HAVLAT Präzisionstechnik GmbH | Maschinenbau | Sachsen | David Havlat (GF) | CNC-Planung, Angebote |
| 3 | TESOMA GmbH | Maschinenbau | Sachsen | Ulrich Loser (GF) | Fertigung, Planung |
| 4 | Gemeinhardt Gerüstbau Service | Handwerk/Bau | Sachsen | Walter Stuber / Dirk Eckart | Angebote, Disposition |
| 5 | subventcon.de | Fördermittelberater | DE | — | Anträge schreiben |
| 6 | malburg-fleischer.de | Fördermittelberater | Sachsen | — | Anträge schreiben |
| 7 | TU Dresden Institute | Forschung | Dresden | Institutsleiter | ZIM/BMBF-Anträge |
| 8 | Fraunhofer IWS Dresden | Forschung | Dresden | — | Forschungsanträge |
| 9 | HTW Dresden | Forschung | Dresden | — | Drittmittelanträge |

## Förder-Angle (Sales-Verstärker)
- **Sachsen Digital**: 50% Zuschuss auf bis zu €100K für Digitalisierung von KMU
- **ZIM**: Bis €380K für F&E-Projekte
- **go-digital**: Bis €16.500 für Digitalisierungsberatung
- Pitch: "Ihr Pilot kostet €4.900 — mit Förderung zahlen Sie €2.450."
