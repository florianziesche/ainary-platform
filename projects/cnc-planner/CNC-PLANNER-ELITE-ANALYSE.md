# CNC Planner Elite — Competitive Analysis & Roadmap

**Erstellt:** 2026-02-05 22:30  
**Ziel:** CNC Planner von Good → Elite  
**Definition Elite:** Top 3 Features der Competitors + Unique Differentiators

---

## EXECUTIVE SUMMARY

**Aktueller Stand:**
- CNC Planner v16: Solid foundation, 6-Tab Navigation, Zuschlagskalkulation, Feedback System
- Demo-ready, erste positive Resonanz (Onkel Demo)
- Pricing: Pro €149/mo

**Gap zu Elite:**
- ❌ Kein File Upload (nur Demo-Parts)
- ❌ Keine CAD-Analyse (nur manuelle Eingabe)
- ❌ Kein Arbeitsplan-Export
- ❌ Keine ERP-Integration
- ❌ Kein Team-Management

**Empfehlung:**
- **Phase 1 (MVP+):** File Upload + Basic CAD Analysis → Closes 80% gap
- **Phase 2 (Pro):** Arbeitsplan + PDF Export → Enterprise-ready
- **Phase 3 (Elite):** ERP Integration + Team Features → Marktführer-Niveau

**ROI-Rechnung:**
- Elite Features = €299/mo Pricing (statt €149)
- 10 Customers × €150 Mehrumsatz = +€1.500/mo = €18K/Jahr
- Development: ~4 Wochen (bei focused work)

---

## I. COMPETITOR ANALYSIS

### 1. **Spanflug MAKE** — Der Marktführer

**Company:** Spanflug (Berlin), SaaS, ISO 27001 certified  
**Pricing:** 5 parts/mo free, dann Subscription (Preis nicht public)  
**Target:** CNC Lohnfertiger (Drehen + Fräsen)

**Core Features:**
- ✅ CAD Model Upload (STEP, IGES, etc.)
- ✅ 2D Drawing Analysis
- ✅ Automatische Bauteilanalyse (AI-powered)
- ✅ Fertigungszeit + Kosten automatisch
- ✅ **Arbeitsplan-Export** (Operations list)
- ✅ **Quote PDF Generation** (ready-to-send)
- ✅ **Stock + Tool Management** (inkl. Beschaffung)
- ✅ **ERP Integration** (Export zu externen Systemen)
- ✅ **Customer Management** (CRM-lite)
- ✅ **Team-Management** (zentrale Settings für alle User)
- ✅ Part + Quote Archive
- ✅ <1 Min Calculation Time
- ✅ Cloud-based (AWS Germany)

**Unique Strengths:**
- Millionen Parts trainiert (algorithm)
- Stock direkt über Spanflug beschaffbar
- ISO 27001 certified = Enterprise-ready
- Real-time stock prices

**Weaknesses:**
- Preis nicht transparent (vermutlich €300+/mo)
- Keine Free Tier (nur 5 parts/mo)
- Komplexität (große Lernkurve für kleine Betriebe)

---

### 2. **Aspio nextOffer** — Der Effiziente

**Company:** Aspio (Freiburg)  
**Pricing:** Nicht public  
**Target:** CNC Frästeile

**Core Features:**
- ✅ CAD Upload (STEP)
- ✅ **3D Viewer** (interaktiv, Transparenz, Messwerkzeuge)
- ✅ **Feature-Einfärbung** (nach Farbcode für CAM-Abteilung)
- ✅ Materialberechnung (Rohmaß optimiert)
- ✅ E-Mail-Generator für Materialanfrage
- ✅ 2 Min Calculation
- ✅ **Keine Lernphase** (im Gegensatz zu AI)
- ✅ Export für externe Systeme
- ✅ STEP Export mit Einfärbungen

**Unique Strengths:**
- 60% Zeitersparnis claimed
- Feature-Einfärbung = direkter Nutzen für CAM
- Materialoptimierung (vermeidet falsches Material)
- Geringe Fachkenntnisse nötig

**Weaknesses:**
- Nur Fräsen (kein Drehen?)
- Keine Quote PDF Generation erwähnt
- Keine Team-Features erwähnt

---

### 3. **TICC (R+B)** — Der Klassische

