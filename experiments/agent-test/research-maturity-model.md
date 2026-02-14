# Research Brief — Report #4: The AI Agent Maturity Model
<!-- Date: 2026-02-14 | Agent: RESEARCHER (Opus) | Audience: [PUBLIC] -->
<!-- Confidence: 75% | Sources checked: 22 | Time: ~45 min -->

---

## THESIS

**"Most organizations think they're at Level 3. They're at Level 1."**

No existing maturity model accounts for what makes AI agents different from traditional AI: autonomy, memory, multi-agent orchestration, trust architecture, and human-in-the-loop design. Every major framework (Gartner, McKinsey, Deloitte, Microsoft) treats AI as a tool. Agents aren't tools — they're actors.

---

## PART 1: EXISTING AI MATURITY MODELS — What Exists Today

### 1.1 Gartner AI Maturity Model (4 Levels)
- **Levels:** Awareness → Active → Operational → Transformational
- **Focus:** Organizational readiness, governance, strategy alignment
- **Key finding:** Only **54% of AI projects move from pilot to production** (Gartner 2024)
- **What it measures:** Data strategy, talent, governance, technology infrastructure
- **What it misses:** Agent autonomy, inter-agent trust, memory architecture, orchestration patterns
- **Source:** Gartner "4 Levels of AI Maturity" (2024); Gartner "5 Practices to Build AI Readiness" (2025)

### 1.2 McKinsey AI Maturity / "AI High Performers"
- **Not a formal maturity model** — but effectively a 3-tier classification
- **Tiers:** Experimenters → Scalers → High Performers
- **Key finding:** Only **6% are "AI High Performers"** (≥5% EBIT impact, n=1,993)
- **High performers:** 55% redesign workflows (vs 20% others), achieve 2-3x productivity gains
- **What it measures:** Revenue impact, workflow redesign, scale of deployment
- **What it misses:** Agent-specific capabilities entirely — treats AI as analytics/automation
- **Source:** McKinsey State of AI 2025 (n=1,993)

### 1.3 Deloitte State of AI in the Enterprise
- **Framework:** "Pathseekers → Explorers → Practitioners → Seasoned"
- **Key finding:** Most enterprises cluster at "Explorers" — experimenting without production deployment
- **Focus:** ROI measurement, organizational change, talent gaps
- **What it misses:** No agent dimension at all. Model predates agentic AI wave.
- **Source:** Deloitte "State of AI in the Enterprise" Survey (7th edition, 2024)

### 1.4 Microsoft AI Maturity Assessment
- **5 levels:** Foundational → Approaching → Aspirational → Mature → Transformational
- **Focus:** Cloud infrastructure, data platform, organizational culture
- **Key finding:** Microsoft uses this internally and with enterprise customers for Azure AI adoption
- **What it misses:** Agent-specific: no orchestration, no trust, no memory, no autonomy scoring
- **Source:** Microsoft AI Maturity Assessment Tool (2024)

### 1.5 Google Cloud AI Maturity Scale
- **3 phases:** Tactical → Strategic → Transformational
- **Focus:** Data readiness, ML operations, organizational alignment
- **Key finding:** Google named "Agent Trust" as key 2026 theme but has no concrete maturity framework for it
- **What it misses:** Explicitly acknowledges agents as new but hasn't updated the model
- **Source:** Google Cloud Blog (2025); Google Developers Blog (2026)

### 1.6 IBM AI Ladder
- **4 rungs:** Collect → Organize → Analyze → Infuse
- **Focus:** Data lifecycle — very data-centric, not capability-centric
- **What it misses:** Entire agent paradigm. This is a data maturity model wearing AI clothes.
- **Source:** IBM Think (2023)

---

## PART 2: MATURITY MODELS THAT WORKED — Precedents

### 2.1 CMMI (Capability Maturity Model Integration)
- **Developed:** Carnegie Mellon SEI, 1987-present (V3.0 in 2023)
- **5 levels:** Initial → Managed → Defined → Quantitatively Managed → Optimizing
- **Why it worked:** Required by US Government contracts. Clear criteria per level. Appraisal process (SCAMPI). Measurable.
- **Key design:** Each level has specific process areas with goals and practices
- **Lesson for us:** The model must be PRESCRIPTIVE enough to be useful, not just descriptive
- **Source:** Wikipedia/CMMI; ISACA/CMMI Institute

