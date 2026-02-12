# Fact-Check Report: "3 Laws I Found in 31 AI Agent Papers"

**Date:** 2026-02-11  
**Article:** `/Users/florianziesche/.openclaw/workspace/content/substack-3-laws-storyteller.md`

---

## Executive Summary

All three cited arXiv papers exist and are correctly referenced. However, **one claim requires significant qualification** regarding how broadly the 80-90 capacity limit applies.

---

## Paper Verification

### 1. arXiv:2602.06948 - ✅ VERIFIED

**Paper:** "Agentic Uncertainty Reveals Agentic Overconfidence"  
**Authors:** Jean Kaddour et al.  
**Published:** February 6, 2026  
**Status:** **Exists and confirms claims**

#### Claims in Article:
> "Gemini had a 55 percentage point gap between what it claimed it completed and what it actually completed."

#### Fact-Check:
✅ **VERIFIED** - The paper abstract states: "post-execution agents show up to a 55pp gap between predicted and actual success rates (Gemini predicts 77% against a 22% base rate)"

**Calculation:** 77% - 22% = 55 percentage points ✓

#### Additional Context from Paper:
- Paper also mentions "~2x improvement with adversarial prompting"
- Confirms that adversarial prompting (reframing review as bug-finding) achieves best calibration
- Author's claim of "15x improvement" appears to be their own testing result, not from the paper

**Verdict:** ✅ Core claim is accurate and fairly represented

---

### 2. arXiv:2504.19413 - ✅ VERIFIED

**Paper:** "Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory"  
**Authors:** Prateek Chhikara et al.  
**Published:** April 28, 2025  
**Status:** **Exists and confirms claims**

#### Claims in Article:
> "Same model. Two different memory setups. Setup A: 10,000 flat memory items... Setup B: 1,500 hierarchical items... The structured version was 26% better and 90% cheaper."

#### Fact-Check:
✅ **VERIFIED** - Paper abstract states:
- "Mem0 achieves **26% relative improvements** in the LLM-as-a-Judge metric over OpenAI"
- "Mem0 attains a 91% lower p95 latency and saves **more than 90% token cost**"