**Company:** R+B Entwicklungs- und Vertriebs GmbH  
**Pricing:** Nicht public (vermutlich Lizenz-Modell)  
**Target:** Maschinenbau + Anlagenbau

**Core Features:**
- ✅ CAD-Daten Import
- ✅ Grafisch interaktive Kalkulation
- ✅ Zeit + Kostenkalkulation
- ✅ Angebotskalkulation
- ✅ Planzeitkalkulation
- ✅ Montage-Kalkulation
- ✅ Auch 2D (DXF) + Papierzeichnungen
- ✅ Stückzahlbezogene Preise + Staffelungen

**Unique Strengths:**
- Breiter einsetzbar (nicht nur CNC)
- 2D + Paper Drawings = flexibler
- Montage-Kalkulation

**Weaknesses:**
- Älter wirkende Software (nicht Cloud-native?)
- Keine AI/Automation erwähnt
- Vermutlich On-Premise (keine SaaS)

---

### 4. **goCAD** — Der Metallbau-Fokus

**Company:** goCAD  
**Target:** Metallbau, Blechbearbeitung

**Core Features:**
- ✅ CAD Upload
- ✅ Schnelle Quote Preparation
- ✅ Machining + Sheet Metal Components
- ✅ "Submit first quotation" = Speed-fokussiert

**Unique Strengths:**
- Blechbearbeitung (unser Focus: Fräsen/Drehen)

**Weaknesses:**
- Wenig Info verfügbar
- Scheint Nischen-Player

---

### 5. **Imnoo** — Der Automatisierungs-Champion

**Company:** Imnoo AG (Schweiz)  
**Pricing:** Nicht public  
**Target:** CNC Components

**Core Features:**
- ✅ 90% automatische Kalkulation
- ✅ 1.200 Stunden/Jahr gespart (Kundenclaim)
- ✅ App-basiert (mobile-friendly?)

**Unique Strengths:**
- 90% Automatisierung = höchster Claim
- Schweizer Engineering

**Weaknesses:**
- Wenig Details verfügbar
- Vermutlich teuer (Schweiz)

---

### 6. **PROfirst** — Der Blech-Spezialist

**Company:** PROfirst Group  
**Target:** Blechbearbeitung  
**Core Features:**
- ✅ CAD/CAM/Kalkulation in einer Software
- ✅ Von Angebot bis Programmierung

**Unique Strengths:**
- End-to-End Lösung
- CAM Integration

**Weaknesses:**
- Nur Blech (nicht unser Market)

---

## II. COMPETITOR FEATURE MATRIX

| Feature | Spanflug | Aspio | TICC | goCAD | Imnoo | **CNC Planner v16** |
|---------|----------|-------|------|-------|-------|---------------------|
| **File Upload** | ✅ CAD+2D | ✅ STEP | ✅ | ✅ | ✅ | ❌ Demo only |
| **3D Viewer** | ✅ | ✅ Interactive | ? | ? | ? | ❌ |
| **Auto Analysis** | ✅ AI | ✅ | ✅ | ✅ | ✅ | ❌ Manual input |
| **Fertigungszeit** | ✅ Auto | ✅ Auto | ✅ | ✅ | ✅ | ✅ Formula-based |
| **Materialkosten** | ✅ Real-time | ✅ Optimiert | ✅ | ✅ | ? | ✅ Manual |
| **Zuschläge** | ✅ | ? | ✅ | ? | ? | ✅ |
| **Quote PDF** | ✅ | ? | ✅ | ✅ | ? | ✅ (Angebot Tab) |
| **Arbeitsplan** | ✅ | ❌ | ✅ | ? | ? | ❌ |
| **NC-Code** | ? | ❌ | ❌ | ? | ? | ✅ (Basic) |
| **Feature-Einfärbung** | ? | ✅ | ? | ? | ? | ❌ |
| **Stock Management** | ✅ | ✅ | ? | ? | ? | ❌ |
| **ERP Integration** | ✅ | ✅ | ? | ? | ? | ❌ |
| **Team Management** | ✅ | ? | ? | ? | ? | ❌ |
| **Archive** | ✅ | ? | ? | ? | ? | ❌ |
| **Calculation Time** | <1 min | 2 min | ? | ? | ? | <10 sec |
| **Feedback System** | ? | ? | ? | ? | ? | ✅ Unique! |