### 2.2 DORA / DevOps Maturity (Accelerate)
- **Framework:** 4 key metrics (Deployment Frequency, Lead Time, Change Failure Rate, MTTR)
- **4 tiers:** Low → Medium → High → Elite
- **Why it worked:** Measurable metrics, not subjective assessment. Annual report creates benchmarking pressure. Correlates with business outcomes.
- **Key insight:** DORA didn't measure "are you doing DevOps?" — it measured OUTCOMES
- **Lesson for us:** Measure agent outcomes (reliability, autonomy rate, trust calibration) not inputs (tools, frameworks)
- **Source:** DORA Research Program (Google); "Accelerate" (Forsgren, Humble, Kim)

### 2.3 Cloud Maturity Model (AWS / Industry)
- **Typical levels:** Project → Foundation → Migration → Reinvention → Optimization
- **Why it worked:** Clear migration path. Each level has specific technical milestones.
- **Lesson for us:** Organizations need to know WHAT TO DO NEXT, not just where they are
- **Source:** AWS Cloud Adoption Framework; various industry models

### 2.4 Data Maturity Model (various)
- **Notable:** Data Management Maturity Model (DMM) by CMMI Institute
- **Levels mirror CMMI:** Performed → Managed → Defined → Measured → Optimized
- **Why relevant:** Data maturity is a prerequisite for agent maturity
- **Source:** CMMI Institute DMM

---

## PART 3: WHAT'S MISSING — The Agent Gap

### 3.1 Dimensions No Existing Model Covers

| Dimension | Why It's Agent-Specific | Current Coverage |
|---|---|---|
| **Autonomy Level** | Agents act independently; traditional AI assists | ZERO models measure this |
| **Trust Architecture** | Inter-agent trust, confidence calibration, provenance | Google mentions it, nobody measures it |
| **Memory Governance** | Episodic/semantic/procedural memory with integrity | Not in ANY maturity model |
| **Orchestration Patterns** | Single vs multi-agent, delegation, escalation | Not measured anywhere |
| **Human-in-the-Loop Design** | Alert fatigue, intervention quality, not just existence | EU AI Act requires HITL but doesn't define quality |
| **Failure Recovery** | Graceful degradation, rollback, containment | Partially in CMMI (incident management) |
| **Agent Identity** | Non-human identity management, credential governance | 10% have strategy (WEF) |

### 3.2 The Core Problem with Existing Models
Every existing AI maturity model asks: **"How well do you USE AI?"**

The right question for agents is: **"How well do you GOVERN actors that make decisions on your behalf?"**

This is the difference between measuring tool usage and measuring organizational trust in autonomous systems. It's closer to HR maturity than IT maturity.

### 3.3 Data on Current Enterprise State

| Metric | Value | Source | Confidence |
|---|---|---|---|
| AI projects failing | 95% (methodology unclear) | MIT via secondary | **Low** |
| Projects reaching production | 54% move from pilot | Gartner 2024 | **Medium** |
| "AI High Performers" | 6% of enterprises | McKinsey (n=1,993) | **High** |
| Enterprise apps with agents by 2026 | 40% (projection) | Gartner | **Medium** |
| Agentic projects canceled by 2027 | >40% (projection) | Gartner | **Medium** |
| Orgs experimenting with agents | 62% | McKinsey 2025 | **High** |
| Agents in enterprise-wide production | <10% | McKinsey 2025 | **High** |
| Orgs with non-human identity strategy | 10% | WEF 2025 | **Medium** |
| Agent credential leaks reported | 23% of IT pros | Okta | **Medium** |
| Agent observability adoption | 94% of prod agent devs | LangChain | **Medium** |

**Interpretation:** 62% experiment, <10% deploy enterprise-wide, 6% see EBIT impact. The vast majority are at Level 1 or 2, not where they think they are.

---

## PART 4: GAP ANALYSIS — Research Pack vs. New

### What We Already Knew (from research-pack)
- Trust vacuum across the agent stack (5/7 briefs confirm)
- Overconfidence is structural: 84% overconfident, VCE biased, 12/12 defenses broken
- Three-layer trust gap: Communication (solved) → Identity (early) → Trustworthiness (missing)
- HITL empirically fails: 67% alerts ignored, alert fatigue documented
- Memory has no governance: no provenance, no confidence per memory, no integrity checks
- 6% are high performers, 95% fail (methodologically weak but directionally correct)
- Regulatory pressure converging: EU AI Act Aug 2026, $2-5M compliance cost

