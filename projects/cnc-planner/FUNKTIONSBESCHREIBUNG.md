# CNC Planner Pro — Vollständige Funktionsbeschreibung

**Version:** v16-complete  
**Stand:** 2026-02-05  
**Datei:** `demo-v16-complete.html`

---

## Übersicht

CNC Planner Pro ist eine browserbasierte Kalkulationssoftware für CNC-Fertigungsbetriebe. Sie ermöglicht die schnelle Kalkulation von Bearbeitungszeiten und Kosten basierend auf parametrischen Formeln und Industriestandards.

---

## 1. Navigation (6 Hauptbereiche)

### Sidebar-Struktur

```
┌─────────────────────┐
│ CNC Planner Pro     │
│ [BETA]              │
├─────────────────────┤
│ EINGABE             │
│ ├─ 📐 Teil & Param. │
├─────────────────────┤
│ ERGEBNIS            │
│ ├─ 💰 Kalkulation   │
│ ├─ 📄 Angebot       │
│ └─ 💻 NC-Code       │
├─────────────────────┤
│ 📝 Feedback         │
│ ⚙️ Einstellungen    │
└─────────────────────┘
```

---

## 2. Teil & Parameter

### 2.1 Bauteil-Auswahl

**Demo-Bauteile (3 vorkonfiguriert):**

| Teil | Maße | Material | Besonderheit |
|------|------|----------|--------------|
| Verbindungsplatte | 130×130×50 | S235JR | h5, H7 Toleranzen |
| Flansch DN50 | Ø160×25 | 1.4301 | 4× M10 Bohrungen |
| Halterung | 80×60×40 | AlMg3 | Standard |

**Funktionen:**
- Klick auf Karte → Teil wird ausgewählt
- Ausgewähltes Teil: blauer Rahmen + hellblauer Hintergrund
- "Eigene Zeichnung hochladen" → Platzhalter (noch nicht implementiert)

### 2.2 Zeichnungsvorschau

- Integriertes Bild der technischen Zeichnung
- Aufklappbar/zuklappbar
- "Vollbild" Button → öffnet in neuem Tab
- Zeigt: Teilenummer, Maße, Toleranzen

### 2.3 Werkstück-Parameter

**Material-Auswahl (Dropdown):**

| Gruppe | Werkstoffe |
|--------|------------|
| Edelstahl | 1.4301, 1.4404, 1.4571 |
| Baustahl | S235JR, S355J2, C45 |
| Vergütungsstahl | 42CrMo4, 34CrNiMo6 |
| Aluminium | AlMg3, AlMgSi1, Al7075 |
| Buntmetalle | Messing, Bronze |
| Kunststoff | POM, PA6, PEEK |

**Jeder Werkstoff hat:**
- Preis (€/kg)
- Dichte (kg/dm³)
- Zeitfaktor (Bearbeitbarkeit)

**Rohmaße:**
- X, Y, Z Eingabefelder (mm)
- Automatische Gewichtsberechnung

**Stückzahl:**
- Eingabefeld (min: 1)
- Beeinflusst Rüstkosten-Umlage

### 2.4 Fertigungs-Parameter

**Spannung (Dropdown):**

| Spannart | Rüstzeit | Beschreibung |
|----------|----------|--------------|
| Schraubstock | 15 min | Standard |
| 2× Schraubstock | 25 min | Für größere Teile |
| Tischspannung | 35 min | Direktspannung |
| Nullpunktspannsystem | 5 min | Schnellwechsel |
| Sondervorrichtung | 45 min | Kundenspezifisch |

**Aufspannungen:**
- Dropdown: 1-5 Aufspannungen
- Mehr Aufspannungen = mehr Rüstzeit

**Zusatzoperationen (Checkboxen):**

| Operation | Zeit | Stundensatz |
|-----------|------|-------------|
| Entgraten | 5 min | €47/h |
| Sägen | 3 min | €50/h |
| Prüfung | 5 min | €60/h |

### 2.5 Live-Ergebnis

Zeigt sofort:
- Gewicht (kg)
- Materialkosten (€)
- Bearbeitungszeit (min)
- Maschinenkosten (€)

Button: "Kalkulation anzeigen →"

---

## 3. Kalkulation

### 3.1 Preis-Hero

**Großer Preisanzeige:**
- Stückpreis in großer Schrift (€XX,XX)
- Konfidenz-Badge: 🟢 ±10% | 🟡 ±15% | 🔴 ±25%
- Untertitel: "inkl. Material, Bearbeitung, Einrichtung"