**Legende:**
- ✅ = Feature vorhanden
- ❌ = Feature fehlt
- ? = Unklar aus Public Info

---

## III. PAIN POINTS DER ARBEITSVORBEREITER

**Research-Basis:** Web Search, Competitor-Docs, Schwab CNC Case Study

### 1. **Zeitaufwand bei Kalkulation**

**Problem:**
- 20-30 Minuten pro Teil (manuell)
- Bei Großprojekten: 500 Teile = Wochen
- Anfragen können nicht schnell beantwortet werden → Kunden gehen zu Konkurrenz

**Impact:**
- Verlust von Aufträgen
- Überlastung der AV-Abteilung
- Hohe Personalkosten

**Was Competitors lösen:**
- Spanflug: <1 Min
- Aspio: 2 Min (60% Zeitersparnis)
- Imnoo: 1.200h/Jahr gespart

**Was wir lösen:**
- v16: <10 Sekunden Berechnung ✅
- **Gap:** Dateneingabe ist noch manuell (10-15 Min) → File Upload fehlt

---

### 2. **Unsichere Kalkulationen ("Bauchgefühl")**

**Problem:**
- Erfahrungswerte = inkonsistent zwischen Mitarbeitern
- Unterschätzte Zeiten = Verluste
- Überschätzte Zeiten = Auftrag geht an Konkurrenz
- Keine Reproduzierbarkeit

**Impact:**
- Unrentable Aufträge
- Verlorene Aufträge
- Fehlendes Vertrauen in eigene Zahlen

**Was Competitors lösen:**
- Spanflug: "Präzise Kalkulationen auf Basis von Millionen Parts"
- Aspio: "Keine bösen Überraschungen in der Fertigung"
- TICC: "Höchste Planungssicherheit"

**Was wir lösen:**
- v16: Formel-basierte Berechnungen nach DIN/VDI ✅
- Transparenz: Alle Formeln sichtbar ✅
- **Gap:** Keine Verifikation durch historische Daten

---

### 3. **Falsches Material bestellt**

**Problem:**
- Rohmaß falsch berechnet → Material zu klein
- Verzögerungen in der Fertigung
- Zusätzliche Kosten

**Impact:**
- Lieferverzug
- Kundenzufriedenheit leidet
- Interne Konflikte (AV ↔ Einkauf)

**Was Competitors lösen:**
- Aspio: Optimierte Materialberechnung, E-Mail-Generator für Anfrage
- Spanflug: Stock Management inkl. Beschaffung

**Was wir lösen:**
- v16: Materialberechnung mit Verschnitt ✅
- **Gap:** Keine direkte Material-Anfrage, keine Rohmaß-Optimierung für verschiedene Formate

---

### 4. **Datensilos zwischen Abteilungen**

**Problem:**
- Konstruktion, AV, Fertigung arbeiten mit unterschiedlichen Daten
- Excel-Listen, Papier-Notizen, handgeschriebene Pläne
- Keine gemeinsame Sprache

**Impact:**
- Fehlerhafte Übergaben
- Doppelarbeit
- Verzögerungen

**Was Competitors lösen:**
- Spanflug: Zentrale Plattform, Team-Management
- Aspio: Feature-Einfärbung für CAM = direkte Übergabe
- TICC: CAD-Daten durchgängig nutzbar

**Was wir lösen:**
- v16: Zentrale Kalkulation ✅
- **Gap:** Keine CAM-Integration, keine Feature-Erkennung

---

### 5. **Langwierige Angebotserstellung**

**Problem:**
- Kalkulation → Excel → Word → PDF = viele Schritte
- Fehleranfällig (Copy-Paste Fehler)
- Kunde wartet

**Impact:**
- Langsame Response-Time
- Unprofessioneller Eindruck
- Kunde geht woanders hin

**Was Competitors lösen:**
- Spanflug: "Ready-to-send Quote PDF within seconds"
- goCAD: "Always submit the first quotation"

**Was wir lösen:**
- v16: Angebot-Tab mit PDF-Export ✅
- **Gap:** PDF-Design noch Basic, keine Firmendaten-Anpassung

---

### 6. **Fehlende Arbeitspläne**

**Problem:**
- Arbeitsplan muss manuell erstellt werden
- Werkzeuge, Aufspannungen, OPs müssen durchdacht werden
- Zeitaufwand