### What's NEW in This Research
1. **No existing maturity model includes agent-specific dimensions** — confirmed across Gartner, McKinsey, Deloitte, Microsoft, Google, IBM
2. **CMMI's success factors are transferable:** prescriptive levels, government adoption pressure, appraisal process
3. **DORA's approach is the right template:** measure OUTCOMES not inputs; 4 key metrics per tier
4. **The "governance of actors" framing** — agents need HR-like maturity, not IT-like maturity
5. **10% non-human identity strategy (WEF)** — even basic identity management is absent
6. **Gartner's own prediction: >40% agentic projects canceled by 2027** — the maturity gap will kill projects
7. **The self-assessment gap:** no tool exists for a CTO to assess agent readiness in 5 minutes
8. **Cloud Maturity precedent:** "what to do next" is more valuable than "where you are"

---

## PART 5: THE AI AGENT MATURITY MODEL — 5 Levels

### Design Principles (from CMMI + DORA)
1. **Outcome-based:** Measure what agents DO, not what tools you bought
2. **Prescriptive:** Each level tells you WHAT TO DO NEXT
3. **Measurable:** Max 5 criteria per level, each binary (yes/no) or quantifiable
4. **Self-assessable:** A CTO can place their org in <5 minutes
5. **Progressive:** You can't skip levels (Level 3 requires Level 2 foundations)

### The 5 Agent Maturity Dimensions (scored per level)

| Dimension | What It Measures |
|---|---|
| **A — Autonomy** | How independently agents operate |
| **G — Governance** | Policies, audit trails, compliance |
| **E — Error Handling** | Calibration, failure recovery, graceful degradation |
| **N — Networked Trust** | Inter-agent trust, identity, orchestration |
| **T — Team Integration** | Human-agent collaboration, HITL design |

**(AGENT — the acronym)**

---

### Level 1: Ad Hoc — "The Playground"

**Description:** Individual employees experiment with AI agents. No organizational strategy. Agents are glorified chatbots with tool access.

**Criteria:**
- [ ] Agents used by individuals, not teams
- [ ] No shared prompts, no version control on agent configs
- [ ] No observability — you don't know what agents did yesterday
- [ ] No defined escalation path (agent → human)
- [ ] Agent credentials = personal API keys

**Typical Mistakes:**
- Treating ChatGPT/Claude with tool use as "having agents"
- Demo-driven adoption: "Look what it can do!" without "What happens when it fails?"
- No incident tracking for agent errors

**Example:** A dev team uses Cursor + Claude for code generation. Each developer has their own prompts. Nobody tracks hallucination rates. When an agent-generated bug hits production, it's logged as a human bug.

**What's Missing to Reach Level 2:** Centralized visibility into what agents are doing.

---

### Level 2: Managed — "The Dashboard"

**Description:** Organization has visibility into agent activities. Basic guardrails exist. Agents are tracked, but trust is binary (on/off).

**Criteria:**
- [ ] Centralized agent observability (logs, traces, costs)
- [ ] Defined use cases: which tasks agents MAY perform
- [ ] Basic input/output validation (guardrails)
- [ ] Agent inventory: you know how many agents you run
- [ ] Incident tracking for agent failures (separate from human errors)

**Typical Mistakes:**
- Observability without action: dashboards nobody checks
- Guardrails as afterthought: bolted on after incidents
- Confusing agent monitoring with agent governance
- "We have LangSmith/Langfuse" ≠ "We manage our agents"

**Example:** A fintech deploys customer service agents via CrewAI. They track all conversations in Langfuse. They know cost per interaction ($0.35). But when an agent hallucinates a refund policy, nobody catches it until a customer complains on Twitter.

**What's Missing to Reach Level 3:** Confidence scoring and calibrated trust.

---

### Level 3: Calibrated — "The Trust Layer"

**Description:** Agents have measurable confidence. Outputs are calibrated. HITL is designed (not just required). Agent identity is managed.

