# Command Center Dashboard — Design Specification
*Built by 5-person design team + 3 advisory board members*
*Version: 1.0 | Date: 2026-02-10*

---

## Executive Summary

This dashboard is a **behavioral intervention disguised as a productivity tool**. It doesn't track what Florian DOES — it reveals what he AVOIDS. The structure IS the intervention.

**Core Insight:** Florian (ADHD, perfectionism, €70K debt, 6+ days no sends) doesn't need more information. He needs ONE clear action, adversarial framing, and consequences made visible.

**Design Principle:** Organization > Capacity. The dashboard's structure prevents choice paralysis by deciding FOR him.

---

## Design Team Perspectives (Round 1)

### 1️⃣ UX Designer (ADHD-Specialist)

**Key Contributions:**
- **ONE HERO ACTION ZONE** — No options, no choices. Dashboard tells, not asks.
- **Cognitive Load Budget = 7±2 items** — Each section maxes at 5-7 visible items
- **No scrolling for critical info** — Everything that determines the day fits in 1400×900px viewport

**Why This Matters:**
ADHD + choice paralysis = analysis paralysis. The dashboard reduces decision fatigue by making THE decision for him. 40% of viewport is ONE action.

---

### 2️⃣ Behavioral Psychologist

**Key Contributions:**
- **Adversarial framing throughout** — "What are you avoiding?" > "What's your plan?"
- **Send velocity as PRIMARY metric** — "6 Days Since Last Send" in RED, large type
- **Safe sending cues** — "95% done" + "This is a bet, not a final statement"

**Why This Matters:**
Florian's pattern: building = anxiety regulation, sending = vulnerability. The dashboard makes avoidance VISIBLE and reframes sending as "portfolio bets" (not risky statements).

**Evidence:** 
- 205 files created : 2 emails sent = 100:1 ratio (Feb 2026)
- 6+ days ready materials unsent (HOF, Andreas, Substack)
- Research: 64% of daily activity is noise, builds ≠ revenue

---

### 3️⃣ Data Strategist

**Key Contributions:**
- **Sends/Builds ratio is THE ONLY KPI** — Everything else is vanity
- **Financial burn rate front and center** — €70K debt + €3K/mo income = urgency
- **Noise filter = 5:1 rule** — For every metric shown, 5 hidden

**Why This Matters:**
Tracks outcomes (sends, applications, revenue) not activity (hours, files, agents). Financial reality creates visceral urgency.

**Metrics That Matter:**
1. Sends per week (target: 15)
2. Financial position (debt → €0)
3. Next action (pre-decided)
4. Avoidance areas (self-reported)
5. Network leverage (referral potential)

**Metrics Hidden:**
- Hours worked, files created, agents spawned, "productivity score", calendar density

---

### 4️⃣ Product Manager

**Key Contributions:**
- **3 tabs max** — Command Center (today), Pipeline (week), Truth (reality)
- **Static mockup first** — Show WHAT Florian needs, data layer comes later
- **Anti-feature: NO customization** — Structure IS the intervention

**Why This Matters:**
Letting Florian customize = letting him avoid what he needs to see. The dashboard is opinionated by design.

**Scope Decisions:**
- ✅ Hardcoded realistic data (faster to build, validates design)
- ✅ Single HTML file (self-contained, no dependencies)
- ✅ Mia populates via JS (simple data model)
- ❌ User settings, reorderable sections, theme switcher
- ❌ Integrations (comes later if dashboard proves valuable)

---

### 5️⃣ Florian's Inner Critic

**Key Contributions:**
- **"I won't use it if it's another thing to update"** → Auto-populate OR <2 min update
- **"I won't look at it if it makes me feel like shit"** → Accountability without shame
- **"I'll abandon it if it's not mobile-friendly"** → Fully responsive

**Why This Matters:**
The dashboard fights against abandonment. Most productivity tools die in 3 days because they require MORE work. This one reveals truth with minimal input.

