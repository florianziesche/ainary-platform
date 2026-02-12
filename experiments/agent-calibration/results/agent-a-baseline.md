# Agent A — Baseline

## CNC-Bearbeitungszeit Kalkulation

### Werkstück-Parameter
- Material: GJS-700 (Sphäroguss)
- Abmessungen: 2095 × 500 × 190 mm
- Anzahl Aufspannungen: 4
- Bearbeitungsschritte: Planfräsen, Konturfräsen, Bohren, Gewinde

### Kalkulationslogik

**1. Planfräsen (pro Aufspannung)**
- Fläche pro Seite: ca. 1.047.500 mm² (2095 × 500)
- Schnittgeschwindigkeit GJS-700: ~150 m/min
- Vorschub: ~0,2 mm/Zahn, 4-Schneider
- Zustellung: 2-3 mm
- Bearbeitungszeit pro Fläche: ~25-35 min
- 4 Aufspannungen → 120-140 min

**2. Konturfräsen**
- Geschätzte Konturlänge pro Aufspannung: ~3.000 mm
- Vorschubgeschwindigkeit: 800-1200 mm/min
- Mehrere Durchgänge (Schruppen + Schlichten): 3-4 Durchgänge
- Zeit pro Aufspannung: ~15-20 min
- 4 Aufspannungen → 60-80 min

**3. Bohren**
- Geschätzte Anzahl Bohrungen: 40-60 (bei dieser Bauteilgröße typisch)
- Durchmesser: Ø 8-20 mm gemischt
- Bohrzeit pro Loch: 1-3 min (inkl. Positionierung)
- Gesamt: 80-120 min

**4. Gewinde schneiden**
- Geschätzte Gewinde: 30-40
- Zeit pro Gewinde (M6-M16): 2-4 min
- Gesamt: 60-100 min

**5. Nebenzeiten**
- Werkzeugwechsel: ~40 min
- Umspannen (4×): ~60 min
- Einrichten/Mess-Zyklen: ~50 min
- Gesamt Nebenzeiten: 150 min

### Gesamtkalkulation

| Vorgang | Zeit (min) |
|---------|------------|
| Planfräsen | 120-140 |
| Konturfräsen | 60-80 |
| Bohren | 80-120 |
| Gewinde | 60-100 |
| Nebenzeiten | 150 |
| **GESAMT** | **470-590** |

### Ergebnis

**Geschätzte Bearbeitungszeit: 520-580 Minuten**
**Mittelwert: 550 Minuten (~9,2 Stunden)**

**Konfidenzintervall: 520-580 min, 75% confident**

### Begründung der Unsicherheit
- Keine exakte Zeichnung vorhanden (Anzahl Bohrungen/Gewinde geschätzt)
- Konturenkomplexität unbekannt
- Maschinentyp und -zustand nicht spezifiziert
- Erfahrung des Programmierers/Bedieners variabel
- Werkzeugverschleiß bei GJS-700 kann Zeiten beeinflussen

Die Schätzung basiert auf Standardwerten für GJS-700 und typischen Bearbeitungsparametern für Gussteile dieser Größenordnung.
