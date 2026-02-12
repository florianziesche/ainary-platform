# Risikoanalyse — Lagerungstraverse 10028104.79 (KBA)
## CNC Planer Pro | Interne Analyse | Stand: 11.02.2026

---

## 1. Kalkulationsübersicht

| Parameter | Wert |
|-----------|------|
| Bauteil | Lagerungstraverse KBA |
| Zeichnung | 10028104.79 |
| Werkstoff | GJS-700-2 (Sphäroguss) |
| Maße | 2095 × 500 × 190 mm |
| Stückzahl | 4 |
| Materialkosten | €1.200 (Beistellung KBA) |
| Bearbeitungszeit | 497 min / Stk (8,3 h) |
| Rüstzeit | 164 min (4 Aufspannungen) |
| **Stückpreis (netto)** | **€2.383,58** |
| **Auftragswert (4 Stk, netto)** | **€9.534,33** |

---

## 2. Wo entstehen die größten Abweichungen?

### 🔴 HOHES RISIKO (Abweichung >20%)

#### R1: Bearbeitungszeiten (±30%)
**Kalkuliert:** 497 min/Stk | **Realistischer Korridor:** 350–650 min
- **Ursache:** KI-Schätzung basiert auf REFA-Richtwerten und VDI 3321, NICHT auf gemessenen Ist-Zeiten bei MBS
- **Größte Unsicherheit:** AG50 Taschen fräsen (46 min) — abhängig von Restaufmaß des Gussteils, das stark variieren kann
- **Kosteneffekt:** ±30% auf Fertigungskosten = **±€176/Stk**
- **Mitigation:** Andreas soll Ist-Zeiten der ersten 2 Teile erfassen → Nachkalkulation

#### R2: GJS-700 Zerspanbarkeit (±20%)
**Kalkuliert mit:** timeFactor 1.18 | **Realistisch:** 1.0–1.5
- **Ursache:** GJS-700 ist gut zerspanbar für Gusseisen, ABER: Gusshaut, Lunker, harte Zonen können Werkzeuge zerstören und Zeiten verdoppeln
- **Worst Case:** Lunker in Bohrungsbereich → Ausschuss
- **Kosteneffekt:** ±€100/Stk durch Werkzeugverschleiß, ±€200/Stk bei Hartflecken
- **Mitigation:** Eingangsprüfung (AG10) kritisch — Ultraschallprüfung bei teurem Material empfehlen

#### R3: Aufspannung Großteil (±25%)
**Kalkuliert:** 4 × 35-50 min = 164 min | **Realistisch:** 120–250 min
- **Ursache:** 2095mm Bauteil auf 3-Achs-BAZ — Spannsituation ist komplex. Durchbiegung beim Planfräsen möglich
- **Worst Case:** Bauteil verzieht sich nach Gussspannungen → Nacharbeit
- **Kosteneffekt:** ±€50/Stk
- **Mitigation:** Spannungsarmglühen vor Bearbeitung klären (Kosten: ~€150/Teil)

### 🟡 MITTLERES RISIKO (Abweichung 10-20%)

#### R4: Materialkosten-Schwankung
**Kalkuliert:** €1.200 fest (Beistellung) | **Risiko:** Aufmaß-Nacharbeit
- **Ursache:** Gussteil kann Übermaße haben → mehr Abtrag → mehr Zeit
- **Kosteneffekt:** ±€80/Stk
- **Mitigation:** Rohteil-Maße bei Wareneingang prüfen, Aufmaß dokumentieren

#### R5: Stundensätze nicht kalibriert
**Kalkuliert:** CNC €70/h, Sägen €45/h, Entgraten €31/h
- **Ursache:** Branchenübliche Richtwerte für Sachsen — MBS hat eigene Kalkulation
- **Frage an Andreas:** "Was ist euer Maschinenstundensatz für die Hermle?"
- **Kosteneffekt:** ±15% auf Gesamtpreis = **±€350/Stk**
- **Mitigation:** Andreas' echte Stundensätze eintragen → sofortige Neuberechnung

#### R6: Zuschlagssätze geschätzt
**Kalkuliert:** MGK 5%, AV 12%, VwGK 10%, VtGK 5%, Gewinn 8%
- **Ursache:** Branchenübliche Werte, nicht MBS-spezifisch
- **Kosteneffekt:** ±€200/Stk
- **Mitigation:** Andreas nach betrieblichen Zuschlagssätzen fragen

### 🟢 NIEDRIGES RISIKO (Abweichung <10%)

#### R7: Werkzeugkosten
**Kalkuliert:** €24,47/Stk | **Realistisch:** €15–40/Stk
- Im Maschinenstundensatz teilweise enthalten
- Bei 4 Stück kaum Standzeit-Probleme

#### R8: Toleranzen H7
**Kalkuliert in AG30:** 44 min für 12 Bohrungen H7
- H7-Toleranzen bei GJS-700 sind Standard
- Reiben funktioniert zuverlässig bei korrekter Vorbereitung

---

## 3. Sensitivitätsanalyse

| Szenario | Stückpreis | Abweichung |
|----------|-----------|------------|
| **Optimistisch** (schneller, alles glatt) | €1.950 | -18% |
| **Berechnet** (REFA-Richtwerte) | **€2.384** | Basis |
| **Pessimistisch** (Gussprobleme, Rüstprobleme) | €3.100 | +30% |
| **Worst Case** (Ausschuss 1 Teil) | €3.500 | +47% |

### Haupttreiber der Abweichung:
```
Bearbeitungszeiten    ████████████████████ 45%
Stundensätze          ████████████        25%
Rüstzeiten            ████████            15%
Zuschläge             ██████              10%
Werkzeug/Material     ██                   5%
```

---

## 4. Empfohlene Mitigations für Praxistest

### SOFORT (vor Angebotserstellung)
1. ☐ **Stundensätze von Andreas erfragen** → in CNC Planer Pro eintragen
2. ☐ **Zuschlagssätze von Andreas erfragen** → MGK, VwGK, VtGK, Gewinn
3. ☐ **Rohteil-Zustand klären** → Aufmaße, Gusshaut, spannungsarmgeglüht?

### BEI FERTIGUNG (Ist-Daten erfassen)
4. ☐ **Ist-Zeiten AG für AG protokollieren** (Teil 1 + 2)
5. ☐ **Rüstzeiten pro Aufspannung messen**
6. ☐ **Werkzeugstandzeiten dokumentieren** (besonders bei GJS-700)
7. ☐ **Abweichungen > 15% sofort melden** → Kalkulation anpassen

### NACH FERTIGUNG (Nachkalkulation)
8. ☐ **Soll-Ist-Vergleich pro AG erstellen**
9. ☐ **Korrektur-Faktoren für GJS-700 ableiten**
10. ☐ **Korrekturfaktoren in CNC Planer Pro einspeisen** → nächste Kalkulation besser

---

## 5. Fazit

Die Kalkulation ist ein **fundierter Richtwert auf Basis von REFA/VDI-Daten**, nicht eine verbindliche Zusage. Der Praxistest mit Andreas dient genau dazu, die Schätzgenauigkeit zu validieren und zu verbessern.

**Erwartete Genauigkeit:** ±20-30% vor Kalibrierung → ±10-15% nach erstem Praxistest

**Kritischer Erfolgsfaktor:** Andreas' echte Stundensätze und Ist-Zeiten aus der Fertigung. Ohne diese Daten bleibt jede Kalkulation ein Richtwert.

---

*INTERN — Nicht für Kunden. Erstellt von CNC Planer Pro, verifiziert am 11.02.2026.*
