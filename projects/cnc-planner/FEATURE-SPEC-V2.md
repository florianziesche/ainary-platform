# CNC Planer Pro — Feature Spec V2

**Erstellt:** 2026-02-05
**Quelle:** Demo-Feedback Andreas + Florians Produkt-Vision

---

## Kernkonzept: Standard vs. Ist-Kalkulation

```
┌─────────────────────────────────────────────────────────┐
│           STANDARD-KALKULATION (DIN-Werte)              │
│  • Richtwerte aus Tabellenbüchern                       │
│  • Allgemeine Schnittdaten nach Material                │
│  • Durchschnittliche Rüstzeiten                         │
│  → Schneller Benchmark, Vergleichbarkeit                │
└─────────────────────────────────────────────────────────┘
                           ↓
┌─────────────────────────────────────────────────────────┐
│           IST-KALKULATION (Individuell)                 │
│  • Maschinenspezifische Limits                          │
│  • Betriebseigene Erfahrungswerte                       │
│  • Angepasste Schnittwerte                              │
│  • Korrigierte Spannvorschläge                          │
│  → Realistische Kalkulation für Angebote               │
└─────────────────────────────────────────────────────────┘
```

---

## Feature 1: Maschinen-Profile

### Beschreibung
Benutzer kann Maschinen mit spezifischen Parametern hinterlegen. Kalkulation passt sich automatisch an.

### Datenstruktur
```yaml
maschine:
  id: "dmg-cmx600"
  name: "DMG Mori CMX 600 V"
  typ: "3-Achs Vertikal"
  
  verfahrwege:
    x: 600  # mm
    y: 560  # mm
    z: 510  # mm
  
  spindel:
    max_drehzahl: 12000  # U/min
    leistung: 18  # kW
    drehmoment: 86  # Nm (bei 40% ED)
    aufnahme: "SK40"  # oder HSK-A63, BT40, etc.
  
  vorschübe:
    eilgang_xy: 30000  # mm/min
    eilgang_z: 24000  # mm/min
    arbeitsvorschub_max: 15000  # mm/min
  
  werkzeugwechsel:
    zeit: 4  # Sekunden
    magazin_plätze: 24
  
  steuerung: "Heidenhain TNC 620"
  
  # Betriebsspezifisch
  stundensatz: 85  # €/h
  verfügbarkeit: 0.85  # 85% Nutzungsgrad
```

### UI-Konzept
- Maschinenauswahl per Dropdown
- "Neue Maschine anlegen" Button
- Import von Hersteller-Datenblättern (PDF → Auto-Extract)

---

## Feature 2: Schnittwerte anpassbar

### Problem
API liefert Hersteller-Empfehlungen, aber:
- Maschine hat weniger Leistung
- Material weicht ab
- Oberfläche muss besser sein
- Betrieb hat eigene Erfahrungswerte

### Lösung
```
┌─────────────────────────────────────────┐
│  Werkzeug: VHM Schaftfräser Ø10         │
├─────────────────────────────────────────┤
│  Parameter    │ API-Wert │ Ihr Wert    │
├───────────────┼──────────┼─────────────┤
│  vc (m/min)   │   200    │  [180]  ✏️  │
│  fz (mm/Zahn) │   0.05   │  [0.04] ✏️  │
│  ap (mm)      │   10     │  [8]    ✏️  │
│  ae (mm)      │   5      │  [4]    ✏️  │
└───────────────┴──────────┴─────────────┘
  [ ] Als Standard für dieses Werkzeug speichern
```

### Logik
1. API-Werte als Ausgangspunkt
2. Benutzer kann überschreiben
3. Optional: Als Betriebsstandard speichern
4. Warnung wenn Werte außerhalb sicherer Bereiche

---

## Feature 3: Spann-Vorschlag mit Korrektur

### Automatischer Vorschlag basierend auf:
- Geometrie (L × B × H)
- Gewicht
- Toleranzen
- Anzahl bearbeitete Seiten

### Regeln
```python
def spann_vorschlag(teil):
    if teil.länge > 300 and teil.breite < 100:
        return "2× Schraubstock oder Tischspannung"
    
    if teil.höhe > teil.breite * 1.5:
        return "Warnung: Kippgefahr — Abstützung empfohlen"
    
    if teil.seiten_bearbeitet > 1:
        return f"{teil.seiten_bearbeitet} Aufspannungen nötig"
    
    if teil.gewicht > 20:
        return "Kran/Hebezeug erforderlich"
    
    return "Standard: 1× Schraubstock"
```

