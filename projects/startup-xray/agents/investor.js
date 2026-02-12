import { callOpenAI, log } from '../utils.js';

export async function evaluateInvestment(startup, scannerData, marketData) {
  log('INVESTOR', `Investment evaluation for ${startup}...`);
  return callOpenAI(
    `You are a Partner at a $500M venture fund evaluating this startup for investment. Write like you're presenting to your investment committee. Be specific, not generic. Rate confidence for each section.`,
    `Evaluate investment opportunity: "${startup}"

Scanner data: ${JSON.stringify(scannerData)}
Market data: ${JSON.stringify(marketData)}

Produce:
1. DEAL SCORE (0-100): Weighted score across Team (30%), Market (25%), Product (20%), Traction (15%), Timing (10%)
   - Include individual scores for each dimension
   - Show your calculation methodology
2. FOUNDER ASSESSMENT: Background strength, domain expertise, founder-market fit, red flags
3. PRODUCT ANALYSIS: Product-market fit signals, differentiation, technical depth
4. GROWTH LEVERS: Top 3 growth opportunities with estimated impact
5. COMPARABLE DEALS: 3-5 similar companies that raised recently, their valuations, outcomes
6. INVESTMENT THESIS: In 2-3 paragraphs, the bull case for investing
7. ANTI-THESIS: In 2-3 paragraphs, the bear case against investing

For each major section provide:
- Your analysis (detailed, 2-3 paragraphs minimum for narratives)
- confidence_level: "HIGH", "GOOD", "MODERATE", "LOW", or "SPECULATIVE"
- confidence_rationale: why this confidence level

Return structured JSON with scores, narratives, and confidence metadata.`,
    { json: true }
  );
}