### 3.2 Kostenaufschlüsselung

**Zuschlagskalkulation (Industriestandard):**

```
Materialkosten (Gewicht × €/kg × Verschnitt)
  + MGK (10% Materialgemeinkosten)
────────────────────────────────────
= Materialkosten mit GK

Fertigungskosten (Maschine + Rüsten + Nebenzeiten)
  + AV-Aufschlag (8% Arbeitsvorbereitung)
────────────────────────────────────
= Fertigungskosten mit AV

+ Werkzeugverschleiß (pauschal)
────────────────────────────────────
= HERSTELLKOSTEN (HK)

+ VwGK (12% Verwaltungsgemeinkosten)
+ VtGK (5% Vertriebsgemeinkosten)
────────────────────────────────────
= SELBSTKOSTEN (SK)

+ Gewinn (10%)
────────────────────────────────────
= ANGEBOTSPREIS (netto)
```

**Jede Zeile zeigt:**
- Bezeichnung
- Berechnungsformel
- Betrag (€)

### 3.3 Mengenstaffel

**Tabelle mit Staffelpreisen:**

| Stück | Pro Stück | Gesamt | Ersparnis |
|-------|-----------|--------|-----------|
| 1 | €64,89 | €64,89 | — |
| 5 | €52,30 | €261,50 | -19% |
| 10 | €46,15 | €461,50 | -29% |
| 25 | €41,20 | €1.030 | -36% |
| 50 | €38,50 | €1.925 | -41% |

### 3.4 Kalkulationsgrundlage

- Ausgewähltes Teil mit Bild
- Material, Maße, Gewicht
- Bearbeitungszeit (Haupt + Neben)
- Rüstzeit

### 3.5 Operationen & Bearbeitungszeiten

**Tabelle mit allen OPs:**

| OP | Beschreibung | Werkzeug | t_h | t_n | Gesamt |
|----|--------------|----------|-----|-----|--------|
| OP10 | Planfräsen | T1 Ø63 | 1,9 | 0,8 | 2,7 min |
| OP20 | Kontur schruppen | T2 Ø20 | 6,2 | 1,8 | 8,0 min |
| OP30 | Taschen fräsen | T2 Ø20 | 4,5 | 1,2 | 5,7 min |
| OP50 | Schlichten ⚠️ | T3 Ø16 | 4,2 | 0,9 | 5,1 min |
| OP60 | Feinbohren ⚠️ | T11 | 3,3 | 0,8 | 4,1 min |

**Aufklappbare Details pro OP:**
- SVG-Skizze der Bearbeitungsstrategie
- Hauptzeit-Berechnung (Formeln)
- Nebenzeit-Aufschlüsselung
- Bei kritischen Toleranzen: Warnbox

**Kritische Operationen (rot markiert):**
- OP50: h5 Toleranz (0/-0,018 mm)
- OP60: H7 Toleranz (+0,021/0 mm)

### 3.6 Maschinenzeitkalkulation (aufklappbar)

**Schnittparameter pro Werkzeug:**
- Schnittgeschwindigkeit v_c
- Vorschub pro Zahn f_z
- Zustellung a_p
- Drehzahl n
- Tischvorschub v_f

**Formeln:**
- v_f = n × z × f_z
- t_h = L / v_f
- Sicherheitszuschlag: +20%

### 3.7 Materialkalkulation (aufklappbar)

- Rohteilvolumen (mm³)
- Gewicht (kg)
- Materialpreis (€/kg)
- Verschnitt (%)
- Gesamtkosten

### 3.8 Einrichtkosten (aufklappbar)

- Grundrüstzeit pro Spannart
- Zusatzzeit pro Aufspannung
- Kosten = Zeit × Stundensatz

### 3.9 Berechnungsmethodik

**Angewandte Normen:**
- REFA — Zeitgliederung
- VDI 3321 — Schnittdaten Fräsen
- DIN 8580 — Fertigungsverfahren
- DIN EN 10027 — Werkstoffbezeichnung

### 3.10 Werkzeuge & Schnittdaten

**Werkzeugliste:**

| T# | Werkzeug | v_c | f_z | a_p | Kosten |
|----|----------|-----|-----|-----|--------|
| T1 | Planfräser Ø63 | 180 | 0,15 | 2,0 | €4,20 |
| T2 | Schaftfräser Ø20 | 150 | 0,12 | 8,0 | €8,50 |
| T3 | Schlichtfräser Ø16 | 200 | 0,08 | 0,3 | €5,80 |
| T11 | Feinbohrkopf Ø26 | 80 | 0,05 | — | €2,24 |

