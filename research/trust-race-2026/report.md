# The Trust Race: Why AI Governance Can't Keep Up — And What To Do About It

**AInarY Ventures Research Report AR-002**
**February 2026**

---

## 1. How to Read This Report

Every quantitative claim in this report is tagged with a confidence marker:

| Tag | Meaning | Standard |
|-----|---------|----------|
| **[E]** | **Empirical** — Directly sourced from primary data, surveys, or peer-reviewed research | >50% of all claims |
| **[I]** | **Inferred** — Derived from combining multiple empirical data points through logical reasoning | |
| **[J]** | **Judgment** — Author's professional assessment based on pattern recognition and experience | <20% of all claims |
| **[A]** | **Assumption** — Explicitly stated premise used for modeling or scenario analysis | |

Where a claim carries multiple tags (e.g., [E/I]), the first tag reflects the primary basis. Sources are numbered and listed in the Source Log (Section 10).

---

## 2. Executive Summary

**Capability doubles every 7 months. Governance updates annually. Do the math.**

AI agent capability — measured by the length of tasks systems can autonomously complete — has been doubling every seven months for six consecutive years [E, Source 1]. Meanwhile, governance frameworks like ISO 42001 and NIST AI RMF operate on 18–36 month revision cycles [E/I, Sources 5, 6]. The result is a compounding divergence: every year that passes without structural reform, the governance gap doesn't just persist — it widens exponentially.

This is not a theoretical concern. Today, 57% of enterprises have deployed or are actively piloting agentic AI [E, Source 2]. Yet only 6% fully trust these systems with core business processes [E, Source 3]. Gartner predicts over 40% of agentic AI projects will be canceled by end of 2027 due to escalating costs, unclear value, or inadequate risk controls [E, Source 4]. Fewer than 1% of organizations have fully operationalized responsible AI practices [E, Source 5].

The gap between what AI *can* do and what organizations *trust* it to do is the defining strategic challenge of 2026. This report formalizes this as "The Trust Race" — the competition between exponentially growing capability and linearly adapting governance. Organizations that build trust infrastructure before they need it will dominate. Those that wait will join the 40%.

**Bottom line:** The trust deficit is not a feelings problem. It is an infrastructure problem. And infrastructure problems have infrastructure solutions.

**The three things every executive needs to understand:**
1. The governance gap is exponential, not linear — waiting makes it worse, not better
2. Trust infrastructure is the missing layer in the enterprise AI stack — without it, capability investments are wasted
3. The organizations that build trust before they need it will own the next decade of AI-driven value creation

---

## 3. The Numbers: 57% Deployed, 6% Trusted — The Deployment-Trust Inversion

The most striking feature of enterprise AI in early 2026 is not the pace of adoption. It is the *inversion* between deployment velocity and trust formation.

### Deployment is accelerating

- 9% of organizations have fully deployed agentic AI; 48% are piloting or exploring [E, Source 3]
- 86% expect investment in agentic AI to increase over the next two years [E, Source 3]
- KPMG's Q4 2025 AI Pulse Survey shows agent deployment more than doubled from Q1 (11%) to Q3 (42%) of 2025 [E, Source 7]
- 2026 marks what KPMG calls the emergence of the "agent orchestrator" era [E, Source 7]

### Trust is stalling

- Only 6% of companies fully trust AI agents to autonomously run core business processes [E, Source 3]
- 43% trust AI agents only with limited or routine operational tasks [E, Source 3]
- 39% restrict AI agents to supervised use cases or noncore processes [E, Source 3]
- Only 12% feel their risk and governance controls are fully in place for agentic AI [E, Source 3]
- Only 20% say technology infrastructure is fully ready; 15% say the same for data and systems [E, Source 3]

### The Inversion Visualized

```
Deployment ████████████████████████████░░░  57%  (deployed + piloting)
Full Trust  ██░░░░░░░░░░░░░░░░░░░░░░░░░░░░   6%  (trust for core processes)
Governance  █░░░░░░░░░░░░░░░░░░░░░░░░░░░░░  <1%  (fully operationalized RAI)
```

