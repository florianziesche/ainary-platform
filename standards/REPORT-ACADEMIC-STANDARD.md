# REPORT-ACADEMIC-STANDARD.md — Ainary Research Report Standard
*Hybrid Academic-Practitioner Format. Locked 2026-02-21.*

---

## Report Structure (mandatory, in this order)

### 1. YAML Frontmatter
```yaml
---
tags: [ainary-report, <topic-tags>]
report: AR-XXX
qa-score: XX/100
date: YYYY-MM-DD
audience: [<roles>]
tier: OPERATIONAL | STRATEGIC | FOUNDATIONAL
expires: YYYY-MM-DD (6 months from date)
research-question: "<Single clear question this report answers>"
---
```

### 2. Title
`# AR-XXX <Title> — <Subtitle>`

### 3. Abstract
- 150-250 words, ONE paragraph, prose (no bullets)
- Structure: Context → Problem → Method → Key Findings → Implications
- Must be independently readable — someone reads only this and gets the picture
- No citations in abstract

### 4. Keywords
- 5-7, comma-separated, below abstract
- Include: domain, method, key concepts

### 5. Confidence Framework
Table with E/I/J/A badge definitions + count per badge in this report + overall confidence % with 1-sentence justification.

### 6. Introduction
- **Problem:** What gap or question motivates this research? (2-3 sentences)
- **Scope:** What does this report cover and NOT cover? (2-3 sentences)
- **Research Question:** Explicit, single-sentence RQ
- **Structure:** "This report proceeds as follows: Section 2 reviews..."
- Max 1 page

### 7. Methodology
- **Search Strategy:** Which databases/engines, how many queries, date range
- **Inclusion Criteria:** What qualifies as a source? (Tier 1/2 only, etc.)
- **Exclusion Criteria:** What was deliberately excluded and why?
- **Saturation:** When did search stop and why? (3× no-new-info rule)
- **Limitations of Method:** What could this approach miss?
- Max 0.5 page

### 8. Related Work
- Grouped by theme/sub-topic (not chronological)
- Each group: 3-5 key works, what they established, where they disagree
- End with: "This report builds on [X] by [doing Y differently]"
- This section POSITIONS our report in the landscape

### 9. Findings
- Numbered sections: "1. [Topic]", "2. [Topic]"
- **Key Insight** as bold first sentence per section (like McKinsey "At a glance")
- All claims labeled [E], [I], [J], or [A]
- All exhibits numbered: "Exhibit 1:", "Table 2:"
- All figures captioned with source
- Inline citations: (Author, Year) — full ref in References

### 10. Discussion
- **Synthesis:** What emerges from the findings taken together?
- **Tensions:** Where do findings contradict each other?
- **Implications:** What does this mean for practitioners?
- Separated from Findings — Findings = what the literature says, Discussion = what WE interpret
- Must include: "What would invalidate this report's conclusions?"

### 11. Actionable Insights
- 5-7 numbered recommendations
- Each: What to do + Why (evidence reference) + Confidence level
- Sorted by ROI (highest first)
- This is our USP — papers stop at "future work", we stop at "do this Monday"

### 12. Sales Angles
- 2-3 angles for consulting outreach
- Quote-ready sentences
- Tagged with target audience

### 13. Content Ideas
- 2-3 derivatives: LinkedIn, Substack, Workshop
- Each with angle and hook

### 14. Limitations & Future Work
- What this report doesn't cover
- What new research would strengthen the conclusions
- Known biases in source selection

### 15. References
- APA 7th format
- DOI where available
- Admiralty rating [A1], [B2], etc. after each reference
- Grouped: Tier 1 (Peer-Reviewed) → Tier 2 (Practitioner/Industry) → Tier 3 (Guides/Other)

### 16. Source Registry (Appendix)
- Full table: Citation | Admiralty | Category | Summary | Used For
- Source Statistics: count by tier, credibility, category, year range
- Linked as separate file: `AR-XXX-source-registry.md`

---

## Quality Gates

### Pre-Research (before searching)
- [ ] Research Question written as single clear sentence
- [ ] Hypothesis stated ("I expect X because Y")
- [ ] MECE decomposition (3-7 sub-components)
- [ ] Time box set
- [ ] Source plan defined

### During Research
- [ ] Admiralty rating assigned to every source live
- [ ] Saturation tracking (tally of new-info vs. no-new-info)
- [ ] Deliberate disconfirmation search performed
- [ ] At least 30 sources consulted, 50 target
- [ ] ≥50% sources are Tier 1 (A-rated)

### Post-Research (before commit)
- [ ] Abstract is independently readable
- [ ] All claims have E/I/J/A badges
- [ ] All exhibits numbered and captioned
- [ ] Discussion separated from Findings
- [ ] "What would invalidate this?" answered
- [ ] Source Registry complete
- [ ] Overall confidence score assigned with justification
- [ ] Methodology section documents search strategy
- [ ] No Tier 3 sources used as evidence (context only)
- [ ] APA 7th citations complete with DOIs

---

## Exhibit Numbering

- Tables: "Table 1:", "Table 2:", etc.
- Figures: "Figure 1:", "Figure 2:", etc.
- Mixed: Use "Exhibit 1:" (McKinsey convention) when mixing types
- Every exhibit has: Number + Title + Source line below

---

## Citation Format

### Inline
`(Cleveland & McGill, 1984)` or `Cleveland and McGill (1984) found that...`

### Reference List (APA 7th)
```
Cleveland, W. S., & McGill, R. (1984). Graphical Perception: Theory,
    Experimentation, and Application to the Development of Graphical Methods.
    Journal of the American Statistical Association, 79(387), 531–554.
    https://doi.org/10.2307/2288400 [A1]
```

### Admiralty Ratings in References
Append `[A1]`, `[B2]`, etc. after each reference.

---

## What This Standard is NOT

- Not a template for blog posts (see CONTENT-VOICE.md)
- Not for customer-facing deliverables (see BRAND.md for those)
- Not peer-reviewed academic publication (we don't claim it is)
- IS: A rigorous internal research standard that produces consultant-grade intelligence with academic-level source discipline

---

## Related Standards
- `RESEARCH-PROTOCOL.md` — Pre-research methodology (MECE, BLUF, Admiralty)
- `BRAND.md` — Visual design rules
- `CONTENT-VOICE.md` — Writing style
- `SUB-AGENT-CONTEXT.md` — E/I/J/A badge system
- `pipeline-pack.md` — Pipeline phases and QA rubric

---

*Locked: 2026-02-21 by MIIA*
*Cite as: Ainary Research (2026). [Title]. AR-XXX.*
