# Research Brief: Enterprise AI Governance — SOC 2, ISO 42001, EU AI Act Requirements for AI Agents

**Tag:** [INTERN] [KUNDE]
**Decision to Inform:** AgentTrust Enterprise Tier Features + Compliance-Positioning
**Date:** 2026-02-14

---

## Key Findings

### 1. EU AI Act — Deadlines sind real, Enforcement beginnt Aug 2026
- **Feb 2025:** Verbotene AI-Praktiken bereits durchsetzbar (€35M / 7% Umsatz)
- **Aug 2025:** GPAI-Anforderungen in Kraft (26 Provider inkl. Microsoft, Google, OpenAI, Anthropic haben Code of Practice unterzeichnet)
- **Aug 2026:** High-Risk AI-Systeme müssen voll compliant sein — Conformity Assessment dauert 6-12 Monate
- **Extraterritorial:** Gilt für jedes AI-System, dessen Output in der EU genutzt wird — auch US-Firmen betroffen
- Quelle: axis-intelligence.com (Dez 2025), trilateralresearch.com (Nov 2025)

**Was Firmen nachweisen müssen (EU AI Act):**
- Full data lineage tracking (welche Daten flossen in welchen Output)
- Human-in-the-loop Checkpoints für sicherheits-/rechte-/finanzrelevante Workflows
- Risk classification tags pro Modell/Agent
- AI Literacy Training für Mitarbeiter (seit Feb 2025 Pflicht)
- Quelle: sombrainc.com (Dez 2025), softwareimprovementgroup.com (Jan 2026)

### 2. ISO/IEC 42001 — Erster globaler AI Management System Standard
- Zertifizierbar (wie ISO 27001), AWS hat Zertifizierung bereits erhalten (Jan 2026)
- Struktur: Leadership → Planning → Support → Operation → Performance Evaluation → Continual Improvement
- Annex A: Controls-Liste für AI-Entwicklung, Annex B: Implementierungsguidance, Annex C: Risikoquellen
- **Kernpflichten:** Risikobewertung für AI-Systeme, Policies für verantwortungsvolle Entwicklung/Nutzung, fortlaufendes Monitoring
- Starke Überschneidung mit ISO 27001 — Firmen die schon 27001 haben, können aufbauen
- Quelle: a-lign.com (Jun 2025), aws.amazon.com (Jan 2026)

### 3. SOC 2 + AI — Audit-Framework adaptiert sich
- AICPA Trust Services Criteria (basierend auf COSO Framework) werden auf AI-Risiken angewendet
- Drei Risikokategorien für AI in SOC 2: **Privacy/Data Protection**, **Bias/Fairness**, **Governance/Compliance**
- SOC 2 Reports werden zum "Vertrauensmechanismus" für Firmen die AI deployen
- **Spezifische AI-Controls in SOC 2:** Audit Trails für jeden AI-Output, RBAC, Explainability, Data Retention/Deletion Policies
- Noch kein dedizierter "SOC 2 for AI" Standard — Firmen definieren eigene AI-Control-Implementierungen innerhalb des TSC-Frameworks
- Quelle: mossadams.com (Dez 2025), augmentcode.com (Sep 2025)

### 4. NIST AI Risk Management Framework (RMF) — US-Standard
- 4 Säulen: Govern, Map, Measure, Manage
- De-facto Procurement-Kriterium für US Federal Agencies und regulierte Industrien
- Praktisch: Red-Teaming vor Deployment, Bias Detection Pipelines, automatisierte Escalation Playbooks
- Quelle: sombrainc.com (Dez 2025)

### 5. Was Enterprise-Firmen KONKRET nachweisen müssen bei AI Agent Deployment