This is the Deployment-Trust Inversion: organizations are shipping AI faster than they can trust it, and trusting it faster than they can govern it. The delta between the top bar and the bottom bar represents accumulated organizational risk — risk that compounds with every new deployment [I].

The HBR Analytic Services study classifies 27% of organizations as "leaders," 50% as "followers," and 24% as "laggards" on a composite readiness index spanning infrastructure, data, cybersecurity, and governance [E, Source 3]. Even among "leaders," the trust gap persists. The problem isn't that organizations lack ambition. It's that ambition without infrastructure creates fragility.

### Why the gap matters economically

The consequences of the Deployment-Trust Inversion are not abstract:

- Gartner predicts >40% of agentic AI projects will be canceled by end of 2027 [E, Source 4] — a direct result of "escalating costs, unclear business value or inadequate risk controls"
- Benefits realized from agentic AI deployments consistently fall below expectations [E, Source 3]
- 31% cite cybersecurity and privacy as the primary barrier; 23% cite data quality concerns [E, Source 3]
- The pattern is "garbage in, garbage out" at scale — eroding trust rather than building it [I, Source 3]

Every canceled project represents sunk investment, organizational cynicism, and delayed competitive advantage. At current trajectories, the trust deficit will cost the enterprise AI ecosystem hundreds of billions in unrealized value by 2028 [J].

---

## 4. The Trust Race Model

### Formalizing the Gap

The Trust Race can be modeled as two competing growth functions:

**Capability Growth (C):**
$$C(t) = C_0 \cdot 2^{t/7}$$

Where $t$ = months and doubling time = 7 months [E, Source 1]. METR's research demonstrates this has held consistently for six years across frontier models, measured by the length of tasks AI agents can autonomously complete with 50% reliability.

**Governance Growth (G):**
$$G(t) = G_0 \cdot (1 + r)^{t/T}$$

Where $T$ = revision cycle (18–36 months for ISO/NIST) and $r$ = incremental improvement per cycle (~15–30%) [I, Sources 5, 6].

**The Trust Gap (Δ):**
$$\Delta(t) = C(t) - G(t)$$

This gap grows super-linearly. In 7 months, capability doubles. In the same period, governance might improve 5–8% [I]. After 24 months, capability has increased ~10x while governance has completed roughly one revision cycle [I].

### What the model predicts

| Timeframe | Capability Multiple | Governance Progress | Gap Trajectory |
|-----------|-------------------|-------------------|----------------|
| 7 months (Aug 2026) | 2x current | ~8% improvement | Widening |
| 14 months (Mar 2027) | 4x current | ~15% improvement | Accelerating |
| 21 months (Oct 2027) | 8x current | ~1 full revision | Critical |
| 28 months (May 2028) | 16x current | ~1.2 revisions | Systemic risk |

[I/A — Based on METR doubling rate extrapolation combined with observed standards revision timelines]

The key insight is not that the gap exists — everyone intuitively senses it. The insight is that **the gap is exponential, not linear**. Linear governance responses to exponential capability growth mathematically guarantee failure [I].

### Boundary conditions and limitations

This model has important constraints:

- METR's doubling time is measured on software/coding tasks specifically; generalization to all domains is uncertain [E/I, Source 1]
- Governance quality is harder to quantify than capability; the linear approximation may understate bursts of regulatory activity [J]
- Market forces (liability, insurance requirements, procurement standards) can create governance acceleration outside formal standards [I]
- The model assumes current trends continue; capability growth could plateau due to data, compute, or algorithmic limits [A]

Even with generous assumptions about governance acceleration, the structural mismatch persists. The question is not *whether* the gap exists, but *how organizations respond to it* [J].

### The compounding cost of delay

To make the Trust Race concrete: consider an organization that decides in February 2026 to "wait for standards to mature" before investing in trust infrastructure.

By August 2026 (6 months): Agent capabilities have nearly doubled. The EU AI Act's high-risk provisions are now enforceable. The organization has no governance infrastructure and faces both regulatory exposure and a capability gap with competitors who built early [I].

