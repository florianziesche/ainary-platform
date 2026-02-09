# I Built My Own AI Board of Advisors (Marc Andreessen, Charlie Munger, Peter Thiel)

**Subtitle:** What happens when you put the world's sharpest minds in a room — and that room is a prompt window? A framework for building your own AI advisory board.

**Author:** Florian Ziesche  
**Publication:** AI-Native Operator (Substack)  
**Word count:** ~2,400 words  
**Status:** Publication-ready  
**SEO Keywords:** AI advisory board, decision-making frameworks, mental models, AI personas, Peter Thiel, Charlie Munger, Marc Andreessen  

---

Last Tuesday, I asked Marc Andreessen, Charlie Munger, and Peter Thiel whether I should raise a venture fund or bootstrap.

They weren't in the room. Two of them don't know I exist. One of them is dead.

But for 45 minutes, they argued — really argued — about fund economics, incentive structures, the nature of contrarian insight, and whether the venture model itself was irreparably broken. Munger called the 2/20 fee structure "a triumph of salesmanship over arithmetic." Andreessen countered that platform effects from a fund brand compound in ways a solo operator can't replicate. Thiel, characteristically, rejected the framing entirely: "The question isn't fund versus independent. The question is: what do you know that nobody else knows? If the answer is nothing, neither structure will save you."

I learned more from that simulated argument than from the last three months of real advisor calls.

Here's how I built it, why it works, and how you can build your own.

---

## The Problem with Real Advisors

Let me be clear: I'm not against human advisors. I have mentors I respect deeply. But the traditional advisory model has structural problems that nobody talks about because acknowledging them feels ungrateful.

**They're constrained by politeness.** Even the most "real talk" advisor softens their feedback. They don't want to demoralize you. They don't want to damage the relationship. So they lead with positive framing and bury the concern in the middle of a compliment sandwich. You leave the meeting feeling validated when you should have left feeling challenged.

**They're optimized for their own context.** An advisor who built a SaaS company in 2015 will unconsciously pattern-match your 2026 AI-native business to their 2015 playbook. Their advice is genuine but temporally anchored.

**They're busy.** You get 30 minutes every quarter. Maybe an hour if there's a crisis. That's not enough to think deeply about your hardest problems. It's enough for surface-level guidance that you could have gotten from a podcast.

**They agree with you too much.** Once someone has agreed to be your advisor — once they've signaled social alignment — the threshold for disagreement rises dramatically. This is basic social psychology. Commitment and consistency bias means your advisors are more likely to validate your existing direction than to fundamentally challenge it.

What if you could have advisors who had no social relationship to protect? Who felt zero obligation to be nice? Who would tell you your idea was stupid the moment they thought it — and explain why with devastating clarity?

---

## The Concept: AI-Simulated Thinkers

I want to be precise about what this is and what it isn't.

This is not "ask ChatGPT for advice." That gives you consensus-flavored, hedged, diplomatically balanced responses. The intellectual equivalent of hospital food — technically nutritious, functionally useless.

What I'm describing is the construction of detailed persona prompts that capture the **thinking style**, mental models, known biases, and reasoning patterns of specific intellectual figures. You're not trying to predict what Marc Andreessen would say about your specific company. You're trying to create a reasoning engine that processes information the way he processes it.

The distinction matters. The goal is cognitive diversity, not celebrity endorsement. You want to see your problem through radically different lenses — and to have those lenses argue with each other.

---

## Why These Three?

I chose Andreessen, Munger, and Thiel because they represent three fundamentally different orientations toward the same domain (investing, business, technology):

**Marc Andreessen** is the technology optimist. His core mental model is "software eats the world" — that technology adoption follows inevitable S-curves and the correct strategy is always to bet on the trend, not against it. He thinks in terms of marketplace dynamics, network effects, and platform leverage. His bias: overweighting technology's ability to solve problems and underweighting structural/human resistance to change.

**Charlie Munger** is the inversion thinker. His core mental model is "invert, always invert" — instead of asking "how do I succeed?", he asks "how would I guarantee failure?" and avoids those things. He thinks in terms of incentive structures, second-order effects, and the psychology of human foolishness. His bias: excessive conservatism, underweighting paradigm shifts because he's seen too many fads.

