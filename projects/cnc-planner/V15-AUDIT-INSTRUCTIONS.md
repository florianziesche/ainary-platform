# V15 AUDIT INSTRUCTIONS — Systematische Feature-Analyse

## 🎯 Ziel
v15 muss MINDESTENS alle Features von v14 haben, PLUS neue Trust-Features.
Kein Feature darf verloren gehen.

---

## Phase 1: Kundenanforderungen verstehen

### Wer ist der Kunde?
- **Primär:** Arbeitsvorbereiter in CNC-Lohnfertigung (wie Andreas)
- **Kontext:** Muss schnell kalkulieren, aber NACHVOLLZIEHBAR
- **Schmerz:** Excel-Tabellen, Bauchgefühl, keine Dokumentation
- **Ziel:** Vertrauen durch Transparenz, nicht durch Magie

### Was braucht der Kunde?
1. **Schnelle Kalkulation** — <30 Sekunden für Standardteil
2. **Nachvollziehbarkeit** — Jede Zahl erklärbar, jede Formel sichtbar
3. **Anpassbarkeit** — Seine Stundensätze, seine Materialpreise
4. **Flexibilität** — Arbeitsgänge hinzufügen/entfernen
5. **Dokumentation** — PDF für Angebot, für Fertigung
6. **Lernen** — System wird besser durch sein Feedback

### Kundenerwartung an UI:
- Sieht aus wie SAP/b-logic (vertraut, nicht "spielzeughaft")
- Keine Überraschungen — alles nachvollziehbar
- Professionelle Dokumente

---

## Phase 2: v14 Feature-Inventar

### ANWEISUNG: Lies v14 komplett und dokumentiere JEDES Feature

**Kategorien:**
1. **Eingabe-Features** (was der User eingeben kann)
2. **Berechnungs-Features** (was berechnet wird)
3. **Anzeige-Features** (wie es dargestellt wird)
4. **Export-Features** (was ausgegeben werden kann)
5. **Individualisierungs-Features** (was angepasst werden kann)
6. **Feedback-Features** (wie der User zurückmelden kann)
7. **UX-Features** (Interaktionen, Animationen, Hilfen)

### Dokumentiere für jedes Feature:
- [ ] Name
- [ ] Beschreibung
- [ ] Wo in v14 (Zeile/Tab)
- [ ] In v15 vorhanden? Ja/Nein
- [ ] Wenn Nein: Muss rein

---

## Phase 3: Fehlende Features identifizieren

### Bekannte Lücken (Initial-Liste):

#### Berechnungen:
- [ ] **Expandierbare Berechnungsdetails** — Klick auf Zeile zeigt Formel
- [ ] **Operationen-Tabelle** — Alle OPs mit Zeiten einzeln
- [ ] **Hauptzeit/Nebenzeit Trennung** — th vs tn
- [ ] **Werkzeugkosten-Tabelle** — Jedes Tool mit Preis, Standzeit, Einsatz
- [ ] **Schnittparameter-Tabelle** — Vc, n, fz, vf, ap, ae pro Werkzeug
- [ ] **Prüfzeit-Tabelle** — Editierbar mit Prüfmitteln

#### Individualisierbarkeit:
- [ ] **Arbeitsgänge hinzufügen** — Button "+ Arbeitsgang"
- [ ] **Arbeitsgänge entfernen** — × Button pro Zeile
- [ ] **Prüfmerkmale hinzufügen** — Button "+ Prüfung"
- [ ] **Prüfmerkmale entfernen** — × Button pro Zeile
- [ ] **Prüfmittel-Dropdown** — Mit Zeitvorschlag
- [ ] **Prüfzeit in Kalkulation** — Checkbox ob einrechnen

#### Feedback:
- [ ] **Feedback-Sektion** — Am Ende der Fertigungsanweisung
- [ ] **Feedback-Optionen** — Correct / Too High / Too Low / Other
- [ ] **Kommentar-Feld** — Freitext
- [ ] **Ist/Soll Vergleich** — Eingabe tatsächlicher Zeiten
- [ ] **Lern-Indikator** — "System lernt aus Ihrem Feedback"

#### Anzeige:
- [ ] **Loading Animation** — 5 Schritte beim Laden
- [ ] **Zeichnungs-Preview** — Aufklappbar, Vollbild
- [ ] **Zeichnungs-Upload** — In Fertigungsanweisung
- [ ] **Collapsible Sections** — Für lange Inhalte
- [ ] **Troubleshooting-Tabelle** — Problem/Ursache/Maßnahme

#### Navigation:
- [ ] **Tab "Werkzeuge"** — Separate Schnittparameter-Ansicht
- [ ] **Tab "Kalkulation"** — Detaillierte Kostenaufschlüsselung

---

## Phase 4: Golden Standard Research

### Existierende Dokumente nutzen:
```
research/golden-standards/
├── design-system.md      — CSS, Farben, Spacing
├── sidebar-navigation.md — Navigation Pattern
├── form-inputs.md        — Input Styling
└── price-display.md      — Preisanzeige
```

### Neue Research nötig für:
- [ ] **Expandable Calculation Rows** — Wie zeigen CPQ-Tools Details?
- [ ] **Editable Tables** — Best Practice für editierbare Zeilen
- [ ] **Feedback Collection** — Wie sammeln SaaS-Tools Feedback?

---

## Phase 5: Implementation

### Reihenfolge (nach Kundenwert):
1. **Alle Berechnungen vollständig** — Ohne das ist alles andere nutzlos
2. **Expandierbare Details** — Nachvollziehbarkeit ist Kernversprechen
3. **Editierbare Arbeitsgänge** — Individualisierung ist USP
4. **Feedback-System** — Lernen ist Differenzierung
5. **Export & Dokumentation** — Deliverables müssen funktionieren

### Definition of Done für v15:
- [ ] ALLE v14 Features vorhanden
- [ ] ALLE neuen Trust-Features (Konfidenz, Tooltips, Warnungen)
- [ ] ALLE Berechnungen expandierbar
- [ ] Arbeitsgänge hinzufügbar/entfernbar
- [ ] Prüfmerkmale hinzufügbar/entfernbar
- [ ] Feedback-Sektion funktional
- [ ] PDF Export funktioniert
- [ ] Einstellungen persistieren (localStorage)

---

## Nächste Schritte

1. **JETZT:** v14 komplett lesen (alle ~5500 Zeilen)
2. **Feature-Inventar erstellen** (neues Dokument)
3. **Gap-Analyse** — Was fehlt in v15?
4. **Priorisieren** — Was ist kritisch?
5. **Implementieren** — Feature für Feature
6. **Validieren** — Gegen v14 checken

---

*Erstellt: 2026-02-05 18:45*