**Criteria:**
- [ ] Confidence scoring on agent outputs (calibrated, not self-reported)
- [ ] HITL triggers based on confidence thresholds (not random sampling)
- [ ] Agent identity management: dedicated credentials, not personal keys
- [ ] Defined SLAs for agent reliability (e.g., <2% hallucination rate)
- [ ] Memory governance: agents don't accumulate unchecked context

**Typical Mistakes:**
- Using verbalized confidence (VCE) instead of calibrated methods — VCE is "systematically biased" (arXiv:2602.00279)
- HITL without severity tiering → alert fatigue (67% ignored, Vectra 2023)
- Memory without provenance: agent "remembers" things nobody verified
- Setting SLAs without measurement infrastructure

**Example:** An insurance company runs claims processing agents. Each output has a Budget-CoCoA confidence score ($0.005/check). Claims below 85% confidence auto-escalate to a human reviewer. The reviewer sees context (why the agent is uncertain), not just "please review." Agent credentials are managed via Microsoft Entra Agent ID.

**What's Missing to Reach Level 4:** Multi-agent orchestration with inter-agent trust.

---

### Level 4: Orchestrated — "The Network"

**Description:** Multiple agents collaborate with defined trust relationships. Delegation, escalation, and inter-agent verification are systematic. Agents can challenge each other.

**Criteria:**
- [ ] Multi-agent workflows with defined delegation rules
- [ ] Inter-agent trust scoring: Agent A knows how reliable Agent B is
- [ ] Automated escalation chains (agent → agent → human)
- [ ] Audit trail across agent interactions (not just per-agent)
- [ ] Adversarial testing: regular red-teaming of agent systems

**Typical Mistakes:**
- Orchestration without trust: agents blindly pass outputs to each other (MAS hijacking: 45-64% success, arXiv:2503.12188)
- No cross-agent audit trail: you see what each agent did, but not the chain
- Skipping adversarial testing: "our agents work well in demos"
- Memory poisoning across agents: one compromised memory infects the network (MINJA >95%, arXiv:2503.03704)

**Example:** A logistics company runs a multi-agent system: demand forecasting agent → inventory optimization agent → procurement agent. Each agent's output includes a confidence score. The procurement agent won't execute orders above $50K unless the forecasting agent's confidence exceeds 90% AND the optimization agent independently confirms. Weekly red-team exercises test for prompt injection and memory poisoning.

**What's Missing to Reach Level 5:** Autonomous adaptation and self-improvement.

---

### Level 5: Autonomous — "The Organism"

**Description:** Agent systems self-monitor, self-improve, and adapt. Human oversight is strategic (goals, boundaries), not tactical (individual decisions). The system learns from failures and adjusts autonomy boundaries automatically.

**Criteria:**
- [ ] Agents adjust their own confidence thresholds based on historical accuracy
- [ ] Automatic capability expansion/contraction based on performance
- [ ] Self-healing: agent systems detect and recover from failures without human intervention
- [ ] Continuous calibration: trust scores update based on real outcomes
- [ ] Regulatory compliance automated: audit trails meet EU AI Act / NIST standards by design

**Typical Mistakes:**
- Premature autonomy: jumping to Level 5 without Level 3-4 foundations
- No kill switch: autonomous systems without human override capability
- Optimizing for speed instead of reliability
- Assuming self-improvement = improvement (it can also mean self-reinforcing bias)

**Example:** Nobody is here yet. This is the target state. Closest analog: Waymo's autonomous driving system — continuous learning from real-world data, automated edge case detection, progressive autonomy expansion based on safety metrics. But even Waymo had a 1,212-unit recall.

**Reality Check:** Level 5 is aspirational for 2026-2028. Organizations should aim for Level 3 as the near-term target.

---

## PART 6: SELF-ASSESSMENT QUICK TEST

**For a CTO to score their org in 5 minutes:**

| # | Question | Yes = this level achieved |
|---|---|---|
| 1 | Do you know how many AI agents your organization runs? | Level 2 |
| 2 | Can you tell me the error rate of your agents last month? | Level 2 |
| 3 | Do your agents have confidence scores on their outputs? | Level 3 |
| 4 | Are those confidence scores calibrated (not self-reported)? | Level 3 |
| 5 | Do your agents have dedicated identity/credentials (not personal API keys)? | Level 3 |
| 6 | When Agent A passes output to Agent B, does B verify it? | Level 4 |
| 7 | Do you have a cross-agent audit trail? | Level 4 |
| 8 | Do you red-team your agent systems at least quarterly? | Level 4 |
| 9 | Do your agents automatically adjust their autonomy based on performance? | Level 5 |
| 10 | Does your agent system self-heal from failures without human intervention? | Level 5 |

