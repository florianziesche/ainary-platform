# MIA Pipeline — Complete Specification (v1.1)

*Date: 2026-02-19 · Author: Florian Ziesche & MIA · Status: Ready for first run*

## Canonical Sources (ChatGPT Exec Research Factory)

These files are the authoritative standards. Every prompt in this pipeline
MUST be consistent with them. If a conflict exists, these win.

| File | Location | What it defines |
|------|----------|----------------|
| ERF System Prompt v2 | `standards/ERF-SYSTEM-PROMPT-v2.md` | Producer: 5 phases, epistemic integrity, E/I/J separation |
| ERF Reviewer Prompt v1 | `standards/ERF-REVIEWER-PROMPT-v1.md` | Reviewer: rubric 0-16, claim audit, contradiction scan, fix requests |
| ERF Templates A-J | `standards/ERF-TEMPLATES.md` | Template A (Intake), B (Brief), C (Report), D (Source Log), E (Claim Ledger), F (Contradiction Register), G (Reviewer Rubric), H (Repair Pass), I (Injection Tests), J (Canonical Prompts) |
| ERF Eval Pack | `standards/ERF-EVAL-PACK.md` | 6 regression tests (ER-01 to ER-06), tier thresholds |
| ERF Source Log Template | `standards/ERF-SOURCE-LOG-TEMPLATE.md` | Blank source log per report |
| ERF Prompt Registry | `standards/ERF-PROMPT-REGISTRY.md` | Version control for prompts |
| ERF Changelog | `standards/ERF-CHANGELOG.md` | Audit trail |
| AB System Prompt v1 | `standards/ASSET-BUILDER-SYSTEM-PROMPT.md` | Asset Builder: no new facts, epistemic labeling, dedupe |
| AB Templates | `standards/ASSET-BUILDER-TEMPLATES.md` | Atomic Note, Playbook, Template formats |
| AB RAG Schema | `standards/ASSET-BUILDER-RAG-SCHEMA.md` | JSON spec for RAG output |
| AB Eval Pack | `standards/ASSET-BUILDER-EVAL.md` | 6-point rubric, tier thresholds |
| AB Registry | `standards/ASSET-BUILDER-REGISTRY.md` | Naming (AB-[slug]-[TYPE]-[0001]), tags, ontology |
| EIJA Framework | `standards/EIJA-FRAMEWORK.md` | E/I/J/A labeling, self-calibrating protocol |
| Report Blueprint | `standards/REPORT-BLUEPRINT.md` | 12 building blocks, 3 tests, grading A+++/A+/B/C |
| Gold Standard | `standards/GOLD-STANDARD-OUTPUT.md` | What a €200K McKinsey report looks like |
| **Beipackzettel** | **`standards/BEIPACKZETTEL-STANDARD.md`** | **Golden Bible: Confidence formula, Trust Score, all 7 fields, validation rules** |

---

## 3 Gesetze

> 1. **Opus empfängt nur.** Erfindet keine Fakten. Verbindet was es bekommt.
> 2. **Sonnet spricht nur mit Python.** Nie mit Opus direkt. Nie mit anderem Sonnet.
> 3. **Python überall wo zählbar, prüfbar, deterministisch.**

---

## Architektur-Diagramm

