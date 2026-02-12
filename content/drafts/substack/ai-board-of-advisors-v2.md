# I Built an AI Board of Advisors (And They Argue Like the Real Thing)

Last week, I asked 100 AI agents to design their own evolution.

The finding: **cognitive diversity beats individual intelligence.** When agents with different reasoning styles collaborated, they outperformed any single "smarter" model.

So I tested it on myself.

Last Tuesday, I put Marc Andreessen, Charlie Munger, and Peter Thiel in a room to argue about whether I should raise a venture fund or bootstrap. They weren't physically there. Two don't know I exist. One is dead.

But for 45 minutes, they tore into fund economics, incentive structures, and contrarian insight with brutal honesty.

Munger called the 2/20 fee structure *"a triumph of salesmanship over arithmetic."*

Andreessen countered that platform effects from a fund brand compound in ways a solo operator can't replicate.

Thiel rejected the framing entirely: *"The question isn't fund versus independent. The question is: what do you know that nobody else knows?"*

I learned more from that simulated argument than from three months of real advisor calls.

Here's why it works.

---

## Why Real Advisors Hold Back (And AI Doesn't)

Real advisors are constrained by politeness.

They soften feedback to preserve the relationship. They lead with validation and bury the concern in a compliment sandwich. You leave the meeting feeling good when you should leave feeling challenged.

They're busy. You get 30 minutes every quarter. That's enough for surface-level guidance, not deep thinking.

Here's the structural problem nobody talks about: **once someone agrees to advise you, the threshold for disagreement rises.** Social alignment means they're more likely to validate your direction than fundamentally challenge it.

AI advisors have no relationship to protect.

They'll tell you your idea is stupid the moment they think it. That's the feature, not the bug.

---

## Why These Three

I chose Andreessen, Munger, and Thiel because they map directly to the cognitive diversity findings from my agent research.

| Advisor | Role | Mental Model | Bias |
|---------|------|--------------|------|
| **Charlie Munger** | Adversarial Reasoning / Red Team | Inversion: "How would I guarantee failure?" | Excessive conservatism |
| **Peter Thiel** | First Principles / Contrarian | "What truth do few people agree on?" | Overvaluing disagreement itself |
| **Marc Andreessen** | Systems Thinking / Optimist | "Software eats the world" | Underweighting human resistance |

The magic isn't any one perspective.

It's the **tension** between them.

When Andreessen says "the market is massive," Munger asks "what's the incentive structure?" and Thiel asks "if it's so obvious, why hasn't someone already won?"

That three-way tension generates better thinking than any single advisor ever could.

---

## The Knowledge Architecture That Makes It Work

Here's where most people get AI advisors wrong.

The naive approach: dump all of Munger's books into a vector database (RAG). When you ask a question, the AI retrieves relevant chunks and synthesizes an answer.

This creates a *well-read* advisor. It knows what Munger said about incentives, what Thiel said about monopolies, what Andreessen said about network effects.

But it's shallow.

It retrieves facts, not thinking patterns.

What I built instead is a **hierarchical knowledge structure:**

```
Mental Models (Core reasoning frameworks)
  ↓
Reasoning Patterns (How to apply them)
  ↓
Examples (Specific cases from their work)
  ↓
Known Biases (Where they overweight/underweight)
```

This doesn't just store *what* they said. It encodes *how* they think.

For Munger: inversion as a top-level model, then the pattern of "ask what would guarantee failure," then examples like Coca-Cola and See's Candies, then the bias toward conservation of existing structures.

For Thiel: the contrarian question as top-level model, then the pattern of "identify the secret no one else sees," then examples like PayPal and Palantir, then the bias toward valuing disagreement itself.

**The difference in output quality is dramatic.**

RAG gives you a persona that can *quote* the thinker. Hierarchical structure gives you a persona that *reasons* like the thinker.

Think about it: embeddings capture semantic similarity but not causal reasoning chains. The hierarchical approach pre-computes the reasoning structure. The AI doesn't retrieve random relevant chunks — it follows the actual cognitive path.

