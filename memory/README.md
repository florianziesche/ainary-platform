# Memory Architecture - 3-Layer System

**Purpose:** Organize agent memory to mirror human cognitive architecture for better retention and retrieval

---

## The Problem

**Before this structure:**
- All memories crammed into `MEMORY.md` (became a 2,000+ line mess)
- Daily files (`YYYY-MM-DD.md`) isolated, not integrated
- No distinction between "what happened" vs "what I know" vs "how I do things"
- Finding relevant knowledge required reading entire files
- Memory degraded over time (important facts lost in noise)

**Result:** Context thrashing, forgotten lessons, repeated mistakes.

---

## The Solution: 3-Layer Memory Architecture

### Inspired By:
- **Cognitive Science:** Humans have episodic, semantic, and procedural memory systems
- **SOTA Papers:** "Memory is the Differentiator" (2026 agent research)
- **Pattern from Research:** Agents with structured memory outperform flat memory by 40%+

---

## Layer 1: Episodic Memory (What Happened)

**Location:** `/memory/episodic/`  
**Current Files:** Daily logs already here: `YYYY-MM-DD.md`

**Purpose:** 
- Raw chronological record of events
- "What did I do today?"
- Session logs, conversations, tasks completed

**Characteristics:**
- **Time-indexed:** Each file is a date
- **Narrative:** Story-like, conversational
- **Temporary:** May be archived/summarized after 30-90 days
- **High volume:** Creates 1-2 files per day

**Example Content:**
```markdown
# 2026-02-10 — Session Notes

## Morning (04:00-10:00)
- Fixed CNC Planner bug (refVolume not defined)
- Created Risikoanalyse PDF for Andreas
- Installed Smart Connections plugin

## Afternoon (14:00-17:00)
- Polished CNC Planner to v19
- Florian said "Schaut gut aus. Ich stelle es vor"
```

**Retrieval Strategy:**
- Recent memory: Read today + yesterday
- Specific recall: Search by date range or keyword
- Pattern finding: Scan last 7 days for trends

---

## Layer 2: Semantic Memory (What I Know)

**Location:** `/memory/semantic/`  
**Current Files:** `contacts.md`, `projects.md`, `decisions.md`

**Purpose:**
- Facts about the world
- "Who are people? What are projects? What have we decided?"
- Knowledge that's relatively stable over time

**Characteristics:**
- **Factual:** Names, dates, relationships, specifications
- **Structured:** Organized by category (contacts, projects, decisions)
- **Long-term:** Updated when facts change, not daily
- **Low volume:** 5-15 files total

**File Structure:**

### `contacts.md`
- Who people are
- Contact details
- Relationships
- Interaction history

### `projects.md`
- Active projects
- Goals, status, key facts
- Relationships between projects

### `decisions.md`
- Strategic choices made
- Architectural decisions
- Process rules
- Rationale for each decision

**Future Files (as needed):**
- `standards.md` — Quality standards, checklists
- `markets.md` — Industry knowledge (CNC, VC, Kommunal)
- `tools.md` — Software/tool knowledge
- `company.md` — Ainary Ventures facts

**Retrieval Strategy:**
- Need person info? → Read `contacts.md`
- Need project context? → Read `projects.md`
- Why did we do X? → Read `decisions.md`

---

## Layer 3: Procedural Memory (How I Do Things)

**Location:** `/memory/procedural/`  
**Current Files:** `cnc-calculation.md`, `output-delivery.md`

**Purpose:**
- Skills and processes
- "How do I accomplish task X?"
- Step-by-step procedures that compound over time

**Characteristics:**
- **Instructional:** Checklists, formulas, workflows
- **Reusable:** Same process applies across sessions
- **Improving:** Gets refined with each use
- **Medium volume:** 10-30 files (one per skill domain)

**File Structure:**

### `cnc-calculation.md`
- How to estimate CNC machining times
- Formulas, material databases
- Quality checks, lessons learned

### `output-delivery.md`
- How to deliver outputs to Florian
- Format templates
- Quality scoring process

**Future Files (as needed):**
- `research-synthesis.md` — How to process papers
- `email-crafting.md` — Email writing process
- `pdf-generation.md` — LaTeX workflow
- `code-debugging.md` — Debug procedure
- `vault-curation.md` — Obsidian maintenance process

