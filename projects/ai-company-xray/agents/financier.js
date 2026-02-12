import { callOpenAI, log } from '../utils.js';

export async function calculateFinancials(company, scannerData, industryData) {
  log('FINANCIER', `Modeling financials for ${company}...`);
  return callOpenAI(
    `You are a CFO advisor and financial modeler specializing in AI/digital transformation investments. You build business cases that boards approve. You think in NPV, IRR, payback periods, and always model conservative, base, and optimistic scenarios.`,
    `Based on this intelligence:

COMPANY: ${JSON.stringify(scannerData, null, 2)}
INDUSTRY: ${JSON.stringify(industryData, null, 2)}

Build the FINANCIAL CASE for AI investment at ${company}:

1. TOTAL_OPPORTUNITY: Annual value of all AI opportunities combined (conservative estimate)
2. INVESTMENT_REQUIRED: Range (min-max) for a comprehensive AI program
3. PAYBACK_PERIOD: In months (conservative)
4. DEPARTMENT_ECONOMICS (for top 5 departments):
   Each: { department, current_cost, ai_savings, implementation_cost, roi_percent, payback_months }
5. THREE_YEAR_MODEL:
   - year1: investment, savings, net
   - year2: investment, savings, net
   - year3: investment, savings, net
6. RISK_ADJUSTED_ROI: Factor in failure rates, delays, change management costs
7. FUNDING_RECOMMENDATION: How to fund this (CapEx, OpEx, phased, POC-first)

Use realistic numbers proportional to company size. Show your reasoning.
Return as structured JSON.`,
    { json: true }
  );
}