```
                         FLORIAN
                        ┌───┴───┐
                   CP1 ─┤       ├─ CP2
                   30s  │       │  2min
                        └───┬───┘
                            │
          ┌─────────────────┴─────────────────┐
          │          OPUS (Brain)              │
          │          1M Token Context          │
          │                                    │
          │  Empfängt NUR Files von Python.    │
          │  Erfindet KEINE neuen Fakten.      │
          │  Verbindet, synthetisiert,         │
          │  schreibt narrativ.                │
          │                                    │
          │  Phase 1: FRAME     (10 min)       │
          │  Phase 3: SYNTHESIZE (10 min)      │
          │  Phase 4: ASSETS    (10 min)       │
          └─────────────┬──────────────────────┘
                        │
                   liest/schreibt
                   NUR über Python
                        │
          ┌─────────────┴──────────────────────┐
          │         PYTHON (Gateway)            │
          │                                     │
          │  Einziger Kommunikationskanal.       │
          │  Speichert, zählt, validiert.        │
          │  Kein LLM. Kein Raten.              │
          │                                     │
          │  Phase 2:   Orchestrate + Brave     │
          │  Phase 2b:  Pre-Validate            │
          │  Phase 3.5: Validate                │
          │  Phase 5:   Quality Gate            │
          └──┬─────┬─────┬─────┬─────┬─────────┘
             │     │     │     │     │
             ▼     ▼     ▼     ▼     ▼
           ┌───┐ ┌───┐ ┌───┐ ┌───┐ ┌───┐
           │S1 │ │S2 │ │S3 │ │S4 │ │S5 │
           └───┘ └───┘ └───┘ └───┘ └───┘
           Sonnet Agents (isoliert)

           Jeder sieht NUR:
           - Seine 1 Sub-Question
           - Brave-Ergebnisse dafür
           - Reference Library
           Sonst NICHTS.
```

---

## Ablauf

```
 Zeit   Phase                    Wer          Was passiert
─────── ──────────────────────── ──────────── ─────────────────────────────────
 0:00   Phase 1: FRAME           Opus         Echte Frage + 5 SQs + 3 Blindspots
 10:00  🔴 CHECKPOINT 1          Florian      30 Sek: GO / EDIT / ADD BLINDSPOT
 10:30  Phase 2a: RESEARCH       Python       Brave ×5-7 parallel (SQs + promoted blindspots)
                                  Sonnet ×5    Je 1 Sub-Question recherchieren
 20:30  Phase 2b: EXTRACT        Sonnet ×5    Claims extrahieren (verbatim)
                                  Sonnet ×1    Contradictions finden
                                  Sonnet ×5    Sub-Reports reviewen
                                  Python       Zählen, GOOD/WEAK labeln
 32:30  Phase 3: SYNTHESIZE      Opus         Alles lesen → Report schreiben
 42:30  Phase 3.5: VALIDATE      Python       E/I/J/A, CRT-Check, New Facts
 42:35  Phase 3.6: QA REVIEW     Sonnet       Semantic check (ERF Rubric /16)
 47:35  Phase 4: ASSETS          Opus         Notes + Playbooks + RAG JSON
 52:35  Phase 5: QUALITY GATE    Python       Grade → SHIP/REVISE/REJECT
 52:40  🔴 CHECKPOINT 2          Florian      2 Min: SHIP / REVISE / REJECT
─────── ──────────────────────── ──────────── ─────────────────────────────────
 ~55m   FERTIG                                19 LLM Calls, $0, 2.5 Min Human
```

---

## Phase 1: FRAME

**Wer:** Opus (1 Call, ~10 Min)
**Input:** Topic, CRTs, Corrections, Decisions
**Output:** research-brief.json

### Prompt

```markdown
You are MIA, a research strategist. Your job: find the REAL question
and decompose it into researchable sub-questions.

## TOPIC
{topic}

## DECISION CONTEXT
{decision}

## WHAT YOU ALREADY KNOW (verified — do not contradict)
{crts}

## WHAT WE GOT WRONG BEFORE (learn from these)
{corrections}

## KEY DECISIONS WE'VE MADE
{decisions}

## TASK
1. State THE REAL QUESTION (1 sentence — the question behind the question)
   Bad: "What is trust calibration?"
   Good: "Should we build calibration infrastructure before EU AI Act
          enforcement in Aug 2026, or wait for standards?"

2. WHY NOW (what changed in the last 90 days that makes this urgent)

3. Decompose into {n_sub} SUB-QUESTIONS:
   - MECE (mutually exclusive, collectively exhaustive)
   - Each independently researchable by a separate analyst
   - Each answerable with available evidence
   - Ordered by importance to the decision

4. For EACH sub-question:
   - question: 1 sentence
   - why_it_matters: 1 sentence connecting it to the decision
   - evidence_needed: what specific evidence would answer it
   - search_queries: 2-3 Brave search queries (specific, not generic)

## OUTPUT FORMAT (JSON only, no explanation)
```json
{
  "real_question": "...",
  "why_now": "...",
  "sub_questions": [
    {
      "id": "SQ-1",
      "question": "...",
      "why_it_matters": "...",
      "evidence_needed": "...",
      "search_queries": ["...", "..."]
    }
  ],
  "blindspots": [
    {
      "question": "What question is nobody asking about this topic?",
      "why_its_a_blindspot": "Why this gets overlooked",
      "confidence": 75,
      "reasoning": "What would raise/lower this confidence",
      "evidence_hint": "What evidence would answer this",
      "who_would_know": "What expert would spot this immediately",
      "recommendation": "YES — priority 2 / MAYBE / NO"
    }
  ]
}
```

Think about blindspots:
- What would a CRITIC ask?
- What would someone from a DIFFERENT FIELD ask?
- What ASSUMPTION could be wrong?
- What SECOND-ORDER EFFECT are we ignoring?
- What worked in ANALOGOUS SITUATIONS?

Generate exactly 3 blindspots. Be specific.
```

