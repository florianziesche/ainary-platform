# RISIKOANALYSE: Kalkulation Lagerungstraverse KBA

**⚠️ INTERNES DOKUMENT – NICHT FÜR KUNDEN**  
**Bauteil:** Lagerungstraverse | **Zng.-Nr.:** 10028104.79 | **Kunde:** KBA  
**Datum:** 2026-02-10 | **Status:** Entwurf

---

## 1. MANAGEMENT SUMMARY

Die automatische Kalkulation ergibt **€19.730/Stück**. Diese Analyse zeigt, wo dieser Preis richtig und wo er falsch liegen könnte.

| Szenario | Preis/Stück | Abweichung | Wahrscheinlichkeit |
|----------|-------------|------------|-------------------|
| 🟢 **Best Case** | €14.200 | −28% | 15% |
| 🟡 **Expected Case** | €19.730 | Basis | 50% |
| 🔴 **Worst Case** | €26.800 | +36% | 20% |
| ⚫ **Katastrophe** | €32.000+ | +62% | 5% |

**Kernaussage:** Die größten Risiken liegen im **Material** (€1,65/kg vs. €7,50/kg = €9.100 Differenz) und in der **Zeichnungsinterpretation** (2D → 3D Unsicherheit). Die Fertigungszeiten sind vergleichsweise robust (±20%).

---

## 2. KRITISCHE FRAGEN — Sortiert nach € Impact

### 🔴 Kategorie A: Preisbestimmend (>€2.000/Stück Einfluss)

#### A1: Materialpreis — Was kostet S355 in 200mm Blech wirklich?

| Quelle | Preis/kg | Rohteil 1.856kg | Impact vs. Basis |
|--------|----------|-----------------|-----------------|
| v18 Demo (aktuell) | €1,65 | €3.062 | −€10.858 |
| Stahlhandel 02/2026 (Basis) | €7,50 | €13.920 | **Basis** |
| Thyssen/Klöckner (Dickblech >100mm) | €8,50 | €15.776 | +€1.856 |
| Sonderqualität S355J2+N, Zeugnis 3.1 | €9,20 | €17.075 | +€3.155 |

**⚠️ Problem in der Demo-App:** Der Default-Materialpreis von €1,65/kg ist für Stahlblech **viel zu niedrig** — das sind Schrottpreise. Realistisch: €7–9/kg für S355 Dickblech (200mm), Quelle: Stahlhandel Q1/2026.

**Mitigation:**
- [ ] Aktuellen Tagespreis bei 2-3 Stahlhändlern einholen (Klöckner, Thyssen, Salzgitter)
- [ ] Klären: Liefert KBA das Rohteil? (Dann entfallen Materialkosten komplett → Preis fällt auf ~€4.400/Stück!)
- [ ] In v18: Materialpreis-Default für S355 auf €7,50/kg setzen

#### A2: Rohteil-Zustand — Brennschnitt inklusive?

| Szenario | Auswirkung |
|----------|-----------|
| Kontur wird ausgebrannt geliefert (Annahme) | Basis-Kalkulation |
| Rohmaterial als Platte, Brennschnitt selber | +€800–1.200/Stück |
| Rohmaterial als Platte, Wasserstrahlschnitt | +€1.500–2.000/Stück |

**Warum kritisch:** Die Zeichnung zeigt eine komplexe Außenkontur. Ohne Vorschnitt müsste das gesamte Material abgefräst werden → Bearbeitungszeit x3–x5.

**Mitigation:**
- [ ] KBA fragen: "Liefern Sie das Rohteil mit ausgebrannter Kontur oder als Rohplatte?"
- [ ] Falls Rohplatte: Brennschnitt als separate Angebotsposition

#### A3: Material — S355 oder GJS-700?

**⚠️ Widerspruch in der Zeichnung:**
- Zeichnungskopf nennt S355 (Baustahl) UND GJS-700 (Gusseisen mit Kugelgraphit)
- Das sind **komplett verschiedene Werkstoffe** mit verschiedenen Preisen, Zerspanbarkeit und Rohteilformen

| Werkstoff | Preis/kg | Zerspanbarkeit | Rohteil-Form | Impact |
|-----------|----------|---------------|-------------|--------|
| S355J2 (Baustahl) | €7,50 | Mittel (v_c=150) | Blech/Platte | Basis |
| GJS-700 (Sphäroguss) | €3,50–5,00 | Gut (v_c=180) | **Gussteil** | **−€5.000 bis −€8.000** |

**Wenn GJS-700 (Gussteil):**
- Rohteil ist ein **gegossenes Bauteil** → nahezu Endkontur
- Materialpreis: Gießerei-Preis für Rohteil (~€3.000–5.000 statt €13.920 für Vollmaterial)
- Zerspanvolumen: Nur Aufmaß 3-5mm → Bearbeitungszeit halbiert sich
- → Gesamtpreis: **€8.000–12.000/Stück statt €19.730**

**Mitigation:**
- [ ] **SOFORT klären mit KBA: S355 oder GJS-700?** Dies ändert den Preis um ±50%
- [ ] Falls Guss: Separate Kalkulation erstellen

