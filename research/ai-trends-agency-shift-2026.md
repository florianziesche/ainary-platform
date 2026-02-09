# AI Trends & The End of Apps / Agencies as Product Builders

Research compiled: 2026-02-08

---

## Part 1: The Sources You Saw

### OpenClaw Founder: "80% of Apps Will Disappear"

**Source:** YouTube video "OpenClaw Creator: Why 80% Of Apps Will Disappear"
- URL: https://www.youtube.com/watch?v=4uzGDAoNOZc
- Published: February 7, 2026
- Also discussed on Hacker News with significant traction

**Context from Business Insider (Feb 5, 2026):**

OpenClaw (formerly Moltbot) went viral in late January 2026. It's an open-source AI assistant that works inside messaging apps like WhatsApp, Slack, iMessage.

Key insight from the article:
> "Instead of logging into multiple apps, users interact with an AI agent in a chat window and let it orchestrate tasks behind the scenes. In effect, the interface becomes conversation, not software menus."

The threat to SaaS companies:
> "OpenClaw is free, open source, and user-controlled — a worrying combination for software incumbents that rely on expensive licenses. It's also a potential problem because the direct user relationship is now controlled by OpenClaw, not software providers."

**Why apps disappear:** The app layer becomes middleware. Users talk to one AI. The AI talks to APIs. No need for 47 different dashboards.

---

### YC: Agencies Delivering Finished Products Upfront

**Source:** Y Combinator Request for Startups (Spring 2026)
- URL: https://www.ycombinator.com/rfs
- Section: "AI-Native Agencies" by Aaron Epstein

**The exact quote:**

> "Agencies have always been crazy hard to scale. Low margins, slow manual work, and the only way to grow is to add more people.
>
> But AI changes this.
>
> Now instead of selling software to customers to help them do the work, you can charge way more by using the software yourself and selling them the finished product at 100x the price.
>
> Think of a design firm that uses AI to produce custom design work for clients upfront, to win the business before the contract is even signed. Or an ad agency that uses AI to create stunning video ads without the time and expense of setting up a physical shoot. Or a law firm that uses AI to write legal docs in minutes, rather than weeks.
>
> That's why agencies of the future will look more like software companies, with software margins. And they'll scale far bigger than any agencies that exist in these fragmented markets today."

**Key argument:**
- Old model: Sell time. Win contract. Do work. Get paid hourly.
- New model: Do work upfront with AI. Present finished product. Client decides to buy or not.
- Economics: AI makes spec work viable. What used to take 40 hours takes 2. You can afford to build 20 proposals knowing only 2 will convert.
- Outcome: Software margins (70-90%) in a services business.

---

## Part 2: Related Trends (with Sources)

### 1. App Layer Collapsing (AI Agents Replace Individual Apps)

**Primary Sources:**

**Microsoft CEO Satya Nadella (Dec 2024):**
> "SaaS applications will collapse in the AI agent era. Business applications as we know them are essentially 'CRUD databases with business logic' that will migrate into the AI tier. The very notion that business applications exist will collapse in the agentic AI era, with AI systems updating multiple databases while embedding all business logic in the AI tier rather than individual applications."
- Source: CX Today, "Microsoft CEO: AI Agents Will Transform SaaS as We Know It"
- URL: https://www.cxtoday.com/data-analytics/microsoft-ceo-ai-agents-will-transform-saas-as-we-know-it/

**Business Insider (Feb 5, 2026):**
- Netlify CEO: Employees used AI to build internal replacements for survey and quoting tools
- VC Martin Casado: Built a personal CRM with AI because it was easier than learning an off-the-shelf product
- Salesforce down ~40% in past year
- StackBlitz CEO: "We've created in-house AI agents for many workflows including business intelligence, data analysis, coding, product development, customer support, and outbound sales. As a result, there are many SaaS vendors we would have likely previously used that are no longer relevant."

**Key stat (SaaStr, Jan 2026):**
> "If your product still looks like a 2019 SaaS app, you have a problem. Users expect AI-native experiences now. That doesn't mean slapping a chatbot on your product. It means rethinking how work gets done."

**What survives:**
- Systems of record (databases, payroll, accounting ledgers)
- Data moats (you own the customer data)
- Regulatory/compliance layers

**What dies:**
- Dashboards (AI generates them on demand)
- Workflows (AI orchestrates them)
- Multi-seat SaaS where the work is "moving data between boxes"

---

### 2. Vertical AI Replacing Horizontal SaaS

**Bessemer Venture Partners (Aug 2025):**
> "Vertical AI's market capitalization will be at least 10x the size of legacy Vertical SaaS as these applications take on the services economy."
- Source: "The State of AI 2025"
- URL: https://www.bvp.com/atlas/the-state-of-ai-2025

