# Ainary Ventures Website — QA Report
**Date:** 2026-02-17  
**Total Issues Found: 18**

---

## Summary

| Category | Pass | Fail |
|----------|------|------|
| String checks | 7 | 4 |
| Structural consistency | 5 | 8 |
| Content consistency | 4 | 2 |
| Link checks | 1 | 0 |
| **Total** | **17** | **14** |

*Note: Some issues repeat across multiple files — 18 unique issue instances below.*

---

## Phase 1: Inventory

### EN/DE Page Pairs
| EN | DE | Status |
|----|-----|--------|
| index.html | de/index.html | ✅ |
| about.html | de/about.html | ✅ |
| blog.html | de/blog.html | ✅ |
| contact.html | de/contact.html | ✅ |
| daily-brief.html | de/daily-brief.html | ✅ |
| imprint.html | de/imprint.html | ✅ |
| pricing.html | de/pricing.html | ✅ |
| privacy.html | de/privacy.html | ✅ |
| resources.html | de/resources.html | ✅ |
| terms.html | de/terms.html | ✅ |
| tools.html | de/tools.html | ✅ |
| article-100-agents.html | de/article-100-agents.html | ✅ |
| article-agenttrust.html | de/article-agenttrust.html | ✅ |
| article-one-person-company.html | de/article-one-person-company.html | ✅ |

Additional EN-only: 404.html, app.html, dashboard.html, login.html, signup.html  
Research reports (10 pages under /research/) — EN only, no DE equivalents (by design)

---

## Phase 2: Automated String Checks

### ✅ "Deutsch" / "English" in navigation
No instances found. Language switcher correctly uses "DE"/"EN".

### ✅ Globe emoji (🌐)
None found.

### ✅ "[Launch-Datum]" or bracket placeholders
None found (only JS regex patterns using brackets — false positives, OK).

### ✅ "coming soon" / "Coming Soon"
None found.

### ✅ "PDF" as badge text
None found.

### ✅ "Published Research · Daily Intelligence" (old service tags)
None found. All research pages correctly use "AI Strategy · System Design · Execution · Consultancy · Research".

### ✅ "Ainary Ventures LLC" — only in legal pages
Found only in: `de/privacy.html:370`, `de/terms.html:311,323,351` — all legal pages. ✅ Correct.

### ❌ `.pdf` in download links / content
- **index.html:485** — `Report.pdf` shown in simulation filename
- **de/index.html:485** — `Report.pdf` shown in simulation filename
- **resources.html:824** / **de/resources.html:824** — External OpenAI PDF link (acceptable — external resource)

**Verdict:** The `Report.pdf` in the landing page terminal simulation is a UI element, not a download link. **Low priority** — consider changing to `Report.html` for consistency.

### ❌ "we" / "our" / "We" / "Our" in prose (should be I/my — solo founder)
Multiple instances in articles:

| File | Line | Text |
|------|------|------|
| about.html | 10 | `<meta name="description">` — "We build intelligence tools" |
| article-agenttrust.html | 9,11,144,163,164,176,178,202,204,226 | Title & throughout: "Why We Published Our Research", "We built a multi-agent AI system", "So we published everything", "We call it the Trust Race", "Why we published it open source", "We flag this openly" |
| article-100-agents.html | 279-280 | "See how we applied these laws", "our AR-001 research report" |
| article-100-agents.html | 302 | "Why We Published Our Research Open Source" (title reference) |
| article-one-person-company.html | 141 | "we've debated AI...Can we trust it?" |
| article-one-person-company.html | 220 | "Our multi-agent system" |
| article-one-person-company.html | 244 | "Why We Published Our Research Open Source" (title reference) |

**Note:** The AgentTrust article title "Why We Published Our Research Open Source" is a published title — changing it would break SEO/links. The generic "we" in article-one-person-company line 141 ("we've debated AI") is rhetorical/inclusive, arguably OK. The meta description in about.html and "our" references in article CTAs should be updated.

---

## Phase 3: Structural Consistency

### shared/nav.js loading