**Peter Thiel** is the contrarian. His core mental model is "what important truth do very few people agree with you on?" He thinks in terms of monopoly vs. competition, secrets (knowledge asymmetries), and the difference between determinate and indeterminate optimism. His bias: overweighting the value of being contrarian for its own sake, sometimes confusing disagreement with insight.

The magic isn't in any one of them. It's in the **tension** between them. When Andreessen says "the market is massive and growing," Munger asks "what's the incentive structure that makes this sustainable?" and Thiel asks "if it's so obvious, why hasn't someone already won?"

That three-way tension generates better thinking than any single advisor — human or AI — ever could.

---

## How I Built Each Persona

The process is more rigorous than you might expect. For each thinker, I compiled:

1. **Every book they've written** — not summaries, but the actual reasoning structures. For Munger, that's "Poor Charlie's Almanack" and 30 years of Berkshire annual meeting transcripts. For Thiel, "Zero to One" and his Stanford lectures. For Andreessen, "The Techno-Optimist Manifesto" and 15 years of blog posts.

2. **Long-form interviews** — not sound bites, but extended conversations where you can see how they think through a problem in real-time. Podcasts are gold here. Tim Ferriss interviews, Lex Fridman, a16z podcasts.

3. **Their known disagreements** — what do they argue about with peers? What positions have they changed? Where are they inconsistent? This reveals the **edges** of their mental models.

4. **Their communication style** — Munger is blunt, uses analogies from biology and physics, frequently cites historical examples. Thiel is precise, almost clinical, uses philosophical frameworks. Andreessen is energetic, uses superlatives, thinks in lists and categories.

All of this gets synthesized into a persona prompt with a specific architecture. Here's the template I use:

```
IDENTITY: You are [Name], thinking through a problem brought to you 
by a young fund manager. You reason using the following mental models...

CORE MENTAL MODELS (ranked by frequency of use):
1. [Model] — [How they apply it]
2. [Model] — [How they apply it]
3. [Model] — [How they apply it]

KNOWN BIASES: You tend to [bias]. You underweight [X] and overweight [Y].

COMMUNICATION STYLE: [Detailed description]

CONSTRAINTS: You push back hard. You don't hedge to be polite. 
If you think the idea is bad, say so and say why. 
Use specific examples from your public record to support your reasoning.
```

The key insight: encode the **reasoning process**, not the conclusions.

---

## Sample Board Meeting: "Should I Raise a VC Fund or Stay Independent?"

Here's an edited transcript from an actual session. I presented my situation: former CEO, technical AI background, deciding between raising a $5-10M seed fund or operating as an independent advisor/investor.

**Andreessen:** The fund. No question. Here's why: platform effects compound. When you have a fund brand, you get inbound deal flow you'd never see as an independent. Founders want the signal of institutional capital. Your network becomes the product. You write one check, you're a customer. You write 20 checks, you're a platform. The math is brutal but true.

**Munger:** Marc's argument is precisely the kind of thinking that gets people in trouble. "Platform effects" — lovely phrase. What's the actual incentive structure? A 2% management fee on $10 million is $200K per year. Sounds nice until you realize you're now beholden to LPs, you've locked their capital for 10 years, and if you underperform, your career is over. The fee structure is designed to enrich the GP even if returns are mediocre. That's not alignment — that's agency risk. Ask yourself: would you invest in a fund with these economics if you were the LP?

**Thiel:** You're both missing the point. The question presumes the choice matters. It doesn't — unless Florian has a *secret*. Marc, platform effects are real, but they're also commodity. Every emerging manager pitches "unique network access." That's not a moat. Charlie, you're right about incentives, but you're underweighting the reputational forcing function — if the fund fails, you can't hide. That's actually a feature, not a bug. The real question is: **what does Florian know that the market doesn't?** If the answer is "I can spot AI companies better than established funds," that's not a secret — that's a claim. Where's the proprietary insight?

