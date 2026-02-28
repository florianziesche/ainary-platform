# KNOWLEDGE BRAIN — Nightly Consolidation

**Schedule:** 03:30 CET daily  
**Model:** sonnet (cost-efficient)  
**Session:** isolated  
**Purpose:** Maintain knowledge graph freshness, detect conflicts, integrate daily learnings

---

## Task Specification

### 1. FRESHNESS CHECK

**Goal:** Identify stale knowledge, refresh critical facts

**Actions:**
1. Read all files in `~/Library/Mobile Documents/iCloud~md~obsidian/Documents/System_OS/70_Mia/knowledge/`
2. For each file:
   - Check last modified date (via `stat -f "%Sm" -t "%Y-%m-%d" <file>`)
   - If older than 14 days → flag as `[STALE:YYYY-MM-DD]` in first line
3. For CORE files (`verified-truths.md`, `decisions.md`):
   - Extract 3-5 key claims
   - Run `web_search` to verify each claim is still current
   - Update if contradicted
   - Add verification timestamp

**Output:** `knowledge-freshness.log` with stale files + verification results

---

### 2. CONFLICT DETECTION

**Goal:** Find duplicate or contradictory information

**Actions:**
1. Compare `people.md` with `knowledge/contacts.md`:
   - Extract all person names from both
   - Flag duplicates or conflicts (different info about same person)
2. Compare `projects.md` with `ACTIVE.md`:
   - Check for projects listed in one but not the other
   - Flag status mismatches
3. Compare `knowledge/decisions.md` with root `decisions.md`:
   - Flag duplicates or contradictions

**Output:** `conflicts.md` with:
```markdown
## Duplicates
- Person X in people.md AND knowledge/contacts.md

## Contradictions
- Project Y: ACTIVE says "paused", projects.md says "active"

## Recommendations
- Merge people.md + knowledge/contacts.md
- Update ACTIVE.md status for Project Y
```

---

### 3. ORPHAN WATCH

**Goal:** Ensure every file is linked somewhere

**Actions:**
1. List all `.md` files in `70_Mia/` (excluding archived subdirs)
2. For each file, search Vault for any `[[filename]]` references
3. If 0 references → orphan
4. Categorize orphans:
   - Should be linked → suggest where to link
   - Should be archived → suggest moving to `90_Archive/`

**Output:** `orphans.md` with categorized orphan files

---

### 4. DAILY INTEGRATION

**Goal:** Extract learnings from today's work and update knowledge graph

**Actions:**
1. Check if today's daily note exists: `~/.openclaw/workspace/memory/daily/YYYY-MM-DD.md`
   - If exists, read it
   - If not, skip this section
2. Extract:
   - New facts (look for factual claims, statistics, learnings)
   - Decisions made (look for "decided to...", "going with...", etc.)
   - New contacts (names + context)
   - Project updates (progress, blockers, changes)
3. Apply Memory-R1: **Will this matter in 30 days?**
   - If NO → don't store
   - If YES → proceed
4. Update relevant files:
   - New facts → `verified-truths.md` (if verified) or note for verification
   - Decisions → `decisions.md` (with date + reasoning)
   - Contacts → `people.md` or `knowledge/contacts.md`
   - Project updates → `projects.md`
5. Create new connections:
   - Identify 2-3 cross-topic insights
   - Add to `connections.md`

**Output:** Updates to knowledge files + integration summary

---

### 5. BRIEF

**Goal:** Summarize findings for morning brief

**Actions:**
1. Generate summary:
   ```markdown
   ## Knowledge Brain — YYYY-MM-DD 03:30 CET
   
   **Freshness:** X files checked, Y stale, Z refreshed
   **Conflicts:** N found (see conflicts.md)
   **Orphans:** M files unlinked
   **Daily Integration:** 
   - X new facts added to verified-truths.md
   - Y decisions logged
   - Z people updated
   - W connections created
   
   **Action Required:**
   - [If conflicts found] Review conflicts.md
   - [If orphans found] Review orphans.md
   - [If stale critical files] Update knowledge/X.md
   ```

**Output:** Append to `~/.openclaw/workspace/memory/daily/YYYY-MM-DD.md` (tomorrow's date)

---

## Success Criteria

- ✅ All 20 knowledge files checked for freshness
- ✅ Conflicts detected and logged
- ✅ Orphans identified
- ✅ Today's daily note processed (if exists)
- ✅ Brief generated and logged

## Error Handling

- If daily note doesn't exist: Skip section 4, note in brief
- If web_search fails: Log error, continue with other checks
- If file not found: Log warning, continue

## Estimated Runtime

~5-10 minutes (depending on web searches needed)

## Cost Estimate

- Sonnet model: ~$0.10-0.30 per run
- Monthly: ~$3-9

---

*Spec version: 1.0*  
*Created: 2026-02-20*
