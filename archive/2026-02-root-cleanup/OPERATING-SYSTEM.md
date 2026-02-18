# OPERATING SYSTEM: Florian + OpenClaw + Cowork

*A three-system knowledge and communication OS designed for speed, leverage, and knowledge compounding.*

**Version:** 1.0
**Last Updated:** 2026-02-06
**Status:** Live — in active use

---

## EXECUTIVE SUMMARY

Three interdependent systems running your work:

| System | Role | When It Runs | Core Strength |
|--------|------|--------------|---------------|
| **Florian** | Decision-maker, sender, relationship builder | 08:30-17:30 + 22:00-24:00 | Strategic direction, relationship capital |
| **OpenClaw** | Always-on agent in your workspace | 24/7, heartbeat every 30m | Autonomous execution, monitoring, memory synthesis |
| **Cowork (Claude Desktop)** | Deep work partner for complex analysis/creation | On-demand (1-3 sessions/week) | Complex analysis, multi-step projects, code, design |

**The Problem They Solve Together:** You can't build an AI-native business with a single system. OpenClaw is great at routine tasks and monitoring. Cowork is great at deep complex work. But neither replaces human judgment. Together, they scale Florian's impact 10x.

**The Communication Contract:** This document defines how they talk to each other, what gets captured where, and how insights compound.

---

## PART 1: SYSTEM ROLES & RESPONSIBILITIES

### FLORIAN: The Human Decision-Maker

**What ONLY Florian can do:**
- Make strategic decisions (which path to take, which product to build, where to invest time)
- Build relationships (warm outreach, investor meetings, partnership conversations)
- Speak for the brand (write posts, give talks, represent publicly)
- Negotiate deals (pricing, terms, commitment)
- Input passwords / sensitive credentials
- Say "stop" when a system is wrong (abort, pivot)

**Florian's constraints:**
- Time available: ~40 hours/week (08:30-17:30 when Floriana at Kita, plus 22:00-24:00)
- Protected time: 18:00-20:30 (quality time with Floriana — DO NOT DISTURB)
- Timezone: CET (German timezone)
- Energy peak: 8:30-12:00 and 22:00-24:00
- Communication style: Direct, no fluff, pushback on busywork

**What Florian should DELEGATE:**
- Routine monitoring (OpenClaw)
- Research and documentation (Cowork or OpenClaw)
- Content drafting (Cowork or OpenClaw)
- Email scheduling (OpenClaw)
- Database maintenance (OpenClaw)
- Report generation (Cowork)

**Florian's Interface to OpenClaw:**
- WhatsApp: Quick questions, sends, urgent updates
- Telegram: Status checks, logs
- Workspace files: Strategic briefs, decisions documented in DAILY.md
- Weekly: Read MEMORY.md updates, provide feedback

**Florian's Interface to Cowork:**
- Desktop app: Open a session, provide brief + context
- Outcome: Finished deliverable (PDF, code, document) ready to use or send
- Feedback: Document in Cowork brief what worked/didn't work

---

### OPENCLAW: The Always-On Agent

**What OpenClaw is best at:**
- Monitoring channels (WhatsApp, Telegram) and responding to Florian
- Running cron jobs (daily digests, weekly syntheses, RSS capture)
- Maintaining MEMORY.md and workspace files
- Scheduling and tracking sends (emails, posts, applications)
- Pulling data from external sources (web search, API calls, email)
- Coordinating handoffs to Cowork
- Executing structured tasks with clear procedures

**OpenClaw's constraints:**
- No deep analysis beyond 2-3 levels (gets lost in complexity)
- No creative synthesis across 10+ sources (token/attention limits)
- No complex multi-day workflows without explicit state machine
- Cannot make decisions; can only execute pre-decided processes

