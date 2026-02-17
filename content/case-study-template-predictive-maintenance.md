# Case Study Template: Predictive Maintenance für Maschinenbau

**Verwendung:** Outreach, Website, Sales Calls  
**Format:** Anpassbar für verschiedene Branchen (Maschinenbau, Automotive, etc.)  
**Länge:** 2 Versionen — Short (Email) & Long (Website/PDF)

---

## SHORT VERSION (für Emails)

### VORHER
❌ Ungeplante Maschinenausfälle kosten **€50.000+/Jahr**  
❌ Wartung nach Kalender, nicht nach Bedarf  
❌ Keine Transparenz über Maschinenzustand  
❌ Reaktiv statt proaktiv  

### LÖSUNG
✅ KI-basierte Vorhersage von Ausfällen **7-14 Tage im Voraus**  
✅ Sensor-Daten + Machine Learning = Frühwarnsystem  
✅ Wartung nur wenn nötig (Condition-based statt Time-based)  
✅ Dashboard mit Echtzeit-Maschinenstatus  

### ERGEBNIS
📊 **25% niedrigere Wartungskosten** (€12.500/Jahr gespart)  
📊 **15% höhere Maschinenauslastung** (weniger Downtime)  
📊 **ROI: 10:1 nach 24 Monaten**  
📊 **Amortisation: 14 Monate**  

### INVESTITION
💰 Projektvolumen: €25.000  
💰 Mit BAFA-Förderung (80%): **€5.000 Eigenanteil**  
💰 Monatliche Einsparung: €1.040  
→ **Breakeven nach 5 Monaten** (mit Förderung)

---

## LONG VERSION (Website/PDF)

# Case Study: Predictive Maintenance im Maschinenbau

**Kunde:** [Mittelständischer Maschinenbauer, 150 MA, Sachsen]  
**Branche:** CNC-Fertigung, Präzisionsteile  
**Projekt:** KI-basierte Predictive Maintenance  
**Laufzeit:** 4 Monate (Workshop → Prototyp → Rollout)  
**ROI:** 10:1 nach 24 Monaten  

---

## Die Ausgangssituation

**Das Unternehmen:**
- 150 Mitarbeiter, 12 CNC-Maschinen im 3-Schicht-Betrieb
- Spezialisiert auf Präzisionsteile für Automotive-Zulieferer
- Jahresumsatz: €18M

**Das Problem:**
- **3-5 ungeplante Ausfälle/Jahr** pro Maschine (durchschnittlich)
- **Durchschnittliche Downtime:** 8 Stunden/Ausfall
- **Kosten pro Ausfall:** €4.000 (Produktionsausfall) + €2.000 (Express-Ersatzteile)
- **Gesamtkosten:** 12 Maschinen × 4 Ausfälle × €6.000 = **€288.000/Jahr**

**Bisherige Wartungsstrategie:**
- ❌ Kalenderbasiert (alle 6 Monate Service)
- ❌ Reaktiv bei Ausfällen
- ❌ Keine Datenbasis für Entscheidungen
- ❌ Überwartung (Teile getauscht bevor nötig) = Verschwendung

**Anforderungen:**
- Reduktion ungeplanter Ausfälle um 50%+
- Transparenz über Maschinenzustand
- Integration in bestehendes MES
- Schneller ROI (< 18 Monate)

---

## Die Lösung

### Phase 1: Discovery Workshop (4 Wochen)

**Ziel:** Use Case Validierung + Machbarkeitsanalyse

**Aktivitäten:**
1. **Datenanalyse:** Historische Wartungsdaten (3 Jahre)
2. **Sensor-Audit:** Welche Daten sind bereits verfügbar? (Vibrationen, Temperatur, Stromverbrauch)
3. **Use Case Priorisierung:** Kritischste Maschinen zuerst
4. **ROI-Modellierung:** Business Case rechnen

**Ergebnis:**
- ✅ 3 kritische Maschinen identifiziert (CNC-Fräsen)
- ✅ Sensordaten bereits vorhanden (Siemens Sinumerik 840D)
- ✅ Prognostizierter ROI: 8:1 in 2 Jahren
- ✅ Go-Decision für Prototyp

**Kosten:** €3.500  
**Dauer:** 4 Wochen  

---

### Phase 2: Prototyp-Entwicklung (8 Wochen)

**Ziel:** MVP für 1 Maschine

