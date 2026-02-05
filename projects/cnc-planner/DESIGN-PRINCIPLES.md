# CNC Planner Pro — Design-Prinzipien

*Leitprinzipien für Produktentwicklung, basierend auf Branchenanforderungen und State-of-the-Art.*

---

## 1. Nachvollziehbarkeit (Traceability)

### Warum es wichtig ist
Fertigungsbetriebe müssen Kalkulationen gegenüber Kunden, Einkauf und Controlling rechtfertigen. "Der Computer hat das berechnet" reicht nicht.

### Branchenanforderung
- **ISO 9001:** Dokumentierte Prozesse, nachvollziehbare Entscheidungen
- **Automotive (IATF 16949):** Lückenlose Rückverfolgbarkeit
- **Kundenanforderung:** "Wie kommen Sie auf den Preis?"

### Umsetzung im CNC Planner

| Prinzip | Implementierung |
|---------|-----------------|
| **Formel sichtbar** | Jeder Kostenpunkt zeigt die Berechnungsformel |
| **Eingaben → Ausgaben** | Klare Verbindung zwischen Parametern und Ergebnis |
| **Änderungshistorie** | Was wurde wann geändert (für Audit) |
| **Export mit Berechnung** | PDF/Excel enthält vollständige Kalkulation |

### Konkrete UI-Elemente
```
Bearbeitung: €18,96
└─ 12,5 min × €91/h (CNC gesamt)
   └─ Lohn €49/h + Maschine €42/h
```

### State-of-the-Art Referenz
- **Paperless Parts:** Zeigt Berechnungslogik im "Pricing Waterfall"
- **SAP:** Kalkulationsschema mit Zuschlagssätzen
- **b-logic:** Stundenverrechnungssätze aufgeschlüsselt

---

## 2. Transparenz (Transparency)

### Warum es wichtig ist
Vertrauen entsteht durch Offenheit. Versteckte Berechnungen erzeugen Misstrauen ("Da rechnen die sich reich").

### Branchenanforderung
- **Einkäufer erwarten:** Aufschlüsselung Material vs. Fertigung
- **Großkunden fordern:** Open-Book-Kalkulation
- **Wettbewerb:** Wer transparent ist, gewinnt Vertrauen

### Umsetzung im CNC Planner

| Prinzip | Implementierung |
|---------|-----------------|
| **Datenquellen nennen** | "Basierend auf echten Fertigungsdaten" |
| **Grenzen ehrlich angeben** | "±15% Genauigkeit für Standardteile" |
| **Annahmen dokumentieren** | Referenzmaschine, Standardwerkzeuge |
| **Keine Black Box** | Benutzer sieht ALLE Parameter |

### Konkrete UI-Elemente
```
┌─────────────────────────────────────────────┐
│ ℹ️ Kalkulationsgrundlage                    │
├─────────────────────────────────────────────┤
│ Referenzmaschine: 3-Achs Hermle C400        │
│ Stundensätze: b-logic Kalkulationsblatt     │
│ Materialpreise: Stand Februar 2026          │
│ Genauigkeit: ±15% für prismatische Teile    │
└─────────────────────────────────────────────┘
```

### Was wir NICHT können (ehrlich kommunizieren)
- Automatische Geometrieerkennung aus CAD
- 5-Achs-Strategien berechnen
- Toleranzen < IT8 berücksichtigen
- Sonderwerkstoffe (Titan, Inconel)

### State-of-the-Art Referenz
- **Xometry:** Zeigt Preisrange + Confidence Level
- **Hubs:** "Instant Quote" mit klaren Limitationen
- **Fictiv:** Transparente Design-for-Manufacturing Hinweise

---

## 3. Nutzer-Dokumentation (User Documentation)

### Warum es wichtig ist
Software ohne Dokumentation ist Shelfware. Arbeitsvorbereiter haben keine Zeit für Trial-and-Error.

### Branchenanforderung
- **Zertifizierungen:** Dokumentierte Arbeitsanweisungen (ISO)
- **Einarbeitung:** Neue Mitarbeiter müssen schnell produktiv sein
- **Support-Reduktion:** Gute Docs = weniger Anfragen

### Umsetzung im CNC Planner

| Prinzip | Implementierung |
|---------|-----------------|
| **Kontextuelle Hilfe** | Tooltips direkt am Element |
| **Inline-Erklärungen** | Was bedeutet "Spannung"? |
| **Beispiel-Teile** | Echte Bauteile zum Lernen |
| **Funktionsbeschreibung** | Was kann die Software (und was nicht) |

### Dokumentations-Struktur

```
📁 Dokumentation
├── Schnellstart (2 min)
│   └── Teil laden → Berechnen → Fertig
├── Funktionsbeschreibung
│   ├── Anwendungsbereich
│   ├── Berechnungsprinzip
│   └── Grenzen
├── Einstellungen anpassen
│   ├── Stundensätze
│   ├── Materialpreise
│   └── Maschinenspezifisch
├── Für Fortgeschrittene
│   ├── Mehrfach-Aufspannung
│   ├── Mengenkalkulation
│   └── Export-Optionen
└── FAQ / Troubleshooting
```

