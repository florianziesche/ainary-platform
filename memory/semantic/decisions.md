# Decisions - Semantic Memory

**Purpose:** Strategic choices, architectural decisions, and process rules that shape how we work

---

## Strategic Decisions

### Decision 1: PARA Structure for Vault (v3)
**Date:** Early February 2026  
**Decision:** Restructure Obsidian vault from 13 folders to 7 top-level PARA structure  
**Rationale:** Simpler navigation, clearer categories, industry-standard methodology  
**Structure:**
- **Projects/** — Active work with deadlines
- **Areas/** — Ongoing responsibilities
- **Resources/** — Reference materials, knowledge base
- **Archive/** — Completed or paused projects
- **Daily/** — Daily notes (episodic memory)
- **Templates/** — Reusable structures
- **System/** — Meta documentation

**Impact:** All new files follow this structure. Legacy files migrated gradually.

---

### Decision 2: Audience Tagging (Mandatory)
**Date:** February 2026 (Kintsugi #5)  
**Decision:** Every document MUST have an audience tag  
**Tags:** `[KUNDE]` `[LP/VC]` `[PUBLIC]` `[INTERN]`  
**Rationale:** Prevent messaging confusion between Ainary Fund (LP audience) and Ainary Consulting (client audience)  
**Rule:** After every 3 changes to a document, ask: "Same audience? Same message as Florian?"

**Example Mistakes Prevented:**
- Showing consulting prices to potential LPs
- Using VC thesis language in client demos
- Mixing fund positioning with consulting sales materials

---

### Decision 3: LaTeX > HTML for Print PDFs
**Date:** Validated multiple times in January-February 2026  
**Decision:** Always use LaTeX (TinyTeX, XeLaTeX) for professional PDF outputs, never HTML-to-PDF  
**Rationale:** Better typography, precise control, professional appearance, consistent formatting  
**Path:** `$HOME/Library/TinyTeX/bin/universal-darwin`  
**Use Cases:** Reports, risk analyses, work instructions, client deliverables

---

### Decision 4: Linking Rules (Obsidian)
**Date:** February 2026  
**Decision:** Strict linking discipline to prevent vault bloat  
**Document:** `standards/LINKING-RULES.md`  
**Rules:**
- Max 3-5 links per file
- Links inline with context (not in "Related" sections)
- Use links for relationships, tags for categories
- Wikilinks: Filename only `[[File]]`, never `[[Folder/File]]`
- Backlinks automatic in Obsidian — don't duplicate manually

**Rationale:** Over-linking creates noise. Context beats quantity.

---

### Decision 5: Iterative Development > Rebuilding
**Date:** Validated with CNC Planner v16→v17→v18→v19  
**Decision:** Improve existing versions rather than starting from scratch  
**Pattern:** Build v1 fast → test → v2 with feedback → polish → v3 presentation-ready  
**Example:** CNC Planner went through 19 versions iteratively, each fixing real issues  
**Anti-Pattern:** Scrapping working code to "rebuild clean" (wastes time, loses tribal knowledge)

---

### Decision 6: Files > Mental Notes (Always)
**Date:** Recurring lesson, formalized February 2026  
**Decision:** "I'll remember this" = wrong. Write it to a file immediately.  
**Rationale:** AI memory doesn't persist across sessions. Files are the ONLY memory.  
**Action:** When someone says "remember this" → update `memory/YYYY-MM-DD.md` or relevant file immediately  
**Applies to:** Lessons learned, preferences, facts, decisions, todos

---

### Decision 7: Targeted Edits > Full Rewrites
**Date:** February 2026 (Kintsugi #6)  
**Decision:** NEVER overwrite entire files when editing. Change only the specific section that needs updating.  
**Rationale:** Full rewrites lose headers, frontmatter, tags, related sections, sources, changelogs  
**Method:** Use Edit tool with exact old text → new text replacement  
**Exceptions:** Generating brand new files from scratch

---

### Decision 8: Read Original Documents for Thesis/Positioning
**Date:** February 2026 (Kintsugi #5)  
**Decision:** ALWAYS read Florian's original documents (Decile Hub Sprints, LinkedIn) before creating thesis/positioning content  
**Rationale:** Florian's own words are better than AI-generated summaries. Avoid drift and misrepresentation.  
**Apply to:** VC thesis, fund positioning, personal brand, CV content  
**Don't:** Reconstruct from memory or generic AI knowledge

---

## Process Decisions

### Process 1: Pre-Flight Checklist (Mandatory)
**Date:** Established in AGENTS.md, reinforced February 2026  
**Decision:** Before EVERY non-trivial task, run the 7-step pre-flight checklist  
**Checklist:**
1. Run `./scripts/pre-flight.sh [task-type]` to load relevant knowledge
2. Read `TWIN.md` — Can I decide autonomously? (>90% confidence → act, <90% → ask)
3. Read `standards/FLORIAN.md` — What does Florian expect?
4. `grep -i "[keyword]" INDEX.md` — Does something already exist?
5. Load task-specific knowledge from Vault
6. For complex tasks → spawn Sub-Agent WITH relevant knowledge files
7. Read `standards/checklists/before-any-output.md` before delivering

**Impact:** Quality consistency across sessions, fewer mistakes, less rework

---

### Process 2: Output Tracker (After Every Delivery)
**Date:** February 2026  
**Decision:** After every major output, update `failures/output-tracker.md` with A/B/C/? score  
**Scoring:**
- **A** = Used as-is
- **B** = Needed minor edits
- **C** = Rejected/redone
- **?** = Unknown (no feedback yet)

**Goal:** Track quality trends, identify what works, improve over time  
**Baseline:** 90.9% success rate, 54.5% used-as-is rate (established 2026-02-10)

---

### Process 3: Options > Solutions (Let Florian Decide)
**Date:** Recurring pattern, formalized February 2026  
**Decision:** Present 2-3 options with pros/cons, don't pick for Florian  
**Exception:** >90% confidence + TWIN.md authorization → act autonomously  
**Rationale:** Florian wants agency, not a yes-man. He decides strategy, I execute.  
**Format:** "Here are 3 approaches: [A] pros/cons, [B] pros/cons, [C] pros/cons. My recommendation: [X] because [reason]. What do you think?"

---

### Process 4: A/B/C Output Variants (For Important Deliverables)
**Date:** February 2026 (Kintsugi feedback loop)  
**Decision:** For high-stakes outputs (emails, proposals, headlines), generate 2-3 variants  
**Rationale:** Gives Florian choice, demonstrates range, captures his preference patterns  
**Log:** Track which variants get chosen in output-tracker.md  
**Over time:** Learn Florian's preferences, reduce need for variants

---

### Process 5: Executive Summary First (Long Reports)
**Date:** February 2026 (learned from Mittelstand 59-page report with no feedback)  
**Decision:** For reports >10 pages, ask "Want executive summary or full report?" before generating  
**Rationale:** Unsolicited 50-page reports may not get read. Respect attention.  
**Alternative:** Generate exec summary, then offer "Want the full deep dive?"

---

## Technical Decisions

### Technical 1: Sub-Agent Limits
**Decision:** Max 5 sub-agents running in parallel  
**Model:** Claude Sonnet (not Opus) for cost efficiency  
**Use Case:** Parallel research, batch processing, isolated complex tasks  
**Token Budget:** Monitor to avoid billing errors (200K+ tokens = expensive)

---

### Technical 2: Smart Connections (Obsidian RAG)
**Date:** February 2026  
**Decision:** Use Smart Connections plugin for Obsidian semantic search  
**Model:** Multilingual E5 Small (free, local, handles DE/EN mix)  
**Settings:**
- Result Limit: 20
- Lookup: 50
- Heading-level blocks: ON
- Exclude: Templates, System folders

**Alternative Rejected:** PaperQA2 (requires OpenAI Tier 2, 500 RPM limit too low)

---

### Technical 3: HTML Dashboards with Tabs + Ainary CI
**Decision:** HTML dashboards with tabbed interfaces work consistently well  
**Pattern:** Single-file HTML, embedded CSS/JS, Ainary color scheme (gold #DAA520)  
**Use Cases:** CNC Planner, project dashboards, client demos  
**Rationale:** Portable, no dependencies, works in any browser, easy to share

---

## Anti-Decisions (Never Do This)

### Anti-Decision 1: Building Before Sending
**Lesson:** 6 days of building, 0 sends = €2,105 opportunity cost  
**Rule:** Cannot build >2 features in a day with ZERO sends  
**Enforcement:** `./scripts/pre-build-check.sh` blocks building until 1 send logged  
**Rationale:** Building ≠ Revenue. Sending = Revenue. Protect priorities.

---

### Anti-Decision 2: Prices in Client Deliverables
**Lesson:** Showing internal costs/pricing in demos confuses customers  
**Rule:** External-facing demos hide pricing by default, "Contact for Quote" button instead  
**Exception:** Florian explicitly requests price transparency for negotiation

---

### Anti-Decision 3: Outputs Without Path/Link
**Lesson:** "I created a file" without telling Florian WHERE = useless  
**Rule:** Every output delivery includes full file path or URL  
**Format:** "Created: `/full/path/to/file.md`" or "Live at: https://..."

---

### Anti-Decision 4: Numbers Without Sources
**Lesson:** Unsourced facts in persistent files = hallucinations in 6 months  
**Rule:** See `standards/SOURCE-REQUIREMENT.md` — No numbers in memory/ or products/ without citation  
**Format:** "Value [Source: URL/document/date]"  
**Exception:** Estimates clearly marked with "~" or "estimated"

---

## Research & Experimentation Framework Decisions

### Decision 9: Multi-Lens Research Pattern
**Date:** 2026-02-10  
**Decision:** When analyzing complex topics or large datasets, spawn multiple agents with different perspectives ("lenses")  
**Rationale:** Convergence = high-confidence findings, Divergence = unique insights worth exploring  
**Pattern Validated:**
- 5 agents on Vault (205 files) → 5/5 convergence on "build statt send" problem, divergence found unique opportunities
- 6 agents on 31 SOTA papers → 3 universal laws discovered, novel findings identified
- 10 agents on CNC calculation → 3.4x variance by persona, adversarial = best calibration

**Implementation:**
- Use different personas (VC Partner, McKinsey Consultant, Academic, Adversarial, etc.)
- Look for patterns in convergence (high confidence)
- Mine divergence for novel insights (things only 1 agent finds)
- Document experiments in `experiments/` directory

---

### Decision 10: Agent Persona Matters for Calibration
**Date:** 2026-02-10  
**Decision:** Loss-averse personas (Controller, Adversarial) produce better time estimates than domain experts  
**Evidence:** Agent calibration experiment on CNC Lagerungstraverse
- Controller (+3.5% error) and Adversarial (+5.6%) beat Meister (-33%), REFA (-35%), Physiker (-69%)
- Adversarial self-correction: Phase 1 (47min) → Phase 2 (698min) = 15x improvement
- Average of all 10 agents: -29.5% (systematic optimism bias)
- Persona variance: 3.4x (204 min to 698 min)

**Implication:** For estimation tasks, use skeptical/conservative personas, not domain-expert personas

---

### Decision 11: Three Universal Laws (from 31 Papers)
**Date:** 2026-02-10  
**Decision:** Strategic architecture decisions based on research synthesis  
**The Laws:**
1. **Kapazitätslimit ~80-90** — Skills, Memory, Agents all hit same threshold. Solution: Hierarchical organization.
2. **Selbstkritik > Selbstvertrauen** — Adversarial prompting = biggest lever (our 15x vs papers' max 2x)
3. **Organisation > Kapazität** — Bottleneck = Representation (how knowledge is structured), not Reasoning

**Source:** MEGA-SYNTHESIS of 31 SOTA papers (2026-02-10)  
**Application:** Memory restructure (episodic/semantic/procedural), skill audit, adversarial as mandatory step

---

## Decision Review Schedule

- **Weekly:** Review active decisions for conflicts or needed updates
- **Monthly:** Audit if anti-decisions are being followed (check Kintsugi log)
- **Quarterly:** Strategic decisions review — still aligned with goals?

---

**Last Updated:** 2026-02-10  
**Source:** Extracted from MEMORY.md + Kintsugi lessons + daily session logs + research experiments
