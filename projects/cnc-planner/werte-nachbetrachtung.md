# Alle Werte — Nachbetrachtung Lagerungstraverse

## QUELLEN
- MBS: Vorkalkulation Nr. 74374, b-logic, 09.02.2026, Björn Krügel
- CNC Planer: Kalkulationsbericht v0.20, 11.02.2026

---

## MBS VORKALKULATION (pro Stück, Menge: 1 Stk.)

### Arbeitsgänge (alle)
| Pos | Bezeichnung | Tr [min] | Te [min] | HK Lohn | HK Maschine | HK Gesamt |
|-----|-------------|----------|----------|---------|-------------|-----------|
| 10 | Kontrolle | ? | ? | ? | ? | 28,67€ |
| 15 | Sägen | ? | ? | ? | ? | 128,00€ |
| 17 | Schweißen | ? | ? | ? | ? | 36,00€ |
| 20 | AXA (Fräszentrum) | 450 | 1.800 | 1.417,50€ | 1.050,00€ | 2.467,50€ |
| 25 | FLP 8000 (Portalfräse) | 240 | 435 | 410,06€ | 900,00€ | 1.310,06€ |
| 30 | Lackieren | ? | ? | ? | ? | 116,85€ |

### Nur Fräsen (Pos 20 + 25)
- Tr: 450 + 240 = 690 min
- Te: 1.800 + 435 = 2.235 min
- Tr + Te: 2.925 min = 48,75h
- HK Lohn: 1.417,50 + 410,06 = 1.827,56€
- HK Maschine: 1.050,00 + 900,00 = 1.950,00€
- HK Gesamt Fräsen: 3.777,56€

### Preisanteile Grenzkosten
- Material: 1.228,60€
- Maschinen: 2.056,67€
- Lohn: 1.504,75€
- Fremd: 0,00€
- **Grenzkosten: 4.790,02€**

### Preisanteile Herstellkosten
- Material: 1.290,03€
- Maschinen: 2.056,67€
- Lohn: 2.031,41€
- **Herstellkosten: 5.378,11€**

### Differenz GK → HK
- Material: 1.290,03 - 1.228,60 = 61,43€ (= MGK 5%)
- Lohn: 2.031,41 - 1.504,75 = 526,66€ (= FGK auf Lohn)
- Maschinen: gleich (2.056,67€)
- GKZ gesamt: 588,09€ (= 12,28% auf GK)

### DB-Rechnung (MBS)
- Grenzkosten: 4.790,02€
- + GKZ 12,28%: 588,09€
- = Herstellkosten: 5.378,11€
- + VuV 20%: 1.075,62€
- = Selbstkosten: 6.453,73€
- + Gewinn 10%: 645,37€
- **= Kalk. VK: 7.099,10€**
- DB I (VK - GK): 2.309,09€ (32,5%)
- DB II (VK - HK): 1.720,99€ (24,2%)
- Gewinn (VK - SK): 645,37€ (9,1%)

---

## CNC PLANER PRO (pro Stück)

### Stammdaten
- Werkstoff: GJS-700-2 (Sphäroguss)
- Abmessungen: 2.095 × 500 × 190 mm
- Rohgewicht: ca. 1.415 kg
- Stückzahl Auftrag: 4
- Maschine: 3-Achs BAZ (in PDF: Hermle C 400, in Nachbetrachtung: "CNC-Maschine")
- Aufspannungen: 4

### Rüstzeiten (4 Aufspannungen)
| Nr | Beschreibung | Zeit |
|----|-------------|------|
| 1 | Unterseite | 50 min |
| 2 | Oberseite | 38 min |
| 3 | Stirnseite 1 | 39 min |
| 4 | Stirnseite 2 | 37 min |
| **Gesamt** | | **164 min** |
| **Pro Stück (÷4)** | | **41 min** |

