# Gotham vs. Ainary Research Network — Capability Matrix

*Quelle: UK Government G-Cloud 14 Service Definition Document (Nov 2024), Palantir.com, IEEE Xplore*
*Stand: 2026-03-07*

---

## Zusammenfassung

Gotham hat **~25 Kern-Capabilities** in 7 Kategorien. Wir decken **8 davon ab** (teilweise), **6 sind in Arbeit**, **11 fehlen komplett**. Die größten Gaps: **Collaboration**, **Geospatial**, **Video/Edge**, und **Workflow Automation**.

Unsere Stärke gegenüber Gotham: **Beipackzettel-System** (Epistemic Transparency), **Audience-Briefings** (demokratisiertes COP), **Automated Signal Ingest** (kein FDE nötig). Gotham hat nichts Vergleichbares zu unserem Trust-Scoring auf Claim-Ebene.

---

## Die Matrix

### Legende
- ✅ **HAVE** — Feature existiert und funktioniert
- 🟡 **PARTIAL** — Grundlage da, aber unvollständig
- 🔧 **IN PROGRESS** — Code/Konzept existiert, noch nicht deployed
- ❌ **MISSING** — Nicht vorhanden
- 🚫 **N/A** — Nicht relevant für unseren Use Case (Defense-spezifisch)

---

## 1. CORE PLATFORM / ONTOLOGIE

| # | Gotham Capability | Gotham Details | Wir | Status | Was wir haben | Definition of Done |
|---|---|---|---|---|---|---|
| 1.1 | **Ontology (Semantic Data Model)** | Objects + Properties + Relationships. Menschen, Orte, Organisationen, Dokumente, Events als semantische Objekte. Adaptiv. | 🟡 | PARTIAL | 15 Topics, 55 Claims, 4 Reports. Flache Topic→Claim Zuordnung. Keine echten Entities/Relationships. | **DONE wenn:** Entity-Typen (Person, Org, Concept, Event) mit Properties. Relationships zwischen Entities (nicht nur Topic-Tags). Min. 3 Relationship-Types (supports, contradicts, depends_on). Entity Resolution (Deduplizierung). |
| 1.2 | **Data Integration Engine** | Jedes Format, jedes Volume. Audio, Video, Streaming. Single cohesive data asset. | 🟡 | PARTIAL | 6 RSS-Feeds via ingest-signals.js. Nur Text/RSS. Kein Audio, Video, API, Streaming. | **DONE wenn:** ≥10 Quellen-Typen (RSS ✅, API, PDF, Twitter, GitHub, ArXiv, Podcast-Transkript). Incremental ingest (nur neue Signale). Dedup auf URL-Ebene. Source-Health-Monitoring. |
| 1.3 | **Unified Search** | Single search across all data. Federated. External records promotable. | ❌ | MISSING | Kein Search. Browser-Filter auf Topics, aber keine Freitext-Suche. | **DONE wenn:** Freitext-Suche über Signals + Claims + Reports. Ergebnisse mit Trust-Score sortierbar. Faceted filtering (Source, Topic, Confidence, Date). |
| 1.4 | **Secure Collaboration** | Multi-User, Access Control, Attribute-Level Security, Cross-Org Sharing. | 🚫 | N/A | Single-User-System. Kein Multi-User geplant (Phase 1). | **DONE wenn:** (Phase 2+) Shareable Links mit Read-Only. Optional: Kommentar-Layer. |
| 1.5 | **Open APIs** | REST APIs, Open Formats, Client Generation. | ❌ | MISSING | Kein API. Static JSON Files. | **DONE wenn:** `/api/signals`, `/api/claims`, `/api/search` Endpoints. JSON-Export. Webhook für neue Signale. |
| 1.6 | **Workspace (Unified Entry Point)** | Single UI für alle Apps. Browser oder Desktop. | ✅ | HAVE | index.html ist der Entry Point. Tabs für alle Views. Responsive. | **DONE.** Verbesserung: Breadcrumb-Navigation zwischen Views. |

---

## 2. CORE APPLICATIONS

