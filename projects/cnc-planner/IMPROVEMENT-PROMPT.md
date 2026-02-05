# CNC Planner Pro — Verbesserungs-Anleitung

*Selbst-Instruktion für kontinuierliche Weiterentwicklung*

---

## 🎯 ZIEL

CNC Planner Pro auf **Spanflug-Niveau** bringen — ein verkaufsfähiges SaaS-Produkt für CNC-Lohnfertiger.

**Aktueller Stand:** v16 (Demo-ready)
**Ziel:** Production-ready mit zahlenden Kunden

---

## 🏆 DIE 10 SPANFLUG-FEATURES (Benchmark)

| # | Feature | Spanflug | CNC Planner v16 | Priorität |
|---|---------|----------|-----------------|-----------|
| 1 | **CAD/PDF Upload → Auto-Analyse** | ✅ STEP/PDF → Maße, Features | 🟡 Demo-Bild only | P0 |
| 2 | **Intelligenter Algorithmus** | ✅ "Millionen Teile" | 🟡 Formelbasiert | P2 |
| 3 | **Detaillierte Kostenaufschlüsselung** | ✅ Material, Prog, Rüsten, Fert, NB | 🟢 Vorhanden | ✅ |
| 4 | **Arbeitsvorbereitung** | ✅ Arbeitsplan mit allen OPs | 🟢 Fertigungsanweisung | ✅ |
| 5 | **Angebotserstellung** | ✅ PDF + Kundenmanagement | 🟡 PDF basic, kein CRM | P1 |
| 6 | **Anpassbarkeit** | ✅ Maschinen, Parameter, Preise | 🟢 Einstellungen | ✅ |
| 7 | **Archiv** | ✅ Teile, Kalkulationen, Angebote | 🔴 Fehlt komplett | P1 |
| 8 | **ERP-Integration** | ✅ API/Export | 🔴 Fehlt | P2 |
| 9 | **Cloud-basiert** | ✅ Browser, kein Install | 🟢 HTML/JS, keine Install | ✅ |
| 10 | **Datensicherheit** | ✅ ISO 27001, DSGVO | 🟡 Lokal only | P2 |

**Legende:** 🟢 Vorhanden | 🟡 Teilweise | 🔴 Fehlt | P0 = Sofort | P1 = Diese Woche | P2 = Später

---

## 🚀 FEATURE-ROADMAP (nach Spanflug-Benchmark)

### P0 — VOR DEMO (heute/morgen)
```
[ ] 1. CAD/PDF Upload implementieren (FileReader API)
    - Datei auswählen
    - Vorschau anzeigen
    - Maße manuell bestätigen (Auto später)
    
[ ] 2. Zuschlagskalkulation aktiv machen
    - AV-Aufschlag in calculate() integrieren
    - VwGK, VtGK berechnen
    - Deckungsbeitrag anzeigen
```

### P1 — DIESE WOCHE
```
[ ] 3. Archiv-Funktion (localStorage)
    - Projekt speichern
    - Projekt laden
    - Projekt löschen
    - Liste aller gespeicherten Projekte
    
[ ] 4. PDF-Export verbessern
    - LaTeX-Template nutzen
    - Firmenlogo einbinden
    - Professionelles Layout
    
[ ] 5. Kundenverwaltung (basic)
    - Kunde zu Angebot zuordnen
    - Kundenliste speichern
    - Kunde auswählen bei neuem Angebot
```

### P2 — NÄCHSTE 2 WOCHEN
```
[ ] 6. Intelligenterer Algorithmus
    - Feedback-Loop: Ist vs. Soll speichern
    - Korrekturfaktoren pro Werkstoff
    - "Basierend auf X Teilen" anzeigen
    
[ ] 7. ERP-Export
    - CSV Export
    - XML Export (BMEcat?)
    - JSON API Endpoint
    
[ ] 8. Datensicherheit Doku
    - DSGVO-Statement
    - Datenverarbeitung nur lokal
    - Kein Server = keine Datenschutzrisiken
```

### P3 — SPÄTER (nach erstem Kunden)
```
[ ] 9. Backend + Cloud
    - Node.js/Supabase Backend
    - User Authentication
    - Cloud-Sync
    
[ ] 10. Auto-Analyse aus CAD
    - STEP Parser (OpenCascade.js?)
    - Feature-Erkennung
    - Automatische OP-Generierung
```

