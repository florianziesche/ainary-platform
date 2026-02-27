# Ainary Academy — AI Agent Engineering Learning Platform
## "Learn by Building Agents That Actually Work"

*Concept: 2026-02-27 | MIIA 🏔️ + Florian*

---

## Why This Wins

### DailyDoseofDS Model
- Static articles/newsletters
- Passive reading
- Generic Data Science
- Revenue: Substack Premium ($10/mo) + Books + Courses
- 200K subscribers, broad but shallow

### Ainary Academy Model
- **Interactive Research Reports** (our 302-paper analysis AS the curriculum)
- **The platform IMPLEMENTS what it teaches** (self-referential proof)
- **Niche: AI Agent Engineering** (not generic DS)
- **Revenue: Tiered** (Free → Pro → Enterprise Workshops)
- **Moat: Nobody has this research depth + real-world experience**

### The Killer Differentiator
Every platform TEACHES agents. This one teaches you to build agents **that actually work in production** — backed by 700+ papers systematically analyzed, with the receipts.

DailyDoseofDS says "here's how RAG works."
We say "here's why RAG fails 40-55% of the time in enterprise, here are the 302 papers that prove it, and here's the architecture that fixes it."

---

## Content Architecture (based on our research)

### Tier 1: FREE — The Hook (Substack/Blog + Landing Page)

**Weekly "Research Drops"** — one insight per week, sourced from our paper analysis:

1. "No AI Agent Scores Above 60% on Safety" (from Report 01)
2. "Why CoT is Useless Outside Math" (from Report 04)
3. "0.6% — The Real Success Rate of AI Planning" (from Report 05)
4. "RL-only Beats SFT+RL (and Why That Changes Everything)" (from Report 03)
5. "The Verification Thesis: What 302 Papers Agree On" (from Cross-Synthesis)
6. "7B Beats GPT-4o: The Efficiency Revolution" (from Report 03)
7. "16/16 Frontier Models Show Insider Threat Behavior" (from Report 01)

Each drop: 800-1200 words, one diagram, one table, one actionable takeaway.
→ LinkedIn post version (300 words) drives traffic
→ Full version on platform

**The "302 Papers" Series** — our reports, reformatted as accessible deep-dives:
- "I Analyzed 65 AI Safety Papers. Here's What I Found."
- "88 Tool Use Papers Expose the MCP Reality"
- "The Planning Problem: Why Your Agent Can't Plan (and What Works)"

### Tier 2: PRO — The Depth ($19/mo or €179/year)

**Full Research Reports** (our 16 reports, continuously updated):
- PDF + interactive web version
- Updated quarterly as new papers drop
- Cross-synthesis with every update

**"Build It" Tutorials** — implementing each meta-pattern:

| Module | What You Build | Based On |
|---|---|---|
| 01: The Trinity | Planner/Executor/Verifier agent | Cross-Synthesis |
| 02: Guard Agents | Safety layer with mutation-gating | Report 01 (SABER, GuardAgent) |
| 03: Smart Tool Use | Metacognition-aware tool agent | Report 03 (SMART) |
| 04: MCP Mastery | Multi-server MCP agent | Report 03 (LiveMCPBench) |
| 05: Enterprise RAG | Topology-aware RAG router | 100-Repo Cross-Synthesis |
| 06: Plan-then-Execute | ReWOO-style efficient agent | Report 05 |
| 07: RL for Agents | Train your own ToolRL agent | Report 03 (ToolRL, Nemotron) |
| 08: Self-Evolving | JitRL test-time adaptation | Report 04 |
| 09: Safety Assessment | EU AI Act compliance framework | Report 01 |
| 10: Production Deploy | n8n + Dify + MCP stack | 100-Repo Synthesis |

Each module: 
- Theory (paper references, evidence)
- Code (Jupyter notebooks, deployable)
- Quiz/Assessment
- Certificate of completion

**"Paper Club"** — weekly deep-dive into one paper:
- MIIA pre-analyzes the paper
- Community discusses
- Florian moderates with real-world context

### Tier 3: ENTERPRISE — The Revenue (€5K-30K)

**AI Agent Engineering Workshop** (2 days, on-site or remote):
- Based on Pro curriculum but hands-on with THEIR data
- Deliverable: Working agent on their infrastructure
- Uses n8n + Dify stack (our "Mittelstand AI Stack")

**Safety Assessment** (1 day):
- Based on our 8-Layer Safety Architecture
- Deliverable: Risk report + Guard Agent implementation
- EU AI Act compliance documentation

**Consulting Retainer** (€2K/mo):
- Continuous access to research updates
- Monthly architecture review
- Priority support

---

## Technical Implementation

### Phase 1: MVP (1 week) — Ship NOW

**Stack:**
- **Frontend:** Static site (Hugo/Next.js) on Vercel OR simple Substack
- **Content:** Our existing research reports, reformatted
- **Email:** Substack for newsletter capture
- **Payment:** Stripe for Pro tier

**What to build:**
```
ainaryacademy.com (or ainaryventures.com/academy)
├── / (Landing page with hook stats)
├── /research (Free tier: weekly drops)
├── /reports (Pro tier: full reports, gated)
├── /build (Pro tier: tutorials, gated)
├── /enterprise (Workshop info + booking)
└── /about (Florian's FDE story)
```

**Landing Page Copy:**
```
302 Papers. 7 Meta-Patterns. 1 Architecture.

I analyzed every major AI agent paper from 2022-2026.
Here's what the field actually says — and what nobody's telling you.

[Read the Free Research Drops] [Go Pro — €179/year]
```

