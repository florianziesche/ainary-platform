# Formulas — Ainary Execution Platform

**Version:** 0.12.5 | **Date:** 2026-02-19

> Mathematical reference for all scoring, ranking, and updating algorithms.
> See also: [DOCUMENTATION.md](DOCUMENTATION.md) · [DB-SCHEMA.md](DB-SCHEMA.md) · [ARCHITECTURE.md](ARCHITECTURE.md)

---

## 1. Bayesian Trust Update (Per-Skill)

**Location:** `app.py` → `POST /api/trust/skills/{skill}/feedback`

### Formula

```
observed_score = 100 × up / (up + down × 1.5)
bayesian_score = (C × prior + observed_score × n) / (C + n)
```

### Parameters

| Symbol | Value | Meaning |
|--------|-------|---------|
| C | 10 | Confidence parameter — how many data points before the prior is overwhelmed |
| prior | 50 | Neutral starting score for new skills |
| up | varies | Count of positive feedback events |
| down | varies | Count of negative feedback events |
| n | up + down | Total feedback count |
| 1.5 | fixed | Asymmetric penalty multiplier for mistakes |

### Example Calculation

Skill "email" has 8 ups and 4 downs:

```
observed_score = 100 × 8 / (8 + 4 × 1.5) = 100 × 8 / 14 = 57.14
n = 12
bayesian_score = (10 × 50 + 57.14 × 12) / (10 + 12) = (500 + 685.7) / 22 = 53.9 → 54
```

### Rationale

- **Why Bayesian, not linear (+2/-3):** Linear scoring is noisy — one bad result after 10 good ones causes a disproportionate drop. Bayesian scoring converges smoothly: high-data-point skills are stable, low-data-point skills stay near the prior.
- **Why asymmetric (1.5× penalty):** In a trust system, false negatives (trusting bad output) are costlier than false positives (being too cautious). The 1.5× multiplier ensures mistakes cost 50% more than successes earn.
- **Why C=10:** Balances between being too sensitive to early data (C=2) and too slow to learn (C=50). With C=10, the system needs ~10 data points before the prior influence drops below 50%.
- **Why prior=50:** Neutral start. New skills don't start trusted (100) or distrusted (0) — they earn their position.

### Graduated Autonomy Thresholds

| Score | Level | Behavior |
|-------|-------|----------|
| 0–29 | CONFIRM | Output hidden until pre-flight passes |
| 30–59 | REVIEW | Output visible with badges |
| 60–79 | AUTO | Direct output, background pre-flight |
| 80+ | DELEGATED | Multi-step without confirmation |

---

## 2. Compound Score

**Location:** `app.py` → `_calc_compound_score()`

### Formula

```
compound_score = confidence × (usage + connections) × relevance
```

Where:

```
usage = |systems| × 3.0 + |content| × 1.0 + |revenue| × 5.0
connections = (|supports| + |contradicts|) × 0.5
relevance = exp(-0.693 × age_days / half_life)
```

### Parameters

| Symbol | Meaning |
|--------|---------|
| confidence | Finding confidence (0.0–1.0) |
| \|systems\| | Number of systems using this finding |
| \|content\| | Number of content pieces using this finding |
| \|revenue\| | Number of revenue applications using this finding |
| \|supports\| | Number of findings this supports |
| \|contradicts\| | Number of findings this contradicts |
| age_days | Days since finding creation |
| half_life | Decay period in days (varies by tag) |

### Half-Life by Tag

| Tag | Half-Life | Rationale |
|-----|-----------|-----------|
| ai_technology | 90 days | AI landscape changes rapidly |
| market_data | 180 days | Market data has medium shelf life |
| business_model | 360 days | Business models are relatively stable |
| personal_fact | ∞ (no decay) | Personal facts don't expire |
| (default) | 365 days | Conservative default |

### Example Calculation

Finding RF-042: confidence=0.75, used in 2 systems + 1 content + 1 revenue, supports 2 others, 30 days old, tagged "ai_technology":

```
usage = 2×3.0 + 1×1.0 + 1×5.0 = 12.0
connections = (2 + 0) × 0.5 = 1.0
relevance = exp(-0.693 × 30 / 90) = exp(-0.231) = 0.794
compound_score = 0.75 × (12.0 + 1.0) × 0.794 = 0.75 × 13.0 × 0.794 = 7.74
```

### Rationale

- **Revenue weighted 5×:** Findings that directly impact revenue are the most valuable in an execution platform.
- **Systems weighted 3×:** Technical findings that affect multiple systems compound value.
- **Exponential decay:** Knowledge has a half-life. AI technology findings lose relevance faster than business fundamentals.
- **Connections add value:** Findings that support or contradict other findings are more interconnected and valuable to the knowledge graph.

---

## 3. Pre-Flight Scoring (3-Layer Engine)

**Location:** `app.py` → `GET /api/preflight/{topic_id}`

