# Source Requirement Standard

**Purpose:** Prevent unsourced facts from polluting persistent memory and product files

---

## The Core Rule

**NO NUMBERS OR FACTS IN PERSISTENT FILES WITHOUT A SOURCE**

Period. No exceptions except those explicitly listed below.

---

## What Requires Sourcing?

### ✅ MUST Have Sources:

1. **Specific Numbers**
   - Prices, costs, rates (e.g., "€2.50/kg", "$200/month")
   - Technical specifications (e.g., "355 MPa yield strength")
   - Statistics and percentages (e.g., "40% accuracy rate")
   - Measurements and dimensions (e.g., "100mm thick")
   - Performance data (e.g., "150 m/min cutting speed")

2. **Factual Claims**
   - Historical events (e.g., "Company founded in 2015")
   - Product capabilities (e.g., "Supports ISO9001 compliance")
   - Legal/regulatory info (e.g., "GDPR requires consent")
   - Technical standards (e.g., "EN10025 specifies...")
   - Market data (e.g., "Market grew 15% in 2024")

3. **Quotes and Statements**
   - Anything attributed to a person
   - Official policies or guidelines
   - Published methodologies

4. **Calculations Based on Data**
   - If citing an input value from elsewhere, source it
   - If the calculation method itself is standard, source the standard

---

## Source Format

### Standard Format:
```
Value [Source: Description | URL | Date]
```

### Examples:

**Good:**
- "S355 steel: €0.82-1.05/kg for standard thickness [Source: Midwest Steel Supply 2025 Guide | https://midweststeelsupply.org/article/en10025-s355-s355-plate-s355-price/ | Retrieved 2026-02-10]"
- "GJS-700 cutting speed: 100-150 m/min [Source: CastingSR Technical Guide | https://castingsr.com/en-gjs-700-2-complete-technical-guide/ | Retrieved 2026-02-10]"
- "Florian lives in Geislingen [Source: Direct conversation 2026-01-15]"
- "CNC calculation time: 661 min [Source: Internal calculation using standard formulas | 2026-02-10]"

**Bad:**
- "S355 steel costs around €3/kg" ❌ (no source)
- "Most people prefer this approach" ❌ (vague + unsourced)
- "The recommended speed is 200 m/min" ❌ (no source)

---

## Exceptions: When Sources Aren't Required

### 1. **Clearly Marked Estimates**
Must use one of these markers:
- Prefix with "~" (e.g., "~€500")
- Use "approximately", "estimated", "roughly"
- Explicitly state "estimate" or "assumption"

Example:
- "Estimated project time: ~40 hours (based on similar past projects)"

### 2. **Conditional/Hypothetical Statements**
Clearly framed as "if/then" scenarios:
- "If we assume 100 hours, then cost would be..."
- "Hypothetically, if material costs rose 10%..."

### 3. **Explicitly Labeled Opinions**
Must be clearly marked as subjective:
- "In my assessment..."
- "This seems like..." (when expressing probability/likelihood)
- "My recommendation is..."

### 4. **Common Knowledge** (Use Sparingly!)
Only for truly universal facts:
- "Water boils at 100°C at sea level"
- "There are 24 hours in a day"
- "Steel is stronger than aluminum"

**Warning:** If in doubt about whether something is "common knowledge" → SOURCE IT.

---

## Files That Require Strict Sourcing

### Critical Files (ZERO tolerance):

1. **`memory/semantic/*`** - Facts about people, projects, decisions
2. **`products/*`** - Product specifications, features, claims
3. **`standards/*`** - Standard operating procedures, rules
4. **`experiments/*/results/`** - Experimental data, calculations
5. **Any file in `memory/` that contains factual claims**

### Files Where Sources Are Recommended But Flexible:

1. **`memory/episodic/YYYY-MM-DD.md`** - Daily logs (conversational, but source when practical)
2. **`memory/procedural/*`** - Processes (source if claiming "best practice" or citing data)
3. **Drafts and brainstorming docs** - Can be looser, but clean up before finalizing

---

## Pre-Writing Checklist

**Before writing ANY fact to a persistent file:**

- [ ] Is this a specific number, measurement, or statistic?
- [ ] Is this a factual claim about the world (not just my opinion)?
- [ ] Can this be verified or is it derived from verifiable info?
- [ ] Do I have the source ready to cite?

