# AI Tools Platform — Konzept & Strategie
*Erstellt: 2026-02-12 04:45 CET*
*Zweck: Platform Website die alle AI Tools unter einem Dach vereint*

---

## 🎯 Vision

**"AI Tools That Replace $200K Consultants"**

Eine einheitliche Platform für AI-powered Strategic Intelligence. Statt 5 separate Tools, ein Ecosystem das zeigt: Florian Ziesche baut die Zukunft der Unternehmensberatung.

---

## 📦 Produkt-Portfolio

| Tool | Zielgruppe | Wertversprechen | Status |
|------|------------|----------------|--------|
| **Corporate X-Ray** | CEOs, Strategy Teams | McKinsey-Level AI Strategy Audit in 5 Min | ✅ Live |
| **Startup X-Ray** | VCs, Angels | AI Due Diligence + Deal Score | 🔨 Feb '26 |
| **AI Advisory Board** | Founders, Executives | 5 AI Experten diskutieren deine Frage | ⏳ Geplant |
| **Research Engine** | Analysts, Strategists | Academic-Grade Research in Minuten | ⏳ Geplant |
| **Personal Intelligence Feed** | Knowledge Workers | Dein persönlicher Research Assistant | ⏳ Geplant |

---

## 🎨 Design-System

### Farben (Unified Gradient)
Jedes Tool hat eine Akzentfarbe. Der Platform-Gradient vereint alle:

- **Corporate X-Ray:** #6366f1 (Indigo) — Enterprise Trust
- **Startup X-Ray:** #8b5cf6 (Purple) — Innovation
- **AI Advisory Board:** #ec4899 (Pink) — Collaboration
- **Research Engine:** #f59e0b (Amber/Gold) — Knowledge
- **Intelligence Feed:** #10b981 (Emerald) — Real-time

**Platform-Gradient:** `linear-gradient(135deg, #6366f1, #8b5cf6, #ec4899, #f59e0b, #10b981)`

### Design-Prinzipien
1. **Dark Mode First:** #0a0a0f Background (gleich wie X-Ray Reports)
2. **Glassmorphism Cards:** Semi-transparent mit backdrop-blur
3. **Inter Font:** Professionell, lesbar, modern
4. **SVG Icons:** Heroicons-Style, 24x24, keine Emoji
5. **Responsive:** Mobile-first, breakpoints bei 640px / 1024px / 1280px
6. **Single Page:** Kein Framework, pure HTML/CSS/JS

### Komponenten-Hierarchie
```
Hero (Full Viewport)
  ↓
Tool Grid (5 Cards, 2-3 Spalten Desktop, 1 Spalte Mobile)
  ↓
Email Capture (Newsletter Modal/Section)
  ↓
Social Proof (Logos / Testimonials — wenn vorhanden)
  ↓
About (Florian Ziesche Background)
  ↓
Pricing (Free / Pro / Enterprise)
  ↓
Footer (Links, Legal, Social)
```

---

## 🧩 Sections — Detailed Specs

### 1. Hero Section
**Ziel:** In 5 Sekunden klar machen was das ist + warum es wertvoll ist.

**Elemente:**
- **Headline:** "AI Tools That Replace $200K Consultants"
- **Subheadline:** "Strategic Intelligence in Minutes, Not Months. Built by Florian Ziesche."
- **CTA (Primary):** "Explore Tools" (scroll to grid)
- **CTA (Secondary):** "Join Newsletter" (modal/popup)
- **Visual:** Animated Gradient Orb/Mesh (CSS animation, kein Canvas)
- **Badge:** "Launching Monday, Feb 16 2026" (temporary, remove after launch)

**Mood:** Confidence, Ambition, Speed. "Du verschwendest Geld auf langsame Berater."

---

### 2. Tool Grid
**Layout:** 5 Cards, 2 Spalten (Desktop 1280px+), 3 Spalten (Desktop 1024px), 1 Spalte (Mobile)

