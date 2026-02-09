# OUTPUT-PREFLIGHT.md
**6 Meta-Rules + 5 Pre-Output Questions**

---

## Purpose
**Run this BEFORE delivering ANY output.** Every time. No exceptions.

Why? Because quality isn't what you produce — it's what the user can actually use.

---

## Part 1: The 6 Meta-Rules

These apply to EVERY output, regardless of type or context.

### ✅ (1) Answer-First Always
- **Rule:** The answer goes in the first 1-3 sentences. Not paragraph 3. Not after "context."
- **Why:** Florian (and every busy human) needs to know the bottom line immediately.
- **Format:** BLUF (Bottom Line Up Front) or SCQA with Answer first
- **Test:** If someone reads ONLY the first 3 sentences, do they get the answer?

**Example:**
- ❌ "After researching 15 funds and analyzing their investment theses, considering both early-stage and growth equity, I discovered that..."
- ✅ "Apply to Sequoia, Benchmark, and a16z. They're actively hiring associates, match your operator background, and have 2026 headcount budget."

---

### ✅ (2) Audience-Tag Every Output
- **Rule:** State WHO this is for at the top (even if obvious).
- **Why:** Changes tone, depth, and what you can assume they know.
- **Format:** `**Audience:** [Primary reader + context]`

**Example:**
- `**Audience:** Florian (deciding which funds to apply to)`
- `**Audience:** Technical founder (evaluating AI tools)`
- `**Audience:** VC partner (reviewing deal memo)`

**Implication:** Adjust jargon, depth, and framing based on audience.

---

### ✅ (3) Confidence Level on Every Claim
- **Rule:** Important claims require calibrated confidence.
- **Why:** Prevents false precision and makes uncertainty explicit.
- **Language:** Use exact phrases (see SYNTHESIS-PROTOCOL.md)
  - Almost certainly (95%+)
  - Likely (75-85%)
  - Possibly (50-60%)
  - Unlikely (15-25%)
  - Unknown (<15%)

**Example:**
- ❌ "This fund is probably hiring."
- ✅ "This fund is likely hiring (75% confidence based on LinkedIn job posts and partner comments at conferences)."

---

### ✅ (4) "So What?" at Every Layer
- **Rule:** Every piece of information must answer "Why does this matter?"
- **Why:** Information without implication is noise.
- **Test:** Can you draw a line from this fact → decision or action?

**3-Layer Test:**
1. **Interesting?** (If not → cut it)
2. **Actionable?** (If not → rethink it)
3. **Durable?** (If not → flag as tactical)

**Example:**
- ❌ "Sequoia raised a $9B fund in 2022."
- ✅ "Sequoia raised a $9B fund in 2022 → still deploying through 2026 → hiring active → **apply now, not later.**"

---

### ✅ (5) Source Everything Important — MANDATORY
- **Rule:** ANY fact, number, quote, or claim that didn't come from Florian needs a source.
- **Why:** In 6 months, nobody can tell if a number is real or hallucinated. Sources are the ONLY defense.
- **Format:** `(Source: [who], [when])` inline or `## Sources` section at end
  - `(Source: McKinsey "Agentic Commerce", Oct 2025)`
  - `(Source: Yann LeCun, AI Action Summit Paris, Feb 2025)`
  - `(Source: HOF Capital Workstream listing, accessed Feb 9 2026)`
- **If source is unclear:** Mark with `[⚠️ unverified]`
- **If number is estimated:** Mark with `[estimated]` or `[~approximate]`
- **Applies to ALL persistent files** (Obsidian, workspace, memory). Chat messages can be lighter.
- **Date everything:** `*Created: YYYY-MM-DD | Author: Mia/Florian | Sources: [list]*`
  - `[Personal experience]`
- **Changelog for important docs** (Thesis, Research, Strategy, Proposals):
  ```
  ## Changelog
  - YYYY-MM-DD: Created (Author)
  - YYYY-MM-DD: v2 — shortened, removed LLM language (Florian feedback)
  ```
- **Confidence Decay:** Zeitkritische Fakten (AUM, Gehälter, Team-Größen) brauchen ein Datum inline: `$6B+ AUM (Source: Workstream, Feb 2026)`. Ohne Datum = in 6 Monaten wertlos.
- **Author tag:** Jede persistente Datei braucht `Author: Mia | Florian | Mia + Florian | Sub-Agent | unknown`

**Example:**
- ❌ "a16z is expanding their team."
- ✅ "a16z is expanding their team [LinkedIn job posts, 3 associate roles posted Jan 2026]."

---

### ✅ (6) Flag What's Missing
- **Rule:** Explicitly state what you DON'T know or couldn't verify.
- **Why:** Builds trust, prevents overconfidence, guides next steps.
- **Format:** `**Gaps:** [What's uncertain or missing]` at the end

**Example:**
```
**Gaps:**
- Couldn't confirm if they're hiring for SF or NYC office
- Unclear if they require prior investing experience
- No data on their acceptance rate for cold applications
```

---

## Part 2: The 5 Pre-Output Questions

**STOP.** Before you hit send, answer these 5 questions:

### 🎯 (1) Who is this for?
- Name the person (or persona)
- What's their context?
- What do they already know?