### In-App Dokumentation

**Tooltips (Hover):**
```
Spannung [?]
└─ "Wie wird das Teil auf der Maschine fixiert?
    Beeinflusst Einrichtzeit und Zugänglichkeit."
```

**Info-Boxen (Kontext):**
```
ℹ️ Bei 6-Seiten-Bearbeitung: Mindestens 2 Aufspannungen.
   Automatische Erkennung nicht möglich — bitte manuell angeben.
```

**Onboarding (Erstnutzung):**
```
Willkommen bei CNC Planner Pro!

1. Passen Sie die Stundensätze an Ihren Betrieb an
2. Wählen Sie ein Beispielteil oder laden Sie eigenes
3. Sehen Sie sofort die Kalkulation

→ Zu den Einstellungen
```

### State-of-the-Art Referenz
- **Notion:** Inline-Hilfe + Templates + Tooltips
- **Linear:** Keyboard Shortcuts sichtbar
- **Figma:** Interaktive Tutorials

---

## 4. Branchenspezifische Anforderungen

### Maschinenbau / CNC-Fertigung

| Anforderung | Umsetzung |
|-------------|-----------|
| **DIN/ISO-Konformität** | Bezeichnungen nach Norm (IT8, Ra, etc.) |
| **Werkstoff-Bezeichnung** | 1.4301 UND V2A zeigen |
| **Maßeinheiten** | mm, kg, min — keine Umrechnung nötig |
| **Fachsprache** | "Spannung" nicht "Befestigung" |

### Qualitätsmanagement

| Anforderung | Umsetzung |
|-------------|-----------|
| **Audit-Trail** | Wer hat wann was geändert |
| **Versionierung** | Alte Kalkulationen abrufbar |
| **Export** | PDF mit Zeitstempel + Benutzer |

### Integration

| Anforderung | Umsetzung |
|-------------|-----------|
| **ERP-Schnittstelle** | Export für SAP, ProAlpha, etc. |
| **CAD-Import** | STEP/PDF Unterstützung (später) |
| **Datenbank** | Materialstamm pflegbar |

---

## 5. Anti-Patterns (Was wir NICHT tun)

| Anti-Pattern | Warum schlecht | Stattdessen |
|--------------|----------------|-------------|
| **Schwarze Box** | Kein Vertrauen | Formeln zeigen |
| **Falsche Präzision** | €64,8923 suggeriert Genauigkeit die nicht existiert | €64,89 + "±15%" |
| **Feature-Overload** | Überfordert Nutzer | Progressive Disclosure |
| **Englische UI** | Zielgruppe ist DE/AT/CH | Konsequent Deutsch |
| **Bunte Farben** | Wirkt unseriös | Industrielles Design |
| **Versteckte Einstellungen** | Nutzer findet sie nicht | Prominent platzieren |

---

## 6. Validierung der Prinzipien

### Wie wir prüfen ob wir's richtig machen

**Nachvollziehbarkeit:**
- [ ] Kann ein Dritter die Kalkulation verstehen?
- [ ] Sind alle Eingaben → Ausgaben nachvollziehbar?
- [ ] Würde die Kalkulation einem Audit standhalten?

**Transparenz:**
- [ ] Sind Datenquellen genannt?
- [ ] Sind Grenzen ehrlich kommuniziert?
- [ ] Weiß der Nutzer was die Software NICHT kann?

**Dokumentation:**
- [ ] Kann ein neuer Nutzer ohne Einweisung starten?
- [ ] Sind Fachbegriffe erklärt?
- [ ] Gibt es Hilfe im Kontext (nicht nur in separater Doku)?

---

## 7. Zusammenfassung

### Die drei Säulen

```
┌─────────────────────────────────────────────────────────┐
│                    CNC PLANNER PRO                      │
├─────────────────┬─────────────────┬─────────────────────┤
│ NACHVOLLZIEHBAR │   TRANSPARENT   │    DOKUMENTIERT     │
├─────────────────┼─────────────────┼─────────────────────┤
│ Formeln zeigen  │ Grenzen nennen  │ Hilfe im Kontext    │
│ Audit-fähig     │ Datenquellen    │ Beispiele bieten    │
│ Änderungs-Log   │ Keine Black Box │ Onboarding          │
└─────────────────┴─────────────────┴─────────────────────┘
```

### Das Versprechen

> **"Jede Zahl hat eine Erklärung. Jede Grenze ist dokumentiert. Jeder Nutzer weiß, was er tut."**

---

## Referenzen

- **Paperless Parts:** paperlessparts.com — US Marktführer CPQ
- **Xometry:** xometry.com — Instant Quote mit Confidence Levels
- **Hubs (Protolabs):** hubs.com — Upload → Configure → Quote
- **b-logic:** Kalkulationsblatt als Referenz für Stundensätze
- **ISO 9001:2015:** Qualitätsmanagement-Dokumentation
- **VDI 3633:** Simulation in der Produktion

---

*Dokument erstellt: 2026-02-05*
*Für: CNC Planner Pro v15+*