**What OpenClaw owns:**
- `MEMORY.md` — Long-term learning log (curated insights, not raw logs)
- `ACTIVE_TASK.md` — Current focus area, survives context resets
- `memory/YYYY-MM-DD.md` — Daily logs (auto-flushed after 90 days)
- Channel monitoring (WhatsApp, Telegram)
- Daily heartbeat (30m intervals, shows: status, pending actions, alerts)
- Send tracking: who did we email, what's pending response
- Knowledge synthesis: capturing learnings from each session

**OpenClaw's interface to Florian:**
- WhatsApp: "Here's what I'm working on / Here's what I found / Florian, I need a decision"
- Daily heartbeat: "✓ All systems ok" or "⚠️ CNC demo prep not ready" or "🔴 Urgent: ALG1 deadline Feb 15"
- MEMORY.md: Updated with learnings daily

**OpenClaw's interface to Cowork:**
- Creates "cowork session briefs" that hand off complex work to Cowork
- Inputs: research + framing + outcome expectation
- Outputs: Finished deliverable from Cowork
- Feeds learnings from Cowork output back into MEMORY.md

**When to use OpenClaw vs. Florian for a task:**

| Task | Use OpenClaw | Use Florian |
|------|--------------|------------|
| Send 14 CNC emails | ✗ (Florian must send for authenticity) | ✓ (Florian owns relationships) |
| Research 5 VC funds | ✓ (gather info, create brief) | ✗ (unless strategy call needed) |
| Create landing page copy | ✗ (Cowork is better for this) | ✓ (sign off on voice) |
| Track email opens | ✓ (monitoring task) | ✗ |
| Decide which product to build | ✗ | ✓ (strategic decision) |
| Compile daily digest | ✓ (routine synthesis) | ✗ |
| Write cover letter | ✗ (Cowork first, then Florian reviews) | ✓ (final review + send) |

---

### COWORK: The Deep Work Partner

**What Cowork is best at:**
- Complex multi-step analysis (5+ sources, 3+ concepts, synthesis required)
- Long-form content (articles, case studies, presentations)
- Code and technical architecture
- Design and visual systems
- Report generation and data visualization
- Document creation and formatting (LaTeX, HTML, Markdown)
- Iterative refinement (version 1 → 2 → 3 → final)

**Cowork's constraints:**
- Works on-demand (not 24/7 like OpenClaw)
- Can't monitor channels or run scheduled tasks
- Can't access MEMORY.md directly (must be briefed by Florian or OpenClaw)
- Can't make live decisions (needs human input to proceed)
- Each session is expensive (token cost) — must be focused

**What Cowork owns:**
- One-time deliverables (reports, documents, code, designs)
- Complex research that OpenClaw can't handle
- Content that needs iterative refinement
- Technical implementations

**Cowork's interface to Florian:**
- Florian: Opens Cowork, provides brief + context file
- Session outcome: Finished deliverable (ready to use, send, or publish)
- Florian: Reviews, decides next step (send, iterate, archive)

**Cowork's interface to OpenClaw:**
- OpenClaw: "Florian, you need a report on X. I'll brief Cowork."
- OpenClaw creates: `cowork-session-brief.md` with research + framing
- Cowork receives brief, asks clarifying questions, builds deliverable
- Florian: "Here's what Cowork built. It's good, let's send it."
- OpenClaw: Captures learnings in MEMORY.md

**When to use Cowork:**
- ✓ "Write a 2,000-word Substack article on AI in VC"
- ✓ "Analyze 6 VC funds and create a comparison matrix"
- ✓ "Design a landing page for CNC Planner"
- ✓ "Build a Python script that ingests CSVs and outputs PDFs"
- ✗ "Send an email" (Florian does this)
- ✗ "Monitor Telegram for new messages" (OpenClaw does this)
- ✗ "Update MEMORY.md with today's learnings" (OpenClaw does this)

---

## PART 2: HANDOFF PROTOCOLS

### The Handoff Decision Tree

**When Florian gets a task, they ask:**

