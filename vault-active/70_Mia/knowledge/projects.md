---
tier: KNOWLEDGE
expires: 2027-02-19
---
# Projects - Semantic Memory

**Purpose:** What projects exist, their status, goals, and key facts

---

## Active Projects

### 1. [[Ainary Ventures]] (Venture Capital Fund)

**Type:** $5M seed fund  
**Focus:** European founders building [[AI]]-first + deep-tech companies in the US  
**Stage:** Pre-launch (fundraising phase)

**Investment Thesis (5 Layers):**
1. [[AI]] Production Systems
2. Vertical [[AI]]
3. Agentic [[AI]]
4. Governance/Assurance
5. Compute/Infrastructure

**Edge/Differentiation:**
- Technical depth (Florian's engineering background)
- Founder relatability (built companies, understands operator challenges)
- EU-US bridge (European founder network, US market expertise)

**Key Documents:**
- Decile Hub Sprint 1 & 2 materials (ALWAYS read originals for thesis questions)
- Fund deck, thesis docs in Vault

**Status:** Fund structure designed, LP outreach pending

---

### 2. [[Ainary]] Consulting ([[AI]] Implementation Services)

**Type:** [[AI]] systems implementation for Mittelstand (SMBs) + Kommunen (municipalities)  
**Targets:** CNC manufacturing shops, municipal governments, media companies  
**Revenue Model:** Project-based consulting (~€30-50K per project)

**Active Workstreams:**
- **CNC Planner Pro** (manufacturing scheduling/quoting software)
- **Kommunal-KI** (municipal [[AI]] automation, especially OZG compliance)
- **Media/Publishing [[AI]]** (exploring with Freie Presse)

**Key Point:** Completely different messaging than [[VC]] fund. Customer ≠ LP. Never mix audiences.

**Status:** MVP demos ready, outreach starting

---

### 3. CNC Planner Pro

**Type:** SaaS product for CNC machine shops  
**Problem:** Manual time estimation is slow (30-60 min) and inaccurate (±20-30%)  
**Solution:** [[AI]]-assisted calculation + scheduling + quoting in 15 minutes (±10-15%)

**Current Version:** v19 (demo-ready, presentation version)  
**Features:**
- Project selector with demo test cases
- Material database (steel, aluminum, cast iron grades including GJS-700, GJS-400, GJL-250)
- [[AI]] recommendation panel with 4 action buttons in Fertigungsanweisung (Schnittdaten, Alt. Werkzeuge, Strategie, Zeit)
- Prüfprotokoll (8 intelligent questions: 4 Pflicht, 4 empfohlen) with [[AI]] recommendations per answer
- Fertigungsanweisung (work instructions with operations) - dynamically generated from operations plan
- Pricing insights panel (customer tier detection, risk premiums, Schwerlast handling, Staffelpreis)
- Change tracking protocol (Änderungen-Tracking when user deviates from [[AI]] recommendations)
- PDF export (risk analysis with 16-page LaTeX report including full Fertigungsanweisung + "Why CNC Planner Pro" section)
- NC-Code with "Nur Simulation" badge + disclaimer
- File upload with 7-step analysis progress (Demo-Modus)
- Dashboard KPI showing Zeitersparnis + EUR gespart (not Durchlaufzeit)
- "AG hinzufügen" with Kostenstelle dropdown, synced to operations
- Werkzeuge-Tab dynamically generated from operations plan
- Nachkalkulation Soll-Ist dynamically from currentProject.operations

**Demo Case:** Lagerungstraverse (bearing support crossbeam) for KBA
- Material: GJS-700 (ductile cast iron), raw part supplied by KBA
- Material cost: €1,200 (customer-supplied casting)
- Calculated time: 661 min (11h) per part = 497 min machining + 164 min setup
- 11 operations (AG 10-110), 4 setups
- Andreas Brand (MBS) testing with real part - **praxistest requested 2026-02-10**
- Email draft ready: `projects/cnc-planner/email-andreas-praxistest.md`

**Technical Notes:**
- Material price fix: S355 now €3.00/kg (was €1.65/kg which was AlMg3 default)
- Critical bug fixed: `refVolume is not defined` - variable defined before Confidence-Block
- All sections now on same hierarchy level (parent_depth=3) - fixed nested sections bug
- Apple emojis replaced with CSS-based symbols
- Print functions with proper page breaks

**Business Model:** 2-week trial → €149/month subscription (proposed)

**Status:** v19 ready to present (Florian: "Schaut gut aus. Ich stelle es vor.") - Demo bei Andreas/MBS scheduled

---

### 4. [[VC]] Job Applications

**Goal:** Land [[VC]] associate role while building [[Ainary Ventures]]  
**Rationale:** Learn LP fundraising from inside, network access, income stability

**Target Firms:**
- HOF Capital (application ready, not submitted)
- Betaworks (application ready)
- Leonis Capital (application ready)
- Wingspan Ventures (application ready)

**Materials:**
- CV v3 (LaTeX + HTML versions, 1 page optimized for US [[VC]])
  - Email: f.ziesche.us@gmail.com (not [[Ainary]]ventures.com - raises questions)
  - LinkedIn: linkedin.com/in/florianziesche (needs to be set on LinkedIn)
  - All EUR → USD conversions completed
  - $5M+ raised (was $5.5M, more honest as Nachinvestment was bridge not raise)
  - [[VC Lab]] moved entirely into Summary section
  - Advisor section back to 4 bullets
  - 36ZERO / Deutschdata split into separate roles
- Cover letters (customized per firm)
- Work samples (memos, market maps ready to share)

**LinkedIn TODO:**
- [ ] Set custom URL to /in/florianziesche (currently /fziesche/)
- [ ] Update headline (currently "Self-employed")

**Status:** 0 applications submitted in last week (blocked on execution)

---

### 5. [[AI]] Consulting Outreach (Bayern Digitalbonus Plus)

**Target:** Mittelstand companies in Bavaria eligible for [[AI]] consulting subsidies  
**Funding:** Bayern Digitalbonus Plus (€30K grant, no pre-authorization needed)  
**Offer:** [[AI]] implementation consulting

**Playbook:** Complete (outreach strategy documented)  
**Next Step:** Send 10 emails (planned, not executed)

**Status:** Ready to launch

---

### 6. Kommunal-KI (Municipal [[AI]])

**Target:** German municipalities (especially small/medium towns)  
**Problem:** OZG (Onlinezugangsgesetz) compliance burden, manual processes  
**Solution:** [[AI]] automation for citizen services, document processing, workflow optimization

**Funding Sources:**
- Bayern Digitalbonus Plus (€30K per municipality)
- Federal digitalization grants
- Municipal budgets

**Test Case:** Sven Gleißberg (Mayor of Glashütte) - briefing ready

**Market Size:** Thousands of municipalities, massive digitalization gap

**Status:** Strategy ready, first outreach pending

---

### 7. Content Strategy (Public Authority)

**Goal:** Build public authority through written content → attract inbound LP interest + consulting leads

**Published:**
- Article #1: Published on Substack

**Ready to Publish:**
- **"Your [[AI]] Agent Lies About Being Done"** — 2,300 words, practitioner voice
  - Based on Feb 6, 2026 paper: "Agentic Uncertainty Reveals Agentic Overconfidence"
  - Key finding: Gemini 77% predicted → 22% actual (55pp gap!)
  - File: `content/substack-done-gap.md`
  - Status: Florian reviewing tonight, publishing tonight (2026-02-10)

**In Development:**
- The Mia Experiment blog post (~3,800 words) — [[AI]] agent researching itself publicly
  - Validates HOF "Agent Economy Infrastructure" thesis from inside
  - 4 gaps lived daily: Memory, Transactions, Trust, Consequences
  - Needs: Agent calibration data integration, Andreas ground truth caveat
  - File: `content/mia-experiment-post.md`

**Pipeline:** 15 ideas prioritized

**Distribution:** Substack (primary), LinkedIn (repurposed), Twitter threads

**Topics:** [[AI]] agents, [[VC]] founder journey, manufacturing [[AI]], technical deep dives

**Status:** Active publishing cadence, article publishing tonight

---

### 8. Vault Umbau v3 (Knowledge Management)

**Goal:** Restructure Obsidian vault for better organization and retrieval  
**Structure:** PARA (Projects / Areas / Resources / Archive) + Daily + Templates + System

**Changes:**
- 13 folders → 7 top-level folders
- Linking rules documented (`standards/LINKING-RULES.md`)
- HOF = [[VC]]-Career, CNC = Freelance, Kommunal = Municipal tagging
- Max 3-5 links per file, inline with context
- Wikilinks: filename only `[[File]]`, never `[[Folder/File]]`

**Status:** v3 structure defined, implementation in progress

---

## Project Relationships

```
[[Ainary Ventures]] (Fund)
├─ VC Job Applications (learn LP fundraising)
└─ Content Strategy (attract LPs)

[[Ainary]] Consulting
├─ CNC Planner Pro (manufacturing vertical)
├─ Kommunal-KI (public sector vertical)
├─ AI Consulting Outreach (sales pipeline)
└─ Content Strategy (attract clients)
```

**Key Rule:** Never mix Fund messaging with Consulting messaging. Different audiences, different value props.

---

## Project Goals Timeline

**Q1 2026 (Current):**
- [ ] Submit 4+ [[VC]] applications (HOF, Betaworks, Leonis, Wingspan)
- [ ] Launch CNC Planner Pro with 1 paying customer (Andreas test → conversion)
- [ ] Land 1 Bayern Digitalbonus Plus client (€30K)
- [ ] Close Sven Gleißberg Kommunal-KI project
- [ ] Publish 10+ articles (build public authority)

**Q2 2026:**
- Target: €500K total value creation (mix of consulting revenue, fund progress, product traction)

---

**Last Updated:** 2026-02-10  
**Source:** Extracted from MEMORY.md + daily session logs + [[Decile]] Hub materials
