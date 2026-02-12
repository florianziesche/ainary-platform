import { callOpenAI, log } from '../utils.js';

export async function strategize(company, scannerData, industryData) {
  log('STRATEGIST', `Developing strategy for ${company}...`);
  return callOpenAI(
    `You are a McKinsey Senior Partner with 20 years of experience in AI transformation engagements. You have led $50M+ transformation programs for Fortune 500 companies. You think in frameworks, quantify everything, and always tie recommendations to business outcomes. Your analysis is sharper than what clients pay $500K for.`,
    `Based on this intelligence:

COMPANY: ${JSON.stringify(scannerData, null, 2)}
INDUSTRY: ${JSON.stringify(industryData, null, 2)}

Produce a STRATEGIC AI ASSESSMENT for ${company}:

1. AI_READINESS_SCORES (0-100 each, be honest not generous):
   - overall: weighted average
   - data_infrastructure: data quality, pipelines, governance
   - talent: AI/ML team strength, hiring, skills
   - strategy: clarity of AI vision, executive buy-in, roadmap
   - culture: experimentation culture, change readiness, agility

2. SWOT_ANALYSIS: Strengths, Weaknesses, Opportunities, Threats (3-4 each, specific to AI)

3. DEPARTMENT_OPPORTUNITIES (5-7 departments):
   Each: { department, current_state, ai_opportunity, estimated_annual_impact, difficulty, timeline }
   Use realistic dollar amounts based on company size.

4. COMPETITIVE_POSITION:
   - radar_scores (0-100): innovation, data_maturity, ai_adoption, talent, investment
   - competitive_insights: 3-4 specific insights about vs competitors

5. RECOMMENDATIONS (exactly 3, ranked by impact):
   Each: { title, why_it_matters, expected_roi, timeline, difficulty, first_step }
   Be SPECIFIC — not "implement AI" but "Deploy predictive maintenance on Line 4 using vibration sensor data"

6. IMPLEMENTATION_ROADMAP:
   - phase1 (months 1-3): quick wins
   - phase2 (months 4-6): core capabilities
   - phase3 (months 7-12): transformation

Return as structured JSON. Every number must be justified.`,
    { json: true }
  );
}
