# Base44 Prompt — Ainary Intelligence Platform

Build a premium dark-themed AI intelligence platform called "Ainary." This is not just a website — it's an interactive product that lets prospects experience AI-powered research before they buy.

Design reference: Linear.app (clean, dark, precise) + ElevenLabs.io (product-forward). Dark background (#08080c), gold accent (#c8aa50), Geist font family.

---

## CORE CONCEPT

Ainary is an AI consulting company that builds multi-agent systems for executives. The platform has two sides:

1. **PUBLIC SIDE** — Marketing + Interactive Demo (no login required)
2. **ADMIN SIDE** — Lead dashboard + Report management (login required, only for the founder)

---

## PUBLIC PAGES

### Page 1: Landing Page (/)

**Navigation** (sticky):
- Logo "Ainary" with gold dot animation
- Links: Research · Use Cases · About · Blog
- CTA: "Get in touch" (gold button → Calendly link)
- No login/signup in nav

**Hero Section:**
- H1: "Multiply your team." (3.75rem, weight 600, tight letter-spacing)
- Subheadline: "We do 80% of the work. You do the 20% that matters." (1.6rem, weight 600)
- Body: "Reports, analysis, due diligence, operations — in minutes, not weeks. Five agents research, verify, and synthesize — so you can focus on what only humans can: judgment, relationships, and decisions. Not a replacement. A multiplier."
- Two buttons: "Get in touch" (gold) + "Try it yourself" (outline — THIS IS KEY, scrolls to interactive demo)

**KPI Bar** (3 metrics, gold numbers, monospace):
- 80% / Task Automation
- ~10 Min / Not Days or Weeks
- 2-3× / More Output (with superscript ¹ linking to McKinsey source: https://www.mckinsey.com/capabilities/tech-and-ai/our-insights/unleashing-developer-productivity-with-generative-ai)
- Small footnote below: "¹ McKinsey, 'Unleashing developer productivity with generative AI,' 2023"

**Interactive Demo Section** ⭐ (THE KILLER FEATURE):
Header: "Try it yourself. Enter any company name."
- Large input field with gold border: placeholder "e.g. Tesla, Stripe, your competitor..."
- Button: "Generate Snapshot" (gold)
- When user submits:
  - Show animated loading state with 5 agent avatars "working" (Researcher → Analyst → Strategist → Writer → QA)
  - After 3-5 seconds, display a "Company Snapshot" card:
    - Company name + logo (fetch from clearbit logo API: https://logo.clearbit.com/{domain})
    - Industry classification
    - 3 "AI Readiness Signals" (generate plausible ones based on company name)
    - Confidence score with gold progress bar
    - "Want the full 47-page report? Get in touch →" CTA
  - **IMPORTANT**: Save the company name + email (if provided) to the database as a lead
  - Below the snapshot: "This took 4 seconds. The full report takes 10 minutes. Imagine what that means for your workflow."

**Showcase Tabs** (3 tabs):

Tab 1: "AI Research" (default active)
- Sub-pills: Agent Trust · Personal AI Stack · Knowledge Compounding
- Shows AR-001 report preview:
  - Left column: Executive Summary ("The 51-point chasm between deployment 57% and trust 6%...") + 4 Key Findings with gold left-border accent (6% trust, 87% experiment, 40% canceled, 7-month doubling)
  - Right column: Confidence Breakdown bars (Data Quality 78%, Source Diversity 82%, Recency 71%, Methodology 65%) + Claim Transparency bar (Evidenced 62% / Interpreted 24% / Judgment 14%) + Stats boxes (47 Sources, 18/20 QA, <10m Build)
  - Footer: agent chips (Researcher, Analyst, Strategist, Writer, QA)
  - CTA: "Read the full report →" links to /research/state-of-agent-trust-2026/

Tab 2: "Due Diligence"
- Fake company "Arclight AI" analysis
- Left: Company overview + 3 stat boxes ($14.2M raised, 340% YoY, Series B)
- Right: Confidence assessment with dot ratings (Team ●●●, Market ●●●, PMF ●●○, Economics ●○○) + Hidden Signal box ("CTO GitHub activity dropped 80%")
- Footer: "2 red flags · 1 hidden signal · Recommendation: Conditional Pass"

Tab 3: "AI Systems"
- CNC manufacturing case
- Left: Executive summary (35 employees, manual quoting 45min, 23% orders lost) + stats (€40-60K/yr savings, 92% time saved, 3mo break-even)
- Right: Key recommendations (numbered list) + Hidden Insights (Surprising + Contrarian) + Strategic Risks
- CTA: "Talk about your process →"

**Process Animation Section:**
Header: "From technical drawing to quote in 4 minutes."
5-step vertical timeline with animated progression:
1. 📄 PDF uploaded — part specs appear
2. 🔍 Drawing Analysis — extracted data items animate in (Material, Dimensions, Tolerance, Surface, Batch)
3. 📊 Supplier Cross-Reference — price/availability data
4. ⚙️ REFA Calculation — progress bars animate (Milling, Turning, QA)
5. ✅ Quote Generated — full cost breakdown card appears with confidence score
After animation: Before/After comparison grid (red vs green cards)
Timer running in corner showing elapsed time

**Trust Section:**
Heading: "In a world of noise, clarity wins."
3 cards:
1. Source-grounded — list of source types in monospace
2. Honest about gaps — confidence dot-rating explanation
3. Operator perspective — 5 agent role pills in gold

**Why I Built This:**
2-column: Photo left (240×280px rounded) + text right
Text: "McKinsey found that AI power users produce 2-3× more output. What I've seen is significantly more — because an agent system has unlimited resources once you've built the process, system, and standard. The standard keeps rising..."
Signature: "— Florian Ziesche, Founder" + LinkedIn/Substack links

**Published Research:**
3 report cards linking to real URLs:
1. "State of AI Agent Trust 2026" → /research/state-of-agent-trust-2026/ (HIGH badge)
2. "Personal AI Stack Architecture 2026" → /research/personal-ai-stack-2026/ (HIGH badge)
3. "Knowledge Compounding 2026" → /research/knowledge-compounding-2026/ (MED badge)

**Use Cases Section:**
Two feature blocks with real data:

Block 1: "12 months of development → 1 week"
- CNC quoting system description
- Tech pills: REFA · CAD/CAM · Heidenhain · Python · FastAPI · LLM
- Stats: 92% Time saved · €40-60K/yr Projected · 1 week Implementation

Block 2: "A compounding knowledge engine that never forgets"
- Second Brain / multi-agent description
- Stats: 24/7 Always on · Minutes Not days · ∞ Compounding

**Before/After Comparison Table:**
8 rows showing time savings:
- Competitive Analysis: 3 weeks → 5 min
- Board Preparation: 2 days → 5 min
- Grants & Subsidies: Unknown → Mapped
- Content Creation: 1 week → 30 min
- Trend Tracking: Ongoing → Automated
- Investor Reporting: 2 weeks → Minutes
- Technology Scouting: Ongoing → Automated
- CEO Decision Support: Memory → Second Brain

**How it works in practice:**
3 example prompts showing real use cases:
1. "Create a custom offer for Company X with competitive analysis and pricing recommendation."
2. "Research 27 VC funds that invest in AI-first startups. Include team backgrounds and application angles."
3. "Write a consulting pitch for a newspaper publisher. 4 documents: Executive Brief, ROI Analysis, Case Study, Implementation Plan."

**Day 1-7 Timeline:**
Visual timeline showing what was built in one week:
- Day 1: CNC pilot (€40-60K/yr projected)
- Day 2: Consulting pitch (Overnight)
- Day 3: 27 VC funds (1 session)
- Day 5: 18-page platform (48 hours)
- Day 7: Knowledge graph (Compounding)

**FAQ Section** (accordion):
- "Is this for my industry?" → Yes, any industry where decisions depend on information
- "Do I need technical knowledge?" → No
- "What does compounding mean?" → Every interaction makes the system smarter
- "Is my data private?" → Yes, no storage beyond session, no model training

**Footer:**
Logo + links (Research · About · Blog · Contact · Imprint · Privacy · Terms) + copyright "© 2026 Ainary Ventures. Dresden / NYC."

---

### Page 2: Use Cases (/use-cases)
Full detailed use cases page (content from tools.html — same as above Use Cases section but expanded)

### Page 3: About (/about)
- Founder photo + bio
- Name: Florian Ziesche
- Title: Former CEO & MD at 36ZERO Vision · €5.5M raised · BMW, Siemens, Bosch
- Story: 5 years building enterprise AI
- Links: LinkedIn, Substack

### Page 4: Research (/research)
List of published reports with cards linking to external URLs

### Page 5: Blog (/blog)
Simple blog listing page

---

## ADMIN DASHBOARD (login required, single user: founder)

### Admin: Leads Dashboard
- Table of all leads from the Interactive Demo
- Columns: Company Name · Email (if provided) · Timestamp · IP/Location · Snapshot Generated (Y/N)
- Sort by date, filter by company
- Export to CSV

### Admin: Analytics
- Total demo interactions (chart over time)
- Most searched companies
- Page views per section
- Tab click distribution (AI Research vs Due Diligence vs AI Systems)
- Average time on page

### Admin: Report Manager
- List of published reports with links
- Add/edit report metadata (title, badge, URL, description)
- Toggle visibility on public pages

---

## TECHNICAL REQUIREMENTS

### Database Tables:
1. **leads** — company_name, email, timestamp, source_page, snapshot_data
2. **demo_interactions** — company_name, timestamp, completed (boolean)
3. **page_analytics** — page, section, action, timestamp
4. **reports** — title, description, url, badge, published (boolean), sort_order

### Integrations:
- Clearbit Logo API for company snapshots (https://logo.clearbit.com/{domain})
- Calendly embed or link (https://calendly.com/florian-ainaryventures/15-minutes-chat)
- Optional: OpenAI API for generating dynamic company snapshots (if available in Base44)

### Design System:
- Background: #08080c (body), #111116 (cards)
- Text: #ededf0 (primary), #8b8b95 (secondary), #55555e (muted)
- Accent: #c8aa50 (gold)
- Success: #4ade80 (green)
- Error: #f87171 (red)
- Font: Geist Sans (body), Geist Mono (data/labels)
- Border radius: 16px cards, 8px buttons
- NO gradients, NO shadows. Flat, minimal, Linear-style.
- Fully responsive (mobile-first)
- Dark mode only

### Performance:
- Lazy load below-fold sections
- Smooth scroll-reveal animations (fade-in + slide-up)
- Tab switching without page reload
- Demo interaction should feel instant (fake the AI processing with 3-5 second animation)
