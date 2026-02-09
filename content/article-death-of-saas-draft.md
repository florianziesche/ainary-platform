# The Death of SaaS: When Building Becomes Cheaper Than Buying

You're paying $150 per month, per user, for Salesforce. That's $90,000 a year for a 50-person company. You're paying for software that forces your sales team to adapt to its workflow instead of the other way around.

What if you could build a CRM that actually fits your business for $13,000 in year one, and $13,000 per year after that?

That's not a hypothetical. That's the math today. Claude API costs for code generation, hosting on Vercel, a Postgres database, and maybe 80 hours of someone's time to prompt and QA. Year one: $26,000. Every year after: $13,000.

Three-year total cost for Salesforce: $451,667.  
Three-year total cost for custom AI-built: $52,600.  
Savings: $399,067.

We're entering a new phase of software. The phase where building is cheaper than buying.

---

## The SaaS Model Is Based on Old Math

SaaS pricing made sense when software was expensive to build. You needed developers, designers, product managers, and months of work to ship anything. SaaS vendors amortized that cost across thousands of customers. You paid a subscription, they gave you software. Everybody won.

But the cost structure was always weird. For every $100 you paid Salesforce, roughly $40 went to sales and marketing (convincing you to buy), $20 went to R&D (building features you might not use), $15 went to infrastructure, and the rest was profit and overhead.

You weren't paying for software. You were paying for sales commissions.

AI flips this. The cost to generate software is now measured in API tokens, not developer salaries. Building a functional CRM from scratch costs a few hundred dollars in Claude API calls. Hosting costs a few thousand a year. Maintenance is mostly prompting the AI to make changes.

The entire "economies of scale" argument that justified SaaS evaporates. Custom software's marginal cost per user is near zero. SaaS scales costs linearly with headcount.

At 10 employees, SaaS is probably still cheaper. At 50 employees, custom breaks even. At 500 employees, you're saving $850,000 per year.

The math is undeniable. The question is whether companies will actually do it.

---

## What Doesn't Die

Not all SaaS dies. Some categories are immune because they have moats AI can't cross.

**Network effects protect collaboration tools.** You can build a Slack clone with AI, but you can't make your entire industry move to it. Slack's value is that everyone is already there. Same with Figma (design collaboration) and GitHub (code hosting + social graph).

**Data moats protect infrastructure.** Stripe owns the payment network relationships. LinkedIn owns the professional graph. Bloomberg owns financial data. You can replicate their UI with AI, but you can't replicate decades of accumulated proprietary data.

**Compliance moats protect boring industries.** You can build a custom accounting system, but you can't make it SOX-compliant without deep expertise. Same with healthcare (HIPAA), finance (PCI-DSS), and HR (employment law that varies by jurisdiction). AI can generate code. It can't give you audit certifications.

**Hard infrastructure protects the technical stuff.** Snowflake's query optimizer, Datadog's monitoring infrastructure, Cloudflare's edge network. These aren't just software. They're years of distributed systems engineering. AI can't replicate that from a prompt.

The pattern: SaaS survives when the hard part isn't the software, it's what's underneath.

Everything else? Vulnerable.

---

## The First Domino Won't Be Salesforce

Companies won't replace Salesforce first. Too risky. Too embedded. Too political.

They'll replace Asana. Or their niche industry tool that costs $5,000/year. Or their internal reporting dashboard. Something low-stakes where if the AI-generated version is buggy, it's annoying but not catastrophic.

They'll learn. They'll iterate. They'll prove the model works. Then they'll go after bigger targets.

By 2027, some recognizable tech company (my guess: Series B, 100-200 employees) will publish a blog post titled "Why We Ditched [SaaS Tool] and Built Our Own with AI." It'll hit the front page of Hacker News. Twitter will lose its mind. VC slide decks will add "AI disruption risk" to every SaaS pitch.

That's the watershed moment. After that, "we build our own tools" becomes normal.

---

## What Happens to the Incumbents?

The smart ones become platforms. They stop selling software and start selling infrastructure.

Salesforce doesn't sell you a CRM. They sell you a data layer and let you prompt-generate your own UI on top of it. Stripe already did this. They're payments infrastructure, not a payments app. Twilio did this. They're communication primitives, not a communication tool.