---

## 🔴 CHECKPOINT 1: Florian

**Florian sieht:** Real Question + 5 Sub-Questions + Blindspot Questions (5 Sätze + 3 Blindspots)
**Zeitaufwand:** 30 Sekunden
**Optionen:**
- **GO** → Phase 2 startet (mit oder ohne Blindspots)
- **EDIT** → Sub-Question ändern/streichen/hinzufügen
- **REFRAME** → Neue Frage, Phase 1 nochmal
- **ADD BLINDSPOT** → Florian fügt eigene Blindspot-Frage hinzu

**Warum:** Falsche Frage = 40 Min verschwendet. 30 Sek Review verhindert das.

---

## Phase 1b: BLINDSPOT DISCOVERY

**Wer:** Opus (same call as Phase 1, or separate 5 Min call)
**Input:** Research Brief + CRTs + Corrections
**Output:** 3 Blindspot Questions mit Confidence + Begründung

### Prompt (Anhang zu Phase 1 Prompt, oder separater Call)

```markdown
## BLINDSPOT ANALYSIS

Now challenge your own framing. Find what you're NOT asking.

For each blindspot:
- question: The question nobody is asking about this topic
- why_its_a_blindspot: Why this gets overlooked (1 sentence)
- confidence: How confident are you this is a real blindspot? (0-100%)
- reasoning: Why this confidence level (what would raise/lower it)
- evidence_hint: What kind of evidence would answer this
- who_would_know: What type of expert would spot this immediately
- recommendation: Should Florian investigate this? (YES with priority / MAYBE / NO)

Think about:
- What would a CRITIC of this topic ask?
- What would someone from a DIFFERENT FIELD ask?
- What ASSUMPTION are we making that could be wrong?
- What SECOND-ORDER EFFECT are we ignoring?
- What worked in ANALOGOUS SITUATIONS that we're not considering?

Output 3 blindspots. Be specific. "We might be missing something" is not a blindspot.
"We assume calibration generalizes across languages — but all studies are English-only" IS.

```json
{
  "blindspots": [
    {
      "question": "...",
      "why_its_a_blindspot": "...",
      "confidence": 75,
      "reasoning": "...",
      "evidence_hint": "...",
      "who_would_know": "...",
      "recommendation": "YES — priority 2"
    }
  ]
}
```
```

### Was passiert mit Blindspots

```
Opus generates 3 blindspots
          │
          ▼
🔴 CHECKPOINT 1: Florian sieht:
   - 5 Sub-Questions (von Phase 1)
   - 3 Blindspot Questions (von Phase 1b)
   - Jede mit Confidence + Begründung
   
   Florian kann:
   ├── Blindspot → SQ-6 promoten (wird recherchiert)
   ├── Eigene Blindspot-Frage hinzufügen
   └── Ignorieren (wird nur im Appendix dokumentiert)
   
   Auch wenn Florian NICHTS tut:
   └── Blindspots werden im Final Report als
       "Documented Blindspots" Appendix aufgeführt
       → Ehrlichkeit + Credibility
```

### Warum das wertvoll ist