### Layer 1: Regex Pattern Matching

```
For each active correction with patterns:
  For each regex pattern:
    matches = re.findall(pattern, output_text, IGNORECASE)
    if matches → status = "fail"

Fallback (no patterns): simple substring match on 'wrong' field
  wrong_terms = split(correction.wrong, ',')
  if any term in output_text → status = "fail" (severity≥2) or "warn" (severity<2)
```

**Cost:** <50ms | **Deterministic:** Yes

### Layer 2: Structural Validators

Output-type-specific rules:

| Output Type | Check | Threshold | Status |
|-------------|-------|-----------|--------|
| email | Has greeting | `^(hi|hello|hallo|dear|sehr geehrte)` | warn |
| email | Has sign-off | `(best|regards|grüße|florian)$` | warn |
| email | Length | 20–500 words | warn |
| linkedin | Character limit | ≤3000 chars | fail |
| linkedin | Has CTA | `(\?|comment|share|thoughts?)` | warn |
| blog | Minimum length | ≥300 words | warn |
| blog | Has headings | `^#{1,3}\s` at >200 words | warn |
| report | Has sources | `(source|https?://|\[\d+\])` | warn |
| report | Numbers with sources | `\d{2,}\s*%` without sources | fail |
| website | Brand colors only | Non-brand hex codes | fail |
| (all) | Not empty | >0 words | fail |
| (all) | Minimum length | ≥5 words | warn |

**Cost:** <100ms | **Deterministic:** Yes

### Layer 2b: Standards Check

```
For each quality_standard where output_type matches:
  status = "pass" if output_text exists, else "warn"
```

### Layer 3: LLM-as-Judge (Planned)

```
Only activated for REVIEW/CONFIRM guardrail levels.
LLM checks output against top corrections semantically.
Not yet implemented.
```

**Cost:** 2–3s | **Deterministic:** No

### Overall Score

```
overall = "pass"  if failed == 0 AND warned == 0
          "warn"  if failed == 0 AND warned > 0
          "fail"  if failed > 0
```

### Rationale

- **3 layers by cost:** L1 is free and catches 80%. L2 catches structural issues. L3 is expensive — only for low-trust situations.
- **Output-type filtering:** Email corrections don't apply to blog posts. Reduces false positives.
- **Deterministic by default:** L1 and L2 don't use AI — reproducible, instant, offline-capable.

---

## 4. Daily Standup Scoring

**Location:** `app.py` → `PUT /api/standup/recalc`

### Formula

```
score = 100 (base)
  + Σ(committed tasks done) × 2
  - Σ(committed tasks missed) × 3
  + Σ(extra tasks done) × 2
  + Σ(sends) × 1

EMA = 0.3 × today_score + 0.7 × yesterday_ema
```

### Point Values

| Event | Points | Rationale |
|-------|--------|-----------|
| Committed task done | +2 | Reward for keeping commitments |
| Committed task missed | -3 | Asymmetric: broken commitments cost more |
| Extra task done | +2 | Bonus work rewarded equally |
| Send action (email/application) | +1 | Sends are high-value outputs |
| Base (daily reset) | 100 | Neutral starting point |

### EMA (Exponential Moving Average)

```
α = 0.3 (smoothing factor for ~7-day effective window)
EMA_today = α × score_today + (1 - α) × EMA_yesterday
```

### Example

Day with 3 committed tasks (2 done, 1 missed), 1 extra task, 1 send:

```
score = 100 + (2 × 2) - (1 × 3) + (1 × 2) + (1 × 1) = 100 + 4 - 3 + 2 + 1 = 104
EMA = 0.3 × 104 + 0.7 × 98.5 = 31.2 + 68.95 = 100.15
```

### Rationale

- **Asymmetric penalties (-3 vs +2):** Missing a commitment is worse than completing one is good. Encourages realistic commitments.
- **EMA smoothing (α=0.3):** One bad day doesn't tank the trend. Conversely, one great day doesn't mask a pattern of misses. The 7-day effective window shows recent trajectory.
- **Sends bonus (+1):** Sends (emails, applications) are the most valuable output type — they directly create pipeline.

---

## 5. Topic Auto-Prioritization

**Location:** `app.py` → `POST /api/topics/auto-prioritize`

### Formula

```
score = 0
  + (30 if meta.potential exists)         # Factor 1: Revenue potential
  + (35 if deadline ≤ 3 days)             # Factor 2: Deadline proximity
  + (25 if deadline ≤ 7 days)
  + (15 if deadline ≤ 14 days)
  + stage_score                            # Factor 3: Stage weight
  + (20 if revenue stage AND progress < 50%) # Factor 4: Sends pending
  - (10 if last_updated > 7 days ago)     # Factor 5: Staleness penalty

priority = NOW   if score ≥ 60
           HIGH  if score ≥ 35
           NORMAL if score ≥ 15
           LOW   otherwise

confidence = (factors_with_data / 5) × 100%
```

