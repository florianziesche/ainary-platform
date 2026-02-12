# I Built 5 AI Tools in 48 Hours — Here's What Actually Worked

**And what completely fell apart at 4am.**

---

It's 3:17am on a Tuesday. I'm staring at my terminal watching three AI agents argue with each other about Siemens' AI strategy.

Agent 1 (Strategist): "Conservative approach recommended."  
Agent 2 (Provocateur): "That's exactly what's killing them."  
Agent 3 (Hyperthink): "Both of you are missing the point."

I'm not mediating a debate. I'm watching my code debate itself. And weirdly, it's working.

Forty-eight hours ago, I had an idea: What if I could build McKinsey-level strategy reports for $0.15 instead of $200,000?

Now I'm sitting here with five working tools:

1. **Corporate X-Ray** — AI strategy audits that cost less than a coffee
2. **Startup X-Ray** — VC due diligence with actual confidence scores
3. **AI Advisory Board** — Six AI experts who answer strategic questions
4. **Platform Website** — Landing page for all of it
5. **GA4 Intelligence Dashboard** — Analytics agent that actually explains what's happening

Total build time: 48 hours. Total sleep: maybe 6. Total lessons learned: more than I can count.

Let me show you what actually happened when you build AI tools with AI, at 3am, with no plan and too much coffee.

---

## The Setup: How I Actually Build

Before we get into the chaos, here's my stack:

**Me:** Florian (ex-startup CEO, now AI consultant, borderline insomnia)  
**My AI:** Mia (Claude Opus 4 running in OpenClaw, basically my co-founder)  
**The tools:** Node.js, OpenAI GPT-4o, Puppeteer, too many terminals

Here's how it works: I tell Mia what I want to build. She spawns sub-agents. Those sub-agents write code, test it, fix it, and report back. I review, approve, or redirect.

It's pair programming where your pair is three agents simultaneously writing different parts of the system.

Sound insane? It kind of is. But it's also the fastest I've ever built anything.

---

## Night 1: Building Corporate X-Ray (11pm–7am)

**The idea:** Feed an AI system a company name. Get back a 20-page strategy report that looks like McKinsey wrote it.

**The reality:** Way harder than I thought. Way better than I expected.

### Hour 1-3: The Architecture

I started with a simple question: How would McKinsey actually do this?

Answer: Five specialists, each looking at different angles, then a senior partner synthesizing everything.

So I built that. Five AI agents:

