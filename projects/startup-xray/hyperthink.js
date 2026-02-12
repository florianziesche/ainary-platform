import { callOpenAI, log } from './utils.js';

export async function hyperthink(startup, agentOutputs) {
  // Round 1: Synthesize
  log('HYPERTHINK', 'Round 1/3: Synthesizing all agent outputs...');
  const draft = await callOpenAI(
    `You are a senior VC partner synthesizing due diligence from your analyst team. You resolve contradictions, prioritize insights, and ensure every claim is supported. You write with DEPTH and HONESTY — every section should be substantive, and you NEVER hide data gaps. Admitting uncertainty is a strength in VC analysis.

Your job is to produce insights that NOBODY ELSE HAS. Connect non-obvious data points. Look for hidden signals in hiring patterns, tech stack choices, competitive moves, and funding sources. Think like an operator who's been in the trenches.`,
    
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
- UNIQUE INSIGHTS must connect 2+ non-obvious data points
- HIDDEN SIGNALS must be based on real patterns (hiring, tech, competitive, funding)
- TAM/SAM/SOM must include methodology
- Valuation range must be defensible with comps
- Timing analysis must explain WHY NOW in detail

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
  
  "founder_network_analysis": "2 paragraphs analyzing what the founders' LinkedIn connections, board members, advisors, and investor choice reveal about their strategy, network quality, and ability to execute. What doors can they open? Who's advising them? Are their investors strategic or just financial?",
  
  "market_opportunity": {
    "tam_sam_som": { 
      "tam": "$X", 
      "sam": "$X", 
      "som": "$X", 
      "methodology": "How these numbers were calculated (bottom-up or top-down)"
    },
    "market_timing": "2 paragraphs on why now (NOT GENERIC)",
    "dynamics": "2 paragraphs on market structure (winner-take-all vs fragmented, etc.)",
    "confidence": "HIGH|GOOD|MODERATE|LOW|SPECULATIVE",
    "data_gaps": ["what market data we couldn't find"]
  },
  
  "timing_analysis": "3-4 paragraphs with a detailed timeline: What changed in the last 12-24 months? Regulatory shifts, technology breakthroughs, consumer behavior changes, macro trends. Be SPECIFIC with dates and events. This is the 'Why Now' deep dive.",
  
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
  
  "hidden_signals": {
    "hiring_signal": "2-3 sentences: What do their job postings reveal? Are they hiring sales (GTM focus) or engineers (product focus)? Senior roles (scaling) or junior (cost-conscious)? Remote vs office (culture)? SPECIFIC roles and what they mean.",
    "tech_signal": "2-3 sentences: What does their tech stack choice reveal? (Modern vs legacy, open-source vs proprietary, cloud-native, API-first, etc.) What does this say about their technical priorities and sophistication?",
    "competitive_signal": "2-3 sentences: What are competitors doing RIGHT NOW that reveals market timing? Recent funding rounds, product launches, M&A activity, pricing changes. What does this tell us about the startup's position?",
    "funding_signal": "2-3 sentences: Who invested in them and what does that reveal? Are investors strategic (with distribution) or just financial? Do they have competitive portfolio companies? What stage are investors known for?"
  },
  
  "unique_insights": [
    "An insight that requires connecting 2+ non-obvious data points from different sections (e.g., hiring + funding timing, tech stack + market positioning, founder background + product strategy). Each insight should be 2-3 sentences and show reasoning that a typical analyst would miss.",
    "A prediction based on patterns that aren't obvious (e.g., 'Their recent hire of 3 enterprise sales VPs from Oracle + Series B from Salesforce Ventures suggests a pivot from PLG to enterprise — this could 3x ARR but requires nailing a new sales motion').",
    "A risk or opportunity that only an operator would see (e.g., 'Founder's lack of B2B sales experience is a red flag given the pivot to enterprise, but their advisory board (3 ex-Snowflake execs) could bridge this gap if they're actively involved')."
  ],
  
  "financial_assessment": {
    "valuation_range": { 
      "min": "$XB", 
      "estimated": "$XB", 
      "max": "$XB", 
      "methodology": "2-3 sentences: Based on comparable transactions (list 2-3), revenue multiples (if known), growth rate adjustments, and market positioning. Be transparent about assumptions."
    },
    "comparables": [{ "company": "", "stage": "", "valuation": "", "outcome": "" }],
    "unit_economics": "What we can infer about LTV/CAC, margins, burn (be honest about gaps)",
    "fundraising_signals": "Are they raising? Evidence?",
    "confidence": "HIGH|GOOD|MODERATE|LOW|SPECULATIVE",
    "assumptions": ["key assumptions behind estimates"]
  },
  
  "execution_risk_score": N (0-100, where 100 = high risk of execution failure),
  "market_timing_score": N (0-100, where 100 = perfect market timing),
  
  "growth_levers": [
    { 
      "lever": "Specific opportunity", 
      "impact": "estimated effect (e.g., '30% increase in conversion', '2x ARR in 18mo')", 
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
- execution_risk_score: 0-100 (higher = more risk)
- market_timing_score: 0-100 (higher = better timing)
- difficulty: "Easy", "Medium", or "Hard" only
- recommendation: "INVEST", "PASS", or "DIG_DEEPER" only
- five_questions: exactly 5 items
- unique_insights: 3-4 items, each connecting non-obvious dots
- hidden_signals: all 4 must be present and specific
- confidence levels must use exact strings listed above

QUALITY CHECKS:
- Are unique_insights actually unique? Or generic observations anyone could make?
- Are hidden_signals based on real patterns? Or speculation?
- Is timing_analysis specific with dates and events? Or vague "market is growing"?
- Is founder_network_analysis substantive? Or just "they have good connections"?
- Is valuation_range defensible? Or pulled from thin air?`,
    
    { json: true, temperature: 0.6 }
  );

  // Round 2: Critique
  log('HYPERTHINK', 'Round 2/3: Critical review...');
  const critique = await callOpenAI(
    `You are a hostile LP reviewing this due diligence. Your job is to find EVERY weakness. Missing data? Unsubstantiated claims? Overly optimistic projections? Find them all. VCs hate bullshit — check if the analyst is being honest about data gaps.

You are ESPECIALLY critical of:
1. Generic insights that any analyst could produce
2. Vague timing analysis without specific dates/events
3. Valuation estimates without comparable transactions
4. Hidden signals that are speculation, not based on real patterns
5. Unique insights that don't actually connect non-obvious dots`,
    
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
8. UNIQUE INSIGHTS CHECK: Are these insights actually unique? Or could any analyst produce them?
9. HIDDEN SIGNALS CHECK: Are these based on real patterns? Or speculation?
10. TIMING ANALYSIS CHECK: Is this specific with dates/events? Or vague?
11. VALUATION CHECK: Is the range defensible with comparable transactions?
12. FOUNDER NETWORK CHECK: Is this substantive or superficial?

For each issue, be SPECIFIC about what's wrong and how to fix it.

Return as JSON: { "issues": [{ "section": "", "issue": "", "severity": "critical|high|medium|low", "fix": "" }] }`,
    
    { json: true, temperature: 0.5 }
  );

  // Round 3: Finalize
  log('HYPERTHINK', 'Round 3/3: Incorporating critique and finalizing...');
  const final = await callOpenAI(
    `You are the final editor. Take the draft report and the critique, incorporate all valid criticisms, and produce the definitive report. The result must be honest, balanced, and thorough. If data is missing, SAY SO. If confidence is low, LOWER THE SCORES. A VC who admits uncertainty is more credible than one who bullshits.

CRITICAL FIXES TO PRIORITIZE:
1. If unique_insights are generic, REWRITE them to connect non-obvious dots
2. If hidden_signals are speculative, FLAG THE SPECULATION or base them on real patterns
3. If timing_analysis is vague, ADD SPECIFIC DATES AND EVENTS
4. If valuation_range lacks comps, ADD COMPARABLE TRANSACTIONS or lower confidence
5. If founder_network_analysis is superficial, ADD SPECIFIC NAMES AND CONNECTIONS
6. If sections are too shallow, EXPAND THEM (2-4 paragraphs)
7. If confidence levels don't match data quality, ADJUST THEM
8. If recommendation doesn't match evidence, FIX IT`,
    
    `DRAFT REPORT: ${JSON.stringify(draft)}

CRITIQUE: ${JSON.stringify(critique)}

Incorporate all valid criticisms. Lower confidence where appropriate. Add missing data gaps. Make thin sections deeper. Adjust scores that were flagged as overly optimistic. REWRITE generic insights. ADD specific dates to timing analysis. ENSURE hidden signals are based on real patterns (or flag if speculative).

VALIDATION RULES (MUST FOLLOW):
- If confidence is LOW or SPECULATIVE, scores should reflect that uncertainty
- data_gaps and critical_missing_data must be comprehensive
- recommendation must match the evidence (don't say INVEST if confidence is SPECULATIVE)
- All narrative fields must be 2+ paragraphs
- five_questions must have exactly 5 items
- difficulty must be "Easy", "Medium", or "Hard"
- unique_insights must connect NON-OBVIOUS data points (rewrite if generic)
- hidden_signals must be specific and based on real patterns (flag if speculative)
- timing_analysis must have SPECIFIC DATES AND EVENTS (not vague "market is growing")
- execution_risk_score: 0-100 (higher = more risk)
- market_timing_score: 0-100 (higher = better timing)

FINAL QUALITY CHECK:
- Would a top-tier VC partner find these insights valuable?
- Are the unique insights actually unique?
- Is the timing analysis specific enough to be actionable?
- Is the valuation range defensible?
- Is the founder network analysis substantive?
- Are hidden signals based on real patterns?
- Is the report honest about data gaps?

Produce the FINAL report for ${startup}. Return the SAME JSON structure but improved, honest, and substantive.`,
    
    { json: true, temperature: 0.5 }
  );

  log('HYPERTHINK', 'Complete. 3 rounds of synthesis finished.');
  
  // Final validation: ensure all required fields exist
  const validated = {
    ...final,
    unique_insights: final.unique_insights || [
      "Unique insight data not generated - requires deeper analysis of non-obvious patterns.",
      "Connect hiring patterns + funding timing + market positioning for fuller picture.",
      "Analyze founder background + tech stack choice + advisory board for execution risk assessment."
    ],
    hidden_signals: final.hidden_signals || {
      hiring_signal: "Hiring signal analysis requires access to job posting data.",
      tech_signal: "Tech stack analysis requires deeper technical due diligence.",
      competitive_signal: "Competitive signal requires real-time market monitoring.",
      funding_signal: "Funding signal analysis available from public investor data."
    },
    founder_network_analysis: final.founder_network_analysis || "Founder network analysis requires LinkedIn data and board composition details.",
    timing_analysis: final.timing_analysis || "Detailed timing analysis with specific dates and events requires comprehensive market research.",
    tam_sam_som: final.tam_sam_som || final.market_opportunity?.tam_sam_som,
    valuation_range: final.valuation_range || final.financial_assessment?.valuation_range,
    execution_risk_score: final.execution_risk_score || 50,
    market_timing_score: final.market_timing_score || 50
  };
  
  return validated;
}