**Card-Struktur:**
```
┌──────────────────────────────┐
│ [SVG Icon]   [Badge: Status] │
│ Tool Name                     │
│ 2-3 Sätze: Was es macht +    │
│ warum es besser ist           │
│ ────────────────────────────  │
│ [Try Free] [Learn More]      │
└──────────────────────────────┘
```

**Card 1: Corporate X-Ray**
- **Icon:** Building/Office SVG (Indigo)
- **Badge:** "Live" (Green dot)
- **Description:** "AI-powered strategy audit for your company. What McKinsey charges $200K for, delivered in 5 minutes. Honest, data-driven, provocative."
- **CTA:** "Generate Report" → `/corporate-xray`

**Card 2: Startup X-Ray**
- **Icon:** Rocket SVG (Purple)
- **Badge:** "Beta" (Yellow dot)
- **Description:** "VC-grade due diligence for any startup. Deal score, red flags, and the questions your associates should be asking—but aren't."
- **CTA:** "Try Beta" → `/startup-xray`

**Card 3: AI Advisory Board**
- **Icon:** Users/Team SVG (Pink)
- **Badge:** "Coming Soon" (Grey)
- **Description:** "5 AI experts (Yann LeCun, Fei-Fei Li, Andrew Ng, Demis Hassabis, Sam Altman) debate your strategic question. Like having the smartest room—on demand."
- **CTA:** "Join Waitlist" → Email capture

**Card 4: Research Engine**
- **Icon:** MagnifyingGlass/Search SVG (Gold)
- **Badge:** "Coming Soon" (Grey)
- **Description:** "Academic-grade research in minutes. Synthesize 100+ papers, blogs, and reports into a single strategic brief. No hallucinations, full citations."
- **CTA:** "Join Waitlist" → Email capture

**Card 5: Personal Intelligence Feed**
- **Icon:** Lightning/Bolt SVG (Emerald)
- **Badge:** "Coming Soon" (Grey)
- **Description:** "Your personal AI research assistant. Tracks 1,000+ sources, learns what matters to you, delivers insights before your competitors see them."
- **CTA:** "Join Waitlist" → Email capture

---

### 3. Email Capture (Newsletter)
**Placement:** Between Tool Grid und Social Proof (oder als Modal bei "Join Waitlist")

**Headline:** "Get Early Access + Weekly AI Strategy Insights"

**Form:**
- Name (optional, pre-filled wenn bekannt)
- Email (required)
- Tool Interest (dropdown: Corporate X-Ray / Startup X-Ray / All / Other)
- CTA: "Join Waitlist"

**Privacy:** "No spam. Unsubscribe anytime. Read [Privacy Policy]."

**Backend:** Form POST zu n8n webhook (noch zu implementieren) oder Mailchimp/ConvertKit.

---

### 4. Social Proof
**IF available** (Florian hat evtl. noch keine Logos/Testimonials):

- **Logos:** "Used by teams at [Horváth] [Capgemini] [Roland Berger]"
- **Stats:** "X reports generated | Y companies analyzed"
- **Testimonials:** 1-2 Quotes (wenn vorhanden)

**IF NOT available:**
- Skip this section completely
- OR: "Launching Monday Feb 16, 2026. Be the first."

---

### 5. About Florian Ziesche
**Ziel:** Trust + Authority aufbauen.

**Struktur:**
```
[Photo]  Florian Ziesche
         Founder, AI Tools Platform
         
         "I spent years watching $200K consultants deliver
         obvious insights in 6 months. AI can do it in 5 minutes—
         but only if you build it right. These tools are how
         strategy SHOULD work: fast, honest, and always learning."
         
         [LinkedIn] [Twitter] [Substack]
```

**Bullets:**
- 🎓 Strategy Consultant Background (wenn relevant)
- 🏢 Built AI tools for VCs, startups, and corporates
- 📝 Writes about AI, Strategy, and compounding systems
- 🚀 Founder of Ainary Ventures (AI-focused fund, wenn public)

---

### 6. Pricing
**Ziel:** Anchoring. Zeigen dass Free-Tier existiert, aber echtes Business dahinter steht.

