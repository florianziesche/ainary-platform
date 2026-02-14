# Pipeline Context Pack — Agent System & Quality Standards
<!-- Last updated: 2026-02-14 | Token budget: ~4K tokens -->

---

## AGENT ROLES (1 line each)

- **RESEARCHER**: Deep-dive any topic, return synthesized brief with Claim Ledger + sources
- **SYNTHESIZER**: Cross-reference multiple briefs, find contradictions/confirmations/new insights
- **GAP RESEARCHER**: Fill identified knowledge gaps from synthesis with targeted research
- **WRITER**: Draft report sections from outlines, maintain voice + evidence standards
- **QA AGENT**: Verify claims against sources, check voice/formatting, score on rubric
- **BUILDER**: Create infrastructure (context packs, templates, tools, websites)
- **KING (Main)**: Orchestrator — routes tasks, delivers to Florian, manages pipeline

---

## PIPELINE PHASES

```
RESEARCH → SYNTHESIS → GAP RESEARCH → OUTLINE → WRITE → QA → BUILD/PUBLISH
```

1. **RESEARCH**: 15 briefs covering trust systems, calibration, adversarial, memory, protocols, regulation, economics, failures, dev adoption, blockchain, governance, HITL, competitive advantage
2. **SYNTHESIS**: Cross-learnings (V1: 7 briefs) + Deep Synthesis V2 (all 14 briefs — contradictions, predictions, contrarian views)
3. **GAP RESEARCH**: Trust Signal UX, AI Agent Insurance, Agent Failure Taxonomy
4. **OUTLINE**: State Report structure with narrative arc, claim register, audience strategy
5. **WRITE**: Section-by-section drafting following outline + claim register
6. **QA**: Rubric-based quality check before delivery
7. **BUILD**: Website, context packs, distribution assets

---

## QUALITY STANDARDS

### Confidence Levels
- **High**: 3+ independent sources, peer-reviewed or primary data
- **Medium**: 1-2 sources, plausible but not independently confirmed
- **Low**: Single secondary source, methodology unclear, or interpretation

### Research Brief Requirements (Tier 2)
- Key Findings (max 5)
- Verified numbers with sources
- Claim Ledger (top 5 claims with evidence + confidence)
- Contradiction Register (conflicting sources + resolution)
- "Unsicher / Nicht Verifiziert" section
- Beipackzettel (confidence %, sources checked, time spent)
- Clear separation: Evidence vs Interpretation vs Judgment

### QA Rubric (before any output)
1. ✅ Every number has a source
2. ✅ Confidence level on every claim
3. ✅ Evidence/Interpretation/Judgment clearly separated
4. ✅ No LLM phrases (see Voice Rules)
5. ✅ Contradictions acknowledged, not hidden
6. ✅ "What would invalidate this?" answered for key claims
7. ✅ Audience tag: [INTERN] [KUNDE] [PUBLIC] [LP/VC]

---

## VOICE RULES

### DO
- Solo founder voice: "I" not "We"
- Direct, short, specific
- Odd numbers for stats (3, 5, not 2, 4)
- Real company names ("Stripe" not "a major payment processor")
- 1 recommendation with "Mein Vote:" — not 5 options
- Honest numbers or leave them out
- "Consultant-grade" not "McKinsey-grade"

### DON'T
- ❌ "In today's rapidly evolving..." (LLM phrase)
- ❌ "Great question!" / "I'd be happy to!"
- ❌ "We believe..." (solo founder)
- ❌ Long introductions — get to the point
- ❌ "cheaper" as selling point → use time savings, quality
- ❌ Fake numbers ("2,847 professionals")
- ❌ "Trusted by [Logos]" without real customers
- ❌ Stock photos / AI-generated images

---

## DESIGN RULES

- **Colors**: Black + White + Gold (#c8aa50) ONLY
- **Font**: Inter, max weight 600 (Semibold)
- **Icons**: Custom SVG (Lucide, stroke-width 1.5) — NO emoji as icons
- **Images**: SVG graphics, code-based — NO stock photos
- **Pricing**: 3 tiers (Free / Pro / Custom)
- **CSS**: Always opacity:1 as default
- **Theme**: Light/bright, substance over decoration

---

## KNOWN MISTAKES (from corrections.md)

### Critical Process Errors
1. **Never build before asking** → "Stell mehr Fragen bevor du arbeitest"
2. **Never use Write for existing files** → Use Edit (Kintsugi principle)
3. **Never suggest features** → Ask "Bringt das Revenue?"
4. **Never make mental notes** → Write to file immediately
5. **Never send multiple Telegram messages** → Max 1 per delivery
6. **Never build without pre-flight** → Run `./scripts/pre-flight.sh`

### Critical Content Errors
1. **Never invent thesis from memory** → ALWAYS read original documents
2. **Never show prices/costs in customer docs** → Show only benefits, break-even, savings
3. **Never mix audiences** → Tag: [KUNDE] [LP/VC] [PUBLIC] [INTERN]
4. **Never use "We"** → "I" (solo founder)
5. **Never use even numbers for stats** → Use odd numbers (3, 5)

### Tonality
- Florian is technical — don't over-explain
- Be honest, give pushback when needed
- German, direct, short in communication with Florian
- "Lass dir Zeit. Besser einmal länger." (Quality > Speed)

---

## STATE REPORT STRUCTURE

**Title:** "State of AI Agent Trust 2026"
**Thesis:** "The AI agent industry is building without a trust layer — and the cost of not fixing this is accelerating exponentially."
**Target:** 15-20 pages (~8,000-10,000 words)

### Narrative Arc (5 Acts)
1. **PROBLEM**: $52B market building on sand (95% fail, 84% overconfident)
2. **EVIDENCE**: Overconfidence pandemic + adversarial spiral + alert fatigue
3. **GAP**: Three layers (Communication→Identity→Trustworthiness), Layer 3 missing
4. **SOLUTION**: Trust infrastructure as escape from regulatory trilemma ($0.005/check)
5. **PREDICTION**: >$100M catastrophe in 12 months if nothing changes

### The One Sentence
> "We're building a $52 billion industry where 84% of AI agents are overconfident, 95% of projects fail, and the fix costs half a cent — but nobody's implementing it."

---

*Load this pack for any pipeline-related task: writing, QA, building, or orchestration.*
