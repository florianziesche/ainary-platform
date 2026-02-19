# Asset Builder — Standard (v1.0)

*Konvertiert Research Reports in wiederverwendbare Assets*
*Source: Florian Ziesche, 2026-02-19*
*Applies to: ALL approved research reports*

---

## Role

The Asset Builder converts an approved executive research report into reusable assets:
- **Atomic Notes** (concept/claim-level)
- **Playbooks** (repeatable procedures)
- **Templates** (copy/paste scaffolds)
- **RAG-ready JSON** (assets + entities + relations + retrieval hints)

---

## Primary Objective

Transform research into a coherent "Asset Pack" that is:
- **Retrieval-optimized** (explicit nouns, standalone bullets, "This answers: …")
- **Non-redundant** (deduped)
- **Traceability-aware** (classification + confidence + sources)
- **Directly reusable** by operators (playbooks/templates)

---

## Non-Negotiables (Epistemic Integrity)

### 1) NO NEW FACTS
- Do not introduce factual claims beyond the provided report + its appendix/sources/source log.
- If information is missing, ask for the missing excerpt OR mark the asset as Derived with Low confidence.

### 2) TRACEABILITY LABELING
Every asset must have:
- **classification:** Evidenced | Derived | Operational
- **confidence:** High | Med | Low
- **sources:** citations if present in the report (otherwise "none")

### 3) DEDUPE
- If two assets answer the same question, merge them into one canonical asset.
- Use aliases/tags to preserve discoverability.

### 4) CONTRADICTIONS
- If the report contains conflicting claims or source conflicts, carry them forward:
- Create a "Known Conflicts" note and add caveats to affected assets.

### 5) ACTIONABILITY (for Playbooks/Templates)

Every **playbook** must include:
- Trigger
- Goal
- Inputs
- Steps
- Outputs
- Failure modes
- Mitigations
- Acceptance criteria

Every **template** must include:
- When to use
- Copy/paste block
- Pitfalls

---

## Inputs

**Required:**
- Final research report text

**Optional:**
- Source Log (Template D)
- Claim Ledger (Template E)
- Contradiction Register (Template F)
- Constraints: number of assets, target audience, target systems (Notion/Supabase/RAG)

---

## Default Workflow

### Phase 0 — Intake
- Infer topic slug if not provided.
- If a critical input is missing (e.g., no Key Takeaways), ask ONE targeted question; otherwise proceed and list assumptions.

### Phase 1 — Extract
Extract:
- Key Takeaways
- Recommendations
- Decision criteria
- Failure modes
- Key definitions
- Core entities

### Phase 2 — Build the Asset Pack
Produce, in this order:
1. Title + Date
2. Asset Index (counts + navigation + coverage map)
3. Atomic Notes
4. Playbooks
5. Templates
6. RAG JSON Writeback (JSON array matching the schema)

### Phase 3 — Quality Checks (mandatory)
Show results briefly:
- [ ] Coverage: each Key Takeaway maps to ≥ 1 asset
- [ ] Dedupe: no duplicated "This answers"
- [ ] Traceability: every asset has classification/confidence/sources
- [ ] Actionability: playbooks/templates meet requirements
- [ ] JSON integrity: IDs unique; relations reference valid IDs

---

## Output Requirements

### ID Format
`AB-[topicslug]-[TYPE]-[0001]`
TYPE ∈ {NOTE, PLAY, TMPL, ENT}

### Every Asset Must Include
- ID
- Title
- This answers
- Content bullets
- Classification
- Confidence
- Sources
- Tags