| # | Gotham Capability | Gotham Details | Wir | Status | Was wir haben | Definition of Done |
|---|---|---|---|---|---|---|
| 2.1 | **Browser (Entity Detail View)** | Object Detail anzeigen. Properties, Notes, History, Relationships. Double-Click Navigation. | 🟡 | PARTIAL | Claim-Karten mit Trust-Score, Sources, So-What. Aber kein dedizierter Entity-Detail-View. Kein History. | **DONE wenn:** Dedizierter Claim/Entity Detail View (Fullscreen-Modal oder eigene URL). Zeigt: alle Properties, verlinkte Claims, Source-Trail, Änderungshistorie, Beipackzettel. |
| 2.2 | **Custom Object Views (COVs)** | Konfigurierbare Dashboards pro User/Team. Gleicher Object Type, verschiedene Views. | ❌ | MISSING | Eine fixe View pro Audience (Briefings). Nicht konfigurierbar. | **DONE wenn:** User kann Dashboard-Layout wählen (Grid/List/Cards). Persistente Filter-Presets. Min. 2 vordefinierte Views pro Audience. |
| 2.3 | **Object Explorer (Top-Down Analysis)** | Drill-down über Millionen Records. Histogramme, Aggregationen, Trend-Analyse, Alerts. | 🟡 | PARTIAL | Topic Dossiers mit Claim-Counts. Trends (5 trending topics). Kein Drill-down, keine Histogramme. | **DONE wenn:** Interactive Filter-Chain (Domain → Topic → Claim → Signal). Histogramm (Claims per Topic, Signals per Week). Time-Series Trend-Chart. Drill-down von Aggregat zu Einzelsignal. |
| 2.4 | **Chat (Secure Messaging)** | IM, Channels, File/Object Sharing, Classification-Controlled. | 🚫 | N/A | Nicht relevant. Florian kommuniziert via Telegram/Signal. | N/A für Solopreneur-Phase. |
| 2.5 | **Inbox (Alerts & Notifications)** | Zentrales Alert-System. Search Feeds, Object Watch, Geofence Alerts, Sharing Alerts. | ❌ | MISSING | Kein Alert-System. Keine Notifications. | **DONE wenn:** Email/Telegram Digest (täglich oder bei High-Confidence Signal). Watchlist für Topics (Alert wenn neues Signal). Prediction-Deadline-Alerts. |
| 2.6 | **Slides (Data-Backed Briefings)** | Live-Daten in Presentations. Collaborative. Export PPTX/PDF. | 🟡 | PARTIAL | Audience Briefings (COP) sind quasi "Live Slides" — datengetrieben, auto-generiert. Kein Export. | **DONE wenn:** Export als PDF/PNG (Briefing-Snapshot). "Share Briefing" Link. Quarterly Trend-Report auto-generiert. |
| 2.7 | **Dossier (Collaborative Notes)** | Real-time Editor. Drag-Drop Entities. Dynamic Links. Templates. Export Word/PDF. | 🔧 | IN PROGRESS | Topic Dossiers existieren konzeptionell (Knowledge Graph hat executiveSummary, openQuestions). Kein Editor, kein Drag-Drop. | **DONE wenn:** Topic-Dossier-Page mit Executive Summary, Claims-Liste, Open Questions, Related Topics. Edit-Fähigkeit (Admin). Export als Markdown/PDF. Template-System für neue Dossiers. |
| 2.8 | **Graph (Network Analysis)** | Visual Network auf Canvas. Search Around. Timeline. Histogram. Collaborative. Export HTML. | 🔧 | IN PROGRESS | Knowledge Graph JSON existiert (Topics, Claims, Connections). Visualisierung: nur Topic-Liste und Claim-Karten. Kein visueller Graph. | **DONE wenn:** D3.js oder Sigma.js Force-Directed Graph. Nodes = Topics + Claims. Edges = supports/contradicts/related. Click-to-Expand (Search Around). Timeline-View (Claims über Zeit). Export als SVG/PNG. |
| 2.9 | **Gaia (Geospatial/Map)** | Collaborative Map. Heatmaps. Geo-Search. Real-Time Tracking. GIS Workflows. | 🚫 | N/A | Kein Geo-Use-Case in Research Network. (Dossier-Platform hat Geo für Städte, aber anderes Produkt.) | N/A für Research Network. Potenzial: Signal-Herkunft auf Weltkarte. |
| 2.10 | **Video (FMV Analysis)** | Live Video + AR Overlays + AI Detection. | 🚫 | N/A | Nicht relevant für Research Intelligence. | N/A. |

---

## 3. ANALYSIS & INTELLIGENCE