1. **Jede Recherche hat Blindspots.** McKinsey hat 3-5 Consultants die sich gegenseitig challengen. Wir haben 1 Opus. Blindspot Discovery ist der Ersatz.
2. **Dokumentierte Blindspots erhöhen Credibility.** Ein Report der sagt "Wir haben X nicht untersucht weil Y" ist vertrauenswürdiger als einer der so tut als wäre er vollständig.
3. **Florian bringt Domain-Expertise ein.** Opus sieht Papers. Florian sieht den Markt, die Kunden, die politische Lage. Seine Blindspot-Frage könnte die wichtigste SQ werden.
4. **Kostet fast nichts.** Same Opus Call oder +5 Min.

---

## Phase 2a: RESEARCH

**Wer:** Python orchestriert, Sonnet ×5 parallel (~10 Min)
**Input pro Sonnet:** 1 Sub-Question + Brave Results + Reference Library
**Output pro Sonnet:** Sub-Report (800 Wörter, E/I/J labeled)

### Python tut:
1. Brave Search API: 2-3 Queries pro Sub-Question (parallel)
2. Fetch Top-3 URLs pro SQ → speichern als `papers/web-*.md`
3. Sonnet ×5 parallel starten (max 3 gleichzeitig wegen OAuth)
4. Sub-Reports als Files speichern

### Sonnet Prompt (pro Sub-Question)

```markdown
You are a research analyst answering ONE specific question with evidence.

## YOUR QUESTION
{question}

## WHY IT MATTERS
{why_it_matters}

## EVIDENCE NEEDED
{evidence_needed}

## WEB SEARCH RESULTS (from Brave — real, current sources)
{web_results}

## VERIFIED REFERENCES (cite as [S#])
{references}

## RULES
1. ONLY use evidence from the web results and references above
2. Cite EVERY claim with [S#] or source URL
3. If no evidence found: say "No evidence found" — do NOT invent
4. Label each finding:
   [E] Evidenced — directly from source with citation
   [I] Interpreted — inferred from sources, explain logic
   [J] Judged — your assessment, no direct source
5. End with "SO WHAT: ..." (1-2 sentences for the decision maker)
6. Max 800 words. Dense, not verbose.

## OUTPUT

### Answer to: {question}

**Key Findings:**
- Finding 1 [E/I/J] [S#]
- Finding 2 ...

**Evidence Quality:**
- Strongest source: ...
- Weakest point: ...
- What's missing: ...

**So What:** ...

**Claims:**
| # | Claim | [S#] | E/I/J | Admiralty | Confidence |
```

---

## Phase 2b: EXTRACT + VERIFY

**Wer:** Sonnet ×11 + Python (~12 Min)
**Alle Sonnet-Jobs: Extraktion auf gegebenem Text. Kein Hallucination-Risiko.**

### 2b-1: Claim Extractor (Sonnet ×5, parallel)

```markdown
Extract the 3 most important factual claims from this sub-report.

## SUB-REPORT
{report}

For each claim, output JSON:
- text: the claim (VERBATIM quote from the report, not rephrased)
- label: E, I, or J (as labeled in the report)
- source: [S#] if cited, or "none"
- admiralty: A1 (DOI cited) / B2 (URL cited) / C3 (source named) / D4 (no source)

Output ONLY a JSON array of 3 claims. No explanation.
```

### 2b-2: Contradiction Finder (Sonnet ×1)

```markdown
Compare these sub-reports and find where they CONTRADICT each other.

## SUB-REPORTS
{all_5_sub_reports}

For each contradiction found:
- claim_a: verbatim text + which SQ
- claim_b: verbatim text + which SQ
- why_they_differ: 1 sentence
- which_is_stronger: A or B, and why (which has better source?)
- impact: how does this affect the main decision?

Output ONLY a JSON array. If no contradictions found: output []
Be thorough. Check every finding against every other finding.
```

### 2b-3: Reviewer (Sonnet ×5, parallel)

Uses canonical ERF Reviewer Prompt (standards/ERF-REVIEWER-PROMPT-v1.md).
Abbreviated for sub-reports (full rubric only on final report in Phase 3.5):

