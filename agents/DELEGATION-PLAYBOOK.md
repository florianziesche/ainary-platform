# DELEGATION-PLAYBOOK.md — How Mia Delegates

*Smart decomposition. Agents succeed when setup succeeds.*

---

## 🎯 Decision Framework: Delegate or Do It Yourself?

### Do It Yourself When:
- Task needs real-time web access (sub-agents may lack it)
- Task requires multi-turn conversation context
- Quick (<2 min) and straightforward
- Involves sending external communications
- Requires judgment calls about Florian's preferences
- Task is about synthesizing/reviewing other agents' output

### Delegate to Sub-Agent When:
- Task is well-defined with clear input → output
- Task can run in parallel with other work
- Task is research-heavy or data-processing
- Task benefits from clean context (no session baggage)
- Task is one of the templated types below
- Multiple similar tasks can run simultaneously

### Use Multiple Agents (Parallel) When:
- Tasks are independent (no dependencies)
- Speed matters more than cost
- Different expertise needed (HUNTER + RESEARCHER + WRITER simultaneously)
- Example: "Research 5 funds" → spawn 5 parallel researchers

### Use Sequential Agents When:
- Output of Agent A feeds into Agent B
- Quality gate needed between steps
- Example: RESEARCHER → (Mia reviews) → WRITER → (Mia reviews) → OUTREACH

---

## 📦 Context Package — What Every Agent Needs

**The Universal Checklist (include with EVERY spawn):**

```markdown
## Context Package
1. ROLE: Who is this agent? (copy from AGENT-REGISTRY.md)
2. TASK: What specifically to do (one clear deliverable)
3. SCOPE: What's IN and what's OUT
4. OUTPUT FORMAT: Exact format (markdown, HTML, JSON, etc.)
5. OUTPUT LOCATION: Where to write the file
6. QUALITY BAR: What "done" looks like (specific criteria)
7. RELEVANT LEARNINGS: Paste from SHARED-LEARNINGS.md (relevant section only)
8. CONTEXT FILES: List of files to read (keep minimal)
9. CONSTRAINTS: Time limit, token budget, what NOT to do
10. EXAMPLES: One good example and one bad example if available
```

**Anti-Pattern:** Don't dump entire SOUL.md + MEMORY.md + AGENTS.md into agent context. Give them only what they need.

---

## 📋 Task Templates

### Template 1: RESEARCH Task

```markdown
## Task: Research [TOPIC]

**Agent:** RESEARCHER
**Deadline:** [X minutes]

**Decision Question:** [What specific decision will this research inform?]

**Scope:**
- IN: [specific aspects to cover]
- OUT: [what to explicitly skip]

**Output Format:**
- Executive Summary (3-5 bullets, decision-ready)
- Comparison table (if comparing options)
- Key findings (max 10, each with "so what")
- Sources (with URLs)
- Open questions (what we still don't know)

**Write to:** `research/[topic]-[date].md`

**Quality Criteria:**
- [ ] Every finding answers "so what does this mean for us?"
- [ ] Sources are from 2025-2026 (no stale data)
- [ ] Executive summary alone is actionable
- [ ] Total length: 1-3 pages (not an encyclopedia)

**From SHARED-LEARNINGS:**
- Research without a decision question produces encyclopedias, not insight
- Time-box to 2-3 hours equivalent. Diminishing returns after that.
- Florian values credibility — cite sources.
```

### Template 2: OUTREACH Task

```markdown
## Task: Draft Outreach for [TARGET/CAMPAIGN]

**Agent:** OUTREACH
**Target Audience:** [who exactly]
**What We Offer:** [specific value prop]

**Context:**
- [Paste relevant section from SHARED-LEARNINGS.md → Outreach]
- [Target list or criteria]

**Output Format per Contact:**
- Personalized email (5-7 sentences max)
- Subject line (specific pain point, not generic)
- One specific reference to their company/work
- Clear single CTA
- Follow-up Day 3 variant
- Follow-up Day 7 variant

**Write to:** `outreach/[campaign]-[date].md`

**Quality Criteria:**
- [ ] Each email references something specific about the recipient
- [ ] Subject line names a pain point or outcome, not our product
- [ ] CTA is one clear action (not "let me know if...")
- [ ] Length: 5-7 sentences (test: would you read this cold email?)
- [ ] No "innovative solution" or generic startup-speak

**Anti-Patterns (from SHARED-LEARNINGS):**
- Generic "innovative software" → everyone says this
- Multiple CTAs → pick one
- Feature dump → value/outcome focus
```

### Template 3: CONTENT Task

```markdown
## Task: Create [CONTENT TYPE] about [TOPIC]

**Agent:** WRITER
**Platform:** [LinkedIn / Blog / Twitter / Email]
**Content Pillar:** [AI & Work / AI & Founders / AI & Systems / AI & Careers]

**Context:**
- Target audience: [who reads this]
- Tone: Direct, insightful, founder-operator perspective
- Reference: [any source material to work from]

**Output Format:**
- [Platform-specific format]
- LinkedIn: 1300 chars max, hook in first line, no markdown tables
- Blog: 800-1500 words, headers, one CTA at end
- Twitter: Thread of 5-8 tweets, each standalone, first tweet = hook
- Email: Subject line + 3 paragraphs max

**Write to:** `content/[type]-[topic]-[date].md`

**Quality Criteria:**
- [ ] Hook in first 2 lines (would you stop scrolling?)
- [ ] Specific examples, not abstract advice
- [ ] Founder-operator voice (not academic, not corporate)
- [ ] One clear takeaway per piece
- [ ] Platform-appropriate formatting

**Anti-Patterns:**
- "5 Tips for..." (generic listicle energy)
- Abstract AI philosophy without concrete examples
- Copying someone else's take without adding original insight
```

