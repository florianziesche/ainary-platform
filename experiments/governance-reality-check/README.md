# Experiment: Governance Reality Check
**Date:** 2026-02-15
**Report:** AR-028 — AI Governance: Framework vs. Reality
**Purpose:** Apply ISO 42001 and NIST AI RMF to our own Ainary agent pipeline, document what they catch and miss.

## Our Pipeline (What We're Testing Against)
- Multi-agent research system (Claude-based)
- Subagent spawning for parallel research
- Web search + web fetch for source gathering
- File system read/write for report generation
- HTML template-based output with PDF generation
- Memory system (MEMORY.md, daily notes)
- Quality pipeline: 6-phase A+ process with adversarial review

## Documented Failure Modes (From Our Reports)
1. **Hallucination / Fabrication** — Agent generates false statistics or citations (AR-010 Grok RAG poisoning)
2. **Confidence Drift** — Confidence scores inflate over successive reports without evidence improvement
3. **Source Quality Degradation** — Agent cites vendor marketing as primary research
4. **Prompt Injection via Web Fetch** — External content contains adversarial instructions
5. **Agent Contagion** — One subagent's error propagates to main agent output
6. **Memory Corruption** — Stale or wrong data persists in memory files
7. **Template Drift** — Report deviates from locked template rules
8. **Circular Citation** — Agent cites our own previous reports as independent evidence
9. **HITL Bypass** — Human reviewer approves without reading (automation bias)
10. **Cost Runaway** — Agent spawns excessive API calls without budget constraint

---

## ISO 42001 Assessment Against Our Pipeline

### Clause-by-Clause Review

| ISO 42001 Clause | Relevant? | Our Pipeline Status | Catches Our Failures? |
|---|---|---|---|
| 4. Context of Organization | Partially | We document purpose in AGENTS.md | No — doesn't address agent-specific risks |
| 5. Leadership | Yes | Florian = single decision-maker | Catches HITL bypass (requires management commitment) |
| 6. Planning (Risk Assessment) | Yes | No formal risk register for pipeline | Would catch if implemented — but ISO doesn't specify AI-specific risks |
| 7. Support (Resources, Competence) | Partially | Tools documented in TOOLS.md | Doesn't address model capability limits |
| 8. Operation (AI Lifecycle) | Yes | 6-phase pipeline = lifecycle | Partially catches — requires testing, validation |
| 9. Performance Evaluation | Partially | output-tracker.md exists | Would catch confidence drift IF we measured it |
| 10. Improvement | Yes | Pipeline improvement protocol exists | Catches template drift (requires corrective action) |
| A.2 AI Policy | Yes | Not formalized | Would require us to write one — process improvement |
| A.3 AI System Impact Assessment | Critical gap | We don't do impact assessments | Would catch source quality issues IF implemented rigorously |
| A.4 AI System Lifecycle | Yes | Covered by 6-phase pipeline | Partially addresses hallucination via testing requirements |
| A.5 Data for AI Systems | Critical gap | No data quality framework | Doesn't catch web fetch poisoning specifically |
| A.6 AI System Performance | Yes | Confidence scores exist | Could catch confidence drift — but ISO doesn't specify HOW to measure |
| A.7 Third-party/Supplier Management | Critical gap | No vendor assessment for API providers | Doesn't address model provider risk (Anthropic API changes) |

**ISO 42001 Score: Catches 4/10 failure modes (40%)**
- ✅ Catches: Confidence drift (via performance eval), Template drift (via improvement), HITL bypass (via leadership commitment), Cost runaway (via resource planning)
- ❌ Misses: Hallucination, Source quality, Prompt injection, Agent contagion, Memory corruption, Circular citation

**Why:** ISO 42001 is a process framework. It would require us to BUILD monitoring — but doesn't tell us WHAT to monitor for AI agents specifically.

---

## NIST AI RMF Assessment Against Our Pipeline

### Pillar-by-Pillar Review

| NIST Pillar | Sub-function | Our Pipeline Status | Catches Our Failures? |
|---|---|---|---|
| **GOVERN** | Gov 1: Policies | AGENTS.md + TEMPLATE-RULES.md | Partially — structure exists, not formalized as governance |
| | Gov 2: Accountability | Florian reviews all output | Catches HITL bypass — requires defined roles |
| | Gov 3: Workforce | Single operator + AI system | Doesn't address competence gaps |
| | Gov 4: Organizational | Memory system + daily notes | Partially catches memory corruption — requires audit trail |
| | Gov 5: Engagement | Reports are public artifacts | Doesn't address stakeholder feedback loops |
| | Gov 6: Risk management integration | Not integrated with broader risk | Would require formal risk integration |
| **MAP** | Map 1: Context/purpose | Defined per report | Catches circular citation — requires use case scoping |
| | Map 2: Categorize AI | Pipeline not formally categorized | Would require risk classification |
| | Map 3: Benefits & costs | API costs tracked | Catches cost runaway — requires cost-benefit analysis |
| | Map 4: Risks & impacts | No formal risk mapping | Would catch more if implemented |
| **MEASURE** | Measure 1: Metrics | Confidence scores, output-tracker | Could catch confidence drift — requires baseline |
| | Measure 2: AI systems evaluated | Ad-hoc review only | Would require systematic testing → catches hallucination |
| | Measure 3: Track identified risks | Not tracked systematically | Would catch source quality if tracked |
| | Measure 4: Feedback | Post-production reflection exists | Partially catches agent contagion |
| **MANAGE** | Manage 1: Prioritize risks | No prioritization framework | Would improve if implemented |
| | Manage 2: Plan responses | Circuit breakers not implemented | Would catch prompt injection — requires response plans |
| | Manage 3: Manage risks | Manual review only | Insufficient for automated agents |
| | Manage 4: Regular assessment | Not regular | Would catch confidence drift if regular |

