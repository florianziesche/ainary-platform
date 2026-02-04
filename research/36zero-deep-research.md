# 36ZERO Vision — Deep Strategic Research Report

*February 4, 2026 | Prepared for Heiko Huber, CEO*

---

## Executive Summary

36ZERO Vision hat die technologische Grundlage für etwas viel Größeres als visuelle Qualitätsinspektion. Die Kombination aus dateneffizienter KI (5-20 Bilder), bestehenden Enterprise-Partnerschaften (Bosch, SAP, Siemens) und gelabelten Industriedaten ist eine seltene Ausgangsposition.

**Die revolutionäre Idee:** 36ZERO wird nicht "besser inspizieren." 36ZERO wird das **Betriebssystem für Fertigungsqualität** — von Erkennung über Diagnose bis zur autonomen Korrektur. Inspection ist nur die Datenschicht. Der Wert liegt darüber.

---

## 1. Agentic Quality — Die nächste Stufe

### Was ist Agentic AI in der Fertigung?

Agentic AI geht über Detection hinaus: Autonome Agenten erkennen Probleme, diagnostizieren Ursachen und **handeln selbstständig** — ohne menschliche Intervention in der Schleife.

**Der konkrete Ablauf:**
1. **Detect:** Kamera erkennt Riss an Bremsscheibe (36ZERO heute)
2. **Diagnose:** Agent korreliert mit Prozessparametern — Spindeltemperatur war 12°C über Schwellwert seit 14:32
3. **Prescribe:** Agent empfiehlt Kalibrierung der Spindel + Werkzeugwechsel
4. **Act:** Agent sendet Korrekturbefehl an SPS/MES, pausiert Produktion wenn Schwellwert kritisch

**State of the Art (2025/26):**
- Closed-Loop Quality Control existiert bereits im Spritzguss: AI erkennt Prozessdrift, identifiziert Ursachen und **passt Maschinenparameter automatisch an** (Druck, Temperatur, Einspritzgeschwindigkeit, Kühlzeit) — Quelle: tedesolutions.pl
- Ein führender Automotive-Zulieferer erreichte mit autonomer Prozessanpassung: **23% weniger Defekte**, €89K vermiedene katastrophale Ausfälle in der Validierungsphase — Quelle: MDPI Applied Sciences
- Agentic AI in Smart Factories: "Lernt aus Mustern, rekalibriert wenn nötig, arbeitet mit minimalem menschlichem Input" — Industrial Equipment News

**Gap-Analyse für 36ZERO:**
- 36ZERO ist auf Stufe 1 (Detect). Stufe 2 (Diagnose) erfordert **ERP/MES-Integration** — Partnerschaft mit SAP besteht bereits. Stufe 3-4 erfordern **SPS-Anbindung** — Partnerschaft mit Bosch Rexroth (ctrlX) besteht bereits.
- Die technische Infrastruktur ist da. Was fehlt: Produktentwicklung der Korrelations-Engine und ein mutiger Produktvisions-Shift.

**Revolutionäres Potenzial:** Der Markt für "Inspection" ist $30B. Der Markt für "Autonomous Quality Management" (Detect + Diagnose + Prescribe + Act) ist ein Vielfaches — weil er Inspection, Process Control, Predictive Maintenance und Compliance in einem vereint.

---

## 2. ERP-Integration als Wertmultiplikator

### Warum ERP der Schlüssel zum Sales-Cycle-Problem ist

**Das Problem heute:** 36ZERO verkauft an den Qualitätsleiter. Der hat begrenztes Budget und muss IT, Produktion und Einkauf überzeugen. → 12 Monate Cycle.

**Mit ERP-Integration:** 36ZERO liefert Daten die den CFO, CPO und COO betreffen. Budget kommt aus 4 Töpfen statt einem. Und der Business Case ist offensichtlich.

### Konkrete Use Cases

**Supplier Quality Scoring:**
- Inspektionsdaten automatisch mit Lieferanten-ID (SAP MM) verknüpfen
- Dashboard: "Lieferant A: 0.3% Defektrate / Lieferant B: 2.8% / Branchenschnitt: 1.2%"
- SAP QM unterstützt bereits Supplier Scorecards und Trend Reports (Quelle: sotatek.com)
- **Wert:** Einkaufsentscheidungen datenbasiert treffen → CPO wird zum Champion

