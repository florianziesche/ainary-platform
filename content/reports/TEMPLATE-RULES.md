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

### 03. TOC — Option C (Grouped, TIGHTENED)
- "CONTENTS" heading: Black (#1a1a1a), weight 600, uppercase
- Section markers: Grey (#888), 0.65rem, uppercase (FOUNDATION / ANALYSIS / ACTION)
- Plain numbers (1, 2, 3 — NOT 01, 02)
- **TOC entry padding: 8px 0** (NOT 12px — academic-tight spacing)
- **TOC section-label margin-bottom: 8px** (NOT 12px)
- Hover: title turns gold (#c8aa50)
- Page numbers right-aligned (print only)
- Appendix items (Transparency Note, Claim Register, References) listed in TOC

### 04. How to Read — Option B (Standalone Mini-Section, STANDARDIZED)
- Position: between TOC and Executive Summary
- **Structure (exact order, identical across ALL reports):**
  1. Intro paragraph: "Every claim in this report carries a classification badge and confidence level."
  2. **Table 1: Evidence Classification** — 4 rows, columns: Badge / Meaning / Example
     - Use TEXT labels, not colored badge spans: `[E] Evidenced`, `[I] Interpretation`, `[J] Judgment`, `[A] Assumption`
     - Examples must be report-specific
  3. **Table 2: Confidence Levels** — 3 rows, columns: Confidence / Meaning
     - High: "3+ independent sources, peer-reviewed or large-sample primary data"
     - Medium: "1–2 sources, plausible but not independently confirmed"
     - Low: "Single secondary source, methodology unclear, or extrapolated"
  4. **Overall Confidence Score paragraph** (MANDATORY): "Overall Report Confidence (X%): This score reflects..." + 3 factors + "The score is an honest signal, not a mathematical output."
  5. Pipeline mention: "This report was produced using a multi-agent research pipeline. Full methodology and limitations are in the Transparency Note (Section N)."
- RULE: NO inline badge explanation paragraphs (use the table)
- RULE: Table 1 header = "Badge", NOT "Rating"
- RULE: Confidence Score paragraph references the specific framework by name

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

### 12. Transparency Note — Option A (expanded)
- Heading: "Transparency Note" (English, not Beipackzettel)
- Fields: Overall Confidence, Sources (with counts), Strongest Evidence, Weakest Point, What would invalidate, Methodology (full version here), Limitations, Conflict of Interest
- **Limitations** (absorbs Adversarial Self-Review): 5-7 honest bullets about what this report does NOT do well. Factual, no role-play, no theatrical perspectives.
- **Conflict of Interest**: "The publisher of this report researches, builds, and advises on AI agent systems — and has a commercial interest in the conclusions presented here. Evaluate evidence independently; claims marked [J] reflect judgment, not evidence."
- RULE: Not bold. No specific service lists. Covers research + build + advisory in one line.
- **NO System Disclosure section** — redundant with Methodology (Full) and "About This Report" on the last page. Saying it 3 times is too many.
- NO quarterly update commitment

### 13. Claim Register — Option B (Fixed Column Widths)
- `table-layout: fixed` — MANDATORY to prevent auto-width collapse
- Columns and widths: # (5%) / Claim (45%) / Type (8%, centered) / Source (17%) / Confidence (10%) / Used In (15%)
- Header "Classification" → "Type" (shorter = less wasted width)
- 10-20 claims (better 10 good than 20 bad)
- Top 5 claims get "Invalidated If" note below table
- Confidence types: "High (modeled)", "Medium (practitioner)", "Low (single analyst)"
- No gold. No colored backgrounds.
- `page-break-inside: auto` for tables >10 rows (don't force to next page)

### 14. References + Citation — Option A + Citation B
- Numbered [1][2][3] with hanging indent
- Format: [N] Author/Org. (Year). "Title." Source. URL.
- Citation format: `Ainary Research (2026). [Title]. AR-XXX.`
- RULE: Ainary Research = author (not Florian Ziesche). System produced it, Florian directed it. Name is in Author Bio.
- Cite as: last line in References section

### 15. About This Report (replaces Author Bio)
- Heading: "About This Report"
- Text: "This report was produced by Ainary's multi-agent research system — a pipeline of specialized AI agents that research, validate, write, and quality-check independently."
- Link: ainaryventures.com
- RULE: Identical across all reports
- RULE: No personal name. No credentials. No slogans. Ainary = the brand. Who's behind it → website.
- RULE: Technical details (agent count, model, pipeline timing) belong in Transparency Note, not here.

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