**Impact:**
- AV-Bottleneck
- Fertigung startet nicht schnell

**Was Competitors lösen:**
- Spanflug: Automatischer Arbeitsplan
- Aspio: Feature-Einfärbung = Vorbereitung für CAM

**Was wir lösen:**
- v16: OP-Details mit Werkzeugen + Strategien ✅
- **Gap:** Kein exportierbarer Arbeitsplan, nur UI-View

---

### 7. **Keine Transparenz über Maschinenauslastung**

**Problem:**
- "Ist die Maschine frei?"
- Keine Übersicht über laufende Aufträge
- Zusagen werden gemacht ohne Kapazitätsprüfung

**Impact:**
- Überbuchung
- Verzögerungen
- Stress

**Was Competitors lösen:**
- Größere Systeme: ERP-Integration → Kapazitätsplanung

**Was wir lösen:**
- v16: Nicht adressiert ❌
- **Gap:** Kapazitätsplanung out-of-scope (ERP-Thema)

---

## IV. GAP ANALYSIS: CNC Planner v16 vs. Elite

### **Was wir HABEN (v16):**

✅ **Solid Foundation:**
- Zuschlagskalkulation (MGK, AV, VwGK, VtGK, Gewinn)
- Fertigungszeit-Berechnung (REFA, VDI 3321)
- Material + Werkzeugkosten
- 6-Tab Navigation (Teil, Kalkulation, Angebot, NC-Code, Feedback, Settings)
- NC-Code-Generierung (Heidenhain, Siemens, Fanuc)
- Angebot PDF
- Feedback-System (Erfassen, Cross-Learnings, Historie)
- Design Standard (CSS classes, professional)
- <10 Sekunden Berechnung

✅ **Unique Differentiators:**
- Feedback System mit Cross-Learnings (KEIN Competitor hat das!)
- Transparenz (alle Formeln sichtbar)
- NC-Code Templates (Spanflug hat das NICHT explizit)

---

### **Was uns FEHLT für Elite:**

#### 🔴 **Kritisch (Must-Have):**

1. **File Upload (CAD/Drawing)**
   - Status: ❌ Nur Demo-Parts
   - Gap: User müssen alles manuell eingeben
   - Competitor: Spanflug ✅, Aspio ✅, TICC ✅, alle haben es
   - Impact: Dealbreaker für 80% der Kunden
   - Effort: Medium (FileReader API, STEP parser)

2. **Auto Part Analysis (CAD)**
   - Status: ❌ Vollständig manuell
   - Gap: Keine automatische Feature-Erkennung (Bohrungen, Taschen, etc.)
   - Competitor: Spanflug ✅ (AI), Aspio ✅
   - Impact: 15 Min manuelle Arbeit pro Teil
   - Effort: High (3D Geometry Analysis, ML optional)

3. **Arbeitsplan Export (PDF/Excel)**
   - Status: ❌ Nur UI-View
   - Gap: AV kann Arbeitsplan nicht drucken/weitergeben
   - Competitor: Spanflug ✅
   - Impact: Medium (AV muss noch manuell übertragen)
   - Effort: Low (Template + Export)

---

#### 🟡 **Wichtig (Should-Have):**

4. **3D Viewer**
   - Status: ❌ Keine Visualisierung
   - Gap: User muss CAD extern öffnen
   - Competitor: Aspio ✅ (interaktiv), Spanflug ?
   - Impact: UX deutlich schlechter
   - Effort: Medium (three.js, STEP viewer)

5. **Stock/Material Optimization**
   - Status: Partial (Materialberechnung ✅, aber nicht optimiert)
   - Gap: Kein Rohmaß-Vorschlag für verschiedene Formate (Platte, Stange, Rund)
   - Competitor: Aspio ✅ (optimiert), Spanflug ✅
   - Impact: Material-Einkauf suboptimal
   - Effort: Medium (Geometry optimization)

6. **Archive (Parts + Quotes)**
   - Status: ❌ Keine Speicherung (nur localStorage pro Session)
   - Gap: User kann alte Kalkulationen nicht wiederfinden
   - Competitor: Spanflug ✅
   - Impact: Wiederholungsaufträge = neue Kalkulation
   - Effort: Medium (Backend + DB)

