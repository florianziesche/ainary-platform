# Capability Evolver — Daily Learnings

## 2026-03-06 (05:00 CET)

### External Scan
**OpenClaw v2026.3.2 (Mar 3):**
- ✅ PDF tool with native Anthropic+Google support — already using `pdf` tool, native support is incremental
- ✅ `sessions_spawn` attachments (base64/utf8, subagent-only) — could improve Research→Build pipeline (pass context files directly)
- ✅ Ollama embeddings for `memory_search` — alternative to OpenAI, cost-saving potential
- ⚠️ BREAKING: `tools.profile` defaults to `messaging` for new installs (broad coding tools opt-in only)
- ⚠️ BREAKING: ACP dispatch enabled by default

**AI Agent Workflows 2026:**
- **4 workflow categories** (StackAI): Single Agent / Hierarchical / Sequential Pipeline / Decentralized Swarm — we use Hierarchical (main orchestrates sub-agents)
- **Reflection+Iteration** (Dextralabs) — we have REFLECTION-PROTOCOL.md, but iteration loop missing
- **Agent Supervisors** (Deloitte) — humans at exception points = matches D-207 (Definition of Done)

### Internal Analysis (last 48h)

**Wins:**
- Research Network v2.0: Ontology Schema, Claim Extraction, Trust×Relevance scoring, Project Layer
- Quality Ladder visible: Fürth/Nürnberg (Gold) vs Base cities (~350 errors)
- Strategiewechsel documented: Send First → Best Agent Wins
- Palantir Deep Research structured (50 sources, 9 categories)

**Recurring Errors:**
1. **D-200 Violation (05.03. 18:48):** Sub-Agent spawned despite Single Agent Default (NON-NEGOTIABLE)
   - Root Cause: decisions.md not loaded by default
   - Fix: decisions.md → IMMER-laden-Liste (done per memory)
2. **Pre-Delivery Check missing (05.03. multiple):** "Würde Florian es akzeptieren?" in AGENTS.md, but not enforced
   - Current: Rule exists, no executable
   - Need: Pre-send validation step
3. **Vault noise (05.03. 22:00):** 12,623 ingested claims → 40 curated (99.7% noise)
   - Root Cause: Line-pattern-matching > LLM-extraction
   - Lesson: ingest-vault.js needs LLM rewrite

**Quantified Improvements (since 04.03.):**
- 3 cities: 557 ontology errors → 0 errors (Fürth/Nürnberg/Ottobrunn)
- Knowledge Graph: 4 reports, 55 claims, 15 enriched topics
- Trust Score: 25% multi-source claims, 89% avg trust
- Research→Schema→Build gap closed (ONTOLOGY.md v1.0, validate-ontology.js, extract-claims.js)

### Actionable Findings

**1. Iteration Loop Missing (NEW PATTERN)**
- We have Reflection (REFLECTION-PROTOCOL.md: 5 questions before delivery)
- Missing: Explicit iteration after DoD-Check fails
- Industry pattern: Planning → Execution → Reflection → **Iteration** → Ship
- **Recommendation:** Add to AGENTS.md Task Loop Step 3: "PRÜFEN: Beantwortet? Belegt? Nutzbar? → Nein = **Retry (max 2×)**, dann flag für Florian"

**2. sessions_spawn Attachments (NEW OPENCLAW FEATURE)**
- Can now pass files directly to sub-agents (base64/utf8)
- Use case: Research Report → pass markdown+sources → sub-agent extracts claims without re-reading
- **Recommendation:** Update SUB-AGENT-CONTEXT.md with attachment pattern (wenn Research Output >10KB → attach statt paste)

**3. Pre-Delivery Validation (ENFORCEMENT GAP)**
- Rule exists in AGENTS.md (Step 3 "Prüfen")
- Not enforced programmatically
- **Recommendation:** `scripts/pre-delivery-check.js` — runs before `message(action=send)`:
  - Frage beantwortet? (LLM self-audit)
  - Externe Zahlen belegt? (regex check for unverified claims)
  - Sofort nutzbar? (confidence ≥ threshold)

### No Action Needed
- OpenClaw features are incremental (PDF native support, Ollama embeddings)
- AI agent workflow patterns align with existing architecture (we're already Hierarchical + Reflection)
- Last 48h work quality high: 0 ontology errors on 3 cities, Research Network shipped

### Summary
**3 actionable improvements identified:**
1. Iteration Loop (add to AGENTS.md Task Loop)
2. sessions_spawn attachments pattern (update SUB-AGENT-CONTEXT.md)
3. Pre-Delivery Validation script (create scripts/pre-delivery-check.js)

**No critical bugs. No breaking patterns. System stable.**

---
*Next scan: 2026-03-07 05:00 CET*
