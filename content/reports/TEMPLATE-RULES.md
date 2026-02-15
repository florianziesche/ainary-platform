# TEMPLATE-RULES.md — Ainary Report Standard (LOCKED)
*Locked: 2026-02-15 01:58 CET by Florian. No changes without explicit approval.*

## Reference Files
- **Template:** `REPORT-TEMPLATE-FINAL.html` (the locked standard)
- **Design Tokens:** `template-elements/00-design-tokens.html` (all CSS specs)
- **Chooser:** `TEMPLATE-CHOOSER.html` (decision history)

---

## LOCKED DECISIONS (Florian-approved)

### 01. Cover — Option E (McKinsey + Confidence)
- Gold-Punkt + "Ainary" top-left (0.85rem, weight 500)
- "Confidence: XX%" + "AR-XXX" top-right (#888, 0.75rem)
- Title big (2.2rem, weight 600, letter-spacing -0.02em)
- Subtitle regular weight (1.0rem, #666)
- Date bottom-left (0.75rem, #888)
- "Florian Ziesche · Ainary Ventures" bottom-center (0.75rem, #888)
- Version indicator next to date: "v1.0"
- NO audience tag. Title = audience filter.
- 80% whitespace.

### 02. Quote Page — Option A (Centered, Optional)
- Centered italic quote, maximum whitespace
- Source attribution below
- RULE: Only include if quote is genuinely strong. Weak quote = no quote page.
- RULE: Quote must be external (not from the report itself)

### 03. TOC — Option C (Grouped)
- "CONTENTS" heading: Black (#1a1a1a), weight 600, uppercase
- Section markers: Grey (#888), 0.65rem, uppercase (FOUNDATION / ANALYSIS / ACTION)
- Plain numbers (1, 2, 3 — NOT 01, 02)
- Hover: title turns gold (#c8aa50)
- Page numbers right-aligned (print only)
- Appendix items (Transparency Note, Claim Register, References) listed in TOC

### 04. How to Read — Option B (Standalone Mini-Section)
- Table: Rating / Meaning / Example
- Mentions multi-agent pipeline
- Links to Transparency Note
- Position: between TOC and Executive Summary

### 05. Executive Summary — Option C (Thesis + Bullets + Keywords)
- Explicit thesis sentence first (always)
- Supporting evidence as bullets (bold key phrase + normal rest)
- 5-7 keywords at bottom (comma-separated, italic)

### 06. Methodology — Option B (Structured, Hybrid Position)
- SHORT version as Chapter 2: max 1 paragraph (4 sentences: sources, pipeline, confidence scale, limitations)
- FULL version in Transparency Note (Appendix)
- Always mention multi-agent pipeline
- Explicit source categories with counts
- Limitations paragraph in bold

### 07. Sections/Body — Option A (Security Playbook Callouts)
- Key Insight: first sentence weight 600 (#1a1a1a)
- Body: 0.95rem, weight 400, #333, line-height 1.75
- Bold terms: weight 600, #1a1a1a
- Footnotes: [N] superscript, 0.65rem, #888
- 3 Callout types:
  1. CLAIM: bg #f5f4f0, no border, label #555
  2. WHAT WOULD INVALIDATE THIS?: bg #f5f4f0, left-border 3px #ddd, label #888
  3. SO WHAT?: bg #f5f4f0, left-border 3px #c8aa50, label #c8aa50
- ORDER: Invalidation BEFORE So What. Always.
- Text directly under label, no page break between.
- RULE: Every chapter with a strong claim gets Invalidation + So What. Chapters without strong claims (e.g., pure methodology) can skip.
- RULE: Use CLAIM box for the chapter's central claim. Use bold for supporting claims.

### 08. Exhibits/Tables — Option A (Financial Services)
- "Exhibit X:" bold caption (0.75rem, weight 600, #555)
- Headers: ALL CAPS, dark grey bg #f5f4f0, 0.7rem, weight 600
- Cells: 0.85rem, #333
- Source line below table (0.7rem, #888, italic)
- Text for checkmarks: Yes / No / Partial — NEVER Apple symbols
- Numbering: sequential through whole report (Exhibit 1, 2, 3...)
- RULE: Max 1 table per page to avoid clutter

### 09. KPI Figures — Option C (Black Bold Only)
- All numbers: weight 600, #1a1a1a
- NO gold for numbers
- Gold reserved ONLY for: So What labels, Gold-Punkt, CTAs
- Source + Confidence below each KPI (0.65rem, #888)

### 10. Recommendations — Option A (Categories + Bullets)
- Heading: "Recommendations"
- Own confidence rating per recommendation section
- Bold lead terms in bullets
- Bullets for non-sequential lists
- Numbers for sequential steps
- Short intro paragraph setting scope

### 11. Predictions — Option A (Table + Beta Badge)
- "BETA" badge visible after heading
- Table: Prediction / Timeline / Confidence
- 3-5 predictions (better 3 good than 5 bad)
- Versioning note: "Predictions scored publicly at 12 months."
- RULE: Only include if report has forward-looking claims

### 12. Transparency Note — Option A
- Heading: "Transparency Note" (English, not Beipackzettel)
- Fields: Overall Confidence, Sources (with counts), Strongest Evidence, Weakest Point, What would invalidate, Methodology (full version here), System disclosure
- NO quarterly update commitment
- "This report was created with a multi-agent research system" as full sentence

### 13. Claim Register — Option A (Financial Services Full Table)
- Columns: # / Claim / Value / Source / Confidence / Used In
- 10-20 claims (better 10 good than 20 bad)
- Top 5 claims get "Invalidated If" note below table
- Confidence types: "High (modeled)", "Medium (practitioner)", "Low (single analyst)"
- No gold. No colored backgrounds.

### 14. References + Citation — Option A + Citation B
- Numbered [1][2][3] with hanging indent
- Format: [N] Author/Org. (Year). "Title." Source. URL.
- Citation format: `Ainary Research (2026). [Title]. AR-XXX.`
- RULE: Ainary Research = author (not Florian Ziesche). System produced it, Florian directed it. Name is in Author Bio.
- Cite as: last line in References section

### 15. Author Bio — Option B (Minimal + Mission)
- Initials circle (48px, #e5e3dc background)
- Name bold
- Bio text: "Florian Ziesche is the founder of Ainary Ventures, where AI does 80% of the research and humans do the 20% that matters. Before Ainary, he was CEO of 36ZERO Vision and advised startups and SMEs on AI strategy and due diligence. His conviction: HUMAN × AI = LEVERAGE. This report is the proof."
- Link: ainaryventures.com
- RULE: Bio is identical across all reports (not customized per report)

### 16. Back Cover — Option A (D-143)
- Gold-Punkt + "Ainary" centered
- Services: "AI Strategy · Published Research · Daily Intelligence" (#666)
- CTA: "Contact · Feedback" (#888, no bold, no gold, no button)
- Contact → mailto:florian@ainaryventures.com
- Feedback → mailto:florian@ainaryventures.com?subject=Feedback: AR-XXX
- Website + email below
- © 2026 Ainary Ventures
- page-break-before: always

---

## HARD RULES (apply to every report)

### Typography
- Font: Inter Variable, self-hosted (/fonts/inter-variable.woff2)
- Max weight: 600 (Semibold). NEVER 700 (Bold).
- No Apple symbols, no emoji in headers
- Section headers: only numbers (1, 2, 3), no icons
- Numbers for sequences, bullets for lists (academic standard)

### Content
- No "I reviewed/analyzed/examined" — only facts
- No "Security Theater" — use "Checkbox security"
- Thesis always explicit in Executive Summary
- Invalidation BEFORE So What, always
- "Recommendations" as heading (not "What Actually Works")
- 5-7 keywords per report
- 3-5 predictions max (if applicable)
- 10-20 claims in register

### Color
- Background: #fafaf8
- Gold (#c8aa50) = meaning ONLY: So What border, TOC hover, Gold-Punkt, max 1 hero KPI per report
- No gold for numbers, icons, or structural elements
- Red/Green only for comparison tables (With/Without Trust Infrastructure)

### Layout
- max-width: 900px centered
- Page padding: 48px 40px
- Section gap: 3rem margin-top
- No opacity: 0 defaults (Kintsugi #7)
- No external dependencies (zero CDN)

### Print
- @page A4, margins 2cm
- Header: "Ainary Report | [Title]" (0.7rem, #888)
- Footer: "© 2026 Ainary Ventures" left, page number right
- Cover and back cover: no header/footer
- page-break-inside: avoid on callouts and tables

### Naming
- Report numbers: AR-001, AR-002, etc. (sequential)
- Citation: Ainary Research (not Ziesche, F.)
- "Transparency Note" (not Beipackzettel)
- "Exhibit" (not Figure, not Table)

---

## PROCESS RULES

1. No report without this template
2. Feedback → Template update (never individual report fix)
3. Template changes require Florian's explicit approval
4. Every report produces 1-2 sales angles (documented in Obsidian)
5. Every report gets a post-production reflection (what worked, what didn't)
6. Pipeline Improvement Protocol: 1 variable per report, measure, learn

---

*This document is the law. The template is the implementation. Both are locked.*