**Key Insight:** It's the difference between giving someone a library card versus teaching them how to think.

---

## Sample Board Meeting: "Should I Raise a VC Fund?"

I presented my situation: former CEO, technical AI background, deciding between raising a $5-10M seed fund or operating independently.

Here's what happened.

**Marc Andreessen:**

*"The fund. Platform effects compound. When you have a fund brand, you get inbound deal flow you'd never see as an independent. Your network becomes the product. You write one check, you're a customer. You write 20 checks, you're a platform."*

**Charlie Munger:**

*"Marc's argument is precisely the kind of thinking that gets people in trouble. What's the incentive structure? A 2% management fee on $10 million is $200K per year before you've returned a penny to LPs. The fee structure is designed to enrich the GP even if returns are mediocre. Ask yourself: would you invest in a fund with these economics if you were the LP?"*

**Peter Thiel:**

*"You're both missing the point. Marc, platform effects are real, but they're also commodity. Every emerging manager pitches 'unique network access.' Charlie, you're right about incentives, but you're underweighting the reputational forcing function — if the fund fails, you can't hide. The real question is: what does Florian know that the market doesn't? If the answer is 'I can spot AI companies better,' that's not a secret — that's a claim."*

**Me:**

"The insight is that AI-native companies will be built differently. Most VCs evaluate them using SaaS metrics — ARR, CAC, churn — but those metrics break when your product is a 24/7 autonomous agent. I've built these systems. Most VCs haven't."

**Munger:**

*"Is that true? Or is it something you want to be true because it justifies the fund? Here's the inversion test: assume you're wrong. Assume AI-native companies will be evaluated the same way as SaaS. What happens to your thesis? If it collapses, you don't have a thesis — you have a hope."*

**Thiel:**

*"If the edge lasts 18 months, you don't need a fund. You need speed. Fund formation takes 6-12 months. By the time you've closed, half your edge is gone. The independent operator can move faster. Do you want to be a fund manager or deploy capital into AI-native companies? Those aren't the same goal."*

No consensus. No resolution.

Three radically different lenses on the same decision.

That's exactly what I needed.

**Practical Takeaway:** The goal isn't agreement. It's seeing your blind spots from multiple angles. The hardest pushback is the most valuable — it's the question you're avoiding.

---

## Beyond Arguments: What I Actually Use Them For

The fund debate makes for a good story. But the board earns its keep in the mundane decisions — the ones where you don't realize you need a second opinion.

**Outcome Measurement.** I spent a week building an elaborate knowledge management system. 7 folders, dashboards, templates. I was proud of it. Then I ran it through the board.

Munger: *"You're measuring activity, not outcomes. Where are the kill criteria? If this system doesn't produce a paying customer in 14 days, it's a toy."* Graham was blunter: *"Overengineered. Zero customers. 10 phone calls would teach you more than 7 folders."* Gil: *"You've built a Phase 3 system for a Phase 0 company. Focus on your first €1,000."*

The consensus was unanimous and painful: **too much built, too little sold.**

I didn't want to hear it. That's how I knew it was valuable.

**Reorganizing How I Work.** After that feedback, I restructured my entire workflow. Not based on what felt productive, but based on what the board's frameworks predicted would actually generate results. Thiel's "pick ONE thing and monopolize" became my daily filter. Andreessen's "5 real users in 7 days" became my shipping deadline. Hoffman's "first customer → reference → flywheel" became my sales strategy.

The board didn't just help me make one decision. It changed how I make all decisions.

---

## What Surprised Me

**They push back harder than real advisors.** Munger will call your idea stupid. Thiel will question your premises. When Munger asked *"is this true or do you want it to be true?"* — I felt it. That's the question a friend won't ask.

**The process itself clarifies thinking.** Constructing the personas forces you to understand *how* great thinkers think, not just *what* they think. That cognitive transfer is the real value.

---

## Build Your Own (3 Steps)