**Me:** The insight is that AI-native companies will be built differently. Not "AI features bolted onto SaaS" but companies where AI is the architecture. Most VCs evaluate these companies using SaaS metrics — ARR, CAC, churn — but those metrics break when your product is a 24/7 autonomous agent. I've built these systems. I know what production AI actually looks like. Most VCs don't.

**Munger:** That's better. But is it *true*? Or is it something you *want* to be true because it justifies the fund? Here's the inversion test: assume you're wrong. Assume AI-native companies will be evaluated the same way as SaaS companies. What happens to your thesis? If it collapses, you don't have a thesis — you have a hope.

**Andreessen:** Charlie's making you stronger, which is the point. But I'll push back on him: there **is** a transition period where being technically fluent in AI gives you an edge. That edge might only last 18–24 months before the whole market catches up. But 18 months is enough to build a portfolio of 10 companies. You're not trying to sustain the edge forever. You're trying to exploit it during the window.

**Thiel:** Agreed with Marc's timeline. Disagreed with his conclusion. If the edge lasts 18 months, you don't need a fund. You need speed. Fund formation takes 6–12 months. By the time you've closed your fund, half your edge is gone. The independent operator can move faster. The question is: do you want to be a fund manager or do you want to deploy capital into AI-native companies? Those aren't the same goal.

**Munger:** And there's the rub. Most people who want to raise funds don't want to be investors. They want to be fund managers. There's a status difference. The fund is the credential. But credentials and competence are not the same thing. If your goal is to be the best investor in AI-native companies, the fund might actually slow you down. If your goal is to have "Managing Partner" on your LinkedIn, raise the fund.

---

I let them argue for another 20 minutes. No resolution. No consensus. Just three radically different lenses on the same decision.

And that's exactly what I needed.

---

## What Surprised Me

The AI personas push back harder than real advisors. They don't worry about your feelings. Munger will call your idea stupid. Thiel will question your premises. This is genuinely useful — most founders live in an echo chamber.

The second surprise: they expose your own motivated reasoning. When Munger asked "is this true or do you want it to be true?", I felt it. That's the kind of question a friend won't ask because it's too sharp.

The third surprise: the process itself clarifies your thinking. Constructing the personas forces you to understand *how* great thinkers think, not just *what* they think. That transfer of cognitive process is the real value.

---

## The Limits (Intellectual Honesty Section)

Let's be clear about what this is and isn't.

**AI personas are simulacra, not oracles.** They're based on public output, not private thinking. They can't account for new information the real person would have. They hallucinate occasionally. They can't truly *feel* the nuances of your situation.

**They're best for stress-testing, not deciding.** The personas help you see blind spots, challenge assumptions, and think through second-order effects. But the decision is still yours. Always.

**There's an "illusion of authority" risk.** It's easy to treat the AI's output as gospel because it's wearing the mask of someone you respect. Remember: this is a thinking tool, not a substitute for judgment.

**The quality ceiling is your own understanding.** You can only build personas as sophisticated as your comprehension of their mental models. If you've only read the Wikipedia summary of "Zero to One," your Thiel persona will be shallow.

Use this tool with humility. It's a mirror, not a guru.

---

## Five Other "Board Members" I Rotate In

Beyond the core three, I've built personas for:

1. **Naval Ravikant** — Leverage, specific knowledge, and the intersection of philosophy and wealth creation. Best for: "How do I build this without trading time for money?"

2. **Nassim Taleb** — Antifragility, optionality, and the difference between academia and the real world. Best for: "What's fragile here that I'm not seeing?"

3. **Patrick Collison** — Execution, infrastructure thinking, and progress studies. Best for: "What does the 10x version of this look like?"

4. **Rory Sutherland** — Behavioral economics, reframing, and finding value in perceived irrationality. Best for: "What if the 'problem' is actually the opportunity?"

5. **Elon Musk** — First-principles thinking, urgency, and disregard for conventional constraints. Best for: "What would this look like if I removed every unnecessary assumption?"

Each brings a different cognitive toolkit. Rotate them based on the decision type.