---

## 📋 VOR JEDER SESSION

1. **v16-complete.html öffnen** und im Browser testen
2. **V14-FEATURE-INVENTORY.md** lesen — was fehlt noch?
3. **MATURITY-ROADMAP.md** lesen — wo sind wir?
4. **Dieses Dokument** lesen — was ist der nächste Schritt?

---

## 🔴 KRITISCHE LÜCKEN (Phase 0 — noch offen)

### Funktional
- [ ] **Zuschlagskalkulation in Berechnung integrieren** — AV, VwGK, VtGK werden noch nicht berechnet!
- [ ] **Zeichnung hochladen** — Aktuell nur Demo-Bild, kein echter Upload
- [ ] **Siemens/Fanuc NC-Code Templates** — Nur Heidenhain funktioniert
- [ ] **Editierbare Prüftabelle** — +/- Buttons für Prüfmerkmale
- [ ] **Editierbare Arbeitsgänge** — +/- Buttons für OPs

### UX
- [ ] **Mobile Ansicht** — Sidebar kollabierbar machen
- [ ] **Projekt speichern/laden** — localStorage für Kalkulationen
- [ ] **PDF mit Layout** — LaTeX-Standard implementieren
- [ ] **Druckansicht** — CSS @media print optimieren

### Daten
- [ ] **Dynamische Operationen** — OPs aus Bauteilgeometrie ableiten
- [ ] **Werkzeugdatenbank** — Mehr als Demo-Werkzeuge
- [ ] **Materialpreise aktualisieren** — API zu Stahlhandel?

---

## 🟡 WICHTIGE VERBESSERUNGEN (Phase 1)

### Berechnung
- [ ] **Deckungsbeitrag anzeigen** — DB I, DB II, DB III
- [ ] **Break-Even berechnen** — Ab welcher Stückzahl rentabel?
- [ ] **Ist/Soll Vergleich** — Nachkalkulation vs. Vorkalkulation
- [ ] **Lernender Algorithmus** — Feedback → bessere Schätzungen

### Ausgabe
- [ ] **PDF Angebot** — Professionelles Layout mit LaTeX
- [ ] **PDF Fertigungsanweisung** — Druckfertig für Werkstatt
- [ ] **Excel Export** — Für ERP-Import
- [ ] **E-Mail Integration** — Direkt aus App senden

### Onboarding
- [ ] **Erste-Schritte-Wizard** — Stundensätze, Materialpreise eingeben
- [ ] **Beispiel-Projekte** — Mehr als 2 Demo-Teile
- [ ] **Hilfe-Tooltips** — Bei jedem Eingabefeld

---

## 🟢 NICE-TO-HAVE (Phase 2+)

### Features
- [ ] **STEP-Upload** — 3D-Datei → automatische Maßerkennung
- [ ] **CAM-Integration** — NC-Code aus echtem CAM
- [ ] **Maschinenpark-Verwaltung** — Mehrere Maschinen, Kapazitäten
- [ ] **Kundendatenbank** — CRM-lite
- [ ] **Angebots-Archiv** — Historie aller Kalkulationen
- [ ] **Team-Funktionen** — Mehrere Benutzer, Rollen

### Technik
- [ ] **Backend** — Node.js/Python für Persistenz
- [ ] **Datenbank** — PostgreSQL für Projekte, Kunden
- [ ] **Auth** — Login/Registration
- [ ] **Bezahlung** — Stripe Integration
- [ ] **API** — REST für ERP-Anbindung

---

## 🛠️ KONKRETE NÄCHSTE SCHRITTE

### JETZT (vor Demo):
```
1. Zuschlagskalkulation in calculate() Funktion integrieren
2. Ergebnis-Sektion um Deckungsbeitrag erweitern
3. Prüfen dass alle Werte korrekt berechnet werden
```

### DIESE WOCHE:
```
1. Zeichnung-Upload implementieren (FileReader API)
2. Siemens + Fanuc NC-Templates hinzufügen
3. Editierbare Prüftabelle mit +/- Buttons
4. 3 weitere Demo-Bauteile erstellen
```