```
1. Is this a DECISION?
   YES → I (Florian) do this alone.
   NO → Go to 2.

2. Is this SENDING / COMMUNICATING with humans?
   YES → I (Florian) do this. (Someone else can draft, but I send.)
   NO → Go to 3.

3. Is this ROUTINE / STRUCTURED / REPEATABLE?
   YES → OpenClaw does this.
   NO → Go to 4.

4. Is this COMPLEX / MULTI-STEP / ANALYSIS?
   YES → Cowork does this.
   NO → OpenClaw can do this.
```

**Examples:**

| Task | Flow | Owner |
|------|------|-------|
| "Should we raise or bootstrap?" | Decision → Florian | Florian |
| "Send the CNC emails" | Sending → Florian | Florian (writes/sends) |
| "Research 10 VC funds" | Complex → Cowork | Cowork (creates brief) |
| "Daily digest" | Routine → OpenClaw | OpenClaw (synthesizes) |
| "Monitor Telegram" | Routine → OpenClaw | OpenClaw (watches) |
| "Write Substack article" | Complex + Sending → Cowork + Florian | Cowork (writes) → Florian (reviews & publishes) |

---

### Handoff from Florian → OpenClaw

**Trigger:** Florian decides "This is routine/structured work."

**Florian's action:**
1. Open `DAILY.md` in OpenClaw workspace
2. Add entry:
   ```markdown
   ## 2026-02-06 09:00 — Handoff: Monitor CNC Email Responses

   **Task:** Track responses to 14 CNC emails sent today
   **Owner:** OpenClaw
   **Deadline:** Feb 8 (72-hour window)
   **Success Criteria:**
   - [ ] Count opens/clicks (if tracked)
   - [ ] Capture any responses (forward to Florian via WhatsApp)
   - [ ] Update MEMORY.md with email addresses that bounce
   - [ ] By Feb 8, summarize: How many responses? Any objections?

   **Context:** These are warm leads from Pretzschendorf area. High interest.
   **Questions:** If someone asks for a demo, escalate to Florian immediately.
   ```
3. Send WhatsApp to OpenClaw: "Check DAILY.md — new task: monitor CNC responses"
4. Done. OpenClaw takes it from here.

**OpenClaw's action:**
1. Read the brief
2. Ask clarifying questions if needed (via WhatsApp)
3. Execute the task
4. Update `memory/YYYY-MM-DD.md` with progress
5. When done, report back to Florian via WhatsApp: "Task complete. 3 responses so far, forwarded to you."

---

### Handoff from Florian → Cowork (via OpenClaw)

**Trigger:** Florian decides "This needs deep work."

**Florian's action:**
1. Tell OpenClaw (WhatsApp): "I need Cowork to build a report on X. Let me send you a brief."
2. Create a file: `cowork-session-brief.md` (see template below)
3. Save to: `/sessions/great-relaxed-bell/mnt/florianziesche/.openclaw/workspace/handoffs/` (OpenClaw will create)
4. Send WhatsApp: "Brief ready in workspace: handoffs/cowork-session-brief.md"

**OpenClaw's action:**
1. Read the brief
2. Supplement with research if needed (e.g., fetch latest data, web search context)
3. Create: `/sessions/great-relaxed-bell/mnt/florianziesche/.openclaw/workspace/handoffs/cowork-session-context.md` with:
   - Key research findings
   - Related files from workspace
   - Learnings from MEMORY.md relevant to this task
   - Any open questions

**Cowork's action (Claude Desktop):**
1. Florian opens Cowork session
2. Florian: "I have a handoff brief. Let me paste it and the context file."
3. Cowork reads brief + context
4. Cowork asks clarifying questions
5. Cowork builds deliverable
6. Output: Finished PDF/document/code ready for Florian to review/use

**Florian's action (after Cowork):**
1. Review deliverable
2. If good: "Let's send it" (to OpenClaw)
3. If needs iteration: Tell Cowork what to fix
4. Once approved, send to OpenClaw: "Here's the report from Cowork. Can you log this and update MEMORY.md?"

