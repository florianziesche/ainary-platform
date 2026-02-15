# SHARED-LEARNINGS.md — Team Knowledge Base

*Compound intelligence. Every agent reads this. Every session improves it.*

**Rule:** Before spawning any agent, check if relevant learnings exist here. Include them in the agent's context.

---

## 🧑 Florian — Preferences & Standards

### Communication Style
- **Direct, no fluff.** No "Great question!" or "I'd be happy to help!" — just deliver.
- **German for internal, English for professional/external.** Code comments in English.
- **Push back when needed.** He respects challenge, not compliance.
- **Recommendations > Options.** Don't ask "What do you want?" — tell him what he should do.

### Visual & Design Standards
- **McKinsey-level or don't bother.** No emojis in professional decks. No clip-art energy.
- **Whitespace is king.** Slides need air to breathe. Never compress margins to fit more content.
- **Title + Content must complement, never repeat.** "93% weniger Fehler" as title + "93%" as stat = redundant.
- **Black + White + Gold (#c8aa50) ONLY** for all Ainary materials.
- **Beim Rewrite: Design beibehalten.** Don't compress CSS when rewriting code. Original spacing is intentional.
- **REPORT TEMPLATE LOCKED (2026-02-15).** All reports use `REPORT-TEMPLATE-FINAL.html`. Copy + swap content. Never build from scratch.
- **PDF via `./scripts/html-to-pdf.sh`** — $0, 2s, no agent needed.

### Report-Specific Rules (2026-02-15)
- **Citation: `Ainary Research (2026). [Title]. AR-XXX.`** — System = author, not Florian
- **"Checkbox security" not "Security Theater"** — know audience vocabulary
- **"Contact · Feedback" not "Start a project →"** — Sales CTA kills research trust
- **Bio identical across all reports** — never customize per report
- **Chooser Pattern for ALL design decisions** — 3+ options, research-based, per-option comments, Florian picks
- **Research > Meinung** — every design option needs a benchmark (BCG, McKinsey, Economist)
- **Invalidation BEFORE So What** — always, no exceptions
- **Template-First (Kintsugi #8)** — feedback → template, never individual reports

### Document Standards
- **"Would Florian send this UNCHANGED to a client/investor?"** If no → not done.
- **Pyramid Principle:** Conclusion first, supporting points second, details only if asked.
- **No placeholders in deliverables.** `[INSERT HERE]` = unfinished work, not a deliverable.
- **Delivery = OPEN it for him.** `open /path/to/file` — no paths to copy-paste.

### Pricing & Positioning
- **"Was nichts kostet ist nichts wert."** Never position anything as free.
- **Sonderkonditionen mündlich, nie auf Website.** Discounts = verbal negotiation leverage.
- **Features = Kundenwert, nicht Technik-Checkliste.** "Für Einzelfertiger" > "Bis zu 50 Kalkulationen."
- **Weniger ist mehr bei Pricing.** 4 points per tier max. Each must signal demand/value.
- **Remove CTA buttons from pricing cards** if no self-service signup exists.
- **"Demo" > "Pilotphase"** as CTA wording.

### What Gets Rejected (Anti-Patterns)
| ❌ Don't | ✅ Do Instead |
|----------|--------------|
| Emoji in professional decks | Clean icons or no icons |
| Generic outreach templates | Personalized with specific company detail |
| "Options A, B, C — what do you think?" | "I recommend B because X. Here's why." |
| LaTeX for simple docs | HTML + CSS + Chrome Print |
| Paths to copy-paste | `open` command to open directly |
| 15-point feature lists | 4 high-impact points per section |
| Building systems when shipping needed | Ship first, systematize after |
| "Fertig genug für einen Draft" | "Ready for client/investor without changes" |

---

## 📧 Outreach — What Works

### Email Best Practices
- **Subject line:** Specific pain point, not generic. "CNC Kalkulation: 45min → 5min" > "Innovative Software-Lösung"
- **Opening:** Reference something specific about their company. Pull from website/LinkedIn.
- **Length:** 5-7 sentences max for cold outreach. Longer = deleted.
- **CTA:** One clear action. "Kurzes Gespräch nächste Woche?" — not multiple options.
- **Follow-up sequence:** Day 1, Day 3, Day 7. After 3 touches without response, stop.

### What Worked (CNC Outreach, Feb 2026)
- Referencing specific manufacturing capabilities from their website
- Quantified value: "€X Ersparnis pro Auftrag" (concrete numbers)
- 12 real leads with contact details — specificity beats volume
- Personalized angle per lead based on their specialization

### What Didn't Work
- Generic "innovative software" pitches — everyone says this
- Sub-agents for lead research without web search access — they can't find contacts
- Batch emails without personalization — response rate drops below 5%

---

## 🔬 Research — What Works

### Format That Delivers
- **Executive summary first** (3-5 bullet points, no more)
- **Actionable insights** — each finding must answer "so what?"
- **Sources cited** — Florian values credibility, not volume
- **Comparison tables** — visual, scannable, decisive
- **Time-boxed:** 2-3 hours equivalent max. Diminishing returns after that.

### Common Failures
- Research without a decision question → produces encyclopedia, not insight
- Too many sources, too little synthesis → noise, not signal
- Forgetting to check recency → citing 2023 data in 2026 context

### Research Agent Performance (Feb 3)
- Competitor analysis: delivered in <3 min, structured, actionable ✅
- Market map: clear positioning, useful for strategy ✅
- Lesson: Deep research sub-agents work best with very specific scope + clear output format

---

## 💻 Code & Technical — What Works

### Standards
- **Test before delivering.** "Should work" ≠ works.
- **Demo must be ≥ product.** Never ship less than what was shown.
- **HTML > LaTeX** for documents. Zero dependencies, better CSS control.
- **Dashboard: terminal-based > HTML** — browser security restrictions cause friction.
- **PNG direkt liefern** for graphics, not HTML that needs conversion.

### Common Failures
- Edit tool whitespace mismatch → always `Read` before `Edit`
- Presentation: too many elements, not enough whitespace
- Sub-agents can't use web search → do web-dependent research yourself
- Building v4 when v3 was actually better (overengineering)

---

## 📊 Presentations — What Works

### The Scorecard (check before ANY delivery)
1. ☐ Title ≠ Content (no redundancy)
2. ☐ Whitespace adequate (slides breathe)
3. ☐ No emoji/unprofessional elements
4. ☐ Numbers are prominent and specific
5. ☐ CTA is clear on final slide
6. ☐ Brand-consistent (colors, fonts)
7. ☐ Tested on target device

### What Got Rejected
- v1: Had emojis → rejected → professional icons only
- v4: Compressed margins to fit more → rejected → v3 with proper spacing was better
- Sales deck: Symbols/shortcuts → rejected → McKinsey standard or nothing

---

## 🏗️ Content & Writing — What Works

### Blog / LinkedIn
- **Founder-operator perspective.** Not academic, not generic AI takes.
- **Content Pillars:** AI & Work, AI & Founders, AI & Systems, AI & Careers
- **Repurpose:** 1 blog → LinkedIn + Twitter + carousel
- **Strategic timing:** Post before important meetings (conversation starters)
- **Platform formatting:** No markdown tables on Discord/WhatsApp. No headers on WhatsApp.

### Tone
- Direct, insightful, no fluff
- Write like someone who's built things and learned from failures
- Specific examples > abstract advice
- Acceptable to be opinionated and contrarian

---

## 🔄 Process Learnings

### Sub-Agent Delegation
- **Context is everything.** Sub-agents don't see the main session. Give them what they need.
- **Scope tightly.** One agent, one clear deliverable. Not "do everything about X."
- **Cheaper models for research, premium for synthesis.** Don't burn Opus tokens on data gathering.
- **Parallel execution works:** 6 tasks in 15 minutes (Feb 3 session)
- **Check tool access:** Sub-agents may not have web search. Verify before spawning.

### Memory & Context
- **ACTIVE_TASK.md before working.** Context compaction can kill in-progress work.
- **Token budget = currency.** Don't load everything every session.
- **Progressive disclosure:** Index first, details on demand. ~10x token savings.
- **Write it down immediately.** "Mental notes" don't survive restarts.

### Quality Control
- **First version is rarely good enough.** Budget for at least one revision.
- **Always verify against reference.** Compare output to best existing version.
- **Read before Edit.** The edit tool needs EXACT whitespace match.
- **One thing = one file/action.** Avoid overloaded, multi-purpose outputs.

---

## 📅 Update Log

| Date | What Changed | Why |
|------|-------------|-----|
| 2026-02-04 | Initial creation | Operating System v2 build |

---

*This file compounds. Every significant learning gets added here.*
*Before spawning an agent for a task type, check the relevant section.*
*Update whenever Florian corrects something or a new pattern emerges.*