1. **Scanner** — Gathers intel (web search, company data, news)
2. **Industry Expert** — Benchmarks against competitors
3. **Strategist** — McKinsey-style analysis
4. **Financier** — ROI models and business cases
5. **Provocateur** — The contrarian voice (this one's my favorite)

Each agent runs in parallel. No waiting. Three agents working simultaneously, each pulling different data, analyzing from different angles.

**First mistake:** I tried to make them all run at once. Five parallel API calls. My terminal looked like a Christmas tree. Rate limits everywhere.

**Fix:** Three at a time. Scanner + Industry first. Then Strategist + Financier + Provocateur. Cuts runtime in half, no rate limit issues.

Total time for all five agents: ~60 seconds.

### Hour 4-8: The Hyperthink Synthesis

This is where it gets interesting.

Five agents means five different perspectives. Some contradict each other. Some miss obvious things. You can't just concatenate their outputs and call it a report.

I needed a synthesis layer. Something that could take all five perspectives and create a coherent narrative.

Enter **Hyperthink**: Three-round synthesis process.

**Round 1 (Synthesize):** Combine all agent outputs into one unified analysis  
**Round 2 (Critique):** Find gaps, contradictions, weak arguments  
**Round 3 (Finalize):** Produce the final report with everything integrated

Each round is a separate GPT-4o call with a structured JSON schema. No hallucinations, no "I'll just make up some numbers." If the data's not there, it says "insufficient data."

This was the breakthrough. The reports went from "okay" to "wait, this is actually good."

Time per Hyperthink cycle: ~120-230 seconds (it varies based on complexity).

### Hour 9-12: The Renderer

Now I have perfect JSON. But JSON doesn't impress clients. I needed it to look professional.

HTML template. Dark mode. Glassmorphism cards (yes, I care about aesthetics at 4am). SVG charts. Radar diagrams. Risk matrices.

**Biggest pain point:** SVG coordinate math while sleep-deprived.

Do you know how a radar chart works? You take five scores (0-100), map them to polar coordinates, and draw a polygon.

Simple, right?

Not at 5am when you keep getting the viewBox wrong and your pentagon is halfway off the screen.

I must have regenerated that template 15 times before the math was right.

**But then:** PDF generation with Puppeteer. Full dark mode in HTML. Academic print version in PDF. Page breaks, headers, footers, table of contents.

Final output: A 20-page strategy report that looks like a consulting firm made it.

**Cost:** $0.15 in API calls.  
**Time:** 3-5 minutes from company name to PDF.  
**Comparison:** McKinsey charges $200K and takes 6 weeks.

I sat back and stared at the first real report (Siemens). It was good. Legitimately good.

---

## Night 2: Startup X-Ray + Platform Website (11pm–6am)

Night one proved the concept. Night two was about scaling the idea.

### The VC Version

Corporate X-Ray was built. But I'm also a VC (transitioning, anyway). I needed a version for startups.

Same architecture. Different agents:

1. **Scanner** — Startup intel + confidence scoring (this is key)
2. **Market Analyst** — TAM/SAM/SOM + market timing
3. **Investor** — Deal score + investment thesis
4. **Financier** — Valuation + unit economics
5. **Devil's Advocate** — Red flags + kill shots

**The differentiator:** Confidence indicators.

Every claim in a Startup X-Ray report has a confidence score: ●●●○○ (3/5), ●●●●● (5/5), etc.

Why? Because honesty is a feature.

When you're doing due diligence on a pre-seed startup with no revenue, you *don't* have complete data. Pretending you do is how bad investments happen.

So my system says: "Here's what we know. Here's how confident we are. Here's what we couldn't verify."

No other tool does this. Because no other tool wants to admit uncertainty.

I built this in ~6 hours (copy-pasted a lot from Corporate X-Ray). Purple accent color instead of indigo. "Devil's Advocate" instead of "Provocateur." Same bones, different skin.

### The Platform Website

By 5am I had two working tools. But they were just Node.js scripts. No one could use them except me.

I needed a front door.

One-page website. Clean design. "AI-Powered Strategy Intelligence."

Three product cards:
- Corporate X-Ray (for companies)
- Startup X-Ray (for VCs)
- Coming Soon (everything else)

Email capture modal. Name, email, company, role. Download the report, join the waitlist.

Built in one sitting. Deployed to GitHub Pages. Done.

**Lesson learned:** You don't need a SaaS dashboard on day one. You need a landing page and an email form. Ship the minimum viable front door.

---

## The Chaos: What Didn't Work

Let me be brutally honest about what broke, spiraled, or just didn't work.

### 1. The Research Machine That Wrote a Novel

Early version of Scanner had web search integration. I told it: "Get comprehensive data on this company."

It took me literally.

Fifty-five pages. Single-spaced. Every news article, every press release, every LinkedIn post about the company for the last three years.

Useless. Completely useless.

**The problem:** I didn't give it constraints. "Comprehensive" to an AI means "everything."

**The fix:** Explicit limits. "Max 10 sources. Prioritize last 6 months. Focus on strategic moves, not press fluff."

Lesson: Sub-agents are like interns. They do exactly what you say. If you say "get me everything," they will drown you in everything.

### 2. CSS Bugs in `file://` URLs

Puppeteer generates PDFs by rendering HTML in headless Chrome. I developed the template by opening `template.html` in my browser with a `file://` URL.

Looked perfect.

Then I ran it through Puppeteer. Half the styles were broken.

Why? Chrome treats `file://` URLs differently than `http://` URLs. Some CSS properties (especially `backdrop-filter`) just don't work.

I spent an hour debugging CSS that worked in my browser but not in Puppeteer.

**The fix:** Always test in Puppeteer. What you see in your browser is a lie.

### 3. Double Messages from Sub-Agents

This one was my fault.

I had sub-agents reporting progress back to the main chat. "Scanner complete." "Hyperthink Round 1 done." Etc.

Useful for debugging. Annoying for production.

Then I tried to suppress those messages. Ended up with some agents sending duplicates, some sending nothing, complete chaos.

**The Kintsugi fix:** Embraced it. Instead of suppressing, I made the messages *useful*. Each sub-agent now reports status, runtime, and a one-line summary of what it found.

Turned a bug into a feature. Progress updates are actually valuable when you're waiting 3 minutes for a report.

### 4. Overbuilding Instead of Shipping

Here's the uncomfortable truth: I could've shipped Corporate X-Ray after 8 hours.

Instead, I spent 4 more hours perfecting the PDF styling. Making sure the radar chart had the exact right padding. Obsessing over whether the risk matrix circles were pixel-perfect.

At 6am, exhausted, I realized: No one cares if the SVG is 2 pixels off.

They care if the insights are good.

**Lesson:** Ship ugly. Improve later. Perfection is procrastination in disguise.

---

## The Numbers (Because Specifics Matter)

Let's talk real data.

**Corporate X-Ray:**
- 5 agents
- 3-round Hyperthink synthesis
- 8 OpenAI API calls per report
- ~$0.15 cost per report
- 3-5 minutes runtime
- 20-page PDF output

**Startup X-Ray:**
- Same architecture
- Confidence scoring on every claim
- ~$0.12 cost per report (slightly less data)
- Purple instead of indigo (yes, this matters for branding)

**Platform:**
- 1 landing page
- GitHub Pages (free)
- 0 lines of backend code (yet)
- Email capture via form endpoint

**Total build time:** 48 hours  
**Total sleep:** ~6 hours  
**Total coffee:** I stopped counting  
**Total API cost during development:** ~$8  
**Total revenue so far:** $0 (haven't launched)

**Projected Q1 revenue (conservative):** €67,000  
**Projected Q1 revenue (optimistic):** €180,000

Why the range? Because I don't know yet if this will work. But the unit economics are insane.

If I can get 100 companies to pay €49 for a Corporate X-Ray report, that's €4,900. Cost: €15. Margin: 99.7%.

If I can get 5 consulting firms to pay €5,000 for white-label access, that's €25,000.

The math works. The product works. Now I just have to see if anyone wants it.

---

## What I Learned About Building With AI

### 1. Sub-Agents Need Exact Briefings

You can't tell an AI agent "figure it out." You have to be explicit.

Bad: "Analyze the company's strategy."  
Good: "Analyze the company's AI strategy. Focus on: data infrastructure, talent, investment, competitive position. Output JSON with scores 0-100 for each dimension."

The more specific your instructions, the better the output. Every time I got frustrated with an agent, it was because *I* wasn't clear enough.

### 2. Parallel Beats Sequential (But Not Always)

Running agents in parallel is 3x faster than sequential.

But you can't parallelize everything. Hyperthink *has* to be sequential. Round 2 needs Round 1's output. Round 3 needs Round 2's critique.

Know when to parallelize, when to sequence. It's the difference between 2 minutes and 6 minutes.

### 3. Errors Become Features (Kintsugi System)

Every bug I hit became an improvement.

- Rate limits → forced me to batch smartly  
- CSS bugs → made me test in production environment  
- Double messages → became useful progress updates  
- Research overload → forced explicit constraints  

I started calling this the "Kintsugi System" (Japanese art of repairing pottery with gold). Errors aren't failures. They're scars that make the system stronger.

### 4. Honest Beats Perfect

The Confidence Indicator system was born from a limitation.

Early Startup X-Ray reports made claims I couldn't verify. "This startup has product-market fit." Based on what? A landing page and 3 tweets?

I could've hidden the uncertainty. Instead, I made it explicit.

"Product-market fit: ●●○○○ (Low confidence — limited data available)"

Counterintuitive: Admitting what you *don't* know builds more trust than pretending you know everything.

### 5. Ship Ugly, Improve in Public

The first version of Corporate X-Ray had Apple emoji in the section headers. 🎯 for Strategy, 💰 for Financials.

Looked terrible in the PDF. Florian (me, reviewing my own work) was like "what is this, a Notion page?"

I could've spent 2 hours picking the perfect icons. Instead, I shipped, got feedback, replaced them with SVG icons in 20 minutes.

Shipping beats polishing. Every time.

---

## The Tools That Emerged

By the end of 48 hours, I had:

**1. Corporate X-Ray** — Strategy audits for €49 (vs McKinsey's €200K)  
**2. Startup X-Ray** — Due diligence for VCs with honesty built in  
**3. AI Advisory Board** — 6 AI experts (Strategist, Financier, Growth, Product, Tech, Culture) answering questions  
**4. Platform Website** — One landing page to rule them all  
**5. GA4 Dashboard** — Analytics agent (bonus: built this in 3 hours on Night 2 because I was procrastinating)

**What's next:**
- Content X-Ray (analyze articles, suggest improvements)
- IC Co-Pilot (investment committee prep)
- Competitor X-Ray (market positioning)
- News Intelligence Layer (auto-updating company intel)

Each one is 1-2 days of build time. Because once you have the architecture, you're just swapping agents.

---

## The Uncomfortable Truth

Here's what I keep coming back to:

**I built these tools faster than I can sell them.**

48 hours to build 5 tools. How long to get the first customer? I don't know yet.

This is the operator's curse: Building is the easy part. Distribution is the hard part.

I can spin up a new AI tool in a weekend. But getting someone to trust it enough to pay? That's the real work.

And I don't have an answer yet.

Right now, these are demos. Impressive demos, but demos. The real test is: Will a CFO pay €49 to X-Ray their own company? Will a VC pay €499/month for unlimited Startup X-Rays?

The product works. The economics work. But do the humans work?

That's what I'm about to find out.

---

## What This Means for You

If you're a **founder:** You can build faster than you think. Seriously. I built 5 tools in 48 hours. Not because I'm special, but because I let AI do the heavy lifting. Stop building everything yourself. Orchestrate agents. Ship faster.

If you're a **consultant:** Your industry is about to get disrupted. Hard. I just built a McKinsey replacement for $0.15. You can either build your own AI tools or compete on the one thing AI can't replace: relationships and judgment.

If you're a **VC:** Due diligence is about to get commoditized. Startup X-Ray does in 3 minutes what an associate does in 3 days. The VCs who win will use AI to see *more* deals, not replace human judgment on which ones to back.

If you're **anyone building with AI:** The infrastructure is ready. The models are good enough. The only bottleneck is you.

Stop waiting for the perfect idea. Start building. Ship ugly. Learn fast.

I went from "what if" to working product in 48 hours. You can too.

---

## The Real Lesson

Here's what 48 hours of building at 3am taught me:

**Speed is a feature.**

Not because fast is better. But because fast forces you to make decisions.

Should I spend 4 hours perfecting the PDF styling? No, ship it.  
Should I build a full SaaS dashboard? No, landing page first.  
Should I wait until I have 10 tools? No, launch with 2.

Every hour I spent building was an hour I *wasn't* overthinking.

The best product decisions I made were the ones I didn't have time to overthink.

And the worst decisions? The ones I agonized over at 5am when I should've just shipped and learned.

---

## What Happens Next

Monday, February 16th, I'm launching this publicly.

Corporate X-Ray goes live. Startup X-Ray goes live. Platform website goes live.

Then I'll find out if any of this actually matters.

Maybe I'll get 100 signups in the first week. Maybe I'll get 3.

Either way, I'll learn something. And I'll build the next version based on what real users actually want, not what I *think* they want at 3am.

Because that's the real superpower of building fast: You get to fail fast. And failing fast is how you find what works.

---

**The tools are built. The reports are real. The pricing is set.**

Now I just have to see if anyone cares.

If you're reading this and thinking "I'd actually use that," hit reply. Or find me on LinkedIn. Or just go to the website and download a sample report.

Because the only way I'll know if this works is if you tell me.

And if it doesn't? I'll build something else. In 48 hours. At 3am. With too much coffee.

That's how this works now.

---

**Florian Ziesche**  
*AI Consultant | Ex-Startup CEO | Professional 3am Builder*

*Built with: Claude Opus, OpenAI GPT-4o, Node.js, Puppeteer, and an alarming amount of caffeine.*  
*Timeline: February 10-12, 2026 (11pm–7am, twice)*  
*Cost: ~$8 in API calls + €0 in sleep*

---

**Want to try it?**  
Corporate X-Ray: [coming Monday]  
Startup X-Ray: [coming Monday]  
Or just reply and tell me what you'd actually use.

---

*Published: February 12, 2026*  
*Reading time: ~12 minutes*  
*Word count: 3,247*

*(Yes, I went over the target. Turns out I had more to say than I thought. That's what happens when you write at 5am after building for 48 hours straight.)*