**Batch-Traceability:**
- Defekt erkannt → automatisch Chargen-Nr., Maschine, Schicht, Rohmaterial-Los zuordnen
- SAP S/4HANA verbindet Inspektionspläne, Testergebnisse und Non-Conformance Reports direkt mit Produktionsbatches (Quelle: highbartechnocrat.com)
- Bei Rückruf: Sofort wissen welche Chargen betroffen sind → Millionen gespart

**Automatische 8D-Reports:**
- AI generiert standardisierten 8D-Report aus Inspektionsdaten + ERP-Kontext
- Defektbild + Ursachenhypothese + betroffene Chargen + Sofortmaßnahme
- Spart dem Qualitätsmanager 5-10 Stunden pro Vorfall

**Automatische Sperrmeldungen:**
- Qualitätsschwellwert überschritten → automatische Sperrung im SAP → kein fehlerhaftes Teil verlässt das Werk
- Real-time statt Tage Verzögerung

### Sales-Cycle-Effekt

Wenn 36ZERO SAP-integriert liefert:
- **Budget:** Nicht mehr nur Quality, sondern auch IT, Procurement, Operations
- **Champion:** Nicht mehr nur Qualitätsleiter, sondern auch CFO (Scrap-Kosten), CPO (Supplier-Daten), COO (OEE)
- **Procurement:** SAP-Partner → vereinfachte Beschaffung → "ist schon im SAP-Ökosystem" = schnellere Freigabe
- Menlo Ventures: 27% des Enterprise-AI-Spends kommt jetzt über PLG/Marketplace — 4x vs. traditionelle Software

---

## 3. Manufacturing Knowledge Base (RAG für Qualität)

### Das Konzept

Ein RAG-System (Retrieval-Augmented Generation) für Fertigungsqualität:

**Flow:** Defekt erkannt → System durchsucht Wissensdatenbank → "Dieser Risstyp tritt typischerweise auf bei: Spindeltemperatur >180°C, Werkzeugverschleiß >80%, Materialcharge mit hohem Kohlenstoffgehalt → Empfohlene Maßnahmen: 1. Kalibrierung, 2. Werkzeugwechsel, 3. Materialprüfung"

### Wissensquellen

| Standard | Branche | Inhalte |
|----------|---------|---------|
| **IATF 16949** | Automotive | Qualitätsmanagement, FMEA, PPAP, 8D |
| **VDA 6.3/6.5** | Automotive (DE) | Prozess- und Produktaudits |
| **IPC-A-610** | Elektronik | Akzeptanzkriterien elektronische Baugruppen |
| **GMP (FDA/EU)** | Pharma | Partikelinspektion, Dokumentation |
| **ISO 9001/14001** | Übergreifend | QM-Systeme, Umweltmanagement |
| **DIN EN ISO 5817** | Schweißtechnik | Schweißnahtbewertung |

### Netzwerkeffekt — Der wahre Moat

1. Kunde A hat Riss-Problem → System schlägt Lösung vor aus anonymisierten Daten von Kunde B-Z
2. Je mehr Kunden → bessere Ursache-Wirkungs-Datenbank → bessere Vorschläge
3. Kunden tragen anonymisiert bei → bekommen Zugang zum gesamten Netzwerkwissen
4. **Switching Cost = unmöglich** — welcher Konkurrent hat dieses kollektive Wissen?

**Präzedenzfall:** Stack Overflow für Entwickler. Jeder trägt bei, alle profitieren. Aber für Fertigungsqualität.

---

## 4. Foundation Models für Manufacturing

### State of the Art

- **Arxiv Feb 2025:** "A Survey on Foundation-Model-Based Industrial Defect Detection" — Foundation Models werden aktiv für industrielle Defekterkennung erforscht. Ansätze: Vision Transformers, CLIP-basierte Anomalieerkennung, Segment Anything Model (SAM) für industrielle Segmentierung.
- **NVIDIA Jan 2026:** "Optimizing Semiconductor Defect Classification with Generative AI and Vision Foundation Models" — NVIDIA arbeitet aktiv an Foundation Models für Halbleiter-Inspektion.
- **Trend:** Allgemeine Vision Models (CLIP, SAM, DINOv2) werden auf industrielle Domänen fine-tuned.

