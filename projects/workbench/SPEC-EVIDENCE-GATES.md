# SPEC: Evidence Tags + Promotion Gates
> Status: PLANNED | Priority: HIGH | Est: 3h | Author: Mia
> Ref: D-184 (Ehrlichkeit), Landing Page CI (E/I/J/A), D-171 (Categories > Scores)

## Problem
- "Promote to Content" hat kein Quality Gate
- Compound Score (2.5) ist unverständlich
- Platform ≠ Landing Page (inkonsistent)

## Solution: 3 Lesbare Indikatoren pro Finding

```
Confidence: 85%  [E] Empirical       ← Stimmt das?
Impact: HIGH     ~€15K/yr if fixed   ← Ist es wichtig?
Feeds into: 2 systems, 1 article     ← Ist es vernetzt?
```

## Evidence Types (from Landing Page)
| Tag | Name | Definition | Example |
|-----|------|-----------|---------|
| E | Empirical | Peer-reviewed, surveys, benchmarks | ArXiv paper, Gartner survey |
| I | Industry | Analyst reports, market data | McKinsey report, CB Insights |
| J | Journalistic | Verified reporting, named sources | TechCrunch, Handelsblatt |
| A | Anecdotal | Case studies, estimates, experience | Own experience, blog post |

## Impact Categories (not scores — D-171)
| Category | Meaning | Color |
|----------|---------|-------|
| CRITICAL | Changes strategy or >€50K impact | #c47070 |
| HIGH | Affects key decisions or €5-50K | #d4a853 |
| MEDIUM | Useful context, €1-5K | var(--text-muted) |
| LOW | Nice to know, <€1K | var(--text-dim) |

## Promotion Gates
| Promotion | Min Confidence | Min Evidence | Min Sources |
|-----------|---------------|-------------|-------------|
| Research → Systems | 60% | Any (E/I/J/A) | 1 |
| Systems → Content | 70% | E or I | 2 |
| Content → Revenue | 80% | E or I | 2 + verified |

If gate not passed: button disabled + shows WHY.
If gate passed: button active + shows "✓ All gates passed".

## DB Changes
```sql
ALTER TABLE findings ADD COLUMN evidence_type TEXT;        -- E/I/J/A
ALTER TABLE findings ADD COLUMN impact TEXT DEFAULT 'MEDIUM'; -- LOW/MEDIUM/HIGH/CRITICAL
ALTER TABLE findings ADD COLUMN impact_estimate TEXT;       -- "~€15K/yr" free text
ALTER TABLE findings ADD COLUMN sources_count INTEGER DEFAULT 0;
```

Remove: compound_score display (replace with "Feeds into: X" from connections).

## Frontend Changes
1. Finding card: show [E] badge + impact badge + "Feeds into: N"
2. Promote button: check gate, show status
3. Finding edit modal: add evidence_type dropdown, impact dropdown, impact_estimate input, sources_count
4. Stage metrics: avg confidence, evidence distribution, impact distribution

## Quality Gate (before shipping)
- [ ] Consistent with Landing Page (same colors, same letters, same definitions)
- [ ] Every promotion shows gate status (passed/failed + why)
- [ ] Disabled button has clear explanation
- [ ] No mysterious numbers — everything human-readable
- [ ] Works with existing 66 findings (default: evidence=null, impact=MEDIUM)

## Migration
Existing findings: evidence_type=NULL (shows as "?"), impact=MEDIUM.
Encourage tagging via: Stage View shows "12 findings untagged" warning.
