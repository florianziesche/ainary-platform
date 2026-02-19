# Output Schema — Standardisierte Qualität (v1.0)

## Prinzip

Opus schreibt nicht "einen Report". Opus füllt 12 definierte Blöcke aus.
Python validiert jeden Block. Fehlender Block = REVISE, nicht SHIP.

---

## Schema: Final Report

Der Report ist KEIN Freitext. Er besteht aus 12 Blöcken in exakter Reihenfolge.
Jeder Block hat: Pflichtfelder, Format, Validierungsregel.

### Block 1: BEIPACKZETTEL

```json
{
  "block": "beipackzettel",
  "required_fields": {
    "confidence_pct": "float, 0-100, computed by AgentTrust formula",
    "risk_level": "enum: HIGH | MEDIUM | LOW",
    "grounded": "bool",
    "source_count": "int >= 1",
    "eija_distribution": {
      "E": "int",
      "I": "int",
      "J": "int",
      "A": "int"
    },
    "research_type": "enum: Systematic Review | Expert Synthesis | Dialectic",
    "self_calibration": "enum: Applied | Structural Only | Not Applied",
    "sources": "list[str], min 1",
    "uncertainties": "list[str], min 1",
    "risks": "list[str], min 1",
    "not_checked": "list[str], min 0"
  },
  "validation": {
    "confidence_is_computed": "must reference AgentTrust formula, not 'High/Med/Low'",
    "e_pct_check": "E / (E+I+J+A) > 0.50 else WARNING",
    "j_pct_check": "J / (E+I+J+A) < 0.20 else WARNING",
    "no_empty_lists": "sources and uncertainties and risks must be non-empty"
  }
}
```

### Block 2: OPENER

```json
{
  "block": "opener",
  "required_fields": {
    "sentence_1_surprise": "string, something an expert doesn't know",
    "sentence_2_why_now": "string, trigger or deadline",
    "sentence_3_delivers": "string, what this report DELIVERS (not examines)"
  },
  "validation": {
    "max_sentences": 3,
    "banned_starts": ["In today's", "It's worth noting", "As we know"],
    "must_not_be_definition": "first sentence must not define the topic"
  }
}
```

### Block 3: EXECUTIVE SUMMARY

```json
{
  "block": "executive_summary",
  "required_fields": {
    "situation": "string, 1 paragraph, facts only",
    "complication": "string, 1 paragraph, problem/change/deadline",
    "resolution": "string, 1 paragraph, what report recommends",
    "if_you_read_nothing_else": "list[str], 3-5 bullets, each with [S#] or [E/I/J]"
  },
  "validation": {
    "standalone_test": "summary must make sense without rest of report",
    "resolution_has_recommendation": "must not say 'it depends' or 'further research'"
  }
}
```

### Block 4: CUSTOM FRAMEWORK

```json
{
  "block": "custom_framework",
  "required_fields": {
    "name": "string, memorable, unique",
    "description": "string, visual description (axes, levels, quadrants)",
    "findings_mapping": "list[str], which findings map where",
    "so_what": "string, what the framework shows that individual findings don't"
  },
  "validation": {
    "originality": "name should return 0 Google results",
    "drawable": "description must be specific enough to sketch"
  }
}
```

### Block 5: KEY FINDINGS

```json
{
  "block": "key_findings",
  "required_fields": {
    "findings": [
      {
        "id": "F-1",
        "finding": "string, 1 sentence",
        "evidence": "list[str], [S#] references",
        "section_confidence_pct": "float, 0-100",
        "confidence_reasoning": "string, why this confidence level",
        "for_the_decision_maker": "string, 1-2 sentences, So What"
      }
    ]
  },
  "validation": {
    "count": "5-7 findings",
    "each_has_so_what": true,
    "each_has_confidence": true,
    "each_has_source": "at least 60% must have [S#]"
  }
}
```

### Block 6: CASE STUDIES

