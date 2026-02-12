# FERTIGUNGSVERFASSUNG
## Constitutional AI für CNC-Planung nach REFA

**Version:** 1.0  
**Letzte Aktualisierung:** 2026-02-10  
**Zweck:** Automatisches Self-Check System für Kalkulationsplausibilität

---

## 🎯 Konzept

Wie Constitutional AI dem LLM Regeln gibt und es sich selbst prüfen lässt, gibt diese Verfassung dem CNC Planner REFA-basierte Fertigungsregeln. Jede Kalkulation durchläuft automatisch diese Checks vor Ausgabe.

**Prinzip:** Prüfen → Warnen → Confidence Score → Entscheidung

---

## 1. Plausibilitäts-Checks

**Diese Checks laufen automatisch nach jeder Kalkulation:**

### 1.1 Schnittgeschwindigkeit (vc)

| Material | Minimum vc | Maximum vc | Einheit | Status bei Abweichung |
|----------|------------|------------|---------|----------------------|
| S355 (Baustahl) | 80 | 120 | m/min | ⚠️ WARNUNG |
| GJS-700 (Guss) | 60 | 90 | m/min | ⚠️ WARNUNG |
| AlMg (Aluminium) | 200 | 400 | m/min | ⚠️ WARNUNG |
| 1.4301 (V2A) | 50 | 80 | m/min | ⚠️ WARNUNG |
| C45 (Vergütungsstahl) | 100 | 150 | m/min | ⚠️ WARNUNG |
| 42CrMo4 (gehärtet) | 40 | 70 | m/min | ⚠️ WARNUNG |

**Check-Logik:**
```
IF vc < min_vc OR vc > max_vc:
    WARNUNG: "Schnittgeschwindigkeit außerhalb REFA-Bereich"
    Confidence -= 15%
```

### 1.2 Vorschub pro Zahn (fz)

| Werkzeugtyp | fz_min | fz_max | Einheit | Anwendung |
|-------------|--------|--------|---------|-----------|
| Schruppen Ø>20mm | 0.15 | 0.30 | mm/Zahn | Grobbearbeitung |
| Schlichten Ø>20mm | 0.05 | 0.15 | mm/Zahn | Feinbearbeitung |
| Bohren Ø8-20mm | 0.10 | 0.25 | mm/Zahn | Vollbohren |
| Gewindebohren | 0.05 | 0.12 | mm/Zahn | Gewinde |

**Check-Logik:**
```
IF fz < fz_min OR fz > fz_max:
    WARNUNG: "Vorschub pro Zahn unplausibel"
    Confidence -= 10%
```

### 1.3 Zeitaufwand pro Zerspanvolumen

**REFA-Richtwerte:**

| Bearbeitungstyp | min (min/cm³) | max (min/cm³) | Bemerkung |
|-----------------|---------------|---------------|-----------|
| Schruppen (Fräsen) | 0.5 | 1.5 | Grobe Zerspanung |
| Schlichten (Fräsen) | 1.0 | 2.5 | Feinbearbeitung |
| Bohren | 0.3 | 1.0 | Standardbohrungen |
| Reiben | 0.8 | 2.0 | Toleranzarbeit |

**Berechnung:**
```
Zeitaufwand_pro_cm³ = Bearbeitungszeit_netto / Zerspanvolumen_cm³

IF Zeitaufwand_pro_cm³ < min OR > max:
    WARNUNG: "Zerspanzeit pro cm³ außerhalb REFA-Korridor"
    Confidence -= 12%
```

### 1.4 Rüstzeit pro Aufspannung

**REFA-Standard:**
- **Minimum:** 30 Minuten
- **Maximum:** 60 Minuten
- **Median:** 45 Minuten

**Ausnahmen:**
- Einfache Teile (Blech, prismatisch, <3 Werkzeuge): 20-30 min
- Komplexe Teile (5-Achs, >10 Werkzeuge): 60-90 min

**Check-Logik:**
```
IF Rüstzeit < 20 OR Rüstzeit > 90:
    WARNUNG: "Rüstzeit außerhalb üblichem Bereich"
    Confidence -= 8%
    
IF Rüstzeit < 30 OR Rüstzeit > 60:
    HINWEIS: "Rüstzeit am Rand des Standardbereichs"
    Confidence -= 3%
```

### 1.5 Entgratzeit

