# Ainary Standards

**Production-grade quality standards for all output types.**

This directory contains the rules, protocols, and checklists that govern how work is done in the Ainary Platform. Every standard is opinionated, specific, and enforced.

---

## Philosophy

**Why standards matter:**
- **Consistency:** Same quality bar across all outputs, regardless of agent or human
- **Scalability:** New agents/humans can onboard by reading standards, not tribal knowledge
- **Auditability:** Clear pass/fail criteria for every output type
- **Learning:** Violations become corrections, corrections become rules, rules improve standards

**What makes a good standard:**
1. **Specific:** "No LLM phrases" with examples > "Be concise"
2. **Measurable:** Pass/fail criteria, not subjective judgment
3. **Actionable:** Clear steps to comply, not abstract principles
4. **Justified:** Explain the "why" — rationale beats rules

---

## Standards Overview

| Standard | Purpose | For |
|----------|---------|-----|
| **[RESEARCH-PROTOCOL.md](RESEARCH-PROTOCOL.md)** | MECE framework, hypothesis-driven research, source verification | Research reports, deep dives |
| **[CONTENT-VOICE.md](CONTENT-VOICE.md)** | Anti-LLM voice, human tone, no bullshit | Blog posts, LinkedIn, articles, emails |
| **[Q1-BUILD-VERIFY.md](Q1-BUILD-VERIFY.md)** | 7-step verification for every code change | All software development |
| **[Q2-DEVELOPMENT-INTAKE.md](Q2-DEVELOPMENT-INTAKE.md)** | WAS/WARUM/SCOPE before any build | Feature requests, bug fixes, refactors |
| **[WEBSITE-DESIGN-GUIDE.md](WEBSITE-DESIGN-GUIDE.md)** | Typography, layout, spacing, interactions | Website design, landing pages |
| **[BRAND.md](BRAND.md)** | Visual identity, voice, positioning | All public-facing content |
| **[FLORIAN.md](FLORIAN.md)** | Personal context for AI agents | Email drafts, outreach, anything in Florian's voice |
| **[S1-ERSTTERMIN-PREP.md](S1-ERSTTERMIN-PREP.md)** | Client meeting prep checklist | Consulting, sales meetings |
| **[R2-DEEP-DIVE-RESEARCH.md](R2-DEEP-DIVE-RESEARCH.md)** | Deep dive research standard (15/15 quality gate) | R2-tier research reports |
| **[SYNTHESIS-PROTOCOL.md](SYNTHESIS-PROTOCOL.md)** | Cross-source synthesis, pattern identification | Multi-source research, literature reviews |
| **[AGENT-CONTEXT-PACKAGE.md](AGENT-CONTEXT-PACKAGE.md)** | What context to load for what task | Agent system rules |

---

## Standards by Use Case

### When Writing Content

**Load:** [CONTENT-VOICE.md](CONTENT-VOICE.md)

**Rules:**
- No LLM phrases ("I'd be happy to", "delve into", "foster", "leverage")
- Active voice > passive voice (90% active)
- Short sentences (median <15 words)
- Specific > vague ("3x throughput" not "significant improvement")
- Human voice (I/we, not "one" or "the author")

**Anti-patterns:**
- ❌ "I'd be happy to explore this fascinating topic."
- ✅ "Let's look at three examples."

---

### When Conducting Research

**Load:** [RESEARCH-PROTOCOL.md](RESEARCH-PROTOCOL.md)

**Process:**
1. **Hypotheses first** — State 3-5 hypotheses before searching
2. **MECE structure** — Mutually exclusive, collectively exhaustive categories
3. **Source verification** — Every claim needs a citation
4. **Confidence calibration** — Rate certainty (HIGH/MEDIUM/LOW) per finding
5. **Try to disprove** — Seek contradictory evidence, not just confirmation

**Output format:**
```markdown
## Finding 1
**[Confidence: 85%] Title**
Description. Specific evidence. Nuance/limitations.
*Source: Author (Year), Link*
```

---

### When Building Software

**Load:** [Q2-DEVELOPMENT-INTAKE.md](Q2-DEVELOPMENT-INTAKE.md) + [Q1-BUILD-VERIFY.md](Q1-BUILD-VERIFY.md)

**Before coding (Q2):**
- WAS: What are we building?
- WARUM: Why? What problem does it solve?
- SCOPE: What's in, what's out, done when?
- FERTIG WENN: Explicit definition of "done"

**After coding (Q1):**
1. ✅ Code runs without errors
2. ✅ All new endpoints tested (curl/Postman)
3. ✅ Browser test (if UI changed)
4. ✅ Screenshot of changes (if visual)
5. ✅ No unintended changes (git diff review)
6. ✅ Database backup (if schema changed)
7. ✅ Documentation updated

**Violation = Trust score decreases.** No commits without verification.

---

### When Designing Websites

**Load:** [WEBSITE-DESIGN-GUIDE.md](WEBSITE-DESIGN-GUIDE.md) + [BRAND.md](BRAND.md)

**Typography:**
- Headings: Inter (600 weight)
- Body: Inter (400 weight)
- Code: JetBrains Mono
- Scale: 14px → 16px → 20px → 24px → 32px → 48px

**Spacing:**
- Vertical rhythm: 8px base unit (8, 16, 24, 32, 48, 64, 96)
- Section padding: 64px min, 96px desktop
- Container max-width: 1200px