### 36ZERO's Vorteil

36ZERO hat etwas, das fast niemand hat: **gelabelte industrielle Defektdaten von Tier-1 Herstellern** (Siemens, Bosch, LEONI). Diese Daten sind extrem selten und wertvoll.

**Strategie:**
1. **Phase 1:** Pre-trained Models pro Branche (Automotive Surface, Electronics PCB, Pharma Particles)
2. **Phase 2:** Cross-Industry Foundation Model trainiert auf aggregierten, anonymisierten Kundendaten
3. **Phase 3:** "Manufacturing GPT" — Foundation Model das auf Bild eingibt und Defekttyp, Ursache und Lösung ausgibt

**Das ist der Moment wo 36ZERO von einem Inspection Tool zu einer AI Company wird.** Nicht "wir nutzen AI" sondern "wir BAUEN das AI für Manufacturing Quality."

---

## 5. Neue Märkte & Anwendungen

### Tier 1: Höchste Priorität (Fit + Marktgröße + Regulierung)

**Pharma & Medtech**
- Visuelle Inspektion ist **gesetzlich vorgeschrieben** (FDA, EU GMP)
- Partikelinspektion in Injektionslösungen, Vial-Inspektion, Blister-Prüfung
- FDA entwickelt aktiv AI-Kompetenz für Inspektionen (FDA Technology Modernization Action Plan)
- **Willingness to pay:** 3-5x Manufacturing (Recall-Kosten = $100M+)
- **Sales Cycle:** Paradoxerweise kürzer — Compliance ist nicht verhandelbar, Budget ist vorhanden
- **Fit:** 36ZERO's Dateneffizienz (5 Bilder) ist perfekt — in Pharma bekommt man keine 10.000 Defektbilder

**Semiconductor / Wafer**
- Marktgröße: **$8.15B (2025) → $14.4B (2031)**, CAGR 9.5%
- Dominiert von KLA ($11B Revenue) und ASML — aber Software-Layer ist offen
- 36ZERO hat dies selbst als Ziel genannt
- Sub-Nanometer Defekterkennung bei <5nm Nodes — extrem hohe Anforderungen, extrem hohe Zahlungsbereitschaft
- **Risiko:** Technologisch sehr anspruchsvoll, andere Physik als Surface Inspection

### Tier 2: Starkes Potenzial

**Energie (Solar + Wind)**
- Drone Wind Turbine Blade Inspection: **$211M (2025) → $1.47B (2035)**, CAGR 21.4%
- Inspection Drone Market insgesamt: **$34.4B by 2031**
- Kombination: 36ZERO-AI auf Drohne = automatische Blade/Panel-Inspektion
- Regulierung treibt: Periodische Inspektion vorgeschrieben
- **Fit:** Hardware-agnostisch (iPhone bis NVIDIA Jetson) passt perfekt zu Drohnen-Kameras

**Construction & Infrastruktur**
- Brückeninspektion per Drohne + AI: Massiver Wachstumsmarkt
- Deutschland: 40.000+ Brücken, viele sanierungsbedürftig
- EU Infrastructure Regulation treibt verpflichtende Inspektionen
- **Fit:** Ähnliche Defekttypen (Risse, Korrosion, Abplatzungen)

### Tier 3: Perspektivisch

**Recycling & Circular Economy**
- EU Circular Economy Regulation → Materialsortierung wird Pflicht
- AI-basierte Materialerkennung und Sortierung
- Wachsender Markt, aber noch früh

**Agriculture & Food**
- Qualitätssortierung, Kontaminationserkennung
- Hohe Volumina, niedrige Margen — passt zu PLG/Volume-Pricing

---

## 6. Multimodal Quality Assessment

### Vision allein reicht nicht

Viele Defekte sind mit dem Auge nicht sichtbar:
- **Haarrisse:** Akustische Emission erkennt interne Risse bevor sie an die Oberfläche treten
- **Materialhärte:** Vibrationsmuster zeigen Strukturveränderungen
- **Überhitzung:** Thermografie zeigt Hotspots die zu späteren Defekten führen

### Sensor Fusion Architecture

**Research (2024/25):** "Comprehensive Framework for Multimodal Sensor Fusion in Intelligent Manufacturing" — Hybrid-Fusion mit Attention-Mechanismen, die automatisch die wichtigsten Sensordaten gewichten.