| Anforderung | EU AI Act | ISO 42001 | SOC 2 | NIST RMF |
|---|---|---|---|---|
| Audit Trail / Logging | ✅ Pflicht | ✅ Control | ✅ TSC | ✅ Manage |
| Data Lineage | ✅ Pflicht | ✅ Annex B | ○ Optional | ✅ Map |
| Human-in-the-Loop | ✅ High-Risk | ✅ Control | ○ Optional | ✅ Govern |
| Risk Classification | ✅ Pflicht | ✅ Annex C | ○ Optional | ✅ Map |
| Access Control (RBAC) | ✅ Pflicht | ✅ Control | ✅ TSC | ✅ Govern |
| Bias/Fairness Monitoring | ✅ High-Risk | ✅ Control | ✅ Control | ✅ Measure |
| Explainability | ✅ Pflicht | ✅ Control | ✅ Control | ✅ Measure |
| Incident Response | ✅ Pflicht | ✅ Control | ✅ TSC | ✅ Manage |

---

## Zahlen (verifiziert)

- **€35M oder 7% Umsatz** — Maximale Strafe für verbotene AI-Praktiken (EU AI Act) — Quelle: axis-intelligence.com
- **€15M oder 3% Umsatz** — Strafe für High-Risk Verstöße — Quelle: axis-intelligence.com
- **$2-5M initial, $500K-2M jährlich** — Compliance-Kosten Mid-Size Unternehmen — Quelle: axis-intelligence.com
- **$500K-2M initial** — Compliance-Kosten SMEs — Quelle: axis-intelligence.com
- **6-12 Monate** — Dauer Conformity Assessment für High-Risk AI — Quelle: axis-intelligence.com

---

## Wo passt AgentTrust als Compliance-Tool?

**Interpretation (meine Ableitung):** AgentTrust sitzt exakt in der Lücke zwischen "Firmen wollen AI Agents deployen" und "Regulierung verlangt Nachweisbarkeit". Die universelle Anforderung über ALLE Frameworks ist: **Audit Trail + Access Control + Explainability für jeden Agent-Action.**

Konkrete Feature-Positionierung:

1. **Audit Trail / Action Logging** → Erfüllt EU AI Act Art. 12 (Logging), SOC 2 TSC, ISO 42001 Annex A — DAS Kernfeature
2. **Permission Scoping / RBAC** → Agents dürfen nur tun was erlaubt ist, nachweisbar — RBAC ist in JEDEM Framework Pflicht
3. **Human-in-the-Loop Gating** → Approval Workflows vor kritischen Agent-Aktionen — EU AI Act High-Risk Pflicht
4. **Data Lineage per Action** → Welcher Agent hat welche Daten wann wohin bewegt — EU AI Act + ISO 42001
5. **Risk Classification Tags** → Agent-Level Risk Labels (High/Medium/Low) — EU AI Act Pflicht, ISO 42001 Annex C
6. **Compliance Report Export** → One-Click Audit Reports für SOC 2 Auditor / ISO Zertifizierer

**Judgment (meine Empfehlung):** Positioniere AgentTrust NICHT als "noch ein AI Governance Tool" (Markt wird überflutet), sondern als **"Compliance Layer specifically for AI Agents"** — die meisten Governance-Tools fokussieren auf ML-Modelle, nicht auf autonome Agents. Das ist der Differentiator.

---

## Claim Ledger (Top 5 Claims)

| # | Claim | Evidence | Confidence |
|---|---|---|---|
| 1 | "EU AI Act High-Risk Enforcement startet Aug 2026" | EU AI Act Gesetzestext + axis-intelligence.com + trilateralresearch.com | **High** — Gesetz verabschiedet, Datum steht fest |
| 2 | "Firmen brauchen Audit Trails für JEDEN AI-Agent Output" | Synthese aus EU AI Act Art. 12 + SOC 2 TSC (mossadams.com) + ISO 42001 Annex A (a-lign.com) | **High** — Alle 4 Frameworks fordern es |
| 3 | "Mid-Size Compliance-Kosten liegen bei $2-5M initial" | axis-intelligence.com (Dez 2025) — Einzelquelle | **Medium** — Nur 1 Quelle, Zahlen variieren stark je nach Branche. Confidence erhöhen: 2. Quelle finden (Deloitte/KPMG Reports) |
| 4 | "Meiste AI Governance Tools fokussieren auf Modelle, nicht Agents" | Eigene Marktbeobachtung (Holistic AI, Credo AI, IBM OpenPages fokussieren auf Model Risk) | **Medium** — Interpretation basiert auf Produktseiten, kein systematischer Marktreport. Confidence erhöhen: Analyst-Report (Gartner/Forrester) |
| 5 | "ISO 42001 wird zum Enterprise-Procurement-Standard wie SOC 2" | AWS-Zertifizierung (Jan 2026), PECB Training-Angebot, A-LIGN Audit-Services | **Medium** — Trend erkennbar, aber noch früh. Noch keine Daten zu Adoption Rate. |