**Werkzeugkosten-Berechnung:**
- Standzeit-basiert
- Werkstoff-Faktor berücksichtigt

### 3.11 Fertigungsanweisung

**Arbeitsanweisung für Werker:**

| Abschnitt | Inhalt |
|-----------|--------|
| Maschine | FEHLMANN VERSA 943 |
| Spannung | Parallelspanner, 2× Aufspannung |
| Nullpunkt | Mitte Rohteil |
| Operationsfolge | OP10 → OP20 → OP30 → OP50 → OP60 |
| Prüfmaße | Ø120 h5, 3× Ø26 H7 |
| Hinweise | Fräskanten, Messprotokoll |

---

## 4. Angebot

### 4.1 Angebots-PDF

**Header:**
- Angebotsnummer (automatisch)
- Datum
- Buttons: E-Mail, PDF

**Positionstabelle:**

| Pos | Beschreibung | Menge | EP | GP |
|-----|--------------|-------|----|----|
| 1 | Verbindungsplatte... | 1 | 64,89 | 64,89 |

**Footer:**
- Zwischensumme
- MwSt. (19%)
- Gesamtbetrag

**Konditionen:**
- Lieferzeit: 3-4 Wochen
- Zahlungsziel: 14 Tage
- Gültigkeit: 30 Tage

---

## 5. NC-Code

### 5.1 Code-Generator

**Formate (Tabs):**
- Heidenhain (Standard)
- Siemens 840D
- Fanuc

**Code-Anzeige:**
- Syntax-Highlighting
- Zeilennummern
- Copy-Button

**Generierter Code enthält:**
- Programm-Header mit Teilename
- Werkzeugaufrufe
- Verfahrbewegungen
- Schnittparameter
- Programm-Ende

**Hinweis:**
- "Code vor Einsatz prüfen"
- Geschätzte Laufzeit
- Maschinen-Info

---

## 6. Feedback

### 6.1 Feedback erfassen

**Eingabefelder:**
- Projekt-Nr. (automatisch)
- Datum
- Erfasser (Name/Kürzel)

**Zeitabweichungen pro OP:**

| OP | Beschreibung | Kalk. | Ist | Delta | Grund | Notiz |
|----|--------------|-------|-----|-------|-------|-------|
| OP10 | Planfräsen | 2,7 | [__] | auto | [Dropdown] | [Text] |
| ... | ... | ... | ... | ... | ... | ... |

**Grund-Kategorien (Dropdown):**
- Einrichtung
- Werkzeug
- Material
- Toleranz
- NC-Programm
- Sonstiges

**Setup-Zeit separat:**
- Kalkuliert vs. Ist
- Grund (Fräskanten, Ausrichten, Nullpunkt, Spannung)

**Ergebnis (Radio):**
- ✅ Teil i.O. (Erstfertigung)
- ✅ Teil i.O. (nach Korrektur)
- ⚠️ Nacharbeit nötig
- ❌ Ausschuss

**Empfehlung:**
- Freitext für Verbesserungsvorschläge

### 6.2 Cross-Learnings

**Statistiken:**
- Ø Abweichung (%)
- Anzahl Feedbacks
- Erkannte Muster

**Häufigste Zeitfresser (Balkendiagramm):**
- Einrichtung: +18%
- Toleranz: +15%
- Bearbeitung: +3%

**Erkannte Muster (Cards):**

```
┌─────────────────────────────────────────────┐
│ Einrichtzeit bei Parallelspanner      [HOCH]│
│ 8/12 Aufträge (67%) • Ø +12 min             │
│                                             │
│ Ursache: Fräskanten fehlen in Kalkulation   │
│                                             │
│ 💡 Vorschlag: Setup-Zeit +15 min            │
│ [Anwenden] [Ignorieren]                     │
└─────────────────────────────────────────────┘
```

**Empfehlungen aus Feedback:**
- Liste mit Zitat + Häufigkeit + Datum

### 6.3 Historie

**Tabelle aller Feedbacks:**

| Datum | Projekt | Erfasser | Kalk. | Ist | Delta | Grund | Ergebnis |
|-------|---------|----------|-------|-----|-------|-------|----------|
| 05.02 | 2500473 | Schmidt | 42 | 48 | +14% | Einrichtung | ✅ |

