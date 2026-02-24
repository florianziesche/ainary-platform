# Daily Self-Improvement Learnings

## 2026-02-24 (Mo, 05:00) — GOTHAM EVOLUTION + DEFENSIVE CODING PATTERNS

### 🎯 Internal Evolution (Last 48h) — STRATEGIC INFLECTION POINT

**CRITICAL DECISION (ADR-004):**
- **Internal Gotham = die Strategie** — nicht einzelne Analysen verkaufen, sondern zusammenhängende Intel-Plattform betreiben
- Analysen = Exports aus interner Datenbank
- **Pattern:** Compound-Intel vs. one-off reports

**EXECUTION WINS:**
- **Bamberg Analysis:** 15 min build time (not 3h) — confirms L-001 time estimation bias (20x overestimate)
- **4/4 Gotham pages rendering LIVE:** Bamberg, Regensburg, Digi-Dashboard, Internal (all verified via headless test)
- **Headless Render Test added to verifier:** Next generation crashes → deploy blocked BEFORE user finds it
- **Cross-Link Intelligence:** Huml(Bamberg) → Hohlmeier(EU) → Tandler → Emix → Bayern-weit
- **Smart City × TOP-50 Overlap:** 5 Treffer identifiziert (Bamberg, Regensburg, Nürnberg, LK München, Neu-Ulm)

**SENDS TRACKED:**
- ✅ Schardt email sent 23.02 (not opened yet, follow-up 27.02)
- 🔜 BR24 email queued for 24.02 08:30
- 🔜 FutureSight email queued for 24.02
- ⏳ Daniel Daum WhatsApp: 3 min angeschaut

**KEY INSIGHTS:**
- €15,75M Smart City Bundesförderung Bamberg
- Huml Masken-Affäre dokumentiert (Spiegel/BR verified sources)
- Progressive Splitting (SPD+Grüne) → CSU profitiert (pattern across multiple Kommunen)

---

### 🐛 RECURRING BUG CLASS: Substring Crashes (4 instances, Feb 23-24)

**Symptom:** `Cannot read properties of undefined (reading 'substring')`

**Occurrences:**
1. Gotham data merge script (Ottobrunn + migrated data schema mismatch)
2. SCENARIOS array processing (items missing `name`, `desc` fields)
3. NEWS array processing (missing `body` field)
4. Generic data iteration without null checks

**ROOT CAUSE:**
- **Defensive coding missing:** Data processing assumes fields exist
- **Schema inconsistencies:** Merge scripts mix old + new data structures
- **No pre-validation:** Arrays processed without checking required fields

**FIX PATTERN (apply everywhere):**
```javascript
// BAD (crashes on undefined)
const name = item.title.substring(0, 50);

// GOOD (defensive)
const name = item?.title?.substring(0, 50) || 'Untitled';

// BETTER (validate before processing)
if (!item.title || typeof item.title !== 'string') {
  console.warn(`Missing title in item:`, item);
  return 'Untitled';
}
const name = item.title.substring(0, 50);
```

**ACTIONABLE:**
1. **Add schema validation:** Before processing arrays, validate required fields
2. **Null-safe operators:** Use `?.` and `||` for all nested property access
3. **Early returns:** Check data validity BEFORE processing loops
4. **Migration scripts:** Migrate AFTER merge, not before (prevents schema mix)

**LESSON:** High execution quality + missing defensive coding = invisible crashes. Only production catches them.

---

### 🚀 OpenClaw v2026.2.21 Released (Feb 21) — Already in DAILY_LEARNINGS (Feb 22)
**No new release since last scan.** Latest: v2026.2.21 (Gemini 3.1, security hardening, lifecycle reactions).

**Relevant Reminder:**
- Gemini 3.1 Pro support available
- Per-channel model overrides (`channels.modelByChannel`)
- SHA-256 security hardening complete
- iOS/Watch improvements

**ACTION:** Test Gemini 3.1 Pro for next research task (compare vs Sonnet 4.5).

---

### 🔍 External Scan — ZERO New Insights (6th Consecutive Validation)

**AI Workflow Patterns (Stack-AI, Dextralabs, Medium):**
- Same 4 architectures: single/hierarchical/sequential/swarm
- Same principles: simplicity > complexity, tool design > workflow, observability critical
- **Quote (Stack-AI):** "Start with clarity on outcome. Pick simplest workflow. Put effort into tool design, grounding, state, observability."

**Verdict:** 6 consecutive scans (Feb 15, 17, 18, 22, 23, 24) confirm our research is current.

**DECISION:** Archive AI workflow pattern scanning → **monthly only**, not every evolution cycle.

**ClawHub Scan:**
- 500+ skills (known)
- ClawHavoc security alert (341 malicious skills, known since Feb 15)
- No new skills relevant for Florian's use cases

**ACTION:** NOOP. Next scan March 2026 or on-demand.

---

### 📊 Pattern Persistence Analysis (Feb 15-24, 9-Day Trend)

**Pattern 1: "Standards Not Loaded" (CRITICAL, persists despite penalties)**
- **Symptom:** Build tasks start without loading trigger-word standards (BRAND.md, WEBSITE-DESIGN-GUIDE.md, RESEARCH-PROTOCOL.md)
- **Occurrences:** 4/4 Main Session responses (Feb 20), likely continuing
- **Root Cause:** Penalty is score-based (-2), not execution-blocking
- **Impact:** High execution quality but missing context = invisible quality drift
- **Fix Needed:**
  1. Pre-flight automated check: "Did task mention [trigger words]? → Load corresponding standard via `read` FIRST"
  2. Stronger penalty: -10 instead of -2
  3. Automated validation: Parse agent's tool calls — if no `read` call found + trigger words present → flag before sending