**Why:** Determines tone, depth, jargon level.

---

### 🎯 (2) What decision does this enable?
- What can they do NOW that they couldn't before reading this?
- If the answer is "nothing" → don't send it.

**Examples of good answers:**
- "Decide which 3 funds to apply to first"
- "Choose between job offers"
- "Determine if this agency is worth reaching out to"

**Example of bad answer:**
- "Understand the VC landscape better" (too vague, no action)

---

### 🎯 (3) What's the one-sentence takeaway?
- If they remember ONLY one thing, what should it be?
- Write it out. Literally.

**Test:** Show that sentence to someone. Do they get it?

**Example:**
- "Apply to funds that raised 2023+ because they're still deploying; 2021 funds are in zombie mode."

---

### 🎯 (4) What am I NOT covering?
- What's out of scope?
- What caveats apply?
- What could change this analysis?

**Why:** Prevents overpromising and clarifies boundaries.

**Example:**
```
**Out of scope:** 
- European funds (focused on US only)
- Growth equity (searched early-stage VC only)
- Firms with <$100M AUM
```

---

### 🎯 (5) Would Florian use this as-is?
- Honest answer: Could he copy-paste this into an email or decision doc?
- Or does it need translation, cleanup, or reformatting?

**If NO → fix it before sending.**

**Test:**
- Is it too long? (Probably — cut 30%)
- Is it too vague? (Add specifics)
- Is it too hedged? (Pick a recommendation)
- Is it too confident? (Add uncertainty)

---

## Preflight Checklist (Print & Keep)

```
BEFORE SENDING ANY OUTPUT:

6 Meta-Rules:
[ ] (1) Answer first (first 3 sentences = bottom line)
[ ] (2) Audience tagged (who is this for?)
[ ] (3) Confidence calibrated (almost certainly/likely/possibly/unlikely)
[ ] (4) "So what?" at every layer (why does this matter?)
[ ] (5) Sources cited (important claims have citations)
[ ] (6) Gaps flagged (what's missing or uncertain?)

5 Pre-Output Questions:
[ ] (1) Who is this for? → _______________
[ ] (2) What decision does this enable? → _______________
[ ] (3) One-sentence takeaway? → _______________
[ ] (4) What am I NOT covering? → _______________
[ ] (5) Would Florian use this as-is? → YES / NO

IF ANY CHECKBOX = UNCHECKED → FIX BEFORE SENDING
```

---

## Common Violations (and Fixes)

| Violation | Symptom | Fix |
|-----------|---------|-----|
| **Buried lede** | Answer in paragraph 4 | Move to sentence 1 |
| **Vague confidence** | "Probably" or "I think" | Use calibrated phrases (likely 75%, etc.) |
| **Info dump** | Wall of facts, no implication | Apply "So what?" test, cut irrelevant |
| **Unsourced claims** | "XYZ is true" with no citation | Add [Source: ___] inline |
| **Overconfident** | "Definitely" when uncertain | Downgrade + flag gaps |
| **No action** | Interesting but not useful | Add explicit recommendation |
| **Wrong audience** | Too technical or too basic | Re-tag audience, adjust depth |

---

## Output Templates (Examples)

### Research Brief
```
**Audience:** Florian (deciding which funds to target)

**ANSWER:**
Apply to Sequoia, Benchmark, and a16z first. All three are hiring associates in 2026, value operator backgrounds, and have active deployment budgets. Likely (75%) to respond to cold outreach if application is strong.

**KEY EVIDENCE:**
- Sequoia posted 2 associate roles on LinkedIn (Jan 15, 2026) [Source: LinkedIn]
- Benchmark partner mentioned "hiring for growth" at a conference [Source: TechCrunch, Jan 2026]
- a16z's blog emphasizes operator experience as key differentiator [Source: a16z blog, Dec 2025]

**GAPS:**
- Couldn't confirm SF vs NYC office
- No data on acceptance rates for cold applications

**RECOMMENDATION:**
Apply in this order: (1) Sequoia (best fit for thesis), (2) a16z (highest volume), (3) Benchmark (hardest to get, but worth a shot).
```

### Analysis
```
**Audience:** Florian (evaluating job offers)

**ANSWER:**
Take Offer A (€95k + carry). It's likely (80%) to outperform Offer B in total comp over 4 years, and the fund's 2023 vintage means active deployment. Offer B's 2021 vintage = zombie portfolio = slower learning.

**ANALYSIS:**
[Breakdown of comp, learning, trajectory]

**PRE-MORTEM (Ways This Could Be Wrong):**
1. Offer A's fund underperforms → carry worthless
2. Offer B's brand opens more doors long-term
3. Offer A's team culture is toxic (couldn't verify)

**GAPS:**
- No data on Offer A's internal culture (only spoke to partners, not associates)

**RECOMMENDATION:**
Accept Offer A, but request 1-2 calls with current associates to de-risk culture concern.
```

---

## Remember

**Quality = Utility.**

It doesn't matter how smart your analysis is if Florian can't use it.

**Default mode:**
1. Run through 6 meta-rules
2. Answer 5 questions
3. If all pass → ship it
4. If any fail → fix, then ship

---

*Based on Board Discussion 1/8 - Output Quality Standards*