### NÄCHSTE WOCHE:
```
1. PDF-Export mit LaTeX (Server oder LaTeX.Online API)
2. localStorage für Projekt-Speicherung
3. Mobile-optimierte Ansicht
4. Onboarding-Flow
```

---

## 📐 DESIGN-PRINZIPIEN (nicht vergessen!)

1. **Nachvollziehbarkeit** — Jede Zahl muss erklärbar sein
2. **Transparenz** — Formeln sichtbar, nicht Black Box
3. **Vertrauen** — Echte Daten, Normen-Referenz, Konfidenz-Badges
4. **Einfachheit** — Weniger Klicks, schnellere Ergebnisse
5. **Professionalität** — Aussehen wie SAP, nicht wie Hobby-Tool

---

## 🔧 TECHNISCHE REGELN

### Code-Struktur
- **CSS:** CSS-Variablen für alles (Farben, Spacing, etc.)
- **HTML:** Semantische Struktur, keine Inline-Styles wenn vermeidbar
- **JS:** Funktionen klein halten, klare Namen, Kommentare

### Berechnung
- **Formeln dokumentieren** — REFA, VDI Normen referenzieren
- **Einheiten konsistent** — mm, min, €, kg
- **Rundung:** 2 Dezimalstellen für €, 1 für min

### UX
- **Feedback sofort** — Jede Eingabe → sofortige Neuberechnung
- **Fehler abfangen** — Keine NaN oder undefined anzeigen
- **Loading States** — Bei längeren Operationen Spinner zeigen

---

## 📊 ERFOLGS-METRIKEN

| Metrik | Aktuell | Ziel |
|--------|---------|------|
| Features vs. Spanflug | ~40% | 80% |
| Demo-Bauteile | 2 | 10 |
| Zahlende Kunden | 0 | 1 (Pilot) |
| Bugs/Crashes | ? | 0 |
| Mobile-fähig | Nein | Ja |
| PDF-Export | Basic | LaTeX |

---

## 🧪 TEST-CHECKLISTE

Vor jedem Commit:
- [ ] Projekt auswählen → Loading Animation läuft
- [ ] Alle Tabs funktionieren (Navigation)
- [ ] Werte ändern → Neuberechnung korrekt
- [ ] Einstellungen speichern/laden
- [ ] NC-Code kopieren/download
- [ ] Keine Console-Errors

---

## 📚 REFERENZEN

- **Spanflug MAKE:** https://spanflug.de/make/
- **REFA-Zeitgliederung:** T = tr + ta, tg = th + tn
- **VDI 3321:** Schnittdatenberechnung
- **DIN 8580:** Fertigungsverfahren
- **Report-Design:** `skills/report-design/SKILL.md`
- **LaTeX-Template:** `research/36zero-report.tex`

---

## 💡 IDEEN-SAMMLUNG

*Hier Ideen notieren, die während der Arbeit kommen:*

- [ ] Werkstoff-Empfehlung basierend auf Anforderungen
- [ ] Automatische Angebots-Nummerierung
- [ ] Dark Mode
- [ ] Sprachauswahl (DE/EN)
- [ ] Vergleich: Intern fertigen vs. Zukaufen
- [ ] Kapazitätsplanung: Wann ist Maschine frei?
- [ ] WhatsApp-Benachrichtigung wenn Angebot angenommen

---

## 🚨 BEKANNTE PROBLEME

1. **Zuschläge nicht berechnet** — AV, VwGK, VtGK sind in Settings, aber nicht in calculate()
2. **Statische OPs** — Operationen sind hardcoded, nicht aus Geometrie
3. **Nur Heidenhain** — Siemens/Fanuc zeigen gleichen Code
4. **Kein echter Upload** — Zeichnung ist Demo-Bild

---

## ⏰ ZEITSCHÄTZUNG

| Task | Zeit |
|------|------|
| Zuschläge integrieren | 1h |
| Zeichnung-Upload | 2h |
| NC-Templates (Siemens/Fanuc) | 1h |
| Editierbare Tabellen | 2h |
| PDF-Export (LaTeX) | 4h |
| Mobile-Ansicht | 2h |
| Onboarding-Flow | 3h |
| **Gesamt bis MVP** | ~15h |

---

*Erstellt: 2026-02-05*
*Nächstes Update: Nach Demo mit Onkel*