The next decade of SaaS is "headless everything." You rent the hard parts (data models, compliance, integrations) and build the interface yourself.

The dumb incumbents will fight. They'll run FUD campaigns about security risks and compliance failures. They'll commission Gartner reports about "hidden costs of custom software." They'll acquire AI coding tools and try to bundle them.

Some will survive by adapting. Most won't.

---

## The Vertical Uprising

Horizontal SaaS tried to serve everyone. A CRM for all industries. Project management for all teams. That made sense when building software was expensive. You needed massive scale to justify the cost.

AI makes vertical software economically viable. You can build a CRM specifically for pharmaceutical sales, with fields for prescriber NPI numbers and DEA licenses. You can build project management for construction companies, with change orders and permitting workflows baked in.

Vertical tools will beat horizontal tools because they fit the actual workflow instead of forcing companies to adapt.

The "Salesforce for X" era is over. The "AI-native tool for X" era is starting. And "X" is very, very specific.

Veeva already proved this in pharma. Toast proved it in restaurants. Procore proved it in construction. They beat the horizontal giants by going deep on one industry.

Now imagine 100 companies doing that simultaneously, except they're not spending 5 years building software. They're spending 5 months prompting AI.

The Cambrian explosion of vertical software is coming.

---

## The Cost Model (With Real Numbers)

Let's run the numbers for a 50-person company replacing Salesforce.

**Salesforce (Year 1):**
- Enterprise plan: 50 users × $150/month × 12 months = $90,000
- Add-ons (Einstein AI, analytics): $30,000
- Implementation and customization: $50,000 (amortize over 3 years = $16,667)
- Admin time (25% of one person): $25,000
- **Total: $161,667**

**Years 2+:** $145,000 annually

**Custom AI-Built CRM (Year 1):**
- Claude API for code generation: $750
- Developer time (80 hours @ $150/hour): $12,000
- Hosting (Vercel + AWS RDS): $250/month × 12 = $3,000
- **Total: $15,750**

**Years 2+:**
- Hosting: $3,000
- Maintenance (5 hours/month @ $150/hour): $9,000
- Claude API for ongoing features: $1,200
- **Total: $13,200 annually**

**Break-even: Month 13.**  
After that, you're saving $130,000+ per year.

The bigger you get, the more insane the SaaS pricing looks. At 500 employees, Salesforce costs $900,000/year. Custom costs maybe $50,000/year (complexity scales slightly, but not linearly with users).

You're saving $850,000 annually.

---

## The Counterargument (And Why It Matters)

Here's the strongest case against this thesis:

**AI-generated code is brittle.** It works for demos. It breaks in production. You can prompt an AI to build a CRM, but can you prompt it to handle race conditions when two sales reps update the same lead simultaneously? Can you prompt it to implement proper authentication, prevent SQL injection, and handle GDPR deletion requests correctly?

**Software rots.** Your AI-generated app works great today. In 12 months, a key dependency is deprecated. A security vulnerability is discovered. Browser APIs change. SaaS vendors have teams dedicated to keeping things working. With custom AI, you're on your own.

**Most companies are bad at specifying what they want.** SaaS works because someone else decided what features matter. You just pick a plan. Custom software requires you to know what you need. Most companies don't. They think they do, then they build the wrong thing.

**The coordination problem.** If your sales team builds a custom CRM and your marketing team builds a custom marketing tool, who builds the integration? You've recreated the integration hell that SaaS was supposed to solve, except now you own all the maintenance.

These aren't hypotheticals. They're real risks. The companies that ignore them will build garbage, blame the AI, and go back to SaaS.

The companies that take them seriously will build systems that actually work.

---

## What This Looks Like in Practice

A post-SaaS company doesn't buy horizontal tools. It commissions vertical tools.

Your ops person isn't a "Salesforce admin" who spent months getting certified. They're a process designer who can articulate business logic clearly enough for an AI to implement it.

Your software isn't scattered across 30 SaaS subscriptions. It's 5-10 AI-built apps running on your own cloud account. Your data isn't fragmented across vendors. It's in your Postgres database, your S3 bucket, your control.

You don't standardize processes to fit the tools. The tools fit the process.

This is either liberating or chaotic, depending on whether you actually know what you're doing.