---

### 🟡 Kategorie B: Signifikant (€500–2.000/Stück Einfluss)

#### B1: Anzahl Aufspannungen

| Szenario | Rüstzeit | FEK-Differenz |
|----------|----------|--------------|
| 3 Aufspannungen (optimiert, 5-Achs) | 90 min | −€450 |
| 4 Aufspannungen (Basis) | 164 min | Basis |
| 5 Aufspannungen (Zusatzbearbeitung nötig) | 205 min | +€350 |
| 6 Aufspannungen (enge Toleranzen erfordern Schleifen-Setup) | 250 min | +€650 |

#### B2: Programmierzeit / CAM

**Nicht kalkuliert!**

| Position | Zeit | Kosten |
|----------|------|--------|
| CAM-Programmierung (Erstprogramm) | 4–8h | €360–720 |
| Simulation & Optimierung | 1–2h | €90–180 |
| Einfahren (1. Teil mit Vorsicht) | +50% der Bearbeitungszeit | ~€460 |

**Impact bei 4 Stück:** €225–330/Stück (CAM auf Losgröße umgelegt + Einfahren nur 1. Teil)

**Mitigation:**
- [ ] CAM-Kosten als separate Angebotsposition "Einmalige Einrichtung"
- [ ] Alternativ: Im Gewinnzuschlag auffangen

#### B3: Werkzeugverschleiß

**Aktuell: €0 (im Maschinenstundensatz enthalten)**

Bei 8h Zerspanung in S355:
| Werkzeug | Standzeit | Verbrauch | Kosten |
|----------|-----------|-----------|--------|
| Planfräser Ø80 (Wendeschneidplatten) | ~180min | 2 Satz WSP | €120 |
| VHM-Fräser Ø20 | ~60min Vollschnitt | 1–2 Fräser | €80–160 |
| VHM-Fräser Ø16 | ~45min Vollschnitt | 1–2 Fräser | €60–120 |
| Bohrer diverse | ~300 Bohrungen | Minimal | €30 |
| **Gesamt** | | | **€290–430/Stück** |

**Mitigation:**
- [ ] Werkzeugkosten explizit kalkulieren oder Pauschale 5% auf FEK
- [ ] Bei GJS-700: Werkzeugverschleiß ~40% geringer

#### B4: Handling & Transport (1,5 Tonnen!)

| Position | Kosten |
|----------|--------|
| Kran-Handling pro Umspannung (4×) | Inkl. in Rüstzeit |
| Innerbetrieblicher Transport | ~€50/Stück |
| Lieferung LKW (4× 1,2t Fertigteile) | €200–500 je nach Entfernung |
| Sondertransport (Übergröße) | €500–1.000 |

---

### 🟢 Kategorie C: Feintuning (< €500/Stück Einfluss)

| Faktor | Bandbreite | Mitigation |
|--------|-----------|-----------|
| Entgrataufwand (manuell vs. NC-Fase) | ±€80 | Zeichnung prüfen: definierte Fasen? |
| Messprotokoll-Aufwand | ±€120 | KBA fragen: Welche Dokumentation? |
| Oberflächenbehandlung | €0–€500 | Zeichnung prüfen: Lackierung/Korrosionsschutz? |
| Energiekosten (Großmaschine, 8h) | ~€80 | Im MSS enthalten |
| Kühlschmierstoff | ~€20 | Im MSS enthalten |

---

## 3. SZENARIOANALYSE

### Best Case (€14.200/Stück)
- GJS-700 Gussteil (Rohteil €4.000 statt €13.920)
- 3 Aufspannungen (optimiert)
- Bearbeitungszeit −30% (weniger Zerspanvolumen bei Guss)
- Kunde liefert Rohteil → Material entfällt in Kalkulation

### Expected Case (€19.730/Stück)  
- S355 Blech, Brennschnitt geliefert
- 4 Aufspannungen, 10h Fertigung
- Materialpreis €7,50/kg
- 12% Gewinn

### Worst Case (€26.800/Stück)
- S355 Rohplatte (kein Brennschnitt) → +€1.200
- 5 Aufspannungen nötig → +€350  
- Materialpreis €9,20/kg (Zeugnis 3.1) → +€3.155
- Sonderwerkzeuge für Tiefbohrungen → +€400
- CAM-Programmierung + Einfahren → +€1.000
- Werkzeugverschleiß höher als erwartet → +€430
- Oberflächenbehandlung gefordert → +€500

### Katastrophe (€32.000+/Stück)
- Alles aus Worst Case plus:
- Toleranz ±0.1mm nicht haltbar → Schleifen nötig (+€800)
- Nacharbeit wegen Verzug beim Fräsen (+€1.500)
- Material-Neubestellung wegen Fehler (+€13.920)

---

## 4. RISIKO-MATRIX (Visuell)