| Tier | Price | Best For | Limits |
|------|-------|----------|--------|
| **Free** | $0 | Exploration | 1 report/month, public data only |
| **Pro** | $49/mo | Founders, Analysts | 10 reports/month, priority support |
| **Enterprise** | $499/mo | Teams | Unlimited, custom integrations, white-label |
| **Custom** | Contact | Consultancies, Funds | Full API access, dedicated support |

**Notes:**
- Preise sind **PLACEHOLDER** — Florian finalisiert am 13.02.
- Button: "Coming Soon" für Pro/Enterprise, "Contact" für Custom

---

### 7. Footer
**Links:**
- Tools: Corporate X-Ray | Startup X-Ray | Advisory Board | Research | Feed
- Company: About | Pricing | Blog | Contact
- Legal: Privacy Policy | Terms of Service | Imprint (DE required)
- Social: Twitter | LinkedIn | Substack | GitHub

**Copyright:** "© 2026 Florian Ziesche. Built with AI, not consultants."

---

## 🔧 Technical Implementation

### File Structure
```
projects/platform-website/
├── CONCEPT.md          (dieses Dokument)
├── index.html          (single file, production-ready)
└── assets/             (optional, für spätere Iteration)
    ├── logo.svg
    └── icons/
```

### HTML/CSS/JS Guidelines
1. **Single File:** Alles in `index.html` (inline CSS/JS)
2. **Pure HTML:** Keine Frameworks (React/Vue/Svelte)
3. **Modern CSS:** Flexbox, Grid, Custom Properties (`:root`)
4. **Vanilla JS:** Smooth scroll, modal handling, form validation
5. **Performance:** Lazy-load images (wenn welche existieren), kritisches CSS inline
6. **Accessibility:** Semantic HTML, ARIA labels, keyboard navigation

### CSS Variables (Design Tokens)
```css
:root {
  /* Colors */
  --bg-primary: #0a0a0f;
  --bg-card: #12121a;
  --text-primary: #f5f5f7;
  --text-secondary: #a0a0aa;
  
  /* Accents */
  --accent-indigo: #6366f1;
  --accent-purple: #8b5cf6;
  --accent-pink: #ec4899;
  --accent-gold: #f59e0b;
  --accent-emerald: #10b981;
  
  /* Gradient */
  --gradient-platform: linear-gradient(135deg, #6366f1, #8b5cf6, #ec4899, #f59e0b, #10b981);
  
  /* Glassmorphism */
  --glass-bg: rgba(18, 18, 26, 0.7);
  --glass-border: rgba(255, 255, 255, 0.1);
  --glass-blur: 16px;
  
  /* Typography */
  --font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
  
  /* Spacing */
  --spacing-xs: 0.5rem;
  --spacing-sm: 1rem;
  --spacing-md: 1.5rem;
  --spacing-lg: 2rem;
  --spacing-xl: 3rem;
  --spacing-2xl: 4rem;
  
  /* Breakpoints (for media queries) */
  --breakpoint-sm: 640px;
  --breakpoint-md: 768px;
  --breakpoint-lg: 1024px;
  --breakpoint-xl: 1280px;
}
```

### Responsive Breakpoints
- **Mobile:** < 640px (1 column)
- **Tablet:** 640px - 1024px (2 columns)
- **Desktop:** 1024px+ (3 columns, 2 for 5-card grid)
- **Large Desktop:** 1280px+ (optimal spacing)

### JavaScript Features
1. **Smooth Scroll:** Anchors zu Sections (Hero → Grid → Pricing)
2. **Modal:** Email capture popup (ESC to close, click outside to close)
3. **Form Validation:** Email format check
4. **Badge Logic:** "Live" / "Beta" / "Coming Soon" basierend auf Status
5. **Animations:** Fade-in on scroll (Intersection Observer)

---

## 🚀 GTM Integration