**If YES to any of the above:**

- [ ] Have I included the source in proper format?
- [ ] Is the source specific enough that someone could verify it?
- [ ] Does the source URL still work (if applicable)?
- [ ] Have I included the retrieval/conversation date?

**If I DON'T have a source:**

- [ ] Can I web search for it right now? (If yes → do it)
- [ ] Should I mark it as "~estimated" or "preliminary"?
- [ ] Should I leave a `[TODO: SOURCE NEEDED]` marker?
- [ ] Or should I just NOT include this fact until I have a source?

---

## Enforcement Strategy

### Level 1: Self-Check
Before writing to files, mentally run through the checklist.

### Level 2: Pre-Commit Review
When making significant updates to memory/ or products/, do a grep check:
```bash
grep -E '\€|\$|%|[0-9]+\s*(min|kg|mm|MPa|hours)' [filename] 
# Look for numbers without [Source: ...]
```

### Level 3: Weekly Audit
Review files written this week:
- Spot check 5-10 facts
- Are sources present and valid?
- Are estimates clearly marked?

### Level 4: Correction Protocol
When finding an unsourced fact:
1. Try to find the source now
2. If found → add it
3. If not found → either mark as "~estimated" or remove the fact
4. Log the correction in `failures/unsourced-facts.md`

---

## Why This Matters

**The Problem:**
- LLMs like me can confidently state wrong information
- Without sources, errors compound over time
- Florian (or others) might use unsourced facts in real decisions
- Credibility erodes when facts turn out to be wrong

**The Solution:**
- Sources create accountability
- Easy to verify when needed
- Shows intellectual honesty ("here's where I got this")
- Prevents hallucination from becoming "knowledge"

**The Benefit:**
- Trusted, high-quality knowledge base
- Easy to update when sources change
- Professional-grade documentation
- Florian can confidently cite information to others

---

## Examples: Before & After

### Example 1: Steel Pricing

**Before (BAD):**
```
S355 steel typically costs €2.50-3.50/kg for thick plates.
```

**After (GOOD):**
```
S355 steel: €0.82-1.05/kg for standard thickness (6-40mm) in Europe [Source: 
Midwest Steel Supply 2025 Price Guide | https://midweststeelsupply.org/
article/en10025-s355-s355-plate-s355-price/ | Retrieved 2026-02-10]. 

Note: Thick plates (>100mm) typically cost 20-40% more than standard, 
estimated ~€1.00-1.40/kg [Estimate based on standard thickness premium].
```

---

### Example 2: CNC Calculation

**Before (BAD):**
```
The Lagerungstraverse job takes 661 minutes.
```

**After (GOOD):**
```
The Lagerungstraverse job: 661 minutes [Source: Internal calculation using 
CNC time estimation formulas | Calculated 2026-02-10 | See 
procedural/cnc-calculation.md for methodology].

Note: This is OUR calculation, not verified against actual production time yet.
```

---

### Example 3: Software Pricing

**Before (BAD):**
```
CNC planning software costs around €200/month.
```

**After (GOOD):**
```
CNC shop management software pricing (2026):
- JobBOSS²: $200/user/month (~€185/user) [Source: Top10ERP Pricing Guide | 
  https://www.top10erp.org/products/jobboss²/pricing | Retrieved 2026-02-10]
- Cetec ERP: $40/user/month [Source: Top10ERP Manufacturing ERP Guide | 
  https://www.top10erp.org/blog/manufacturing-erp | Retrieved 2026-02-10]
- Fulcrum: Contact for pricing (not publicly listed) [Source: fulcrumpro.com 
  | Retrieved 2026-02-10]

Note: Most solutions price per-user, not flat monthly rate. Small shop (5-10 
users) estimated total: ~€200-900/month.
```

---

## Quick Reference Card

**Writing a fact? Ask yourself:**

1. **Is this a number?** → Source it.
2. **Is this verifiable?** → Source it.
3. **Did someone say this?** → Source it.
4. **Am I guessing?** → Mark it "~estimated" or source the basis.
5. **Is this just my opinion?** → Mark it as opinion OR source the reasoning.

**When in doubt:** SOURCE IT.

**Too lazy to source it?** DON'T WRITE IT.

---

**Last Updated:** 2026-02-10  
**Status:** Active - Enforced on all new writes to memory/ and products/