**REFA-Richtwert:**
- **Standard:** 10-20% der Bearbeitungszeit
- **Minimum:** 5% (einfache Geometrie)
- **Maximum:** 30% (komplexe Konturen, viele Kanten)

**Check-Logik:**
```
Entgratzeit_Prozent = (Entgratzeit / Bearbeitungszeit_netto) * 100

IF Entgratzeit_Prozent < 5 OR > 30:
    WARNUNG: "Entgratzeit unplausibel"
    Confidence -= 10%
    
IF Entgratzeit_Prozent < 10 OR > 20:
    HINWEIS: "Entgratzeit am Rand des Normbereichs"
    Confidence -= 3%
```

---

## 2. Material-Constraints (REFA-basiert)

### 2.1 Material-Datenbank

| Material | Kurzbezeichnung | vc_min | vc_max | Zeitfaktor | Zerspankraftfaktor | Bemerkung |
|----------|----------------|--------|--------|------------|-------------------|-----------|
| S235JR | Baustahl | 90 | 130 | 1.0 | 1.0 | Referenzmaterial |
| S355J2 | Baustahl | 80 | 120 | 1.0 | 1.05 | Standard Konstruktionsstahl |
| C45 | Vergütungsstahl | 100 | 150 | 1.0 | 1.1 | Wellen, Bolzen |
| 42CrMo4 | Vergütungsstahl | 40 | 70 | 1.5 | 1.4 | Gehärtet, hohe Festigkeit |
| GJS-700 | Sphäroguss | 60 | 90 | 1.3 | 1.2 | Spröde, kurze Späne |
| GJL-250 | Grauguss | 80 | 120 | 0.9 | 0.9 | Leicht zerspanbar |
| AlMg3 | Aluminium | 200 | 400 | 0.6 | 0.4 | Weich, hohe vc |
| AlMg4.5Mn | Aluminium | 180 | 380 | 0.65 | 0.45 | Zäher als AlMg3 |
| 1.4301 | Edelstahl (V2A) | 50 | 80 | 1.4 | 1.5 | Zäh, kaltverfestigend |
| 1.4571 | Edelstahl (V4A) | 40 | 70 | 1.5 | 1.6 | Noch zäher |
| CuZn39Pb3 | Messing | 150 | 250 | 0.7 | 0.6 | Gut zerspanbar |

### 2.2 Zeitfaktor-Anwendung

**Formel:**
```
Zeit_korrigiert = Zeit_basis × Material_Zeitfaktor
```

**Beispiel:**
- Bearbeitungszeit für S355 (Faktor 1.0): 45 min
- Gleiches Teil in 1.4301 (Faktor 1.4): 45 × 1.4 = **63 min**

**Check-Logik:**
```
IF Material_Zeitfaktor NOT IN Database:
    FEHLER: "Material nicht in Datenbank"
    Confidence = 0%
    → Manuelle Eingabe erforderlich
    
IF Zeitfaktor_angewendet != Zeitfaktor_Soll:
    WARNUNG: "Falscher Material-Zeitfaktor"
    Confidence -= 20%
```

---

## 3. Toleranz-Checks

### 3.1 ISO-Toleranzen und erforderliche Verfahren

| ISO-Toleranz | Toleranzbereich (Ø100mm) | Erforderliches Verfahren | Ra_max | Warnung wenn... |
|--------------|--------------------------|-------------------------|--------|-----------------|
| IT6 | ±0.022mm | Schleifen, Feinbohren (Diamant) | 0.8 μm | Ohne Schleifen geplant |
| IT7 | ±0.035mm | Schleifen oder Feinbohren | 1.6 μm | Nur Standardbohren |
| IT8 | ±0.054mm | Reiben, Feinbohren | 3.2 μm | Nur Bohren ohne Reiben |
| IT9 | ±0.087mm | Reiben optional | 6.3 μm | — |
| IT10 | ±0.14mm | Standardbohren ausreichend | 12.5 μm | — |
| IT11+ | ±0.22mm+ | Bohren, Fräsen | 25 μm | — |

### 3.2 Oberflächengüte (Ra) und Verfahren

