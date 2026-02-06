# CNC Planer Pro v18 - Complete Requirements Document

**Status:** 🟡 PHASE 1 KOMPLETT ✅  
**Ziel:** Alle Features aus v17 + Industrial Design + MBS Standards  
**Methodik:** Feature-by-Feature Research → Dann Build

**Fortschritt:**
- ✅ **Phase 1:** Feature-Audit (86 Features erfasst, `V17-FEATURE-AUDIT-COMPLETE.md`)
- 🔴 **Phase 2:** Research pro Feature (0/86)
- 🔴 **Phase 3:** Implementation (0/86)

---

## 📋 PHASE 1: FEATURE AUDIT ✅ KOMPLETT

**Audit-Datei:** `V17-FEATURE-AUDIT-COMPLETE.md` (3331 Zeilen, 86 Features erfasst)

### Was hat v17 ALLES? (Vollständige Liste)

#### 0. DESIGN SYSTEM
- [x] CSS Variables (Color Palette, Typography, Spacing)
- [x] Industrial Color Palette (Neutrale Grautöne, kein Rot/Grün/Blau)
- [x] Typography System (System-Fonts + Mono für Zahlen)
- [x] 8-Punkt Spacing Scale (xs-2xl)
- [x] Shadow System (Subtil)

#### 1. TEIL-EINGABE TAB
- [x] Trust Badges (3× Feature-Highlights mit Icons)
- [x] Scope Notice (Collapsible Info-Box)
  - [x] "Geeignet für" Liste
  - [x] "Nicht geeignet für" Liste
  - [x] Berechnungsprinzip + Genauigkeit
- [x] Part Grid (Demo-Teile mit Thumbnails)
  - [x] Verbindungsplatte Card
  - [x] Adapterplatte Card
  - [x] Selected-State
  - [x] onclick → selectProject()
- [x] File Upload Card (STEP/PDF Drop-Zone)
  - [x] Hidden File-Input
  - [x] Accept-Filter (.step, .stp, .pdf)
- [x] Werkstück-Eingabeformular
  - [x] Werkstoff-Dropdown (15 Materialien, grouped)
  - [x] Rohmaße X/Y/Z (mit Unit-Labels "mm")
  - [x] Dimension-Group (X × Y × Z Visual)
  - [x] Stückzahl (mit Constraint min="1")
- [x] Action Buttons
  - [x] Analysieren-Button
  - [x] Weiter zu Parameter-Button (mit Confirm-Dialog)

#### 2. PARAMETER TAB
- [x] Sub-Tab Navigation (3 Tabs: Fertigung, Preisangaben, Maschine)

##### Sub-Tab: Fertigung
- [x] Spannart-Dropdown (5 Methoden mit Zeit)
  - [x] Schraubstock (15 min)
  - [x] 2× Schraubstock (25 min)
  - [x] Tischspannung (35 min)
  - [x] Nullpunktspannsystem (5 min)
  - [x] Sondervorrichtung (45 min)
- [x] Aufspannungen-Select (1-4+)
- [x] Einrichtzeit-Infobox (Live-Update: Zeit + Kosten + Beschreibung)

##### Sub-Tab: Preisangaben
- [x] Maschinenstundensätze-Tabelle (6 Arbeitsgänge)
  - [x] CNC-Fräsen 3-Achs: Lohn + Maschine = Gesamt
  - [x] CNC-Fräsen 5-Achs
  - [x] CNC-Drehen
  - [x] Sägen
  - [x] Entgraten/Schleifen
  - [x] Qualitätsprüfung
  - [x] Editierbare Inputs → updateRates()
- [x] Hinweis-Infobox (Branchenübliche Sätze)
- [x] Materialpreise-Karten (3 Gruppen, 11 Materialien)
  - [x] Baustahl: S235JR, S355J2, C45, 42CrMo4
  - [x] Edelstahl: 1.4301, 1.4404, 1.4571, Duplex
  - [x] Aluminium: AlMg3, AlMgSi1, Al7075-T6
  - [x] Editierbare €/kg-Inputs
  - [x] Hinweis: "Tagesaktuelle Preise"
