# Base44 Prompt — 5 Interactive Demos for Ainary

Build 5 separate interactive demos as pages within one app. Each demo should be fully functional, visually impressive, and use the same dark premium design system. The app has a home page that shows all 5 demos as cards — click to open each one.

Design reference: Linear.app + ElevenLabs.io. Dark background (#08080c), gold accent (#c8aa50), Geist font family. No gradients, no shadows. Flat, minimal, premium.

---

## DESIGN SYSTEM (applies to ALL demos)

- Background: #08080c (body), #111116 (cards/surfaces)
- Text: #ededf0 (primary), #8b8b95 (secondary), #55555e (muted)
- Accent: #c8aa50 (gold) — buttons, active states, highlights, progress bars
- Success: #4ade80 (green)
- Warning: #fbbf24 (yellow)
- Error: #f87171 (red)
- Info: #60a5fa (blue)
- Font: Geist Sans (body), Geist Mono (data, labels, numbers, code)
- Border radius: 16px cards, 8px buttons/pills, 4px small tags
- Borders: rgba(255,255,255,0.06)
- All pages fully responsive
- Smooth animations and transitions everywhere
- Dark mode only

---

## HOME PAGE: Demo Selector

Header: "Ainary — Interactive Demos"
Subtext: "Experience AI-powered intelligence systems. Pick a demo."

5 cards in a grid (2 columns on desktop, 1 on mobile). Each card has:
- Demo number + icon
- Title
- One-line description
- "Try it →" button (gold)
- Tag showing what it captures (e.g. "Captures: Company Name")

Cards:
1. 🔍 Company X-Ray — "Enter any company. Get an AI-generated executive analysis in seconds."
2. 📊 ROI Calculator — "Your industry + team size = personalized savings projection."
3. 🤖 Report Builder Live — "Watch 5 AI agents build a research report in real-time."
4. 🛡️ Trust Dashboard — "Explore how we measure quality across 30+ research reports."
5. 🧠 Knowledge Graph Explorer — "Navigate 18 months of compounding intelligence."

---

## DEMO 1: Company X-Ray

### Concept
User enters a company name. The system simulates an AI analysis and produces a beautiful executive summary card. This is the #1 lead capture tool.

### UI Flow

**Step 1: Input**
- Large centered heading: "Enter any company."
- Subtext: "Our agents analyze public data in seconds. See what they find."
- Large input field with gold focus border, placeholder: "e.g. Tesla, Stripe, BMW, your competitor..."
- Button: "Run X-Ray" (gold, full width below input)
- Below input, small text: "No signup required. Results in ~5 seconds."

**Step 2: Processing Animation (5 seconds)**
Show a dark card that animates through the 5 agent steps:
- Agent avatars appear one by one in a horizontal row, each with a name and status:
  1. 🔍 Researcher — "Scanning public data..." → after 1s: "Found 47 sources" (green check)
  2. 📊 Analyst — "Processing financials..." → after 2s: "Revenue signals identified" (green check)
  3. 🧠 Strategist — "Cross-referencing..." → after 3s: "3 patterns detected" (green check)
  4. ✍️ Writer — "Synthesizing report..." → after 4s: "Executive summary ready" (green check)
  5. ✅ QA — "Verifying claims..." → after 5s: "Confidence scored" (green check)
- Progress bar at bottom fills from 0% to 100% during the 5 seconds
- Each agent step has a subtle pulse animation while active

**Step 3: Result Card**
Beautiful dark card with:
- **Header**: Company name + logo (use https://logo.clearbit.com/{company}.com — if it doesn't load, show a placeholder icon)
- **AI Readiness Score**: Large number (generate a random score between 45-85) with a circular progress ring in gold
- **Industry**: Auto-classify based on company name (tech, manufacturing, finance, healthcare, etc.)
- **3 Key Signals** (generate plausible ones based on the company name):
  - Each with an icon, title, one-line description, and confidence tag (HIGH/MED/LOW)
  - Example for "BMW": "Manufacturing AI adoption accelerating" / "Supply chain optimization opportunity" / "Competitor Tesla 3 years ahead on autonomy"
- **Risk Assessment**: 2 items with red/yellow flags
- **Opportunity Score**: Green badge with percentage
- **Footer**: "Generated in 4.7 seconds · 47 sources scanned · Confidence: 72%"

**Step 4: Lead Capture**
Below the result card:
- "Want the full 47-page report with detailed analysis?"
- Email input field + "Get Full Report" button
- Small text: "We'll send the report within 24 hours. No spam."
- "Or book a call →" link to Calendly

**Database**: Save company_name, email (if provided), timestamp, generated_score to a "leads" table.

---

## DEMO 2: ROI Calculator

### Concept
User inputs their industry and team size. The calculator shows personalized time/cost savings projections based on real benchmarks.

### UI Flow

**Step 1: Input Form**
Heading: "How much time could you save?"
Subtext: "Based on real data from Anthropic (2025) and McKinsey (2025)."

Form fields (all styled as dark cards):
1. **Industry** — Dropdown: Manufacturing / Consulting / Financial Services / Healthcare / Technology / Media & Publishing / Legal / Other
2. **Team Size** — Slider or number input: 1-500 people
3. **Primary Use Case** — Radio buttons:
   - Research & Analysis
   - Due Diligence
   - Reporting & Documentation
   - Operations & Process Automation
4. **Current Time per Task** — Dropdown: "1-2 hours" / "Half a day" / "1-2 days" / "1 week" / "2+ weeks"

Button: "Calculate Savings" (gold)

**Step 2: Results Dashboard**
Animated counters that tick up to the final numbers:

**3 large KPIs:**
- ⏱️ Time Saved: "X hours/week" (based on: current_time × 0.8 reduction × tasks_per_week estimate)
- 💰 Annual Savings: "€XX,XXX/year" (based on: hours_saved × avg_hourly_rate_for_industry)
- 📈 Output Multiplier: "X.Xx" (based on industry benchmarks, 2-3× range)

**Breakdown Table:**
| Task | Before | After | Savings |
Populated with industry-specific tasks. Example for "Consulting":
- Competitive Analysis: 3 weeks → 5 min
- Board Preparation: 2 days → 5 min
- Client Report: 1 week → 30 min
- Market Research: 2 weeks → Minutes

**Benchmark Context:**
- "80% faster task completion — Anthropic Research, 2025 (100K conversations analyzed)"
- "AI power users produce 2-3× more output — McKinsey, 2025"
- Small chart showing industry average vs. with AI systems

**CTA:**
- "These numbers are conservative. Let's discuss your specific case."
- "Book a 15-min call →" (Calendly link)
- Optional email capture: "Send me this report"

**Database**: Save industry, team_size, use_case, calculated_savings, email to "roi_leads" table.

---

## DEMO 3: Report Builder Live

### Concept
User enters a research topic. They watch an animated simulation of 5 AI agents building a report in real-time, with live-updating content panels.

### UI Flow

**Step 1: Topic Input**
Heading: "Watch AI agents build a research report."
Subtext: "Enter any topic. See the process unfold."
Input field: "e.g. AI in manufacturing, European VC landscape, Remote work trends..."
Button: "Build Report" (gold)

**Step 2: Live Builder (30-second animation)**

Split layout:
- **Left panel (40%)**: Agent Pipeline
- **Right panel (60%)**: Report Preview (builds up in real-time)

**Left Panel — Agent Pipeline:**
Vertical timeline with 5 agents, each activates in sequence:

Agent 1: 🔍 Researcher (0-6s)
- Status: "Scanning 5 platforms..."
- Live counter: "Sources found: 0 → 12 → 28 → 47"
- Source pills appear one by one: "ArXiv" "SEC" "News" "GitHub" "Industry Reports"
- When done: green check, "47 sources collected"

Agent 2: 📊 Analyst (6-12s)
- Status: "Processing data..."
- Live items: "Key finding identified" × 4 (appear one by one)
- Confidence bars animate filling up
- When done: green check, "4 key findings extracted"

Agent 3: 🧠 Strategist (12-18s)
- Status: "Cross-referencing claims..."
- Claim transparency bar animates: Evidenced 62% / Interpreted 24% / Judgment 14%
- "3 contradictions detected → resolved"
- When done: green check, "Framework synthesized"

Agent 4: ✍️ Writer (18-24s)
- Status: "Drafting report..."
- Word counter ticking up: "0 → 500 → 1,200 → 2,400 words"
- Section titles appear: "Executive Summary ✓" "Key Findings ✓" "Recommendations ✓"
- When done: green check, "Report drafted"

Agent 5: ✅ QA (24-30s)
- Status: "Running quality checks..."
- Checklist items tick off: "Source verification ✓" "Claim accuracy ✓" "Bias scan ✓" "Confidence scoring ✓"
- QA Score animates: "16/20 → 17/20 → 18/20"
- When done: green check, "QA complete — 18/20"

**Right Panel — Report Preview:**
A report card that fills in progressively as agents work:
- Header appears at 0s: Report title (based on user input) + "AR-XXX · FEB 2026"
- Executive Summary text fades in during Writer phase
- Key Findings appear one by one during Analyst phase
- Confidence bars fill during QA phase
- Final confidence badge appears: "73% CONFIDENCE"

**Step 3: Completed Report**
Full report card with:
- Title, confidence score, executive summary
- 4 key findings with source citations
- Confidence breakdown bars
- Claim transparency bar
- Stats: "47 sources · 5 agents · 3 synthesis rounds · built in 28 seconds"
- "In production, this takes ~10 minutes with deeper analysis."

**CTA:**
- "See a real report →" links to the AR-001 Agent Trust report
- "Get a custom report for your industry →" Calendly link

---

## DEMO 4: Trust Dashboard

### Concept
Interactive dashboard showing quality metrics across Ainary's published reports. Executives can explore how quality is measured — transparency as a product feature.

### UI Flow

**Dashboard Layout:**

**Top Bar:**
- "Trust Dashboard — Ainary Research Quality Metrics"
- Filter pills: "All Reports" · "High Confidence" · "Medium" · "2026" (toggleable)

**Summary Cards (top row, 4 cards):**
- Total Reports: 32 (with small chart showing growth over time)
- Avg Confidence: 71% (gold progress ring)
- Total Sources: 1,200+ (counter)
- Avg QA Score: 17.5/20 (green badge)

**Main Section: Report Quality Matrix**
Interactive table/grid showing all reports:

| Report | Confidence | Sources | QA | Claim Transparency | Date |
|--------|-----------|---------|-----|-------------------|------|
| AR-001 State of Agent Trust | 73% | 47 | 18/20 | E:62% I:24% J:14% | Feb 2026 |
| AR-031 Personal AI Stack | 72% | 38 | 17/20 | E:58% I:28% J:14% | Feb 2026 |
| AR-032 Knowledge Compounding | 62% | 29 | 16/20 | E:51% I:32% J:17% | Feb 2026 |

(Generate 10-15 more rows with plausible report titles and metrics)

Each row is clickable → expands to show:
- Executive summary (2 lines)
- Source diversity breakdown (pie chart: Industry Reports, Academic, News, Practitioner)
- Top 3 claims with evidence tags [E] [I] [J]
- "Read full report →" link

**Right Sidebar: Methodology**
Expandable sections:
- "What is Confidence?" — explanation of the scoring
- "Claim Transparency" — what E/I/J means
- "QA Process" — the 5-agent pipeline
- "Why we publish these numbers" — transparency statement

**Bottom: Comparison**
"How does this compare?"
- Traditional consulting: "Trust us" (no metrics)
- Ainary: Every claim sourced, every gap disclosed, every confidence scored
- Visual comparison showing Ainary's transparency advantage

---

## DEMO 5: Knowledge Graph Explorer

### Concept
Interactive visualization of a knowledge graph showing how information compounds over time. Nodes represent concepts, edges represent connections. Users can explore and click into topics.

### UI Flow

**Main View: Force-directed graph**
- Dark background with floating nodes (circles)
- Nodes are different sizes based on importance/connections
- Nodes are colored by category:
  - Gold: AI & Technology
  - Green: Business & Strategy  
  - Blue: Research & Data
  - Purple: People & Organizations
  - White: Core Concepts

- Edges (lines) connect related nodes, with varying thickness based on connection strength
- The graph gently animates/breathes (nodes slightly move)

**Node Examples (pre-populated, ~80-100 nodes):**
Core cluster: "AI Agent Trust" → connects to "Confidence Scoring", "Claim Transparency", "Source Verification", "QA Pipeline"
Business cluster: "CNC Manufacturing" → "REFA Calculation", "Quoting Automation", "€50K Savings"
Research cluster: "AR-001" → "HBR 6% Trust", "Gartner 40% Canceled", "Trust Race Model"
People cluster: "McKinsey" → "2-3× Output", "Anthropic" → "80% Faster"
Technology cluster: "Multi-Agent Systems" → "Researcher", "Analyst", "Strategist", "Writer", "QA"

**Interactions:**
- **Hover** a node: highlights all connected nodes and edges, dims the rest
- **Click** a node: opens a sidebar panel with:
  - Node title
  - Category tag
  - Description (2-3 sentences)
  - "Connected to:" list of linked nodes (clickable)
  - "First seen:" date
  - "Times referenced:" count
  - If it's a report: "Read report →" link
- **Scroll** to zoom in/out
- **Drag** nodes to rearrange
- **Search bar** at top: type to find and highlight specific nodes

**Stats Bar (bottom):**
- "2,400 memories · 180 relationships · 50 behavioral patterns · 18 months compounding"
- "Every conversation makes the system smarter. Every connection compounds."

**Time Slider:**
A slider at the bottom that lets users scrub through time (Month 1 → Month 18)
- As the slider moves, nodes and connections appear progressively
- Shows how the knowledge graph grew from empty to dense
- Counter shows: "Month 1: 12 nodes, 8 edges" → "Month 18: 2,400 nodes, 4,200 edges"
- This is THE money shot — visually shows compounding knowledge

**CTA:**
- "This is what happens when AI systems remember everything and forget nothing."
- "Build your knowledge engine →" Calendly link

---

## DATABASE SCHEMA

### Table: leads
- id (auto)
- demo (text: "xray" / "roi" / "report" / "trust" / "graph")
- company_name (text, nullable)
- email (text, nullable)
- industry (text, nullable)
- team_size (number, nullable)
- generated_data (JSON, nullable — stores the generated result)
- timestamp (datetime, auto)

### Table: demo_interactions
- id (auto)
- demo (text)
- action (text: "started" / "completed" / "cta_clicked")
- metadata (JSON, nullable)
- timestamp (datetime, auto)

---

## IMPORTANT NOTES
- All demos should feel INSTANT and POLISHED. Animations matter.
- The "AI processing" is simulated — we're not calling real APIs. Generate plausible data based on input.
- Every demo should end with a clear CTA to Calendly: https://calendly.com/florian-ainaryventures/15-minutes-chat
- Mobile responsive is critical — executives will view on phones.
- The Knowledge Graph should be the visual showpiece — spend extra effort on making it beautiful.
- Lead capture is optional (never required) — reduce friction.