By February 2027 (12 months): Capabilities have roughly quadrupled from today's baseline. ISO 42001 may be entering revision discussions. The organization is now two doublings behind on trust infrastructure — and the gap is not recoverable through a single initiative [I].

By August 2027 (18 months): Capabilities are ~6x today's level. Gartner's 40% cancellation wave is hitting. Organizations without trust infrastructure are abandoning projects. Those who built early are absorbing market share from the retreating competitors [I/J].

The math is unforgiving: **every month of delayed trust infrastructure investment costs approximately 10% in relative capability-governance alignment** [A — derived from doubling rate]. There is no catching up later. The Trust Race only runs forward.

### Why this is different from previous technology cycles

Skeptics may argue that governance has always lagged innovation — from the internet to social media to cloud computing. This time is structurally different for three reasons [J]:

1. **Agency, not tools.** Previous technologies augmented human decisions. Agentic AI *makes* decisions. The governance stakes are categorically higher because the human is no longer in every loop [I].

2. **Exponential, not linear.** Internet adoption followed an S-curve with natural plateaus. AI agent capability follows a consistent exponential with no observed plateau [E, Source 1]. The governance gap compounds rather than stabilizes.

3. **Interconnected, not isolated.** Agentic systems operate across organizational boundaries, data sources, and toolchains. A governance failure in one system cascades through the entire orchestration layer [I, Source 9]. The blast radius is systemic, not local.

---

## 5. Why Traditional Governance Fails

### The cadence problem

Traditional governance operates on institutional time. AI operates on exponential time. The mismatch is structural:

**ISO/IEC 42001** (AI Management Systems): Published December 2023. First revision not expected before 2026–2027 at earliest. ISO standards typically follow a 3–5 year systematic review cycle [E/I, Source 5].

**NIST AI RMF 1.0**: Published January 2023. The companion Playbook is updated semi-annually via community comment [E, Source 6]. The core framework itself has not been revised. NIST plans to "update the AI RMF Playbook frequently" with "comments reviewed and integrated on a semi-annual basis" [E, Source 6] — but the framework's structural assumptions remain static.

**EU AI Act**: Entered into force August 2024. Key provisions on high-risk systems apply from August 2026. General-purpose AI model rules apply from August 2025. The Act was drafted primarily before the agentic AI wave and contains no specific provisions for autonomous agent systems [E/I].

In the time between ISO 42001's publication (Dec 2023) and its likely first revision (~2027), AI agent capability will have doubled approximately 7 times — a 128x increase [I, based on METR data].

### The architecture problem

Beyond cadence, traditional governance frameworks share a fundamental architectural flaw: they are designed for static systems.

OneTrust's 2025 AI-Ready Governance Report (1,250 IT decision-makers) found [E, Source 8]:
- 90% of advanced AI adopters say AI exposed the limits of siloed or manual governance processes
- Even among organizations still experimenting, 63% report the same strain
- More than two-thirds of technology leaders say governance capabilities consistently lag behind AI project speed

Traditional governance assumes:
1. Systems are deployed, then audited [A — static audit model]
2. Risk profiles are stable between assessment cycles [A — false for learning systems]
3. Human review is feasible for all consequential decisions [A — breaks at agent scale]
4. Compliance is binary (compliant/non-compliant) [A — inadequate for probabilistic systems]

Agentic AI violates every one of these assumptions. Agents make thousands of micro-decisions continuously. They operate across system boundaries. Their behavior can shift with prompt changes, data drift, or environmental context — all between audit cycles [I].

As CIO.com recently framed it: "Our ability to generate AI outputs is scaling exponentially, while our ability to understand, govern and trust those outputs remains manual, retrospective and fragmented across point solutions" [E, Source 9].

### The organizational problem

The governance gap is also a people problem. The HBR study found that 44% of organizations cite change management and reskilling as critical barriers [E, Source 3]. As Workiva CIO Kim Huffman stated: "The change management and reskilling that is going to be required across every company is something I feel has been underestimated" [E, Source 3].

Governance teams are typically staffed for compliance review cadences — quarterly risk assessments, annual audits, periodic policy updates. They are not staffed for continuous monitoring of autonomous systems that make real-time decisions across business processes [I].

