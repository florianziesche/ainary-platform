import { callOpenAI, log } from '../utils.js';

export async function analyzeFinancials(startup, scannerData, marketData) {
  log('FINANCIER', `Financial analysis for ${startup}...`);
  return callOpenAI(
    `You are a financial analyst specializing in startup valuations. Flag CLEARLY what's estimated vs. known. Most startup financials are private — be honest about that. Provide confidence levels for each estimate.`,
    `Analyze financials for: "${startup}"

Scanner data: ${JSON.stringify(scannerData)}
Market data: ${JSON.stringify(marketData)}

Analyze:
1. VALUATION ESTIMATE: Based on comparable transactions, what's this worth?
   - Revenue multiple approach (if revenue known)
   - Comparable company approach
   - Stage-appropriate benchmarks
2. UNIT ECONOMICS: What we can infer about LTV/CAC, margins, burn
3. FUNDRAISING ASSESSMENT: 
   - Are they likely raising? (signals from hiring, press)
   - Appropriate round size
   - Likely valuation range
4. PATH TO PROFITABILITY: Realistic assessment
5. EXIT SCENARIOS: Likely acquirers, IPO potential, timeline

For EACH section provide:
- Your analysis with specific numbers and ranges
- confidence_level: "HIGH", "GOOD", "MODERATE", "LOW", or "SPECULATIVE"
- assumptions: list the key assumptions behind each estimate
- data_available: what financial data was actually available vs. estimated

Return structured JSON with financial analysis and comprehensive confidence metadata for each section.`,
    { json: true }
  );
}
