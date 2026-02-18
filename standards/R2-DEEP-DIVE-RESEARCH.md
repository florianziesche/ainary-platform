# R2 — Deep Dive Research
> Version 1.0 | Created 2026-02-18 | Tag: [INTERN]
> Status: ACTIVE | Proven: 0 times

---

## 1. IDENTITY

**What:** Structured research deliverable that produces actionable insights with verified sources, explicit contradictions, and a clear recommendation.

**For Whom:** Florian (decision-making), Mia (knowledge base), Platform (Findings import).

**Quality Level:** Tier 2 (QS-019). Every claim sourced. Every number verified or marked "unverified". Contradictions surfaced, not hidden.

**Time Budget:** 60–90 minutes total execution. If exceeding 90 min, the scope is wrong — split into two R2s.

---

## 2. TRIGGER

Use R2 when:
- Exploring a company, market, technology, or competitor in depth
- Preparing strategic decisions (build vs. buy, enter vs. skip)
- Building knowledge that will be reused (Findings, Content, Pitches)

Do NOT use R2 when:
- Quick fact-check → use **R1** (15 min, bullet points only)
- Academic-level exhaustive research → use **R3** (4–6h, paper format)
- You already know the answer and just need confirmation → don't research, decide

---

## 3. INPUTS REQUIRED

Before starting R2, you need:
- [ ] **Primary Question** — One sentence. "What is X and why should we care?"
- [ ] **Context** — Why are we asking this now? What decision does it inform?
- [ ] **Known Priors** — What do we already know? (Check verified-truths.md, connections.md, Platform Findings)
- [ ] **Hypothesis** — A strong guess BEFORE researching. "I think X because Y." This prevents confirmation bias by giving you something to actively try to disprove.

If you cannot state a hypothesis, you don't understand the question well enough. Go back.

---

## 4. PROCESS

### Step 1: Frame (5 min)
- Write Primary Question
- Write Hypothesis
- Define 3 Sub-Questions that would prove or disprove the hypothesis
- Define scope boundary: "I will NOT research Z because..."

### Step 2: Search (20–30 min)
- Minimum 8 sources. Mix of:
  - Company's own materials (website, press releases, docs)
  - Independent analysis (analyst reports, reviews, comparisons)
  - Critical voices (complaints, limitations, alternatives)
- For each source: extract 2–3 key claims with quotes
- TRY TO DISPROVE your hypothesis. Not confirm it.

### Step 3: Synthesize (15–20 min)
- Group findings into themes (max 5 themes)
- Identify contradictions between sources
- Rate confidence per theme (how much evidence, how reliable)
- Check: Does the evidence support or disprove the hypothesis?

### Step 4: Conclude (10 min)
- Write recommendation: 1 clear action with reasoning
- State what you're still unsure about
- Identify 2–3 connections to existing knowledge (connections.md pattern)
- Define: What would change this conclusion? (falsifiability)

### Step 5: Quality Gate (5 min)
- Run the Quality Gate checklist below
- Fix any failures
- If >2 failures: the research is not done. Go back to Step 2 or 3.

---

## 5. OUTPUT TEMPLATE

```markdown
# R2: [Topic]
> Date: YYYY-MM-DD | Time: Xmin | Confidence: X%
> Primary Question: [one sentence]
> Hypothesis: [what I expected to find]
> Verdict: [CONFIRMED / DISPROVED / NUANCED]

## Key Findings

### 1. [Theme Name]
[2–4 sentences. Core insight.]
- Source: [name, URL, date]
- Confidence: X% — [why]

### 2. [Theme Name]
...

### 3. [Theme Name]
...

## Contradictions Found
- [Source A] says X, but [Source B] says Y.
  Resolution: [which is more credible and why] / [unresolved — needs more data]

## Connections to Existing Knowledge
- Relates to [Finding RF-XXX]: [how]
- Supports/Contradicts [Finding RF-YYY]: [how]
- New insight for [research_line]: [what]

## Recommendation
[1 clear action. What should Florian do with this knowledge?]
- Why: [reasoning]
- Risk if wrong: [what happens]
- What would change this: [falsifiability]

## Open Questions
- [What I couldn't answer]
- [What needs R3-level investigation]

## Sources
1. [Name] — [URL] — [date accessed] — [reliability: high/medium/low]
2. ...

## Metadata
- Research Line: [for Platform import]
- Tags: [for Platform import]
- Findings to create: [list of RF-IDs to seed]
```

---

## 6. QUALITY GATE

Every box must be checked. No exceptions.

### Structure
- [ ] Primary Question stated (one sentence)
- [ ] Hypothesis stated BEFORE findings
- [ ] Verdict explicitly addresses hypothesis (confirmed/disproved/nuanced)

### Evidence
- [ ] Minimum 8 sources cited
- [ ] At least 2 sources are critical/opposing voices
- [ ] Every factual claim has a source
- [ ] Numbers are verified or explicitly marked "unverified"
- [ ] Source dates are noted (nothing older than 2 years without justification)

### Analysis
- [ ] At least 1 contradiction identified and addressed
- [ ] Confidence rating per theme (not just overall)
- [ ] Connections to 2+ existing Findings or knowledge
- [ ] "What would change this conclusion" stated

### Actionability
- [ ] Exactly 1 recommendation (not 3 options)
- [ ] Recommendation includes risk assessment
- [ ] Open questions listed (intellectual honesty)
- [ ] Findings ready for Platform import (IDs, tags, research_line defined)

**Scoring: 15 checkboxes. 13+ = PASS. 11-12 = REVISE. <11 = FAIL (redo).**

---

## 7. KNOWN FAILURE MODES

| Failure | How it manifests | Prevention |
|---------|-----------------|------------|
| Confirmation Bias | All sources support hypothesis, no contradictions found | Force Step 2: "find 2 sources that disagree" |
| Scope Creep | 90 min becomes 3 hours, rabbit holes | Hard stop at 90 min. If not done, scope was wrong. |
| Source Laziness | All sources from page 1 of Google | Require: 1 academic, 1 industry report, 1 critical voice |
| No Recommendation | "It depends" / 3 options without pick | Force: "If you had to bet €10K on one action, which?" |
| Stale Research | Using 2020 data for 2026 decisions | Check source dates. Flag anything >2 years. |
| Isolated Knowledge | Great research, never connected to existing Findings | Step 4 forces 2+ connections. No exceptions. |

---

## 8. PROVEN ON

| # | Date | Topic | Quality Gate Score | Output |
|---|------|-------|--------------------|--------|
| — | — | No outputs yet | — | — |

---

## 9. IMPROVEMENT LOG

| Date | Change | Why | Based On |
|------|--------|-----|----------|
| 2026-02-18 | v1.0 created | Initial standard | QS-019 + Google Design Doc research + Mia's Research Audit (scored 8-11/16 FAIL) |

---

## META

- **Depends on:** R1 (Quick Scan) as lighter alternative
- **Feeds into:** S1 (Ersttermin-Prep), C1 (LinkedIn Post), C2 (Blog Artikel), Platform Findings
- **Improves from:** Every R2 output that scores <15/15 on Quality Gate — the failure reveals a standard gap