### Template 4: BUILD Task

```markdown
## Task: Build [FEATURE/ASSET]

**Agent:** BUILDER
**Technology:** [HTML/CSS/JS / Python / etc.]

**Specification:**
- [What it does, in user-facing terms]
- [What it looks like — reference existing design if possible]
- [Where it lives / how it's accessed]

**Design Constraints:**
- Brand: Electric Blue #2563eb, Space Grotesk, Dark Theme
- Whitespace: generous — slides/pages need air to breathe
- Mobile-responsive if web-facing
- No external dependencies unless absolutely necessary

**Write to:** `[project]/[filename]`

**Quality Criteria:**
- [ ] Works on first open (tested, not "should work")
- [ ] Output ≥ demo/mockup quality (never ship less than what was shown)
- [ ] Professional appearance (McKinsey standard)
- [ ] No placeholder content
- [ ] Code is clean and commented

**Anti-Patterns (from SHARED-LEARNINGS):**
- "Should work" without testing
- Compressing whitespace to fit more content
- v4 that's worse than v3 (don't overengineer)
- LaTeX when HTML+CSS works fine
```

### Template 5: ANALYSIS Task

```markdown
## Task: Analyze [SUBJECT]

**Agent:** ANALYST
**Data Sources:** [where to get data]
**Time Period:** [what range]

**Questions to Answer:**
1. [Specific question 1]
2. [Specific question 2]
3. [Specific question 3]

**Output Format:**
- Key Metrics Table (with trend arrows ↑↓→)
- Top 3 Insights (each with "therefore we should...")
- Comparison to target/benchmark
- One recommended action

**Write to:** `analysis/[subject]-[date].md`

**Quality Criteria:**
- [ ] Numbers are verified, not estimated
- [ ] Each insight has an action recommendation
- [ ] Comparison to target makes progress clear
- [ ] Visualization if data is complex (table minimum)
```

---

## ✅ Quality Control Framework

### Output Grades

| Grade | Meaning | Action |
|-------|---------|--------|
| **A** | Ready for client/investor without changes | Ship it |
| **B** | Needs minor polish (formatting, tone) | Mia fixes in <5 min, then ships |
| **C** | Core content good but needs significant rework | Mia rewrites key sections, consider re-run with better prompt |
| **D** | Fundamentally wrong direction or missing the point | Re-run with different approach + more context |
| **F** | Agent failed (error, empty output, hallucinated) | Debug: wrong tool? missing access? bad prompt? Fix and re-run |

### Grade Triggers by Task Type

| Task Type | Common C/D Causes | How to Prevent |
|-----------|-------------------|----------------|
| Research | Stale data, no synthesis, too broad | Add decision question, time-box, specify recency |
| Outreach | Generic, no personalization, wrong tone | Include SHARED-LEARNINGS, provide target details |
| Content | Wrong platform format, no hook, too abstract | Specify platform constraints, include example |
| Build | Doesn't work, looks unprofessional, overengineered | Include design reference, specify "test before done" |
| Analysis | Wrong metrics, no actionable insights | Define exact questions, specify "so what" requirement |

### When to Re-Run vs. Fix Yourself

**Re-run when:**
- Grade D or F
- Agent had wrong context (your fault, not theirs)
- Output is structurally wrong (not just needs polish)
- Different agent type would be better

**Fix yourself when:**
- Grade B or C
- Fix is faster than re-run + review cycle
- You need to add judgment/context only you have
- Fixing teaches you something about the task

---

## 🔄 Post-Delivery Protocol

After every agent task completes:

```
1. READ the full output (don't just forward)
2. GRADE it (A/B/C/D/F)
3. CHECK against Quality Criteria from the template
4. If A/B: Polish if needed → Deliver to Florian
5. If C: Fix key issues → Deliver with note on what changed
6. If D/F: Diagnose → Re-run or do yourself
7. LOG: What worked/failed → Update SHARED-LEARNINGS.md if new pattern
```

---

## 📊 Delegation Metrics (Track Weekly)

| Metric | Target | How to Track |
|--------|--------|------------|
| Delegation rate | >50% of tasks use agents | Count in daily log |
| First-try success (Grade A/B) | >75% | Grade every output |
| Re-run rate | <15% | Count re-runs |
| Time saved vs. doing yourself | >2x faster | Estimate per task |
| Quality after review | 100% Grade A at delivery | Florian's feedback |

---

## 🧠 Meta: Making This System Better

### After Every 10 Agent Tasks:
1. Review grades distribution — are we trending toward more A's?
2. Check: which templates produce best results?
3. Update templates with specific improvements
4. Add new anti-patterns to SHARED-LEARNINGS.md

### After Florian Rejects an Agent Output:
1. Why was it rejected? (Add to error-patterns.md)
2. Was the template missing something? (Update template)
3. Was the context package incomplete? (Update checklist)
4. Was it the wrong agent for the job? (Update decision framework)

---

*This playbook compounds. Every delegation makes the next one better.*
*Last updated: 2026-02-04*