7. **Customer Management**
   - Status: ❌ Keine CRM-Features
   - Gap: Firmendaten müssen bei jedem Angebot neu eingegeben werden
   - Competitor: Spanflug ✅
   - Impact: Zeitaufwand, unprofessionell
   - Effort: Low (Simple CRUD)

---

#### 🟢 **Nice-to-Have:**

8. **ERP Integration**
   - Status: ❌
   - Gap: Daten müssen manuell in ERP übertragen werden
   - Competitor: Spanflug ✅, Aspio ✅
   - Impact: Doppelarbeit
   - Effort: High (API, verschiedene ERP-Systeme)

9. **Team Management**
   - Status: ❌ Single-User
   - Gap: Mehrere Kalkulatoren können nicht zentral Settings teilen
   - Competitor: Spanflug ✅
   - Impact: Kleine Betriebe OK, größere brauchen das
   - Effort: Medium (Multi-User, Auth, Permissions)

10. **Feature-Einfärbung (für CAM)**
   - Status: ❌
   - Gap: CAM-Abteilung muss Features manuell identifizieren
   - Competitor: Aspio ✅ (Unique Strength)
   - Impact: Medium (nur wenn CAM vorhanden)
   - Effort: High (Feature Recognition + Color Coding)

11. **Real-Time Stock Prices**
   - Status: ❌ Manuelle Preise
   - Gap: Materialpreise veralten schnell
   - Competitor: Spanflug ✅
   - Impact: Kalkulationen werden ungenau
   - Effort: Medium (API zu Material-Lieferanten)

---

## V. REQUIREMENTS FÜR ELITE VERSION

### **Definition: Elite = Top 3 in der Kategorie**

**Kriterien:**
1. **Feature-Completeness:** 80%+ der Competitor-Features
2. **Speed:** <30 Sekunden from Upload → Quote PDF
3. **Accuracy:** ±10% (besser als ±15% aktuell)
4. **UX:** Professional, intuitive, keine Schulung nötig
5. **Differentiator:** Mind. 1 Feature das Competitors NICHT haben

---

### **Elite Feature Set (Priorisiert)**

#### **PHASE 1: MVP+ (4 Wochen)**
**Ziel:** Competitor-Parität bei Core Features

1. **File Upload (1 Woche)**
   - STEP, IGES, STL Upload
   - 2D Drawing Upload (PDF, DXF)
   - Drag & Drop Interface
   - File Validation
   - Preview (Image + Metadata)

2. **Basic CAD Analysis (2 Wochen)**
   - Bounding Box (L × B × H)
   - Volume (für Materialberechnung)
   - Feature Detection (Bohrungen, Taschen) — Rule-based, kein ML
   - Material auto-fill aus CAD metadata

3. **Arbeitsplan Export (3 Tage)**
   - PDF Export (Arbeitsplan mit OPs, Werkzeugen, Zeiten)
   - Excel Export (für ERP-Import)
   - Template customizable (Firmendaten, Logo)

4. **Archive (Basic) (2 Tage)**
   - localStorage → IndexedDB (client-side)
   - Part + Quote History
   - Search by Name/Datum
   - Re-load alte Kalkulationen

**Outcome:**
- 80% Feature-Gap zu Spanflug geschlossen
- €299/mo Pricing gerechtfertigt
- "File Upload + Auto Analysis" = Dealmaker für die meisten Kunden

---

#### **PHASE 2: Pro (6 Wochen)**
**Ziel:** Enterprise-ready + Unique Differentiator stärken

5. **3D Viewer (1 Woche)**
   - three.js Integration
   - STEP/STL Rendering
   - Rotate, Zoom, Pan
   - Measure Tool
   - Feature Highlighting (Bohrungen rot, Taschen blau, etc.)

6. **Advanced CAD Analysis (2 Wochen)**
   - ML-based Feature Recognition (oder Rule-Engine erweitern)
   - Toleranzen aus Drawing extrahieren
   - Oberflächenangaben (Ra) erkennen
   - Automatische OP-Vorschläge

7. **Material Optimization (1 Woche)**
   - Rohmaß-Optimierung für Platte/Stange/Rund
   - Material-Vorschlag mit Begründung
   - Verschnitt-Minimierung