### Arbeitsgänge (11 AG, alle)
| AG | Beschreibung | Zeit [min] | Satz [€/h] | Kosten |
|----|-------------|-----------|-----------|--------|
| 10 | Sägen & Vorbereitung | 28 | 45 | 21,00€ |
| 20 | Planfräsen Unterseite | 55 | 70 | 64,17€ |
| 30 | Bohrungen Unterseite | 44 | 70 | 51,33€ |
| 40 | Planfräsen Oberseite | 52 | 70 | 60,67€ |
| 50 | Taschen fräsen (4×) | 46 | 70 | 53,67€ |
| 60 | Langlöcher (3×) | 24 | 70 | 28,00€ |
| 70 | Konturfräsen Außen | 28 | 70 | 32,67€ |
| 80 | Stirnseite 1 | 40 | 70 | 46,67€ |
| 90 | Stirnseite 2 | 57 | 70 | 66,50€ |
| 100 | Entgraten komplett | 68 | 31 | 35,13€ |
| 110 | QS & Messprotokoll | 55 | 70 | 64,17€ |
| **Summe** | **alle 11 AG** | **497 min** | | **523,97€** |

### Nur Fräsen (AG 20-90)
- Zeit: 55+44+52+46+24+28+40+57 = **346 min = 5,77h**
- Kosten: 64,17+51,33+60,67+53,67+28,00+32,67+46,67+66,50 = **403,68€**

### Zeiten pro Stück
- Fertigung alle AG: 497 min = **8,3h**
- Rüst anteilig (÷4): 41 min = 0,68h
- **Gesamt: 538 min = 8,97h ≈ 9,0h**

### Materialkosten
- Rohteil GJS-700: 1.200,00€ (Festpreis Beistellung)
- MGK 5%: 60,00€
- **Material gesamt: 1.260,00€**

### Kostenstruktur pro Stück
- Material: 1.260,00€
- Fertigung (11 AG): 523,97€
- Rüst anteilig: 47,83€ (41 min × 70€/h)
- **Gesamt Fertigungskosten: 571,80€**
- **Gesamtkosten (Mat + Fert): 1.831,80€**

### Preispunkte (aus CNC Planer)
- Basispreis: 2.383,58€
- Betriebsleiter-Korrektur: 2.680€
- **Empfehlung: 2.750€** (korrigierte REFA-Zeiten + Risikopuffer)
- REFA-Korrektur: 2.900€
- Premiumkunde: 2.950€
- Sicherheitsmarge: 3.100€

### Zuschläge zum Angebotspreis
- Empfehlung: 2.750,00€
- + Kran-Handling: 178,00€
- + NC-Programmierung (÷4): 70,00€
- + QS H7 (30 min): 35,00€
- + Großkunde 15%: 79,00€
- **= Angebotspreis: 3.112,00€**

### Peer-Review Korrekturen (aus CNC Planer Dokument)
- REFA-Kalkulateur: "6 von 11 AGs zu knapp"
  - AG50 Taschen: 46 → 110 min
  - AG30 Bohrungen: 44 → 65 min
  - Rüstzeiten um 60% unterschätzt
  - Empfehlung: 2.800-2.900€
- Betriebsleiter: "Brot-Preis, kein Butter-Preis"
  - NC-Programmierung fehlt (280€)
  - QS-Aufwand H7 fehlt
  - Empfehlung: 2.650-2.700€

---

## VERGLEICHBARKEIT

### Direkt vergleichbar (gleicher Scope):
- **Fräsoperationen:** MBS Pos 20+25 vs. CNC Planer AG 20-90
  - MBS: 2.925 min, 3.777,56€
  - CNC: 346 min (+41 min Rüst = 387 min), 403,68€ (+47,83€ Rüst = 451,51€)
  - ACHTUNG: MBS hat 2 Maschinen, CNC 1. MBS-Zeiten enthalten Rüst (Tr) + Bearbeitung (Te).

### NICHT direkt vergleichbar:
- MBS Gesamtherstellkosten (5.378€) vs. CNC Planer Gesamtkosten (1.832€)
  → Verschiedener Scope (MBS hat Schweißen, Lackieren; CNC hat Entgraten, QS)
- MBS kalk. VK (7.099€) vs. CNC Planer AP (3.112€)
  → MBS rechnet GKZ+VuV+Gewinn auf HK; CNC Planer rechnet Zuschläge anders
- MBS DB-Rechnung vs. CNC Planer DB-Rechnung
  → MBS-Zuschlagssätze (GKZ 12,28%, VuV 20%) sind betriebsspezifisch für MBS

### Was man zeigen KANN:
1. Fräszeiten-Vergleich (gleicher Scope, direkt)
2. MBS DB-Rechnung (Original, vollständig)
3. CNC Planer Preisaufbau (eigene Methodik)
4. Gegenüberstellung der Endpreise mit Erklärung warum sie unterschiedlich sind
