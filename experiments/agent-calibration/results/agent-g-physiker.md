# Agent G — Physiker (First Principles)

## Aufgabenstellung
**Material:** GJS-700 (Sphäroguss)  
**Abmessungen:** 2095 × 500 × 190 mm  
**Aufspannungen:** 4  
**Operationen:** Planfräsen, Konturfräsen, Bohren, Gewinde

---

## Physikalische Grundlagen

### Materialeigenschaften GJS-700
- **Härte:** HB 240-300 (Mittelwert: HB 270)
- **Empfohlene Schnittgeschwindigkeit:** vc = 120-180 m/min (Hartmetall beschichtet)
- **Physikalische Basis:** vc = 150 m/min als Arbeitswert (Mittelwert)

### Fundamentale Formeln

**Schnittgeschwindigkeit:**
```
vc = (π × d × n) / 1000
→ n = (vc × 1000) / (π × d)
```

**Vorschubgeschwindigkeit:**
```
vf = fz × z × n
```

**Hauptzeit:**
```
th = Schnittweg / vf
```

**Materialabtrag:**
```
V = L × B × ap
```

---

## 1. PLANFRÄSEN (4 Aufspannungen)

### Flächenberechnung
- **2 große Flächen:** 2095 × 500 mm = 1.047.500 mm² (je Fläche)
- **2 mittlere Flächen:** 2095 × 190 mm = 397.050 mm² (je Fläche)
- **Annahme:** Pro Aufspannung wird mind. 1 große Referenzfläche geschlichtet

### Werkzeugparameter Planfräser
- **Durchmesser:** d = 100 mm (typischer Planfräser für diese Größe)
- **Schneidenzahl:** z = 8 (Hartmetall-Wendeschneidplatten)
- **Schnitttiefe:** ap = 2 mm (Schlichtschnitt für Genauigkeit)
- **Vorschub pro Zahn:** fz = 0.25 mm (konservativ für GJS-700)

### Berechnung Drehzahl
```
n = (vc × 1000) / (π × d)
n = (150 × 1000) / (π × 100)
n = 150000 / 314.16
n ≈ 477 U/min
```

### Berechnung Vorschubgeschwindigkeit
```
vf = fz × z × n
vf = 0.25 × 8 × 477
vf = 954 mm/min
```

### Berechnung Hauptzeit pro Fläche

**Große Fläche (2095 × 500 mm):**
- **Effektive Breite pro Übergang:** 80 mm (ae = 0.8 × d bei Planfräsen)
- **Anzahl Übergänge:** 500 / 80 ≈ 6.25 → 7 Übergänge
- **Schnittweg pro Übergang:** 2095 mm + 50 mm (Anlauf/Auslauf) = 2145 mm
- **Gesamter Schnittweg:** 7 × 2145 = 15.015 mm

```
th = Schnittweg / vf
th = 15.015 / 954
th ≈ 15.74 min
```

**4 Aufspannungen (jeweils 1 große Referenzfläche):**
```
t_Planfräsen = 4 × 15.74 = 62.96 min
```

---

## 2. KONTURFRÄSEN

### Konturannahmen
- **Konturlänge gesamt:** ~8000 mm (Außenkontur + innere Taschen/Durchbrüche)
- **Mittlere Tiefe:** 40 mm
- **Anzahl Tiefenschnitte:** 40 / 5 = 8 Schnitte (ap = 5 mm pro Schnitt)

### Werkzeugparameter Schaftfräser
- **Durchmesser:** d = 20 mm
- **Schneidenzahl:** z = 4
- **Vorschub pro Zahn:** fz = 0.15 mm (konturgenau)

### Berechnung Drehzahl
```
n = (150 × 1000) / (π × 20)
n = 150000 / 62.83
n ≈ 2387 U/min
```

### Berechnung Vorschubgeschwindigkeit
```
vf = 0.15 × 4 × 2387
vf = 1432 mm/min
```

### Berechnung Hauptzeit
```
Gesamter Schnittweg = 8000 mm × 8 Tiefenschnitte = 64.000 mm

th = 64.000 / 1432
th ≈ 44.69 min
```

---

## 3. BOHREN

### Bohrungsannahmen
- **Anzahl Bohrungen:** 40 Stück (Mix aus M6-M16)
- **Durchschnittliche Tiefe:** 50 mm
- **Mittlerer Durchmesser:** 12 mm

### Werkzeugparameter Bohrer
- **Durchmesser:** d = 12 mm
- **Schnittgeschwindigkeit:** vc = 80 m/min (reduziert für Bohren in GJS)
- **Vorschub pro Umdrehung:** f = 0.2 mm/U

### Berechnung Drehzahl
```
n = (80 × 1000) / (π × 12)
n = 80000 / 37.7
n ≈ 2122 U/min
```

### Berechnung Vorschubgeschwindigkeit
```
vf = f × n = 0.2 × 2122
vf = 424 mm/min
```

### Berechnung Hauptzeit
```
Schnittweg pro Bohrung = 50 mm + 5 mm (Überlauf) = 55 mm
Gesamter Schnittweg = 40 × 55 = 2200 mm

th = 2200 / 424
th ≈ 5.19 min
```

---

## 4. GEWINDESCHNEIDEN

### Gewindeannahmen
- **Anzahl Gewinde:** 40 Stück (korrespondierend zu Bohrungen)
- **Mittlere Gewindetiefe:** 40 mm
- **Mittleres Gewinde:** M10 (Steigung P = 1.5 mm)

### Werkzeugparameter Gewindebohrer
- **Schnittgeschwindigkeit:** vc = 15 m/min (stark reduziert für formende Zerspanung)
- **Vorschub:** f = P = 1.5 mm/U (zwingend gleich Steigung)