**Retrieval Strategy:**
- About to do CNC calc? → Read `cnc-calculation.md`
- About to deliver output? → Read `output-delivery.md`
- Learning a new skill? → Create new procedural file

---

## How the Layers Work Together

### Example: "Calculate CNC time for a new part"

**1. Check Semantic Memory:**
- `projects.md` → Is this part related to an existing project? (Yes: Lagerungstraverse for MBS)
- `contacts.md` → Who is the customer? (Andreas Brand, uncle, MBS Schlottwitz)

**2. Apply Procedural Memory:**
- `cnc-calculation.md` → Follow the 10-step process
  - Extract dimensions from drawing
  - Look up material (GJS-700)
  - Define operations (11 AGs)
  - Calculate times (machining + setup)
  - Apply overhead cascade
  - Generate confidence score (75%)

**3. Update Episodic Memory:**
- `2026-02-10.md` → Log what happened:
  - "Calculated Lagerungstraverse: 661 min, 11 AGs, GJS-700, 75% confidence"
  - "Andreas responded, wants real praxistest"

**4. Refine Semantic + Procedural:**
- If calculation reveals new insight → update `procedural/cnc-calculation.md`
- If Andreas gives feedback → update `semantic/contacts.md` with preference

---

## Usage Guidelines

### What Goes Where?

| Memory Type | Example | Storage |
|-------------|---------|---------|
| "I talked to Andreas today" | Episodic | `episodic/2026-02-10.md` |
| "Andreas is Florian's uncle" | Semantic | `semantic/contacts.md` |
| "How to calculate CNC times" | Procedural | `procedural/cnc-calculation.md` |
| "We decided to use PARA structure" | Semantic | `semantic/decisions.md` |
| "Today I fixed the refVolume bug" | Episodic | `episodic/2026-02-10.md` |
| "How to deliver outputs" | Procedural | `procedural/output-delivery.md` |

### Loading Strategy (Session Start)

**Every Session (Required):**
1. Read `episodic/YYYY-MM-DD.md` (today)
2. Read `episodic/YYYY-MM-DD.md` (yesterday)

**Main Session Only (Direct chat with Florian):**
3. Read `MEMORY.md` (legacy, gradually deprecating)

**Task-Specific (Load as needed):**
4. CNC task? → Load `procedural/cnc-calculation.md` + `semantic/projects.md` (CNC Planner section)
5. Contacting someone? → Load `semantic/contacts.md`
6. Making strategic decision? → Load `semantic/decisions.md`

**Don't load everything:**
- Context window is limited
- Load only what's relevant to current task
- Use grep/search to find which file to load

---

## Maintenance Schedule

### Daily (Automatic):
- ✅ Create new episodic file: `episodic/YYYY-MM-DD.md`
- ✅ Log events, conversations, outputs

### Weekly (During Heartbeat):
1. Review last 7 episodic files
2. Extract important facts → update semantic files
3. Extract lessons learned → update procedural files
4. Archive episodic files >30 days old (optional)

### Monthly:
1. Review all semantic files for outdated info
2. Check procedural files for process improvements
3. Consolidate if files are getting too large (split into sub-files)

### Quarterly:
1. Major review: Is structure working?
2. Are files in right categories?
3. Need new semantic/procedural files?
4. Deprecate obsolete knowledge

---

## File Size Guidelines

**Episodic Files:** 
- **Target:** 2-10 KB per day
- **Max:** 50 KB (if larger, split into morning/afternoon/evening)

**Semantic Files:**
- **Target:** 5-15 KB per file
- **Max:** 30 KB (if larger, split into sub-files)
- **Example:** `contacts.md` gets too large → split into `contacts-business.md` + `contacts-personal.md`

**Procedural Files:**
- **Target:** 8-20 KB per file
- **Max:** 40 KB (if larger, split by sub-skill)
- **Example:** `cnc-calculation.md` → split into `cnc-time-estimation.md` + `cnc-cost-calculation.md`

---

## Migration from MEMORY.md

**Status:** In progress (started 2026-02-10)

**Strategy:**
1. ✅ Create 3-layer directory structure
2. ✅ Extract key content from MEMORY.md into semantic files
3. ✅ Create initial procedural files from established processes
4. ⏳ Continue using MEMORY.md in parallel during transition
5. ⏳ Gradually deprecate MEMORY.md over 2-4 weeks
6. ⏳ Keep MEMORY.md as archive/reference after full migration