```markdown
You are the Exec Research Reviewer (ERF-REVIEWER-PROMPT-v1).

## SUB-REPORT
{report}

Score each dimension 0-2 (from Template G — Reviewer Rubric):
1. Evidence discipline — are claims cited with [S#]?
2. Uncertainty integrity — does it say what it doesn't know?
3. Actionability — is there a clear "So What"?

Also:
- List any uncited load-bearing claims (from Template E — Claim Ledger format)
- Flag any internal contradictions (from Template F — Contradiction Register format)

Output JSON:
{"evidence": 0-2, "uncertainty": 0-2, "actionability": 0-2,
 "total": 0-6, "top_issue": "one sentence",
 "uncited_claims": ["..."],
 "contradictions": ["..."]}
```

### Python tut danach:
1. E/I/J zählen pro Sub-Report
2. Sources zählen
3. GOOD (E ≥ J und ≥2 Sources) / WEAK labeln
4. AgentTrust Confidence pro Claim berechnen
5. Alles als JSON Files speichern
6. Validation Summary für Opus zusammenbauen

---

## Phase 3: SYNTHESIZE

**Wer:** Opus (1 Call, ~10 Min)
**Input:** ALLES was Python gesammelt hat (via Files)
**Output:** Final Report (5000-8000 Wörter)

### Prompt

```markdown
You are MIA, synthesizing research into an executive report.

## THE REAL QUESTION
{real_question}

## WHY NOW
{why_now}

## SUB-REPORTS (independently researched — verified by Python + Sonnet)
{5_sub_reports}

## EXTRACTED CLAIMS (verbatim, verified by Sonnet)
{15_claims_with_eij_and_admiralty}

## CONTRADICTIONS FOUND (by Sonnet)
{contradictions}

## SUB-REPORT QUALITY (scored by Sonnet, validated by Python)
{validation_summary_with_GOOD_WEAK_labels}

## PROPRIETARY KNOWLEDGE (do not contradict)
### Compounding Research Truths
{crts}
### Corrections (we got these wrong before)
{corrections}

## BEST PREVIOUS REPORT (improve on this, don't restart)
{ar020_v5}

## VAULT KNOWLEDGE (proprietary insights)
{vault_files}

## PAPER TEXTS (for verification)
{papers}

## YOUR RULES
1. **NO NEW FACTS.** Only combine what's in the sub-reports + CRTs + papers.
   If it's not sourced in any input above, do NOT include it.
2. **WEAK sub-reports:** Use findings ONLY if corroborated by another SQ or CRT.
   GOOD sub-reports: trust their [E] findings.
3. **E/I/J/A LABELS** in the Claim Ledger (appendix). Prose flows narratively.
4. **V3 STYLE:** Engaging opener. Case studies inline. Section confidence.
   Start with something an expert DOESN'T already know.
5. **"SO WHAT" per section.** Every section ends with: "For the decision maker: ..."
6. **CUSTOM FRAMEWORK.** Design ONE original model. Name it. Make it drawable.
   Map findings to it. It must show relationships you can't find on Google.
7. **SELF-CALIBRATING.** Apply the trust methods this report describes to itself.
   Every section: confidence %. Key claims: consistency check.
8. **RECOMMENDATIONS:** Phased (Week 1 / Month 1 / Quarter 1). Specific.
   Each [A] label must reference supporting [E]/[I]/[J].
   Each must have "If wrong:" (what happens, is it reversible?).
   Include "Do Not Deploy If" (5 specific conditions).

## CANONICAL TEMPLATES (from ERF-TEMPLATES.md — follow exactly)
Use Template C (Executive Report) for overall structure.
Use Template D (Source Log) for Appendix A.
Use Template E (Claim Ledger) for Appendix B.
Use Template F (Contradiction Register) for Appendix C.
Use Template G (Reviewer Rubric) for self-assessment.

## STRUCTURE (12 building blocks — all required, mapped to Templates)

### 1. Beipackzettel
**IMPORTANT:** Write `{{CONFIDENCE}}` as placeholder. Python will replace with computed value.
| Confidence | {{CONFIDENCE}} (computed by Python, AgentTrust formula) |
| Risk Level | HIGH/MEDIUM/LOW |
| Grounded | Yes/No |
| Sources | N |
| E/I/J/A | {{EIJA}} (counted by Python) |
| Research Type | ... |
| Self-Calibration | Applied |

Sources: (list)
Uncertainties: (list)
Risks: (list)
Not Checked: (list)

### 2. Opener (3 sentences)
Sentence 1: The surprise (what an expert doesn't know)
Sentence 2: Why now (trigger/deadline)
Sentence 3: What this report delivers (not "examines" — "delivers")

### 3. Executive Summary (SCR)
Situation (1 para) → Complication (1 para) → Resolution (1 para)
"If you read nothing else:" (3-5 standalone bullets with [S#])

### 4. Custom Framework
Name, visual description, mapping of findings, "So What" of the framework.

### 5. Key Findings (5-7)
Each: Finding → Evidence → Section Confidence % → "For the decision maker:"
Case studies woven in (real, sourced, verifiable).

### 6. Recommendations
Decision Matrix + Phased Plan (W1/M1/Q1) + "Do Not Deploy If" (5 conditions)
Each recommendation: [A] + supporting [E/I/J] + "If wrong:"

### 7. Risks & "What Would Change This"
Top 5 risks. Each: specific trigger + probability + what to monitor.

### 8-12. Appendices
Claim Ledger (12 claims, E/I/J/A, [S#], Admiralty, Confidence)
Source Log (all [S#] with Title, Venue, DOI/URL, Key Finding, Caveats)
Contradiction Register
Self-Calibration Results (E/I/J/A distribution, CRT cross-check, consistency)
Reviewer Rubric Score (/16)
Documented Blindspots (from Phase 1b — what we chose NOT to investigate + why)

## BANNED
NO: landscape, tapestry, delve, synergy, cutting-edge, game-changer,
    "It's worth noting", "In today's world"

Target: 5000-8000 words.
```