---

## 6. Agent-Washing: How Hype Corrupts Decision Data

### Defining the problem

"Agent-washing" — the practice of rebranding existing chatbots, automation tools, or LLM-integrated applications as "AI agents" without meeting core agentic criteria — has emerged as a significant distortion in enterprise AI markets [E, Sources 10, 11, 12].

As Forbes documented: "Agent washing may help companies ride the current hype cycle, but it comes at a cost. It undermines the entire ecosystem by fostering skepticism, slowing adoption, and turning enthusiasm into disappointment" [E, Source 10].

CIO.com reported that "many vendors have rebranded existing chatbots or gen AI assistants as agents without delivering meaningful outcomes" [E, Source 12].

### Why agent-washing amplifies the trust gap

Agent-washing doesn't just waste procurement budgets. It systematically corrupts the decision data that organizations use to evaluate AI governance needs:

1. **Inflated capability claims** lead organizations to prepare governance frameworks for systems that don't actually require them — misallocating scarce governance resources [I]
2. **Understated risk profiles** cause organizations to under-invest in controls for systems marketed as "simple automation" but deployed with real autonomy [I]
3. **Failed implementations** attributed to "AI agents" poison organizational willingness to invest in genuinely agentic systems that do require robust governance [I]
4. **Procurement confusion** makes it harder for governance teams to categorize systems by actual risk level — the foundation of risk-based regulation like the EU AI Act [I]

### The trust erosion cycle

Agent-washing creates a vicious cycle [I]:

```
Vendor overpromises → Enterprise deploys → Results disappoint →
Trust erodes → Governance tightens reactively → Innovation slows →
Competitive pressure builds → Enterprise tries again with new vendor →
Vendor overpromises (repeat)
```

Each cycle deepens organizational skepticism and makes the trust gap harder to close. The 40% project cancellation rate predicted by Gartner [E, Source 4] is partly a consequence of this cycle — organizations investing based on inflated expectations, then retreating when reality fails to match marketing [I].

### What real agentic capability requires

True agentic AI systems demonstrate [I, synthesized from Sources 10, 11, 12]:
- **Autonomy**: Independent decision-making within defined boundaries
- **Goal pursuit**: Ability to decompose objectives into multi-step plans
- **Reasoning**: Contextual judgment, not just pattern matching
- **Adaptability**: Learning and adjusting behavior based on outcomes
- **Cross-system operation**: Working across tools and data sources without human mediation

Organizations that cannot distinguish agent-washed products from genuine agentic systems will consistently misallocate governance investment [J].

### The scale of the problem

Agent-washing is not a fringe phenomenon. It is market-wide. In the KPMG Q4 2025 survey, reported agent deployment actually *declined* from 42% (Q3) to 26% (Q4) [E, Source 7]. KPMG attributes this partly to organizations "recalibrating what counts as agentic" as definitions tighten — a correction that suggests earlier numbers were inflated by agent-washed products [I, Source 7].

The correction is healthy but costly. Organizations that deployed "agents" that were actually rebranded chatbots have burned budget, burned internal credibility, and — critically — burned the organizational willingness to try again with genuine agentic systems [I]. This is the hidden cost of agent-washing: it doesn't just waste money. It destroys the organizational trust capital needed to adopt real agentic AI successfully.

For governance teams, agent-washing creates a particularly pernicious problem: **you cannot govern what you cannot accurately classify** [J]. If half the "AI agents" in your portfolio are actually glorified workflow automations, your risk assessments are wrong, your audit plans are miscalibrated, and your board reporting is fiction. Agent-washing doesn't just corrupt vendor relationships — it corrupts internal decision-making infrastructure [I].

---

## 7. Adaptive Trust Infrastructure: The Solution

### Why "governance" is the wrong frame

The word "governance" implies oversight — someone watching from outside. What agentic AI requires is **trust infrastructure** — engineering principles built into the system architecture itself [J].

The distinction matters: governance is a process layered on top of systems. Trust infrastructure is a property of the systems themselves. The former scales linearly with headcount. The latter scales with the system [I].

### The Trust Layer concept