| # | Gotham Capability | Gotham Details | Wir | Status | Was wir haben | Definition of Done |
|---|---|---|---|---|---|---|
| 3.1 | **Investigative Workflows** | Link Analysis, CDR Analysis, Produce Actionable Intelligence. | 🟡 | PARTIAL | Signal → Claim → Topic Chain existiert. "So What" und "Research Gaps" pro Signal. Aber kein geführter Workflow. | **DONE wenn:** Investigation-Template: Start mit Frage → relevante Signals → Claims → Widersprüche → Conclusion. Speicherbar als "Investigation". |
| 3.2 | **Network Analysis** | Multi-Hop Graph Queries. Pattern Discovery. | ❌ | MISSING | Connections-Feld existiert in KG JSON aber ist leer. Kein Multi-Hop. | **DONE wenn:** Connections populated (min. 30). 2-Hop-Query möglich ("Was hängt mit X zusammen, und was hängt damit zusammen?"). Pattern-Detection ("3 unabhängige Quellen sagen dasselbe"). |
| 3.3 | **Trend & Time Series** | Timeline across all data. Forecast. Pattern Discovery. | 🟡 | PARTIAL | 5 Trending Topics (7d window). Predictions mit Horizont. Aber kein visuelles Timeline-Chart. | **DONE wenn:** SVG/Canvas Timeline-Chart. X-Achse = Zeit, Y = Signal-Dichte pro Topic. Overlay: Predictions mit Deadline-Marker. Sparklines in Topic-Cards. |
| 3.4 | **AI/ML Integration** | Model Integration, Detection, Feedback Loop, Accuracy Improvement. | 🟡 | PARTIAL | Regelbasierte Klassifikation (Topic-Keywords). Regelbasierte Predictions. Kein ML-Modell. Kein Feedback-Loop. | **DONE wenn:** LLM-basierte Claim-Extraction aus Signals (statt Keyword). LLM-basierte Zusammenfassung für Briefings. User-Feedback auf Predictions (correct/wrong → Kalibrierung). |

---

## 4. DATA MANAGEMENT

| # | Gotham Capability | Gotham Details | Wir | Status | Was wir haben | Definition of Done |
|---|---|---|---|---|---|---|
| 4.1 | **Data Import/Export** | Any system, any format. Streaming. | 🟡 | PARTIAL | RSS-Ingest (6 Quellen). JSON-Export (static files). Kein Import-UI, kein Streaming. | **DONE wenn:** CLI für Ad-hoc-Import (URL, PDF, JSON). Export: Full JSON + CSV. Streaming: Webhook für Echtzeit-Ingest. |
| 4.2 | **Data Federation** | External Systems durchsuchbar neben internen Daten. | ❌ | MISSING | Nur eigene Daten. Kein Federated Access. | **DONE wenn:** Obsidian Vault als federierte Quelle (Search across Research Network + Vault). Optional: Externe APIs (ArXiv, Semantic Scholar). |
| 4.3 | **Data Lineage / Provenance** | Jedes Datum tethered to original source. Full audit trail. | ✅ | HAVE | Jeder Claim hat: reportId, sources[], realSources[], provenance, admiralty code, EIJA rating. Jedes Signal hat: sourceId, sourceTrustFloor, url. | **DONE.** Verbesserung: Visual Provenance Trail (Signal → Claim → Report → Decision). |
| 4.4 | **Alert System** | Object Watch, Search Feeds, Geofence. | ❌ | MISSING | Kein Alert-System. | **DONE wenn:** = 2.5 (Inbox). |

---

## 5. COLLABORATION & BRIEFING

| # | Gotham Capability | Gotham Details | Wir | Status | Was wir haben | Definition of Done |
|---|---|---|---|---|---|---|
| 5.1 | **Common Operating Picture (COP)** | Einheitliches Lagebild für alle Nutzer. | ✅ | HAVE | 4 Audience-Briefings (Founders, Devs, VCs, SMEs) mit Summary, Top Signals, Themes, Recommendations. Auto-generiert aus Signaldaten. | **DONE.** Verbesserung: LLM-generierte Summaries statt Keyword-Templates. |
| 5.2 | **Report Builder** | Daten-getriebene Reports. Templates. Auto-Population. | 🟡 | PARTIAL | Report Builder UI existiert (buildReport function). 4 Research Reports im KG. | **DONE wenn:** Template-System (Weekly Digest, Topic Deep-Dive, Prediction Review). Auto-Population aus aktuellen Daten. Export PDF. Scheduled Generation (Cron). |
| 5.3 | **Sharing & Distribution** | Cross-Org Sharing. Export. Broadcasting. | ❌ | MISSING | Keine Share-Funktion. Nur Public URL. | **DONE wenn:** Share-Link pro Briefing/Report (mit UTM). Email-Digest (Weekly). Social-Share (Twitter/LinkedIn Card Preview). |

---

## 6. UNSERE UNIQUE CAPABILITIES (Gotham hat das NICHT)

