# MOONSHOT v5 — SYNTHESIS: Deduplicated & Prioritized Findings
**Generated:** 2026-02-19 | **Source:** Batch 1 (Red Team, Empiricist, Formalist) + Batch 2 (Practitioner, Writer, Ethicist)

---

## Deduplicated Finding Table

| # | Finding | Severity | Agents | Action for v5 |
|---|---------|----------|--------|----------------|
| 1 | "84% overconfidence" figure unverifiable from corpus | CRITICAL | Empiricist | Add caveat: "widely cited but primary source not independently verified in our corpus" |
| 2 | "Provably wrong" (multiplicative confidence) is tautological, not a proof | MAJOR | Formalist, Red Team | Replace with "mathematically inconsistent under positive correlation" |
| 3 | Section 5 correlation theory not integrated into Section 6 architecture (fixed thresholds ignore correlation) | MAJOR | Red Team | Add correlation-adjusted threshold guidance in architecture section |
| 4 | Complacency paradox math misleading; ignores intelligent routing | MAJOR | Red Team, Ethicist | Reframe with Tier 3 selective prediction context |
| 5 | $0.005 in Key Numbers contradicts $0.0005-0.015 range in body | MAJOR | Empiricist | Update Key Numbers to range |
| 6 | 42.9% BaseCal ECE reduction unverifiable | MAJOR | Empiricist | Label as "per preprint abstract, not peer-reviewed" |
| 7 | Section 2.8 "Formal Bounds" are conceptual, not formal | MAJOR | Formalist | Rename to "Conceptual Model" |
| 8 | "Monday Morning" framing is fictional — only 3/10 steps doable tomorrow | MAJOR | Practitioner, Writer | Rename to "10-Step Calibration Roadmap (6-12 Weeks)" |
| 9 | No "Do Not Deploy If" framework | MAJOR | Ethicist | Add explicit 5-scenario framework |
| 10 | Multi-agent propagation is novel contribution but buried in Section 5 | MAJOR | Writer | Move earlier in report structure |
| 11 | Step 4 (Deploy Consistency) has critical implementation gaps | MAJOR | Practitioner | Add API choice, semantic clustering, caching guidance |
| 12 | Conformal prediction composability unsolved for multi-agent — should be blocker, not footnote | MAJOR | Practitioner, Formalist | Flag as "single-step only" until composability solved |
| 13 | "First practical architecture" overstated | MINOR | Red Team | Soften to "a production-oriented integration guide" |
| 14 | $755K legal damage figure unsourced | MINOR | Red Team | Label as "author estimate including reputational damage" |
| 15 | "Destroys calibration" overstates regime-dependent finding | MINOR | Red Team | Change to "Damages" |
| 16 | 46% Amazon ensemble reduction — industry source, not peer-reviewed | MINOR | Empiricist | Label as industry publication |
| 17 | rho=0.036 unverifiable | MINOR | Empiricist | Low priority, keep with caveat |
| 18 | CP n>=200 oversimplified (theoretical min is ~10) | MINOR | Formalist | Add theoretical vs practical distinction |
| 19 | Two-agent formula doesn't scale without distributional assumptions | MINOR | Formalist | Add caveat about exchangeability |
| 20 | "Best ECE on GAIA" ambiguous | MINOR | Formalist | Specify direction |
| 21 | Exec Summary fails 2-min test for non-experts (ECE undefined, RLHF unexplained) | MINOR | Writer | Define ECE inline, rephrase RLHF |
| 22 | Section 2 and Section 3 redundant (method families + decision tree) | MINOR | Writer | Merge decision tree into method comparison |
| 23 | Fairness section acknowledges gap but offers no go/no-go guidance | MINOR | Ethicist | Add to "Do Not Deploy If" |
| 24 | Prompt injection can inflate calibration scores — not addressed in architecture | MINOR | Practitioner, Ethicist | Add defense: separate confidence estimation from generation |
| 25 | Calibration regression testing missing from checklist | MINOR | Practitioner | Add as implementation step |
| 26 | Latency analysis superficial — no app-type breakdown | MINOR | Practitioner | Add latency table by application type |

---

## Priority Actions for v5

**P0 (Must fix — credibility at stake):**
1. 84% overconfidence caveat (#1)
2. "Provably wrong" → "mathematically inconsistent" (#2)
3. Cost range fix in Key Numbers (#5)
4. "Do Not Deploy If" framework (#9)

**P1 (Should fix — quality improvement):**
5. Restructure: multi-agent propagation earlier (#10)
6. Rename "Monday Morning" → honest timeline (#8)
7. Integrate correlation into architecture thresholds (#3)
8. Reframe complacency paradox (#4)
9. Rename Section 2.8 "Formal Bounds" → "Conceptual Model" (#7)

**P2 (Nice to have — polish):**
10. All MINOR items (#13-26)

---

## New CRTs Proposed (all batches)

| ID | Claim | Confidence | Source |
|----|-------|------------|--------|
| CT-028 | Fixed thresholds inappropriate for correlated multi-agent chains | 80% | RT-2 |
| CT-029 | Headline numbers rely on papers outside verification corpus | 75% | EM audit |
| CT-030 | ECE not formally decomposable into epistemic + aleatoric | 85% | FM-2 |
| CT-031 | "Provably wrong under correlation" is tautological | 90% | FM-1 |
| CT-032 | Prompt injection can inflate confidence scores | 83% | Ethicist |
| CT-033 | Deploying calibration without fairness verification may violate EU AI Act Art. 10 | 75% | Ethicist |
| CT-034 | Well-calibrated AI may increase error rates if vigilance drops below break-even | 70% | Ethicist |