**Scoring:** Your level = highest level where ALL questions are answered "Yes."

**Prediction:** 80%+ of organizations answering honestly will score Level 1.

---

## PART 7: OUTLINE — Report Structure

### Section 1: The Maturity Illusion (1,000 words)
- Open with the gap: 62% experiment, <10% enterprise-wide, 6% see EBIT impact
- Existing maturity models measure AI-as-tool, not AI-as-actor
- Thesis: "Most organizations think they're at Level 3. They're at Level 1."
- Why this matters: >40% agentic projects will be canceled by 2027 (Gartner)

### Section 2: Why Existing Models Fail for Agents (1,200 words)
- Quick tour: Gartner (4 levels), McKinsey (3 tiers), Deloitte, Microsoft, IBM
- The common blind spot: none measure autonomy, trust, memory, orchestration
- The "governance of actors" vs "management of tools" distinction
- What CMMI and DORA got right that AI maturity models got wrong

### Section 3: The AGENT Framework — 5 Dimensions (800 words)
- Introduce the 5 dimensions: Autonomy, Governance, Error Handling, Networked Trust, Team Integration
- Why these 5 (derived from research: overconfidence, adversarial attacks, HITL failure, memory poisoning, identity gaps)
- How to read the model

### Section 4: The 5 Levels — Detailed (2,500 words)
- Level 1: Ad Hoc — "The Playground"
- Level 2: Managed — "The Dashboard"
- Level 3: Calibrated — "The Trust Layer"
- Level 4: Orchestrated — "The Network"
- Level 5: Autonomous — "The Organism"
- Each level: description, criteria (5 binary), typical mistakes, example, what's missing

### Section 5: The 5-Minute Self-Assessment (600 words)
- 10-question diagnostic
- Scoring methodology
- "If you said yes to question 1 but no to question 2, you're at Level 1"
- The honesty problem: why organizations over-rate themselves

### Section 6: The Level 1 → Level 3 Playbook (1,200 words)
- Practical steps: what to do first
- Cost: $0.005/check for calibration vs $7.5B for failure
- Timeline: 3-6 months for Level 2, 6-12 months for Level 3
- What to STOP doing (removing false confidence is step 1)

### Section 7: Why Level 3 Is the Real Goal for 2026 (800 words)
- EU AI Act enforcement Aug 2026 requires Level 3 minimum
- Level 5 is aspirational, Level 3 is survival
- The regulatory trilemma: deploy fast vs deploy compliant vs don't deploy
- Insurance angle: AIUC and the coming market for agent liability

### Section 8: Predictions (600 words)
- >$100M agent catastrophe in 12 months (55% confidence)
- Agent Maturity assessments become procurement requirement by 2027
- Level 3 becomes table stakes for enterprise AI by 2028
- The "DORA for Agents" moment: when benchmarking creates industry pressure

**Total: ~8,700 words / 8 sections**

---

## CLAIM REGISTER