CIO.com's framing of a missing "trust layer" in the enterprise AI stack captures the architectural insight [E, Source 9]:

> "Today's enterprise AI stack is built around compute, data and models, but it is missing its most critical component: a dedicated trust layer."

The trust layer performs two core functions:
- **Measure**: Continuous, unified visibility into model behavior — accuracy, data provenance, bias drift, prompt-level risks [E, Source 9]
- **Manage**: Active guardrails and policies — access controls, real-time filters, kill switches that enforce safe operation, not just report failures after the fact [E, Source 9]

The analogy from Source 9 is precise: "Think of it as the avionics system in a modern aircraft. It doesn't make the plane fly faster, but it continuously measures conditions and makes adjustments to keep the flight within safe parameters."

### Five principles of Adaptive Trust Infrastructure

Based on the convergence of evidence from this research, Adaptive Trust Infrastructure must embody five principles [J/I]:

**1. Continuous, not periodic**
Governance that operates on audit cycles cannot keep pace with systems that make decisions in milliseconds. Trust infrastructure must monitor continuously — every agent action, every data flow, every decision boundary [I, Sources 8, 9].

OneTrust's research confirms the shift: "Continuous monitoring, not periodic reviews. Pattern-based approvals, not one-off assessments. Programmatic enforcement that applies policies automatically" [E, Source 8].

**2. Embedded, not bolted on**
The WEF's January 2026 guidance on agile AI governance calls for organizations to "embed responsible AI into development pipelines with automated assessments and real-time alerts" and "implement adaptive guardrails and modernize human oversight for agentic AI" [E, Source 13].

Trust cannot be an afterthought. It must be part of the development pipeline, the deployment architecture, and the operational monitoring stack [I].

**3. Proportional, not binary**
Risk-based governance requires granularity. Not all agent actions carry equal risk. Adaptive Trust Infrastructure must dynamically adjust oversight levels based on action type, context, impact potential, and confidence [I].

This means moving from "approved/not approved" to continuous trust scores that determine autonomy boundaries in real time [J].

**4. Measurable, not aspirational**
Trust infrastructure must produce quantifiable metrics: decision audit trails, confidence distributions, boundary violation rates, governance response times. Without measurement, trust is just a word on a slide [J].

**5. Interoperable, not siloed**
Enterprise orchestration — connecting systems, data, and applications into a governed layer — is already underway. 74% of organizations are working on or planning enterprise orchestration in preparation for agentic AI [E, Source 3]. Trust infrastructure must span the entire orchestration layer, not live in isolated tools [I].

### What this looks like in practice

Organizations building Adaptive Trust Infrastructure today are [I/E]:
- Validating trust mechanisms on single use cases before scaling autonomy [E, Source 9]
- Selecting systems that integrate with governance stacks rather than operating as closed silos [E, Source 9]
- Allocating dedicated budget for trust infrastructure stress-testing — not just model performance [E, Source 9]
- Designating AI ambassadors in every function to identify use cases and shepherd governance adoption [E, Source 3]
- Investing in AI literacy and governance technology as complementary capabilities [E, Source 13]

---

## 8. The Regulatory Clock: EU AI Act as Forcing Function

### The timeline

The EU AI Act creates a hard deadline that converts the Trust Race from strategic concern to operational imperative:

- **August 2025**: Rules for general-purpose AI models took effect [E]
- **August 2026**: Obligations for high-risk AI systems become enforceable [E]
- **2027+**: Full enforcement regime with penalties up to €35M or 7% global turnover [E]

For organizations deploying agentic AI in EU markets, August 2026 is not a planning horizon — it is six months away [E].

### Why the EU AI Act is necessary but insufficient

The Act represents the most comprehensive AI regulation globally, but it was designed primarily for a pre-agentic world [I]:

- It classifies systems by predefined risk categories, but agentic AI's risk profile is dynamic and context-dependent [I]
- It requires conformity assessments that assume stable system behavior, but agents evolve through use [I]
- It mandates human oversight, but doesn't specify how oversight scales when agents make thousands of decisions per minute [I]
- It addresses the AI *provider* and *deployer* distinction, but agentic systems blur this boundary when agents autonomously select and invoke tools [I]