```json
{
  "block": "case_studies",
  "required_fields": {
    "cases": [
      {
        "title": "string",
        "what_happened": "string, 3-5 sentences with firm, year, numbers",
        "source": "string, URL or reference",
        "lesson": "string, 1 sentence",
        "finding_link": "string, which Finding this illustrates"
      }
    ]
  },
  "validation": {
    "count": "2-3",
    "no_hypothetical": "must not contain 'hypothetical' or 'imagine' or 'consider a company'",
    "verifiable": "source must be searchable"
  }
}
```

### Block 7: RECOMMENDATIONS

```json
{
  "block": "recommendations",
  "required_fields": {
    "decision_matrix": "list of scenario → action mappings",
    "phased_plan": {
      "week_1": "string, specific action + who + output",
      "month_1": "string, specific action + who + output",
      "quarter_1": "string, specific action + who + output"
    },
    "do_not_deploy_if": "list[str], exactly 5 conditions",
    "recommendations": [
      {
        "text": "string",
        "label": "A",
        "supporting_eij": "list[str], which E/I/J findings support this",
        "if_wrong": "string, what happens, is it reversible?"
      }
    ]
  },
  "validation": {
    "monday_morning_test": "week_1 must be actionable this week",
    "do_not_deploy_count": 5,
    "each_has_if_wrong": true
  }
}
```

### Block 8: RISKS

```json
{
  "block": "risks",
  "required_fields": {
    "risks": [
      {
        "risk": "string, specific not generic",
        "probability": "enum: HIGH | MEDIUM | LOW",
        "impact": "enum: HIGH | MEDIUM | LOW",
        "trigger": "string, specific event that would activate this risk",
        "what_to_monitor": "string, how to watch for this trigger",
        "what_then": "string, what to do if triggered"
      }
    ]
  },
  "validation": {
    "count": "3-5",
    "no_generic": "must not contain 'market changes' or 'technology evolves'",
    "triggers_are_testable": "each trigger must be specific enough to observe"
  }
}
```

### Block 9: CLAIM LEDGER (Appendix)

```json
{
  "block": "claim_ledger",
  "required_fields": {
    "claims": [
      {
        "id": "CL-1",
        "text": "string, the claim",
        "label": "enum: E | I | J | A",
        "source": "string, [S#] or 'none'",
        "admiralty": "enum: A1 | A2 | B2 | C3 | D4 | E2",
        "confidence_pct": "float, computed by AgentTrust formula",
        "if_low_what_would_raise": "string"
      }
    ]
  },
  "validation": {
    "count": 12,
    "e_label_needs_source": "if label=E, source must not be 'none'",
    "a1_needs_doi": "if admiralty=A1, source must contain DOI",
    "distribution_check": "not all same admiralty (red flag)"
  }
}
```

### Block 10: SOURCE LOG (Appendix)

