# Woche 4 — Evolution Experiment Results
*2026-02-17 | Question: High-Stakes Human-AI Decision-Making*

## Question
**"How should a human-AI pair make high-stakes decisions together — when should the AI lead, when should it defer, and how do they calibrate trust?"**

## Status
- 10 Groups spawned (A-J)
- 3 complete responses: G (Constraint), I (Systems), J (Random Mutation/Jazz)
- 6 substantial partials (terminated before completion): A, B, C, E, F, G2
- 2 failed: D (Adversarial), H (Narrative)
- Note: First run used `cleanup=delete`, losing results. Second run had timeout issues.

## Group Scores (based on available content)

| Group | Strategy | Originality | Actionability | Depth | Coherence | Surprise | Total |
|-------|----------|------------|--------------|-------|-----------|---------|-------|
| A | First Principles | 7 | 7 | 8 | 8 | 6 | 36 |
| B | Inversion | 8 | 7 | 8 | 8 | 8 | 39 |
| C | Analogical | 9 | 7 | 8 | 9 | 9 | 42 |
| E | Quantitative | 8 | 9 | 8 | 7 | 7 | 39 |
| F | Socratic | 8 | 7 | 9 | 8 | 8 | 40 |
| G | Constraint | 7 | 9 | 6 | 8 | 7 | 37 |
| I | Systems | 9 | 10 | 9 | 9 | 8 | 45 |
| J | Random Mutation | 9 | 9 | 9 | 9 | 10 | 46 |

### 🏆 Winner: Group J (Random Mutation — Jazz Improvisation, 46/50)
### 🥈 Runner-up: Group I (Systems — Three-Axis Framework, 45/50)

## Key Ideas Per Group

### A — First Principles
- 3 Axioms: Information ≠ knowledge ≠ wisdom; Consequences exist only in human reality; All decisions are probabilistic bets
- AI should propose, never impose — human holds veto because they bear consequences
- Novel situations require human lead; data-rich + reversible = AI can lead

### B — Inversion (Failure Modes)
- **Abdication Spiral**: Human rubber-stamps AI → misses context-specific anomalies
- **False Deference Loop**: AI punts everything → human abandons the partnership
- **Calibration Illusion**: Early wins on medium stakes → overconfidence on true high stakes
- **Accountability Vacuum**: Neither party owns failures → trust erodes permanently

### C — Analogical (Biology/Physics/History)
- **Gut-Brain Axis**: Complementary incompetencies — gut leads on pattern recognition, brain overrides with context
- **Apollo 13**: Computer calculates constraints (what's possible), humans choose between options (values + risk tolerance)
- **Roman Dual Consul**: Structured asymmetry — deliberation in peacetime, decisive authority in crisis with time limits

### E — Quantitative
- **Calibrated Confidence (CC)**: ≥85% → AI leads; <70% → AI defers; 70-85% → joint
- **Reversibility Cost Ratio (RCR)**: Cost to reverse / Cost of decision → determines authority level
- **Domain Expertise Gap (DEG)**: AI training examples / Human experience hours
- Composite AI Leadership Score formula: ALS = (CC×0.4) + ((1/RCR)×30) + (log10(DEG)×0.3)

### F — Socratic
- High-stakes = irreversibility + asymmetric downside + value-laden trade-offs → can't A/B test
- Trust calibration isn't "score: 73%" — it's domain-specific: "I trust AI on X-type problems but not Y-type"
- Humans have "skin-in-the-game wisdom" — judgment born from having previously been wrong
- Lead vs. defer is a false binary — it's a spectrum of collaborative modes

### G — Constraint (500 words)
- **Complementary Asymmetry**: AI leads on pattern recognition, human leads on ethics + irreversibility
- **Contrarian**: "Stop asking who decides" — redesign decisions to be lower-stakes through better information flow
- **Collaborative decision decomposition** > delegation: What can be measured? (AI) What are we optimizing for? (Human)
- Protocol: 15-min Decision Audit tomorrow

### I — Systems (Complete, 2300 words) ⭐
- **Three-Axis Framework**: Reversibility × Legibility × Consequence Asymmetry
- **Legibility insight**: "Black box confident" more dangerous than "transparent uncertain"
- **Trust as a surface, not a point**: AI doesn't have one trustworthiness level — it has a trustworthiness surface across decision-space
- **Confidence-Commitment Contract**: Domain-specific threshold table updated monthly
- **Red Team Swap**: Weekly mutual model-building through structured disagreement

### J — Random Mutation / Jazz (Complete, 1400 words) ⭐
- **Jazz Comping metaphor**: Not "who decides" but "who's soloing and is the other comping well?"
- **Mortality Constraint**: "Decide as if the AI will die in 6 months" — forces human capability growth
- **Comp Switch Ritual**: Explicit phrases for real-time leadership handoff ("Take the solo" / "I'm comping")
- **Ensemble performance > negotiation**: Leadership flows to whoever serves the decision quality in that moment
- **Pre-Decision Audit**: Both parties answer structured questions to determine who leads

## Operational Issues
- `cleanup=delete` on sub-agents loses results before parent can read them → always use `cleanup=keep`
- Sub-agents with long outputs get terminated by timeout → need longer timeouts or explicit file-writing instructions
- Duplicate announce notifications for Group G (from first run's cached session)