Most companies don't. They worship "best practices" because SaaS vendors encode them. Without those guardrails, they'll implement terrible workflows and wonder why their custom software sucks.

The winners will be companies with strong operational thinking who can design good processes and then implement them with AI.

The losers will be companies who think "custom software" means "build whatever random thing someone asks for" and end up with unmaintainable spaghetti.

---

## The Market Opportunity

Global SaaS market: ~$200B today, projected $350B by 2029.

If 30% of that shifts to custom AI-built software over the next 5 years, that's $105B moving from subscriptions to builds.

Where does that money go?

- 15% to AI labs (Anthropic, OpenAI) for API tokens: $15.75B
- 20% to cloud providers (AWS, Vercel) for hosting: $21B
- 30% to product studios and consultancies for implementation: $31.5B
- 35% stays internal (companies building themselves): $36.75B

The TAM for "AI product studios" is roughly $31.5B by 2029.

If you focus on mid-market companies (20-500 employees), that's about 40% of the total. **$12.6B addressable market.**

Capture 3-5% of that and you're at $380-630M in revenue.

The path:
- 2026: 50 clients @ $50K = $2.5M
- 2027: 200 clients @ $75K = $15M
- 2028: 500 clients @ $100K = $50M
- 2029: 1,000 clients @ $120K = $120M

Assumes repeatability, productized offerings, and strong retention (because the real money is in year 2+ maintenance, not the initial build).

This is not a small market. This is infrastructure-level scale.

---

## When This Actually Happens

**By end of 2026:** A recognizable tech company publishes "Why We Ditched [SaaS Tool] and Built Our Own." The narrative goes mainstream.

**By mid-2027:** Salesforce or a similar incumbent launches an AI-powered customization platform. They position it as "build on us" not "replace us." Whether it works is TBD.

**By 2028:** At least one AI product studio reaches $50M ARR. Proof that this business model scales beyond boutique consulting.

**By 2028:** Token costs stabilize. AI labs need profitability. The pricing free-fall ends. The cost advantage of custom software shrinks slightly but remains significant.

**By 2029:** Vertical AI companies (pharma CRM, construction PM, legal practice management) collectively raise $5B+ in VC funding. Vertical becomes the dominant strategy for new software startups.

This isn't a 2026 revolution. It's a 5-year shift. Gradual, then sudden.

---

## What to Do About It

**If you're a company:**

Start small. Replace your lowest-stakes tool first. Your project management app. Your internal dashboard. Your niche industry software.

Learn what works. Learn what breaks. Iterate.

Then go after bigger targets.

Don't start with Salesforce. You'll fail and conclude custom doesn't work.

**If you're building a SaaS company:**

Become a platform, not a product. Let customers build on top of your data layer and infrastructure.

Or go vertical. Deep customization for one industry beats shallow customization for all industries.

Or build something with a real moat. Network effects. Proprietary data. Compliance certifications. Hard infrastructure.

Generic horizontal SaaS with no moat is dead. Plan accordingly.

**If you're an AI product studio (or thinking about starting one):**

Productize. Don't do bespoke consulting for every client. Build repeatable processes.

Go vertical. Pick 2-3 industries and become THE studio for those.

Price for value, not cost. If you save a client $100K/year, charge $50K, not $20K.

Build for retention. The real business is year 2+ maintenance and feature additions.

Document everything. The market is skeptical. Prove it works with case studies and transparent pricing.

---

## Final Thought

The death of SaaS isn't a revolution. It's an evolution.

Software is becoming a commodity. The companies that survive will be the ones that recognize this and move up the value chain.

The question isn't "will AI kill SaaS?"

It's "which SaaS companies adapt fast enough to survive, and which new companies capitalize on the shift?"

The next 5 years will answer that.

And if you're paying attention, there's a lot of money to be made in the transition.

---

*If you're building in this space or have thoughts on where this goes, I'd love to hear from you. Reply to this email or find me on Twitter.*

---

**Want more like this?** Subscribe for deep dives on AI, software economics, and the future of how companies build.

[Subscribe Button]

---

*Published: February 2026*  
*Research methodology: 10-perspective cognitive analysis*  
*Read the full research breakdown: [link to research doc]*