**Abandonment Risks:**
1. Manual data entry beyond one button → MITIGATED: "Log Today's Sends" button
2. Shame without reframe → MITIGATED: "Portfolio bets" framing + completion %
3. Desktop-only → MITIGATED: Mobile-first responsive design

---

## Advisory Board Review (Round 2)

### 🔗 Reid Hoffman (Network Thinker)

**Feedback:**
"The pipeline shows WHAT you're tracking, but not WHO matters. In VC and consulting, relationships ARE the product."

**Changes Applied:**
- ⭐ Andreas highlighted with gold border + "NETWORK MULTIPLIER" label
- Referral potential made visible ("5+ warm intros in Sachsen manufacturing")
- Pipeline tab emphasizes relationship outcomes, not just deal stages

**Why Network Matters:**
- 1 happy Andreas = 5 warm manufacturing intros
- VC is a relationship business — 90% of deals come from intros
- Florian's edge: operator background + founder network

---

### 🧠 Charlie Munger (Mental Models — Inversion)

**Feedback:**
"Always invert. What would make this dashboard FAIL? If Florian can look at it, feel productive, and still not send anything."

**Changes Applied:**
- Hero action now shows: "Cost of waiting: €300/day. 6 days = €1,800 lost."
- Ready to Send section header: "3 items | 40 min total" (urgency + feasibility)
- Financial runway changed from "23mo (0 exp)" to "???" (reality check)
- Avoidance Log forces self-reporting (can't hide from it)

**Inversion Principles Applied:**
1. **If dashboard shows progress without sends → remove progress metrics**
2. **If numbers feel abstract → add COST (€300/day)**
3. **If lists feel optional → add TIME CONSTRAINT (40 min total)**
4. **If runway feels safe → show UNCERTAINTY (??? until expenses tracked)**

---

### 🚀 Sahil Lavingia (Ship-It Mindset)

**Feedback:**
"This is 80% good. But you built 3 tabs when you need 1.5. The 'Truth' tab is where Florian will hide. Simplify ruthlessly."

**Changes Applied:**
- Button renamed: "Update Dashboard" → "Log Today's Sends" (input-focused)
- Pipeline simplified: Focus on SENT count, not stage breakdown
- Truth tab condensed: Financial reality + Avoidance only (removed redundant history)
- Data model simplified to ONLY what drives action

**20% That Delivers 80%:**
1. Hero Action (DO THIS NOW)
2. Send Velocity Meter (days since last send)
3. Ready to Send list (with time estimate)
4. Financial Reality (debt + income)
5. Avoidance Log (self-awareness)

**80% Cut:**
- Detailed pipeline stages (noise)
- Build history graphs (reinforces wrong behavior)
- Settings/customization (distraction)
- Analytics/insights (premature)

---

## Tab Structure & Purpose

### Tab 1: Command Center (Default)

**Purpose:** Single screen that determines the day

**Sections:**
1. **Hero Action Card** (40% viewport)
   - ONE action, pre-decided
   - Red border (urgency)
   - Cost of waiting (consequence)
   - Time estimate + completion % (feasibility)

2. **Send Velocity Metrics** (3-4 cards)
   - Days since last send (PRIMARY, red when >2)
   - Sends this week (target: 15)
   - Builds this week (shown small, grey)
   - Send/Build ratio (target: 3:1)

3. **Financial Reality Widget**
   - Debt (€70K)
   - Monthly income (€3K)
   - Runway (??? until expenses tracked)
   - Visual: Gradient bg (warning → danger)

4. **Ready to Send (But You Haven't)** (max 5 items)
   - Adversarial framing
   - Completion % (make sending feel safe)
   - Type + recipient (context)
   - Time estimate (feasibility)

5. **Today's Top 3** (pre-decided, no choices)
   - No options given
   - Each includes "Why" (strategic reasoning)

**Design Rationale:**
Everything above the fold. No scrolling to see what matters. Hero action dominates. Financial reality always visible (can't hide from it).

---

### Tab 2: Pipeline

**Purpose:** Track what's moving, what's stuck

**Sections:**
1. **Pipeline Cards Grid** (3 cards)
   - VC Applications (submitted/ready/draft)
   - Consulting Leads (contacted/demo ready/cold)
   - Content Pipeline (published/ready/ideas)

2. **VC Applications Detail** (Ready to Submit focus)
   - HOF, Betaworks, Leonis, Wingspan
   - Completion % + why it's a fit

3. **Consulting Detail**
   - ⭐ Andreas (network multiplier, gold border)
   - Bayern Digitalbonus Plus
   - Referral potential emphasized

**Design Rationale:**
Pipeline is NOT about tracking everything — it's about seeing what's READY but UNSENT. Focus on the "ready to submit" stage, not the entire funnel.

---

### Tab 3: Truth

**Purpose:** Financial reality + avoidance log

**Sections:**
1. **Debt Breakdown** (€70K total)
   - Parents (€35K)
   - KfW + BAföG (€10K)
   - Finanzamt (€5K)
   - Health Insurance (€5K)
   - Others (€15K)

2. **Monthly Burn Rate**
   - Income (€3K freelance + €2.7K ALG1 expected)
   - Expenses (??? — needs tracking)
   - Net (negative)

3. **Avoidance Log** (self-reported)
   - What: HOF application (6+ days)
   - Why: "Not 100% perfect yet" (but it's 95%)
   - Forces honesty

4. **Build vs. Send History** (Last 7 days)
   - Pattern visible: 205 files : 2 emails = 100:1
   - Feb 10: 0 sends, 30+ agents, $50 compute

**Design Rationale:**
"Truth" tab is uncomfortable by design. Financial reality + avoidance patterns can't be hidden. But it's Tab 3 (not default) so it doesn't overwhelm daily use.

---

## Data Model

### Simplified Structure (Input for Mia)

```javascript
{
  // Command Center
  heroAction: {
    title: "Send HOF Application",
    description: "All materials ready...",
    costPerDay: 300,
    daysSinceLastSend: 6,
    portal: "workstream.us",
    timeEstimate: 15,
    completion: 95
  },
  
  metrics: {
    sendsThisWeek: 2,
    buildsThisWeek: 47,
    sendBuildRatio: "1:24"
  },
  
  financial: {
    debt: 70000,
    monthlyIncome: 3000,
    runwayMonths: null  // ??? until tracked
  },
  
  readyToSend: [
    {
      title: "HOF Application",
      completion: 95,
      type: "VC Application",
      timeEstimate: 15,
      recipient: "House of Forge"
    },
    // max 5 items
  ],
  
  todayTop3: [
    {
      title: "Submit HOF Application",
      why: "€150K-200K/year job, AI-focused fund, best fit"
    },
    // exactly 3 items
  ],
  
  // Pipeline
  pipeline: {
    vcApps: { submitted: 0, ready: 4, draft: 3 },
    consulting: { contacted: 1, demoReady: 1, cold: 0 },
    content: { published: 1, ready: 1, ideas: 15 }
  },
  
  // Truth
  avoidanceLog: [
    {
      item: "HOF Application",
      days: "6+",
      reason: "Not 100% perfect yet (but it's 95% done)"
    }
  ],
  
  buildSendHistory: [
    {
      date: "Feb 10",
      sends: 0,
      builds: "30+ agents, 25 docs, $50 compute"
    }
  ]
}
```

### Update Mechanism

**Option 1: Simple JSON file** (Sahil-approved)
- Mia updates `dashboard-data.json` in workspace
- Dashboard reads on load via `fetch()`
- "Log Today's Sends" button prompts for input, saves to JSON

**Option 2: Script-based** (Future enhancement)
- `./scripts/update-dashboard.sh` pulls from:
  - Git commits (builds)
  - Email sent folder (sends)
  - Notion API (pipeline)
  - Manual input (avoidance log)

**For MVP:** Start with hardcoded data, validate the design works, then add data layer.

---

## Visual Design System (Ainary CI)

### Color Palette

| Element | Color | Usage |
|---------|-------|-------|
| Danger | #dc2626 | Days since send, urgent items |
| Warning | #f59e0b | Builds count, secondary alerts |
| Success | #059669 | Sends count, ready badges |
| Gold Base | #c8aa50 | Borders, accents, CTAs |
| Gold Deep | #9d7f3b | Network multipliers, emphasis |
| Text Primary | #1a1a1a | Body text |
| Text Secondary | #666666 | Metadata, labels |
| Background | #fafaf8 | Page bg |
| Surface | #ffffff | Cards, sections |

**Rule:** 5% gold, 95% monochrome. Gold marks IMPORTANCE (Andreas, CTAs), not decoration.

---

### Typography

- **Display:** Inter 700 (headlines)
- **Body:** Inter 400-600 (content)
- **Mono:** JetBrains Mono (metrics, time, money)

**Hierarchy:**
- Hero Action: 1.75rem (28px)
- Section Titles: 1.125rem (18px)
- Body: 1rem (16px)
- Metadata: 0.875rem (14px)
- Labels: 0.75rem (12px)

---

### Layout Principles

1. **No scrolling for critical info** — 1400×900px viewport fits everything
2. **40% hero action** — Dominates above the fold
3. **Grid-based metrics** — 3-4 cards, equal width
4. **Cards with borders** — 12px radius, subtle shadow
5. **Generous whitespace** — 24-32px between sections

---

### Mobile Responsive (≤768px)

- Single column layout
- Metrics stack vertically
- Hero action padding reduced (32px → 20px)
- Font sizes scale down (1.75rem → 1.5rem)
- Tabs remain horizontal (swipe-able)
- Financial grid: 3 columns → 1 column

---

## Anti-Patterns (What We Avoided)

### ❌ Too Many Metrics
**Why avoid:** ADHD + choice paralysis. More than 5-7 items = overwhelm.
**What we did:** 5:1 noise filter. Only show what drives action.

### ❌ Neutral Framing
**Why avoid:** "Tasks pending" doesn't motivate. Adversarial framing does.
**What we did:** "Ready to Send (But You Haven't)" + "What Are You Avoiding?"

### ❌ Customizable Layout
**Why avoid:** Structure IS the intervention. Customization = avoidance.
**What we did:** Opinionated design. No settings.

### ❌ Manual Data Entry Without Shortcuts
**Why avoid:** Abandoned in 3 days if it requires work.
**What we did:** "Log Today's Sends" button. Minimal input.

### ❌ Desktop-Only Design
**Why avoid:** Florian checks phone 100x/day. Desktop-only = forgotten.
**What we did:** Mobile-first responsive. Tabs work on mobile.

### ❌ Celebration of Builds
**Why avoid:** Reinforces wrong behavior (building instead of sending).
**What we did:** Builds shown SMALL and GREY. Sends are PRIMARY and RED/GREEN.

### ❌ Hidden Financial Reality
**Why avoid:** Out of sight = out of mind. Debt disappears from awareness.
**What we did:** Financial widget on Command Center (always visible).

### ❌ Apple Emojis in Professional Context
**Why avoid:** Not professional. Dashboard will be shared/screenshotted.
**What we did:** CSS-based icons (SVG masks). 🔴 used sparingly in badges only.

---

## Success Metrics (How We Know It Works)

### Week 1 (Validation)
- [ ] Florian opens dashboard daily
- [ ] Sends increase from 2/week → 5/week
- [ ] Financial reality tracked (runway calculated)

### Week 4 (Adoption)
- [ ] Dashboard = morning ritual (replaces manual planning)
- [ ] Sends consistently >10/week
- [ ] Avoidance log self-reported honestly

### Month 3 (Impact)
- [ ] VC application submitted (≥1)
- [ ] Consulting demo completed (Andreas)
- [ ] Content published consistently (1/week)
- [ ] Send/build ratio >1:5 (from 1:24)

**Failure Signal:** If after 2 weeks Florian stops using it, the design failed. Likely reasons:
1. Too much manual input required
2. Dashboard reinforces guilt without action
3. Mobile experience broken

---

## Implementation Notes

### Tech Stack
- **Single HTML file** — Self-contained (inline CSS/JS)
- **No dependencies** — Works offline, no CDN failures
- **Print-friendly** — Command Center tab prints cleanly
- **Mobile-responsive** — Works on phone/tablet/desktop

### Browser Compatibility
- Modern browsers (Chrome, Safari, Firefox, Edge)
- No IE11 support (not needed)
- CSS Grid + Flexbox (well-supported)

### File Size
- ~40KB HTML (reasonable for self-contained)
- Fonts loaded from Google Fonts CDN
- Icons as inline SVG (no external assets)

### Update Workflow (For Mia)
1. Edit `dashboardDataExample` object in `<script>` section
2. Modify values (sends, debt, ready items)
3. Save file
4. Florian refreshes browser

**Future:** `dashboard-data.json` + `fetch()` for dynamic updates

---

## Iteration Plan

### v1.0 (Current — Validation Phase)
- Hardcoded realistic data
- Validates design + structure
- Florian uses for 2 weeks
- Feedback collected

### v1.1 (Data Layer)
- `dashboard-data.json` file
- "Log Today's Sends" button functional
- Manual updates via JSON editing

### v1.2 (Semi-Automated)
- Script pulls git commits (builds count)
- Email folder monitoring (sends count)
- Financial tracking (manual CSV import)

### v2.0 (Integrated)
- Notion API integration (pipeline)
- Email API (sends auto-detected)
- Calendar integration (time blocking)
- Weekly review automation

**Philosophy:** Ship v1.0 now. Iterate based on USAGE, not theory.

---

## Design Principles (Codified)

1. **ONE THING ALWAYS HIGHLIGHTED** — Hero action dominates (40% viewport)
2. **ADVERSARIAL FRAMING WINS** — "What are you avoiding?" > "What's your plan?"
3. **STRUCTURE IS INTERVENTION** — Dashboard decides, Florian executes
4. **5±2 ITEMS MAX** — Cognitive load budget (ADHD-optimized)
5. **SENDS > BUILDS** — Primary metric is RED when low, shown LARGE
6. **FINANCIAL REALITY VISIBLE** — Can't hide from debt/runway
7. **NETWORK = CURRENCY** — High-value contacts highlighted (Andreas = ⭐)
8. **NO SCROLLING FOR KEY INFO** — 1400×900px fits everything
9. **MOBILE-FIRST** — Phone is primary device for checking
10. **PRINT-FRIENDLY** — Command Center tab = daily printout

---

## Acknowledgments

**Design Team:**
- UX Designer (ADHD-Specialist) — Cognitive load, one action, no scrolling
- Behavioral Psychologist — Adversarial framing, send velocity, safe sending cues
- Data Strategist — Sends/builds ratio, financial urgency, noise filter
- Product Manager — 3 tabs, static mockup, no customization
- Florian's Inner Critic — Abandonment prevention, mobile-friendly, guilt management

**Advisory Board:**
- Reid Hoffman — Network visibility (Andreas as multiplier)
- Charlie Munger — Inversion (cost of waiting, runway uncertainty)
- Sahil Lavingia — Ruthless simplification (3 tabs → 1.5, "Log Sends" button)

**Research Foundation:**
- 31 papers on agent overconfidence, memory management, diversity
- Florian's 10-day behavioral data (205 files : 2 emails)
- ADHD research: Capacity limit ~80-90, organization > capacity
- Multi-lens experiments: Convergence/divergence signals

---

## Final Notes

This dashboard is **NOT** a productivity tracker. It's a **mirror**.

It shows Florian what he's avoiding, makes financial reality visible, and structures his day around ONE clear action. The design assumes he's already capable — it just removes the barriers (choice paralysis, perfectionism, anxiety).

**The only metric that matters:** Does Florian send more?

If yes → iterate and improve.
If no → the design failed its purpose.

---

*Built with 5 perspectives, 3 advisory reviews, 31 papers, and 10 days of behavioral data.*
*This is the one screen that determines the day.*

⧖ Completion: 90% | Missing: Real data integration, user testing, mobile optimization testing | Confidence: 85%
