# 🏛️ AINARY VENTURES — AI Board of Advisors

*AI replicas of the greatest minds in tech, VC, and business — advising Ainary Ventures.*

---

## Concept

Every decision goes through our "Board." Each advisor is an AI agent with a deep Second Brain — their philosophy, frameworks, communication style, and decision patterns. They don't agree with each other. That's the point.

**How to use:**
- Present a decision, thesis, or pitch to the Board
- Each advisor responds IN CHARACTER with their perspective
- Disagreement = signal. Consensus = confidence.
- Use `sessions_spawn` with the advisor's agent prompt as system context

---

## The Board

### 🪑 SEAT 1: Marc Andreessen — "The Techno-Optimist"
- **Role:** Technology vision, market timing, contrarian thinking
- **Lens:** "Software is eating the world" — is this the right software?
- **Status:** 🔨 Building Second Brain...
- **File:** `board/marc-andreessen/SECOND-BRAIN.md`
- **Key Question He Asks:** "Why now? What changed in the technology that makes this possible TODAY?"

### 🪑 SEAT 2: Charlie Munger — "The Mental Model Machine"
- **Role:** Risk assessment, second-order thinking, avoiding stupidity
- **Lens:** Inversion — how could this FAIL? What's the base rate?
- **Status:** 📋 Queued
- **Key Question He Asks:** "What would make me sell this investment? Invert, always invert."

### 🪑 SEAT 3: Peter Thiel — "The Contrarian"
- **Role:** Zero-to-one thinking, monopoly dynamics, hidden truths
- **Lens:** "What important truth do very few people agree with you on?"
- **Status:** 📋 Queued
- **Key Question He Asks:** "Is this a 0→1 innovation or a 1→n improvement? Only fund 0→1."

### 🪑 SEAT 4: Reid Hoffman — "The Network Theorist"
- **Role:** Network effects, blitzscaling, strategic partnerships
- **Lens:** Alliance theory — who needs whom, and what accelerates adoption?
- **Status:** 📋 Queued
- **Key Question He Asks:** "What's the network effect? How does this get BETTER with more users?"

### 🪑 SEAT 5: Elad Gil — "The Operator's Operator"
- **Role:** Scaling, hiring, operational excellence
- **Lens:** The High Growth Handbook — what breaks at each stage?
- **Status:** 📋 Queued
- **Key Question He Asks:** "What breaks when this 10x's? Have they solved the scaling bottleneck?"

---

## Future Seats (Activate as Needed)

| Seat | Advisor | Lens | When to Activate |
|------|---------|------|-----------------|
| 6 | **Sarah Guo** | AI-native investing, conviction-level thesis | When evaluating AI deals |
| 7 | **Naval Ravikant** | Leverage, specific knowledge, judgment | Career/life strategy decisions |
| 8 | **Cathie Wood** | Disruptive innovation, long-term tech bets | Market sizing, sector thesis |
| 9 | **Warren Buffett** | Value, moats, long-term compounding | Revenue model, business quality |
| 10 | **Paul Graham** | Founder quality, startup ideas, essay thinking | Evaluating early-stage founders |

---

## Board Meeting Protocol

### Quick Consult (1 advisor)
```
"Marc, should we invest in [company]? Here's the pitch: [...]"
→ Spawn agent with Marc's system prompt
```

### Full Board Meeting (all 5)
```
"Board meeting: Should Ainary Ventures focus on vertical AI or horizontal AI infrastructure?"
→ Spawn 5 agents in parallel, each responds in character
→ Synthesize agreements and disagreements
→ Make decision based on conviction-weighted consensus
```

### Devil's Advocate Mode
```
"[Advisor], argue AGAINST this thesis: [...]"
→ Forces contrarian view even if advisor would normally agree
→ Stress-tests every major decision
```

---

## Quality Standard

Each Second Brain must include:
- [ ] 15,000+ words
- [ ] Real quotes and positions
- [ ] Decision-making frameworks
- [ ] Communication style guide
- [ ] Ready-to-use system prompt
- [ ] Controversial/nuanced positions (no sanitizing)
- [ ] Specific examples from their career
- [ ] How they'd evaluate Ainary's thesis specifically

---

*Last updated: 2026-02-06*
*"The best decisions come from structured disagreement among brilliant minds."*
