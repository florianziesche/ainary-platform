import { callOpenAI, log } from './utils.js';

export async function hyperthink(startup, agentOutputs) {
  // Round 1: Synthesize
  log('HYPERTHINK', 'Round 1/3: Synthesizing all agent outputs...');
  const draft = await callOpenAI(
    `You are a senior VC partner synthesizing due diligence from your analyst team. You resolve contradictions, prioritize insights, and ensure every claim is supported. You write with DEPTH and HONESTY — every section should be substantive, and you NEVER hide data gaps. Admitting uncertainty is a strength in VC analysis.`,
    `Synthesize these 5 agent outputs into ONE coherent due diligence report for ${startup}:

SCANNER: ${JSON.stringify(agentOutputs.scanner)}
MARKET: ${JSON.stringify(agentOutputs.market)}
INVESTOR: ${JSON.stringify(agentOutputs.investor)}
FINANCIER: ${JSON.stringify(agentOutputs.financier)}
DEVIL'S ADVOCATE: ${JSON.stringify(agentOutputs.devilsAdvocate)}

Produce a unified JSON report. Resolve contradictions. Keep the Devil's Advocate insights separate and unfiltered.

CRITICAL REQUIREMENTS:
- Every narrative field must be DETAILED (2-4 paragraphs minimum)
- Include confidence_level for EVERY major section
- Confidence indicators: HIGH (●●●●●), GOOD (●●●●○), MODERATE (●●●○○), LOW (●●○○○), SPECULATIVE (●○○○○)
- Be HONEST about data gaps — list what we couldn't find
- Deal Score must be 0-100 with breakdown by dimension

Return JSON matching this EXACT structure:
{
  "deal_score": {
    "overall": N (0-100),
    "team": N (0-100),
    "market": N (0-100), 
    "product": N (0-100),
    "traction": N (0-100),
    "timing": N (0-100),
    "confidence": "HIGH|GOOD|MODERATE|LOW|SPECULATIVE"
  },
  "tldr": "One paragraph summarizing the opportunity and deal score rationale",
  "tldr_detail": "2-3 additional paragraphs with deeper context",
  
  "founder_xray": {
    "founders": [
      { 
        "name": "", 
        "background": "2-3 sentences", 
        "strength": "specific assessment",
        "confidence": "VERIFIED|LIKELY|ESTIMATED|UNKNOWN"
      }
    ],
    "founder_market_fit": "2 paragraphs on how well founders match this problem",
    "red_flags": ["specific team concerns"],
    "confidence": "HIGH|GOOD|MODERATE|LOW|SPECULATIVE"
  },
  
  "market_opportunity": {
    "tam_sam_som": { "tam": "$X", "sam": "$X", "som": "$X", "methodology": "" },
    "market_timing": "2 paragraphs on why now",
    "dynamics": "2 paragraphs on market structure (winner-take-all vs fragmented, etc.)",
    "confidence": "HIGH|GOOD|MODERATE|LOW|SPECULATIVE",
    "data_gaps": ["what market data we couldn't find"]
  },
  
  "competitive_landscape": {
    "competitors": [{ "name": "", "position": "", "threat_level": "High|Medium|Low" }],
    "defensibility": "2 paragraphs on moats and competitive advantages",
    "defensibility_score": N (0-100),
    "confidence": "HIGH|GOOD|MODERATE|LOW|SPECULATIVE"
  },
  
  "traction_growth": {
    "known_metrics": { "users": "", "revenue": "", "growth": "", "sources": "" },
    "unknown_metrics": ["what traction data we couldn't find"],
    "assessment": "2 paragraphs on traction quality and growth trajectory",
    "confidence": "HIGH|GOOD|MODERATE|LOW|SPECULATIVE"
  },
  
  "financial_assessment": {
    "valuation_estimate": { "low": "$X", "high": "$X", "methodology": "2-3 sentences" },
    "comparables": [{ "company": "", "stage": "", "valuation": "", "outcome": "" }],
    "unit_economics": "What we can infer about LTV/CAC, margins, burn (be honest about gaps)",
    "fundraising_signals": "Are they raising? Evidence?",
    "confidence": "HIGH|GOOD|MODERATE|LOW|SPECULATIVE",
    "assumptions": ["key assumptions behind estimates"]
  },
  
  "growth_levers": [
    { 
      "lever": "Specific opportunity", 
      "impact": "estimated effect", 
      "timeline": "", 
      "difficulty": "Easy|Medium|Hard",
      "detail": "1-2 paragraphs on implementation"
    }
  ],
  
  "devils_advocate": {
    "red_flags": ["detailed paragraph each"],
    "kill_shots": ["detailed paragraph each"],
    "uncomfortable_question": { "question": "", "why_it_matters": "" },
    "pattern_matching": { "failed_comparable": "", "why_similar": "", "what_must_differ": "" },
    "contrarian_take": "2-3 paragraphs"
  },
  
  "investment_thesis": {
    "bull_case": "3 paragraphs on why to invest",
    "bear_case": "3 paragraphs on why to pass",
    "confidence": "HIGH|GOOD|MODERATE|LOW|SPECULATIVE"
  },
  
  "five_questions": [
    { "question": "Sharp, specific question", "why_it_matters": "1-2 sentences" }
  ],
  
  "bottom_line": {
    "recommendation": "INVEST|PASS|DIG_DEEPER",
    "reasoning": "2-3 paragraphs with honest assessment",
    "next_steps": ["specific actions if moving forward"]
  },
  
  "data_confidence_report": {
    "overall_confidence": "HIGH|GOOD|MODERATE|LOW|SPECULATIVE",
    "section_scores": [
      { "section": "Founders", "confidence": "", "source_count": N, "gaps": [""] }
    ],
    "critical_missing_data": ["what we NEED but don't have"],
    "methodology": "How confidence was calculated"
  }
}

VALIDATION RULES:
- deal_score.overall: 0-100
- All dimension scores: 0-100
- difficulty: "Easy", "Medium", or "Hard" only
- recommendation: "INVEST", "PASS", or "DIG_DEEPER" only
- five_questions: exactly 5 items
- confidence levels must use exact strings listed above`,
    { json: true, temperature: 0.6 }
  );

  // Round 2: Critique
  log('HYPERTHINK', 'Round 2/3: Critical review...');
  const critique = await callOpenAI(
    `You are a hostile LP reviewing this due diligence. Your job is to find EVERY weakness. Missing data? Unsubstantiated claims? Overly optimistic projections? Find them all. VCs hate bullshit — check if the analyst is being honest about data gaps.`,
    `Critique this due diligence report for ${startup}:
${JSON.stringify(draft, null, 2)}

Find:
1. FACTUAL ISSUES: Claims that may be wrong or unsubstantiated
2. CONFIDENCE MISMATCH: Sections claiming HIGH confidence without enough sources
3. HIDDEN GAPS: Data gaps that should be acknowledged but aren't
4. LOGICAL GAPS: Arguments that don't follow
5. OVERLY OPTIMISTIC: Where are projections too rosy given the data quality?
6. DEPTH CHECK: Which sections are too shallow?
7. VALIDATION: Are scores realistic? Is recommendation justified by evidence?

Return as JSON: { "issues": [{ "section": "", "issue": "", "severity": "high|medium|low", "fix": "" }] }`,
    { json: true, temperature: 0.5 }
  );

  // Round 3: Finalize
  log('HYPERTHINK', 'Round 3/3: Incorporating critique and finalizing...');
  const final = await callOpenAI(
    `You are the final editor. Take the draft report and the critique, incorporate all valid criticisms, and produce the definitive report. The result must be honest, balanced, and thorough. If data is missing, SAY SO. If confidence is low, LOWER THE SCORES. A VC who admits uncertainty is more credible than one who bullshits.`,
    `DRAFT REPORT: ${JSON.stringify(draft)}

CRITIQUE: ${JSON.stringify(critique)}

Incorporate all valid criticisms. Lower confidence where appropriate. Add missing data gaps. Make thin sections deeper. Adjust scores that were flagged as overly optimistic.

VALIDATION RULES (MUST FOLLOW):
- If confidence is LOW or SPECULATIVE, scores should reflect that uncertainty
- data_gaps and critical_missing_data must be comprehensive
- recommendation must match the evidence (don't say INVEST if confidence is SPECULATIVE)
- All narrative fields must be 2+ paragraphs
- five_questions must have exactly 5 items
- difficulty must be "Easy", "Medium", or "Hard"

Produce the FINAL report for ${startup}. Return the SAME JSON structure but improved and honest.`,
    { json: true, temperature: 0.5 }
  );

  log('HYPERTHINK', 'Complete. 3 rounds of synthesis finished.');
  return final;
}