### UI-Konzept
```
┌─────────────────────────────────────────┐
│  SPANNUNG                               │
├─────────────────────────────────────────┤
│  Vorschlag: 2× Schraubstock             │
│  Grund: Teil ist 435mm lang             │
│                                         │
│  [ ] Vorschlag übernehmen               │
│  [●] Eigene Eingabe:                    │
│      [Tischspannung + Stützbock    ] ▼  │
│                                         │
│  Rüstzeit-Anpassung: [+50%] (komplexer) │
└─────────────────────────────────────────┘
```

---

## Feature 4: NC-Code Optionen

### Checkboxen bei Programmgenerierung:
- [ ] **Anbohrungen einfügen** (vor Tieflochbohren/Gewinde)
- [ ] **Kühlmittel-Steuerung** (M8/M9 automatisch)
- [ ] **Eilgang reduzieren** auf [___]% 
- [ ] **Sicherheitsabstand** [___] mm (Standard: 5mm)
- [ ] **Werkzeugwechsel-Position** (Mitte / Ecke / Benutzerdefiniert)
- [ ] **Kommentare einfügen** (für bessere Lesbarkeit)

### Erweiterung Heidenhain-spezifisch:
- [ ] **TOOL CALL mit TOOL DEF** 
- [ ] **Messzyklen einfügen** (Werkzeuglänge, Radius)
- [ ] **Palettenprogramm** generieren

---

## Feature 5: Feedback-Loop (Lernen)

### Workflow:
```
1. Kalkulation erstellen
   → Geschätzte Zeit: 45 min
   → Geschätzte Rüstzeit: 20 min

2. Fertigung durchführen

3. Ist-Daten erfassen (nach Auftrag):
   ┌─────────────────────────────────────┐
   │  Auftrag #2024-0815 abgeschlossen   │
   │                                     │
   │  Tatsächliche Fertigungszeit:       │
   │  [52] min (Schätzung war 45 min)    │
   │                                     │
   │  Tatsächliche Rüstzeit:             │
   │  [28] min (Schätzung war 20 min)    │
   │                                     │
   │  Kommentar:                         │
   │  [Ausrichten hat länger gedauert]   │
   │                                     │
   │  [Speichern & Lernen]               │
   └─────────────────────────────────────┘

4. System lernt:
   - Korrekturfaktor für ähnliche Geometrien
   - Betriebsspezifische Rüstzeit-Multiplikatoren
   - Material/Maschinen-Kombinationen
```

### Datenspeicherung:
```yaml
kalkulation_feedback:
  teil_id: "2500473.01.11.02.00.001"
  material: "S235JR"
  maschine: "dmg-cmx600"
  
  geplant:
    fertigungszeit: 45
    rüstzeit: 20
  
  ist:
    fertigungszeit: 52
    rüstzeit: 28
  
  abweichung:
    fertigungszeit: +15.5%
    rüstzeit: +40%
  
  tags: ["tischspannung", "erstauftrag", "ausrichten_komplex"]
```

---

## Feature 6: Aufspannungs-Visualisierung (Future)

### Konzept:
3D-Vorschau zeigt:
- Rohteil-Position
- Schraubstock/Spannmittel
- Werkstück-Nullpunkt (WCS)
- Bearbeitungsrichtungen pro Aufspannung

### Nutzen:
- Bediener versteht sofort wie gespannt werden soll
- Reduziert Rückfragen
- Dokumentation für Wiederholaufträge

---

## Priorisierung

| Feature | Prio | Aufwand | MVP? |
|---------|------|---------|------|
| Maschinen-Profile | ⭐⭐⭐ | Mittel | ✅ |
| Schnittwerte anpassbar | ⭐⭐⭐ | Niedrig | ✅ |
| Spann-Vorschlag + Korrektur | ⭐⭐⭐ | Mittel | ✅ |
| NC-Code Optionen | ⭐⭐ | Mittel | ❌ |
| Standard vs. Ist-Kalkulation | ⭐⭐ | Hoch | ❌ |
| Feedback-Loop | ⭐ | Hoch | ❌ |
| 3D-Visualisierung | ⭐ | Sehr hoch | ❌ |

---

## Nächste Schritte

1. [ ] Maschinen-Profil UI implementieren
2. [ ] Schnittwert-Override in bestehende UI einbauen
3. [ ] Spann-Logik als Regelwerk definieren
4. [ ] Mit Andreas validieren: Sind die Regeln sinnvoll?
5. [ ] Feedback nach Pilotphase sammeln

---

*Dieses Dokument wird nach jedem Kunden-Feedback aktualisiert.*