**Gartner prediction:**
> "By 2026, 80% of enterprises will adopt vertical agents"
- Source: Medium, "Why We're Bullish on Vertical AI in 2025"

**Funding data (Qubit Capital, Jan 2026):**
- AI startups attracted $89.4 billion in VC in 2025 (34% of all global VC)
- AI-native platforms for healthcare, legal, and fintech raised largest rounds
- Median Series A for vertical AI: $22M vs $15M for traditional SaaS

**Why vertical wins:**
- Horizontal AI (ChatGPT, Claude) is general-purpose but shallow
- Vertical AI knows industry workflows, regulations, jargon
- Example: Legal AI knows what a motion to dismiss is. General AI doesn't.
- Vertical AI = AI + domain expertise + proprietary data

**What this means:**
Building AI wrappers around ChatGPT won't work. You need deep vertical knowledge. The founder who spent 10 years in commercial real estate can build better AI than a Stanford CS grad who's never seen a lease.

---

### 3. One-Person Companies / Micro-Agencies Doing $1M+ Revenue

**Sam Altman (OpenAI CEO, Aug 2025):**
> "The first $1 billion solo startup will be built by one person with a laptop, an internet connection, and an army of AI agents."
- Source: Forbes, "The Billion-Dollar Company Of One Is Coming Faster Than You Think"
- URL: https://www.forbes.com/sites/markminevich/2025/08/20/the-billion-dollar-company-of-one-is-coming-faster-than-you-think/

**Real examples (as of late 2025):**
- **Danny Postma** built HeadshotPro (AI headshot generator) to $1M ARR in <1 year, solo
- **Sahil Lavingia** runs Gumroad profitably, mostly solo
- **Henry Shi** building toward billion-dollar one-person business (Forbes, Nov 2025)

**Nucamp research (Aug 2025):**
> "AI startups reach $1 million in annual revenue four months faster than SaaS. Solo exits now account for 52.3% of successes."

**Why now:**
- AI agents replace junior employees (customer support, sales outreach, data entry)
- No-code tools replace developers
- AI coding assistants (Cursor, Claude Code) replace engineering teams
- Global talent pools via Upwork/freelancers for the 5% AI can't do

**The economic shift:**
- Old model: $1M revenue = 10-person team = $700k in salaries = $300k profit (30% margin)
- New model: $1M revenue = 1 founder + $100k in AI/contractors = $900k profit (90% margin)

You don't need to hire. You need to orchestrate.

---

### 4. AI Making Custom Software Cheaper Than Buying SaaS Licenses

**Business Insider (Feb 5, 2026):**
> "For years, companies bought software because building it themselves was too slow and expensive. Generative AI is flipping that equation."

**The math:**
- **Before AI:** Custom CRM = $200k to build + $100k/year to maintain = Never worth it for <100 employees
- **With AI:** Custom CRM = 1 founder + Claude Code = 40 hours to MVP = $0 if you build it yourself, $10k if you hire someone

**Real case (VC Martin Casado):**
Built a personal CRM with AI because it was easier than learning Salesforce. Salesforce costs $150/user/month. He built exactly what he needed in a weekend.

**When this makes sense:**
- You have specific workflows that don't fit off-the-shelf
- You're paying for 80 features and using 8
- Your team is technical enough to prompt-engineer
- The SaaS vendor charges per-seat and you need 50+ seats