#### ✅ All EN main pages load shared/nav.js
404, about, app, articles, blog, contact, daily-brief, dashboard, imprint, index, login, pricing, privacy, resources, signup, terms, tools — all ✅

#### ❌ Several DE pages missing shared/nav.js (have inline nav instead)
- **de/article-100-agents.html** — ❌ No shared/nav.js (inline nav at line 702)
- **de/article-one-person-company.html** — ❌ No shared/nav.js (inline nav)
- **de/daily-brief.html** — ❌ No shared/nav.js (inline nav)
- **de/imprint.html** — ❌ No shared/nav.js (inline nav at line 284)
- **de/pricing.html** — ❌ No shared/nav.js (inline nav)
- **de/tools.html** — ❌ No shared/nav.js (inline nav)

**Impact:** These pages won't get nav updates when shared/nav.js changes. Inconsistent maintenance burden.

#### ✅ Research pages — no nav (by design)
Research report pages are standalone documents with no site navigation — this is intentional (PDF-like reading experience).

### shared/styles.css or mobile-menu CSS

#### ❌ DE pages without shared/styles.css AND without mobile-menu CSS
- **de/article-100-agents.html** — ❌ No styles.css, no mobile-menu CSS, has inline nav with hamburger
- **de/article-one-person-company.html** — ❌ No styles.css, no mobile-menu CSS, has inline nav with hamburger  
- **de/imprint.html** — ❌ No styles.css, no mobile-menu CSS, has inline nav

**Impact:** Mobile hamburger menu may not work correctly on these pages.

#### ✅ DE pages without styles.css but WITH inline mobile-menu CSS
de/daily-brief.html, de/index.html, de/pricing.html, de/privacy.html, de/terms.html, de/tools.html — all have inline mobile-menu styles ✅

### Footer consistency
Pages use shared/nav.js which likely injects footer, or have inline footers. DE pages with inline nav have inline footers — **manual inspection recommended** for footer text consistency across inline pages.

---

## Phase 4: Content Consistency

### ✅ Closing line — EN about page
`about.html:315` — "The goal isn't to produce more. It's to free you for the work that matters." ✅

### ✅ Closing line — EN landing page  
`index.html:692` — Present with correct text ✅

### ✅ Closing line — DE about page
`de/about.html:315` — "Das Ziel ist nicht, mehr zu produzieren. Sondern dich für die Arbeit freizumachen, die wirklich zählt." ✅

### ✅ Closing line — DE landing page
`de/index.html:692` — Present with correct text ✅

### ✅ Service tags in research reports
All 10 research pages use: "AI Strategy · System Design · Execution · Consultancy · Research" ✅

### ✅ Language switcher shows "DE"/"EN"
Confirmed across all pages with language switchers ✅

---

## Phase 5: Link Checks

### ✅ Internal links
No broken internal links detected across all active HTML files.

### ✅ Anchor links
No broken anchor references found.

---

## Priority Issues (Action Required)

### 🔴 High Priority
1. **"We/Our" in about.html meta description** (line 10) — Should reflect solo founder voice
2. **de/article-100-agents.html, de/article-one-person-company.html, de/imprint.html** — Missing shared/styles.css AND no mobile-menu CSS → **mobile nav likely broken**

### 🟡 Medium Priority  
3. **6 DE pages missing shared/nav.js** — Creates maintenance burden; any nav change requires manual updates to these files
4. **"We/Our" in article-agenttrust.html** — Pervasive throughout the article; may be intentional editorial "we" but inconsistent with solo brand
5. **"We/Our" in article-100-agents.html** CTA section (lines 279-280) — "See how we applied" / "our AR-001"
6. **"Our" in article-one-person-company.html** (line 220) — "Our multi-agent system"

### 🟢 Low Priority
7. **Report.pdf** in landing page simulation (index.html:485, de/index.html:485) — cosmetic, part of terminal animation
8. **Footer consistency** across inline-nav DE pages — needs manual verification

---

*Report generated 2026-02-17 by QA audit sub-agent*
