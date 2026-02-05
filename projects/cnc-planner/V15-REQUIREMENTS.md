# CNC Planner Pro v15 — Vollständige Anforderungsdokumentation

*Alle Features aus v14 + Verbesserungen für v15*

---

## 📋 Feature-Übersicht

### A. STRUKTUR & NAVIGATION

| # | Feature | v14 Status | v15 Ziel | Priorität |
|---|---------|------------|----------|-----------|
| A1 | **Header mit Logo** | ✅ | Beibehalten | MUST |
| A2 | **Tab-Navigation** (6 Tabs) | ✅ Tabs | Sidebar | MUST |
| A3 | **Projekt-Auswahl mit Thumbnails** | ✅ | Beibehalten | MUST |
| A4 | **Loading-Animation** | ✅ Steps | Optional | NICE |
| A5 | **Responsive Design** | ✅ Basic | Verbessern | SHOULD |

---

### B. TEIL-AUSWAHL & PARAMETER

| # | Feature | v14 Details | v15 Ziel |
|---|---------|-------------|----------|
| B1 | **Projekt-Karten** | 2 echte Teile + Thumbnails, Preis/Zeit/Material anzeigen | Beibehalten |
| B2 | **Werkstoff-Dropdown** | 18 Werkstoffe in Gruppen (Edelstahl, Baustahl, Alu, Buntmetalle, Kunststoff) | Beibehalten |
| B3 | **Spannung-Dropdown** | 5 Optionen (Schraubstock, 2×, Tisch, Nullpunkt, Spezial) | Beibehalten |
| B4 | **Aufspannungen-Dropdown** | 1-4 Aufspannungen | Beibehalten |
| B5 | **Einrichtzeit-Anzeige** | Live-Berechnung mit Beschreibung | Beibehalten |
| B6 | **Optionale Arbeitsgänge** | Sägen (Checkbox + Zeit), Entgraten (Checkbox + Zeit) | Beibehalten |
| B7 | **Rohmaße (L×B×H)** | 3 Inputs mit Live-Update | Beibehalten |
| B8 | **Stückzahl-Eingabe** | Prominent, mit Einrichtkosten/Stück Anzeige | Beibehalten |
| B9 | **Live-Ergebnis-Leiste** | Gewicht, Materialkosten, Zeit, Maschinenkosten | Beibehalten |
| B10 | **Gesamtkosten-Hero** | Großer Preis mit Gradient-Hintergrund | Beibehalten |

---

### C. TAB: ANGEBOT

| # | Feature | v14 Details |
|---|---------|-------------|
| C1 | **Angebot-Header** | Titel, Angebotsnummer, Datum, Firma |
| C2 | **Positions-Tabelle** | Pos, Beschreibung, Menge, EP, GP |
| C3 | **Summenblock** | Zwischensumme, MwSt 19%, Gesamtbetrag |
| C4 | **Zahlungsbedingungen** | Text-Footer |
| C5 | **PDF-Export Button** | Generiert druckbares PDF |
| C6 | **E-Mail-Button** | (Placeholder) |

---

### D. TAB: KALKULATION

| # | Feature | v14 Details |
|---|---------|-------------|
| D1 | **Operationen-Tabelle** | OP, Beschreibung, Zeit (dynamisch aus Projekt) |
| D2 | **Maschinenzeitkalkulation** | Hauptzeit, Nebenzeit, Gesamtzeit, Stundensatz, Maschinenkosten |
| D3 | **Materialkalkulation** | Rohmaße, Volumen, Dichte, Gewicht, Materialpreis, +10% Verschnitt |
| D4 | **Werkzeugkosten-Tabelle** | Werkzeug, Preis, Standzeit, Einsatz, Kosten |
| D5 | **Einrichtkosten** | Spannmethode, Basis-Zeit, Aufspannungen, Gesamt |
| D6 | **Mengenkalkulation-Tabelle** | Kostenart, Berechnung (Formel!), Pro Stück, Gesamt |
| D7 | **Verkaufspreis-Block** | Selbstkosten, Menge, Verkaufspreis |
| D8 | **Marge-Slider/Input** | Dynamische Anpassung 0-100% |
| D9 | **Kalkulationsgrundlage** | Datenquelle, Stundensätze, Zeitberechnung, Materialpreise |

---

### E. TAB: WERKZEUGE

| # | Feature | v14 Details |
|---|---------|-------------|
| E1 | **Schnittparameter-Tabelle** | Werkzeug, Operation, Vc, n, fz, vf, ap, ae |
| E2 | **Werkstoff-Hinweis** | Automatische Anpassung an Werkstoff |
| E3 | **Legende** | Erklärung der Abkürzungen |

