# DepoDigest Pro — Algorithm Documentation

## Overview

DepoDigest Pro uses a multi-stage LLM pipeline to analyze deposition transcripts. The system is designed specifically for personal injury litigation, focusing on extracting actionable intelligence for plaintiff attorneys.

## Pipeline Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    INPUT: Deposition Transcript              │
└─────────────────────────────────┬───────────────────────────┘
                                  │
                                  ▼
┌─────────────────────────────────────────────────────────────┐
│              STAGE 1: Extraction & Summarization             │
│                                                              │
│  • Parse transcript structure (pages, lines, speakers)       │
│  • Extract case metadata                                     │
│  • Generate executive summary                                │
│  • Identify key admissions with page/line citations          │
│  • Build event timeline                                      │
│  • Detect internal contradictions                            │
│  • Assess witness credibility                                │
└─────────────────────────────────┬───────────────────────────┘
                                  │
                                  ▼
┌─────────────────────────────────────────────────────────────┐
│              STAGE 2: Settlement Impact Analysis             │
│                                                              │
│  • Score liability strength (1-100)                          │
│  • Score damages support (1-100)                             │
│  • Score credibility issues (1-100)                          │
│  • Calculate overall impact score                            │
│  • Estimate settlement range adjustment                      │
│  • Generate reasoning narrative                              │
└─────────────────────────────────┬───────────────────────────┘
                                  │
                                  ▼
┌─────────────────────────────────────────────────────────────┐
│           STAGE 3: Cross-Examination Strategy                │
│                                                              │
│  • Generate impeachment points                               │
│  • Create suggested cross-exam questions                     │
│  • Provide follow-up strategies (if admits/denies)           │
│  • Recommend questioning sequence                            │
└─────────────────────────────────┬───────────────────────────┘
                                  │
                                  ▼
┌─────────────────────────────────────────────────────────────┐
│                    OUTPUT: Structured Analysis               │
│                                                              │
│  • JSON format for UI consumption                            │
│  • All findings linked to page/line references               │
│  • Actionable trial preparation materials                    │
└─────────────────────────────────────────────────────────────┘
```

## Key Admission Classification

### Types
| Type | Description | Example |
|------|-------------|---------|
| **Liability** | Statements establishing fault or responsibility | "I made a mistake. I should have been more careful." |
| **Negligence** | Statements showing failure to exercise due care | "I was traveling 35 mph in a 25 mph zone." |
| **Damages** | Statements supporting extent/severity of harm | "I'm sorry to hear about her injuries." |
| **Causation** | Statements linking conduct to outcome | "I didn't have time to stop." |
| **Credibility** | Statements affecting witness trustworthiness | Contradictory statements about sleep duration |

### Severity Levels
| Level | Definition | Impact |
|-------|------------|--------|
| **Critical** | Case-changing admission; likely affects verdict | Highest settlement leverage |
| **Significant** | Strong support for plaintiff's theory | Substantial negotiating value |
| **Moderate** | Helpful but not decisive | Supporting evidence |
| **Minor** | Marginal relevance | Background context |

## Settlement Impact Scoring

### Components

1. **Liability Strength (1-100)**
   - Measures how strongly testimony establishes defendant fault
   - Factors: Direct admissions, circumstantial evidence, corroboration
   - Weight: 35% of overall score

2. **Damages Support (1-100)**
   - Measures how testimony supports damages claim
   - Factors: Acknowledgment of harm, lack of mitigation arguments
   - Weight: 25% of overall score

3. **Credibility Issues (1-100)**
   - Measures witness credibility problems
   - Factors: Contradictions, evasiveness, documentary impeachment
   - Weight: 25% of overall score

4. **Punitive Potential (1-100)**
   - Measures likelihood of punitive damages
   - Factors: Recklessness, pattern of conduct, egregious behavior
   - Weight: 15% of overall score

### Adjustment Calculation

The settlement range adjustment is derived from:
- Overall score > 80: +25-40% adjustment
- Overall score 70-80: +15-25% adjustment
- Overall score 60-70: +5-15% adjustment
- Overall score 50-60: Neutral (±5%)
- Overall score < 50: May require discount

## Contradiction Detection

The system identifies contradictions through:

1. **Semantic Analysis**
   - Compare statements on same topic for inconsistency
   - Identify qualifying language that contradicts prior absolutes

2. **Temporal Analysis**
   - Check timelines and durations for mathematical consistency
   - Flag impossible sequences of events

3. **Documentary Comparison**
   - Cross-reference testimony with exhibits
   - Identify statements contradicted by documents

## Cross-Examination Question Generation

Questions are generated following these principles:

1. **Leading Structure**
   - All questions answerable with yes/no
   - Built on established facts from the deposition

2. **Commitment-Based**
   - Lock witness into specific positions
   - Create foundation for impeachment

3. **Follow-Up Ready**
   - Prepared response for both admission and denial
   - Impeachment material identified in advance

## Multi-Deposition Comparison (Phase 2)

When multiple depositions are provided, the system:

1. **Cross-Reference Statements**
   - Find topics addressed by multiple witnesses
   - Compare versions of events

2. **Identify Conflicts**
   - Flag contradictions between witnesses
   - Assess which version is more credible

3. **Generate Strategy**
   - Recommend which witness to call first
   - Identify impeachment opportunities across depositions

## API Integration

### Request Format
```json
{
  "transcript": "Full deposition text...",
  "options": {
    "include_cross_exam": true,
    "include_settlement_analysis": true,
    "focus_area": "liability|damages|all"
  }
}
```

### Response Format
See `models.py` for complete schema. Response includes:
- metadata
- witness_summary
- executive_summary
- narrative_summary
- key_admissions[]
- timeline[]
- contradictions[]
- cross_exam_questions[]
- impeachment_points[]
- settlement_impact

## Limitations

1. **Context Length**
   - Very long depositions may need chunking
   - Currently supports transcripts up to ~100 pages

2. **Citation Accuracy**
   - Page/line numbers are extracted from transcript formatting
   - Non-standard formatting may affect accuracy

3. **Legal Advice**
   - This is an analysis tool, not legal advice
   - All findings should be reviewed by qualified counsel

## Future Enhancements

- [ ] Discovery document comparison
- [ ] Expert witness database
- [ ] Real-time deposition assistance
- [ ] Multi-case pattern analysis
- [ ] Verdict/settlement outcome tracking for ML training
