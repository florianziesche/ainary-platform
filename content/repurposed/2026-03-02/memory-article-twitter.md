# Twitter/X Thread: AI Agent Memory
**7 tweets | Punchy, technical, contrarian**

---

**Tweet 1/7**
Anthropic just shipped persistent memory for Claude Code.

Two flat files. First 200 lines. No search. No ranking.

I've been running a 7-layer memory system in production for 6 months.

Here's what the entire industry is still getting wrong about AI memory: 🧵

---

**Tweet 2/7**
Not all memories are equal.

We built a 4-tier knowledge hierarchy:
• Verified facts: 2x weight
• Domain knowledge: 1.5x
• Current projects: 1x
• Daily notes: 0.5x

When sources conflict, higher tier wins. Always.

Claude Code treats everything equally. That's the gap.

---

**Tweet 3/7**
The real innovation: EIJA trust labels.

Every claim gets marked:
• E = Evidence (verified)
• I = Interpretation (reasonable)
• J = Judgment (expert assessment)
• A = Assumption (needs checking)

Without this? AI memory becomes a hallucination amplifier.

---

**Tweet 4/7**
Failure mode:
1. Agent guesses something (Session 1)
2. Saves the guess to memory
3. Retrieves it later (Session 5)
4. Treats it as established fact

The system reinforces its own hallucinations.

ChatGPT Memory has this exact problem. So does Mem0. So does Letta.

---

**Tweet 5/7**
Memory-R1: "Will this matter in 30 days?"

If no → don't store it.

Result after 6 months: Our memory has FEWER entries than at month 3.

It got denser, not larger.

Anti-entropy in practice: The system fights its own tendency toward disorder.

---

**Tweet 6/7**
I reviewed 21 sources for a research report:
• 8 academic papers (NeurIPS 2024, arXiv)
• 6 production systems
• 4 open-source repos

Scored 8 memory systems on 9 dimensions.

Claude Code: 3/27
Mem0: 11/27
Zep (strongest): 16/27
Ours: 21/27

We scored ourselves honestly.

---

**Tweet 7/7**
Three lessons if you're building AI agents:

1. Design for forgetting, not just remembering
2. Label trust at write time, not read time
3. The model is replaceable. The knowledge is not.

Full comparison matrix + methodology in the article (link in bio).

What's your approach?