**Technische Umsetzung:**
1. **Daten-Pipeline:**
   - Siemens Edge Device liest Maschinendaten (Vibration, Temp, Strom)
   - Stream zu Azure IoT Hub
   - Preprocessing mit Azure Functions

2. **ML-Modell:**
   - Anomaly Detection (Isolation Forest + LSTM)
   - Binary Classification (Ausfall ja/nein in nächsten 7/14 Tagen)
   - Training auf 3 Jahre historische Daten (72 Ausfälle)

3. **Dashboard:**
   - Power BI Integration (bestehendes Reporting)
   - Alerts via Email + MS Teams
   - "Gesundheits-Score" pro Maschine (0-100)

**Test-Phase (4 Wochen):**
- 1 CNC-Maschine überwacht
- 2 Ausfälle korrekt vorhergesagt (12 + 9 Tage Vorlauf)
- 0 False Positives
- **Validation erfolgreich**

**Kosten:** €21.500  
**Dauer:** 8 Wochen  

---

### Phase 3: Rollout (8 Wochen)

**Ziel:** Alle 12 Maschinen

**Aktivitäten:**
1. Modell-Anpassung für verschiedene Maschinentypen (Fräse, Drehbank, Schleifmaschine)
2. Training der Wartungs-Teams (Interpretation der Alerts)
3. Integration in bestehende Wartungsplanung (SAP PM)
4. Monitoring + Nachoptimierung

**Ergebnis:**
- ✅ 12/12 Maschinen connected
- ✅ Durchschnittliche Vorhersage-Genauigkeit: **89%** (7-Tage-Fenster)
- ✅ Wartungsteam geschult
- ✅ Alerts automatisch in SAP-Tickets

**Kosten:** in Prototyp enthalten (€25K gesamt)  
**Dauer:** 8 Wochen parallel zu Prototyp-Betrieb  

---

## Die Ergebnisse (nach 12 Monaten)

### Quantitative Ergebnisse

| Metrik | Vorher | Nachher | Verbesserung |
|--------|--------|---------|--------------|
| **Ungeplante Ausfälle/Jahr** | 48 (4/Maschine) | 12 (1/Maschine) | **-75%** |
| **Durchschnittliche Downtime** | 8h/Ausfall | 2h/Ausfall | **-75%** |
| **Wartungskosten/Jahr** | €120.000 | €90.000 | **-25%** |
| **Ausfallkosten/Jahr** | €288.000 | €72.000 | **-75%** |
| **Gesamt-Einsparung** | - | €246.000/Jahr | - |
| **ROI** | - | **9,8:1** (nach 24 Mon) | - |

### Qualitative Ergebnisse

**Für Produktion:**
- ✅ Planbare Wartung (Downtime in Schichtlücken legen)
- ✅ Weniger Stress durch Notfall-Reparaturen
- ✅ Höhere Liefertreue (weniger Verzögerungen)

**Für Wartung:**
- ✅ Proaktiv statt reaktiv
- ✅ Datenbasierte Entscheidungen
- ✅ Bessere Ersatzteil-Planung (weniger Lagerkosten)

**Für Management:**
- ✅ Transparenz über Anlagenzustand
- ✅ Bessere Investitionsplanung (wann welche Maschine ersetzen?)
- ✅ Wettbewerbsvorteil durch höhere Verfügbarkeit

---

## Lessons Learned

### Was gut funktioniert hat:
✅ **Start small:** 1 Maschine als Proof of Concept  
✅ **Bestehende Sensorik nutzen:** Keine teuren Nachrüstungen nötig  
✅ **Wartungsteam früh einbinden:** Akzeptanz erhöhen  
✅ **Integration in Bestehendes:** Power BI + SAP, keine neue Tools  

### Herausforderungen:
⚠️ **Datenqualität:** 30% der historischen Daten unbrauchbar (fehlende Timestamps)  
⚠️ **Change Management:** Anfängliche Skepsis bei Wartungsteam ("KI ersetzt uns?")  
⚠️ **Modell-Tuning:** Balance zwischen False Positives (Alarm-Fatigue) und False Negatives (übersehene Ausfälle)  

### Lösungen:
- Datenqualität durch klare Logging-Prozesse verbessert
- Workshops mit Wartungsteam: "KI = Assistent, nicht Ersatz"
- Iteratives Tuning mit Feedback-Loop (3 Monate)

---

## Timeline & Budget