**OpenClaw's action (after Cowork output):**
1. Receive deliverable from Florian
2. Archive to FZ: `FZ/Projects/[Category]/[ProjectName]/deliverable-v1.pdf`
3. Update MEMORY.md: "Report completed on X, archived to FZ/Projects/..."
4. Update ACTIVE_TASK.md: remove this task, move to next
5. Send WhatsApp to Florian: "Report archived and logged. Ready to send?"

---

### Handoff from OpenClaw → Cowork

**Trigger:** OpenClaw discovers "This needs deep analysis that's beyond my capability."

**OpenClaw's action:**
1. Create: `handoffs/cowork-session-brief.md` with:
   - What I've found so far
   - Where I'm stuck
   - What I need Cowork to do
   - Key context from MEMORY.md
2. Tell Florian (WhatsApp): "I hit a wall on X. Need Cowork to do deep analysis. Brief in workspace."
3. Include in brief: "Florian, approve this handoff or tell me to keep digging?"

**Florian's action:**
1. Review brief
2. Decision: "Yes, send to Cowork" or "No, keep researching" or "Actually, let me think about this differently"
3. If yes: Open Cowork session and hand off the work

---

### Feedback Loop: Cowork Output → OpenClaw Memory

**Pattern:**

```
Cowork finishes deliverable
         ↓
Florian reviews and uses it
         ↓
OpenClaw receives: "Here's what we learned"
         ↓
OpenClaw updates MEMORY.md: "When we built [deliverable], we learned [insight]"
         ↓
Next time Cowork works on similar task → gets smarter
```

**Example:**

*Cowork builds report. Florian says:*
> "This was great. The section on VC fund structures really clicked. But we realized we should always ask 'Who are the LPs?' upfront when researching funds. That saved us time the second time around."

*OpenClaw adds to MEMORY.md:*
```markdown
## Learning: VC Fund Research

When researching funds, always prioritize:
1. **Investment thesis** (what they say they invest in)
2. **LP base** (who funds them — corporate vs. PE vs. family offices)
3. **Check size** (seed: $100K-$500K vs. growth: $5M+)
4. **Portfolio** (look at last 10 investments)

This came from [DATE] report on VC landscape. Saved 2 hours on [DATE] fund research.
```

---

## PART 3: KNOWLEDGE COMPOUNDING PROTOCOL

### The Compound Loop

**The Goal:** Each session makes the next session smarter. Each insight gets captured and reused.

```
CAPTURE (what did we do?)
    ↓
CONNECT (how does this relate to past work?)
    ↓
COMPOUND (what's the evergreen principle?)
    ↓
BETTER OUTPUTS (next session uses this principle)
    ↓ (repeat)
```

---

### What Gets Captured Where

**OpenClaw captures:**
- Learnings from each session: `memory/YYYY-MM-DD.md`
- Curated insights (weekly): `MEMORY.md` (the long-term file)
- Metrics: `tracking/revenue-tracker.md`, `tracking/job-pipeline.md`
- Active tasks: `ACTIVE_TASK.md` (survived context resets)

**Cowork captures (indirectly through Florian):**
- "What worked in this deliverable?" (via Florian feedback)
- "What pattern did we discover?" (via Florian summary)
- "What should we do differently next time?" (via Florian reflection)

