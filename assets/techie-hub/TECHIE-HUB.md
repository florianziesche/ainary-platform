# 🚀 The Techie Resource Hub

Your complete guide to AI prompts, tools, and weekend projects.

---

## 📝 Part 1: 50 Super Effective AI Prompts

### Coding Prompts (10)

#### 1. Debug Detective
**Prompt:**
```
I'm getting this error: [paste error message and relevant code]

Please:
1. Identify the root cause
2. Explain why it's happening
3. Provide a fixed version with inline comments
4. Suggest how to prevent similar issues
```

**When to use:** Any time you hit a bug you can't immediately solve  
**Pro tip:** Include the full stack trace and the code context (5-10 lines before/after)

---

#### 2. Refactor for Readability
**Prompt:**
```
Refactor this code for maximum readability and maintainability:

[paste code]

Requirements:
- Keep the same functionality
- Add clear variable names
- Break into smaller functions if needed
- Add comments for complex logic
- Follow [language] best practices
```

**When to use:** When your code works but is messy  
**Pro tip:** Specify your team's style guide (e.g., "Follow Airbnb JavaScript style guide")

---

#### 3. Architecture Review
**Prompt:**
```
I'm building [describe feature/system]. Here's my current approach:

[describe or paste architecture]

Please:
1. Identify potential bottlenecks or scaling issues
2. Suggest alternative patterns if appropriate
3. Point out security concerns
4. Recommend where to add error handling
5. Rate the approach 1-10 with reasoning
```

**When to use:** Before starting a major feature or refactor  
**Pro tip:** Include your scale requirements (users, requests/sec, data volume)

---

#### 4. Code Review Assistant
**Prompt:**
```
Review this code as a senior engineer would:

[paste code]

Focus on:
- Logic errors and edge cases
- Performance issues
- Security vulnerabilities
- Code style and conventions
- Suggestions for improvement

Be direct but constructive.
```

**When to use:** Before submitting a PR or when self-reviewing  
**Pro tip:** Run this on your own code before asking teammates to review

---

#### 5. Test Case Generator
**Prompt:**
```
Generate comprehensive test cases for this function:

[paste function]

Include:
- Happy path tests
- Edge cases
- Error cases
- Mock data examples
- Use [testing framework] syntax
```

**When to use:** When you need to write tests but aren't sure what to cover  
**Pro tip:** Add "Include tests for [specific edge case you're worried about]"

---

#### 6. API Design Consultant
**Prompt:**
```
I need to design an API for [describe purpose].

Requirements:
- [list key requirements]

Please provide:
1. RESTful endpoint structure
2. Request/response examples (JSON)
3. Error handling strategy
4. Authentication approach
5. Rate limiting recommendations
```

**When to use:** Starting a new API or redesigning endpoints  
**Pro tip:** Specify if you need REST, GraphQL, or gRPC

---

#### 7. Performance Optimizer
**Prompt:**
```
This code is too slow: [paste code or describe algorithm]

Context:
- Current performance: [e.g., 5 seconds for 10k items]
- Target: [e.g., under 500ms]
- Constraints: [memory limits, can't change database, etc.]

Please:
1. Identify bottlenecks
2. Suggest optimizations with code examples
3. Estimate improvement for each suggestion
4. Note any trade-offs
```

**When to use:** When performance is noticeably slow  
**Pro tip:** Profile first to confirm the bottleneck before optimizing

---

#### 8. Database Schema Designer
**Prompt:**
```
I'm building [describe application]. Design a database schema for:

Entities:
- [list main entities and key attributes]

Relationships:
- [describe relationships]

Requirements:
- [scale, query patterns, etc.]

Provide:
1. Table schemas (SQL or NoSQL)
2. Indexes needed
3. Relationships/foreign keys
4. Sample queries for common operations
```