**NIST AI RMF Score: Catches 5/10 failure modes (50%)**
- ✅ Catches: Confidence drift (Measure), HITL bypass (Govern), Cost runaway (Map), Circular citation (Map), Hallucination (Measure — via red teaming mandate)
- ❌ Misses: Source quality degradation, Prompt injection, Agent contagion, Memory corruption, Template drift

**Why:** NIST is better than ISO for our use case because it explicitly mentions red teaming and measurement. But it's still too abstract for agent-specific failure modes like prompt injection via web fetch or memory file corruption.

---

## Simulation 1: Agent Hallucination (Grok-style RAG Poisoning)

**Scenario:** Agent fetches a web page that contains fabricated statistics. Agent incorporates them into report without verification.

**Would ISO 42001 catch this?**
- Clause A.5 (Data for AI Systems) requires data quality management → PARTIALLY. ISO would require us to have a data quality process. But it doesn't specify "verify web-fetched statistics against primary sources."
- Clause 8 (Operation) requires testing → PARTIALLY. If we tested with adversarial inputs, we'd catch it. But ISO doesn't mandate adversarial testing.
- **Verdict: ISO would NOT have caught this in practice.** The process would exist on paper, but the specific check (verify web statistics) would not be in the checklist.

**Would NIST AI RMF catch this?**
- Measure 2 explicitly mentions "red teaming" and adversarial testing → YES, if implemented.
- Map 4 requires identifying risks → YES, if "fabricated web sources" is in the risk register.
- **Verdict: NIST WOULD have caught this IF the red teaming was actually conducted.** But NIST is voluntary, so the probability of actually doing red teaming is low (~20% per our AR-022 analysis).

## Simulation 2: Confidence Drift Over 10 Reports

**Scenario:** Report confidence scores: 72%, 75%, 78%, 80%, 82%, 84%, 85%, 87%, 88%, 90% — steady inflation without corresponding evidence improvement.

**Would ISO 42001 catch this?**
- Clause A.6 (AI System Performance) requires monitoring → YES, if confidence is a tracked metric with a baseline.
- Clause 9 (Performance Evaluation) requires audits → YES, if auditor checks trend.
- **Verdict: ISO COULD catch this** — but only if the organization specifically tracks confidence calibration. ISO doesn't mandate it; it just requires "performance evaluation."

**Would NIST AI RMF catch this?**
- Measure 1 (Appropriate metrics) → YES, if confidence calibration is a metric.
- Measure 4 (Feedback incorporated) → YES, if there's a feedback loop comparing confidence to actual accuracy.
- Manage 4 (Regular assessment) → YES, if regular reviews check for drift.
- **Verdict: NIST is BETTER here** because it explicitly requires metrics and feedback loops. But still requires the organization to choose "confidence calibration" as a metric.

---

## Score Card Summary

| Failure Mode | ISO 42001 | NIST AI RMF | Either Framework |
|---|---|---|---|
| 1. Hallucination | ❌ | ⚠️ (if red-teamed) | ⚠️ |
| 2. Confidence Drift | ⚠️ (if tracked) | ✅ (if metrics set) | ✅ |
| 3. Source Quality Degradation | ❌ | ❌ | ❌ |
| 4. Prompt Injection | ❌ | ❌ | ❌ |
| 5. Agent Contagion | ❌ | ❌ | ❌ |
| 6. Memory Corruption | ❌ | ⚠️ (audit trail) | ⚠️ |
| 7. Template Drift | ✅ (improvement) | ❌ | ✅ |
| 8. Circular Citation | ❌ | ⚠️ (use case scoping) | ⚠️ |
| 9. HITL Bypass | ✅ (leadership) | ✅ (governance) | ✅ |
| 10. Cost Runaway | ✅ (resources) | ✅ (cost-benefit) | ✅ |

**ISO 42001: 4/10 caught (40%)**
**NIST AI RMF: 5/10 caught (50%)**
**Combined: 6/10 caught (60%)**
**Neither framework catches: 4/10 (40%) — the agent-specific failure modes**

### The 40% Gap
The failure modes that NEITHER framework catches are:
1. **Source quality degradation** — No framework says "verify that your AI doesn't cite vendor blogs as research"
2. **Prompt injection via web fetch** — Agent-specific attack vector, not in any governance framework
3. **Agent contagion** — Multi-agent coordination failures are too new for existing frameworks
4. **Memory corruption** — Persistent state in AI agents is not addressed by any standard

These are the **agentic AI failure modes** — they didn't exist when ISO 42001 and NIST AI RMF were written.

---

## Conclusion
Frameworks catch the **organizational** failure modes (governance, resources, measurement) but miss the **technical agent-specific** ones (injection, contagion, memory). This is the gap between framework governance and operational reality.