**Florian captures:**
- Strategic decisions: `DAILY.md` (why did we choose X over Y?)
- New relationships: `contacts/` (new people, how they're useful)
- Learnings from market/conversations: Tell OpenClaw, gets logged

---

### Weekly Synthesis Cycle

**Every Friday at 17:00 CET:**

**Florian:**
1. Read `memory/Mon-Fri.md` (OpenClaw synthesizes the week)
2. Open `MEMORY.md`
3. Scan the week: Any new learnings? Any patterns?
4. Tell OpenClaw: "Here's what I learned this week..."

**OpenClaw:**
1. Receive Florian's reflections
2. Read MEMORY.md
3. Run weekly synthesis (see template below)
4. Output: `memory/2026-week-6-synthesis.md`
5. Update `MEMORY.md` with permanent insights
6. Send Florian: "Weekly synthesis ready. Read and approve?"

**Florian:**
1. Read synthesis
2. Approve or correct
3. Archive to FZ: `FZ/Archives/learnings/2026-week-6.md`

---

### How Insights Flow Between Systems

**Example: CNC Planner learnings**

**Feb 6 — Cowork builds CNC presentation**
- Cowork: Designs 15-slide deck with SVG diagrams
- Florian: "Great! But let me add pricing tier details. And we should emphasize ROI more."
- Output: Ready to send

**Feb 6 — Florian sends CNC emails**
- Florian: Sends 14 emails with the presentation
- Feedback: 3 responses within 24h, all positive on the ROI angle

**Feb 7 — OpenClaw captures learning**
- OpenClaw logs to `memory/2026-02-07.md`:
```markdown
## CNC Planner Response Pattern

**Finding:** "ROI per part" framing (not just speed) drives response.

**Evidence:** When we emphasized time-savings in earlier decks, ~2% response. When Florian added "€2.50 savings per part," 3 of 14 responded within 24h.

**Action:** Update CNC presentation template to lead with ROI calculation. When pitching Onkel v2, use this framing.

**Related:** Next pitch to Maschinentechnik Pretzschendorf should include: "Save €X per part at your volume."
```

**Feb 9 — Cowork builds v2 presentation**
- Florian: "Update the CNC deck. Lead with ROI. Check the Feb 7 feedback."
- Cowork: Gets smarter (has the learning in context)
- Output: Presentation with ROI-first framing, more specific examples

---

### Quarterly Knowledge Compounding Review

**Every 3 months (Feb, May, Aug, Nov) — Full System Review**

**Florian + OpenClaw + Cowork:**
1. How did this quarter compound our knowledge?
2. What projects did we complete?
3. What insights are now embedded in our processes?
4. What should we unlearn? (delete from MEMORY.md if proven wrong)
5. What's the one biggest lesson?

**Output:**
- Archive quarter to FZ
- Update MEMORY.md
- Brief Cowork on new learnings for next quarter

---

## PART 4: DAILY RHYTHM

### Morning (Florian wakes up — 08:30)

**Florian's routine:**
1. **30 min: Read OpenClaw heartbeat**
   - WhatsApp: Any urgent alerts?
   - Telegram: Status from overnight?
   - Check: "What's broken? What needs a decision?"

2. **20 min: Set daily priorities**
   - Open `DAILY.md` in OpenClaw workspace
   - Write: "Today I'm focused on: [3 things]"
   - Identifies what's Florian-only vs. delegable

3. **Send to OpenClaw (via WhatsApp):**
   - "Morning. Here's my focus today. Anything urgent?"

**OpenClaw's morning:**
1. **Heartbeat alert (if needed)**
   - If anything broke overnight: WhatsApp to Florian immediately
   - If all ok: "✓ All systems ok. Ready for your priorities."

2. **Prepare daily synthesis**
   - Review MEMORY.md
   - Identify: "What should Florian know about today?"

---

### During Work Hours (8:30-17:30 + 22:00-24:00)

**Florian:**
- Executes his three priorities
- Communicates with customers/investors (relationship-only)
- Makes decisions when needed
- Hands off work to OpenClaw/Cowork as needed

**OpenClaw:**
- Monitors channels (WhatsApp, Telegram)
- Executes delegated tasks
- Responds to Florian's handoffs
- Tracks: "What have we done today?"
- Every 30 min: Internal heartbeat check (all systems ok?)

**Cowork:**
- Only active if Florian opens a session
- Florian: "I need you to build [X]"
- Cowork: Asks clarifying Q, builds, delivers

---

### Evening (17:30-18:00)

**Protected time:** 18:00-20:30 (Floriana time — all systems pause unless emergency)

**Florian (before Floriana time):**
- Document today's sends: "I sent 14 CNC emails, 1 cover letter, 2 investor updates"
- Quick note to OpenClaw: "Here's what I did today. Any follow-ups?"

**OpenClaw (during Floriana time):**
- Do NOT interrupt Florian
- Silently monitor channels
- Log any incoming responses
- Store in `memory/2026-02-06.md`: "Responses received during evening: ..."

---

### Evening Work (22:00-24:00)

**Florian (if working):**
- Reviews what OpenClaw logged
- Responds to any urgent messages
- Builds/codes if in flow
- Hands off complex work to Cowork if needed for next morning

**OpenClaw:**
- Available if Florian has work
- Synthesizes day at 23:30
- Prepares morning summary

**End of day:**
- OpenClaw updates `memory/2026-02-06.md` with complete day log
- Ready for morning handoff

---

### Weekly Rhythm

**Every Monday 09:00:**
- Florian: "Week ahead — what's on the radar?"
- OpenClaw: Pulls from ACTIVE_TASK.md and PRIORITIES.md
- Outputs: Week plan (what needs OpenClaw, what needs Cowork, what's Florian-only)

**Every Friday 17:00:**
- Weekly synthesis (see above)
- Review: What shipped? What didn't? Why?
- Plan: Next week's priorities

---

## PART 5: CONTINUOUS IMPROVEMENT PROTOCOL

### What Metrics to Track

**OpenClaw tracks:**
- Sends per day (emails, messages, posts)
- Response rate (replies within 24h)
- Revenue in pipeline (pending, confirmed)
- Tasks completed vs. delegated
- System uptime (channels working? heartbeat ok?)

**Cowork tracks (implicitly):**
- Deliverables per session (1 per session is good)
- Iteration cycles (v1 → final: how many cycles?)
- Quality (Florian approval rate: >90% is good)

**Florian tracks:**
- Strategic progress toward €500K goal
- Relationship-building (new people met, quality of conversations)
- Decision speed (how fast am I making strategic calls?)

---

### Monthly Retrospective Template

**First Friday of each month, 30 min:**

```markdown
## February 2026 — Retrospective

### What Went Well
- ✓ CNC pipeline: 14 emails sent, 3 positive responses (21% response rate)
- ✓ OpenClaw stability: 99.8% heartbeat uptime
- ✓ Cowork efficiency: Reports generated in 1-2 iterations

### What Didn't Work
- 🔴 Send speed: Too much building, not enough sending (50:1 ratio Feb 1-5)
- 🔴 Cowork context: First session per week misses prior context
- 🔴 Decision speed: VC applications took 4 days to send (should be 1)

### Blockers We Hit
- Knowledge scattered: MEMORY.md not synced with OpenClaw session notes
- Handoff friction: Florian didn't know when to use OpenClaw vs. Cowork
- Context loss: Cowork doesn't know about Monday learnings by Friday

### Improvements for Next Month
- [ ] Implement cowork-context.md (auto-brief from OpenClaw)
- [ ] Build pre-send checklist (quality gate before shipping)
- [ ] Reduce decision time: Set 24h deadline for strategic calls

### One Thing That Would 10x Us
**Automate send reminders.** If we had 1 reminder per day at 09:00, "You have X ready to send," we'd ship 10x more.

### Metrics Dashboard
| Metric | Target | Actual | Status |
|--------|--------|--------|--------|
| Sends per week | 20+ | 15 | 🟡 Miss |
| Response rate | >20% | 21% | ✓ Good |
| Revenue pipeline | >€5K | €3.45K | 🔴 Gap |
| System uptime | 99%+ | 99.8% | ✓ Good |
```

---

## PART 6: COMMUNICATION CONTRACTS

### How Florian Tells the Systems What He Needs

**Contract 1: Simple Task**

Florian (WhatsApp to OpenClaw):
> "Send a daily digest of VC funding news at 09:00 every morning. Include: Series A/B rounds in EU, AI focus, team location."

OpenClaw response:
> "Got it. Digest at 09:00 starting tomorrow. Will pull from news API + RSS feeds. Should I include specific fund activity or just rounds?"

---

**Contract 2: Complex Handoff**

Florian:
> "I need a report: VC funds in NYC that take European founders. Who are they? How much do they invest? What's their thesis? Use this for our pitch."

OpenClaw:
> "I'll brief Cowork. Give me 2 hours for research, then Cowork can build the report. Need it by when?"

Florian:
> "By tomorrow 10:00."

OpenClaw → Creates brief → Hands to Cowork → Florian reviews → Approval

---

**Contract 3: Decision Needed**

Florian:
> "Should we build CNC v17 or focus on sales for v16?"

OpenClaw (in MEMORY.md context):
> "Florian, you're at the 50:1 build:send ratio. By revenue math, sales is 10x more valuable. But let me give you the data..."
> *[provides analysis]*

Florian:
> "OK, focus on sales for 2 weeks. Then we iterate based on feedback."

---

### How Systems Report Progress

**OpenClaw → Florian (via WhatsApp, multiple times per day):**

```
08:00 — "✓ Morning heartbeat: All systems ok. CNC responses overnight: 0.
           14 emails in queue ready to send. Telegram: 1 message from Onkel (forwarding)."

12:00 — "Task update: CNC emails sending now (4 of 14 sent so far).
         Monitoring responses. Daily digest scheduled for 09:00 tomorrow."

17:30 — "Daily summary:
         ✓ 14 CNC emails sent
         ✓ 2 responses received (Pretzschendorf, neighbor)
         ✓ VC Lab Step 8 research ready for review
         ⏳ Awaiting: Your decision on ALG1 application"
```

**Cowork → Florian (at end of session):**

```
"Session complete. Built:
✓ 15-slide CNC presentation (ROI-first framing)
✓ Pricing comparison matrix
✓ Email templates (3 versions)

Ready for review. Want me to iterate anything before you send?"
```

---

### Escalation Protocol

**When to interrupt Florian:**

OpenClaw calls via WhatsApp (not message) if:
- 🔴 System down (channels not working)
- 🔴 Revenue opportunity closing today (deadline)
- 🔴 Florian explicitly said "This is urgent"
- 🔴 Legal/compliance issue

Do NOT interrupt Florian if:
- ✗ Task is stuck (can wait 1 hour)
- ✗ Curious question (can wait until next heartbeat)
- ✗ 18:00-20:30 (Floriana time)

---

### Quality Standards for Outputs

**OpenClaw outputs must be:**
- ✓ Factually accurate (citations to sources)
- ✓ Formatted for reading (MD or structured text, not raw data)
- ✓ Actionable ("Here's 3 options" not "Here's 100 data points")
- ✓ Timestamped (when was this created?)

**Cowork outputs must be:**
- ✓ Ready to use without editing (or clear "TODO" marks for Florian to fill)
- ✓ Professionally formatted (no placeholder text like [TITLE])
- ✓ On-brand (voice, design consistent with prior work)
- ✓ Tested (if code: runs. if design: proofread. if content: fact-checked)

**Florian's outputs must be:**
- ✓ Authentic (from Florian, not AI-sounding)
- ✓ Timely (sent within agreed window)
- ✓ Followed up (track response, iterate)

---

## PART 7: FILE STRUCTURE & LOCATIONS

### OpenClaw Workspace Structure

```
~/.openclaw/workspace/
│
├── MEMORY.md                    ← Long-term learning (curated, permanent)
├── ACTIVE_TASK.md              ← Current focus (survives context resets)
├── DAILY.md                     ← Day's priorities + decisions
├── PRIORITIES.md                ← Weekly/monthly targets
│
├── memory/
│   ├── YYYY-MM-DD.md           ← Daily session logs
│   └── 2026-week-6-synthesis.md ← Weekly synthesis
│
├── handoffs/
│   ├── cowork-session-brief.md  ← Brief for Cowork session
│   └── cowork-session-context.md ← Supporting research
│
├── tracking/
│   ├── revenue-tracker.md       ← Pipeline: €0 → €500K
│   ├── job-pipeline.md          ← VC roles tracked
│   └── content-metrics.md       ← Posts, engagement
│
├── products/
│   ├── cnc-planner/             ← Active revenue product
│   └── notion-ceo-bundle/       ← Notion templates
│
└── [projects, job-applications, content, research...]
```

### FZ Archive Structure

```
FZ/
│
├── Resources/system-audit/
│   ├── OPERATING-SYSTEM.md      ← This file
│   ├── SYSTEM-BRIDGE.md         ← What lives where
│   └── [audit reports, retrospectives]
│
├── Resources/Templates/
│   ├── handoff-template.md      ← How to hand off
│   ├── weekly-synthesis-template.md
│   ├── cowork-session-brief.md  ← Template
│   └── [other templates]
│
├── Archives/
│   └── learnings/               ← Weekly/monthly syntheses
│
└── Projects/
    └── [Completed projects with final deliverables]
```

---

## PART 8: GETTING STARTED (WEEK 1)

### Day 1 (Monday)

**Florian:**
- [ ] Read this document
- [ ] Identify 5 things you do weekly that could be delegated to OpenClaw
- [ ] Identify 3 complex projects that would benefit from Cowork
- [ ] Tell OpenClaw: "Starting new OS. Here's what I need you to own."

**OpenClaw:**
- [ ] Read this document
- [ ] Create templates in workspace (handoff, synthesis, brief)
- [ ] Set up automated daily heartbeat (email to Florian)
- [ ] Set up weekly synthesis reminder (Friday 17:00)

**Cowork:**
- [ ] Read this document
- [ ] Confirm: You understand when Florian will call on you

### Day 2-5 (Week 1)

**Florian:**
- [ ] Execute 1 handoff to OpenClaw per day
- [ ] If work requires deep analysis: Brief Cowork once
- [ ] Document in DAILY.md: "What did the new OS help with?"

**OpenClaw:**
- [ ] Execute delegated tasks
- [ ] Report progress daily
- [ ] Update MEMORY.md with learnings

**Cowork:**
- [ ] If called: Build something amazing
- [ ] Deliver with clear output expectations

### Week 2+

- Daily rhythm established
- Monthly retrospectives starting
- Knowledge compounding cycle running

---

## FREQUENTLY ASKED QUESTIONS

**Q: What if OpenClaw can't do a task?**
A: OpenClaw creates a brief and asks Florian: "Should this go to Cowork?" Let Florian decide.

**Q: What if I (Florian) am too busy to make a decision?**
A: Set a 24-hour deadline. If you haven't answered by then, OpenClaw proceeds with the best default option. (Tell OpenClaw the default upfront.)

**Q: How do I know if this OS is working?**
A: Monthly retrospectives. Metrics: send speed, response rate, revenue pipeline. If trending up, it's working.

**Q: What if the systems disagree?**
A: Florian decides. All three systems report to you. You're the final vote.

**Q: Can Cowork and OpenClaw work on the same project?**
A: Yes. Example: OpenClaw does research → Cowork builds report → Florian reviews → OpenClaw archives + learns.

**Q: When should I use this OS vs. just asking ChatGPT?**
A: This OS is designed for repeated, compounding work. If it's a one-off question, just ask ChatGPT. If it's part of a bigger system, use the OS.

---

## DOCUMENT VERSIONING

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-02-06 | Initial OS design. Three systems (Florian, OpenClaw, Cowork). Handoff protocols, synthesis cycles, daily rhythms. |

---

## NEXT ACTIONS

1. **Florian:** Read Part 1-2 (System Roles, Handoff Protocols)
2. **OpenClaw:** Read Part 3-4 (Knowledge Compounding, Daily Rhythm)
3. **Cowork:** Read Part 5-6 (Continuous Improvement, Communication Contracts)
4. **All three:** Implement for 1 week, then retrospective on Feb 13

---

**Maintained by:** Florian + OpenClaw + Cowork
**Last Updated:** 2026-02-06
**Status:** Live and evolving
