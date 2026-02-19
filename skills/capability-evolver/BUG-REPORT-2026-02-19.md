# Bug Report: Send Enforcement False Negatives

**Date:** 2026-02-19 03:37 CET  
**Severity:** HIGH (undermines trust in enforcement system)  
**Discovered by:** Capability Evolver during learning scan

## Problem
Morning brief and send-enforcer.sh claimed "0 sends" for 2026-02-18, triggering SEND ENFORCEMENT MODE with €1263 opportunity cost warning.

**Reality (from memory/2026-02-19.md):**
- ✅ Glasswing VC email SENT (rudina@glasswing.vc, message_id 19c736b44c46a5b6, 19:42)
- ✅ FutureSight CV v2 FINALIZED (PDF ready, Workable portal)
- ✅ Primary Application SUBMITTED (Florian manually via portal, 08:15)

**Result:** False enforcement creates noise, wastes cognitive energy, undermines trust.

---

## Root Cause
`scripts/send-enforcer.sh` does NOT check actual delivery logs. It:
1. Counts READY-TO-SEND files (drafts waiting)
2. Reads EXECUTION-TRACKER.md for manual 🔴/🟢 markers
3. Counts zero-send days by grepping "| 0 |" in tracker

**Missing:** No integration with:
- `gog gmail list --sent` (Google sent items)
- `message` tool delivery logs
- `sessions_history` for outbound sends
- Portal submissions (tracked manually, not logged)

**If Florian sends via gog/portal but doesn't update EXECUTION-TRACKER.md → script shows "0 sends".**

---

## Impact
- **Trust erosion:** Agent claims "you haven't sent" when user HAS sent
- **False urgency:** "€1263 lost" when real sends happened
- **Wasted time:** Debugging "why no sends" instead of actual work
- **Enforcement bypass:** If warnings are often false, they get ignored

---

## Fix Options

### Option A: Script Queries Real Logs (BEST)
**Change:** `scripts/send-enforcer.sh` queries actual delivery sources:
```bash
# Check gog sent items (last 24h)
SENT_EMAILS=$(gog gmail list --sent --after=$(date -v-1d +%Y/%m/%d) --format=json | jq '. | length')

# Check message tool sends (last 24h)
# (requires message log query, may not be available)

# Check sessions history for outbound messages
# (requires sessions_history + grep for user sends)
```

**Pros:**
- Accurate, no manual tracking needed
- Works even if Florian forgets to update tracker
- Real-time data

**Cons:**
- Needs gog auth + API access
- message tool may not have queryable log
- Portal submissions still manual (can't be auto-detected)

---

### Option B: Morning Brief Fact-Check (GOOD)
**Change:** Morning brief cron job runs send verification BEFORE reporting:
1. Query gog sent items (last 24h)
2. Check EXECUTION-TRACKER.md
3. If mismatch → report "X sends found (not in tracker), Y in tracker"
4. NEVER claim "0 sends" without verification

**Pros:**
- Prevents false alarms at report time
- Adds transparency ("here's what I found")
- Easy to implement in cron job

**Cons:**
- Still requires gog auth
- Portal sends still manual
- Doesn't fix send-enforcer.sh (used in other contexts)

---

### Option C: Hybrid (RECOMMENDED)
**Implement BOTH:**
1. **send-enforcer.sh:** Add `--verify` flag that queries gog sent (opt-in, requires auth)
2. **Morning brief:** ALWAYS fact-check before reporting zero sends
3. **EXECUTION-TRACKER.md:** Add note "Auto-sync from gog daily (manual portal adds)"

**Pros:**
- Belt + suspenders
- Script works standalone OR with verification
- Morning brief never false-alarms
- Manual tracking remains as backup

**Cons:**
- More implementation work
- Still can't auto-detect portal submissions

---

## Immediate Mitigation (DONE)
✅ **SOUL.md updated:** "CHECK: Telegram delivery log, gog sent items, session history — NICHT schätzen."  
✅ **DAILY_LEARNINGS.md updated:** Bug documented with details.

---

## Next Steps
1. **Florian decides:** Which fix option?
2. **If Option A or C:** Implement gog sent-items query in send-enforcer.sh
3. **If Option B or C:** Add fact-check to morning brief cron (job 216bfa73 or separate)
4. **Test:** Run verification with known send history, confirm accuracy
5. **Deploy:** Update heartbeat/morning brief to use verified data

---

## Related Issues
- SEND ENFORCEMENT MODE activated 3 times (Feb 15, 17, 19) — how many were false?
- Opportunity cost calculation (€421/day) assumes accurate zero-send count
- Agent trust degradation if warnings proven unreliable

---

**Confidence:** 95% — Bug clearly identified, fix options well-defined, immediate mitigation applied.  
**Priority:** HIGH — Undermines core enforcement system, needs fix before next morning brief.