---

## Phase 3.5: VALIDATE

**Wer:** Python (deterministic, 5 Sekunden)

### Python tut:
```python
# 1. E/I/J/A Distribution
eija = count [E], [I], [J], [A] in final report
healthy = E > 50% and J < 20%

# 2. Source Count
sources_used = count unique [S#] references

# 3. CRT Cross-Check
for each CRT: is it mentioned/contradicted in report?

# 4. NEW FACT DETECTOR (kritisch!)
report_claims = extract all factual sentences from report
for claim in report_claims:
    if claim NOT in all-claims.json (from Phase 2b):
        flag as "OPUS-GENERATED — not in sub-reports"

# 5. Save validation.json
```

---

## Phase 3.6: QA REVIEW

**Wer:** Sonnet (1 Call, ~5 Min) — NICHT Opus (Opus hat geschrieben, darf nicht selbst QA-en)
**Input:** Final Report (nach Python Placeholder-Ersetzung) + all-claims.json + sub-reports
**Output:** qa-review.json (Score /16 + Fix Requests)
**Canonical Source:** `standards/ERF-REVIEWER-PROMPT-v1.md` (full rubric)

### Prompt

```markdown
You are the QA Reviewer. You did NOT write this report. Be harsh.
Use the full ERF Reviewer Rubric (Template G from ERF-TEMPLATES.md).

## FINAL REPORT
{final_report}

## ALL EXTRACTED CLAIMS (from Phase 2b — these are the verified claims)
{all_claims_json}

## BEIPACKZETTEL STANDARD
See: standards/BEIPACKZETTEL-STANDARD.md
All fields (confidence, sources, uncertainties, risks, not_checked) MUST be present.

## YOUR CHECKS (score each 0-2, total /16)

1. Opener: Surprises an expert? (not a definition, not "In today's world")
2. Evidence discipline: Every claim has [S#]?
3. E/I/J/A integrity: Labels present? E > 40%?
4. Uncertainty explicit: Beipackzettel uncertainties are specific?
5. Custom Framework: Original? Drawable? Not a 2x2 matrix?
6. Recommendations actionable: Each has "If wrong"? Phased plan specific?
7. Do Not Deploy: Exactly 5 specific conditions?
8. Claim Ledger: 12+ claims, each with Admiralty + Confidence?

## CRITICAL CHECK: New Facts
Compare every claim in the report against {all_claims_json}.
If the report contains a factual claim NOT in all-claims.json:
→ Flag it as "OPUS-GENERATED — not grounded in sub-reports"
→ This is the #1 failure mode.

## CRITICAL CHECK: Case Studies
Are case studies REAL (verifiable company, year, outcome)?
Or HYPOTHETICAL ("imagine a company...")?
Hypothetical = automatic -2 on rubric.

## CRITICAL CHECK: Beipackzettel Completeness
- Confidence: is it a number (not "High/Med/Low")?
- Sources: non-empty list?
- Uncertainties: specific, not generic?
- Risks: actionable, not "things might change"?
- Not Checked: at least 1 item?

Output JSON:
{
  "rubric_scores": {"opener": 0-2, "evidence": 0-2, ...},
  "total": 0-16,
  "new_facts_found": ["claim text that's not in sub-reports"],
  "hypothetical_cases": ["case study that's not verifiable"],
  "beipackzettel_issues": ["what's missing or wrong"],
  "fix_requests": ["specific fix if total < 13"],
  "recommendation": "SHIP / FIX_AND_RESHIP / REJECT"
}
```