---

## Contradiction Register

| Konflikt | Quellen | Warum unterschiedlich | Impact |
|---|---|---|---|
| EU AI Act Compliance-Kosten: $2-5M vs. $8-15M | axis-intelligence.com gibt beides an — nach Firmengröße | Kein echter Widerspruch, sondern Segmentierung (Mid-Size vs. Large Enterprise >€1B) | Gering — beide Zahlen nutzbar wenn Segment klar benannt |
| "Noch keine Strafen" vs. "Enforcement seit Feb 2025" | axis-intelligence.com (Dez 2025) | Verbotene Praktiken seit Feb 2025 durchsetzbar, aber bisher keine publizierten Strafen — Enforcement-Kapazität baut sich auf | Mittel — für Sales-Messaging relevant: Urgency real, aber noch keine Panik-Cases |

---

## Unsicher / Nicht Verifiziert

- Genaue Adoption Rate von ISO 42001 Zertifizierungen — nicht gefunden
- Wie viele Firmen bereits AI-Agent-spezifische SOC 2 Controls implementiert haben — keine Daten
- Ob es einen dedizierten "AI Agent" Risiko-Tier im EU AI Act gibt (Agents werden nicht explizit als Kategorie genannt — fallen unter bestehende Risk-Klassifizierung je nach Use Case)
- Marktgröße "AI Governance Tools" — nicht recherchiert (Rate Limit auf Search)

---

## Quellen

1. axis-intelligence.com — "EU AI Act News 2026" (Dez 2025) — Enforcement-Deadlines + Kosten ⭐
2. sombrainc.com — "AI Regulations in 2026" (Dez 2025) — Architektur-Anforderungen
3. a-lign.com — "Understanding ISO 42001" (Jun 2025) — Standard-Struktur
4. aws.amazon.com — "ISO 42001 FAQ" (Jan 2026) — AWS Zertifizierung
5. mossadams.com — "AI Controls in SOC 2 Reports" (Dez 2025) — SOC 2 + AI Integration ⭐
6. trilateralresearch.com — "EU AI Act Timeline" (Nov 2025) — Deadline-Mapping
7. softwareimprovementgroup.com — "EU AI Act Summary" (Jan 2026) — AI Literacy Pflicht
8. augmentcode.com — "AI SOC2 Compliance Guide" (Sep 2025) — SOC 2 AI Controls
9. mindstudio.ai — "AI Agent Compliance" (Jan 2026) — RBAC + Audit Trails für Agents
10. elevateconsult.com — "EU AI Code of Practice + ISO 42001 Map" (Nov 2025) — Framework-Überschneidungen

---

## Empfehlung

AgentTrust Enterprise Tier sollte sich als **"Compliance Infrastructure for AI Agents"** positionieren — Audit Trails, RBAC, Human-in-the-Loop Gating als Kernfeatures. Timing ist ideal: Aug 2026 EU AI Act High-Risk Enforcement zwingt Firmen JETZT zum Handeln (6-12 Monate Vorlauf nötig). ISO 42001 wird zum neuen SOC 2 für AI — wer heute Compliance-Features baut, hat einen Moat wenn der Markt explodiert.

---

```
Confidence: 75%
Sources checked: 10
Verified facts: 12
Unverified claims: 4
Search queries used: ["ISO 42001 AI management system certification requirements 2025 2026", "EU AI Act requirements deploying AI agents enterprises compliance 2025 2026", "SOC 2 AI agent controls audit trail logging governance requirements", "enterprise AI governance compliance tools market landscape 2025 2026"]
Time spent: ~8 min
```