| Ra-Wert | Verfahren | Bemerkung |
|---------|-----------|-----------|
| Ra ≤ 0.8 μm | Schleifen, Läppen, Feindrehen | Sehr feine Oberfläche |
| Ra 0.8-1.6 μm | Schleifen, Feinbohren | Hochwertige Passflächen |
| Ra 1.6-3.2 μm | Feinbohren, Reiben, Feindrehen | Standard-Passflächen |
| Ra 3.2-6.3 μm | Reiben, Standarddrehen | Normale Funktionsflächen |
| Ra 6.3-12.5 μm | Bohren, Fräsen, Drehen | Standardbearbeitung |
| Ra > 12.5 μm | Sägen, Schruppen | Rohbearbeitung |

### 3.3 Check-Logik Toleranzen

```python
# Beispiel-Implementierung

def check_tolerance_feasibility(tolerance_class, planned_process, surface_finish_ra):
    warnings = []
    
    # IT7 Check
    if tolerance_class <= 7:
        if "schleifen" not in planned_process and "feinbohren" not in planned_process:
            warnings.append("IT7 oder feiner erfordert Schleifen oder Feinbohren")
            confidence_penalty = 20
    
    # IT8-9 Check
    if tolerance_class in [8, 9]:
        if "reiben" not in planned_process and surface_finish_ra < 6.3:
            warnings.append("IT8-9 mit Ra<6.3 erfordert üblicherweise Reiben")
            confidence_penalty = 12
    
    # Ra vs Verfahren Check
    if surface_finish_ra <= 1.6 and "schleifen" not in planned_process:
        warnings.append(f"Ra {surface_finish_ra} μm üblicherweise nur mit Schleifen erreichbar")
        confidence_penalty = 15
    
    return warnings, confidence_penalty
```

---

## 4. Self-Check Prompts (LLM-Integration)

### 4.1 Automatische Prüf-Prompts

Nach jeder Kalkulation führt das System folgende Self-Checks durch:

#### **Check 1: REFA-Zeit-Plausibilität**
```
Prompt: "Prüfe: Liegt die berechnete Bearbeitungszeit im REFA-Korridor?
- Material: {material}
- Zerspanvolumen: {volumen_cm3} cm³
- Bearbeitungszeit: {zeit_min} min
- Zeitaufwand pro cm³: {zeit_pro_cm3} min/cm³
- REFA-Bereich: {refa_min} - {refa_max} min/cm³

Bewertung: [PASS / WARNUNG / FEHLER]
Begründung: [...]"
```

#### **Check 2: Toleranz-Verfahrens-Match**
```
Prompt: "Prüfe: Sind alle Toleranzen mit den gewählten Verfahren erreichbar?
- Toleranzklassen: {liste_toleranzen}
- Geplante Verfahren: {liste_verfahren}
- Oberflächengüten: {liste_ra_werte}

Für jede kritische Toleranz:
  IT-Klasse: {it}
  Verfahren: {verfahren}
  Erreichbar: [JA / NEIN / UNKLAR]
  
Gesamtbewertung: [PASS / WARNUNG / FEHLER]"
```

#### **Check 3: Material-Faktor korrekt**
```
Prompt: "Prüfe: Ist der Werkstoff-Faktor korrekt angewendet?
- Material: {material_name}
- Soll-Faktor (REFA): {faktor_soll}
- Angewendeter Faktor: {faktor_ist}
- Basis-Zeit: {zeit_basis} min
- Korrigierte Zeit: {zeit_korrigiert} min

Berechnung korrekt: [JA / NEIN]
Abweichung: {abweichung_prozent}%"
```

#### **Check 4: Schnittparameter plausibel**
```
Prompt: "Prüfe: Liegen alle Schnittparameter im zulässigen Bereich?

Für jeden Arbeitsschritt:
  Operation: {operation_name}
  Material: {material}
  vc ist: {vc_ist} m/min (Soll: {vc_min}-{vc_max})
  fz ist: {fz_ist} mm/Zahn (Soll: {fz_min}-{fz_max})
  Status: [OK / WARNUNG / KRITISCH]

Gesamtbewertung: [PASS / WARNUNG]"
```

#### **Check 5: Zeitzuschläge vollständig**
```
Prompt: "Prüfe: Sind alle REFA-Zeitzuschläge berücksichtigt?
- Rüstzeit: {ruestzeit} min (Erwartung: 30-60 min) → [OK/WARNUNG]
- Entgratzeit: {entgratzeit} min ({entgrat_prozent}% der Bearbeitung) → [OK/WARNUNG]
- Prüfzeit: {pruefzeit} min → [Vorhanden: JA/NEIN]
- Weitere Zuschläge: {weitere}

Bewertung: [VOLLSTÄNDIG / LÜCKEN ERKANNT]"
```

