# Demo v9 — Anforderungen

## Fehlende Features aus vorherigen Versionen

### 1. 3 Beispiel-Projekte (demo-final.html)
- **Grundplatte WCAD-15-02-2020** — 41,8 min, 1.4571, €122,07 (vollständig)
- **Lagerbock WZ-2024-118** — 28,5 min, 42CrMo4, €85,20 (Entwurf)
- **Flansch FL-889** — 18,2 min, S355, €48,50 (Angebot erstellt)
- Projekte als Karten klickbar, laden jeweils eigene Daten

### 2. Vollständiger NC-Code (app-v5.html)
- **Kompletter Heidenhain TNC 640 Code** mit:
  - Header (Programm-Info, Werkstück, Maschine, Datum)
  - Werkzeug-Definitionen (T1-T15)
  - Nullpunkt & Sicherheitsebene (BLK FORM)
  - Alle 10 Operationen mit Kommentaren
  - CYCL DEF Befehle (256 Rechtecktasche, etc.)
  - Syntax-Highlighting (comment, keyword, gcode, mcode, number, tool)
- **Download als .H** — funktionsfähig
- **Kopieren** — funktionsfähig

### 3. Erweiterte Zeitberechnung (Zeitberechnung_mit_Angebot.html)
- **Formeln sichtbar**: t_h = L / v_f = L / (f × n)
- **Maschinendaten**: FEHLMANN VERSA 943 specs
- **Detailliertere Berechnung** mit:
  - Schnittweg L
  - Vorschub f
  - Berechnung in Formel-Darstellung
  - Mini-Fortschrittsbalken pro Operation
- **Zusammenfassung**: Min/Teil, Erstmuster (+30 min), Teile/Schicht, Schnittzeit%

### 4. Angebotsgenerator (Zeitberechnung_mit_Angebot.html)
- **Formular mit Eingaben**:
  - Kunde / Firma
  - Ansprechpartner
  - Anfrage-Nr.
  - Stückzahl
  - Maschinenstundensatz (€/h)
  - Materialpreis Rohteil (€)
  - Material-Aufschlag (%)
  - Gewinnmarge (%)
  - Lieferzeit (Wochen)
- **Berechnete Angebotserstellung** mit:
  - Professionelles Layout
  - Positionen (Bearbeitung, Material inkl.)
  - Rüstkosten
  - MwSt.
  - Zahlungsbedingungen
  - Technische Details
  - Lieferbedingungen
- **Drucken / PDF**
- **Kopieren**

### 5. Downloads (app-v5.html)
- **PDF** — Druckfunktion
- **CSV (Excel)** — Zeitberechnung als CSV exportieren
- **NC-Code als .H**

### 6. Feedback-Panel (app-v5.html, Fertigungsanweisung_V3.html)
- **Vorherige Feedbacks** von Mitarbeitern anzeigen
- **Feedback-Formular**:
  - Name / Personalnummer
  - Schicht / Datum
  - Betroffene Operation (Dropdown)
  - Sterne-Bewertung
  - Textfeld für Feedback
  - Kategorie (Verbesserung, Problem, Positiv, Frage, Korrektur)
  - Priorität (Niedrig, Mittel, Hoch)

### 7. Korrekturwerte (Fertigungsanweisung_V3.html)
- Grid mit Korrekturwerten für kritische Maße:
  - Ø120 h5
  - Ø26 H7
  - Ø44 H7
- Notizen zu Korrekturanpassungen

### 8. Interaktive Checklisten (Fertigungsanweisung_V3.html)
- "Vor dem Start" Checkliste
- "Prüfintervalle" Checkliste
- Checkboxen anklickbar

---

## Design

- **Landing-Page-Design** (v8 Style)
- Clean, professionell, industrial color palette
- Inter + JetBrains Mono
- Keine verspielten Elemente

---

## Struktur v9

```
1. Header mit Logo
2. ROI-Rechner (aus v8)
3. Projekt-Auswahl (3 Beispiele als Karten)
4. Tabs:
   - Angebot (mit Generator-Formular)
   - Kalkulation (detailliert mit Formeln)
   - Maschinencode (vollständig)
   - Fertigungsanweisung (mit Feedback-Panel)
5. Downloads (PDF, CSV, .H)
```

---

## Prioritäten

1. ✅ 3 Beispiel-Projekte
2. ✅ Vollständiger NC-Code
3. ✅ Erweiterter Angebotsgenerator
4. ✅ CSV-Download für Zeitberechnung
5. ✅ Feedback-Panel
6. ✅ Korrekturwerte-Grid