**Für 36ZERO konkret:**
1. Visuell (Kamera) → Oberflächendefekte ✅ (heute)
2. + Thermal (IR-Kamera) → Prozesstemperatur-Anomalien
3. + Akustik (Mikrofon) → Interne Risse, Materialfehler
4. + Vibration (Beschleunigungssensor) → Maschinenzustand, Werkzeugverschleiß

**Ergebnis:** Nicht "was sehen wir?" sondern "was passiert in diesem Teil?" — holistische Qualitätsbewertung.

**Produktidee:** "36ZERO Multimodal" als Premium-Modul. Hardware-Partner liefern Sensorik (Bosch Rexroth!), 36ZERO liefert die Fusion-AI.

---

## 7. Digital Twin Integration

### Inspection Data als Digital Twin Input

**Siemens, PTC, Dassault** bauen Digital Twins für Fertigung. Was fehlt: Real-time Qualitätsdaten.

**36ZERO liefert:**
- Live-Defektraten pro Linie/Maschine/Schicht
- Defekt-Heatmaps auf dem Teil → zeigt wo im Prozess das Problem liegt
- Historische Trendanalyse: "Defektrate steigt seit 3 Tagen → Prognose: 15% Anstieg in 72h"

**Simulation:**
"Was passiert mit der Defektrate wenn wir Temperatur um 5°C senken?"
→ Digital Twin simuliert → AI empfiehlt optimale Parameter → Closed Loop

**Partnerstrategie:** Integration in Siemens Xcelerator, PTC ThingWorx, Dassault 3DEXPERIENCE. 36ZERO als Quality-Data-Layer im Digital Twin Stack.

---

## 8. Competitive Landscape

| Wettbewerber | Stärke | Schwäche | 36ZERO-Vorteil |
|-------------|--------|---------|---------------|
| **Landing AI** (Andrew Ng) | Brand, $57M Funding, Data-Centric AI | Breit aufgestellt, kein Branchen-Fokus | 36ZERO: Branchenspezifisch, weniger Daten nötig |
| **Cognex** ($950M Revenue) | Hardware+Software, Marktführer | Legacy-Architektur, kein Cloud-native, teuer | 36ZERO: Cloud-first, No-Code, 10x günstiger |
| **Keyence** ($7B Revenue) | Multi-Sensor, riesiger Vertrieb | Closed Ecosystem, kein SaaS-Modell | 36ZERO: Offen, Hardware-agnostisch |
| **Instrumental** | Elektronik-Fokus, gut in PCB | Nur Elektronik, kein Automotive/Pharma | 36ZERO: Multi-Industry |
| **Elementary AI** | Schnelle Deployment, modern | Keine Tier-1 Kunden genannt | 36ZERO: Siemens, Bosch, LEONI = Credibility |

### White Space — Was KEINER bietet:

1. **Closed-Loop Quality** (Detect → Diagnose → Prescribe → Act) — alle bleiben bei Detection
2. **Cross-Industry Knowledge Network** — jeder arbeitet in Silos
3. **Foundation Model für Industrial Defects** — niemand aggregiert genug Daten
4. **ERP-native Quality Intelligence** — alle sind Insellösungen neben dem ERP

**→ DAS ist 36ZERO's strategischer Raum.**

---

## Die neue Company Vision

### Option A: "Manufacturing Quality OS"
> "36ZERO Vision ist das Betriebssystem für Fertigungsqualität. Wir erkennen nicht nur Fehler — wir verstehen warum sie passieren und verhindern dass sie wieder passieren. Autonome Qualitätskontrolle, getrieben von der weltweit größten Manufacturing Quality Knowledge Base."

### Option B: "Zero-Defect Manufacturing"
> "36ZERO macht Null-Fehler-Fertigung Realität. Unsere AI-Plattform verbindet visuelle Inspektion mit Prozessintelligenz, Lieferantendaten und kollektivem Branchenwissen — und wird mit jedem Kunden intelligenter."

### Option C (mein Favorit): "The Quality Intelligence Company"
> "Wir bauen die Intelligenzschicht für Fertigungsqualität. Inspektion war erst der Anfang. Heute liefern wir Herstellern weltweit nicht nur was falsch ist — sondern warum, und was sie dagegen tun können. Autonome Qualität, kollektives Wissen, null Defekte."