### Stage Weights

| Stage | Score | Rationale |
|-------|-------|-----------|
| revenue | 20 | Closest to output/money |
| content | 15 | Creates pipeline |
| systems | 10 | Enables other stages |
| research | 5 | Foundational but less urgent |

### Rationale

- **5 factors, equal consideration:** Each factor contributes independently. Confidence reflects how many factors have data.
- **Deadline dominates:** A 3-day deadline (+35) outweighs most other factors because time-sensitive tasks must be done regardless of other metrics.
- **Staleness penalty:** Topics untouched for >7 days are likely deprioritized naturally — the algorithm reflects this.
- **Revenue stage bonus:** Topics in the revenue stage with <50% progress represent unrealized value.

---

## 6. Finding Confidence (Bayesian Updating with Source Weights)

**Location:** `app.py` → `POST /api/findings/{finding_id}/validate`

### Formula (Bayes' Theorem)

```
P(H|E) = P(E|H) × P(H) / [P(E|H) × P(H) + P(E|¬H) × P(¬H)]
```

**If evidence supports the finding:**
```
P(E|H) = reliability    (reliable source likely gives supporting evidence if H true)
P(E|¬H) = 1 - reliability
```

**If evidence contradicts the finding:**
```
P(E|H) = 1 - reliability    (contradicting evidence unlikely if H true)
P(E|¬H) = reliability
```

### Source Reliability Weights

| Source Type | Reliability | Rationale |
|-------------|-------------|-----------|
| own_hypothesis | 0.40 | Unvalidated personal theory |
| conversation | 0.50 | Casual signal, not rigorous |
| linkedin_poll | 0.55 | Self-selected audience bias |
| industry_report | 0.75 | Professional research with methodology |
| own_data | 0.80 | First-party data is strong |
| academic_paper | 0.85 | Peer-reviewed with methodology |
| revenue_validated | 0.90 | Market validated — strongest signal |
| human_verified | 0.90 | Used for verify endpoint |

### Example Calculation

Finding RF-015 has confidence 0.60. An industry report (reliability=0.75) supports it:

```
P(H) = 0.60 (prior)
P(E|H) = 0.75 (likelihood if true)
P(E|¬H) = 0.25 (likelihood if false)

P(H|E) = (0.75 × 0.60) / (0.75 × 0.60 + 0.25 × 0.40)
        = 0.45 / (0.45 + 0.10)
        = 0.45 / 0.55
        = 0.818 → 0.82
```

Same finding, but a conversation (reliability=0.50) contradicts it:

```
P(E|H) = 1 - 0.50 = 0.50
P(E|¬H) = 0.50

P(H|E) = (0.50 × 0.82) / (0.50 × 0.82 + 0.50 × 0.18)
        = 0.41 / (0.41 + 0.09)
        = 0.41 / 0.50
        = 0.82 → 0.82 (conversation barely moves high-confidence findings)
```

### Clamping

```
new_confidence = max(0.02, min(0.98, calculated))
```

Prevents hard 0.0 or 1.0 — even high-confidence findings remain sensitive to strong contradictory evidence.

### Auto-Status Transition

```
if new_confidence < 0.20 AND status == 'alive':
    status → 'contested'
```

### Rationale

- **Proper Bayesian:** Unlike simple +/- adjustments, Bayesian updating correctly accounts for prior knowledge. A high-confidence finding barely moves from weak contradictory evidence.
- **Source-weighted:** An academic paper moves confidence more than a casual conversation. This reflects real-world evidence quality.
- **Clamping at 0.02/0.98:** Prevents certainty traps. Even a 0.98 finding can be challenged by strong evidence.
- **Automatic contestation:** Findings dropping below 20% confidence are flagged for review, not silently degraded.

---

## 7. Evidence Gate (Stage Promotion)

**Location:** `app.py` → `GET /api/findings/{finding_id}/gate`

### Gate Requirements

| Current Stage | Min Confidence | Evidence Types | Min Sources | Next Stage |
|---------------|---------------|----------------|-------------|------------|
| research | ≥60% | E, I, J, A | ≥1 | systems |
| systems | ≥70% | E, I | ≥2 | content |
| content | ≥80% | E, I | ≥2 | revenue |

### Evidence Type Codes

| Code | Meaning |
|------|---------|
| E | Empirical (own data, experiments) |
| I | Industry (reports, benchmarks) |
| J | Journalistic (news, articles) |
| A | Anecdotal (conversations, observations) |

### Rationale

- **Progressive thresholds:** Each stage requires higher confidence because the cost of acting on wrong findings increases as they move toward revenue.
- **Evidence type narrowing:** Research accepts anecdotal evidence (A). Revenue stage requires empirical (E) or industry (I) — hard data only.
- **Source count increasing:** Multiple independent sources reduce the chance of systematic bias.

---

*6 core formulas + 1 gate system. All implemented in app.py.*