**When to use:** Starting a new project or adding major features  
**Pro tip:** Include your expected query patterns (what you'll search for most)

---

#### 9. Documentation Generator
**Prompt:**
```
Generate clear documentation for this code:

[paste code]

Include:
- Overview/purpose
- Parameters with types and descriptions
- Return value
- Usage examples
- Edge cases or gotchas
- Format as [JSDoc/docstring/markdown/etc.]
```

**When to use:** When you need to document existing code  
**Pro tip:** Generate docs, then refine them — it's faster than starting from scratch

---

#### 10. Migration Planner
**Prompt:**
```
I need to migrate from [old tech] to [new tech].

Current system:
- [describe current setup]
- [scale/usage stats]

Target:
- [describe desired end state]

Create a migration plan with:
1. Step-by-step phases
2. Risks and mitigation strategies
3. Rollback plans
4. Testing approach
5. Timeline estimate
```

**When to use:** Before any major technology migration  
**Pro tip:** Include your risk tolerance and whether you can afford downtime

---

### Writing Prompts (10)

#### 11. Blog Post Expander
**Prompt:**
```
Turn this outline into a compelling blog post:

Topic: [topic]
Audience: [who you're writing for]
Tone: [professional/casual/technical/etc.]

Outline:
[paste outline or bullet points]

Requirements:
- 1000-1500 words
- Include examples
- Add a hook in the intro
- End with a clear takeaway
- SEO-friendly structure (H2s, H3s)
```

**When to use:** When you have ideas but need help structuring a full post  
**Pro tip:** Add "Include a personal anecdote in the intro" for more engaging content

---

#### 12. Email Polisher
**Prompt:**
```
Rewrite this email to be [more professional/more casual/more persuasive/more concise]:

Original:
[paste email]

Context:
- Recipient: [who they are, relationship]
- Goal: [what you want to achieve]

Keep the key points but improve clarity and tone.
```

**When to use:** Before sending important emails  
**Pro tip:** Try "Make this 50% shorter without losing key points" for rambling drafts

---

#### 13. Technical Doc Translator
**Prompt:**
```
Explain this technical concept for [non-technical stakeholders/beginners/executives]:

[paste technical explanation or documentation]

Requirements:
- No jargon (or define it when necessary)
- Use analogies where helpful
- Keep it under [X] words
- Maintain accuracy
```

**When to use:** Writing for non-technical audiences  
**Pro tip:** Specify exactly who will read it (e.g., "board members" vs "marketing team")

---

#### 14. Copy That Converts
**Prompt:**
```
Write conversion-focused copy for:

Product/Service: [what you're selling]
Audience: [who you're targeting]
Goal: [sign up/buy/download/etc.]

Include:
- Headline (3 options)
- Subheadline
- 3 bullet points (benefits, not features)
- Call-to-action (2 variations)
- Tone: [urgent/calm/exciting/professional]

Focus on the transformation, not the product.
```

**When to use:** Landing pages, ads, product pages  
**Pro tip:** Add "Address the objection: [common objection]" for stronger copy

---

#### 15. Content Repurposer
**Prompt:**
```
Repurpose this content into:

Original: [paste blog post/article/video transcript]

Create:
1. LinkedIn post (150-200 words)
2. Twitter thread (8-10 tweets)
3. Email newsletter snippet (100 words)
4. Instagram caption (100 words + 5 hashtags)

Maintain core message but adapt tone for each platform.
```

**When to use:** Maximizing reach from a single piece of content  
**Pro tip:** Specify if certain platforms are priority: "Make LinkedIn version the strongest"

---

#### 16. README Builder
**Prompt:**
```
Create a professional README for this project:

Project: [name]
Purpose: [what it does]
Tech stack: [languages/frameworks]
Target users: [who would use this]

Include:
- Clear description
- Installation instructions
- Usage examples
- Configuration options
- Contributing guidelines
- License info
- Screenshots/demo section (describe what to show)
```

**When to use:** Open-source projects or internal tools  
**Pro tip:** Add "Make it beginner-friendly" if targeting new developers

---

#### 17. Meeting Summary Generator
**Prompt:**
```
Summarize these meeting notes:

[paste notes or transcript]

Format:
- Key decisions made
- Action items (who, what, when)
- Open questions
- Next steps
- Keep it under 200 words

Audience: [attendees/broader team/executives]
```

**When to use:** After any meeting with multiple people  
**Pro tip:** Record and transcribe meetings, then use this prompt to save time

---

#### 18. Headline Generator
**Prompt:**
```
Generate 10 headline options for:

Content: [brief description]
Audience: [who will read it]
Goal: [clicks/shares/SEO/etc.]

Styles to try:
- Curiosity-driven
- Benefit-focused
- Numbered list
- Question-based
- Contrarian take

Make them punchy and specific.
```

**When to use:** Blog posts, emails, landing pages  
**Pro tip:** Test top 3 headlines with a small audience before choosing

---

#### 19. Storytelling Structure
**Prompt:**
```
Turn this information into a compelling story:

Facts/Data: [what happened or what you want to convey]

Structure it with:
1. Hook (grab attention immediately)
2. Context (why it matters)
3. Conflict/Challenge (what went wrong or what's at stake)
4. Resolution (how it was solved or what you learned)
5. Takeaway (what the reader should remember)

Tone: [inspirational/cautionary/educational]
Length: [500/1000/1500 words]
```

**When to use:** Case studies, personal essays, company updates  
**Pro tip:** Real stories beat generic advice — include specific details

---

#### 20. Argument Strengthener
**Prompt:**
```
Strengthen this argument:

Claim: [your main point]
Current reasoning: [your supporting points]

Please:
1. Identify weak points in the logic
2. Add supporting evidence or examples
3. Address obvious counter-arguments
4. Restructure for maximum persuasiveness
5. Suggest a stronger conclusion

Make it bulletproof but honest.
```

**When to use:** Proposals, essays, debates, pitch decks  
**Pro tip:** Play devil's advocate first to find your own weak spots

---

### Research Prompts (10)

#### 21. Market Analysis Framework
**Prompt:**
```
Analyze the market for [product/service/industry]:

Please provide:
1. Market size and growth trends
2. Key players and their positioning
3. Customer segments and pain points
4. Emerging trends and disruptions
5. Opportunities and white spaces
6. Threats and challenges
7. Recommended entry strategy

Focus on actionable insights, not just data.
```

**When to use:** Evaluating new markets or business opportunities  
**Pro tip:** Add specific geographic regions or customer segments to narrow focus

---

#### 22. Competitive Intelligence
**Prompt:**
```
Compare these competitors: [list 3-5 companies]

Analyze:
1. Product/service offerings
2. Pricing models
3. Target customers
4. Unique value propositions
5. Strengths and weaknesses
6. Market positioning
7. Recent moves (acquisitions, launches, pivots)

Output: Comparison table + strategic insights
```

**When to use:** Before launching a product or repositioning  
**Pro tip:** Include "What are they NOT doing that we could?" for differentiation ideas

---

#### 23. Research Synthesizer
**Prompt:**
```
I've gathered research on [topic]. Synthesize it into key insights:

Sources:
[paste excerpts, links, or summaries]

Provide:
1. Main themes (3-5)
2. Consensus points (what most sources agree on)
3. Contradictions or debates
4. Gaps in current knowledge
5. Practical implications
6. Recommended next steps for deeper research

Format: Executive summary + detailed breakdown
```

**When to use:** After collecting multiple sources on a topic  
**Pro tip:** Great for literature reviews or internal research projects

---

#### 24. Trend Spotter
**Prompt:**
```
Identify emerging trends in [industry/technology/market]:

Context: [your business or focus area]

Analyze:
1. What's gaining momentum (data, adoption, investment)
2. Why it matters (underlying drivers)
3. Who's leading (companies, people, regions)
4. Timeline (is this 1 year out or 5+ years?)
5. How it could impact [my business/industry]
6. Recommended actions (watch, experiment, invest, ignore)

Focus on signal, not noise.
```

**When to use:** Strategic planning or innovation initiatives  
**Pro tip:** Ask for "contrarian take: what trends are overhyped?" to balance hype

---

#### 25. SWOT Generator
**Prompt:**
```
Create a detailed SWOT analysis for:

Company/Product: [name]
Context: [brief background]

Analyze:
- Strengths (internal advantages)
- Weaknesses (internal disadvantages)
- Opportunities (external positive factors)
- Threats (external negative factors)

For each: Provide 5-7 specific points with explanations.
Add: Strategic recommendations based on the SWOT.
```

**When to use:** Strategic planning sessions or business reviews  
**Pro tip:** Update quarterly to track how your SWOT evolves

---

#### 26. Academic Paper Summarizer
**Prompt:**
```
Summarize this academic paper for a general audience:

[paste title, abstract, or key sections]

Provide:
1. Research question (what they studied)
2. Methodology (how they studied it)
3. Key findings (what they discovered)
4. Limitations (what to be cautious about)
5. Practical implications (so what?)
6. Related research to explore

Keep it under 500 words, no jargon.
```

**When to use:** Reading research papers for work or learning  
**Pro tip:** Add "Explain like I'm a smart 15-year-old" for maximum clarity

---

#### 27. Data Interpreter
**Prompt:**
```
Analyze this data and extract insights:

Data: [paste data, describe dataset, or attach CSV/spreadsheet]

Context: [what this data represents]

Please:
1. Identify key patterns or trends
2. Highlight outliers or anomalies
3. Suggest correlations worth investigating
4. Visualize recommendations (what charts to create)
5. Actionable insights (what to do with this)

Assume I'm not a data scientist.
```

**When to use:** When you have data but aren't sure what it's telling you  
**Pro tip:** Specify your goal: "I want to reduce churn" helps focus the analysis

---

#### 28. Expert Interview Prep
**Prompt:**
```
I'm interviewing [expert name/role] about [topic].

Background: [brief context on why you're talking to them]

Generate:
1. 10 insightful questions (mix open-ended and specific)
2. Potential follow-up questions for each
3. Topics to avoid (if sensitive area)
4. Key things to listen for
5. How to make this valuable for them too

Goal: [what you want to learn or achieve]
```

**When to use:** Before expert interviews, podcasts, or research calls  
**Pro tip:** Send questions in advance to get better, more prepared answers

---

#### 29. Literature Gap Finder
**Prompt:**
```
Based on this research overview, identify gaps in the literature:

Topic: [your research area]
Current research: [summarize what exists]

Find:
1. Questions that haven't been answered
2. Populations or contexts not studied
3. Methodological limitations to address
4. Contradictions that need resolution
5. Emerging areas with little research
6. Practical applications not explored

Suggest 3-5 potential research directions.
```

**When to use:** Academic research or deep industry analysis  
**Pro tip:** Great for finding unique angles for content or business opportunities

---

#### 30. Scenario Planner
**Prompt:**
```
Create scenario planning for [situation/decision/future state]:

Context: [describe the situation]
Timeframe: [1 year/5 years/etc.]
Key uncertainties: [what's unpredictable]

Develop 4 scenarios:
1. Best case (optimistic but plausible)
2. Worst case (pessimistic but plausible)
3. Most likely case
4. Wild card (low probability, high impact)

For each: Describe what happens, leading indicators, and how to respond.
```

**When to use:** Strategic planning under uncertainty  
**Pro tip:** Use this for big decisions (hiring, expansion, product bets)

---

### Business Prompts (10)

#### 31. Pitch Deck Outliner
**Prompt:**
```
Create a pitch deck outline for:

Company: [name]
Product/Service: [description]
Stage: [pre-seed/seed/Series A/etc.]
Asking for: [amount and use of funds]

Generate:
1. Slide-by-slide outline (12-15 slides)
2. Key points for each slide
3. Data/metrics to include
4. Storytelling flow
5. Anticipated questions and answers

Make it investor-ready.
```

**When to use:** Fundraising or major partnership pitches  
**Pro tip:** Tailor to your audience: "VCs focused on B2B SaaS" or "angel investors"

---

#### 32. Business Model Canvas
**Prompt:**
```
Complete a Business Model Canvas for:

Business: [name and description]

Fill out each section:
1. Customer Segments
2. Value Propositions
3. Channels
4. Customer Relationships
5. Revenue Streams
6. Key Resources
7. Key Activities
8. Key Partners
9. Cost Structure

Be specific and realistic. Identify the riskiest assumptions.
```

**When to use:** Starting a business or validating a new product  
**Pro tip:** Update this quarterly as you learn and pivot

---

#### 33. Pricing Strategy Consultant
**Prompt:**
```
Design a pricing strategy for:

Product: [description]
Target customers: [who they are]
Competitors: [how they price]
Costs: [rough COGS or cost structure]

Recommend:
1. Pricing model (subscription/one-time/usage-based/freemium/etc.)
2. Price points with reasoning
3. Tier structure (if applicable)
4. Discount/promotion strategy
5. Pricing psychology tactics to apply
6. How to test and iterate

Goal: [maximize revenue/market share/etc.]
```

**When to use:** Launching a product or repositioning  
**Pro tip:** Test multiple price points with real customers before committing

---

#### 34. Financial Projection Builder
**Prompt:**
```
Create 3-year financial projections for:

Business: [description]
Current state: [revenue, users, stage]
Assumptions: [growth rate, pricing, costs]

Generate:
1. Revenue projections (monthly Year 1, quarterly Year 2-3)
2. Cost breakdown (COGS, OpEx, headcount)
3. Cash flow analysis
4. Key metrics (CAC, LTV, burn rate, runway)
5. Break-even analysis
6. Sensitivity analysis (what if growth is 50% of plan?)

Output: Spreadsheet-ready format
```

**When to use:** Fundraising, strategic planning, board meetings  
**Pro tip:** Build conservative, moderate, and optimistic cases

---

#### 35. Go-to-Market Strategy
**Prompt:**
```
Design a go-to-market strategy for:

Product: [description]
Target market: [ICP - ideal customer profile]
Budget: [available resources]
Timeline: [launch date or timeframe]

Develop:
1. Positioning and messaging
2. Channel strategy (where to reach customers)
3. Launch phases (pre-launch, launch, post-launch)
4. Metrics to track
5. Budget allocation
6. First 90 days action plan
7. Risks and mitigation

Make it actionable.
```

**When to use:** Product launches or entering new markets  
**Pro tip:** Include "What NOT to do" to avoid common mistakes

---

#### 36. Customer Journey Mapper
**Prompt:**
```
Map the customer journey for:

Product/Service: [what you sell]
Customer type: [specific persona]

Map each stage:
1. Awareness (how they discover you)
2. Consideration (how they evaluate)
3. Purchase (what convinces them)
4. Onboarding (first experience)
5. Retention (ongoing value)
6. Advocacy (why they'd refer)

For each: Touchpoints, emotions, pain points, opportunities to improve.
```

**When to use:** Improving conversion or customer experience  
**Pro tip:** Do this for each major customer segment separately

---

#### 37. OKR Framework Builder
**Prompt:**
```
Create OKRs (Objectives and Key Results) for:

Team/Company: [name]
Time period: [Q1 2026, etc.]
Strategic priorities: [top 3-5 priorities]

Generate:
- 3-5 Objectives (ambitious, qualitative goals)
- 3-4 Key Results per Objective (measurable, achievable)
- Confidence level (how likely to achieve)
- Dependencies and risks
- Alignment with company-level goals (if applicable)

Make them SMART and ambitious but realistic.
```

**When to use:** Quarterly planning for teams or companies  
**Pro tip:** Review and score OKRs weekly to stay on track

---

#### 38. Investor Update Template
**Prompt:**
```
Create an investor update for:

Company: [name]
Period: [month/quarter]
Audience: [investors, advisors, board]

Include:
1. Executive summary (3-4 bullets)
2. Key metrics (growth, revenue, users, etc.)
3. Highlights (wins and progress)
4. Lowlights (challenges and how you're addressing them)
5. Learnings
6. Plan for next period
7. Asks (how investors can help)

Tone: Transparent, confident, concise.
Length: ~500 words
```

**When to use:** Monthly or quarterly investor communications  
**Pro tip:** Be honest about challenges — investors respect transparency

---

#### 39. Partnership Proposal
**Prompt:**
```
Draft a partnership proposal for:

Our company: [name and description]
Target partner: [company name]
Partnership type: [integration/co-marketing/reseller/etc.]

Structure:
1. Executive summary (why this makes sense)
2. Mutual benefits (what each side gains)
3. Proposed collaboration model
4. Success metrics
5. Timeline and milestones
6. Next steps

Make it win-win and easy to say yes to.
```

**When to use:** Reaching out to potential partners  
**Pro tip:** Research what they care about and lead with their benefits

---

#### 40. Crisis Communication Plan
**Prompt:**
```
Create a crisis communication plan for:

Scenario: [describe the crisis or potential crisis]
Stakeholders: [customers, employees, investors, public]

Develop:
1. Immediate response (first 24 hours)
2. Key messages for each stakeholder group
3. Communication channels to use
4. Spokesperson and chain of command
5. FAQ for common questions
6. Long-term reputation recovery plan
7. Preventive measures for future

Tone: [apologetic/factual/reassuring - depends on situation]
```

**When to use:** Preparing for potential crises or responding to one  
**Pro tip:** Have this ready BEFORE you need it

---

### Productivity Prompts (10)

#### 41. Weekly Planner
**Prompt:**
```
Plan my week based on these priorities:

Top goals for the week:
- [goal 1]
- [goal 2]
- [goal 3]

Fixed commitments:
- [meetings, appointments]

Work hours available: [X hours]

Create:
1. Day-by-day schedule (what to focus on each day)
2. Time blocks for deep work
3. Buffer time for unexpected issues
4. Energy-based task allocation (high-energy tasks when I'm sharpest)
5. What NOT to do this week

Format: Calendar-ready time blocks
```

**When to use:** Sunday evening or Monday morning planning  
**Pro tip:** Theme your days (Monday = strategy, Tuesday = creation, etc.)

---

#### 42. Decision Framework
**Prompt:**
```
Help me decide: [describe the decision]

Options:
1. [option 1]
2. [option 2]
3. [option 3]

Criteria that matter to me:
- [criterion 1, e.g., cost]
- [criterion 2, e.g., time]
- [criterion 3, e.g., impact]

Provide:
1. Weighted scoring matrix
2. Pros/cons for each option
3. Second-order consequences
4. What you'd choose and why
5. How to test/validate before committing

Be honest if more info is needed.
```

**When to use:** Any significant decision (hiring, tools, strategy)  
**Pro tip:** Add "What would I regret NOT choosing?" for clarity

---

#### 43. Learning Plan Builder
**Prompt:**
```
Create a learning plan for:

Skill/Topic: [what you want to learn]
Current level: [beginner/intermediate/advanced]
Goal: [what you want to achieve]
Time available: [hours per week]
Timeline: [how long you have]

Design:
1. Learning path (topics in order)
2. Resources for each topic (courses, books, tutorials)
3. Practice projects to build
4. Milestones to track progress
5. Weekly time allocation
6. How to know you've "learned it"

Make it actionable and realistic.
```

**When to use:** Learning a new skill systematically  
**Pro tip:** Block time on your calendar NOW or it won't happen

---

#### 44. Meeting Optimizer
**Prompt:**
```
Optimize this recurring meeting:

Meeting: [name and purpose]
Attendees: [who comes]
Current format: [how it runs now]
Duration: [how long it takes]

Problems:
- [what's not working]

Redesign:
1. Whether it should exist (could it be async?)
2. Right attendees (who's optional?)
3. Optimal frequency and duration
4. Agenda template
5. Pre-work to assign
6. How to make decisions faster
7. Follow-up process

Make meetings suck less.
```

**When to use:** When meetings feel unproductive  
**Pro tip:** Try "No meeting Wednesdays" for deep work time

---

#### 45. Delegation Script
**Prompt:**
```
Help me delegate this task:

Task: [what needs to be done]
Delegating to: [person's role/skill level]
Context they need: [background info]

Create:
1. Clear task description
2. Success criteria (what "done" looks like)
3. Deadline and milestones
4. Resources/access they'll need
5. Decision-making authority (what they can decide vs. escalate)
6. Check-in schedule
7. How I'll provide feedback

Make it clear enough that I don't get asked 20 questions.
```

**When to use:** Delegating to team members or contractors  
**Pro tip:** Over-communicate context the first time, then create a template

---

#### 46. Email Inbox Zero Strategy
**Prompt:**
```
Design an email management system for:

Current situation:
- Inbox size: [number of emails]
- Daily volume: [emails per day]
- Types: [client emails, newsletters, notifications, etc.]

Create:
1. Folder/label structure
2. Filter rules to automate
3. Daily email routine (when and how to process)
4. Templates for common replies
5. Unsubscribe strategy
6. What to delegate or forward
7. 30-day plan to reach inbox zero

Goal: Spend <30 minutes/day on email.
```

**When to use:** When email is overwhelming  
**Pro tip:** Unsubscribe aggressively — if you haven't read it in 3 months, you won't

---

#### 47. Focus Session Designer
**Prompt:**
```
Design a deep work session for:

Task: [what you need to focus on]
Duration: [how long you have]
Distractions: [what usually interrupts you]

Create:
1. Pre-session prep (5 min)
2. Environment setup (minimize distractions)
3. Session structure (Pomodoros or time blocks)
4. Break activities
5. Tools/resources to have ready
6. How to handle interruptions
7. Post-session review (what to capture)

Make it so easy I can't say no.
```

**When to use:** Before tackling hard, important work  
**Pro tip:** Put phone in another room and use website blockers

---

#### 48. Energy Audit
**Prompt:**
```
Help me audit my energy levels:

Typical day:
- [describe your schedule]

Things that drain my energy:
- [list activities/people/situations]

Things that boost my energy:
- [list activities/people/situations]

Analyze:
1. Energy patterns (when am I sharpest?)
2. Energy drains to minimize
3. Energy boosts to add
4. Task-energy matching (do hard things when energized)
5. Recovery strategies
6. Weekly rhythm redesign

Goal: More energy, better work, less burnout.
```

**When to use:** Feeling burnt out or unproductive  
**Pro tip:** Track energy for a week before making changes

---

#### 49. Habit Stacker
**Prompt:**
```
Help me build this habit:

Habit: [what you want to do regularly]
Current situation: [how often you do it now]
Goal: [desired frequency]
Obstacles: [what gets in the way]

Design:
1. Trigger (what will remind you)
2. Routine (exact steps, make it tiny)
3. Reward (what you get immediately)
4. Stack with existing habit (After [X], I will [Y])
5. Environment design (make it easy)
6. Tracking method
7. 30-day implementation plan

Make it so small I can't fail.
```

**When to use:** Building new habits or breaking old ones  
**Pro tip:** Start absurdly small (1 push-up, 2 min meditation) then build up

---

#### 50. Reflection Framework
**Prompt:**
```
Guide me through a reflection on:

Period: [week/month/quarter/year]
Focus area: [work/life/specific project]

Prompts:
1. What went well? (celebrate wins)
2. What didn't go as planned? (be honest)
3. What did I learn?
4. What surprised me?
5. What would I do differently?
6. What am I grateful for?
7. What's one thing to improve next period?
8. What's one thing to keep doing?

Help me extract lessons and set direction.
```

**When to use:** Weekly reviews, monthly retrospectives, annual planning  
**Pro tip:** Schedule this as a recurring event or you'll skip it

---

---

## 🛠️ Part 2: Ultimate AI Stack 2026 (40 Tools)

### Large Language Models (LLMs)

#### 1. Claude (Anthropic)
**What it does:** Advanced reasoning, coding, analysis, and long-context understanding (200K tokens)  
**Pricing:** 
- Claude 3.5 Sonnet: $3/MTok input, $15/MTok output
- Claude Opus: $15/MTok input, $75/MTok output  
**Best for:** Complex reasoning, code generation, working with large documents, safety-critical applications

#### 2. GPT-4 / GPT-4 Turbo (OpenAI)
**What it does:** General-purpose AI with strong multimodal capabilities (text + vision)  
**Pricing:**
- GPT-4 Turbo: $10/MTok input, $30/MTok output
- GPT-4o: $2.50/MTok input, $10/MTok output  
**Best for:** Versatile tasks, vision+text, fast iteration, broad knowledge base

#### 3. Gemini (Google)
**What it does:** Multimodal LLM with deep Google Search integration  
**Pricing:**
- Gemini 1.5 Pro: $1.25/MTok input, $5/MTok output
- Gemini 1.5 Flash: $0.075/MTok input, $0.30/MTok output  
**Best for:** Research, multimodal tasks, real-time information, free tier experimentation

#### 4. Llama 3 (Meta)
**What it does:** Open-source LLM you can run locally or on your own infrastructure  
**Pricing:** Free (open-source), but you pay for compute  
**Best for:** Privacy-sensitive work, custom fine-tuning, cost control at scale, learning AI internals

#### 5. Mistral (Mistral AI)
**What it does:** European open-source LLM with strong multilingual performance  
**Pricing:**
- Mistral Large: €3/MTok input, €9/MTok output
- Mistral Small: €0.2/MTok input, €0.6/MTok output
- Open models: Free  
**Best for:** European data compliance, multilingual tasks, cost-effective API alternative

---

### AI Coding Assistants

#### 6. Cursor
**What it does:** AI-first code editor (VS Code fork) with context-aware pair programming  
**Pricing:** $20/month Pro plan  
**Best for:** Full projects, refactoring, context-heavy coding, "build this feature" level assistance

#### 7. GitHub Copilot
**What it does:** AI pair programmer that suggests code as you type  
**Pricing:** $10/month individual, $19/month business  
**Best for:** Autocomplete++, boilerplate generation, learning new frameworks, working in VS Code/JetBrains

#### 8. Claude Code (Anthropic)
**What it does:** CLI tool for AI-assisted development with full workspace context  
**Pricing:** Uses Claude API credits  
**Best for:** Terminal-based workflows, scripting, automation, DevOps tasks

#### 9. Windsurf (Codeium)
**What it does:** AI code editor with multi-file editing and "Flows" for complex refactors  
**Pricing:** Free tier available, Pro $10/month  
**Best for:** Large refactors across multiple files, working with legacy code

#### 10. Replit AI
**What it does:** Cloud IDE with AI pair programmer, instant deployment  
**Pricing:** Free tier, $20/month for AI features  
**Best for:** Prototyping, learning to code, deploying small apps fast, collaboration

#### 11. Tabnine
**What it does:** Privacy-first code completion with on-premise deployment options  
**Pricing:** $12/month Pro  
**Best for:** Enterprise environments, sensitive codebases, offline coding

---

### Image Generation

#### 12. Midjourney
**What it does:** Best-in-class AI image generation with artistic quality  
**Pricing:** $10/month Basic, $30/month Standard, $60/month Pro  
**Best for:** Marketing visuals, concept art, creative projects, aesthetics-first images

#### 13. DALL-E 3 (OpenAI)
**What it does:** Image generation with excellent prompt following and text rendering  
**Pricing:** $0.04-$0.12 per image depending on resolution  
**Best for:** Text-in-images, precise prompt adherence, quick iterations via ChatGPT

#### 14. Stable Diffusion / SDXL
**What it does:** Open-source image generation you can run locally  
**Pricing:** Free (open-source)  
**Best for:** Custom models, unlimited generation, privacy, learning how diffusion works

#### 15. Flux (Black Forest Labs)
**What it does:** New open image model with fast generation and high quality  
**Pricing:** Free (open-source), hosted options vary  
**Best for:** Fast prototyping, open-source alternative to Midjourney

#### 16. Adobe Firefly
**What it does:** AI image generation integrated into Adobe Creative Suite  
**Pricing:** Included with Creative Cloud (~$55/month)  
**Best for:** Professional design workflows, commercial safety, integration with Photoshop

---

### Voice & Audio

#### 17. ElevenLabs
**What it does:** Ultra-realistic text-to-speech and voice cloning  
**Pricing:** Free tier (10k chars/month), $5/month Starter, $22/month Creator  
**Best for:** Voiceovers, audiobooks, podcasts, realistic character voices

#### 18. Whisper (OpenAI)
**What it does:** Speech-to-text transcription with high accuracy  
**Pricing:** $0.006 per minute via API, free open-source model  
**Best for:** Transcribing meetings, podcasts, interviews, subtitles

#### 19. Descript
**What it does:** Audio/video editing by editing text transcripts + AI voice  
**Pricing:** Free tier, $12/month Creator  
**Best for:** Podcast editing, removing filler words, overdubbing mistakes

#### 20. Play.ht
**What it does:** Text-to-speech with wide voice library and emotion control  
**Pricing:** Free tier, $31/month Pro  
**Best for:** Long-form narration, e-learning, multi-language content

#### 21. Resemble AI
**What it does:** Voice cloning and speech synthesis for brands  
**Pricing:** Custom enterprise pricing  
**Best for:** Brand voices, customer service bots, scaling voice content

---

### Video Generation & Editing

#### 22. Runway Gen-2
**What it does:** Text/image-to-video generation and AI video editing  
**Pricing:** $12/month Standard (125 credits), $35/month Pro  
**Best for:** Short video clips, concept visualization, creative video projects

#### 23. Kling AI
**What it does:** High-quality video generation with good motion  
**Pricing:** Free tier, ~$10/month for more credits  
**Best for:** Realistic motion, longer clips, experimenting with video AI

#### 24. Pika
**What it does:** Text/image-to-video with creative effects  
**Pricing:** Free tier, $8/month Standard  
**Best for:** Quick video prototypes, social media content, creative experiments

#### 25. HeyGen
**What it does:** AI avatar videos with lip sync in multiple languages  
**Pricing:** Free tier, $29/month Creator  
**Best for:** Explainer videos, multi-language content, training videos

#### 26. Descript (Video)
**What it does:** Edit video by editing text transcript + AI features  
**Pricing:** Same as audio ($12/month Creator)  
**Best for:** YouTube videos, removing filler, repurposing long-form to short-form

---

### Automation & Workflow

#### 27. n8n
**What it does:** Open-source workflow automation (self-hosted or cloud)  
**Pricing:** Free self-hosted, $20/month cloud  
**Best for:** Complex workflows, developer-friendly automation, privacy-first

#### 28. Make (Integromat)
**What it does:** Visual automation platform with deep integrations  
**Pricing:** Free tier (1000 ops), $9/month Core  
**Best for:** Mid-complexity automations, visual workflow building

#### 29. Zapier
**What it does:** Connect apps and automate workflows (easiest to use)  
**Pricing:** Free tier (100 tasks), $20/month Starter  
**Best for:** Simple automations, non-technical users, wide app ecosystem

#### 30. Windmill
**What it does:** Open-source developer platform for scripts and workflows  
**Pricing:** Free self-hosted, $10/month cloud  
**Best for:** DevOps automation, internal tools, scripts-as-workflows

#### 31. Activepieces
**What it does:** Open-source business automation, Zapier alternative  
**Pricing:** Free self-hosted  
**Best for:** Privacy-focused teams, unlimited workflows, learning automation

---

### RAG & Vector Databases

#### 32. Pinecone
**What it does:** Managed vector database for semantic search and RAG  
**Pricing:** Free tier (1 index), $70/month for production  
**Best for:** Production RAG systems, scaling semantic search, easy setup

#### 33. Chroma
**What it does:** Open-source vector database, easy to embed in apps  
**Pricing:** Free (open-source)  
**Best for:** Prototyping RAG, small projects, learning vector search

#### 34. Weaviate
**What it does:** Open-source vector database with built-in ML models  
**Pricing:** Free self-hosted, $25/month cloud  
**Best for:** Hybrid search (vector + keyword), GraphQL API fans, ML integration

#### 35. Qdrant
**What it does:** High-performance vector search engine  
**Pricing:** Free tier (1GB), $10/month starter  
**Best for:** Performance-critical apps, filtering + vector search, Rust-based speed

#### 36. Milvus
**What it does:** Open-source vector database for massive scale  
**Pricing:** Free self-hosted  
**Best for:** Billion-scale datasets, research, enterprises

---

### AI Development Frameworks

#### 37. LangChain
**What it does:** Framework for building LLM applications (Python/JS)  
**Pricing:** Free (open-source)  
**Best for:** RAG systems, agents, complex LLM pipelines, prototyping

#### 38. LlamaIndex
**What it does:** Data framework for connecting LLMs to external data  
**Pricing:** Free (open-source)  
**Best for:** Document Q&A, knowledge bases, structured data retrieval

#### 39. AutoGen (Microsoft)
**What it does:** Framework for building multi-agent systems  
**Pricing:** Free (open-source)  
**Best for:** Agent-to-agent workflows, complex reasoning, research

#### 40. LangSmith (LangChain)
**What it does:** Platform for debugging, testing, and monitoring LLM apps  
**Pricing:** Free tier, $39/month Developer  
**Best for:** Production LLM apps, debugging chains, observability

---

---

## 🚀 Part 3: 20 Weekend AI Projects

### 1. Personal RAG Chatbot
**Description:** Chat with your own documents (PDFs, notes, bookmarks). Ask questions and get answers from your knowledge base.  
**Tech Stack:** Python, LangChain, Chroma, OpenAI/Claude API, Streamlit  
**Difficulty:** ⭐⭐⭐ (3/5)  
**Time Estimate:** 6-8 hours  
**What You'll Learn:** Vector embeddings, semantic search, prompt engineering, RAG architecture

---

### 2. Email Assistant Bot
**Description:** Automatically categorize emails, draft responses, summarize long threads, and flag urgent messages.  
**Tech Stack:** Python, Gmail API, LangChain, Claude/GPT-4 API  
**Difficulty:** ⭐⭐⭐ (3/5)  
**Time Estimate:** 8-10 hours  
**What You'll Learn:** Email APIs, NLP classification, automation patterns, prompt chaining

---

### 3. Voice-Activated Task Manager
**Description:** Speak tasks, and they're automatically added to your task manager with categories and priorities.  
**Tech Stack:** Python, Whisper API, LLM for parsing, Notion/Todoist API  
**Difficulty:** ⭐⭐ (2/5)  
**Time Estimate:** 4-6 hours  
**What You'll Learn:** Speech-to-text, intent parsing, API integration

---

### 4. AI Finance Analyzer
**Description:** Upload bank statements or connect to your bank API. Get spending insights, budget recommendations, and anomaly detection.  
**Tech Stack:** Python, Plaid API or CSV parsing, Pandas, Claude API, Streamlit  
**Difficulty:** ⭐⭐⭐⭐ (4/5)  
**Time Estimate:** 10-12 hours  
**What You'll Learn:** Financial data analysis, visualization, privacy-preserving AI

---

### 5. Code Review Bot
**Description:** Automatically review pull requests and comment on potential issues, security vulnerabilities, and style violations.  
**Tech Stack:** Python, GitHub API, Claude Code, Webhooks  
**Difficulty:** ⭐⭐⭐⭐ (4/5)  
**Time Estimate:** 8-10 hours  
**What You'll Learn:** GitHub Actions, webhook handling, automated code analysis

---

### 6. Meeting Summarizer
**Description:** Record meetings, transcribe with Whisper, summarize with LLM, extract action items, and send to Notion/Slack.  
**Tech Stack:** Python, Whisper, Claude/GPT-4, Notion API  
**Difficulty:** ⭐⭐ (2/5)  
**Time Estimate:** 4-6 hours  
**What You'll Learn:** Audio processing, structured extraction, workflow automation

---

### 7. AI-Powered Blog Generator
**Description:** Input a topic, automatically generate outline, research with web search, write sections, and format as markdown.  
**Tech Stack:** Python, LangChain, Serper API (search), Claude API, Markdown  
**Difficulty:** ⭐⭐⭐ (3/5)  
**Time Estimate:** 6-8 hours  
**What You'll Learn:** Multi-step agents, web scraping, content generation pipeline

---

### 8. Smart Bookmark Manager
**Description:** Save bookmarks with AI-generated tags, summaries, and full-text search. Ask questions about saved content.  
**Tech Stack:** Python, FastAPI, Chroma, web scraping (BeautifulSoup), Claude API  
**Difficulty:** ⭐⭐⭐ (3/5)  
**Time Estimate:** 8-10 hours  
**What You'll Learn:** Web scraping, vector search, tagging systems

---

### 9. Automated Social Media Manager
**Description:** Generate posts for Twitter/LinkedIn from blog posts, schedule them, and create image variants.  
**Tech Stack:** Python, OpenAI API, DALL-E, Twitter/LinkedIn APIs, scheduling (APScheduler)  
**Difficulty:** ⭐⭐⭐ (3/5)  
**Time Estimate:** 6-8 hours  
**What You'll Learn:** Content repurposing, API rate limits, image generation

---

### 10. AI Research Assistant
**Description:** Input a research topic, automatically find papers, summarize them, identify gaps, and generate literature review.  
**Tech Stack:** Python, arXiv API, Semantic Scholar API, LangChain, Claude  
**Difficulty:** ⭐⭐⭐⭐ (4/5)  
**Time Estimate:** 10-12 hours  
**What You'll Learn:** Academic APIs, summarization, synthesis, citation handling

---

### 11. Personal Knowledge Graph
**Description:** Convert your notes into a knowledge graph with entities, relationships, and visual exploration.  
**Tech Stack:** Python, Neo4j, LangChain, LLM for entity extraction, D3.js for visualization  
**Difficulty:** ⭐⭐⭐⭐⭐ (5/5)  
**Time Estimate:** 12-16 hours  
**What You'll Learn:** Graph databases, entity extraction, NLP, data visualization

---

### 12. AI Image Organizer
**Description:** Automatically tag photos with AI vision, detect duplicates, organize into folders by content.  
**Tech Stack:** Python, GPT-4 Vision API, PIL/Pillow, file system operations  
**Difficulty:** ⭐⭐ (2/5)  
**Time Estimate:** 4-6 hours  
**What You'll Learn:** Computer vision, image processing, batch operations

---

### 13. Customer Support Bot
**Description:** Create a chatbot that answers customer questions based on your docs, escalates complex issues.  
**Tech Stack:** Python, LangChain, Pinecone, FastAPI, Discord/Slack integration  
**Difficulty:** ⭐⭐⭐⭐ (4/5)  
**Time Estimate:** 10-12 hours  
**What You'll Learn:** Production RAG, conversation handling, escalation logic

---

### 14. AI Job Application Assistant
**Description:** Scrape job postings, match to your skills, auto-generate tailored cover letters, track applications.  
**Tech Stack:** Python, web scraping (Selenium), Claude API, Airtable/Notion API  
**Difficulty:** ⭐⭐⭐ (3/5)  
**Time Estimate:** 8-10 hours  
**What You'll Learn:** Web scraping, NLP matching, workflow automation

---

### 15. Meal Planner & Recipe Generator
**Description:** Input dietary preferences, get meal plans, shopping lists, and new recipes based on what you have.  
**Tech Stack:** Python, Claude API, recipe APIs (Spoonacular), Streamlit  
**Difficulty:** ⭐⭐ (2/5)  
**Time Estimate:** 4-6 hours  
**What You'll Learn:** API integration, constraint satisfaction, user preferences

---

### 16. AI Video Clipper
**Description:** Upload long videos, automatically detect highlights, create short clips with captions for social media.  
**Tech Stack:** Python, Whisper, FFmpeg, Claude for highlight detection, MoviePy  
**Difficulty:** ⭐⭐⭐⭐ (4/5)  
**Time Estimate:** 10-12 hours  
**What You'll Learn:** Video processing, audio transcription, content detection

---

### 17. Habit Tracker with AI Coaching
**Description:** Log habits, get personalized insights and suggestions from an AI coach based on your patterns.  
**Tech Stack:** Python, SQLite, Claude API, Streamlit or React  
**Difficulty:** ⭐⭐ (2/5)  
**Time Estimate:** 6-8 hours  
**What You'll Learn:** Data persistence, behavioral analytics, personalized recommendations

---

### 18. AI-Powered News Aggregator
**Description:** Fetch news from multiple sources, summarize, detect bias, create personalized daily briefing.  
**Tech Stack:** Python, News API, LangChain, Claude, email delivery (SendGrid)  
**Difficulty:** ⭐⭐⭐ (3/5)  
**Time Estimate:** 6-8 hours  
**What You'll Learn:** News APIs, summarization, bias detection, scheduling

---

### 19. Legal Document Analyzer
**Description:** Upload contracts or terms of service, get plain-English summaries and red flags highlighted.  
**Tech Stack:** Python, LangChain, Claude Opus (long context), PDF parsing (PyPDF2)  
**Difficulty:** ⭐⭐⭐⭐ (4/5)  
**Time Estimate:** 8-10 hours  
**What You'll Learn:** PDF processing, long-context handling, legal NLP

---

### 20. AI Dungeon Master (Text RPG)
**Description:** Play an AI-powered text adventure game with dynamic story generation and memory of your choices.  
**Tech Stack:** Python, Claude API, conversation state management, Streamlit or CLI  
**Difficulty:** ⭐⭐⭐ (3/5)  
**Time Estimate:** 6-8 hours  
**What You'll Learn:** Stateful conversations, creative generation, game logic

---

## 🎯 How to Choose Your Project

**If you're a beginner:** Start with #6 (Meeting Summarizer), #3 (Voice Task Manager), or #15 (Meal Planner)

**If you want to build useful tools:** #1 (RAG Chatbot), #2 (Email Assistant), #8 (Bookmark Manager)

**If you want to learn advanced concepts:** #11 (Knowledge Graph), #13 (Customer Support Bot), #19 (Legal Analyzer)

**If you want to have fun:** #20 (AI Dungeon Master), #16 (Video Clipper), #9 (Social Media Manager)

---

## 💡 General Tips for All Projects

1. **Start simple:** Get a basic version working first, then add features
2. **Use existing APIs:** Don't build from scratch what already exists
3. **Version control:** Use Git from day one
4. **Document as you go:** Future you will thank present you
5. **Share your work:** Post on GitHub, Twitter, Reddit — get feedback
6. **Iterate:** Your first version will be rough. That's fine.

---

*Last updated: February 2026*  
*This is a living document. Update it as new tools and techniques emerge.*
