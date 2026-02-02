# CNC Planner — System-Dokumentation

*Intelligente Fertigungsplanung für CNC-Betriebe*

---

## Übersicht

CNC Planner ist eine Web-App zur automatischen Kalkulation von CNC-Fertigungszeiten, Kosten und Angeboten.

**Status:** Demo-Phase (v12)
**Target:** Maschinenbau Schlottwitz (Onkel als Pilot)
**Revenue Target:** €750/Monat

---

## Versionen

| Version | Datum | Features | Status |
|---------|-------|----------|--------|
| v7 | 2026-01-31 | Landing Page Style FA | Archiv |
| v8 | 2026-02-01 | ROI + 4 Tabs | Basis für v11 |
| v9 | 2026-02-01 | 3 Projekte + NC-Code | Content |
| v10 | 2026-02-02 | Ohne Emojis | Zwischenschritt |
| v11 | 2026-02-02 | Kombination v8+v10 | Überholt |
| **v12** | **2026-02-02** | **Finale Demo** | **AKTUELL** |

---

## Aktuelle Version (v12)

### Features

1. **Projekt-Kalkulation**
   - 3 Beispielprojekte (Grundplatte, Lagerbock, Flansch)
   - Detaillierte Operationen (OP10, OP20, OP50)
   - Aufklappbare Berechnungsdetails

2. **Kostenberechnung**
   - Material inkl. 10% Verschnitt
   - Werkzeugkosten (Standzeit-basiert)
   - Maschinenkosten (Stundensatz)
   - Variable Marge

3. **NC-Code Export**
   - Heidenhain
   - Siemens
   - Fanuc
   - Beta-Status mit Feedback-Link

4. **ROI-Rechner**
   - Zeitersparnis-Kalkulation
   - Break-even Berechnung

### Dateien

```
~/.openclaw/workspace/projects/cnc-planner/
├── demo-v12.html          ← Aktuelle Demo
├── app-v4.html            ← Enhanced FA Version
├── landing.html           ← Landing Page
└── demo-v[7-11].html      ← Ältere Versionen
```

---

## Landing Page

**URL:** (noch nicht deployed)
**Pricing:**
- Professional: €199/Monat + €500 Einrichtung
- Includes: Persönliches Onboarding

**Value Props:**
- 85% schnellere Kalkulation
- +40% mehr Angebote möglich
- 10x ROI Garantie

---

## Demo-Werte

| Kennzahl | Wert |
|----------|------|
| Material | €55,98 (inkl. Verschnitt) |
| Werkzeuge | €20,74 |
| Maschinenzeit | 45 min |
| Gesamt | €135,94 |
| Verkaufspreis (10% Marge) | €149,53 |

---

## Technische Architektur

### Frontend
- Vanilla HTML/CSS/JavaScript
- Responsive Design
- Kein Framework (bewusst einfach)

### Backend (geplant)
- Python FastAPI
- PostgreSQL
- PDF-Upload für CAD-Analyse

---

## Roadmap

### Phase 1 — Pilot (Feb 2026)
- [x] Demo fertig
- [ ] Onkel-Meeting
- [ ] Pilot-Vertrag €750/Monat

### Phase 2 — MVP (März 2026)
- [ ] User Login
- [ ] Projekt-Speicherung
- [ ] PDF Upload

### Phase 3 — Scale (Q2 2026)
- [ ] Weitere Kunden
- [ ] API Integration
- [ ] CAM-File Support

---

## Geplante Features

1. **Live Rohmaß → Zeit** — Maße ändern, Zeit berechnet sich
2. **Serienkalkulation** — Rüstzeit auf Stückzahl verteilt
3. **Ist/Soll-Vergleich** — System lernt aus realen Zeiten

---

*Erstellt: 2026-02-02*
*Nächste Aktion: Onkel anrufen!*