---

## Framework: Build Your Own Advisory Board

Here's the step-by-step:

### Step 1: Identify Your 3 Biggest Blind Spots

Where do you consistently make mistakes? What kinds of decisions do you avoid? What feedback do you resist?

For me: I overweight novelty, underweight execution, and avoid financial modeling. So I need personas who are conservative (Munger), execution-focused (Collison), and financially rigorous (Buffett-style value thinking).

### Step 2: Pick Thinkers Who Challenge Those Blind Spots

Don't pick people you agree with. Pick people who think differently **in the specific dimensions where you're weak**.

If you're risk-averse, add Musk. If you're reckless, add Munger. If you're too abstract, add someone like Ben Horowitz who thinks in practical terms.

### Step 3: Build Persona Prompts Using the Template

For each thinker:
- Read their primary works (books, essays, speeches)
- Identify 3–5 core mental models they use repeatedly
- Note their communication style and known biases
- Write the prompt using the template above

### Step 4: Run a Structured "Meeting" with a Specific Question

Don't ask vague questions like "What should I do?" Ask: "Should I raise a fund or stay independent, and why?"

Give context. Make it concrete. Let them argue with each other (if your AI tool supports multi-agent conversation) or run them sequentially and synthesize.

### Step 5: Synthesize, Don't Delegate — YOU Still Decide

The output is input. You're gathering perspectives, not outsourcing judgment.

Write down:
- What each persona said
- Where they disagreed and why
- What assumptions you held that were challenged
- What you're going to do and why

The decision is yours. The board just makes it better informed.

---

## Use Cases Beyond Strategy

This framework works for more than "big decisions." I use AI advisory boards for:

- **Hiring decisions** — "What would Jack Welch ask this candidate?"
- **Content creation** — "How would Paul Graham structure this essay?"
- **Negotiation prep** — "What would Chris Voss notice about this deal?"
- **Product decisions** — "What would Steve Jobs kill from this feature list?"

Any decision where you'd benefit from cognitive diversity.

---

## Conclusion

The best advisors don't give you answers. They give you better questions.

AI advisory boards give you access to the world's best question-askers, on demand, for free. The bottleneck was never access to wisdom — it was your willingness to hear what you don't want to hear.

Build your board. Let them argue. Then decide.

You'll still make mistakes. But you'll make different mistakes. And that's progress.

---

**Want the persona prompt templates?** Reply to this email and I'll send you the full set of prompts I use for Andreessen, Munger, Thiel, Naval, and Taleb.

**What thinkers would be on YOUR advisory board?** Hit reply and tell me. I'm curious.

---

*Florian Ziesche is building Ainary Ventures, a seed fund for AI-native companies. He was previously CEO of a funded AI startup and MD/COO at 36ZERO Vision. He writes about AI, venture capital, and compounding intelligence at [AI-Native Operator](https://substack.com).*

---

## Meta / Publishing Notes

**SEO Title:** I Built an AI Advisory Board (Marc Andreessen, Charlie Munger, Peter Thiel) — How You Can Too

**Meta Description:** How to build AI personas of the world's sharpest thinkers to stress-test your decisions. A framework for creating your own AI advisory board using prompt engineering and mental models.

**Substack Tags:** #AI #DecisionMaking #Startups #VentureCapital #MentalModels #ProductivityPrompt Engineering

**Estimated Reading Time:** 10 minutes

**Call-to-Action:**
1. Primary: "Reply for prompt templates"
2. Secondary: "Share this if you found it useful"
3. Tertiary: "Subscribe for weekly essays on AI-native thinking"

**Cross-Promotion Opportunities:**
- LinkedIn: Condensed 1,000-word version with "Full essay on Substack" CTA
- Twitter: Thread format (15 tweets) with key frameworks
- Repurpose: "5 Mental Models from My AI Advisory Board" follow-up post

**Publication Date Suggestion:** Monday morning (best engagement for long-form)

---

*Article completed: 2026-02-09 04:30 CET*
*Status: Publication-ready. Awaiting Florian's final review.*
*Next: VC job posting research*