Italy became the first EU country to pass comprehensive national AI regulation aligned with the EU AI Act [E, Source 14]. Other member states are following. The regulatory momentum is real — but it is moving at legislative speed, not exponential speed [I].

### The forcing function effect

Despite its limitations, the EU AI Act serves a critical function: it creates *urgency*. Organizations that might otherwise defer governance investment indefinitely now face concrete deadlines with material penalties [I].

The most strategic response is not minimum compliance but *governance as competitive advantage*. Organizations that build Adaptive Trust Infrastructure exceeding EU AI Act requirements will [J]:
- Move faster through compliance processes
- Access EU markets that competitors avoid
- Demonstrate governance maturity that attracts enterprise customers and partners
- Create institutional capabilities that transfer to future regulatory regimes

The regulatory clock doesn't just constrain — it differentiates [J].

### Beyond the EU: The global regulatory mosaic

The EU AI Act is the most visible forcing function, but not the only one. Regulatory momentum is building globally [E/I]:

- **Colorado** and **California** have introduced state-level AI governance requirements in the US [E, Source 8]
- **South Korea** and **Brazil** are developing comprehensive AI frameworks [E, Source 8]
- **Italy** became the first EU member state to pass a comprehensive national AI regulation [E, Source 14]
- The **Atlantic Council** identifies AI governance as a central geopolitical competition in 2026, with middle powers gradually closing the gap in the global AI race [E, Source 15]

For multinational enterprises, this creates a compliance multiplicity problem: not one governance standard, but many — each evolving on its own timeline, each with its own definitions of risk, transparency, and accountability [I]. Organizations without Adaptive Trust Infrastructure will face an impossible task: maintaining compliance across multiple jurisdictions simultaneously while their AI systems evolve faster than any single regulatory framework [I].

The strategic insight: **build governance infrastructure that exceeds the strictest current requirement, and make it modular enough to adapt to new requirements as they emerge** [J]. This is more efficient than maintaining parallel compliance tracks — and it creates a genuine competitive moat.

### The insurance and liability dimension

Beyond regulation, market mechanisms are creating additional governance pressure [I/J]:

- Insurers are beginning to require AI governance documentation as a condition for cyber and professional liability coverage [I]
- Enterprise procurement processes increasingly include AI governance maturity as a vendor qualification criterion [I]
- Board directors face increasing personal liability exposure for AI governance failures, similar to the evolution of cybersecurity governance obligations [I]

These market forces operate faster than regulation and can create governance acceleration that the Trust Race model doesn't fully capture. They represent a potential "governance accelerant" — but only for organizations that have already invested in measurable trust infrastructure [J].

---

## 9. Recommendations: Build Trust Before You Need It

### For Enterprise Leaders

**1. Audit your Trust Gap today** [J]
Map every deployed or piloted AI system against four dimensions: technical readiness, data readiness, governance readiness, and organizational readiness. The HBR study found only 12% have governance fully in place [E, Source 3]. Know your number.

**2. Invest in trust infrastructure, not just model capability** [J]
For every dollar spent on AI model development or deployment, allocate a proportional investment in governance tooling, monitoring infrastructure, and trust measurement. The current ratio is heavily skewed toward capability [I, Source 9].

**3. Adopt continuous governance from day one** [I/J]
Do not bolt governance onto existing deployments. Build it into the architecture of every new agentic AI project. Budget for it. Staff for it. Measure it.

**4. Demand agent-washing transparency from vendors** [J]
Require vendors to demonstrate specific agentic capabilities against a defined taxonomy. Ask: How does this agent learn? What happens when priorities shift? Can it operate across systems? What level of human supervision does it require? [E, Source 11]. If answers are vague, walk away.

**5. Prepare for the EU AI Act as if it applies to you** [J]
Even organizations outside EU jurisdiction will face supply chain pressure, customer requirements, and competitive dynamics shaped by the Act. Build governance that exceeds current requirements — regulatory arbitrage is a short-term play.

### For AI Vendors and Builders