**Export:**
- CSV-Download Button

---

## 7. Einstellungen

### 7.1 Stundensätze

**Tabelle:**

| Bereich | Lohn (€/h) | Maschine (€/h) | Gesamt |
|---------|------------|----------------|--------|
| CNC-Fräsen 3-Achs | 49 | 42 | €91 |
| CNC-Fräsen 5-Achs | 55 | 65 | €120 |
| CNC-Drehen | 45 | 38 | €83 |
| Sägen | 42 | 8 | €50 |
| Entgraten | 42 | 5 | €47 |
| Qualitätsprüfung | 55 | 5 | €60 |

### 7.2 Materialpreise

**Eingabefelder pro Werkstoff:**

| Werkstoff | €/kg |
|-----------|------|
| S235JR | 6,79 |
| S355J2 | 7,50 |
| C45 | 3,50 |
| 1.4301 | 8,50 |
| 1.4404 | 12,00 |
| AlMg3 | 6,50 |

### 7.3 Zuschlagssätze

**Kalkulationszuschläge:**

| Zuschlag | Wert | Basis |
|----------|------|-------|
| MGK | 10% | auf Materialkosten |
| FGK | 10% | auf Fertigungskosten |
| AV-Aufschlag | 8% | auf Fertigungskosten |
| VwGK | 12% | auf Herstellkosten |
| VtGK | 5% | auf Herstellkosten |
| Gewinn | 10% | auf Selbstkosten |
| Skonto | 2% | Abzug bei Zahlung |

**Erklärungstabelle:**
- Zeigt Berechnungsreihenfolge
- Zwischensummen

### 7.4 Sonstige Einstellungen

- Materialverschnitt (%)
- Werkzeugverschleiß (€)
- Skonto (%)
- MwSt. (%)

### 7.5 Firmendaten

**Für Angebote:**
- Firmenname
- Ansprechpartner
- Adresse
- Telefon
- E-Mail
- Steuernummer
- IBAN

### 7.6 Angebotseinstellungen

- Gültigkeit (Tage)
- Standard-Lieferzeit
- Zahlungsziel

### 7.7 Speicherung

- "Einstellungen speichern" → localStorage
- "Zurücksetzen" → Defaults
- "Export" → JSON-Datei
- "Import" → JSON laden

---

## 8. Technische Details

### 8.1 Datenspeicherung

**localStorage Keys:**
- `cncplanner_settings_v16` — Alle Einstellungen
- `cncplanner_feedback` — Feedback-Historie
- `pattern_*` — Angewendete Muster

### 8.2 Berechnung

**Hauptfunktion:** `calculate()`

**Ablauf:**
1. Material + Maße lesen
2. Gewicht berechnen
3. Materialkosten + MGK
4. Bearbeitungszeit berechnen
5. Fertigungskosten + AV
6. Rüstkosten pro Stück
7. Werkzeugkosten
8. Herstellkosten
9. + VwGK + VtGK = Selbstkosten
10. + Gewinn = Angebotspreis
11. Mengenstaffel berechnen
12. UI aktualisieren

### 8.3 Styling

**CSS-Variablen:**
- `--color-primary`: #1E3A5F (Dunkelblau)
- `--color-success`: #059669 (Grün)
- `--color-warning`: #D97706 (Orange)
- `--color-error`: #DC2626 (Rot)

**Card-Header-Klassen:**
- `.card-header-primary` — Weiß auf Blau
- `.card-header-info` — Dunkelblau auf Hellblau
- `.card-header-success` — Grün
- `.card-header-warning` — Orange
- `.card-header-error` — Rot

---

## 9. Bekannte Einschränkungen

1. **Kein echter Upload** — Zeichnungen nur als Demo-Bilder
2. **Kein Archiv** — Kalkulationen werden nicht gespeichert
3. **Keine ERP-Integration** — Standalone-Anwendung
4. **Nur 3-Achs** — 5-Achs-Strategien nicht berechnet
5. **Parametrische Formeln** — ±15-25% Genauigkeit

---

## 10. Geplante Features

- [ ] Zeichnungs-Upload (PDF/Bild)
- [ ] Archiv mit localStorage
- [ ] NC-Code für Siemens/Fanuc
- [ ] Cross-Learning-Algorithmus
- [ ] ERP-Export (CSV/XML)
- [ ] Tablet-optimierte Eingabe

---

*Dokumentation erstellt: 2026-02-05*
*Version: v16-complete*