**Colors:**
- Background: `#FAFAFA` (warm off-white)
- Text: `#1A1A1A` (near-black)
- Accent: `#0066CC` (blue) or `#FF6B35` (orange)
- Borders: `#E5E5E5` (subtle gray)

**Interactions:**
- Transitions: 200ms ease-out (subtle, fast)
- Hover: Subtle color shift, no transform
- Focus: 2px outline, accessible contrast

---

## Checklists

### Before Any Output

**File:** [checklists/before-any-output.md](checklists/before-any-output.md)

- [ ] Does it answer the user's question?
- [ ] Is every claim sourced or marked "unverified"?
- [ ] No LLM phrases?
- [ ] Confidence stated (if uncertain)?
- [ ] Actionable (if applicable)?

### Before Delivery

**File:** [checklists/before-delivery.md](checklists/before-delivery.md)

- [ ] Re-read original requirements
- [ ] Check all links work
- [ ] Spelling/grammar check
- [ ] If email: subject line clear?
- [ ] If PDF: rendered correctly?
- [ ] If code: verified per Q1?
- [ ] If research: sources cited?

---

## How Standards Evolve

### Correction → Rule → Standard

1. **Violation detected** — AI or human makes a mistake
2. **Correction created** — Stored in corrections table with pattern + severity
3. **Pattern emerges** — Same mistake type repeats 3+ times
4. **Rule formalized** — Added to relevant standard file
5. **Pre-flight enforcement** — Automated check added (L1 or L2)

**Example:**
1. Email draft includes "I'd be happy to help" (LLM phrase)
2. Florian corrects → Correction #5: "No LLM phrases in emails"
3. Same phrase appears in 2 more emails
4. Rule added to CONTENT-VOICE.md with 15 example phrases
5. Regex check added to Pre-Flight L1: `/(I'd be happy|delve into|leverage)/i`
6. Future violations auto-flagged before human sees output

---

## Standard Maintenance

### Who Can Edit

- **Florian:** All standards
- **Mia (main agent):** Can propose edits, requires Florian approval
- **Sub-agents:** Read-only (no edits)

### Update Frequency

- **Quarterly review:** Q1, Q2, Q3, Q4 — review all standards for relevance
- **Ad-hoc updates:** When new patterns emerge (3+ violations of same type)
- **Version control:** All changes in Git with commit messages explaining "why"

### Standard Retirement

A standard can be retired if:
1. No violations in 6 months (fully internalized)
2. Superseded by new standard
3. No longer relevant (e.g., tool deprecated)

Retired standards move to `standards/archive/`.

---

## Relationship to Other Systems

### Standards → Pre-Flight Checks

Standards inform the 3-layer Pre-Flight engine:

- **L1 (Regex):** Automated checks for CONTENT-VOICE violations
- **L2 (Structural):** Schema validation per output type (email has subject, blog has title, etc.)
- **L3 (LLM):** Semantic checks for complex rules (persuasiveness, clarity)

[See [ARCHITECTURE.md](../ARCHITECTURE.md) for Pre-Flight details]

### Standards → Corrections

Corrections are violations of standards. The corrections engine tracks:
- Which standard was violated
- Pattern (what triggered it)
- Severity (low/medium/high)
- Fix (how to correct it)

[See [workbench/README.md](../projects/workbench/README.md) for Correction Engine details]

### Standards → Trust Scores

Trust scores track compliance with standards per skill domain:
- High trust (>60): Auto-execute, no review
- Medium trust (30-60): Review before execution
- Low trust (<30): Confirmation required

[See [FORMULAS.md](../projects/workbench/FORMULAS.md) for Trust calculation]

---

## Standard Template

When creating a new standard, use this structure:

```markdown
# [Standard Name]

**Purpose:** One sentence — why this standard exists  
**Applies to:** [Output types]  
**Enforcement:** [Manual / L1 / L2 / L3]

---

## The Rule

[Clear statement of the rule]

**Why it matters:** [Rationale]

---

## Good Examples

[3-5 examples of compliance]

---

## Bad Examples (Anti-patterns)

[3-5 examples of violations]

---

## Checklist

- [ ] Item 1
- [ ] Item 2
- [ ] Item 3

---

**Confidence:** [How certain are we this is the right rule?]  
**Last Updated:** YYYY-MM-DD  
**Owner:** [Florian / Team]
```

---

## FAQ

**Q: What if a standard conflicts with user request?**  
A: User request wins. Flag the conflict, explain the standard, execute as requested. Log the override.

**Q: What if a standard is wrong?**  
A: Challenge it. Propose an edit with rationale. If Florian approves, update the standard and document why it changed.

**Q: What if there's no standard for an output type?**  
A: Use general standards (CONTENT-VOICE, checklists). If the output type repeats, create a new standard.

**Q: What if I violate a standard accidentally?**  
A: Correction logged, trust score updated. Learn from it. System improves.

---

## Related Documentation

- **[Platform README](../README.md)** — Overall platform overview
- **[Workbench README](../projects/workbench/README.md)** — How standards are enforced
- **[AGENTS.md](../AGENTS.md)** — Agent system rules (includes trigger map for standards)

---

**Maintained by:** Florian Ziesche  
**Last Updated:** 2026-02-19  
**Total Standards:** 11 active, 0 archived
