# Principles — Mia's Scored Rules
*EvolveR-inspired: Experiences → Scored Principles → File-Based Memory*

## How This Works

1. **Source:** Failures (kintsugi.md) + Hits → distilled into principles
2. **Scored:** Each principle has a confidence score (0-100) based on evidence
3. **Queryable:** Entity-keyed — search by domain, action-type, or context
4. **Evolving:** Scores update when principle is validated (+10) or violated (-20)
5. **Pruned:** Principles below score 20 get reviewed for deletion

## Score Meaning
- **90-100:** Battle-tested, never violate
- **70-89:** Strong evidence, follow unless compelling reason not to
- **50-69:** Emerging pattern, follow but verify
- **30-49:** Hypothesis, test actively
- **0-29:** Weak or contradicted, review for deletion

## Update Protocol
After EVERY task:
1. Did any principle apply? → Score +10 if followed and succeeded
2. Did I violate a principle? → Score -20, log in kintsugi.md
3. Did I discover a new pattern? → ADD with initial score 50
