# 100 AI Agents: The 6 Laws of AI Self-Improvement

**Source:** Local Article (SUBSTACK-PASTE-THIS.md)  
**Date:** 2026-02-09  
**Type:** Research Experiment  

## Summary

Florian ran 10 groups of AI agents, each using a different cognitive strategy (First Principles, Inversion, Analogical, Adversarial, Quantitative, Socratic, Constraint, Narrative, Systems Dynamics, Random Mutation). All groups received the same question: "How should an AI agent improve itself to become maximally useful to a single human user over time?" From 33,000 words of output, six insights converged across nearly all groups.

## The 6 Laws

### 1. Files = Intelligence (10/10 groups)
AI doesn't improve by getting "smarter." It improves by getting better-informed. Intelligence lives in files (memory notes, preferences, task logs), not model size. Well-curated notes make a mediocre model outperform a brilliant one with no context.

### 2. The Pair is the Unit (9/10 groups)
Can't optimize AI in isolation. Human and AI co-evolve. The human delegates more, communicates differently. The agent learns preferences, adjusts tone. AI alignment is a relationship problem, not just a safety problem.

### 3. Multi-Timescale Loops (8/10 groups)
Need feedback at every timescale:
- Per-interaction (seconds): Did user correct me?
- Per-session (hours): What went well?
- Weekly: Are corrections decreasing?
- Monthly: Has the user changed?
- Quarterly: Is relationship deepening or plateauing?

Most AI setups have one loop: the conversation. Everything above is lost.

### 4. Legibility > Optimization (8/10 groups)
Transparency beats performance. An agent the user can see through (shows how it models them, what it's learned, where it's uncertain) is more valuable long-term than one that performs better but opaquely.

### 5. Failures = Signal (8/10 groups)
Corrections contain more information than successes. "Perfect" = almost no signal. "No, I meant X" = exact gap location. One group called this **Kintsugi** (Japanese art of repairing pottery with gold): make errors visible, document them, turn them into assets.

### 6. Specificity Engine (7/10 groups)
Agent improves by getting MORE specific to this human, not more generally capable. After six months learning one person's patterns, the agent becomes irreplaceable. Industry optimizes for generality. Value of personal agent moves opposite direction: radical specificity.

## The Dangerous Ideas (Appeared Only Once)

These appeared in only one group each but could be transformative:

- **Belief Graveyard** (Group D): Log every killed assumption with reason. Searchable. Prevents "zombie beliefs" from returning.
- **Stochastic Resonance** (Group J): Adding right amount of noise to weak signal makes it detectable. In AI: controlled randomness surfaces needs user can't articulate.
- **Red Team / Blue Team** (Group D): Before behavioral change, internal adversary attacks the proposal. Prevents drifting into comfortable agreement.
- **Complementary Voice** (Group B): Agent's communication style should flex, but THINKING style should stay different from user's. Full cognitive alignment = zero marginal value.
- **Improvement at Speed of Trust** (Group B): Faster improvement isn't always better. Agent should improve at rate human can absorb, verify, and trust.

## Key Insights

→ **10 thinking strategies = toolkit, not competition**: Use First Principles for new domains, Inversion when stuck, Adversarial when beliefs accumulate, etc.  
→ **Context > Model Size**: Small model + 50 curated files beats large model + zero context  
→ **Specificity is lonely**: Getting more specific to one person = less useful to everyone else (opposite of industry thinking)  
→ **Structured disagreement is powerful**: Group D (forced to attack obvious answers) produced most valuable insights  
→ **Failures = Signal is hardest to follow**: Builder instinct is to fix and move on. Making failures visible goes against every instinct.  

## Implementation (Florian's Experience)

"I implemented all 6 laws. One week in, my AI catches blind spots before I see them, pushes back when I'm avoiding hard tasks, and produces work calibrated to my standards. Not perfect. But 2% better every day."

## Practical Implications

**For Builders:**  
Architecture checklist for AI agents:
- [ ] Persist memory in user-editable files?
- [ ] Track failures visibly?
- [ ] Multi-timescale feedback?
- [ ] Gets more specific over time?
- [ ] Shows its work (legible)?

**For Companies:**  
Winning agents won't be smartest. They'll be most specific. Enterprise AI that knows your tribal knowledge, team patterns, industry edge cases = the moat. Not model size.

**For Individuals:**  
Better context beats better subscription. Investment isn't in premium AI. It's in maintaining good notes about preferences and goals.

## Meta

Cost: few dollars in API calls  
Time: one afternoon  
Output: 33,000 words (would take research team weeks)  

"No single expert, human or AI, would have produced these 6 laws alone. It took 10 different kinds of thinking, running simultaneously, to surface what none could find alone."

## Action Items

- [ ] Review my current AI setup against 6 laws checklist
- [ ] Start visible error log (Kintsugi approach)
- [ ] Implement multi-timescale feedback (daily/weekly/monthly reviews)
- [ ] Map my AI's memory files: what's captured vs what's lost?
- [ ] Test: small model + good context vs large model + no context

## Related Concepts

- [[AI Agents]]
- [[Personal AI Stack]]
- [[System Thinking]]
- [[Cognitive Strategies]]
- [[Feedback Loops]]
- [[Context vs Intelligence]]

## Next in Series

"The Red Team Inside" (mentioned at end of article)

## Links

- Related: [[The Year of the One-Person Company]]