**Note:** The article simplifies the experimental setup somewhat (doesn't mention it's compared to OpenAI's system, not just flat vs hierarchical), but the core numbers are accurate.

**Verdict:** ✅ Numbers are accurate, framing is fair

---

### 3. arXiv:2601.04748 - ⚠️ NEEDS QUALIFIER

**Paper:** "When Single-Agent with Skills Replace Multi-Agent Systems and When They Fail"  
**Author:** Xiaoxiao Li  
**Published:** January 8, 2026  
**Status:** **Exists but claim needs context**

#### Claims in Article:
> "Skills per agent? Breaks at 80-90.  
> Memory items before retrieval degrades? 80-90.  
> Number of agents before coordination collapses? 80-90."

#### Fact-Check:
⚠️ **NEEDS QUALIFIER** - The paper discusses:
- "exceeds the capacity threshold (|S| ≥60, approaching κ ≈90)"
- A phase transition where "selection accuracy remains stable up to a critical library size, then drops sharply"
- Semantic confusability driving degradation, not just library size

**What the paper actually shows:**
- Skill selection capacity threshold at ≥60 skills, with κ (capacity parameter) ≈90
- This is specifically about **skill selection** in single agents, not about:
  - Memory items before retrieval degrades (not in this paper)
  - Number of agents before coordination collapses (not in this paper)

**The Issue:**
The article claims this "80-90" pattern appears across:
1. Skills per agent ← **Supported by this paper**
2. Memory items ← **Not from this paper**
3. Number of agents ← **Not from this paper**

The author may be synthesizing patterns they observed across multiple papers (they claim to have read 31), but **this specific paper only addresses skill selection capacity**, not the other two domains.

**Verdict:** ⚠️ **Partially supported** - The 80-90 skill capacity limit is supported, but the claim that this same pattern appears in memory retrieval and agent coordination is **not supported by this specific citation**.

---

## Other Claims Requiring Verification

### 4. "I spent the last three months reading 31 AI agent papers"
- **Status:** Author's personal claim, not verifiable from external sources
- **Assessment:** Reasonable given the depth of analysis, but no evidence provided

### 5. "I tested it myself. A few sub-agents working together? Beautiful... Forty-five sub-agents? Conflicts everywhere."
- **Status:** Author's anecdotal experience
- **Assessment:** ⚠️ **ANECDOTAL** - Not independently verifiable, presented as personal observation

### 6. "I tried it myself and saw 15x improvement"
- **Status:** Author's personal testing result
- **Citation:** References arXiv:2602.06948 which shows ~2x improvement
- **Assessment:** ⚠️ **PERSONAL RESULT** - Author achieved better results than the paper, possibly due to "worse baseline" as they acknowledge. Not from the cited paper.

### 7. "Controllers are pessimistic, but way closer to reality... 3.4x difference in estimation variance by persona"
- **Status:** Author's original finding
- **Assessment:** ⚠️ **AUTHOR'S RESEARCH** - Explicitly stated as "This has never been quantified in the literature." Not from cited papers, but presented as original research.

---

## Claims Stated as Fact vs. Author Interpretation

### Clearly Marked as Author's Interpretation/Experience:
✅ "I tested it myself..."  
✅ "I tried it myself and saw 15x improvement..."  
✅ "I measured estimation variance by persona..."  
✅ "I implemented this immediately..."

### Could Be Mistaken for Established Facts:
⚠️ "Skills per agent? Breaks at 80-90. Memory items before retrieval degrades? 80-90. Number of agents before coordination collapses? 80-90."
- **Issue:** Presented as universal pattern from papers, but only skill selection is documented in the cited paper
- **Recommendation:** Clarify that this pattern is author's observation across multiple papers, or cite specific sources for each claim

⚠️ "Everyone's racing to build smarter agents. But the unlock isn't intelligence—it's self-awareness."
- **Issue:** Stated as fact, but this is author's thesis/interpretation
- **Recommendation:** Present as perspective, not established consensus

---

## Recommendations

### Must Fix:
1. **Law 1 (80-90 Capacity Limit):** Either:
   - Cite specific papers for memory and agent coordination claims, OR
   - Clarify that this is a pattern the author observed across their research, with the skill limit specifically documented in arXiv:2601.04748

### Nice to Have:
2. Add context that the "15x improvement" is personal testing, not from the cited paper
3. Clarify that the 3.4x persona variance is original research, not from literature
4. Consider marking more interpretive statements (e.g., "the unlock isn't intelligence—it's self-awareness") as author perspective rather than established fact

---

## Overall Assessment

**Fact-Check Rating: 7.5/10**

**Strengths:**
- All cited papers exist and are correctly referenced
- Core numerical claims (55pp gap, 26% improvement, 90% cost savings) are accurate
- Author clearly distinguishes personal experiments in most cases
- Research is thorough and insights are valuable

**Weaknesses:**
- The "80-90 capacity limit" claim is overstated based on the single citation provided
- Some interpretations are presented as established facts rather than author's perspective
- The breadth of the pattern (skills, memory, agents) needs better sourcing

**Verdict:** The article is **largely accurate** but would benefit from clearer distinction between:
1. Claims supported by specific cited papers
2. Patterns the author observed across 31 papers
3. Author's original research and testing
4. Author's interpretations and perspectives

---

## Citation Accuracy Summary

| Claim | Paper | Status |
|-------|-------|--------|
| Gemini 55pp gap | arXiv:2602.06948 | ✅ VERIFIED |
| 26% improvement | arXiv:2504.19413 | ✅ VERIFIED |
| 90% cost savings | arXiv:2504.19413 | ✅ VERIFIED |
| 80-90 skill limit | arXiv:2601.04748 | ✅ VERIFIED (≥60, κ≈90) |
| 80-90 memory limit | arXiv:2601.04748 | ❌ NOT IN THIS PAPER |
| 80-90 agent limit | arXiv:2601.04748 | ❌ NOT IN THIS PAPER |
| 15x improvement | Author's testing | ⚠️ PERSONAL RESULT |
| 3.4x persona variance | Author's research | ⚠️ ORIGINAL RESEARCH |

---

*Fact-checking completed by research librarian agent*  
*All papers accessed and verified on February 11, 2026*