| # | Capability | Details | Gotham Equivalent | Vorteil |
|---|---|---|---|---|
| 6.1 | **Beipackzettel (Epistemic Transparency)** | Jedes Signal, jede Prediction, jedes Briefing hat: Confidence, Method, Uncertainties, Not-Checked, Risk-Level. | ❌ Gotham hat kein systematisches Uncertainty-Disclosure. Analyst muss selbst bewerten. | Demokratisiert Intelligence. Auch Non-Experts können Vertrauenswürdigkeit einschätzen. |
| 6.2 | **Admiralty + EIJA Dual-Rating** | Claims haben sowohl Admiralty Code (A1-F6) als auch EIJA-Rating (Evaluated/Implied/Judgemental/Assumed). | 🟡 Gotham hat interne Quality-Scores, aber nicht standardisiert für End-User sichtbar. | NATO-Standard + akademischer Standard kombiniert. Vergleichbar über Quellen hinweg. |
| 6.3 | **Automated Predictions** | System generiert Predictions aus Signal-Clustern. Mit Horizon, Confidence, Basis. | ❌ Gotham unterstützt Analyst-Predictions, generiert sie aber nicht automatisch. | Skaliert ohne Analysten. Prediction-Track-Record messbar. |
| 6.4 | **Research Gap Detection** | System erkennt automatisch: "Zu diesem Aspekt fehlen Daten." | ❌ Gotham identifiziert keine Wissenslücken automatisch. | Steuert Research-Aufwand. "Was wissen wir NICHT?" ist wertvoller als "Was wissen wir?" |
| 6.5 | **Trust Score Computation** | Gewichteter Score aus Source-Trust, Admiralty, Aktualität, Corroboration. | 🟡 Gotham hat Data Lineage, aber keinen computed Trust Score pro Claim. | Quantifiziert Vertrauen. Vergleichbar. Sortierbar. |
| 6.6 | **Audience-Specific COP** | Gleiche Daten, 4 verschiedene Audience-Views mit angepassten Empfehlungen. | ❌ Gotham hat Roles, aber keine automatisch generierten Audience-Summaries. | Palantir braucht FDEs dafür. Wir generieren es automatisch. |

---

## Prioritäts-Ranking (Was bauen wir als nächstes?)

### 🔴 HIGH IMPACT (nächste 2 Wochen)
1. **Visual Knowledge Graph** (2.8) — D3.js Force Graph. Der "Wow-Moment" für jeden Besucher.
2. **Unified Search** (1.3) — Freitext über alles. Grundlage für alles andere.
3. **Object Explorer Drill-Down** (2.3) — Interactive Filtering, Histogramme.

### 🟡 MEDIUM IMPACT (nächste 4 Wochen)
4. **Alert/Digest System** (2.5/4.4) — Email/Telegram bei High-Confidence Signals.
5. **Timeline Chart** (3.3) — SVG Timeline. Signals + Predictions auf Zeitachse.
6. **Topic Dossier Page** (2.7) — Dedicated Page pro Topic mit allem Wissen.

### 🟢 LOWER PRIORITY (Q2+)
7. **LLM-Enhanced Briefings** (3.4/5.1) — LLM-Summary statt Keyword-Template.
8. **More Data Sources** (1.2) — ArXiv, Twitter, GitHub, Podcasts.
9. **API Endpoints** (1.5) — REST API für programmatischen Zugriff.
10. **Sharing & Distribution** (5.3) — Share-Links, Social Cards, Email Digest.

---

## Scoring

| Kategorie | Gotham Capabilities | Wir: HAVE | Wir: PARTIAL | Wir: MISSING | Wir: N/A |
|---|---|---|---|---|---|
| Core Platform | 6 | 1 | 2 | 2 | 1 |
| Applications | 10 | 0 | 4 | 2 | 4 |
| Analysis | 4 | 0 | 3 | 1 | 0 |
| Data Management | 4 | 1 | 1 | 2 | 0 |
| Collaboration | 3 | 1 | 1 | 1 | 0 |
| **TOTAL** | **27** | **3 (11%)** | **11 (41%)** | **8 (30%)** | **5 (18%)** |

**Coverage (excl. N/A): 14/22 = 64% mindestens PARTIAL, 3/22 = 14% HAVE**
**+ 6 Unique Capabilities die Gotham NICHT hat**

---

*Confidence: 80% — Gotham-Features aus offizieller UK Gov Service Definition (Nov 2024). Unsere Audit basiert auf aktuellem Code-Stand. Unsicherheit: Gotham hat "sensitive applications" die nicht dokumentiert sind.*