---

## Revolutionary Product Roadmap

### Phase 1: Foundation (Q1-Q2 2026)
- ERP-Integration (SAP QM Connector) → Batch-Traceability, Supplier Scoring
- PLG: 1-Click Install in Bosch ctrlX World
- Branchenspezifische Pre-Trained Models (Automotive, Electronics)
- Fachkräftemangel-Messaging im Marketing
- **KPI:** Sales Cycle von 12 auf 6 Monate. 2 neue Kunden über Marketplace.

### Phase 2: Intelligence (Q3-Q4 2026)
- Process Parameter Correlation Engine (Inspect → Diagnose)
- Manufacturing Knowledge Base v1 (IATF 16949, VDA, ISO-Standards)
- Auto-generated 8D Reports + Compliance Docs
- Pharma-Modul (GMP-compliant Particle Inspection)
- **KPI:** "Warum ist es kaputt?" als Live-Feature. 1. Pharma-Kunde. NRR >120%.

### Phase 3: Autonomy (2027)
- Closed-Loop Quality: AI empfiehlt + führt Korrekturen aus (SPS-Anbindung via ctrlX)
- Customer Knowledge Network: Anonymisierte Cross-Industry Intelligence
- Multimodal-Modul: Thermal + Acoustic Fusion
- Foundation Model v1 (trainiert auf aggregierten Kundendaten)
- **KPI:** 1. Autonome Korrekturaktion. Foundation Model outperformt Einzelkunden-Modelle. ARR €5M+.

### Phase 4: Platform (2028)
- Manufacturing Quality Marketplace (Pre-trained Models, Third-Party Integrations)
- Digital Twin Integration (Siemens, PTC)
- Global Expansion (US, APAC)
- "Manufacturing GPT" — Generative Quality Intelligence
- **KPI:** Platform Revenue >30% des Gesamtumsatzes. $50M+ Bewertung.

---

## Top 3 Moves (Impact × Feasibility)

### 1. 🏆 ERP-Integration + PLG via Marketplace
**Impact:** Hoch (Sales Cycle halbieren, neue Budget-Töpfe)
**Feasibility:** Hoch (SAP + Bosch Partnerschaften existieren)
**Timeline:** 3-6 Monate
**Warum #1:** Löst das akuteste Problem (Sales Cycle) mit existierenden Assets.

### 2. 🥈 Process Correlation Engine ("Warum ist es kaputt?")
**Impact:** Sehr hoch (3-5x Kundenwert, einzigartiges Feature)
**Feasibility:** Mittel (braucht MES/SPS-Daten, 6-12 Monate Entwicklung)
**Timeline:** 6-12 Monate
**Warum #2:** Differenziert 36ZERO fundamental von JEDEM Wettbewerber. Keiner macht Closed Loop.

### 3. 🥉 Pharma/Regulated Industries Expansion
**Impact:** Hoch (3-5x höhere Zahlungsbereitschaft, kürzerer Sales Cycle)
**Feasibility:** Mittel-Hoch (Tech passt, Regulierung muss gelernt werden)
**Timeline:** 6-9 Monate für ersten Kunden
**Warum #3:** Neue Revenue-Quelle mit weniger Sales-Friction, weil Compliance = must-have.

---

## TL;DR

36ZERO sitzt auf einem **Datenschatz** (gelabelte Industriedefektdaten von Tier-1 Herstellern) und hat **einzigartige Partnerschaften** (Bosch, SAP, Siemens). Das reicht für viel mehr als "bessere Inspektion."

**Die Revolution:** Von "Was ist kaputt?" → "Warum ist es kaputt?" → "Wie verhindern wir es automatisch?" → "Was weiß die gesamte Branche darüber?"

**Jede Stufe verdreifacht den Kundenwert und den adressierbaren Markt.**

Der Wettbewerb bleibt bei Detection stecken. 36ZERO baut die Intelligenzschicht darüber.

---

*Quellen: EU-Startups, Industrial Equipment News, MDPI Applied Sciences, Menlo Ventures State of AI 2025, Arxiv, NVIDIA Developer Blog, SAP Community, tedesolutions.pl, Mordor Intelligence, GlobeNewsWire, FactMR*