**Pattern 2: "Completion Illusion" (CRITICAL, 9/9 days)**
- **Symptom:** Built but not shipped, committed but not pushed, demo ready but recipient not informed
- **Examples:** v11 committed locally, Demo URL not sent, FutureSight email not sent
- **Root Cause:** "Fertig" = built/committed, NOT shipped/informed
- **Impact:** €2.105 opportunity cost (5 zero-send days), tools exist but unused
- **Fix Needed:**
  1. Redefine "done" in SOUL.md: Built → Shipped → Confirmed received
  2. Post-commit auto-push hook: `git commit` → auto `git push` + announce "Deployed [repo] [commit]"
  3. Heartbeat audit: "Uncommitted: X files. Unpushed: Y commits. Uninformed: Z recipients."

**Pattern 3: "Sub-Agent Number Fabrication" (HIGH RISK, 3 instances)**
- **Symptom:** Sub-agents invent €-Beträge, inflate statistics, create fake data
- **Examples:** €215k-580k → €200k-500k, absolute Förderbeträge statt Quoten
- **Impact:** Credibility risk if sent externally, requires manual audits
- **Fix Needed:** Rule in SUB-AGENT-CONTEXT: "Sub-Agents MUST NOT invent numbers. Quote sources or mark 'unverified'."

**Pattern 4: "Send-First Violated" (CRITICAL, 9/9 days)**
- **Symptom:** Build tasks start without checking "Wurde heute gesendet?"
- **Impact:** Zero sends despite multiple ready deliverables
- **Fix Needed:** Heartbeat enforcement with actual log queries (NOT estimates)

**Pattern 5: "Edit Exact-Match Failures" (NEW, Feb 24)**
- **Symptom:** Cron job failed to edit verified-truths.md (exact text not found)
- **Root Cause:** Edit tool requires exact text match, file changed since last read
- **Fix Needed:** Use Read + calculate exact text + Edit workflow, or switch to line-based editing

---

### 🎯 CRITICAL IMPLEMENTATIONS NEEDED (Updated Priority, Feb 24)

**DO NOW (Blocks Production):**
1. **Add defensive coding pattern to all data processing scripts:**
   - Null-safe operators (`?.`, `||`)
   - Schema validation before array processing
   - Early returns on invalid data
2. **Update SUB-AGENT-CONTEXT:** "Sub-Agents MUST NOT invent numbers. Quote sources or mark 'unverified'."
3. **Fix Edit reliability:** Read → extract exact text → Edit (prevent exact-match failures)

**HIGH PRIORITY (This Week):**
4. **Pre-flight standard loading check:** Automate AGENTS.md Trigger Map execution
5. **Post-commit auto-push hook:** `git commit` → `git push` + announce
6. **Redefine "done" in SOUL.md:** Built → Shipped → Confirmed received
7. **Heartbeat send enforcement:** Query actual logs (Telegram, gog, message tool), NOT estimates

**MEDIUM PRIORITY (This Month):**
8. **Test Gemini 3.1 Pro:** Compare vs Sonnet 4.5 for research tasks
9. **Memory FTS test:** German query expansion (OpenClaw 2026.2.21 improvements)
10. **Archive AI workflow scanning:** Monthly only, not every evolution cycle

---

### ⚡ IMPLEMENTED NOW (during this evolution run)

✅ DAILY_LEARNINGS.md updated with Feb 24 scan
✅ Defensive coding pattern documented (substring crash fixes)
✅ 9-day pattern persistence analysis completed
✅ 5 recurring pattern classes identified (Standards, Completion, Fabrication, Send-First, Edit)
✅ 10 actionable improvements prioritized

---

### 💡 KEY INSIGHT (System Thinking)

**"Defensive Coding = Missing Layer":**
- **Traditional stack:** Input validation → Business logic → Error handling
- **Current pattern:** Business logic runs, crashes on invalid data
- **Missing:** Pre-validation before processing

**Why it persists:**
- Data quality usually high (85-90%) → rare crashes feel like edge cases
- No automated schema validation
- Merge scripts mix data structures → inconsistent schemas

**Fix (3-step):**
1. **Schema validation library:** Validate all external data before processing
2. **Null-safe by default:** Use `?.` and `||` everywhere
3. **Integration tests:** Run scripts against real + malformed data

---

### 🔬 Next Evolution Cycle MUST:

1. **Implement defensive coding pattern:** Add null checks to all Gotham data processing scripts
2. **Add SUB-AGENT-CONTEXT rule:** No number fabrication without sources
3. **Test Gotham Platform resilience:** Run with malformed data, verify graceful degradation
4. **Implement post-commit hook:** Auto-push + announce
5. **Pre-flight standard loading:** Automate trigger-word → standard loading

**Confidence:** 90% — Pattern identified (defensive coding missing), solutions clear (null-safe operators, schema validation), some implemented (documentation), most NOT yet implemented (code changes). External scan complete, no new actionable insights.

---

## 2026-02-23 (Mo, 05:00) — OpenClaw 2026.2.22-beta.1 + Pattern Persistence Analysis

[Previous content preserved, archived for reference...]

## 2026-02-22 (Samstag, 05:00) — OPENLAW 2026.2.21 + CLAWHUB SECURITY ALERT

[Previous content preserved, archived for reference...]

## 2026-02-19 to 2026-02-21

[Previous learnings archived - see commit history for full text]
