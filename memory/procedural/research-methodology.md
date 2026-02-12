# Research Methodology - Procedural Memory

**Purpose:** How to conduct research experiments and analyze complex topics (process knowledge)

---

## Multi-Lens Research Pattern

**Use Case:** Analyzing complex topics, large datasets, or strategic questions

**Method:**
1. **Define Question:** Clear research question or analysis task
2. **Select Lenses:** 5-6 different perspectives (personas)
   - Examples: VC Partner, Academic, Practitioner, Adversarial, McKinsey Consultant, Behavioral Scientist
3. **Parallel Execution:** Spawn agents simultaneously with same data, different lens
4. **Convergence Analysis:** What do ALL agents agree on? (high confidence)
5. **Divergence Mining:** What did only 1-2 agents find? (unique insights, potential blind spots)
6. **Synthesis:** Cross-cutting findings + recommendations

**Validated Examples (2026-02-10):**
- **Vault Gold (205 files, 5 lenses):** 5/5 convergence = "build statt send" problem, unique finds = Kill Fund, Andreas=Referral Engine, Mia=Product
- **SOTA Papers (31 papers, 6 lenses):** Universal laws discovered, novel patterns identified
- **CNC Calibration (10 agents, same task):** Persona variance quantified (3.4x), adversarial = best

**Cost:** ~$2-10 per experiment depending on data size

---

## Agent Calibration Experiments

**Use Case:** Testing how different prompting strategies affect output quality

**Method:**
1. **Define Task:** Specific estimation or judgment task with known ground truth (if available)
2. **Create Personas:** 10+ different agent personalities
   - Conservative: Controller, Risk Manager, Red Team
   - Expert: Domain Specialist, REFA Expert, Physiker
   - Other: Startup Founder, Ensemble, Abstraction Layer
3. **Run Parallel:** Same task, same data, different persona
4. **Measure Variance:** How much do estimates differ?
5. **Compare to Ground Truth:** Which personas were most accurate?
6. **Extract Learnings:** What patterns emerge?

**Key Finding (2026-02-10):**
- Loss-averse personas beat domain experts for estimates
- Adversarial self-correction: 15x improvement (Phase 1 → Phase 2)
- Average has systematic optimism bias (-29.5%)
- Persona creates 3.4x variance in estimates

**Next Level:** Run on 3 parts with REAL ground truth (not just our calculation)

---

## Convergence/Divergence Framework

**Convergence = High Confidence**
- When 4+ out of 5 agents agree → treat as validated finding
- Use for strategic decisions
- Example: All 5 agents said "Florian builds too much without sending"

**Divergence = Hidden Opportunities**
- When only 1-2 agents find something → investigate why
- Could be:
  - Persona bias (specific lens sees what others miss)
  - Random noise (agent hallucinated)
  - Hidden insight (others have blind spot)
- Don't ignore divergence — mine it!

**Implementation:**
- Track convergence rate (X/N agents)
- Flag unique findings from divergence
- Follow up: Why did only this agent see it?

---

## Research Synthesis Process

**For Large Paper Sets (20-50 papers):**

**Phase 1: Categorical Batching**
- Group papers by topic/category
- 1 agent per category (reads all papers in that category)
- Output: Category-level synthesis

**Phase 2: Cross-Paper Analysis**
- 1 agent reads ALL category syntheses
- Identifies cross-cutting patterns
- Output: Meta-synthesis

**Phase 3: Novel Findings Extraction**
- What did we discover that NO paper mentioned?
- What did papers miss?
- What's the gap in the research?

**Example (2026-02-10):**
- 31 papers → 6 categories → 6 agents → 1 cross-synthesis
- Result: 3 Universal Laws + Our Novel Findings (adversarial 15x, Γ-tracking, etc.)

---

## Ground Truth Validation

**Problem:** Our calculation isn't ground truth (661 min = our estimate, not Andreas' actual time)

**Solution:**
- Always caveat: "vs our estimate" not "vs reality"
- Seek real ground truth when possible (Andreas' Ist-Zeit after completion)
- Use validated test cases (3 demo parts with real machining times)

**Next Experiment:**
- Run same 10 agents on 3 parts WITH real Ist-Zeiten
- Verbindungsplatte S235JR = 12.5 min (REAL)
- Adapterplatte AlMg3 = 24.8 min (REAL)
- Block AlMg3 = 35.2 min (REAL)
→ 30 datapoints, proper calibration curve

---

## Experiment Documentation

**Directory Structure:**
```
experiments/
├── MANIFESTO.md             — Overall framework
├── agent-calibration/        — Persona variance experiments
│   ├── EXPERIMENT-PLAN.md
│   ├── results/agent-*.md
│   └── ANALYSIS-REPORT.md
├── vault-gold/              — Multi-lens vault analysis
│   └── results/lens-*.md
└── research-deep/           — SOTA paper synthesis
    └── results/category-*.md
```

**File Naming:**
- `lens-[persona].md` for multi-lens
- `agent-[letter]-[task].md` for calibration
- `category-[topic].md` for paper synthesis

---

## Cost Management

**Typical Costs:**
- Single agent task: $0.20-0.50
- Multi-lens (5 agents): $2-5
- Large synthesis (30+ papers): $10-15
- 100-agent experiment: $50-100

**Budget Rule:** Experiments should cost <1% of potential value created

**Example:** CNC calibration ($3) could save hours of manual estimation → ROI = 100x+

---

## When to Use Which Method

| Method | Use When | Cost | Time |
|--------|----------|------|------|
| Multi-Lens | Strategic decisions, vault analysis | $2-5 | 15-30 min |
| Agent Calibration | Testing estimation accuracy | $3-10 | 20-45 min |
| Research Synthesis | Large paper sets, literature review | $10-20 | 30-60 min |
| Single Agent | Routine research, small tasks | $0.50 | 5-15 min |

---

## Key Learnings (2026-02-10)

1. **Convergence Rate Matters:** 5/5 = act on it, 3/5 = investigate, 1/5 = flag but don't prioritize
2. **Adversarial = Calibration Tool:** Mandatory for estimates, not just QA
3. **Personas Create Real Variance:** 3.4x variance in CNC example (not just noise)
4. **Ground Truth is Rare:** Most "truth" is actually "best estimate" — caveat accordingly
5. **Experiments Compound:** Each one teaches method + domain (CNC + research methodology)
6. **Hidden Gems in Divergence:** Things only 1 agent finds = potential breakthroughs

---

**Last Updated:** 2026-02-10  
**Source:** Extracted from agent calibration, vault gold, and SOTA research experiments  
**Next Evolution:** Memory compounding experiment (M0-M5), reproducibility testing