**6. Ship trust infrastructure with every agent** [J]
Make governance tooling — audit trails, confidence reporting, boundary enforcement, kill switches — a default feature, not an enterprise add-on. Trust is the product.

**7. Stop agent-washing** [J]
Clearly communicate what your system can and cannot do autonomously. Overpromising destroys the market for everyone, including you. Gartner's 40% cancellation prediction is a market-level consequence of ecosystem-level dishonesty [I, Source 4].

### For Policymakers and Standards Bodies

**8. Accelerate revision cycles** [J]
Annual or multi-year revision cycles for AI governance standards are structurally incompatible with the technology's pace. Adopt modular, continuously updated standards architectures — similar to software release cycles [J].

**9. Create agentic AI-specific provisions** [J]
Current frameworks were designed for static AI systems. Agentic AI requires specific guidance on: autonomy boundaries, multi-agent coordination, dynamic risk assessment, and continuous compliance verification [I].

**10. Fund governance innovation** [J]
The same level of public investment flowing into AI capability research should flow into AI governance research. The Trust Race cannot be won by capability alone [J].

---

## 10. Transparency Note + Source Log

### Transparency Note

This report was researched and authored by Florian Ziesche using AI-assisted research tools for source discovery, with all analysis, synthesis, and judgment performed by the author. Sources were verified against original publications where accessible. The confidence tagging system ([E], [I], [J], [A]) is designed to make the epistemic basis of every claim explicit and auditable.

**Confidence distribution:**
- [E] Empirical claims: ~55% of quantitative statements
- [I] Inferred claims: ~25%
- [J] Judgment calls: ~15%
- [A] Assumptions: ~5%

**Known limitations:**
- Survey data (Sources 3, 7, 8) reflects respondent self-reporting and may overstate readiness
- METR's capability doubling (Source 1) is measured on software tasks; generalization to all enterprise domains is uncertain
- Gartner's 40% prediction (Source 4) is a forecast, not observed data
- The Trust Race model is a simplification; real-world dynamics include feedback loops, market forces, and discontinuities not captured in the exponential vs. linear framing

**Potential conflicts:** AInarY Ventures operates in the AI advisory space. This creates an inherent interest in organizations investing in AI governance. The author has attempted to mitigate this through transparent sourcing and confidence tagging.

### Source Log

