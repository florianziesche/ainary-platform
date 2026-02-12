import { callOpenAI, log } from './utils.js';

export async function hyperthink(company, agentOutputs) {
  // Round 1: Synthesize
  log('HYPERTHINK', 'Round 1/3: Synthesizing all agent outputs...');
  const draft = await callOpenAI(
    `You are a senior editor at a top-tier strategy consultancy. You take raw analyst work and synthesize it into a coherent, executive-ready report. You resolve contradictions, prioritize insights, and ensure every claim is supported. You write with DEPTH — every section should read like a standalone analysis, not a bullet point summary.`,
    `Synthesize these 5 agent outputs into ONE coherent executive report for ${company}:

SCANNER: ${JSON.stringify(agentOutputs.scanner)}
INDUSTRY: ${JSON.stringify(agentOutputs.industry)}
STRATEGIST: ${JSON.stringify(agentOutputs.strategist)}
FINANCIER: ${JSON.stringify(agentOutputs.financier)}
PROVOCATEUR: ${JSON.stringify(agentOutputs.provocateur)}

Produce a unified JSON report. Resolve contradictions. Keep the Provocateur's insights separate and unfiltered.

CRITICAL: Every text field must be DETAILED and SUBSTANTIVE. No one-liners. Each narrative field should be 2-4 paragraphs minimum. This is a McKinsey-grade report, not a summary.

Return JSON matching this EXACT structure:
{
  "executive_summary": "3-4 detailed paragraphs covering company overview, AI position, key findings, and overall assessment",
  "executive_detail": "2-3 additional paragraphs with deeper context: industry dynamics, competitive pressures, and strategic imperatives",
  "ai_readiness": {
    "overall": N, "data_infrastructure": N, "talent": N, "strategy": N, "culture": N, "percentile": N
  },
  "readiness_analysis": "2-3 paragraphs explaining WHY each score is what it is, with specific evidence",
  "department_opportunities": [
    { "department": "", "current_state": "detailed description", "ai_opportunity": "specific AI use case", "estimated_impact": "$X-Y annually", "difficulty": "Easy|Medium|Hard" }
  ],
  "department_analysis": "2 paragraphs summarizing the department analysis: themes, biggest wins, cross-department synergies",
  "competitive_position": {
    "radar": { "innovation": N, "data_maturity": N, "ai_adoption": N, "talent": N, "investment": N },
    "insights": ["detailed insight with evidence, not just a sentence"]
  },
  "competitive_narrative": "2-3 paragraphs analyzing the competitive landscape in depth: who's ahead, who's behind, and why",
  "recommendations": [
    {
      "title": "",
      "why": "2-3 sentences",
      "roi": "",
      "timeline": "",
      "difficulty": "Easy|Medium|Hard",
      "first_step": "",
      "detail": "1-2 paragraphs with implementation specifics, prerequisites, and success metrics"
    }
  ],
  "roadmap": {
    "phase1": "detailed description with specific milestones and deliverables",
    "phase2": "detailed description",
    "phase3": "detailed description"
  },
  "roadmap_narrative": "1-2 paragraphs explaining the phasing logic and dependencies",
  "risks": [
    { "name": "", "likelihood": N (1-3 ONLY), "impact": N (1-3 ONLY), "mitigation": "detailed mitigation strategy" }
  ],
  "risk_narrative": "1-2 paragraphs on the overall risk landscape and how risks interact",
  "provocateur": {
    "blind_spots": ["detailed paragraph each, not one-liners"],
    "uncomfortable_truths": ["detailed paragraph each"],
    "what_mckinsey_wont_say": "substantial paragraph",
    "hidden_risks": ["detailed"],
    "contrarian_bet": "detailed paragraph with reasoning"
  },
  "critical_questions": [
    { "question": "Specific, sharp question", "why_it_matters": "Why this question is crucial for the company's AI future" }
  ],
  "bottom_line": {
    "total_opportunity": "$X.XM or €X.XB",
    "investment_required": "$XXK-$XXXK range",
    "payback_period": "X-Y months",
    "summary": "2-3 paragraphs with the honest assessment"
  },
  "bottom_line_detail": "Additional 1-2 paragraphs on financial modeling assumptions and caveats",
  "sources": {
    "data_sources": ["List of data sources used (e.g., company annual reports, industry benchmarks, analyst reports)"],
    "methodology": "How the 5-agent system works and what each agent contributes",
    "limitations": "Honest limitations of this analysis",
    "links": ["Relevant URLs or references"]
  }
}

IMPORTANT CONSTRAINTS:
- risks.likelihood and risks.impact must be 1, 2, or 3 ONLY (not 4 or 5)
- difficulty must be exactly "Easy", "Medium", or "Hard" (not "High" or "Low")
- All dollar/euro amounts should be realistic for the company's size
- critical_questions must have exactly 5 items`,
    { json: true }
  );

  // Round 2: Critique
  log('HYPERTHINK', 'Round 2/3: Critical review...');
  const critique = await callOpenAI(
    `You are a hostile reviewer. Your job is to find EVERY weakness in this report. Missing data? Unsubstantiated claims? Logical gaps? Overly optimistic projections? Find them all.`,
    `Critique this AI strategy report for ${company}:
${JSON.stringify(draft, null, 2)}

Find:
1. FACTUAL ISSUES: Claims that may be wrong or unsubstantiated
2. LOGICAL GAPS: Arguments that don't follow
3. MISSING ELEMENTS: What should be in the report but isn't?
4. OVERLY OPTIMISTIC: Where are projections too rosy?
5. DEPTH CHECK: Which sections are too shallow and need more substance?
6. DATA VALIDATION: Are risk scores within 1-3 range? Are difficulties "Easy"/"Medium"/"Hard" only?
7. SPECIFIC FIXES: For each issue, suggest the fix

Return as JSON: { "issues": [{ "section": "", "issue": "", "severity": "high/medium/low", "fix": "" }] }`,
    { json: true }
  );

  // Round 3: Finalize
  log('HYPERTHINK', 'Round 3/3: Incorporating critique and finalizing...');
  const final = await callOpenAI(
    `You are the final editor. Take the draft report and the critique, incorporate all valid criticisms, and produce the definitive report. The result must be bulletproof, balanced, and brilliant. Every section must be SUBSTANTIVE — no thin sections allowed.`,
    `DRAFT REPORT: ${JSON.stringify(draft)}

CRITIQUE: ${JSON.stringify(critique)}

Incorporate all valid criticisms. Adjust numbers that were flagged as overly optimistic. Fill gaps. Fix logical issues. Make thin sections deeper.

VALIDATION RULES (MUST FOLLOW):
- risks[].likelihood: MUST be 1, 2, or 3 only
- risks[].impact: MUST be 1, 2, or 3 only
- recommendations[].difficulty: MUST be exactly "Easy", "Medium", or "Hard"
- department_opportunities[].difficulty: MUST be exactly "Easy", "Medium", or "Hard"
- critical_questions: MUST have exactly 5 items
- All narrative fields must be 2+ paragraphs

Produce the FINAL report for ${company}. Return the SAME JSON structure as the draft but improved.`,
    { json: true }
  );

  log('HYPERTHINK', 'Complete. 3 rounds of analysis finished.');
  return final;
}