| # | Claim | Value | Source | Confidence | Used In |
|---|---|---|---|---|---|
| 1 | Only 6% are AI High Performers | 6% (n=1,993) | McKinsey State of AI 2025 | **High** | S1, S2 |
| 2 | 62% experiment with agents, <10% enterprise-wide | 62% / <10% | McKinsey 2025 | **High** | S1, S5 |
| 3 | >40% agentic projects canceled by 2027 | >40% | Gartner 2025 | **Medium** | S1, S7 |
| 4 | 54% of AI projects move pilot→production | 54% | Gartner 2024 | **Medium** | S1 |
| 5 | LLM overconfidence rate | 84% (9 models, 351 scenarios) | PMC/12249208 | **High** | S3, S4 |
| 6 | VCE is systematically biased | Confirmed | arXiv:2602.00279 | **High** | S4 (L3) |
| 7 | Budget-CoCoA cost | $0.005/check | Anthropic pricing (verified) | **High** | S4 (L3), S6 |
| 8 | SOC alerts ignored | 67% | Vectra 2023 (2,000 analysts) | **High** | S4 (L3) |
| 9 | MAS hijacking success rate | 45-64% | arXiv:2503.12188 | **High** | S4 (L4) |
| 10 | Memory injection success (MINJA) | >95% | arXiv:2503.03704 | **High** | S4 (L4) |
| 11 | All prompt injection defenses broken | 12/12 | arXiv:2510.09023 | **High** | S4 (L4) |
| 12 | VW Cariad loss | $7.5B | VW public filing | **High** | S6 |
| 13 | EU AI Act max penalty | €35M / 7% revenue | Legislative text | **High** | S7 |
| 14 | Orgs with non-human identity strategy | 10% | WEF 2025 | **Medium** | S4 (L3) |
| 15 | Agent credential leaks | 23% of IT pros report | Okta | **Medium** | S4 (L3) |
| 16 | CMMI: 5 levels, 1987-present | Verified | Carnegie Mellon/ISACA | **High** | S2 |
| 17 | DORA: 4 metrics, 4 tiers | Verified | Google DORA Research | **High** | S2 |
| 18 | 40% enterprise apps will have agents by 2026 | 40% | Gartner | **Medium** | S1 |
| 19 | Klarna: $60M saved, then "overpivoted" | $60M | CEO earnings call | **High** | S6 |
| 20 | 94% of prod agent devs use observability | 94% | LangChain report | **Medium** | S4 (L2) |
| 21 | Agent market: $7.8B → $52B by 2030 | 45.8% CAGR | Precedence Research | **Medium** | S1 |
| 22 | Healthcare false positive rate | 80-99% | PMC6904899 | **High** | S4 (L3) |

---

## SOURCE LIST (22 Sources)

### From Research Pack (verified)
1. PMC/12249208 — LLM overconfidence study (9 models, 351 scenarios)
2. arXiv:2602.00279 — VCE calibration bias (Jan 2026)
3. arXiv:2510.09023 — Meta "Rule of Two" (12/12 defenses broken)
4. arXiv:2503.12188 — MAS Hijacking (45-64%)
5. arXiv:2503.03704 — MINJA memory injection (>95%)
6. Vectra 2023 — SOC alert fatigue (2,000 analysts)
7. McKinsey State of AI 2025 — (n=1,993)
8. LangChain State of Agent Engineering — observability adoption
9. WEF 2025 — non-human identity strategy
10. Okta — agent credential leaks
11. EU AI Act — legislative text
12. VW Geschäftsberichte — Cariad losses
13. Anthropic/OpenAI pricing — verified API costs
14. Gartner 2024/2025 — AI maturity, agent projections
15. Precedence Research — agent market CAGR

### New Sources (this research)
16. Wikipedia/CMMI — Capability Maturity Model Integration history and structure
17. DORA Research Program (dora.dev) — Core Model, 4 key metrics
18. "Accelerate" (Forsgren, Humble, Kim) — DevOps maturity research
19. Deloitte "State of AI in the Enterprise" 7th edition (2024) — enterprise AI survey
20. Microsoft AI Maturity Assessment Tool (2024) — 5-level framework
21. Google Cloud AI Maturity themes (2025-2026) — Agent Trust as key theme
22. IBM AI Ladder — 4-rung data-centric model

---

## BEIPACKZETTEL

- **Confidence:** 75%
- **Strongest element:** The maturity model itself — synthesized from CMMI + DORA patterns applied to agent-specific dimensions from 15 research briefs
- **Weakest element:** Level 5 examples — nobody is there yet, making it speculative
- **What would invalidate this:** If a major consultancy (McKinsey, Gartner) publishes an agent-specific maturity model before this report ships, the novelty claim weakens significantly
- **Bias warning:** The model is designed to make organizations feel behind (Level 1). This is intentional — but honest. The data supports it.
- **Search API limitation:** Brave Search quota exhausted during this session. Additional sources fetched via direct URL. Some Gartner/McKinsey content behind paywalls — used publicly available data points.
- **Missing:** Formal validation of the model against real enterprises. This is a proposed framework, not an empirically tested one. CMMI took years of validation. We're proposing the hypothesis.

---

*Research complete. Ready for WRITER agent to draft report sections from this outline + claim register.*
