# Command Center Dashboard — README

**Built:** 2026-02-10  
**Team:** 5 Designers + 3 Advisory Board Members  
**Purpose:** The ONE screen that determines your day

---

## What You Have

### 📄 `command-center-v1.html`
**Your personal command dashboard.** Open it. Use it daily. This is your morning ritual.

**What it does:**
- Shows ONE action to do NOW (no choices)
- Tracks sends vs. builds (the only KPI that matters)
- Makes financial reality visible (can't hide from it)
- Reveals what you're avoiding (adversarial framing)
- Works on desktop AND mobile
- Prints cleanly (Command Center tab)

**How to use:**
1. Open in browser
2. Look at Hero Action (big red box)
3. Do that ONE thing
4. Click "Log Today's Sends" when done
5. Check "Ready to Send" list (40 min to clear it)
6. Don't overthink it

---

### 📋 `DESIGN-SPEC.md`
**Complete design documentation.** Read this if you want to understand WHY it's designed this way.

**What's inside:**
- 5-person design team perspectives
- Advisory board review (Hoffman, Munger, Lavingia)
- Data model + update mechanism
- Visual design system (Ainary CI)
- Anti-patterns avoided
- Success metrics
- Iteration plan (v1.0 → v2.0)

---

## Why This Dashboard Is Different

Most productivity tools track ACTIVITY. This one reveals AVOIDANCE.

**It's designed around your weaknesses:**
- ADHD → ONE thing highlighted, max 5-7 items per section
- Perfectionism → Shows "95% done" to make sending feel safe
- Financial avoidance → Debt/runway always visible
- Building > Sending → Sends are PRIMARY metric (red/green), builds are grey noise
- Loses overview → Everything fits on one screen, no scrolling

**Adversarial framing:**
- "Ready to Send (But You Haven't)" 
- "What Are You Avoiding?"
- "6 Days Since Last Send" in RED
- "Cost of waiting: €300/day"

**The structure IS the intervention.** You can't customize it. You can't hide sections. It shows what you NEED to see, not what you WANT to see.

---

## The 3 Tabs

### 1️⃣ Command Center (Your Default View)
- Hero Action (DO THIS NOW)
- Send Velocity (2 sends this week / target: 15)
- Financial Reality (€70K debt, €3K/mo, ??? runway)
- Ready to Send (3 items, 40 min total)
- Today's Top 3 (no choices, just do)

### 2️⃣ Pipeline
- VC Applications (0 submitted, 4 ready)
- Consulting Leads (1 contacted, 1 demo ready)
- Content Pipeline (1 published, 1 ready)
- Detail view of what's READY but UNSENT

### 3️⃣ Truth
- Debt breakdown (€70K → where it came from)
- Monthly burn rate (income vs. expenses)
- Avoidance log (self-reported honesty)
- Build vs. Send history (last 7 days)

---

## How To Update (For Mia)

### Current (v1.0 — Hardcoded)
Edit the `dashboardDataExample` object in the `<script>` section of `command-center-v1.html`.

### Near Future (v1.1 — JSON)
Create `dashboard-data.json` in workspace. Dashboard reads it on load.

### Future (v2.0 — Automated)
Script pulls from:
- Git commits (builds)
- Email sent folder (sends)
- Notion API (pipeline)

**Philosophy:** Ship now. Iterate based on USAGE.

---

## Success Metrics

### Week 1
- [ ] Dashboard opened daily
- [ ] Sends increase 2/week → 5/week
- [ ] Financial reality tracked

### Week 4
- [ ] Dashboard = morning ritual
- [ ] Sends consistently >10/week
- [ ] Avoidance log self-reported

### Month 3
- [ ] VC application submitted (≥1)
- [ ] CNC demo completed (Andreas)
- [ ] Content published (1/week)
- [ ] Send/build ratio >1:5 (from 1:24)

**Failure signal:** If you stop using it after 2 weeks, the design failed. Tell me why.

---

## Advisory Board Wisdom

### Reid Hoffman (Network)
"Andreas isn't just a customer — he's a channel. 1 happy Andreas = 5 warm manufacturing intros. The dashboard now shows that with a ⭐ and gold border."

### Charlie Munger (Inversion)
"What would make this fail? If Florian can look at it, feel productive, and still not send. So I made the cost visible: €300/day × 6 days = €1,800 lost."

### Sahil Lavingia (Ship-It)
"You built 3 tabs when you need 1.5. Truth tab is where Florian will hide. But fine — just make sure Command Center is 80% of the value."

---

## Design Principles (Your Rules)

1. **ONE thing always highlighted** — Hero action dominates
2. **Adversarial framing wins** — Show what's NOT done
3. **Structure is intervention** — Dashboard decides, you execute
4. **5±2 items max** — Cognitive load budget
5. **Sends > Builds** — Primary metric, large, red/green
6. **Financial reality visible** — Can't hide from debt
7. **Network = currency** — Andreas = ⭐ multiplier
8. **No scrolling for key info** — 1400×900px = everything
9. **Mobile-first** — Phone is primary device
10. **Print-friendly** — Command Center = daily printout

---

## What Makes This Exceptional

This isn't a dashboard. **It's a mirror.**

It shows you what you're avoiding. It makes financial reality visible. It structures your day around ONE action. It assumes you're capable — it just removes the barriers (choice paralysis, perfectionism, anxiety).

**The only metric that matters:** Do you send more?

If yes → we iterate and improve.  
If no → the design failed its purpose.

---

## Next Steps

1. **Open `command-center-v1.html` in browser**
2. **Look at Hero Action** (big red box)
3. **Do that ONE thing TODAY**
4. **Tell Mia:** What worked? What didn't? What's missing?

This is v1.0. It will evolve based on YOUR usage, not theory.

---

**Built by:**  
🎨 UX Designer (ADHD-Specialist)  
🧠 Behavioral Psychologist  
📊 Data Strategist  
📦 Product Manager  
😈 Florian's Inner Critic  

**Reviewed by:**  
🔗 Reid Hoffman (Network Thinker)  
🧮 Charlie Munger (Mental Models)  
🚀 Sahil Lavingia (Ship-It Mindset)

**Research Foundation:**  
31 papers × 10 days behavioral data × 5 perspectives × 3 advisors = This dashboard.

---

*This is the one screen you see every morning.*  
*It determines your day.*  
*Use it.*
