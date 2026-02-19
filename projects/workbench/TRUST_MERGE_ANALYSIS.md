# Trust System Merge Analysis
**Date:** 2026-02-19  
**Task:** Merge trust_scores (legacy) → trust_skills (single source of truth)  
**Codebase:** /projects/workbench/backend/app.py (4117 LOC)

---

## Executive Summary

Two redundant trust systems exist:
1. **trust_scores** — Agent-level, simple up/down voting (LEGACY)
2. **trust_skills** — Skill-level, Bayesian scoring (CURRENT, more granular)

**Decision:** Deprecate trust_scores, redirect all references to trust_skills.

---

## System Comparison

| Feature | trust_scores | trust_skills |
|---------|--------------|--------------|
| Granularity | Agent-level (main, writer, etc.) | Skill-level (research, email, cv, etc.) |
| Algorithm | Simple increment/decrement | Bayesian (C=10, PRIOR=50, asymmetric) |
| Vote weighting | up +1, down -2 | up +1, down weighted ×1.5 |
| Endpoints | GET /api/trust | GET /api/trust/skills, POST /api/trust/skills/{skill}/feedback |
| Created | Earlier (legacy) | Later (current) |
| Usage in code | 7 references | 15+ references |
| Dashboard | Not used | Used in stats, context |

**Verdict:** trust_skills is more sophisticated and already the primary system.

---

## Code References

### trust_scores (7 occurrences)

| Line | Type | Code | Purpose |
|------|------|------|---------|
| 191 | Table Schema | `CREATE TABLE IF NOT EXISTS trust_scores` | DB definition |
| 535 | Seed | `INSERT OR IGNORE INTO trust_scores (agent, score) VALUES (?, ?)` | Initialize agents |
| 1047 | Vote up | `UPDATE trust_scores SET up_votes = up_votes + 1, ... score = MIN(100, score + 1)` | Legacy voting |
| 1049 | Vote down | `UPDATE trust_scores SET down_votes = down_votes + 1, ... score = MAX(0, score - 2)` | Legacy voting |
| 1118 | GET endpoint | `SELECT * FROM trust_scores ORDER BY agent` | GET /api/trust |
| 3304 | **Aliasing** | `context["trust_scores"] = {t['skill']: t['score'] for t in trust_skills}` | **Already redirected!** |
| 3317 | Log output | `- Trust Scores: {json.dumps(context.get('trust_scores', {}))}` | Logging |

### trust_skills (16 occurrences)

| Line | Type | Code | Purpose |
|------|------|------|---------|
| 248 | Table Schema | `CREATE TABLE IF NOT EXISTS trust_skills` | DB definition |
| 531 | Seed | `INSERT OR IGNORE INTO trust_skills (skill, score) VALUES (?,?)` | Initialize skills |
| 1412 | Dashboard stats | `SELECT score FROM trust_skills` | Dashboard calculation |
| 1428 | Active agents count | `SELECT COUNT(*) FROM trust_skills WHERE updated_at >= date('now','-7 days')` | Activity metric |
| 1429 | Total agents count | `SELECT COUNT(*) FROM trust_skills` | Total metric |
| 1441 | Skill query | `SELECT skill, score, updated_at FROM trust_skills WHERE skill IN (...)` | Filtered query |
| 2588 | GET endpoint | `@app.get("/api/trust/skills")` | API definition |
| 2591 | GET query | `SELECT * FROM trust_skills ORDER BY skill` | Fetch all skills |
| 2596 | POST endpoint | `@app.post("/api/trust/skills/{skill}/feedback")` | Feedback API |
| 2606 | Upsert check | `SELECT * FROM trust_skills WHERE skill = ?` | Check existence |
| 2608 | Insert new | `INSERT INTO trust_skills (skill, score, total, up, down) VALUES (?,50,0,0,0)` | Create skill |
| 2618 | Increment up | `UPDATE trust_skills SET up = up + 1, total = total + 1` | Positive feedback |
| 2620 | Increment down | `UPDATE trust_skills SET down = down + 1, total = total + 1` | Negative feedback |
| 2625 | Bayesian calc | `SELECT up, down, total FROM trust_skills WHERE skill = ?` | Fetch for scoring |
| 2635 | Update score | `UPDATE trust_skills SET score = ?` | Write Bayesian score |
| 2863 | Context query | `SELECT skill, score FROM trust_skills ORDER BY score DESC` | Context building |
| 3301 | Context query | `SELECT skill, score FROM trust_skills ORDER BY score DESC` | Context building |

---

## Critical Finding: Already Partially Migrated!

**Line 3304:**
```python
context["trust_scores"] = {t['skill']: t['score'] for t in trust_skills}
```

**This shows trust_skills is ALREADY being used as the source for "trust_scores" in some contexts!**

The system is in an inconsistent state:
- Old vote endpoint (line 1047-1049) still updates trust_scores table
- Context building (line 3304) reads from trust_skills but labels it trust_scores
- Dashboard uses trust_skills (lines 1412+)

---

## Migration Strategy

### Phase 1: Deprecation (No Data Loss)
1. Mark GET /api/trust as deprecated (return warning header)
2. Redirect legacy vote updates to trust_skills with skill="main"
3. Keep trust_scores table (archive-only, don't drop)

### Phase 2: Code Changes
1. Change vote endpoint (lines 1047-1049) to update trust_skills instead
2. Update GET /api/trust to aggregate from trust_skills
3. Fix line 3304 naming (already uses trust_skills, just mislabeled)

### Phase 3: Data Migration
- **No migration needed** — trust_skills is already populated and primary
- Optional: Export trust_scores history for archival

### Phase 4: Cleanup
- Remove trust_scores seeding (line 535)
- Update DB-SCHEMA.md to mark trust_scores as deprecated
- Add deprecation notice in GET /api/trust response

---

## Impact Analysis

### Breaking Changes
- **GET /api/trust** structure changes from agent-level to skill-level
  - Old: `[{agent: "main", score: 8, ...}, ...]`
  - New: `[{skill: "research", score: 65, ...}, ...]`
  - **Mitigation:** Add deprecation warning, keep endpoint alive with transformed data

### Non-Breaking Changes
- Vote endpoint can stay the same, just target trust_skills internally
- Dashboard already uses trust_skills (no change needed)
- Context building (line 3304) already uses trust_skills

### Zero-Risk Areas
- trust_skills endpoints unchanged
- Bayesian scoring logic unchanged
- Dashboard stats unchanged

---

## Migration Script Requirements

1. **Backup:** `cp workbench.db workbench.db.bak`
2. **Archive trust_scores:** Export to JSON
3. **No table drops:** Keep trust_scores for rollback safety
4. **No data writes:** trust_skills is already current

---

## Recommendations

1. **DO NOT drop trust_scores table** — archive it
2. **Deprecate, don't break:** Keep GET /api/trust alive with warning
3. **Vote redirect:** Map legacy votes to skill="main" in trust_skills
4. **Document:** Clear CHANGELOG entry on what changed
5. **Test:** Verify dashboard, votes, context building still work

---

## Next Steps

1. ✅ Analysis complete
2. ⏳ Create migration script (backup + archive)
3. ⏳ Update app.py (deprecate, redirect)
4. ⏳ Update DB-SCHEMA.md
5. ⏳ Test endpoints
6. ⏳ Git commit
7. ⏳ CHANGELOG entry

---

**Confidence:** 95% — Code review complete, migration path clear.  
**Risk:** LOW — No data deletion, endpoints stay alive, trust_skills already primary.