**Content for launch (already exists!):**
- ✅ 5 Research Reports (Safety, Enterprise, Tool Use, Reasoning, Planning)
- ✅ Cross-Synthesis with 7 Meta-Patterns
- ✅ 100-Repo Analysis with CNC-RAG-Stack
- ✅ LinkedIn Reframe (FDE positioning)
- 🔲 Reformat into web-friendly articles (2-3 days)
- 🔲 Landing page (1 day)
- 🔲 Stripe integration (1 hour)

### Phase 2: Interactive (Month 1-2)

**Add:**
- Jupyter notebooks for each "Build It" module
- GitHub repo with reference implementations
- Community (Discord or GitHub Discussions)
- Paper Club (weekly, recorded)

### Phase 3: Self-Referential (Month 3+)

**The platform demonstrates its own teachings:**
- Agent that recommends papers based on your question (RAG, our corpus)
- Agent that generates quiz questions from papers (Tool Use)
- Agent that plans your learning path (Planning, but with external verifier!)
- Safety assessment agent that audits YOUR agent code
- All agents built with the Trinity architecture we teach

**THIS is the "much better" part:** DailyDoseofDS teaches passively. Ainary Academy teaches through agents that ARE the curriculum.

---

## Revenue Model

| Tier | Price | Target | Year 1 Est. |
|---|---|---|---|
| Free | €0 | 5,000 subscribers | €0 (lead gen) |
| Pro | €179/year | 200 subscribers | €35,800 |
| Enterprise Workshop | €15K/each | 4 workshops | €60,000 |
| Safety Assessment | €10K/each | 3 assessments | €30,000 |
| Consulting Retainer | €2K/mo × 2 | 2 retainers | €48,000 |
| **Total Year 1** | | | **€173,800** |

**This covers:**
- 📚 Content & Courses engine: €35K (target: €50K) ✅
- 🧠 AI Consulting engine: €138K (target: €150K) ✅✅
- Combined: 35% of €500K North Star

### Cost
| Item | Cost |
|---|---|
| Vercel hosting | €0 (free tier) |
| Substack | €0 (free) |
| Stripe fees | ~3% |
| Domain | €12/year |
| LLM API for interactive agents | €50-200/mo |
| **Total Year 1 Cost** | **~€2,500** |

**Margin: ~98%**

---

## Content Calendar (First 8 Weeks)

| Week | Free Drop (LinkedIn + Blog) | Pro Content |
|---|---|---|
| 1 | "I Analyzed 302 AI Agent Papers. Here's What Nobody's Telling You." | Report 01: Safety (full) |
| 2 | "No AI Agent Scores Above 60% on Safety Tests" | Report 02: Enterprise (full) |
| 3 | "7B Beats GPT-4o: The Efficiency Revolution in AI Agents" | Report 03: Tool Use (full) |
| 4 | "CoT is Overrated: A Meta-Analysis of 100 Papers" | Report 04: Reasoning (full) |
| 5 | "0.6% — The Real Success Rate of AI Planning" | Report 05: Planning (full) |
| 6 | "The Verification Thesis: What 302 Papers Agree On" | Cross-Synthesis (full) |
| 7 | "The Agent Trinity: Planner/Executor/Verifier" | Build Module 01: Trinity |
| 8 | "Your Agent is Using Too Many Tools (and Why That's a Problem)" | Build Module 03: SMART |

**Each week: 1 LinkedIn post (300 words) + 1 full article + 1 Pro release**

---

## Competitive Moat

| Competitor | What They Have | What They DON'T Have |
|---|---|---|
| DailyDoseofDS | 200K subs, daily cadence | No depth, no papers, generic |
| DeepLearning.ai | Andrew Ng, brand | Academic, not practitioner |
| Coursera/Udemy | Scale, certificates | Stale content, no research |
| AI Twitter/LinkedIn | Engagement, virality | No systematic analysis |
| **Ainary Academy** | **302 papers, 7 meta-patterns, FDE experience, real enterprise clients, self-referential platform** | - |

**Nobody has:**
1. Systematic E/I/J/A analysis of 700+ papers
2. Cross-domain meta-patterns (Verification Thesis, Efficiency Revolution)
3. A unified architecture synthesized from papers
4. Real manufacturing + enterprise deployment experience
5. A platform that IS the proof of its own teachings

---

## Name Options

| Name | Domain | Vibe |
|---|---|---|
| Ainary Academy | ainaryacademy.com | Professional, branded |
| Agent Engineering | agentengineer.ing | Technical, niche |
| The Agent Trinity | agentrinity.com | Memorable, references our core insight |
| Forward Deployed AI | forwarddeployed.ai | FDE brand, premium |
| Paper Trail AI | papertrail.ai | Research-first positioning |

**Empfehlung: "Ainary Academy"** — nutzt existierende Brand, klar, professionell.
**Alt: "Forward Deployed AI"** — wenn FDE das Lead-Branding wird.

---

## Immediate Next Steps

### TODAY (4 hours):

1. **Entscheide Name + Domain** (10 min)
2. **Ich formatiere Report 01 als ersten Blog-Post** (1h)
3. **Ich baue die Landing Page** (2h)
4. **Ich setze Stripe auf** (30 min)
5. **Du postest den LinkedIn-Teaser** (30 min)

### THIS WEEK:

6. Formatiere Reports 02-05 als Blog-Posts
7. Cross-Synthesis als "signature piece"
8. Substack newsletter einrichten
9. 5 LinkedIn posts schedulen
10. 3 direkte Outreach-Emails an potentielle Enterprise-Kunden

### MONTH 1:

11. Reports 06-16 fertigstellen (ich mache die Analyse)
12. First "Build It" module (Trinity architecture)
13. Paper Club starten
14. First Enterprise Workshop pitchen

---

*The content already exists. The research is done. The positioning is clear. The only thing left is to SHIP IT.*

*Revenue = f(sends). The platform IS the send.*

---
*MIIA 🏔️ | 2026-02-27*