8. **Customer Management (3 Tage)**
   - Kundendatenbank (Name, Adresse, Kontakt)
   - Zuordnung zu Quotes
   - Wiederkehrende Kunden = 1-Click Select

9. **Feedback System Upgrade (4 Tage)**
   - **Predictive Insights:** "Ähnliche Teile wurden 10% schneller gefertigt"
   - **Auto-Learning:** Feedback beeinflusst zukünftige Kalkulationen
   - **Benchmark:** Dein Betrieb vs. anonymisierte Industry-Daten

10. **Professional PDF Templates (3 Tage)**
   - Mehrere Template-Optionen (Modern, Classic, Technical)
   - Logo, Firmendaten, individuelle Fußzeilen
   - Multi-Language (DE, EN)

**Outcome:**
- Unique Differentiator: Feedback System = Learning Tool (nicht nur Kalkulation)
- Professional appearance = Enterprise-ready
- €399/mo Pricing für Pro Tier

---

#### **PHASE 3: Elite (8+ Wochen)**
**Ziel:** Marktführer-Features + Platform Play

11. **ERP Integration (3 Wochen)**
   - API für Export (JSON, XML, CSV)
   - Pre-built Connectors für Top 3 ERPs (SAP, Abas, Sage)
   - Webhook Support

12. **Team Management (2 Wochen)**
   - Multi-User Accounts
   - Role-Based Permissions (Admin, Calculator, Viewer)
   - Zentrale Settings (Stundensätze, Materialpreise, Zuschläge)
   - Activity Log (wer hat was kalkuliert)

13. **Cloud Backend (3 Wochen)**
   - User Authentication (JWT)
   - Database (PostgreSQL)
   - File Storage (S3 oder local)
   - API für Frontend

14. **Real-Time Stock Prices (1 Woche)**
   - API-Integration zu Material-Lieferanten
   - Auto-Update Materialpreise
   - Price History (Trend-Anzeige)

15. **Feature-Einfärbung für CAM (2 Wochen)**
   - Color-Code nach Kundenstandard
   - STEP Export mit Einfärbungen
   - CAM-Tool Integration (Fusion 360, Mastercam, etc.)

**Outcome:**
- Top 3 Feature-Set
- €499/mo Enterprise Tier
- Platform statt Tool (Ecosystem-Play)

---

## VI. COMPETITIVE POSITIONING

### **Wo wir JETZT stehen (v16):**

**Kategorie:** Basic Tool  
**Preis:** €149/mo  
**Target:** Einzelfertiger, kleine Betriebe (1-5 Mann)  
**USP:** Schnell, transparent, günstig

**Schwächen:**
- Manuelle Eingabe = Zeitaufwand
- Kein File Upload = Dealbreaker für viele
- Single-User = nicht skalierbar

**Wahrnehmung:**
- "Gutes Tool für den Start"
- "Besser als Excel, aber nicht so gut wie Spanflug"

---

### **Wo wir hinwollen (Elite):**

**Kategorie:** Professional Platform  
**Preis:** €149 Basic / €299 Pro / €499 Enterprise  
**Target:** CNC-Lohnfertiger (5-50 Mann), Arbeitsvorbereiter

**USP:**
1. **Feedback-Driven Learning:** Das einzige Tool das mit dir besser wird
2. **Transparency:** Alle Formeln sichtbar, keine Black Box
3. **Speed:** <30 Sekunden from Upload → Quote PDF

**Positionierung:**
- **vs. Spanflug:** "Gleiche Features, besseres Feedback-System, günstiger"
- **vs. Aspio:** "3D Viewer + Feature-Einfärbung + Learning-Komponente"
- **vs. TICC:** "Cloud-native, modern UI, schneller"

**Wahrnehmung (Ziel):**
- "Das Tool das sich an dich anpasst"
- "Spanflug-Qualität, Aspio-UX, eigener Lern-Algorithmus"

---

## VII. ROADMAP (12 Wochen zum Elite-Status)

### **Woche 1-4: PHASE 1 (MVP+)**

**Ziel:** Competitor-Parität Core Features

| Woche | Feature | Outcome |
|-------|---------|---------|
| 1 | File Upload (STEP, STL, PDF) | User können Dateien hochladen |
| 2-3 | Basic CAD Analysis | Automatische Erkennung: L×B×H, Volume, Bohrungen |
| 3 | Arbeitsplan Export (PDF/Excel) | AV kann Arbeitsplan drucken |
| 4 | Archive (IndexedDB) | User können alte Kalkulationen laden |

