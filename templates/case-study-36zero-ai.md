# Case Study: Computer Vision AI für Quality Control (36ZERO Vision)

**Kunde:** BMW, Siemens, Bosch (Automotive & Manufacturing)  
**Zeitraum:** 2018-2022  
**Rolle:** CEO/Co-Founder & Product Lead  
**Funding:** €5.5M+ raised (VC-backed)

---

## Challenge

**Problem:**
- Manuelle Qualitätskontrolle in der Produktion: langsam, fehleranfällig, teuer
- Fehlererkennung in komplexen Fertigungsprozessen (Automotive, Electronics)
- Traceability-Anforderungen (Tier-1 Automotive Suppliers)
- 24/7 Produktion → begrenzte menschliche Kapazität

**Industrie-Context:**
- Automotive Tier-1 Suppliers: <0.1% Fehlertoleranz
- Kosten pro übersehener Defekt: €5.000-€50.000 (Rückruf-Risiko)
- Fachkräftemangel: Qualitätsprüfer schwer zu finden

---

## Solution: Cloud-Native Computer Vision AI

**36ZERO Vision Plattform:**
1. **Vision AI Models:** Defect Detection, OCR, Classification
2. **Edge-Cloud Architecture:** Real-time Processing (< 100ms)
3. **Continuous Learning:** Active Learning Loop, Model Retraining
4. **Integration:** REST APIs, OPC-UA, existing MES/ERP Systems

**KI-Stack:**
- TensorFlow / PyTorch Custom Models
- Transfer Learning von Pre-trained ImageNet Models
- Active Learning für kontinuierliche Verbesserung
- Cloud-Deployment (AWS, Azure) + Edge Inference

---

## Implementation

**Phase 1: Discovery & PoC (4-6 Wochen)**
- Use Case Definition (Top-3 Defect Types)
- Data Collection (500-1000 labeled images)
- PoC Model Training
- Business Case Validation
- **Output:** Working Prototype, ROI Calculation

**Phase 2: Pilot (3-6 Monate)**
- Production Integration (1 Line)
- Model Optimization (Precision/Recall > 95%)
- Operator Training
- KPI Tracking
- **Output:** Production-ready System, Performance Report

**Phase 3: Scale (6-12 Monate)**
- Rollout über mehrere Produktionslinien
- Continuous Model Improvement
- Change Management
- **Output:** Enterprise Deployment

---

## Results

**BMW Group:**
- **Defect Detection Rate:** 98.7% (vorher: 92% manuell)
- **Inspection Time:** -65% (von 45s auf 15s pro Teil)
- **False Positive Rate:** <2% (vorher: 8%)
- **ROI:** 18 Monate

**Siemens:**
- **Traceability:** 100% (OCR + Data Logging)
- **Quality Data:** Real-time Analytics Dashboard
- **Cost Savings:** €450K/Jahr (reduzierte Nacharbeit)

**Bosch:**
- **Multi-Defect Detection:** 12 verschiedene Defekttypen
- **Deployment:** 8 Produktionslinien
- **Training Time:** -80% (von 4 Wochen auf 3 Tage)

---

## Key Learnings

### Technical
1. **Data Quality > Model Complexity:** 1.000 perfekt gelabelte Bilder > 10.000 schlechte
2. **Edge + Cloud Hybrid:** Best of both worlds (Latency + Flexibility)
3. **Continuous Learning:** Models müssen mit Produkt-Varianten mitwachsen
4. **Integration ist kritisch:** 70% der Arbeit ist System-Integration, nicht Model-Training

### Business
1. **PoC ≠ Production:** Proof of Concept in 4 Wochen, Production-ready dauert 6-12 Monate
2. **Change Management:** Operator Buy-In ist entscheidend (kein "Ersatz", sondern "Augmentation")
3. **Start Small, Scale Fast:** 1 Produktionslinie → validieren → schnell skalieren
4. **ROI-Fokus:** Business Case MUSS klar sein (typisch: 12-24 Monate Payback)

### Organizational
1. **Cross-Functional Teams:** IT + OT + Quality + Production müssen zusammenarbeiten
2. **Data Governance:** Klare Regeln für Data Ownership, Labeling, Model Updates
3. **Vendor Lock-In vermeiden:** Standards nutzen (ONNX, REST APIs, Docker)

---

## Transferable Insights für Mittelstand

**"Was heißt das für Ihr Unternehmen?"**

1. **KI ist kein Hexenwerk:** Mit 4-6 Wochen Discovery + PoC können Sie validieren, ob es funktioniert
2. **Förderung nutzen:** BAFA 50-80% → Ihr PoC kostet €3.000-€6.000 statt €15.000-€30.000
3. **Start mit Quick Win:** Wählen Sie EINEN Use Case mit klarem ROI (nicht "KI-Strategie für alles")
4. **Build vs. Buy vs. Partner:** Mittelstand sollte selten selbst KI-Modelle bauen — Partner nutzen
5. **Daten sind der Schlüssel:** Haben Sie 500-1.000 Beispiele? Dann ist KI machbar.

---

## Anwendbar auf:

- **Maschinenbau:** Predictive Maintenance, Quality Control
- **Automotive:** Vision AI, Process Optimization
- **Medizintechnik:** Diagnostic Support, Regulatory AI
- **Chemie/Pharma:** Prozessoptimierung, Batch-Analyse
- **Logistik:** Route Optimization, Warehouse AI

---

**Kontakt:**  
Florian Ziesche  
AI Consultant | Ex-CEO 36ZERO Vision  
florian@ainaryventures.com  
+49 XXX (TBD)
