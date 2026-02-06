# BUILD BLOCKER SYSTEM

**Problem**: Building features that never get sent = €2,105 opportunity cost (5 zero-send days)

**Solution**: Automatic enforcement of "Send Before Build" rule

---

## 🚨 THE RULE

**You CANNOT build more than 2 features in a day with ZERO sends.**

### Why This Exists

From MEMORY.md:
- "0 External Sends in 3 Tagen" — gravierendstes Problem
- "Alles prepared, nichts gesendet"
- "~€1.260 Opportunity Cost in 3 Tagen ohne Outreach"

Florian's stated weakness: "Can overthink/overbuild systems before shipping"

Mia's job: **Protect Florian's priorities**

This system does that automatically.

---

## 📊 HOW IT WORKS

### Before Starting Any New Feature/Build:

```bash
./scripts/pre-build-check.sh "Feature Name"
```

**The script checks:**
1. How many sends today? (from `memory/YYYY-MM-DD.md`)
2. How many builds today?
3. Calculate send ratio

**Enforcement:**
- 0 sends + >2 builds = **BLOCKED** ❌
- Send ratio <30% + >3 builds = **WARNING** ⚠️
- Otherwise = **APPROVED** ✅

### After Sending Something:

```bash
./scripts/log-send.sh "Description of what was sent"
```

**Examples:**
```bash
./scripts/log-send.sh "Email: CNC Lead Follow-up (Maschinentechnik)"
./scripts/log-send.sh "Application: HOF Capital Associate Role"
./scripts/log-send.sh "LinkedIn: Connection to Monique Barbanson"
```

---

## 🎯 INTEGRATION INTO WORKFLOW

### For Mia (AI):

**BEFORE starting ANY build task:**

1. Run pre-build check:
   ```bash
   ./scripts/pre-build-check.sh "CNC Quote Section v2"
   ```

2. If BLOCKED:
   - **DO NOT PROCEED**
   - Tell Florian: "Build blocked - need 1 send first"
   - Suggest: "Which ready email/application should we send?"
   - Point to: `products/cnc-planner/leads/READY-TO-SEND-EMAILS.md` or `job-applications/READY-TO-APPLY.md`

3. If approved:
   - Proceed with build
   - At completion, log it:
     ```bash
     echo "- [x] Built: CNC Quote Section v2" >> memory/$(date +%Y-%m-%d).md
     ```

**AFTER Florian confirms a send:**

```bash
./scripts/log-send.sh "Email: CNC Demo Follow-up to Onkel"
```

### For Florian:

**When you want to build something:**

Mia will check first. If blocked, you have 3 options:

1. **Send something** (recommended)
2. **Override** (not recommended):
   ```bash
   PRE_BUILD_OVERRIDE=true ./scripts/pre-build-check.sh "Feature Name"
   ```
3. **Defer the build** to tomorrow

---

## 📈 SUCCESS METRICS

Track weekly in `memory/weekly-retro.md`:

**Week of 2026-02-03 (Baseline):**
- Sends: 0
- Builds: 12+
- Send Ratio: 0%
- Opportunity Cost: €2,105

**Week of 2026-02-10 (Target):**
- Sends: 10+
- Builds: 5-7
- Send Ratio: >100%
- Revenue Generated: €500+

---

## 💡 WHY THIS WORKS

**Psychological Principle**: Loss aversion + immediate feedback

- Building = feels productive, but isn't revenue
- Sending = feels scary, but IS revenue
- Block building → forces confrontation with send avoidance
- Make send logging easy → reduces friction

**From Behavioral Economics:**
- Humans optimize what gets measured
- Immediate consequences > delayed consequences
- Pre-commitment devices work (Odysseus & the Sirens)

---

## 🔧 TECHNICAL DETAILS

### Memory File Format

Expected structure in `memory/YYYY-MM-DD.md`:

```markdown
# Daily Log: 2026-02-06

## External Sends
- [x] [14:30] Send: Email to CNC Lead
- [x] [15:45] Send: Application to HOF Capital

## Built
- [x] Built: CNC Quote Section
- [x] Built: LaTeX Report Template

## Revenue
- €0 (pending)
```

### Send Detection

Counts lines matching: `^- \[x\].*Send:`

### Build Detection

Counts lines matching: `^- \[x\].*Built:`

### Override Mechanism

Set environment variable:
```bash
export PRE_BUILD_OVERRIDE=true
```

Or inline:
```bash
PRE_BUILD_OVERRIDE=true ./scripts/pre-build-check.sh "Feature"
```

---

## 🎓 LESSONS ENCODED

From `MEMORY.md` → `BUILD-BLOCKER.md`:

1. **"Nicht blind arbeiten"** → Automated enforcement
2. **"Definition of Done = Florian kann nutzen"** → Requires send before next build
3. **"Mia schützt Florians Prioritäten nicht"** → System does it automatically
4. **"€421/Tag Opportunity Cost"** → Quantified in blocker messages

---

## 📝 EVOLUTION LOG

**Version 1.0** — 2026-02-06 01:15 CET
- Initial implementation
- Created by capability-evolver (Cycle #0021)
- Addresses: 27% execution rate, €2,105 opportunity cost
- Mutation Type: Harden + Automate

**Next Evolution:**
- [ ] Add revenue tracking integration
- [ ] Slack/Telegram notifications on blocks
- [ ] Weekly send/build ratio dashboard
- [ ] Auto-suggest which ready item to send when blocked

---

*This is a self-enforcing system. It doesn't ask permission. It blocks. That's the point.*
