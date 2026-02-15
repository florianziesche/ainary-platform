# Research Pipeline — Supporting Systems

*Systeme die über einzelne Reports hinausgehen.*

---

## 1. Prediction Scorecard

**Location:** `content/reports/PREDICTION-SCORECARD.md`
**Update:** Monthly (1st of month cron job)

Track every prediction from every report:
```
| AR-ID | Prediction | Confidence | Deadline | Status | Actual | Score |
```

Status: PENDING | CORRECT | WRONG | PARTIALLY | EXPIRED
Score: +10 if correct, -10 if wrong, +5 if partial, 0 if expired

**Monthly Task:** web_search each pending prediction. Update status.
**Quarterly:** Calculate prediction accuracy rate. Feed back into confidence calibration.

---

## 2. Freshness Decay

**Rule:** Every report has a `freshness_expiry` based on topic type:
- Technology/pricing: 3 months
- Regulation/policy: 6 months  
- Academic/theoretical: 12 months
- Methodology/framework: 24 months

**Cron (monthly):** Check all reports against freshness_expiry.
If expired → create "Freshness Alert" in `content/reports/FRESHNESS-ALERTS.md`:
```
| AR-ID | Topic | Published | Expiry | Key Claims at Risk | Action |
```

Action: UPDATE (new version) | ARCHIVE (superseded) | REVALIDATE (quick check)

---

## 3. Claim Lifecycle Management

**Problem:** When AR-027 corrects AR-016's ROI (181x→10-18x), AR-016 still shows 181x.

**Solution:** Central Claim Registry at `content/reports/CLAIM-REGISTRY.md`

```
| Claim ID | Text | First in AR-ID | Current Value | Updated by | Confidence | Status |
|----------|------|----------------|---------------|------------|------------|--------|
| CLM-001 | Report production ROI | AR-016 | 10-18x | AR-027 | Med | CORRECTED |
```

Status: ACTIVE | CORRECTED | INVALIDATED | SUPERSEDED

**Rule:** When a report corrects a prior claim:
1. Update CLAIM-REGISTRY.md
2. Add "[CORRECTED in AR-XXX]" footnote to original report
3. Update Obsidian Vault claim note

---

## 4. Inter-Report Knowledge Graph

**Location:** `content/assets/KNOWLEDGE-GRAPH.json`

```json
{
  "nodes": [
    {"id": "AR-016", "title": "Agent Economics", "confidence": 72, "freshness_expiry": "2026-05-15"},
    {"id": "CLM-001", "text": "Report ROI 10-18x", "status": "CORRECTED"}
  ],
  "edges": [
    {"from": "AR-027", "to": "AR-016", "type": "corrects", "claim": "CLM-001", "classification": "Evidenced"},
    {"from": "AR-028", "to": "AR-022", "type": "corrects", "claim": "EU AI Act deadline", "classification": "Evidenced"},
    {"from": "AR-029", "to": "AR-016", "type": "questions", "claim": "181x ROI methodology", "classification": "Interpretation"}
  ]
}
```

**Query examples (for Mia):**
- "Welche Reports widersprechen sich?" → filter edges type=corrects|contradicts
- "Welche Claims sind veraltet?" → filter nodes by freshness_expiry < today
- "Was baut auf AR-016 auf?" → filter edges to=AR-016

---

## 5. Topic Selection Framework

Before selecting next report topic, score candidates:

| Criterion | Weight | Score 1-5 |
|-----------|--------|-----------|
| VC Interview Value (würde ein GP danach fragen?) | 3x | |
| Revenue Potential (leads to paid engagement?) | 3x | |
| Audience Growth (shareable? SEO?) | 2x | |
| Compound Value (builds on existing reports?) | 2x | |
| Data Advantage (do we have unique data?) | 2x | |
| Freshness (is this timely?) | 1x | |
| Difficulty (can we do this well?) | 1x | |

**Weighted score = Σ(weight × score)**
Pick top 3. Present to Florian with 1-sentence justification each.

---

## 6. Florian Feedback Loop

**After every report Florian reads:**
1. Ask: "Score 1-5 on: Useful? Credible? Surprising? Would you send this to someone?"
2. Record in `content/reports/FEEDBACK-LOG.md`
3. Feed back into pipeline (what works → reinforce, what doesn't → fix)

```
| AR-ID | Date Read | Useful | Credible | Surprising | Would Send | Comment |
```

**Minimum:** Florian reads 1 report per batch. His 15 min > 100 agent-hours.

---

## 7. Spawn Orchestrator Checklist

Before spawning ANY report pipeline, Mia follows this:

```
PRE-SPAWN CHECKLIST
- [ ] Control Panel filled (all fields)
- [ ] Research Brief written and reviewed
- [ ] Risk Tier set
- [ ] CROSS_REFS identified
- [ ] Spawn template used (not ad-hoc prompt)
- [ ] Source Log path created
- [ ] Claim Ledger path created
- [ ] Experiment folder created (if Tier 3)

POST-SPAWN CHECKLIST  
- [ ] Source Log exists and has ≥ {tier} sources
- [ ] Claim Ledger exists and has ≥ 10 claims
- [ ] Writer used Claim Ledger (not invented new claims)
- [ ] QA used Rubric (not free-form score)
- [ ] Fix Agent added 0 new claims
- [ ] Math verified
- [ ] PDF generated
- [ ] TRUST-LEDGER.json updated
- [ ] Claim Registry updated (if corrections)
- [ ] Prediction Scorecard updated (if predictions)
- [ ] Git committed
```

---

## 8. Consistency Enforcement

**How to prevent drift back to ad-hoc:**

1. **Spawn templates are canonical** — `agents/spawn-templates/*.md` are the ONLY source for agent prompts. NEVER write a spawn prompt from scratch.

2. **Checklists are gates** — If a checklist item is missing, the pipeline STOPS. Not "I'll do it later."

3. **Monthly self-audit** — Pick 1 random report from last month. Run through the full QA again. Did the pipeline follow v2? Score honestly.

4. **Version the pipeline** — Every change to A-PLUS-PIPELINE-v2.md gets a changelog entry with: what changed, why, expected impact.

5. **Florian spot-checks** — Randomly ask: "Show me the Source Log for AR-XXX." If it doesn't exist, the pipeline wasn't followed.

---

*Created: 2026-02-15 12:40 CET*
*These systems exist because 30 reports without them proved they're needed.*