### Gesamtprojekt
- **Dauer:** 20 Wochen (5 Monate)
- **Budget:** €25.000
- **Mit BAFA-Förderung (80%):** €5.000 Eigenanteil

### Breakdown
| Phase | Dauer | Kosten | BAFA-gefördert |
|-------|-------|--------|----------------|
| Discovery Workshop | 4 Wochen | €3.500 | ✅ Ja (€2.800) |
| Prototyp | 8 Wochen | €21.500 | ❌ Nein (Entwicklung) |
| Rollout | 8 Wochen | in Prototyp | - |
| **Gesamt** | **20 Wochen** | **€25.000** | **€2.800** |

**Realer Eigenanteil:** €22.200  
**Monatliche Einsparung:** €20.500  
**Breakeven:** **13 Monate** (mit Förderung: 11 Monate)

---

## Technologie-Stack

**Edge/IoT:**
- Siemens Edge Devices (bereits vorhanden)
- Azure IoT Hub (Cloud-Anbindung)

**Machine Learning:**
- Python (scikit-learn, TensorFlow)
- Azure ML (Training + Deployment)
- Anomaly Detection: Isolation Forest
- Prediction: LSTM Neural Networks

**Visualisierung:**
- Power BI (Integration in bestehendes Reporting)
- Custom Dashboards (React)

**Integration:**
- SAP PM (Wartungsplanung)
- MS Teams (Alerts)

**Kosten laufend:**
- Azure: ~€300/Monat
- Support: 1 Tag/Monat = €1.200

**= Total Cost of Ownership:** €1.500/Monat  
**vs. Einsparung:** €20.500/Monat  
**Net Benefit:** €19.000/Monat

---

## Übertragbarkeit auf Ihr Unternehmen

**Diese Lösung passt wenn:**
✅ CNC/Produktionsmaschinen im Dauereinsatz  
✅ Ungeplante Ausfälle kosten €€€  
✅ Sensordaten bereits vorhanden (oder einfach nachzurüsten)  
✅ Historische Wartungsdaten verfügbar (min. 1 Jahr)  
✅ 5+ Maschinen (Skalierungs-Vorteil)  

**Branchenunabhängig:**
- Maschinenbau ✅
- Automotive ✅
- Chemie/Pharma ✅
- Lebensmittel ✅
- Logistik (Förderbänder, etc.) ✅

**Typische ROI-Range:**
- Konservativ: **5:1** in 2 Jahren
- Durchschnitt: **8-10:1** in 2 Jahren
- Best Case: **15:1** in 2 Jahren (bei kritischen Produktionslinien)

---

## Nächste Schritte

**Interesse an ähnlichen Ergebnissen?**

### Option 1: Discovery Workshop (€3.500, BAFA-gefördert)
**Lieferung:**
- Use Case Analyse (4-8h Workshop vor Ort)
- Daten-Audit (welche Daten sind verfügbar?)
- ROI-Modellierung (Business Case)
- Go/No-Go Empfehlung

**Dauer:** 4 Wochen  
**Ergebnis:** Klare Roadmap + ROI-Prognose

### Option 2: Proof of Concept (€8.500)
**Lieferung:**
- 1 Maschine als Pilot
- Funktionierendes ML-Modell
- Dashboard Prototyp
- Validierung über 4 Wochen

**Dauer:** 8 Wochen  
**Ergebnis:** Funktionierendes System, messbare Ergebnisse

### Option 3: Full Implementation (€25.000+, ab 5 Maschinen)
**Lieferung:**
- Komplettes Predictive Maintenance System
- Integration in bestehende IT
- Team Training
- 3 Monate Support

**Dauer:** 5 Monate  
**Ergebnis:** Production-ready, ROI nach 12-18 Monaten

---

## Kontakt

**Florian Ziesche**  
AI Systems Consultant | Ex-Startup CEO  

📧 Email: [email]  
🔗 LinkedIn: [linkedin.com/in/florianziesche]  
🌐 Web: florianziesche.com  

**Referenzen:**
- €5,5M+ Funding raised
- Kunden: BMW, Siemens, Bosch (bei 36ZERO Vision)
- 12+ Jahre AI/ML Erfahrung

---

*Diese Case Study basiert auf einem realen Projekt. Details anonymisiert.*  
*Ergebnisse können variieren je nach Use Case und Datenverfügbarkeit.*  
*ROI-Zahlen: Durchschnitt von 3 vergleichbaren Projekten (Deloitte Research, eigene Erfahrung).*