### Was passiert mit QA Ergebnis

```
Sonnet QA Score:
  ≥13/16 + 0 new facts → SHIP (weiter zu Phase 4)
  ≥10/16 oder 1-2 new facts → FIX: Python entfernt flagged claims,
                                 Opus bekommt Fix Requests → Mini-Revision (5 min)
  <10/16 oder 3+ new facts → REJECT: zurück zu Phase 3
```

---

## Phase 4: ASSETS

**Wer:** Opus (1 Call, ~10 Min)
**Input:** Final Report + Vault + CRTs
**Output:** Asset Pack
**Canonical Source:** `standards/ASSET-BUILDER-SYSTEM-PROMPT.md` + `standards/ASSET-BUILDER-TEMPLATES.md` + `standards/ASSET-BUILDER-RAG-SCHEMA.md`

### Prompt

```markdown
You are the Asset Builder (AB-SYSTEM-PROMPT-v1).
Follow the canonical Asset Builder instructions exactly.
See: standards/ASSET-BUILDER-SYSTEM-PROMPT.md

## REPORT
{final_report}

## VAULT KNOWLEDGE (for cross-references to existing notes)
{vault}

## CRTs (link assets to these verified truths)
{crts}

## RULES
- NO NEW FACTS beyond the report. If it's not in the report, don't add it.
- Every asset: ID (AB-[slug]-[TYPE]-[0001]), classification
  (Evidenced/Derived/Operational), confidence, sources
- Dedupe: one canonical asset + aliases, not duplicates
- Contradictions → "Known Conflicts" note
- Cross-reference to Vault notes where relevant

## OUTPUT
1. **Asset Index** (counts + coverage map: which Finding → which Assets)

2. **Atomic Notes** (10-15)
   - ID, Title
   - "This answers: ..."
   - Content (2-5 bullets)
   - Classification: Evidenced / Derived / Operational
   - Confidence: High / Med / Low
   - Sources: [S#]
   - Tags
   - Vault cross-ref (if relevant existing note)

3. **Playbooks** (2-3)
   - Trigger: when to use
   - Goal: what it achieves
   - Inputs: what you need
   - Steps: numbered, specific
   - Outputs: what you get
   - Failure modes + Mitigations
   - Acceptance criteria: how to know it worked

4. **Templates** (1-2)
   - When to use
   - Copy/paste block
   - Pitfalls

5. **RAG JSON** (array of objects)
   Each: id, type, title, this_answers, content, tags,
         classification, confidence, sources, relations
```

---

## Phase 5: QUALITY GATE

**Wer:** Python (deterministic, 5 Sekunden)

