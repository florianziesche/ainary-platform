import { callOpenAI, log } from '../utils.js';

export async function analyzeMarket(startup, scannerData) {
  log('MARKET', `Market opportunity analysis for ${startup}...`);
  return callOpenAI(
    `You are a market research analyst for a top-tier VC fund. Be specific. Use real market data where available. Flag estimates clearly. Rate your confidence for each section: HIGH (15+ sources), GOOD (8-14 sources), MODERATE (3-7 sources), LOW (1-2 sources), or SPECULATIVE (no specific data).`,
    `Analyze the market opportunity for: "${startup}"

Based on this startup data: ${JSON.stringify(scannerData)}

Analyze:
1. TAM/SAM/SOM with methodology and sources
2. Market timing: Why now? What changed?
3. Competitive landscape: Who else is here? Market map.
4. Defensibility: What's the moat? Network effects? Data? Switching costs?
5. Market dynamics: Winner-take-all or fragmented? Regulatory risks?
6. Adjacent opportunities: Where could they expand?

For EACH section provide:
- Your analysis
- confidence_level: "HIGH", "GOOD", "MODERATE", "LOW", or "SPECULATIVE"
- source_count: number of sources
- data_gaps: what specific data you couldn't find

Return structured JSON with market analysis plus confidence metadata for each section.`,
    { json: true }
  );
}