### 4.2 LLM-Response-Format

Das LLM antwortet strukturiert:

```json
{
  "check_results": [
    {
      "check_name": "REFA Zeit-Plausibilität",
      "status": "PASS|WARNUNG|FEHLER",
      "confidence_impact": 0,
      "message": "Beschreibung",
      "details": {}
    },
    ...
  ],
  "overall_status": "PASS|WARNUNG|FEHLER",
  "confidence_score": 85,
  "recommendation": "Freigabe|Review empfohlen|Manuelle Prüfung erforderlich"
}
```

---

## 5. Confidence Score Berechnung

### 5.1 Scoring-System

**Basis-Confidence:** 100%

**Penalty-Tabelle:**

| Fehlertyp | Penalty | Trigger |
|-----------|---------|---------|
| ❌ **FEHLER** (kritisch) | -30% | Material nicht in DB, Toleranz nicht erreichbar |
| ⚠️ **WARNUNG** (wichtig) | -15% | vc außerhalb Bereich, fz implausibel |
| ⚠️ **WARNUNG** (mittel) | -10% | Zeit/cm³ außerhalb, Entgratzeit kritisch |
| ℹ️ **HINWEIS** (gering) | -3% | Wert am Rand des Normbereichs |

### 5.2 Confidence-Kategorien

```
90-100%: ✅ Sehr hohe Konfidenz
  → Automatische Freigabe möglich
  → Alle Checks bestanden
  
70-89%: ⚠️ Mittlere Konfidenz
  → Werker-Review empfohlen
  → 1-2 Warnungen vorhanden
  
50-69%: ⚠️ Niedrige Konfidenz
  → Manuelle Prüfung erforderlich
  → 3-4 Warnungen oder 1 Fehler
  
<50%: ❌ Kritisch
  → Blockierung der Kalkulation
  → Schwerwiegende Fehler, mehrere kritische Warnungen
```

### 5.3 Berechnungsbeispiel

**Szenario:** Frästeile aus S355, IT8 Toleranz, Standardverfahren

```python
confidence = 100

# Check 1: vc = 85 m/min (Soll: 80-120) → OK
confidence -= 0  # ✅ PASS

# Check 2: fz = 0.18 mm (Soll: 0.05-0.3) → OK  
confidence -= 0  # ✅ PASS

# Check 3: Zeit/cm³ = 1.8 min/cm³ (Soll: 0.5-2.5) → OK
confidence -= 0  # ✅ PASS

# Check 4: Rüstzeit = 35 min (Soll: 30-60) → OK
confidence -= 0  # ✅ PASS

# Check 5: Entgrat = 8% (Soll: 10-20%) → HINWEIS
confidence -= 3  # ℹ️ Niedrig aber akzeptabel

# Check 6: IT8 mit Reiben → OK
confidence -= 0  # ✅ PASS

# Final Score
confidence = 97%  # ✅ Sehr hohe Konfidenz → Freigabe
```

### 5.4 Entscheidungsmatrix

| Confidence | Aktion | Routing | Zeitverzögerung |
|------------|--------|---------|-----------------|
| 90-100% | Automatische Freigabe | Direkt zu Angebot | 0 min |
| 80-89% | Review-Flag setzen | Werker checkt vor Freigabe | ~10 min |
| 70-79% | Manuelle Prüfung | Planer muss einzeln durchgehen | ~20 min |
| 50-69% | Detailprüfung erforderlich | Senior Planer | ~45 min |
| <50% | Blockierung | Zurück zur Konstruktion | — |

---

## 6. Implementierung

### 6.1 Integration in CNC Planner