```
                        WAHRSCHEINLICHKEIT
                    Gering    Mittel    Hoch
                  ┌─────────┬─────────┬─────────┐
      >€3.000    │ Verzug/  │ MATERIAL│         │
                  │ Schleifen│ PREIS   │         │
  I               ├─────────┼─────────┼─────────┤
  M  €1-3.000    │ Sonder-  │Brennschn│         │
  P               │ werkzeug │CAM-Prog.│         │
  A               ├─────────┼─────────┼─────────┤
  C  €500-1.000  │ 5.Aufsp. │Werkzeug-│         │
  T               │          │verschleiß         │
                  ├─────────┼─────────┼─────────┤
      <€500      │ Energie  │Transport│Entgraten│
                  └─────────┴─────────┴─────────┘
```

**Top 3 Risiken nach Expected Monetary Value:**
1. **Werkstoff-Klärung S355/GJS-700:** EMV = 50% × €8.000 = **€4.000**
2. **Materialpreis-Unsicherheit:** EMV = 40% × €3.000 = **€1.200**  
3. **Brennschnitt nicht inklusive:** EMV = 30% × €1.200 = **€360**

---

## 5. EMPFEHLUNGEN

### Vor Angebotsabgabe ZWINGEND klären:

| # | Frage an KBA | Impact | Prio |
|---|-------------|--------|------|
| 1 | **S355 oder GJS-700?** Welcher Werkstoff wird gefertigt? | ±€8.000 | 🔴 |
| 2 | **Rohteil:** Liefert KBA das Rohteil oder sollen wir beschaffen? | ±€13.920 | 🔴 |
| 3 | **Brennschnitt:** Ist die Kontur bereits ausgebrannt? | ±€1.200 | 🔴 |
| 4 | **3D-Modell:** STEP-Datei verfügbar für exakte Volumenberechnung? | ±€2.000 (Genauigkeit) | 🟡 |
| 5 | **Dokumentation:** Messprotokoll, Werkszeugnis, Erstmuster? | ±€500 | 🟡 |
| 6 | **Oberfläche:** Lackierung/Korrosionsschutz gefordert? | ±€500 | 🟡 |
| 7 | **Lieferzeit:** Gewünschtes Lieferdatum? | Planungsrelevant | 🟢 |

### Angebotsstrategie

**Empfehlung:** Angebot mit **drei Positionen** abgeben:

1. **CNC-Bearbeitung** (Kernleistung): €X/Stück
   - Inklusive: 4 Aufspannungen, Entgraten, Messprotokoll
   - Exklusive: Material, Oberflächenbehandlung, Transport

2. **Material** (optional): €Y/Stück
   - Nur wenn wir Material beschaffen
   - Tagespreis-Klausel für S355/GJS

3. **Einmalige Kosten**: €Z einmalig
   - CAM-Programmierung, Vorrichtungsbau (falls nötig)
   - Erstmuster-Dokumentation

**Dadurch:** Transparenz für den Kunden, Risikominimierung für uns, klare Trennung von Materialpreisschwankungen.

---

## 6. WERKER-FEEDBACK PROMPTS

Folgende Fragen gezielt an erfahrene Werker stellen (via 📱 im CNC Planner):

| Frage | Kontext |
|-------|---------|
| "Wie lange brauchst du für die Tischspannung eines 2m-Teils mit 1,5t?" | Rüstzeit-Validierung |
| "Planfräsen 2095×500mm in S355 mit Ø80 — schaffst du das unter 60min?" | Hauptzeit AG2 |
| "4 Aufspannungen für dieses Teil — oder geht's mit 3?" | Aufspannungs-Optimierung |
| "Wie viel Werkzeugverschleiß bei 8h S355? Satz WSP pro Teil?" | Werkzeugkosten |
| "Entgraten bei dem Teil — 1h realistisch?" | Entgratzeit |

---

## 7. WAS DIE KALKULATION KANN UND WAS NICHT

### ✅ Robust (±10%)
- Fertigungszeiten für Standard-Operationen (Planfräsen, Bohren)
- REFA-basierte Zuschlagsätze
- Mengenstaffelung und Lernkurve

### ⚠️ Annahmebasiert (±25%)
- Rohteilgewicht (aus 2D-Zeichnung, keine exakte Volumenberechnung)
- Taschengeometrien (Tiefe, Radien aus 2D nur geschätzt)
- Toleranzaufwand (±0.1mm = Schlichten nötig, aber wie viele Flächen?)

### ❌ Nicht abgedeckt
- Guss-Kalkulation (wenn GJS-700 → komplett andere Rechnung)
- Wärmebehandlung (falls gefordert)
- Oberflächenbehandlung
- Logistikkosten
- CAM-Programmierung

---

**Fazit:** Die Kalkulation ist als **Erstindikation gut** (75% Confidence). Vor Angebotsabgabe müssen die 🔴-Fragen beantwortet werden — insbesondere der Werkstoff (S355 vs. GJS-700) kann den Preis **halbieren oder verdoppeln**.

---

*Erstellt: 2026-02-10 | CNC Planner Pro (AI-Assisted)*  
*Gültigkeit: Bis Klärung der offenen Fragen*  
*Klassifizierung: ⚠️ INTERN*