### Berechnung Drehzahl
```
n = (15 × 1000) / (π × 10)
n = 15000 / 31.42
n ≈ 477 U/min
```

### Berechnung Vorschubgeschwindigkeit
```
vf = 1.5 × 477
vf = 716 mm/min
```

### Berechnung Hauptzeit
```
Schnittweg pro Gewinde = 40 mm × 2 (Einschrauben + Rückwärts) = 80 mm
Gesamter Schnittweg = 40 × 80 = 3200 mm

th = 3200 / 716
th ≈ 4.47 min
```

---

## 5. NEBENZEITEN

### Werkzeugwechsel
- **Anzahl Werkzeugwechsel:** ~12 (Planfräser, 3 Schaftfräser, 4 Bohrer, 4 Gewindebohrer)
- **Zeit pro Wechsel:** 1.5 min (automatisch)
```
t_WZW = 12 × 1.5 = 18 min
```

### Aufspannwechsel
- **Anzahl:** 3 Wechsel (4 Aufspannungen → 3 Wechsel)
- **Zeit pro Wechsel:** 15 min (Schwenken, Ausrichten, Antasten)
```
t_Aufspannung = 3 × 15 = 45 min
```

### Messtaster / Kontrolle
- **Anzahl Messvorgänge:** 8 (nach jeder Aufspannung + kritische Maße)
- **Zeit pro Messung:** 3 min
```
t_Messen = 8 × 3 = 24 min
```

---

## GESAMTZEIT-BERECHNUNG

| Operation | Hauptzeit (min) |
|-----------|----------------|
| Planfräsen | 62.96 |
| Konturfräsen | 44.69 |
| Bohren | 5.19 |
| Gewinde | 4.47 |
| **Summe Hauptzeit** | **117.31** |
| | |
| Werkzeugwechsel | 18.00 |
| Aufspannwechsel | 45.00 |
| Messen/Kontrolle | 24.00 |
| **Summe Nebenzeit** | **87.00** |
| | |
| **GESAMTZEIT** | **204.31 min** |

---

## KONFIDENZINTERVALL

### Unsicherheitsquellen

1. **Schnittparameter-Varianz:** ±10%
   - vc kann zwischen 120-180 m/min variieren
   - fz-Werte hängen von Werkzeugqualität ab

2. **Geometrie-Annahmen:** ±15%
   - Tatsächliche Konturlänge unbekannt
   - Anzahl Bohrungen/Gewinde geschätzt

3. **Maschinendynamik:** ±5%
   - Beschleunigung/Verzögerung nicht berücksichtigt
   - Eckenverhalten bei Konturen

4. **Werkzeugverschleiß:** +10%
   - Bei fortschreitendem Verschleiß sinkt vc

### Statistische Behandlung

**Kombinierte Standardabweichung (quadratische Addition):**
```
σ_gesamt = √(10² + 15² + 5² + 10²) = √(100 + 225 + 25 + 100) = √450 ≈ 21.2%
```

**95%-Konfidenzintervall (1.96σ):**
```
KI = 204.31 ± (1.96 × 0.212 × 204.31)
KI = 204.31 ± 84.8
```

### **ERGEBNIS MIT KONFIDENZINTERVALL**

```
Bearbeitungszeit = 204 min (95%-KI: 120-289 min)
```

**Konservative Schätzung (obere Grenze):** **290 Minuten** (≈ 4.8 Stunden)  
**Optimistische Schätzung (untere Grenze):** **120 Minuten** (≈ 2.0 Stunden)  
**Wahrscheinlichster Wert:** **204 Minuten** (≈ 3.4 Stunden)

---

## PHYSIKALISCHE PLAUSIBILITÄTSPRÜFUNG

### Spezifisches Zeitvolumen
```
Bauteilvolumen ≈ 2095 × 500 × 190 / 10⁹ = 0.199 m³ = 199 Liter

Bearbeitungszeit pro Liter:
t_spez = 204 min / 199 L ≈ 1.03 min/L
```

**Physikalische Einordnung:** Für ein großes Gussteil mit mittlerer Komplexität ist dies plausibel. Vergleichbar mit einer Materialabtragsrate von ~10-15 cm³/min über alle Operationen gemittelt.

### Energiebetrachtung (optional)
```
Spezifische Zerspanenergie GJS-700: kc ≈ 2000 N/mm²
Abtragsvolumen ≈ 5000 cm³ (geschätzt)

E = kc × V = 2000 × 5000 × 10³ = 10¹⁰ N·mm = 10 MJ

Bei durchschnittlich 5 kW Spindelleistung:
t_energetisch = 10 MJ / 5 kW = 2000 s ≈ 33 min (reine Zerspanzeit)
```

Dies bestätigt, dass die Hauptzeit von 117 min realistisch ist (Faktor 3.5 durch Eilgänge, nicht-produktive Schnittanteile).

---

## SCHLUSSFOLGERUNG

**Kalkulierte Gesamtbearbeitungszeit: 204 Minuten (3.4 Stunden)**

**95%-Konfidenzintervall: 120-289 Minuten**

Die Berechnung basiert vollständig auf physikalischen Grundprinzipien:
- Materialabtragsmechanik
- Kinematik der Werkzeugbewegung
- Werkstoffmechanische Eigenschaften von GJS-700

**Kritische Annahmen:**
1. Konturlänge und Anzahl Bohrungen sind geschätzt
2. Werkzeugverschleiß vernachlässigt
3. Maschinendynamik idealisiert
4. Keine Komplikationen (Werkzeugbruch, Nacharbeit)

**Empfehlung für Angebotskalkulation:** Nutze den konservativen Wert von **290 Minuten** (obere KI-Grenze) für risikoadjustierte Preiskalkulation.