```python
# Pseudo-Code für Integration

class FertigungsVerfassung:
    def __init__(self):
        self.load_material_database()
        self.load_tolerance_rules()
        
    def validate_calculation(self, calculation_data):
        confidence = 100
        warnings = []
        errors = []
        
        # 1. Material Check
        material_result = self.check_material_constraints(calculation_data)
        confidence -= material_result.penalty
        warnings.extend(material_result.warnings)
        
        # 2. Schnittparameter Check
        cutting_result = self.check_cutting_parameters(calculation_data)
        confidence -= cutting_result.penalty
        warnings.extend(cutting_result.warnings)
        
        # 3. Zeit-Plausibilität Check
        time_result = self.check_time_plausibility(calculation_data)
        confidence -= time_result.penalty
        warnings.extend(time_result.warnings)
        
        # 4. Toleranz Check
        tolerance_result = self.check_tolerance_feasibility(calculation_data)
        confidence -= tolerance_result.penalty
        warnings.extend(tolerance_result.warnings)
        errors.extend(tolerance_result.errors)
        
        # 5. Self-Check Prompts
        llm_check_result = self.run_llm_self_checks(calculation_data)
        confidence -= llm_check_result.penalty
        
        return {
            'confidence': max(0, confidence),
            'warnings': warnings,
            'errors': errors,
            'recommendation': self.get_recommendation(confidence),
            'details': {
                'material': material_result,
                'cutting': cutting_result,
                'time': time_result,
                'tolerance': tolerance_result,
                'llm': llm_check_result
            }
        }
    
    def get_recommendation(self, confidence):
        if confidence >= 90:
            return "FREIGABE"
        elif confidence >= 70:
            return "REVIEW_EMPFOHLEN"
        elif confidence >= 50:
            return "MANUELLE_PRUEFUNG"
        else:
            return "BLOCKIERUNG"
```

### 6.2 UI-Integration

**Anzeige für Planer:**

```
╔══════════════════════════════════════════════════════════╗
║  KALKULATION: Teil-Nr. 4711-A                            ║
║  Status: ⚠️ Review empfohlen                            ║
║  Confidence Score: 82%                                    ║
╠══════════════════════════════════════════════════════════╣
║  ✅ Material-Parameter korrekt                           ║
║  ✅ Schnittgeschwindigkeit im Bereich                    ║
║  ⚠️ Entgratzeit etwas niedrig (8%, Soll: 10-20%)       ║
║  ✅ Toleranzen erreichbar                                ║
║  ✅ Zeitaufwand plausibel                                ║
╠══════════════════════════════════════════════════════════╣
║  [Details anzeigen] [Freigeben] [Zurück zur Bearbeitung]║
╚══════════════════════════════════════════════════════════╝
```

---

## 7. Wartung & Weiterentwicklung

### 7.1 Regelmäßige Updates

**Quartalsweise:**
- Prüfung der Material-Datenbank (neue Werkstoffe?)
- Anpassung der REFA-Richtwerte basierend auf Ist-Daten
- Review der Confidence-Schwellwerte

**Kontinuierlich:**
- Feedback von Werkern sammeln
- False-Positive-Rate minimieren
- Neue Checks hinzufügen

### 7.2 Lernschleife

```
Kalkulation → Self-Check → Freigabe → Fertigung → Ist-Zeit messen
    ↑                                                          ↓
    └──────────────── Rückfluss in REFA-Datenbank ───────────┘
```

**Ziel:** System lernt aus echten Fertigungsdaten und verbessert Prognosen.

---

## 8. Anhang

### 8.1 REFA-Referenzen

- REFA-Verband (Hrsg.): Methodenlehre des Arbeitsstudiums Teil 2
- AWF-Empfehlung 5112: Richtwerte für die Kalkulation
- Tabellenbuch CNC-Technik (Europa-Verlag)

### 8.2 Änderungshistorie

| Version | Datum | Änderung | Autor |
|---------|-------|----------|-------|
| 1.0 | 2026-02-10 | Initiale Version | King (OpenClaw AI) |

---

## 9. Quick Reference Card

**Für Werker/Planer:**

```
🔍 SCHNELL-CHECK VOR FREIGABE:

□ Material in Datenbank?
□ vc im Bereich? (S355: 80-120 m/min)
□ fz plausibel? (0.05-0.3 mm/Zahn)
□ Zeit/cm³ im Korridor? (0.5-2 min/cm³)
□ Rüstzeit 30-60 min?
□ Entgrat 10-20% der Zeit?
□ Toleranzen erreichbar mit Verfahren?

➜ Alle ✅? → Confidence 90%+ → Freigabe!
➜ 1-2 ⚠️? → Review kurz checken
➜ 3+ ⚠️ oder ❌? → Detail-Prüfung
```

---

**Ende der Fertigungsverfassung**

*Diese Verfassung ist ein lebendes Dokument und wird basierend auf Praxiserfahrung kontinuierlich weiterentwickelt.*