- [x] Zuschlagskalkulation-Tabelle (Industriestandard BAB)
  - [x] MGK (Materialgemeinkosten 10%)
  - [x] FGK (Fertigungsgemeinkosten 0%)
  - [x] AV (Arbeitsvorbereitung 8%)
  - [x] VwGK (Verwaltung 12%)
  - [x] VtGK (Vertrieb 5%)
  - [x] Gewinn (10%)
  - [x] Basis-Spalte (auf was wird gerechnet)
  - [x] Branchenüblich-Spalte (Richtwerte)
  - [x] Zwischensummen (HK, SK, Angebotspreis)

##### Sub-Tab: Maschine
- [x] CNC-Typ Selector (3-Achs vs. 5-Achs)

##### Weitere Features
- [x] Plausibilitäts-Warnungen (#warningsContainer)
  - [x] Länge > 400mm + Schraubstock → Warnung
  - [x] Höhe > 100mm → Vibrationsgefahr
  - [x] timeFactor > 1.3 → Schwerzerspanbar
- [x] Weiter zu Kalkulation-Button

#### 3. KALKULATION TAB
- [x] Gesamtkalkulation-Tabelle (Top-Card)
  - [x] Material (mit Formel)
  - [x] Maschinenzeit
  - [x] Werkzeugverschleiß
  - [x] Einrichtung
  - [x] Nebenzeiten
  - [x] HERSTELLKOSTEN (Summe-Row)
- [x] Überschrift "Detailkalkulation nach Kostenarten"
- [x] 2-Spalten-Grid (Maschine + Material)
  - [x] Maschinenzeitkalkulation Card
    - [x] Hauptzeit (th)
    - [x] Nebenzeit (tn)
    - [x] Gesamtzeit
    - [x] × Stundensatz
    - [x] = Maschinenkosten
  - [x] Materialkalkulation Card
    - [x] Rohmaße
    - [x] Volumen (mm³)
    - [x] Werkstoff / Dichte
    - [x] Gewicht (kg)
    - [x] × Preis + Verschnitt
    - [x] = Materialkosten
- [x] Einrichtkosten-Detail Card
  - [x] Spannmethode
  - [x] Basis-Einrichtzeit
  - [x] Aufspannungen
  - [x] Gesamt-Einrichtzeit
  - [x] × Stundensatz
  - [x] = Einrichtkosten
  - [x] ÷ Stückzahl
  - [x] = Pro Stück
  - [x] Tipp-Infobox (Serien-Vorteil)
- [x] Berechnungsgrundlagen Card (Footer)
  - [x] Zeitgliederung (REFA, DIN 8580)
  - [x] Schnittdaten (VDI 3321, DIN EN 10027)
  - [x] Berechnungsformel
  - [x] Referenzen (Links zu Tabs)
  - [x] Genauigkeit (±15%)

#### 4. FERTIGUNGSANWEISUNG TAB
- [x] Action-Buttons (PDF drucken, E-Mail)
- [x] KI-Badge ("KI-generierte Anweisungen")
- [x] Document Header
  - [x] Title "FERTIGUNGSANWEISUNG"
  - [x] Teilnummer (dynamisch)
  - [x] Freigabe-Datum
  - [x] Version
- [x] Werkstück-Info Grid (3 Spalten)
  - [x] Werkstück (Material, Rohteil, Gewicht)
  - [x] Maschine (Name, Steuerung, Zeit)
- [x] Toleranz-Infobox (DIN ISO 2768-mK, Rz 25)
- [x] Zeichnungs-Vorschau (Collapsible)
  - [x] Card-Header mit Chevron + Teilnummer + Vollbild-Button
  - [x] Image mit onerror-Fallback
  - [x] toggleDrawing() + openDrawingFullscreen()
- [x] Operationen-Tabelle (10 OPs)
  - [x] OP10: Planfräsen (mit Expander)
    - [x] 3-Spalten: Skizze | Hauptzeit | Nebenzeit
    - [x] SVG-Skizze (Werkstück + Fräsbahnen)
    - [x] Hauptzeit-Berechnung (detailliert)
    - [x] Nebenzeit-Breakdown
  - [x] OP20: Schruppen Kontur (mit Expander)
  - [x] OP30: Taschenfräsen (mit Expander)
  - [x] OP50: Schlichten h5 (KRITISCH mit Badge + roter Markierung)
    - [x] Toleranz-Box (h5 = ±0,018mm)
    - [x] Reduzierter Vorschub
  - [x] OP60: Feinbohren H7 (KRITISCH)
    - [x] Toleranz-Box (H7 = +0,021/0)
  - [x] OP40: Konturfräsen (kompakt, kein Expander)
  - [x] OP70: Feinbohren Ø44 H7 (kompakt, KRITISCH)
  - [x] OP80: Bohren M8 (kompakt)
  - [x] OP90: Gewindefräsen M8 (kompakt)
  - [x] OP100: Entgraten, Prüfen (kompakt)
  - [x] SUMMEN-Zeile (th + tn = Gesamt)
- [x] Qualitätsprüfung-Tabelle
  - [x] Prüfmerkmale (Ø26 H7, Höhe, Oberfläche)
  - [x] Soll-Werte
  - [x] Prüfmittel
  - [x] Zeit
- [x] Schnittparameter-Tabelle
  - [x] 6 Werkzeuge (T1, T2, T3, T11, T12, T13)
  - [x] Vc, n, fz, vf, ap, ae
  - [x] Legende-Infobox
- [x] Werkzeugkosten-Tabelle
  - [x] Preis, Standzeit, Einsatzzeit, Kosten
  - [x] Gesamt-Row
- [x] Werkzeugverschleiß-Warnung (werkstoffabhängig)
- [x] Feedback-Karte (Inline)
  - [x] 4 Optionen (Korrekt, Zu niedrig, Zu hoch, Sonstiges)
  - [x] Kommentar-Textarea
  - [x] Senden-Button

#### 5. ANGEBOT TAB
- [x] Angebots-Header
  - [x] Title "ANGEBOT"
  - [x] Angebots-Nummer (ANG-2026-0042)
  - [x] Firma (rechtsbündig)
  - [x] Datum (dynamisch)
  - [x] Gültig bis (Datum + 30 Tage)
- [x] Angebots-Tabelle
  - [x] Pos. | Beschreibung | Menge | EP | GP
  - [x] 1 Row (dynamisch befüllt)
- [x] Summen-Bereich (rechtsbündig)
  - [x] Zwischensumme
  - [x] + MwSt. 19%
  - [x] GESAMT (fett, farbig)
- [x] Footer-Text
  - [x] Zahlungsbedingungen (14 Tage netto)
  - [x] Lieferzeit (3-4 Wochen)

#### 6. NC-CODE TAB
- [x] Card-Header
  - [x] Format-Switcher (3 Buttons: Heidenhain, Siemens, Fanuc)
  - [x] Export-Buttons (Kopieren, Download)
- [x] Code-Block mit Syntax-Highlighting
  - [x] .code-comment (Grau)
  - [x] .code-keyword (Blau)
  - [x] .code-number (Orange)
  - [x] Heidenhain-Code (85 Zeilen)
- [x] Programm-Info (Footer)
  - [x] Zeilenzahl
  - [x] Laufzeit
  - [x] Maschine
  - [x] Warn-Hinweis (vor Einsatz prüfen)

#### 7. FEEDBACK TAB
- [x] Sub-Tab Navigation (3 Tabs)

##### Sub-Tab: Feedback erfassen
- [x] Projekt-Header (Projekt-Nr, Datum, Erfasser)
- [x] OP-Zeit-Feedback-Tabelle
  - [x] OP | Beschreibung | Kalk | Ist | Delta | Grund | Notiz
  - [x] 4 Zeilen (OP10, OP20, OP50 rot, OP60 rot)
  - [x] Editierbare Ist-Zeit → updateFeedbackDelta()
  - [x] Grund-Dropdown (6 Optionen)
  - [x] Notiz-Freitext
  - [x] Delta-Färbung (Rot/Grün)
  - [x] Tfoot: Setup-Zeile + Gesamt-Zeile
- [x] Ergebnis-Radio-Buttons (4 Optionen)
  - [x] i.O. (Erstfertigung)
  - [x] i.O. (nach Korrektur)
  - [x] Nacharbeit nötig
  - [x] Ausschuss
- [x] Empfehlung-Textarea
- [x] Action-Buttons
  - [x] Feedback speichern (localStorage)
  - [x] Formular leeren

##### Sub-Tab: Cross-Learnings
- [x] Kalkulations-Genauigkeit KPIs (3 Metriken)
  - [x] Ø Abweichung
  - [x] Feedback-Count
  - [x] Muster-Count
- [x] Zeitfresser-Bar-Charts (3 Kategorien)
  - [x] Einrichtung (72% → +18%)
  - [x] Toleranz (60% → +15%)
  - [x] Bearbeitung (12% → +3%)
- [x] Erkannte Muster-Liste (3 Pattern-Cards)
  - [x] Muster 1: Einrichtzeit Parallelspanner (HOCH)
    - [x] Häufigkeit + Mehraufwand
    - [x] Ursache-Box
    - [x] Vorschlag + Action-Buttons (Anwenden, Ignorieren)
  - [x] Muster 2: Toleranz h5/H7 (MITTEL)
  - [x] Muster 3: S235 Übermaß (NIEDRIG)
- [x] Empfehlungen aus Feedback (3 Top-Empfehlungen)
  - [x] Fräskanten (3× gemeldet)
  - [x] h5-Toleranz (2× gemeldet)
  - [x] S235 Rohteil (1× gemeldet)

##### Sub-Tab: Historie
- [x] Historie-Tabelle
  - [x] Datum | Projekt | Erfasser | Kalk | Ist | Delta | Grund | Ergebnis
  - [x] 5 Demo-Zeilen
- [x] CSV-Export-Button
- [x] Feedback-Statistik (Footer)

#### 8. EINSTELLUNGEN TAB
- [x] Firmendaten-Formular (8 Felder)
  - [x] Firmenname
  - [x] Ansprechpartner
  - [x] Straße
  - [x] PLZ / Ort
  - [x] Telefon
  - [x] E-Mail
  - [x] Steuernummer
  - [x] IBAN
- [x] Angebotseinstellungen (3 Felder)
  - [x] Gültigkeit (Tage)
  - [x] Standard-Lieferzeit
  - [x] Zahlungsziel (Tage)
- [x] Action-Buttons
  - [x] Speichern (localStorage)
  - [x] Zurücksetzen
  - [x] Export (JSON-Download)
  - [x] Import (Placeholder)
- [x] Info-Text (localStorage-Hinweis)

#### 9. GLOBALE FEATURES
- [x] App-Layout (Sidebar + Main)
- [x] Sidebar
  - [x] Logo (Icon + Text + Beta-Badge)
  - [x] Nav-Items (8 Sections)
  - [x] Footer-Items (Feedback, Einstellungen)
- [x] Main Header
  - [x] Dynamischer Titel
  - [x] Action-Buttons (CSV Export, PDF Export)
- [x] Content-Area (Scrollbar)
- [x] Section-Toggle (nur 1 aktiv)
- [x] Loading Overlay
  - [x] Spinner
  - [x] 5-Step Progress-Animation
  - [x] Sequential Steps (400-600ms)
- [x] Card-System
  - [x] .card, .card-header, .card-body
  - [x] Farbvarianten (primary, info, success, warning)
- [x] Info-Box / Warning-Box
- [x] Button-System (.btn, .btn-primary, .btn-secondary, .btn-sm)
- [x] Form-System (input, select, textarea)
- [x] Table-System
  - [x] Striped Rows
  - [x] Hover-Effect
  - [x] Mono-Class für Zahlen
- [x] Grid-System (.grid-2, .grid-3)

#### 10. JAVASCRIPT — DATA OBJECTS
- [x] MATERIALS Object (15 Werkstoffe)
  - [x] Properties: name, price, density, timeFactor
- [x] CLAMPING Object (5 Spannmethoden)
  - [x] Properties: time, desc
- [x] PROJECTS Object (2 Demo-Teile)
  - [x] Properties: id, name, partNumber, material, dims, baseTime, unitPrice, thumbnail
- [x] RATES Object
  - [x] cnc, saegen, entgraten (labor + machine)
- [x] currentProject Variable
- [x] feedbackHistory Array (localStorage)

#### 11. JAVASCRIPT — KEY FUNCTIONS
- [x] calculate() — Zentrale Kalkulation
  - [x] Input-Reading
  - [x] Volumen/Gewicht-Berechnung
  - [x] Materialkosten-Berechnung
  - [x] Setup-Zeit-Berechnung (Multi-Setup-Faktor 0.6)
  - [x] Bearbeitungszeit-Berechnung (sizeFactor^0.7)
  - [x] Zuschlagskalkulation (6-stufig)
  - [x] UI-Update (30+ IDs)
  - [x] Confidence-Badge-Logik
  - [x] Plausibility-Check
- [x] showSection(name, btn) — SPA Navigation
- [x] showParamTab(tab) — Sub-Tab-Wechsel
- [x] selectProject(id) — Demo-Projekt laden + Loading-Animation
- [x] renderPartGrid() — Part-Cards rendern
- [x] updateRates() — Stundensätze-Summe berechnen
- [x] updateMaterials() — Materialpreise updaten
- [x] saveSettings() — localStorage-Persistenz
- [x] loadSettings() — Settings laden
- [x] resetSettings() — localStorage löschen + Reload
- [x] toggleScope() — Scope-Notice expandieren
- [x] toggleDrawing() — Zeichnung expandieren
- [x] openDrawingFullscreen() — window.open()
- [x] toggleOpDetail(opId) — OP-Detail expandieren
- [x] checkPlausibility() — Warnungen generieren
- [x] showFeedbackTab(tab) — Feedback-Sub-Tab-Wechsel
- [x] updateFeedbackDelta(input) — Delta berechnen + färben
- [x] updateSetupDelta() — Setup-Delta
- [x] updateGesamtzeit() — Feedback-Summe
- [x] saveFeedback() — Feedback in localStorage
- [x] clearFeedbackForm() — Form leeren
- [x] updateCrossLearnings() — KPIs berechnen
- [x] updateFeedbackHistory() — Historie-Tabelle füllen
- [x] applyPattern(patternId, value) — Pattern-Flag setzen
- [x] ignorePattern(patternId) — Dismiss
- [x] exportFeedbackCSV() — CSV-Download
- [x] exportSettings() — JSON-Download
- [x] importSettings() — Placeholder
- [x] exportCSV() — Placeholder
- [x] copyCode() — Clipboard-Copy
- [x] downloadCode() — Blob-Download
- [x] setCodeFormat(format) — Button-Toggle
- [x] showLoading() — Loading-Overlay aktivieren
- [x] hideLoading() — Loading-Overlay deaktivieren
- [x] animateLoadingSteps() — Sequential Animation
- [x] selectFeedback(el, type) — Feedback-Option wählen
- [x] submitFeedback() — Feedback senden (Console-Log)
- [x] DOMContentLoaded — Init (loadSettings, renderPartGrid, calculate, Datum setzen)

#### 12. EDGE CASES & VERSTECKTE DETAILS
- [x] Setup-Umlegung auf Stückzahl (/ qty)
- [x] Multi-Setup Kosten-Faktor (2. Setup = 60% der ersten)
- [x] Volumen-Skalierung (sizeFactor^0.7, nicht linear)
- [x] timeFactor Material (Alu < 1.0, Edelstahl > 1.0)
- [x] Werkzeugverschleiß-Faktor (toolCost = toolWear * timeFactor)
- [x] Confidence-Badge Logik (Rot/Gelb/Grün basierend auf timeFactor + Volumen-Ähnlichkeit)
- [x] Plausibility-Warnings werkstoffabhängig
- [x] Feedback Delta-Färbung (Rot >10%, Grün <-5%)
- [x] localStorage-Fallback (leerer Array)
- [x] Image onerror Fallback
- [x] Datum Auto-Berechnung (heute + 30 Tage)

#### 13. NICHT IMPLEMENTIERT / PLACEHOLDERS
- [x] File Upload Handler (kein Event-Listener)
- [x] Siemens/Fanuc Code-Templates (nur Button-Toggle)
- [x] Import Settings (nur Alert)
- [x] CSV Export Kalkulation (nur Alert)
- [x] Nebenoperationen UI (JS vorhanden, UI fehlt)

---

**FEATURE-COUNT: 86 vollständig erfasst**  
**Dokumentation:** `V17-FEATURE-AUDIT-COMPLETE.md` (78KB, 3331 Zeilen analysiert)

---

## 📋 PHASE 2: RESEARCH PRO FEATURE

*Jedes Feature bekommt eigene Research-Sektion*

### Feature 1: Zeichnungsnummer-Display

**Research-Fragen:**
- Wie zeigen echte Maschinenbau-Angebote Zeichnungsnummern?
- Format: Wo steht sie? (unter Produktname, in Spalte, im Header?)
- Schriftart: Monospace oder Normal?
- Farbe: Wie prominent?
- Label: "Zchng Nr.", "Zeichnung-Nr.", "Drawing No."?

**Sources:**
- MBS Angebot (checked: ✅)
- Golden Standards price-display.md
- DIN 5008 Geschäftsbrief

**Best Practice:**
*[HIER KOMMT RESEARCH-ERGEBNIS]*

**Implementation Plan:**
*[HIER KOMMT WIE ES GEBAUT WIRD]*

---

### Feature 2: Position-Nummerierung

**Research-Fragen:**
- 1, 2, 3 oder 10, 20, 30?
- Warum Spacing (10, 20, 30)?
- Wo steht die Position (eigene Spalte?)
- Wie breit ist die Spalte?
- Fett oder Normal?

**Sources:**
- MBS Angebot (checked: ✅ nutzt 10, 20, 30...)
- DIN 5008
- SAP Standard
- Odoo/ERP Best Practices

**Best Practice:**
*[RESEARCH NEEDED]*

**Implementation Plan:**
*[TBD]*

---

### Feature 3: Gültigkeit automatisch berechnen

**Research-Fragen:**
- Standard: 2 Wochen, 4 Wochen, 30 Tage?
- Anzeige wo? (Header, Footer, Info-Box?)
- Format: "Gültig bis DD.MM.YYYY" oder "4 Wochen ab Angebotsdatum"?
- Rechtlich bindend oder "freibleibend"?

**Sources:**
- MBS Angebot (checked: ✅ "4 Wochen")
- BGB Angebots-Gültigkeit
- Branchenstandard Maschinenbau

**Best Practice:**
*[RESEARCH NEEDED]*

**Implementation Plan:**
*[TBD]*

---

### Feature 4: Tabellen-Styling (Professional)

**Research-Fragen:**
- Header: Welche Background-Farbe genau?
- Border: 1px oder 2px? Wo?
- Padding: Wie viel Luft?
- Hover: Ja oder Nein?
- Zebra-Stripes: Ja oder Nein?

**Sources:**
- MBS Angebot (checked: ✅)
- Golden Standards table patterns
- Bootstrap Tables
- Material Design Tables

**Best Practice:**
*[RESEARCH NEEDED]*

**Implementation Plan:**
*[TBD]*

---

### Feature 5: Footer mit Rechtlichem

**Research-Fragen:**
- Welche Infos sind Pflicht? (GmbH, USt-ID, HR-Nr, IBAN?)
- Schriftgröße?
- 1-spaltig oder 2-spaltig?
- Farbe (grau)?
- Position (nach Bedingungen oder ganz am Ende?)

**Sources:**
- MBS Angebot (checked: ✅)
- Impressumspflicht Deutschland
- DIN 5008 Geschäftsbrief
- Handelsgesetzbuch (HGB)

**Best Practice:**
*[RESEARCH NEEDED]*

**Implementation Plan:**
*[TBD]*

---

## 📋 PHASE 3: REQUIREMENTS PRO KOMPONENTE

*Nach Research: Detaillierte Requirements schreiben*

### Component: Professional Quote

**Must-Have Features:**
1. Zeichnungsnummer unter Produktname
2. Position-Nummerierung 10, 20, 30...
3. Gültigkeit automatisch (4 Wochen)
4. Bedingungen-Text
5. Footer mit Rechtlichem
6. Deutsche Formatierung

**Technical Specs:**
- HTML Structure: [TBD after research]
- CSS Classes: [TBD]
- JavaScript: [TBD]
- Data Model: [TBD]

**Edge Cases:**
- Mehrzeilige Produktnamen
- Lange Zeichnungsnummern (>20 Zeichen)
- Keine Zeichnungsnummer verfügbar
- Mehrere Positionen (10, 20, 30, 40...)
- Seite 2 (Übertrag)

**Validation:**
- Preise korrekt formatiert?
- Datum korrekt berechnet?
- Footer vollständig?
- Print-Layout funktioniert?

---

## 📋 PHASE 4: IMPLEMENTATION PLAN

*Nach Research + Requirements: Detaillierter Build-Plan*

### Build Order (Abhängigkeiten beachten):

1. **CSS Foundation** (keine Dependencies)
   - Design System Variables
   - Base Styles
   - Layout Grid

2. **Core Components** (brauchen CSS)
   - Tables
   - Cards
   - Buttons
   - Forms

3. **Angebot Tab** (braucht Core)
   - Header
   - Tabelle
   - Summen
   - Footer

4. **Andere Tabs** (brauchen Core)
   - Kalkulation
   - Fertigungsanweisung
   - etc.

5. **JavaScript Functions** (brauchen HTML)
   - calculate()
   - Gültigkeit
   - Formatierung

6. **Testing & Polish**
   - Browser Test
   - Print Test
   - Edge Cases

---

## 📋 PHASE 5: TESTING CHECKLIST

*Bevor wir "FERTIG" sagen:*

### Visual Tests:
- [ ] Alle Tabs geöffnet und gecheckt
- [ ] Tabellen sehen professional aus
- [ ] Keine Emojis sichtbar
- [ ] System Fonts aktiv
- [ ] Farben wie geplant (Grau, nicht Blau)

### Functional Tests:
- [ ] Calculate() funktioniert
- [ ] Gültigkeit wird berechnet
- [ ] Preise formatiert (XXX,XX €)
- [ ] Datum formatiert (DD.MM.YYYY)
- [ ] Print funktioniert

### Data Tests:
- [ ] Onkel's Teile laden
- [ ] Alle Felder ausgefüllt
- [ ] Zeichnungsnummer angezeigt

### Edge Cases:
- [ ] Sehr lange Produktnamen
- [ ] Sehr hohe Preise (>10.000€)
- [ ] Viele Positionen (>10)

---

## 🚀 DELIVERABLES

Nach diesem Prozess haben wir:

1. ✅ **Feature Audit** - Nichts vergessen
2. ✅ **Research Dokumentation** - Pro Feature
3. ✅ **Requirements Doc** - Klar & detailliert
4. ✅ **Implementation Plan** - Step-by-step
5. ✅ **Testing Checklist** - Komplett
6. ✅ **Working v18** - Beim ersten Mal richtig

---

## ⏱️ TIMELINE

- **Phase 1 (Audit):** 30 min
- **Phase 2 (Research):** 60 min (12 Features × 5 min)
- **Phase 3 (Requirements):** 45 min
- **Phase 4 (Implementation):** 120 min
- **Phase 5 (Testing):** 30 min

**TOTAL:** ~4,5 Stunden

**Aber:** Keine Loops, keine Fehler, beim ersten Mal richtig.

---

*Created: 2026-02-06 02:45*  
*Status: Phase 1 starting...*
