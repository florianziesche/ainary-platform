## Risks

Ainary's calibration infrastructure strategy faces four critical uncertainties that could derail market capture before EU standards crystallize in 2027-2028.

**Multi-agent composability remains unproven at scale.** Current evidence shows Conformal Uncertainty (ConU) failing to compose for multi-agent systems (CL-02), but no research demonstrates whether any calibration method can handle chains of 10+ agents making interdependent decisions. The technical challenge compounds: if Agent A has 85% calibrated confidence and passes to Agent B with 90% confidence, the joint confidence calculation lacks theoretical foundation. Without solving this, Ainary's IP may only address single-agent use cases—limiting addressable market by 60-70% as enterprises increasingly deploy agent swarms.

**RLHF damage shows inconsistent permanence patterns.** While research confirms some models suffer permanent calibration damage from RLHF alignment (CL-02), the predictive factors remain opaque. Model size, training data, and RLHF methodology all influence recoverability, but no systematic study maps these relationships. This creates deployment risk: Ainary might develop calibration methods that work on GPT-4 but fail on Claude or Gemini variants. Healthcare clients requiring 99.9% reliability cannot accept this uncertainty.

**Competitor positioning data shows dangerous gaps.** The absence of explicit calibration offerings from IBM, Microsoft, and Google could indicate either market neglect or stealth development. Without product announcements, API documentation, or patent filings as evidence, Ainary operates blind to potential competitive threats. A single announcement of "Azure Calibration Services" or "Vertex AI Confidence Suite" could eliminate first-mover advantage overnight. The $0.0005-0.015 per-check cost structure (CL-05) means cloud providers could subsidize calibration as a loss leader.

**EU regulatory timeline contains multiple failure points.** While the AI Act enforces in August 2026, CEN/CENELEC committee formation, stakeholder consultation, and draft standard development each introduce delays. Historical precedent from GDPR technical standards shows 6-18 month slippage is common. If standards don't crystallize until 2029, Ainary faces three years of uncertain investment before regulatory alignment becomes clear. Worse, early committee membership requires €50,000-100,000 annual commitment with no guarantee of influence.

The intersection of these risks creates a narrow success corridor. Technical solutions must handle multi-agent complexity while remaining model-agnostic. Market entry must anticipate competitor moves without confirmation. Regulatory influence requires upfront investment with delayed returns. Most critically, all three must align within the 12-24 month window—a timeline that assumes no black swan events like sudden open-source breakthroughs or accelerated EU standardization.

**For the decision maker:** Hedge bets by developing single-agent calibration IP first (proven market) while funding parallel research into multi-agent composability—but set a 6-month kill switch if technical progress stalls.

Section Confidence: 75%