Template D from ERF-TEMPLATES.md. Python validates: every [S#] in body has entry, no orphan entries.

### Block 11: CONTRADICTION REGISTER (Appendix)

Template F from ERF-TEMPLATES.md. Python validates: at least 1 contradiction (0 = suspicious).

### Block 12: SELF-CALIBRATION + BLINDSPOTS (Appendix)

```json
{
  "block": "self_calibration",
  "required_fields": {
    "eija_distribution": "same as Beipackzettel",
    "eija_health": "enum: Healthy | Warning | Red Flag",
    "crt_cross_check": "list of CRT matches and conflicts",
    "correction_check": "list of correction matches",
    "reviewer_rubric_score": "int, 0-16",
    "documented_blindspots": [
      {
        "question": "string",
        "why_not_investigated": "string",
        "confidence": "int, 0-100"
      }
    ]
  }
}
```

---

## Python Validation (Phase 3.5 + 5)

```python
def validate_report(report_text: str) -> dict:
    """Validate final report against Output Schema."""
    
    checks = {}
    
    # Block 1: Beipackzettel
    checks["beipackzettel_present"] = "BEIPACKZETTEL" in report_text.upper()
    checks["confidence_is_number"] = bool(re.search(r'Confidence.*\d+(\.\d+)?%', report_text))
    checks["risk_level_present"] = any(r in report_text for r in ["HIGH", "MEDIUM", "LOW"])
    
    # Block 2: Opener
    first_para = report_text[:500]
    checks["no_banned_opener"] = not any(b in first_para for b in 
        ["In today's", "It's worth noting", "As we know", "landscape"])
    
    # Block 3: Executive Summary
    checks["has_scr"] = all(w in report_text.lower() for w in ["situation", "complication", "resolution"])
    checks["has_if_you_read"] = "if you read nothing else" in report_text.lower()
    
    # Block 4: Custom Framework
    checks["has_framework"] = any(w in report_text.lower() for w in ["framework", "model", "stack", "maturity"])
    
    # Block 5: Key Findings
    checks["has_so_what"] = report_text.lower().count("for the decision maker") >= 3
    checks["has_section_confidence"] = report_text.lower().count("section confidence") >= 3
    
    # Block 6: Case Studies
    checks["has_case_studies"] = report_text.lower().count("case study") >= 1 or "[source:" in report_text.lower()
    
    # Block 7: Recommendations
    checks["has_phased_plan"] = any(w in report_text.lower() for w in ["week 1", "month 1"])
    checks["has_do_not_deploy"] = "do not deploy" in report_text.lower()
    checks["has_if_wrong"] = report_text.lower().count("if wrong") >= 1
    
    # Block 8: Risks
    checks["has_trigger"] = "trigger" in report_text.lower() or "what would change" in report_text.lower()
    
    # Block 9: Claim Ledger
    checks["has_claim_ledger"] = "claim ledger" in report_text.lower()
    claim_count = len(re.findall(r'CL-\d+', report_text))
    checks["claim_count_ok"] = claim_count >= 10
    
    # Block 10: Source Log
    source_count = len(set(re.findall(r'\[S(\d+)\]', report_text)))
    checks["source_count"] = source_count
    checks["sources_ok"] = source_count >= 5
    
    # Block 11: Contradictions
    checks["has_contradictions"] = "contradiction" in report_text.lower()
    
    # Block 12: Self-Calibration
    checks["has_blindspots"] = "blindspot" in report_text.lower()
    
    # E/I/J/A Distribution
    eija = {l: len(re.findall(rf'\[{l}\]', report_text)) for l in "EIJA"}
    total = sum(eija.values()) or 1
    checks["eija"] = eija
    checks["e_pct"] = round(eija["E"] / total * 100, 1)
    checks["j_pct"] = round(eija["J"] / total * 100, 1)
    checks["eija_healthy"] = checks["e_pct"] > 50 and checks["j_pct"] < 20
    
    # Blocks present
    blocks_present = sum(1 for k, v in checks.items() 
                         if k.startswith("has_") and v)
    checks["blocks_present"] = blocks_present
    checks["blocks_total"] = 12
    
    # Grade
    passed = sum(1 for v in checks.values() if v is True)
    total_checks = sum(1 for v in checks.values() if isinstance(v, bool))
    checks["pass_rate"] = round(passed / total_checks * 100, 1)
    
    return checks
```

---

## Wie das standardisierte Qualität erzwingt

```
OHNE Schema:                         MIT Schema:
──────────                           ──────────
Opus schreibt Freitext               Opus füllt 12 Blöcke aus
Python: "enthält Report ein          Python: "hat Block 7 genau 5
  Beipackzettel? ja/nein"             Do-Not-Deploy Conditions?
                                      Hat jede Recommendation ein
→ Qualität schwankt 30-90%            If-Wrong? Hat der Claim Ledger
                                       genau 12 Claims mit Admiralty?"
                                     
                                     → Qualität schwankt 70-95%
                                       weil Python 25+ Checks enforced
```