---

### F. TAB: MASCHINENCODE (NC-Code)

| # | Feature | v14 Details |
|---|---------|-------------|
| F1 | **Format-Auswahl** | Heidenhain TNC, Siemens 840D, Fanuc |
| F2 | **Code-Block** | Syntax-Highlighting (Kommentare, Keywords, Zahlen) |
| F3 | **Copy-Button** | Code in Zwischenablage |
| F4 | **Export-Button** | Download als .H / .mpf / .nc |
| F5 | **Programm-Info** | Zeilen, Laufzeit, Maschine |

---

### G. TAB: FERTIGUNGSANWEISUNG

| # | Feature | v14 Details |
|---|---------|-------------|
| G1 | **Dokument-Header** | Titel, Teilname, Version, Freigabe |
| G2 | **Werkstück-Info** | Werkstoff, Rohmaße, Fertigmaße, Gewicht |
| G3 | **Maschinen-Info** | Maschine, Steuerung, Programm, Zeit |
| G4 | **Zeichnungs-Vorschau** | Thumbnail oder Upload-Zone |
| G5 | **Toleranz-Hinweis** | Box mit Toleranzangaben |
| G6 | **Arbeitsschritte** | OP-Badge, Name, Zeit, Parameter-Grid, Tipps-Liste |
| G7 | **Kritische Operationen** | Rote Markierung, Toleranz-Badge, Danger-Box |
| G8 | **Qualitätsprüfung-Tabelle** | Prüfmerkmal, Soll, Prüfmittel, Zeit, Checkbox, Löschen |
| G9 | **Prüfmittel-Dropdown** | Mikrometer, Messschieber, Innenmessschraube, Messuhr, CMM, Rauheit, Gewindelehrdorn |
| G10 | **Prüfzeit-Checkbox** | In Kalkulation einbeziehen |
| G11 | **Troubleshooting-Tabelle** | Problem, Ursache, Maßnahme |
| G12 | **Feedback-Sektion** | Radio-Buttons (Geprüft, Zu hoch, Zu niedrig), Kommentar, Senden |

---

### H. TAB: EINSTELLUNGEN

| # | Feature | v14 Details |
|---|---------|-------------|
| H1 | **Stundensätze-Tabelle** | CNC, Sägen, Entgraten — jeweils Lohn + Maschine = Gesamt |
| H2 | **Materialpreise-Grid** | Baustahl (S235JR, S355J2, C45), Edelstahl (1.4301, 1.4404, 1.4571), Alu (AlMg3, AlMgSi1, Al7075) |
| H3 | **Sonstige Einstellungen** | Werkzeugverschleiß €, Materialverschnitt %, Standard-Marge %, MwSt % |
| H4 | **Speichern-Button** | localStorage |
| H5 | **Zurücksetzen-Button** | Default-Werte |

---

### I. DATENVERWALTUNG

| # | Feature | v14 Details |
|---|---------|-------------|
| I1 | **Werkstoff-Datenbank** | 18 Werkstoffe mit Name, Preis, Dichte, timeFactor, vcFactor |
| I2 | **Projekt-Datenbank** | 2 echte Teile mit vollständigen Daten |
| I3 | **Stundensätze-Objekt** | cnc, saegen, entgraten — jeweils labor + machine |
| I4 | **localStorage** | Einstellungen speichern/laden |

---

### J. BERECHNUNGSLOGIK

| # | Feature | v14 Formel |
|---|---------|------------|
| J1 | **Volumen** | `L × B × H` (Quader) oder `π × r² × h` (Zylinder) |
| J2 | **Gewicht** | `Volumen (cm³) × Dichte / 1000` |
| J3 | **Materialkosten** | `Gewicht × Preis/kg × 1.1` (Verschnitt) |
| J4 | **Einrichtzeit** | `Basis + (Aufspannungen-1) × 60% × Basis` |
| J5 | **Bearbeitungszeit** | `Basiszeit × (Volumen/RefVolumen)^0.7 × MatFaktor` |
| J6 | **Maschinenkosten** | `Zeit/60 × Stundensatz` |
| J7 | **Werkzeugkosten** | `Basis × MatFaktor` |
| J8 | **Prüfkosten** | `Prüfzeit/60 × Stundensatz` |
| J9 | **Optionale AG** | `Zeit × (Lohn + Maschine)/60` |
| J10 | **Stückkosten** | `Material + Maschine + Werkzeug + Einricht/Menge + Prüf/Menge + Optional` |
| J11 | **Verkaufspreis** | `Stückkosten × (1 + Marge%)` |