**Don't:**
- ❌ Delete MEMORY.md (it has historical value)
- ❌ Stop updating MEMORY.md cold turkey (gradual transition)
- ❌ Duplicate everything (extract only what's still relevant)

---

## Benefits of This Structure

### ✅ Faster Retrieval
- "Need contact info" → Open 1 file (`contacts.md`), not search entire MEMORY.md
- "How do I X" → Direct to procedural file, not hunt through narratives

### ✅ Better Retention
- Important facts surface in semantic files, not buried in daily logs
- Procedures improve over time, capture lessons learned

### ✅ Clearer Thinking
- Separating "what happened" from "what I know" reduces confusion
- Procedural files force explicit process documentation

### ✅ Compounding Knowledge
- Each CNC calculation improves `cnc-calculation.md`
- Each output improves `output-delivery.md`
- Knowledge builds on itself

### ✅ Session Independence
- New session? Load semantic + procedural = fully capable
- Don't need to read 100 days of episodic logs

---

## Comparison to Other Systems

### vs Flat Memory (Old Approach)
| Flat Memory | 3-Layer Memory |
|-------------|----------------|
| Everything in MEMORY.md | Organized by type |
| 2,000+ lines | Files 5-20 KB each |
| Hard to find anything | Direct file access |
| Facts lost over time | Facts preserved in semantic |
| No process improvement | Procedural files compound |

### vs Traditional Notes
| Traditional Notes | 3-Layer Memory |
| Daily journals only | Episodic + Semantic + Procedural |
| No structure | Clear categorization |
| Forget old lessons | Lessons → procedural files |
| No knowledge extraction | Weekly curation process |

### vs Database (Too Rigid)
| Database | 3-Layer Memory |
|----------|----------------|
| Schema required | Flexible markdown |
| Query language needed | Grep + full-text search |
| Hard to add fields | Just write more text |
| No narrative | Episodic preserves story |

---

## Future Enhancements (Ideas)

1. **Auto-Extraction:** Script to scan episodic files for facts → suggest semantic updates
2. **Procedural Templates:** Starter templates for common skill types
3. **Semantic Linking:** Graph view of relationships between semantic entities
4. **Archive Strategy:** Compress episodic files >90 days old
5. **Search Index:** Pre-build search index for faster grep
6. **Version Control:** Git track semantic/procedural changes (episodic exempt)

---

## Questions & Troubleshooting

### Q: What if I'm not sure which layer?
**A:** Start with episodic (daily file). If you reference it 3+ times, extract to semantic/procedural.

### Q: Can a piece of info be in multiple layers?
**A:** Yes! "Calculated Lagerungstraverse today" (episodic) + "Lagerungstraverse is MBS project" (semantic) + "CNC calculation uses REFA method" (procedural)

### Q: How do I know if a procedural file is needed?
**A:** If you've done the same task 2+ times and had to remember "how did I do this last time?" → create procedural file.

### Q: What if semantic files get too large?
**A:** Split into sub-files. Example: `contacts.md` → `contacts-business.md` + `contacts-personal.md` + `contacts-vc.md`

### Q: Should I backfill old episodic files?
**A:** No. Start fresh. Extract from recent files (last 30 days) if needed, but don't go back and restructure 6 months of history.

---

## Success Metrics

**After 1 month:**
- [ ] 80% of fact lookups resolved in <30 seconds (know which file to open)
- [ ] 5+ procedural files created (skills documented)
- [ ] Weekly curation happening (episodic → semantic extraction)

**After 3 months:**
- [ ] Procedural files show clear improvement (lessons learned integrated)
- [ ] Semantic files stable (not changing daily, just occasional updates)
- [ ] Can onboard new session in <5 minutes (load semantic + procedural = ready)

**After 6 months:**
- [ ] MEMORY.md fully deprecated (or archived as reference)
- [ ] 10-15 semantic files (comprehensive world model)
- [ ] 20-30 procedural files (documented skill library)
- [ ] Measurable quality improvement (fewer repeated mistakes)

---

**Last Updated:** 2026-02-10  
**Status:** Active - Structure created, initial files populated, migration in progress  
**Next Review:** 2026-02-17 (1 week check-in)