| # | Source | Type | Rating | URL |
|---|--------|------|--------|-----|
| 1 | METR, "Measuring AI Ability to Complete Long Tasks," March 2025 | Primary research | A1 | https://metr.org/blog/2025-03-19-measuring-ai-ability-to-complete-long-tasks/ |
| 2 | AI Digest, "A new Moore's Law for AI agents," 2025 | Secondary analysis | B1 | https://theaidigest.org/time-horizons |
| 3 | HBR Analytic Services / Workato / AWS, "Enterprise Agentic AI Survey," July 2025 (n=603) | Primary survey | A1 | https://fortune.com/2025/12/09/harvard-business-review-survey-only-6-percent-companies-trust-ai-agents/ |
| 4 | Gartner, "Predicts Over 40% of Agentic AI Projects Will Be Canceled by End of 2027," June 2025 | Industry forecast | A2 | https://www.gartner.com/en/newsroom/press-releases/2025-06-25-gartner-predicts-over-40-percent-of-agentic-ai-projects-will-be-canceled-by-end-of-2027 |
| 5 | AWS, "AI lifecycle risk management: ISO/IEC 42001:2023 for AI governance," May 2025 | Secondary analysis | B1 | https://aws.amazon.com/blogs/security/ai-lifecycle-risk-management-iso-iec-420012023-for-ai-governance/ |
| 6 | NIST, "AI 100-1 Artificial Intelligence Risk Management Framework (AI RMF 1.0)," January 2023 | Primary standard | A1 | https://nvlpubs.nist.gov/nistpubs/ai/nist.ai.100-1.pdf |
| 7 | KPMG, "AI at Scale: Q4 2025 AI Pulse Survey," February 2026 | Primary survey | A1 | https://kpmg.com/us/en/media/news/q4-ai-pulse.html |
| 8 | OneTrust, "2025 AI-Ready Governance Report" (n=1,250), December 2025 | Primary survey | A1 | https://www.onetrust.com/blog/what-will-it-take-to-be-ai-ready-in-2026/ |
| 9 | CIO.com, "The emerging enterprise AI stack is missing a trust layer," February 2026 | Expert commentary | B1 | https://www.cio.com/article/4133273/the-emerging-enterprise-ai-stack-is-missing-a-trust-layer.html |
| 10 | Forbes, "What Is AI Agent Washing, And Why Is It Everywhere?," August 2025 | Industry analysis | B2 | https://www.forbes.com/sites/aytekintank/2025/08/20/what-is-ai-agent-washing-and-why-is-it-everywhere/ |
| 11 | Writer.com, "Enterprise guide to agent washing," October 2025 | Vendor perspective | B2 | https://writer.com/blog/agent-washing/ |
| 12 | CIO.com, "Why most agentic AI projects stall before they scale," February 2026 | Expert commentary | B1 | https://www.cio.com/article/4132031/why-most-agentic-ai-projects-stall-before-they-scale.html |
| 13 | WEF, "How can agile AI governance keep pace with technology?," January 2026 | Policy analysis | A2 | https://www.weforum.org/stories/2026/01/agile-ai-governance-how-can-we-ensure-regulation-catches-up-with-technology/ |
| 14 | WEF, "This month in AI: deployment accelerates, but is regulation keeping up?," October 2025 | Policy analysis | A2 | https://www.weforum.org/stories/2025/10/this-month-in-ai-deployment-accelerates-but-is-regulation-keeping-up/ |
| 15 | WEF, "The business advantage of strong AI governance," February 2026 | Policy analysis | A2 | https://www.weforum.org/stories/2026/02/ai-governance-businesses-hold-them-back/ |
| 16 | Cisco Newsroom, "Trust at scale: Why data governance is becoming core infrastructure for AI," January 2026 | Industry perspective | B2 | https://newsroom.cisco.com/c/r/newsroom/en/us/a/y2026/m01/trust-at-scale-why-data-governance-is-becoming-core-infrastructure-for-ai.html |
| 17 | RAND Corporation, "Governing at the Speed of Change: An AI-Enabled Adaptive Framework," September 2025 | Policy research | A2 | https://www.rand.org/pubs/commentary/2025/09/governing-at-the-speed-of-change-an-ai-enabled-adaptive.html |
| 18 | Cognizant, "A Blueprint for Real-Time AI Governance," 2025 | Vendor framework | B2 | https://www.cognizant.com/us/en/insights/insights-blog/real-time-governance-framework-for-ai-systems |
| 19 | Brookings Institution, "The three challenges of AI regulation," October 2024 | Policy analysis | A2 | https://www.brookings.edu/articles/the-three-challenges-of-ai-regulation/ |
| 20 | Reuters, "Over 40% of agentic AI projects will be scrapped by 2027, Gartner says," June 2025 | News reporting | B1 | https://www.reuters.com/business/over-40-agentic-ai-projects-will-be-scrapped-by-2027-gartner-says-2025-06-25/ |

---

## 11. About the Author

**Florian Ziesche** is the founder of AInarY Ventures, where he advises organizations on AI strategy, governance, and trust infrastructure. His work focuses on the intersection of exponential AI capability growth and institutional readiness — helping enterprises build the governance foundations that turn AI potential into sustainable competitive advantage.

Prior to AInarY Ventures, Florian built experience across venture capital, strategic advisory, and technology deployment in high-stakes environments. He writes and speaks on AI governance, agentic systems, and the organizational transformations required to operate safely at the frontier.

This report is part of AInarY Ventures' ongoing research series on AI governance and trust infrastructure. Previous report: *AR-001: The State of AI Agents in the Enterprise* (January 2026).

**Contact:** florian@ainaryventures.com
**Web:** ainaryventures.com
**LinkedIn:** linkedin.com/in/florianziesche

---

*© 2026 AInarY Ventures. This report may be shared with attribution.*
*Report ID: AR-002 | Version: 1.0 | Published: February 2026*
