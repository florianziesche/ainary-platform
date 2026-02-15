# Base44 Prompt — Ainary Ventures Landing Page

Build a dark, premium landing page for "Ainary" — an AI consulting company that builds multi-agent systems for executives. Design reference: Linear.app and ElevenLabs.io. Dark background (#08080c), gold accent (#c8aa50), Geist font.

---

## SECTION 1: Navigation (sticky top)
- Logo: "Ainary" with a small animated gold dot before the name (3 concentric rings, pulsing)
- Nav links: Research · Use Cases · About · Blog
- Right side: "Get in touch" gold button → links to https://calendly.com/florian-ainaryventures/15-minutes-chat
- No login, no signup, no pricing
- Mobile: hamburger menu with same links

## SECTION 2: Hero (centered, lots of whitespace)
- H1: "Multiply your team." — 3.75rem, font-weight 600, letter-spacing -0.025em, line-height 1.05
- Subheadline: "We do 80% of the work. You do the 20% that matters." — 1.6rem, font-weight 600, letter-spacing -0.02em
- Body text: "Reports, analysis, due diligence, operations — in minutes, not weeks. Five agents research, verify, and synthesize — so you can focus on what only humans can: judgment, relationships, and decisions. Not a replacement. A multiplier." — 0.9rem, gray (#8b8b95), max-width 600px
- Two buttons: "Get in touch" (gold, solid) and "See For Yourself" (outline, border only)
- Both centered

## SECTION 3: Product Showcase (tabbed)
Header: "This is what 5 agents produce in 10 minutes."
Subtext: "No mockups. Actual reports from public data. Judge the quality yourself."

3 tabs with monospace labels: "AI Systems" · "AI Research" · "Second Brain"
Active tab has gold background tint and gold border.

### Tab 1: AI Systems (CNC Manufacturing Case)
A dark card with rounded corners (16px), subtle border.
- Header bar: Date "Feb 12, 2026" left, "Custom Report" and "Share" buttons right
- Body: 2-column grid
  - Left column "EXECUTIVE SUMMARY": Description of a CNC contract manufacturer (35 employees, manual quoting takes 45 min, 23% orders lost). Below: 3 stat boxes in a row: "€40-60K/yr projected savings" · "92% Quoting Time Saved" · "3 mo Break-Even"
  - Right column: "KEY RECOMMENDATIONS" (numbered list: AI-powered quoting 45min→4min, automated pipeline 3 days→2 hours, machine utilization +18%). Then "HIDDEN INSIGHTS" with Surprising + Contrarian findings. Then "STRATEGIC RISKS" (3 bullet points about labor shortage, digital expectations, competitors)
- Footer bar: "47 pages · 5 agents · 3 synthesis rounds · generated in < 5 min" in monospace
- CTA below card: "Analyze any company →" in gold

### Tab 2: AI Research (Due Diligence Report)
Same card style.
- Header: Date + buttons
- Body 2-column:
  - Left "COMPANY OVERVIEW": Description of "Arclight AI" (autonomous agent orchestration, strong team, unproven economics). 3 stat boxes: "$14.2M Total Raised" · "340% YoY Growth" · "Series B Current Round"
  - Right "CONFIDENCE ASSESSMENT": 4 rows with dot ratings (Team ●●● / Market ●●● / PMF ●●○ / Unit Economics ●○○), each with explanation. Then a "HIDDEN SIGNAL" highlight box: "CTO's GitHub activity dropped 80%"
- Footer: "32 pages · 5 agents · 2 red flags · 1 hidden signal · Recommendation: Conditional Pass"
- CTA: "Run due diligence →"

### Tab 3: Second Brain (AI Research Report)
Same card style.
- Header: Sub-tabs for research topics: Prompting · Autonomous Agents · AI Governance · Agent Economics · World Models (monospace pills, active one gold)
- Body 2-column:
  - Left "EXECUTIVE SUMMARY": Text about prompt engineering converging with agent design. "KEY FINDINGS": 3 findings with left-border accent (self-refining prompts +40%, domain-specific libraries losing value, multimodal prompting 3x richer)
  - Right "RECOMMENDATIONS": 3 priority items (HIGH/MED/WATCH labels). "CONFIDENCE": ●●● High — 47 sources, 23 peer-reviewed. "INCLUDED RESOURCES": 3 items with file icons (Prompt Evaluation Framework, Prompt Asset Library 42 templates, ROI Calculator)
- Footer: "47 sources · 5 platforms · 3 synthesis rounds"
- CTA: "Start your research →"

## SECTION 4: Use Cases Link
Simple centered section: "Explore all use cases →" gold link

## SECTION 5: Trust & Clarity
Heading: "In a world of noise, clarity wins."

3 cards in a row:
1. **Source-grounded**: "Every claim linked to its source." List of source types in monospace: SEC Filings · Annual Reports · ArXiv Papers · News Wires · Industry Reports · Patent Databases · Market Data · GitHub · Reddit · Hacker News
2. **Honest about gaps**: Confidence indicator explanation with 3 dot-rating levels (High ●●● / Medium ●●○ / Low ●○○) with descriptions
3. **Operator perspective**: "Built by someone who runs companies — not a research lab." 5 agent role pills in gold: Researcher · Analyst · Strategist · Critic · Synthesizer

Below the 3 cards: 3 large KPI numbers centered:
- "< 10 min" / per automated task
- "+10x" / your team  
- "+$10K" / savings per task
Numbers in monospace, 3rem, bold.

## SECTION 6: Why I Built This
Heading: "Why I built this"
2-column layout:
- Left: Photo (240×280px, rounded corners 16px, border). Image URL: florian.jpg
- Right: Two paragraphs explaining the founder's background (5 years enterprise AI, raised VC, delivered to BMW/Siemens/Bosch, built 5-agent system). Signature: "— Florian Ziesche, Founder". Links: LinkedIn · Substack · Links

## SECTION 7: Published Research
Heading: "Published Research"
3 cards in a row, each linking to a report:
1. "State of AI Agent Trust 2026" — badge: HIGH
2. "Personal AI Stack Architecture 2026" — badge: HIGH  
3. "Knowledge Compounding: Obsidian + Agent" — badge: MED
Each card has title, description, and "Read →" link.

## SECTION 8: Footer
Simple dark footer with:
- Logo "Ainary" left
- Links: Research · About · Blog · Contact · Imprint · Privacy · Terms
- Copyright: "© 2026 Ainary Ventures. Dresden / NYC."

---

## DESIGN SYSTEM
- Background: #08080c (body), #111116 (cards/surfaces)
- Text: #ededf0 (primary), #8b8b95 (secondary), #55555e (muted)
- Accent: #c8aa50 (gold) — buttons, active states, badges, highlights
- Borders: rgba(255,255,255,0.06) default, rgba(255,255,255,0.08) light
- Font: Geist Sans for body, Geist Mono for labels/stats/code
- Border radius: 16px for cards, 8px for buttons/pills
- Animations: Subtle scroll-reveal (fade-in + slide-up), smooth tab transitions
- Mobile: Fully responsive, single column on mobile, hamburger nav
- NO gradients, NO shadows, NO colored backgrounds. Flat, minimal, Linear-style.