**Testing:** Demo mit 3 Kunden (Onkel + 2 neue)  
**Pricing Update:** €149 → €299 Pro (mit File Upload)

---

### **Woche 5-10: PHASE 2 (Pro)**

**Ziel:** Enterprise-ready + Unique Differentiator

| Woche | Feature | Outcome |
|-------|---------|---------|
| 5 | 3D Viewer (three.js) | Visualisierung ohne externes CAD |
| 6-7 | Advanced CAD Analysis | Toleranzen, Oberflächenangaben, OP-Vorschläge |
| 8 | Material Optimization | Rohmaß-Vorschlag für verschiedene Formate |
| 9 | Customer Management | Kundendatenbank + 1-Click Select |
| 10 | Feedback System Upgrade | Predictive Insights + Auto-Learning |

**Testing:** Pilot mit 5 Kunden (€299/mo)  
**Pricing Tier:** €299 Pro → €399 Pro+ (mit Learning)

---

### **Woche 11-18: PHASE 3 (Elite)**

**Ziel:** Marktführer-Features

| Woche | Feature | Outcome |
|-------|---------|---------|
| 11-13 | ERP Integration | API + Pre-built Connectors |
| 14-15 | Team Management | Multi-User, Permissions, Activity Log |
| 16-17 | Cloud Backend | Auth, DB, API |
| 18 | Real-Time Stock Prices | Auto-Update Materialpreise |

**Testing:** Enterprise Pilot (10+ User Betrieb)  
**Pricing Tier:** €499 Enterprise

---

## VIII. DEVELOPMENT PRIORITIES

### **Quick Wins (1-2 Wochen, hoher Impact):**

1. **File Upload** — Dealmaker für 80% der Kunden
2. **Arbeitsplan Export** — Einfach, hoher Nutzen
3. **Archive** — Low-effort, hoher Convenience

**Start HIER.** Diese 3 Features machen v16 → v17 (Elite-ready).

---

### **Strategic Bets (4-6 Wochen, Differentiator):**

4. **3D Viewer** — UX-Upgrade, "feels professional"
5. **Feedback System Upgrade** — Unique, kein Competitor hat das
6. **Advanced CAD Analysis** — Core-Tech, schwer zu kopieren

---

### **Long-Term (8+ Wochen, Platform Play):**

7. **ERP Integration** — Enterprise-Kunden
8. **Team Management** — Skalierbarkeit
9. **Cloud Backend** — Infrastructure

---

## IX. PRICING STRATEGY

### **Current (v16):**
- **Pro:** €149/mo (unlimited calculations)

### **Proposed (Elite):**

| Tier | Preis | Features | Target |
|------|-------|----------|--------|
| **Basic** | €149/mo | v16 Features + File Upload | Einzelfertiger, 1-5 Mann |
| **Pro** | €299/mo | + 3D Viewer, Archive, Arbeitsplan Export | CNC-Lohnfertiger, 5-20 Mann |
| **Pro+** | €399/mo | + Feedback Learning, Material Optimization | Qualitätsbetriebe |
| **Enterprise** | €499/mo | + ERP, Team Management, Stock Prices | 20+ Mann, ISO-zertifiziert |

### **Revenue Impact:**

**Scenario:** 20 Customers nach 6 Monaten

| Tier | Customers | MRR | ARR |
|------|-----------|-----|-----|
| Basic | 8 | €1.192 | €14.304 |
| Pro | 8 | €2.392 | €28.704 |
| Pro+ | 3 | €1.197 | €14.364 |
| Enterprise | 1 | €499 | €5.988 |
| **Total** | **20** | **€5.280** | **€63.360** |

**mit Elite Features:** +€2.000/mo vs. current pricing

---

## X. RISK ANALYSIS

### **Technical Risks:**

1. **CAD Parsing Complexity**
   - STEP files sind komplex
   - Mitigation: Start mit simple Geometry (Box, Cylinder), dann erweitern
   - Fallback: User kann Manual Override

2. **3D Viewer Performance**
   - Große STEP Files (100MB+) können Browser crashen
   - Mitigation: File-Size Limit (10MB), Decimation für Preview