### Python tut:
```python
# Inputs
rubric_score     = extract X/16 from report
eija             = from validation.json
has_beipackzettel = "BEIPACKZETTEL" in report
has_framework    = check for custom framework
has_do_not_deploy = "Do Not Deploy If" in report
new_fact_flags   = from validation.json

# Grading
if rubric >= 15 and E > 50% and J < 15%
   and has_beipackzettel and has_framework
   and has_do_not_deploy and new_fact_flags == 0:
    grade = "A+++"

elif rubric >= 13 and E > 40%:
    grade = "A+"

elif rubric >= 10:
    grade = "B"

else:
    grade = "C"

# Decision
if grade in ("A+++", "A+"):  decision = "SHIP"
elif grade == "B":           decision = "REVISE"
else:                        decision = "REJECT"
```

---

## 🔴 CHECKPOINT 2: Florian

**Florian sieht:**
```
Grade:        A+++
Rubric:       15/16
E/I/J/A:      E:14 I:8 J:3 A:5 (E=47% — WARNING, knapp unter 50%)
New Facts:    0 flags
Beipackzettel: ✅ Complete
Framework:    ✅ "The Confidence Stack"
Risks:        ✅ 5 listed

Decision:     SHIP

Executive Summary:
[3 paragraphs SCR]
"If you read nothing else:"
- Bullet 1 [S7]
- Bullet 2 [S8]
- Bullet 3 ...
```

**Optionen:**
- **SHIP** → Report wird published / gesendet
- **REVISE** → Spezifische Fix Requests → zurück zu Phase 3
- **REJECT** → Neu starten oder verwerfen

---

## Output Files

```
research/mia-pipeline/{topic}-{timestamp}/
├── pipeline.json                 Metadata (timing, models, phases)
├── research-brief.json           Phase 1 output (incl. blindspots)
├── blindspots.json               3 blindspots with confidence + reasoning
├── phase1-framer-prompt.md       Opus prompt
├── sq-01/                        Sub-Question 1
│   ├── prompt.md                 Sonnet prompt
│   └── report.md                 Sonnet output (800w, E/I/J)
├── sq-02/ ... sq-05/             Sub-Questions 2-5
├── all-claims.json               15 claims (Phase 2b)
├── contradictions.json           Cross-SQ contradictions
├── sub-reviews.json              Sonnet review scores (0-6)
├── sub-validations.json          Python GOOD/WEAK labels
├── phase3-synthesis-prompt.md    Opus prompt (full context)
├── final-report.md               A+++ Report
├── validation.json               E/I/J/A + CRT check + new facts
├── assets.md                     Atomic Notes + Playbooks + RAG
├── quality-gate.json             Grade + Decision
└── beipackzettel.json            AgentTrust-compatible JSON
```

---

## Ressourcen

| Phase | Modell | Calls | Zeit | Kosten | Risiko |
|-------|--------|-------|------|--------|--------|
| 1 Frame | Opus | 1 | 10 min | $0 | Falsches Framing → CP1 |
| 🔴 CP1 | Florian | — | 30 sec | — | — |
| 2a Research | Sonnet ×5 | 5 | 10 min | $0 | Halluc. (isoliert) |
| 2a Brave | Python | 10+ | 30s | $0 | Schwache Quellen |
| 2b Extract | Sonnet ×5 | 5 | 5 min | $0 | Keins |
| 2b Contradict | Sonnet ×1 | 1 | 2 min | $0 | Keins |
| 2b Review | Sonnet ×5 | 5 | 5 min | $0 | Keins |
| 2b Validate | Python | — | 5s | $0 | Keins |
| 3 Synthesize | Opus | 1 | 10 min | $0 | Ignoriert WEAK |
| 3.5 Validate | Python | — | 5s | $0 | Keins |
| 3.6 QA Review | Sonnet ×1 | 1 | 5 min | $0 | Semantic Check |
| 4 Assets | Opus | 1 | 10 min | $0 | Neue Facts |
| 5 QGate | Python | — | 5s | $0 | Keins |
| 🔴 CP2 | Florian | — | 2 min | — | — |
| **Total** | | **20** | **~60 min** | **$0** | |