---

### K. UI-KOMPONENTEN

| # | Komponente | v14 Styling |
|---|------------|-------------|
| K1 | **Buttons** | Primary (blau), Secondary (grau), Accent (hellblau) |
| K2 | **Inputs** | Border, Focus-Ring, Monospace für Zahlen |
| K3 | **Cards** | Weiß, Border, Shadow |
| K4 | **Tables** | Striped, Hover, Monospace-Zahlen |
| K5 | **Badges** | Success (grün), Warning (orange), Danger (rot) |
| K6 | **Info-Boxen** | Left-Border, Background |
| K7 | **Code-Block** | Dark Theme, Syntax-Highlighting |
| K8 | **Loading** | Spinner + Steps |
| K9 | **Collapsible** | Chevron + Animation |

---

### L. ZUSÄTZLICHE FEATURES (v14)

| # | Feature | Details |
|---|---------|---------|
| L1 | **Drag & Drop Upload** | STEP/PDF hochladen |
| L2 | **Trust-Badges** | "Echte Betriebsdaten", "<30 Sekunden", "NC-Code inklusive" |
| L3 | **Funktionsprinzip-Collapsible** | Anwendungsbereich + Grenzen |
| L4 | **Zeichnungs-Sektion** | Aufklappbar, Vollbild-Button |
| L5 | **CSV-Export** | Daten exportieren |
| L6 | **PDF-Export** | Print-CSS für professionelles Layout |
| L7 | **Feedback-System** | Radio + Textarea + Submit |

---

## 🎯 v15 VERBESSERUNGEN

### Strukturell

| Änderung | Von (v14) | Zu (v15) |
|----------|-----------|----------|
| Navigation | Tabs | **Sidebar** |
| Layout | Full-Width | **Max-Width Container** |
| Einstellungen | Tab | **Sidebar-Sektion (immer sichtbar)** |
| Design | Bunt | **Enterprise (gedämpft)** |

### Funktional

| Verbesserung | Details |
|--------------|---------|
| **Onboarding** | Erster Start → Einstellungen prompten |
| **Keyboard Shortcuts** | Tab-Wechsel, Speichern, etc. |
| **Dark Mode** | CSS-Variables vorbereitet |
| **Bessere Mobile UX** | Bottom-Nav auf Mobile |

---

## ⚠️ NICHT ÄNDERN (aus v14 übernehmen)

1. **Berechnungslogik** — Validiert, echte Daten
2. **Werkstoff-Datenbank** — 18 Werkstoffe mit korrekten Faktoren
3. **Stundensätze** — €91/h CNC, €55/h Sägen, €36/h Entgraten
4. **Materialpreise** — S235JR €6,79/kg (aus echtem Auftrag)
5. **NC-Code Templates** — Heidenhain-Format
6. **Fertigungsanweisung** — Operationen + QS-Prüfungen

---

## 📐 TECHNISCHE DETAILS

### CSS Variables (v14 → v15)

```css
/* v14 */
--primary: #1e3a5f;
--gray-50: #f8fafc;

/* v15 — gleiche Werte, bessere Struktur */
--color-primary: #1E3A5F;
--color-bg: #F8FAFC;
```

### JavaScript-Struktur

```
RATES = { cnc, saegen, entgraten }
MATERIALS = { ... 18 Werkstoffe ... }
PROJECTS = { verbindungsplatte, adapterplatte }
currentProject = null

loadProject(id)
recalculateAll()
updateRates()
updateMaterialPrices()
saveSettings()
generatePDF()
```

---

## ✅ CHECKLISTE VOR IMPLEMENTIERUNG

- [ ] **Alle Features verstanden?**
- [ ] **Sidebar-Design festgelegt?**
- [ ] **Responsive Breakpoints klar?**
- [ ] **Berechnungslogik 1:1 übernehmen**
- [ ] **Einstellungen prominent platzieren**
- [ ] **Design-Principles einhalten** (siehe DESIGN-PRINCIPLES.md)

---

## 🚦 EMPFEHLUNG

**Vor Implementierung besprechen:**

1. **Sidebar-Struktur** — Welche Sections?
2. **Einstellungen-Position** — Immer sichtbar vs. aufklappbar?
3. **Mobile-Verhalten** — Bottom-Tab-Bar oder Hamburger?
4. **Loading** — Beibehalten oder vereinfachen?
5. **Dark Mode** — Jetzt oder später?

---

*Dokumentiert: 2026-02-05 18:15*
*Basierend auf: demo-v14.html (5.471 Zeilen, 226 KB)*
