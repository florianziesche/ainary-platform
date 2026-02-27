# LLM as Judge — Post-Generation Fact-Check Workflow

## Purpose
Automated self-evaluation to catch factual errors, unsourced claims, and fabricated data BEFORE delivery.

## When To Use
- Before sending ANY content externally (LinkedIn posts, emails, reports)
- After research/analysis tasks (candidate profiles, company research, market analysis)
- After data processing (Gotham dashboards, statistics, numbers)

## Workflow

### Step 1: Generate Content (Existing)
Agent generates content as usual (carousel, email, post, report).

### Step 2: LLM as Judge Prompt (NEW)
After generation, agent MUST run self-audit prompt:

```
You are an expert fact-checker. Evaluate the following content:

[INSERT GENERATED CONTENT HERE]

Your task:
1. **Accuracy Check:** Are names, numbers, dates, affiliations correct?
2. **Source Verification:** Are claims sourced or unsourced?
3. **Fabrication Detection:** Are there invented statistics or fake data?
4. **Confidence Score:** Rate overall accuracy (0-100).

Original sources available:
[INSERT SOURCE DATA HERE]

Return:
- **Score:** X/100
- **Issues Found:** [List all errors, unsourced claims, fabrications]
- **Recommendation:** [SHIP / FIX / BLOCK]
```

### Step 3: Decision Gate
- **Score ≥ 90 + No fabrications:** SHIP (proceed to delivery)
- **Score 70-89 OR unsourced claims:** FIX (revise, add sources, re-check)
- **Score < 70 OR fabrications detected:** BLOCK (manual review required)

### Step 4: Log Result
Record in `memory/daily/YYYY-MM-DD.md`:
```markdown
## LLM Judge Audit: [Task Name]
- **Score:** X/100
- **Issues:** [Brief summary]
- **Action:** [SHIPPED / FIXED / BLOCKED]
- **Learning:** [What to avoid next time]
```

## Integration Points

### Content Tasks (LinkedIn, Blog, Email)
Before `message` tool or file delivery:
1. Read generated content
2. Run LLM Judge prompt (insert content + original sources)
3. Parse response → extract score + issues
4. If score < 90: FIX or BLOCK (do NOT ship)

### Research Tasks (Gotham, Reports, Analysis)
Before committing results:
1. Extract key claims (names, numbers, affiliations)
2. Run LLM Judge prompt (cross-check against verified-truths.md)
3. If fabrications detected: DELETE fabricated data, mark as "unverified"

### Sub-Agent Tasks
Add to SUB-AGENT-CONTEXT.md:
```markdown
## Quality Gate: LLM as Judge (Mandatory for External Content)
Before delivery, sub-agents MUST:
1. Run self-audit prompt (see skills/capability-evolver/llm-as-judge-workflow.md)
2. Score < 90 → FIX
3. Fabrications detected → BLOCK
4. Log result in completion message
```

## Example: LinkedIn Carousel (Feb 27 Bug)

**WHAT WENT WRONG:**
- Carousel generated with "Stephanie Böhm (Grüne)"
- Delivered PDF to Florian
- THEN noticed error: Should be "Cornelia Böhm (CSU/FDP)"

**HOW LLM JUDGE WOULD HAVE CAUGHT IT:**

**Step 1: Generate Carousel** (existing)
- Output: carousel.html with candidate data

**Step 2: LLM Judge Prompt** (NEW)
```
Evaluate this carousel slide:

Candidate: Stephanie Böhm (Grüne)
vs. CSU

Original source data:
- Cornelia Böhm (CSU/FDP) vs. Grüne (Robert Göhl)

Are names and party affiliations correct?
```

**Step 3: LLM Judge Response**
```
Score: 20/100

Issues Found:
1. Name wrong: "Stephanie Böhm" should be "Cornelia Böhm"
2. Party wrong: "Grüne" should be "CSU/FDP"
3. Matchup inverted: Böhm is CSU/FDP, not facing CSU

Recommendation: BLOCK — Major factual errors, credibility risk.
```

**Step 4: Agent Action**
- BLOCK delivery
- Fix errors (Stephanie → Cornelia, Grüne → CSU/FDP)
- Re-run LLM Judge → Score 95/100 → SHIP

**Result:** Error caught BEFORE delivery, not after.

## Implementation Checklist

- [x] Workflow documented (this file)
- [ ] Add to Q1-BUILD-VERIFY.md (Step 0: Verify facts BEFORE design, Step 8: LLM Judge BEFORE delivery)
- [ ] Add to SUB-AGENT-CONTEXT.md (mandatory quality gate for external content)
- [ ] Test with next content task (LinkedIn post, email, carousel)
- [ ] Integrate with verified-truths.md (LLM Judge cross-checks claims against memory)
- [ ] Add to AGENTS.md (Task Loop Step 2.5: LLM Judge audit if external delivery)

## Success Metrics

**Goal:** Catch 90%+ of factual errors BEFORE delivery.

**Current Baseline (Feb 27):**
- Factual errors caught AFTER delivery: 1/1 (100%)
- Factual errors caught BEFORE delivery: 0/1 (0%)

**Target (7 days):**
- Factual errors caught BEFORE delivery: ≥ 90%
- External sends blocked due to LLM Judge: Track count
- LLM Judge false positives: < 10% (score < 90 but content was correct)

## Edge Cases

**Q: What if LLM Judge hallucinates (marks correct content as wrong)?**
A: Manual review required when score < 70. Log false positive, update verified-truths.md.

**Q: What if LLM Judge misses an error (score 95 but content wrong)?**
A: Post-delivery audit → update verified-truths.md → strengthen LLM Judge prompt with new error pattern.

**Q: What if no original sources available?**
A: LLM Judge prompt includes "unsourced claims" flag. Agent must mark claims as "unverified" or find sources.

## Meta-Learning

**Pattern:** Rules exist (Build-Verify, Q1 Standard) BUT not enforced at runtime.

**Fix:** LLM as Judge = automated enforcement gate (blocks delivery if quality < threshold).

**Next Level:** Chain LLM Judge with verified-truths.md → cross-check ALL claims against known facts → flag new claims for human verification → update verified-truths.md after confirmation.

---

*Version: 1.0 — 2026-02-27 05:00 CET — Created during Capability Evolution Cycle*