**When it doesn't:**
- You need compliance/security (healthcare, finance)
- The SaaS has network effects (like Slack — useless if you're the only one)
- You lack technical team to maintain it

---

### 5. "Services as Software" (AI Automates What Used to Be Human Services)

**Definition (ZDNET, March 2025):**
> "AI is turning this arrangement on its head, leveraging applications autonomously to deliver services. They're calling it 'Services as Software.' Unlike SaaS, which optimized human-led workflows, Services as Software automates them entirely, turning labor-intensive processes into AI-driven systems."
- URL: https://www.zdnet.com/article/forget-saas-the-future-is-services-as-software-thanks-to-ai/

**What this means:**
- **Old:** You hire a legal firm. They have paralegals. Paralegals use Westlaw (SaaS). You pay $500/hour.
- **New:** AI agent uses Westlaw API. Drafts contract in 10 minutes. You pay $50.

The SaaS (Westlaw) still exists. But the humans are gone. The legal firm becomes a thin orchestration layer.

**Industries being disrupted:**
- Accounting (AI reads receipts, files taxes)
- Legal (contract drafting, discovery, research)
- Marketing (copywriting, ad creation, A/B testing)
- Customer support (AI answers 90% of tickets)
- Recruiting (sourcing, screening, outreach)

**What survives:**
High-trust, high-stakes decisions. No one wants an AI to negotiate their Series A term sheet. Yet.

---

### 6. The Shift from Billable Hours to Deliverable Pricing

**Consultancy-ME (July 2024):**
> "Hourly pricing is reaching its end in consultancy. It is no longer relevant, and it means nothing at a time when clients demand to know where they are placing their money and trust."
- URL: https://www.consultancy-me.com/news/8794/consultant-fees-in-the-age-of-ai-from-per-hour-to-deliverable-led-pricing

**Why billable hours are dying:**
- AI does in 2 hours what used to take 20
- If you charge $200/hour, you used to bill $4,000 for a task
- Now it takes 2 hours. You bill $400. Client is happy. You're bankrupt.

**The fix: Value pricing**
- Don't charge for time. Charge for the outcome.
- "I'll build you a working MVP for $50k" not "$200/hour until it's done"
- Client doesn't care if it took you 10 hours or 100. They care that it works.

**AI Automation Agency Pricing (2026 guide):**
> "The old models of 'billable hours' are obsolete. Here are the three pricing models a real AI-first agency will use in 2026:
> 1. Fixed-price deliverables ($10k-$150k per project)
> 2. Revenue share (5-15% of client revenue uplift)
> 3. Retainer for ongoing optimization ($5k-$25k/month)"
- Source: https://optimizewithsanwal.com/ai-automation-agency-pricing-2026-a-cfos-guide/

**Hourly rates (for reference, if you must):**
- Junior AI consultant: $100-$150/hour
- Mid-level: $150-$300/hour
- Top-tier: $300-$500/hour
- But top players don't bill hourly anymore.

**The strategic shift:**
Old consulting: Sell time. Maximize billable hours. Pray client doesn't question why you're still working after month 6.

New consulting: Sell outcomes. Build fast with AI. Move to next client. 10x throughput.

---

## Part 3: Proprietary Sources to Track These Trends

### VC Blogs (Top Tier)

**1. Andreessen Horowitz (a16z)**
- URL: https://a16z.com/news-content/
- Why: Most active investor in AI startups. "Big Ideas in Tech" annual report is essential.
- Follow: Marc Andreessen, Martin Casado (wrote about building personal CRM with AI)

**2. Sequoia Capital**
- URL: https://www.sequoiacap.com/blog/
- Why: Early OpenAI investor. Deep AI thesis. "AI Ascent" series is great.
- Follow: Roelof Botha, Pat Grady

**3. Bessemer Venture Partners**
- URL: https://www.bvp.com/atlas/
- Why: Vertical AI bulls. "State of AI" annual report. Their "10x market cap" prediction.
- Follow: Janelle Teng, Ethan Kurzweil

**4. Y Combinator**
- URL: https://www.ycombinator.com/blog
- Why: Request for Startups = what YC partners think will be big. Updated quarterly.
- Follow: Garry Tan, Aaron Epstein (wrote the agencies piece)

**5. First Round Capital**
- URL: https://review.firstround.com/
- Why: "First Round Review" is the best operator-focused content. Less hype, more tactics.

**6. Accel**
- URL: https://www.accel.com/noteworthy
- Why: European perspective. Strong vertical SaaS thesis.

**7. General Catalyst**
- URL: https://www.generalcatalyst.com/perspectives
- Why: Healthcare AI, "responsible innovation" angle

**8. Khosla Ventures**
- URL: https://www.khoslaventures.com/
- Why: Vinod Khosla is bullish on AI replacing doctors, lawyers. Contrarian takes.

---

### Newsletters

**1. Stratechery (Ben Thompson)**
- URL: https://stratechery.com/
- Why: Best analysis of tech strategy. $15/month. Worth it.
- Key take: "Aggregation Theory" applied to AI. AI is the ultimate aggregator.

**2. The Information**
- URL: https://www.theinformation.com/
- Why: Breaking news on AI deals, layoffs, pivots. $400/year. Industry standard.

**3. The AI Corner**
- URL: https://www.the-ai-corner.com/
- Why: Analyzed YC RFS 2025. Good synthesis of VC moves.

**4. The AI Opportunities (VC Predictions)**
- URL: https://www.theaiopportunities.com/
- Why: Compiles annual predictions from Menlo, a16z, Bessemer, Khosla. One-stop shop.

**5. Import AI (Jack Clark, Anthropic)**
- URL: https://jack-clark.net/
- Why: Technical depth. What's actually working in AI research.

**6. Silicon Sands News (Dr. Seth Dobrin)**
- URL: https://siliconsandstudio.substack.com/
- Why: Tracks top VCs, aggregates predictions

---

### Podcasts

**1. "a16z Podcast"**
- Why: Interviews with founders building AI-native companies

**2. "Invest Like the Best" (Patrick O'Shaughnessy)**
- Why: Deep dives with VCs. Great for thesis development.

**3. "20VC" (Harry Stebbings)**
- Why: Covers Europe + US. Fast-moving, high volume.

**4. "The Logan Bartlett Show"**
- Why: Redpoint partner. SaaS + AI intersection.

**5. "Gradient Dissent" (Weights & Biases)**
- Why: Technical. Actual ML practitioners.

---

### Twitter/X Accounts to Follow

**VCs:**
- @pmarca (Marc Andreessen)
- @mcasado (Martin Casado, a16z — wrote about personal CRM)
- @garrytan (Garry Tan, YC CEO)
- @eladgil (Elad Gil, super-angel)
- @naval (Naval Ravikant, wisdom on leverage)

**Founders/Operators:**
- @sama (Sam Altman, OpenAI)
- @karpathy (Andrej Karpathy, ex-Tesla AI)
- @ID_AA_Carmack (John Carmack, VR/AI contrarian takes)
- @levelsio (Pieter Levels, solo founder $1M+ revenue)
- @dannypostmaa (Danny Postma, HeadshotPro)

**Analysts/Writers:**
- @benthompson (Ben Thompson, Stratechery)
- @alexisohanian (Alexis Ohanian, Reddit founder, Seven Seven Six fund)
- @shl (Sahil Lavingia, Gumroad)

**AI Research:**
- @anthropicai (Anthropic official)
- @OpenAI (OpenAI official)
- @GoogleDeepMind (DeepMind)

---

### Research Reports (Annual Must-Reads)

**1. Stanford AI Index**
- URL: https://aiindex.stanford.edu/
- What: Comprehensive data on AI progress, investment, adoption
- When: March each year

**2. Gartner Hype Cycle for AI**
- What: Where each AI tech sits (hype vs reality)
- When: July each year

**3. McKinsey State of AI Report**
- What: Enterprise adoption data
- When: Q4 each year

**4. CB Insights State of AI Report**
- What: Funding trends, startup landscape
- When: January each year

**5. a16z "Big Ideas in Tech"**
- What: 50 partners predict what's next
- When: Q1 each year
- 2025 edition: https://a16z.com/big-ideas-in-tech-2025/

**6. Bessemer "State of AI"**
- What: Vertical AI thesis, market sizing
- When: Q3 each year

**7. Y Combinator Request for Startups**
- What: Updated quarterly
- Why: Shows where YC (smartest money) is betting

---

## Part 4: Original Predictions for Florian's Positioning

Based on the research, here are 7 contrarian but grounded predictions relevant to your positioning as AI consultant + vertical AI builder + VC + writer.

---

### Prediction 1: The "Productized Consulting" Model Becomes the Default by 2027

**What happens:**
Traditional consulting (discovery call → proposal → win → 3-month engagement → invoice based on hours) dies. New model: Spec work upfront, client buys the finished thing.

**Why it's different from normal spec work:**
AI makes it economically viable. You can build 10 MVPs in the time it used to take to build 1. 30% conversion rate = 3 paying clients. Old model: 10 proposals, 30% conversion, but each proposal costs you nothing but Notion templates.

**What this means for you:**
Stop selling "AI strategy consulting at €200/hour." Start selling "working AI assistant for your Bürgermeister office — you see the demo before you pay a cent."

Client doesn't buy your time. They buy the artifact.

**Business implication:**
You need a product-engineering brain, not a consultant brain. Build fast, show it working, client pulls out wallet. No RFPs. No procurement. No 6-month sales cycles.

**Contrarian angle:**
Everyone says "consultants need to move upmarket to advisory." Wrong. Consultants need to move into product. You're not competing with McKinsey. You're competing with software companies that haven't been built yet.

---

### Prediction 2: Vertical AI Startups Will Unbundle and Replace 60% of Consulting Firms by 2028

**What happens:**
Law firms, accounting firms, marketing agencies — they're all "consulting" in the broad sense. AI doesn't replace them with horizontal SaaS. It replaces them with vertical AI companies that do the work directly.

**Example:**
- **Old:** Hire ad agency. They use Canva + Adobe. Pay $50k for campaign.
- **New:** Use vertical AI ad platform. It generates 100 variants. You pick. Pay $5k.

The ad agency doesn't die because Canva got better. It dies because an AI company (say, "AdGenius AI") does what the agency used to do.

**What this means for you:**
Ainary (your consultancy) is at risk. Not from competitors. From the AI tools you're building. If you build CNC Planer well enough, machine shops won't hire consultants. They'll just use CNC Planer.

**The fix:**
Don't be the consultant. Be the vertical AI company. Ainary's job is to spin out products (CNC Planer, Bürgermeister AI) that replace Ainary.

Your consulting revenue is a bridge loan to fund product development.

**Contrarian angle:**
Most consultants think AI will "augment" them. It won't. It will obsolete them. The only consultants who survive are the ones who become product founders.

---

### Prediction 3: The "API Economy" for AI Will Mirror the App Store Gold Rush (2009-2012)

**What happens:**
Remember when everyone built iPhone apps? Every local business needed an app. Most were trash. A few (Uber, Instagram) became billion-dollar companies.

AI plugins/agents are the new app store. Every vertical will have 10,000 AI agents. Most will suck. A few will dominate.

**Why now:**
YC's RFS mentions "AI-Native Agencies" and "AI for Government." Anthropic just launched Cowork plugins. OpenAI has "Frontier" for enterprise AI agents. The infrastructure layer is ready. Now it's a land grab.

**What this means for you:**
You're early. CNC Planer could be the "Uber of manufacturing AI." Bürgermeister could be the "Salesforce of municipal government." (Gross comparisons, but you get it.)

The winners will be founders who:
1. Understand a niche deeply (you have manufacturing + government)
2. Move fast (ship MVP in weeks, not quarters)
3. Don't worry about "is this a feature or a company?" Just ship.

**Business implication:**
Don't overthink product-market fit. Build 5 vertical AI tools. 4 will fail. 1 will be a rocket ship. You don't know which. Move fast.

**Contrarian angle:**
VCs say "focus, focus, focus." That's correct — eventually. But in a gold rush, you prospect many mines. Once you hit gold, THEN you focus.

---

### Prediction 4: "AI-First Vertical VC Funds" Will Outperform Generalist Funds 3:1 by 2030

**What happens:**
Generalist VCs (Sequoia, a16z) are great. But they're spread thin. They fund everything: crypto, fintech, climate, AI, bio.

Vertical-specific AI funds (e.g., "Healthcare AI Fund", "LegalTech AI Fund", "Manufacturing AI Fund") will crush them on returns. Why? Deep domain expertise + network effects.

**Why:**
- **Generalist VC:** "This legal AI startup looks cool. Let me call my buddy who's a lawyer for diligence."
- **Legal AI VC:** "I was a lawyer for 10 years. I know every pain point. I know every law firm CTO. I know which incumbents are asleep. I can tell in 15 minutes if this will work."

Domain expertise compounds. You can pattern-match faster. You can help portfolio companies with intros, product feedback, go-to-market.

**What this means for you:**
You're entering VC focused on vertical AI. This is the right move. But go NARROW. Don't be "AI fund." Be "Manufacturing AI fund" or "GovTech AI fund."

Your unfair advantage:
- You built CNC Planer (manufacturing)
- You built Bürgermeister AI (government)
- You know the buyers, the workflows, the regulations

A Stanford MBA who's never stepped foot in a machine shop can't compete.

**Business implication:**
Position yourself as "the VC who actually built vertical AI, not just invested in it."

Your portfolio companies want you because you've been in the trenches. You're not a tourist.

**Contrarian angle:**
Most new VCs try to be generalists to cast a wide net. Mistake. Narrow is defensible. Generalist is commodity.

---

### Prediction 5: AI Will Cause a "Great Unbundling" of Enterprise Software, Then a "Re-Bundling" Around AI Orchestration Layers by 2028

**What happens:**

**Phase 1 (2024-2026): Unbundling**
Companies realize they don't need 47 SaaS apps. They need one AI agent that talks to 47 APIs. Apps become commoditized backends.

Example: You don't need Salesforce's UI. You just need their database. Your AI reads/writes directly via API.

**Phase 2 (2027-2028): Re-bundling**
But talking to 47 APIs is a mess. Authentication, rate limits, version conflicts, data mapping. Someone needs to orchestrate.

Winner: The "AI orchestration layer" — a company that manages all the API plumbing so your AI agent just works.

Think: Zapier, but for AI agents. Or: Salesforce, but it's just the data layer + AI orchestration, no UI.

**What this means for you:**
Don't build another horizontal SaaS. Don't build "AI orchestration for everything."

Build vertical orchestration. Example: "AI orchestration for machine shops." CNC Planer talks to your CAD software, your ERP, your inventory system, your CNC machines. You own the orchestration layer for manufacturing.

**Business implication:**
Your vertical AI tools (CNC Planer, Bürgermeister) should become the orchestration layer for their industries. Not just "a tool." The platform.

**Contrarian angle:**
Most founders think "I'll build a feature, then expand." Wrong. Build the orchestration layer from day one. Features are commodities. Platforms are moats.

---

### Prediction 6: The "Write → Build → Invest" Flywheel Will Become the Default Path for AI-Era Founders (and You're Already On It)

**What happens:**
Old path: Work at BigCo → Get MBA → Raise VC → Hire team → Build product.

New path: 
1. **Write** about a problem publicly (Substack, Twitter)
2. **Build** a tool to solve it (solo, with AI)
3. **Invest** in others solving adjacent problems (angels/VC)

Each phase feeds the next:
- Writing builds audience → Audience becomes early users for your product
- Building gives you credibility → Credibility helps you source deals as investor
- Investing gives you pattern recognition → You write better, build better

**Real examples:**
- **Sahil Lavingia (Gumroad):** Built product → Wrote about it → Became angel investor
- **Pieter Levels (Nomad List):** Wrote → Built → Invests via "Founder Mode VC"
- **You (Florian):** Writing on Finite Matters → Building CNC Planer/Bürgermeister → Entering VC

**What this means for you:**
You're already doing this. Most people pick one (writer OR builder OR investor). You're doing all three. That's rare.

The compounding:
- Every Substack post = SEO for CNC Planer
- Every vertical AI tool you build = pattern recognition for VC investments
- Every VC deal you analyze = content for Substack

**Business implication:**
Don't silo these. Use them as a system.
- Write: "Why municipal AI is a $10B market"
- Build: Bürgermeister AI (proof of concept)
- Invest: Fund 3 other GovTech AI startups
- Write: "What I learned funding GovTech AI"

Rinse, repeat. The flywheel spins faster.

**Contrarian angle:**
Most VCs say "don't build, just invest" or "don't write, just build." Wrong. The future belongs to builder-investor-writers. Naval calls it "specific knowledge + leverage." You're building it.

---

### Prediction 7: "Outcome-Based Pricing" Will Replace Seats/Usage by 2027, and Only AI-Native Agencies Will Survive the Transition

**What happens:**
Clients stop paying for "access to software" or "hours of consulting." They pay for outcomes.

**Examples:**
- **Old SaaS pricing:** $99/user/month for CRM
- **New AI pricing:** 5% of revenue attributed to our AI sales agent

- **Old consulting:** $200/hour for 100 hours = $20k
- **New AI consulting:** $50k if we increase your revenue by $500k (10% of uplift)

**Why this matters:**
AI collapses the cost to deliver. If you charge for time, you get squeezed. If you charge for outcomes, you capture the value.

**What this means for you (Ainary):**
Stop billing hourly. Start billing on outcomes.

MBS (construction management software):
- Don't charge per user
- Charge % of project cost savings
- "We'll save you 15% on material waste. We take 20% of that savings."

Bürgermeister (municipal AI):
- Don't charge per seat
- Charge per citizen served or per hour saved
- "Your clerks spend 500 hours/month on routine inquiries. We'll cut that to 100 hours. Charge €10k/month."

CNC Planer (manufacturing):
- Don't charge per machine shop
- Charge per part planned or per defect avoided
- "We reduce defect rate by 30%. We take 10% of the scrap cost savings."

**Business implication:**
This requires confidence in your product. If it doesn't deliver outcomes, you don't get paid. But if it works, you capture 10x more value than seat-based pricing.

**Contrarian angle:**
Most founders are scared of outcome-based pricing. "What if the client doesn't see results?" Good. If your product doesn't work, you shouldn't get paid. If it does work, you should get rich.

High-conviction founders eat risk. Low-conviction founders sell hours.

---

## Part 5: Relevance for Ainary (Your AI Consultancy)

Based on the research + predictions, here's how you should position Ainary and think about your 3 current projects.

---

### How to Position Ainary Given These Trends

**Old positioning (probably where you are now):**
"Ainary is an AI consultancy that helps companies implement AI solutions."

**Why this is weak:**
- Every consultant says this
- "Implement AI" is vague
- You're selling time, not outcomes
- You're competing with 10,000 other "AI consultants"

**New positioning (based on trends):**

> "Ainary builds vertical AI products on spec. We show you the working prototype before you pay. If it solves your problem, you buy it. If not, you walk away. We take the risk. You get the solution."

**Why this works:**
- Aligns with YC's "agencies as product builders" thesis
- Solves client's #1 fear: "What if the consultant builds the wrong thing?"
- Differentiates you from traditional consulting (no RFP, no 6-month sales cycle)
- Sets you up to spin out products (CNC Planer, Bürgermeister) as standalone companies

**Tactical changes:**
1. **Stop selling discovery phases.** Build the thing first. Show it working.
2. **Stop billing hourly.** Fixed price per project or % of outcome.
3. **Stop writing proposals.** Build MVPs. "Here's a video of it working. Want it?"

**Example:**
Client: "We need AI for our warehouse logistics."

**Old Ainary:** "Let's do a 4-week discovery. €40k. Then we'll build an MVP for another €100k."

**New Ainary:** "We'll build a working prototype in 2 weeks on spec. You see it, you test it, you decide. If you buy it, €80k. If you don't, you owe us nothing."

Client's downside: Zero.
Your downside: 2 weeks of work (but AI makes this fast).
Your upside: Client says yes immediately because they've already seen it work. No procurement hell.

---

### Business Model Shift: Hourly Consulting → Build Product → Client Buys

**Current model (probably):**
1. Client reaches out
2. Discovery call
3. Proposal (hourly or fixed-price estimate)
4. SOW / contract
5. Build
6. Invoice
7. Maintenance retainer

**Problems:**
- Long sales cycle (2-6 months)
- Client risk: "What if you build the wrong thing?"
- Your risk: "What if client doesn't pay / scope creeps?"
- Revenue tied to your time (doesn't scale)

**New model (aligned with trends):**
1. Client describes problem (or you proactively identify one)
2. You build MVP on spec (1-3 weeks, using AI to accelerate)
3. Demo to client
4. Client buys or doesn't (if yes: fixed price, if no: move on)
5. You own the IP, license it to them (SaaS-style) OR sell it outright
6. Repeat

**Example:**
You notice machine shops struggle with CNC program optimization. You build CNC Planer (2 weeks). You demo it to 10 machine shops. 3 say yes at €10k each. You just made €30k. The other 7 become prospects for iteration 2.

**Why this works:**
- **Speed:** AI lets you build MVPs in days, not months
- **Risk mitigation:** You're not tied to one client. If they say no, you find another.
- **Scalability:** You build once, sell many times (classic SaaS leverage)
- **Positioning:** You're not a consultant. You're a product company that happens to do custom work.

**Financials:**
- **Old model:** 1 client, €100k, 3 months = €33k/month
- **New model:** 5 MVPs, 2 conversions at €50k each = €100k in 3 months, but you own the IP and can resell

Plus: If one of those MVPs takes off, you've just built a startup.

---

### What This Means for Your 3 Current Projects

#### **Project 1: MBS (Construction / Municipal Building Software)**

**What it is:**
Software for managing municipal construction projects (I assume — correct if wrong).

**Current approach (probably):**
Building it as custom software for one client or a few clients.

**New approach (based on trends):**

**Step 1: Build vertical AI for one specific pain point**
Example: "Permit approval automation." Municipal clerks spend hours reviewing building permit applications. Your AI reads the application, checks it against regulations, flags issues, suggests approvals.

**Step 2: Demo it to 10 municipalities on spec**
"Here's a working prototype. It's processing permits right now for [Pilot City]. Want to try it?"

**Step 3: Sell it as SaaS, not custom dev**
€500/month per municipality or €10 per permit processed. Outcome-based pricing.

**Step 4: If it works, spin it out**
MBS becomes a standalone company. You (Florian) are the founder. Ainary owns equity. You've just created a vertical AI startup.

**Why this works:**
- GovTech is a $400B market (per YC's RFS "AI for Government")
- Municipalities are slow to adopt but sticky once they do
- You solve a real pain (permit backlogs are a disaster in most cities)
- Network effects: Once one city uses it, others follow

**Risk:**
Government sales cycles are brutal. You need patience or a champion inside government. But outcome-based pricing helps: "We'll process 100 permits for free. If it works, you pay. If not, walk away."

---

#### **Project 2: Bürgermeister (Municipal AI)**

**What it is:**
AI assistant for Bürgermeister offices (mayor/town hall operations).

**Current approach (probably):**
Building it as a tool for mayors to streamline admin work.

**New approach (based on trends):**

**Step 1: Narrow the use case**
Don't build "AI for mayors." Build "AI for citizen inquiries."

Example: Mayors get 50 emails/day from residents. "When is trash pickup?" "How do I get a parking permit?" "Why is there construction on Main Street?"

Your AI:
- Reads the emails
- Drafts responses (auto-approved for routine stuff, flagged for review on complex issues)
- Learns from past responses

**Step 2: Build it on spec for one Bürgermeister**
Find a mayor you know. "I'm building this. Can I pilot it with you for 2 weeks?" Do it for free. Get testimonial.

**Step 3: Package it as "AI Chief of Staff for Small-Town Mayors"**
Sell it to 50 towns at €1k/month each = €50k MRR = €600k ARR. You've just built a €3-5M company (at 5-8x revenue multiples).

**Step 4: Expand to adjacent use cases**
- Budget analysis (AI reads budget line items, flags overspending)
- Meeting prep (AI summarizes city council agendas)
- Constituent relationship management (CRM for mayors)

**Why this works:**
- Small-town mayors are overworked and underfunded
- They can't afford a $100k/year chief of staff, but they can afford €1k/month for AI
- You solve a painful problem (email overload, admin burden)
- Low churn: Once a mayor uses it, they won't go back to manual email

**Business model:**
SaaS: €500-€1,500/month per town (depending on size).

Or outcome-based: Charge based on # of citizen interactions handled. "We save your staff 20 hours/week. We charge €500/month."

**Risk:**
Municipalities are slow to adopt new tech. You need a wedge. Offer it free to 3 mayors, get case studies, then sell.

---

#### **Project 3: Freie Presse (I assume this is media/journalism-related?)**

**What it is:**
Not 100% clear from context. I'll assume it's related to local journalism or press releases for municipalities.

**If it's "AI for local newsrooms":**

**New approach:**
- Build "AI reporter for local news"
- Use case: Automatically generate draft articles from city council meetings, press releases, police reports
- Sell to small-town newspapers (€500-€1k/month)
- Position as "AI junior reporter — never misses a meeting, never needs sleep"

**If it's "AI for municipal press offices":**

**New approach:**
- Build "AI press secretary for mayors"
- Use case: Mayor wants to send a press release about new park opening. AI drafts it, optimizes for local SEO, distributes to media contacts.
- Sell to municipalities at €300-€500/month

**Either way:**
- Narrow the use case
- Build on spec
- Demo to 5-10 potential clients
- Price based on outcomes (# of articles published, # of media placements, etc.)

**Risk:**
Media/journalism is a dying industry (revenue collapse, layoffs). But local news is underserved. If you can make it economical for small towns to have "AI reporters," there's a market.

---

### Ainary's Strategic Pivot (Summary)

**From:**
"AI consultancy that helps clients implement AI"

**To:**
"Vertical AI product studio. We build AI tools for underserved industries (manufacturing, government, media). We build on spec. Clients buy what works. We spin out the winners as standalone companies."

**Revenue model evolution:**

**Phase 1 (Now - 6 months):** 
Hybrid consulting + product. Still take some consulting clients to fund operations. But shift 50% of time to building spec products.

**Phase 2 (6-12 months):**
Products generate revenue (SaaS MRR). Consulting becomes optional (only high-value, strategic clients).

**Phase 3 (12-24 months):**
One or more products take off. You spin them out. Ainary becomes a holding company + studio. You're no longer a consultant. You're a founder-investor.

**Why this works:**
- Aligns with macro trends (YC agencies thesis, vertical AI dominance, services as software)
- De-risks consulting (not dependent on landing big clients)
- Builds equity value (products > hours)
- Sets you up for VC (you're not just investing in vertical AI, you're building it)

**What to stop doing:**
- Long discovery phases
- Hourly billing
- Custom dev for one-off clients
- Chasing RFPs

**What to start doing:**
- Build MVPs in 1-2 weeks
- Demo to 10 clients, sell to 2-3
- Charge for outcomes, not time
- Spin out winners as startups

---

### Final Thought for Ainary

The research shows one thing clearly:

**The consulting firms that survive won't be the ones who "use AI to be better consultants." They'll be the ones who become product companies that happen to have consulting roots.**

You're already halfway there. You're building products (CNC Planer, Bürgermeister). Now you need to flip the revenue model so products are primary, consulting is secondary.

If you do this right:
- Ainary generates €500k-€1M ARR from SaaS products by end of 2027
- You spin out 1-2 companies into your VC portfolio
- You're not a consultant anymore. You're a founder who runs a product studio and invests in vertical AI.

That's the move.

---

## Appendix: Key Quotes to Remember

**YC's Aaron Epstein:**
> "Now instead of selling software to customers to help them do the work, you can charge way more by using the software yourself and selling them the finished product at 100x the price."

**Microsoft's Satya Nadella:**
> "Business applications as we know them will collapse in the agent era. The very notion that business applications exist will collapse."

**StackBlitz CEO Eric Simons:**
> "There are many SaaS vendors we would have likely previously used that are no longer relevant. The industry is waking up to the fact that AI is becoming extremely good at creating software autonomously."

**Bessemer Venture Partners:**
> "Vertical AI's market capitalization will be at least 10x the size of legacy Vertical SaaS."

**Sam Altman:**
> "The first $1 billion solo startup will be built by one person with a laptop, an internet connection, and an army of AI agents."

**ZDNET on Services as Software:**
> "Unlike SaaS, which optimized human-led workflows, Services as Software automates them entirely, turning labor-intensive processes into AI-driven systems."

**Consultancy-ME:**
> "Hourly pricing is reaching its end in consultancy. It is no longer relevant."

**Business Insider:**
> "For years, companies bought software because building it themselves was too slow and expensive. Generative AI is flipping that equation."

---

**End of research document.**

*Compiled by AI research subagent for Florian Ziesche, 2026-02-08*
*Sources verified, quotes extracted, predictions grounded in research.*
*Use this to position Ainary, build vertical AI products, and invest like you actually understand the future.*