3. **ML for Feature Recognition**
   - Training Data fehlt
   - Mitigation: Start mit Rule-Based, später ML wenn Daten vorhanden

---

### **Market Risks:**

4. **Spanflug Pricing Undercut**
   - Wenn Spanflug plötzlich €99/mo anbietet
   - Mitigation: Unique Differentiator (Feedback System), bessere UX

5. **Free Tier von Competitor**
   - Aspio könnte Free Tier launchen
   - Mitigation: Wir haben Free Tier schon (Demo), aber limitiert

---

### **Execution Risks:**

6. **Feature Creep**
   - Zu viele Features = lange Development, late Launch
   - Mitigation: Strikte Priorisierung, MVP+ first

7. **Customer Churn nach Phase 1**
   - Kunden zahlen €299 aber Features kommen nicht schnell genug
   - Mitigation: Klare Roadmap Communication, Beta-Pricing (€199 für Early Adopters)

---

## XI. SUCCESS METRICS

### **Phase 1 (MVP+) Success:**
- [ ] 5 Customers zahlen €299/mo (vs. €149 aktuell)
- [ ] File Upload funktioniert für 90%+ der CAD Files
- [ ] Arbeitsplan Export wird von 80%+ der User genutzt
- [ ] NPS > 8/10

### **Phase 2 (Pro) Success:**
- [ ] 15 Customers, davon 5× €399/mo (Pro+)
- [ ] Feedback System zeigt messbare Accuracy-Verbesserung (±10% statt ±15%)
- [ ] 3D Viewer wird von 90%+ der User als "sehr hilfreich" bewertet

### **Phase 3 (Elite) Success:**
- [ ] 30 Customers, davon 10× Pro+, 3× Enterprise
- [ ] MRR > €5.000
- [ ] ERP Integration bei 5+ Enterprise Kunden im Einsatz
- [ ] Top 3 Wahrnehmung (Review Sites, Forums)

---

## XII. NEXT ACTIONS

### **SOFORT (Diese Woche):**

1. **Entscheidung:** Phase 1 starten? (File Upload + CAD Analysis)
2. **Prototype:** File Upload UI (1 Tag) → Demo für Onkel
3. **Research:** STEP Parser Libraries (open-source options)

### **Woche 1:**

4. **Build:** File Upload (Drag & Drop, Validation, Preview)
5. **Build:** Basic CAD Analysis (Bounding Box, Volume)
6. **Test:** Mit 2-3 Demo-Files (von Onkel?)

### **Woche 2-3:**

7. **Build:** Feature Detection (Bohrungen)
8. **Build:** Arbeitsplan Export (PDF Template)
9. **Test:** Full Flow: Upload → Analyze → Calculate → Export

### **Woche 4:**

10. **Polish:** UX, Error Handling, Edge Cases
11. **Demo:** Mit Onkel + 2 neuen Leads
12. **Pricing:** Update auf €299/mo für Pro Tier

---

## XIII. FAZIT

**Status Quo:**
- v16 ist ein solides Tool
- ABER: Fehlt kritische Features für breite Adoption

**Recommended Path:**
- **Phase 1 (4 Wochen)** = MUST DO
  - File Upload + Basic CAD Analysis + Arbeitsplan Export
  - Schließt 80% Feature-Gap zu Spanflug
  - Pricing: €299/mo gerechtfertigt

- **Phase 2 (6 Wochen)** = SHOULD DO wenn Phase 1 validated
  - 3D Viewer + Feedback Upgrade = Unique Differentiator
  - Pricing: €399/mo Pro+

- **Phase 3 (8+ Wochen)** = NICE TO HAVE wenn scale validated
  - ERP + Team = Enterprise-Play
  - Pricing: €499/mo Enterprise

**ROI:**
- 4 Wochen Development → +€150/mo per Customer
- 10 Customers = +€1.500/mo = €18K/Jahr
- 20 Customers = +€3.000/mo = €36K/Jahr

**Decision:**
- Start Phase 1 JETZT wenn du an CNC Planner als Haupt-Revenue glaubst
- Skip wenn VC Job + Freelance wichtiger ist (Opportunity Cost)

---

*Nächster Schritt: Entscheidung + Prototype.* 🚀