### 1. Identify Your Blind Spots

Where do you consistently make mistakes? What decisions do you avoid?

For me: I overweight novelty, underweight execution, avoid financial modeling.

So I need personas who are conservative (Munger), execution-focused, and financially rigorous.

### 2. Pick Thinkers Who Challenge Those Blind Spots

Don't pick people you agree with.

Pick people who think differently **in the specific dimensions where you're weak.**

Risk-averse? Add Musk. Reckless? Add Munger. Too abstract? Add an operator like Ben Horowitz.

### 3. Build the Knowledge Hierarchy

For each thinker:
- Read their primary works (books, essays, speeches)
- Identify 3-5 core mental models they use repeatedly
- Map their reasoning patterns (how they apply those models)
- Note communication style and known biases

Then structure it hierarchically: Mental Models → Reasoning Patterns → Examples → Biases.

**Here's the constraint:** The quality ceiling is your understanding. You can only build personas as sophisticated as your comprehension of their thinking.

If you've only read the Wikipedia summary of "Zero to One," your Thiel persona will be shallow.

Do the work.

---

## The Limits

Let me be clear about what this is and isn't.

AI personas are simulacra, not oracles. They're based on public output, not private thinking. They can't account for new information the real person would have. They hallucinate occasionally.

**They're best for stress-testing, not deciding.**

The personas help you see blind spots and challenge assumptions. But the decision is still yours. Always.

There's an "illusion of authority" risk. It's easy to treat the AI's output as gospel because it's wearing the mask of someone you respect.

Remember: this is a thinking tool, not a substitute for judgment.

Use this with humility. It's a mirror, not a guru.

---

## Conclusion

The best advisors don't give you answers.

They give you better questions.

AI advisory boards give you access to the world's best question-askers, on demand, for free. The bottleneck was never access to wisdom.

It was your willingness to hear what you don't want to hear.

Build your board. Let them argue. Then decide.

You'll still make mistakes.

But you'll make *different* mistakes.

And that's progress.

---

## Why This Matters More Than You Think

This isn't just a productivity hack. It's a preview of something bigger.

A smarter model doesn't make your board smarter. **A better architecture does.** Recent research backs this up: structured knowledge retrieval — hierarchical graphs instead of flat vector search — reduces hallucinations by up to 50% compared to naive RAG (Xu et al., 2024; KG-RAG, Nature 2025). Hierarchical architectures are also 90% cheaper to scale because you pre-compute reasoning structures once instead of retrieving and re-processing on every query.

The implication: the quality of your AI advisor isn't a function of the model's intelligence. It's a function of how you organize what it knows.

Now extrapolate.

**Will every startup have its own AI board of advisors?** Probably. Within two years, I'd guess most serious founders will run major decisions through some version of this. The ones who build better knowledge architectures will get better advice. Competitive advantage shifts from "who do you know" to "how well did you build your advisory system."

**What about AI employees managing people?** That's already happening. Agent economics — the emerging field of how autonomous AI agents create, capture, and distribute value — is being built right now. We're not talking about chatbots answering support tickets. We're talking about AI agents that allocate budgets, set priorities, evaluate performance, and make resource decisions. The management layer of companies is about to get very interesting.

**Will AI manage humans?** Some already do. The question isn't whether, but how well — and whether the humans being managed trust the system. Which brings us full circle: transparency beats performance. The AI manager that shows its reasoning will be accepted. The black-box optimizer will be resisted, even if it's technically better.

The future will be interesting. And it's only day one.

---

**Want the prompt templates?** Reply to this email and I'll send you the full hierarchical knowledge structure I use for Munger, Thiel, and Andreessen.

**Read last week's experiment:** [I Asked 100 AI Agents to Design Their Own Evolution](https://finitematter.substack.com) — what happens when 100 agents answer the same question, and why cognitive diversity matters more than individual intelligence.

---

*Florian Ziesche is building Ainary Ventures. He writes at Finite Matters on Substack.*