### Launch-Strategie (16.02.2026)
1. **Domain:** `tools.florianziesche.com` ODER `florianziesche.com/tools` (Florian entscheidet)
2. **LinkedIn Post:** "I built AI tools that replace $200K consultants. Here's the platform."
3. **Substack:** Long-form "Why I'm Building This" + Platform Link
4. **Twitter Thread:** 5 Tools, 5 Tweets, ending mit Platform Link
5. **Direct Outreach:** 5 Consultancies + 5 VCs bekommen personalized Email + Link

### Analytics (Tag nach Launch)
- Google Analytics 4 (oder Plausible, privacy-friendly)
- Track: Page views, CTA clicks, Email signups, Tool interest breakdown
- Goal: 100 Email signups in Woche 1

### SEO (Woche 2+)
- **Title:** "AI Tools That Replace $200K Consultants | Florian Ziesche"
- **Meta Description:** "Strategic Intelligence in minutes. Corporate X-Ray, Startup X-Ray, AI Advisory Board, and more. Built by Florian Ziesche."
- **Keywords:** AI strategy tools, McKinsey alternative, VC due diligence, AI consulting

---

## 📋 Success Metrics

**Week 1 (Launch):**
- [ ] 100+ unique visitors
- [ ] 50+ email signups
- [ ] 10+ Corporate X-Ray reports generated
- [ ] 1+ LinkedIn post with >5K impressions

**Month 1:**
- [ ] 500+ email subscribers
- [ ] 100+ reports generated
- [ ] 5+ consultancy/VC inbound inquiries
- [ ] 1+ paid Pro subscription

**Quarter 1:**
- [ ] 2,000+ subscribers
- [ ] $5K+ MRR (Pro + Enterprise)
- [ ] 3/5 tools live (Corporate, Startup, Advisory Board)
- [ ] Product Hunt launch

---

## 🧠 Strategic Rationale

### Why Platform > Separate Tools?
1. **Cross-Selling:** X-Ray user → Advisory Board user (1 audience, 5 products)
2. **Branding:** "Florian Ziesche builds AI Strategy Tools" (singular narrative)
3. **Data Moat:** Shared data layer (RSS, Research, Papers) compounds value
4. **Distribution:** 1 audience = 5x leverage per post/article
5. **Exit Optionality:** Platform > Tool (acquirer buys ecosystem, not feature)

### Why "Replace Consultants" Positioning?
1. **Provocative:** Gets attention, stirs debate
2. **True:** McKinsey charges $200K+ for what GPT-4 can do in 5 min (with right prompts)
3. **Relatable:** Every CEO has paid a consultant and regretted it
4. **Aspirational:** You're not just using a tool, you're joining a movement

### Risk: "Too Early for Platform"?
- **Mitigation:** Platform is 1-day build. If it doesn't resonate, we kill it and keep tools separate.
- **Upside:** If it DOES resonate, we're 6 months ahead of competitors.

---

## 🔮 Roadmap

| Phase | Timeline | Goal |
|-------|----------|------|
| **Phase 1: Launch** | Feb 16 '26 | Platform live, 2 tools (Corporate, Startup) |
| **Phase 2: Validate** | Feb-Mar '26 | 100+ signups, 10+ reports/week |
| **Phase 3: Monetize** | Mar-Apr '26 | Pro tier live, first paid users |
| **Phase 4: Scale** | Apr-Jun '26 | 3 more tools (Advisory, Research, Feed) |
| **Phase 5: Expand** | Q3 '26 | API access, white-label, partnerships |

---

## 🎯 Open Questions (für Florian)

1. **Domain:** `tools.florianziesche.com` vs `florianziesche.com/tools` vs eigene Domain?
2. **Branding:** "Florian Ziesche" vs "Ainary Tools" vs neuer Name?
3. **Pricing:** Sind $49 / $499 die richtigen Anchors? (finalisiert am 13.02.)
4. **Social Proof:** Gibt es Logos/Testimonials die wir schon nutzen können?
5. **Email Backend:** n8n webhook vs Mailchimp vs ConvertKit vs Custom?
6. **Analytics:** Google Analytics vs Plausible vs Custom tracking?

---

*Nächster Step: `index.html` produktionsreif bauen.*
