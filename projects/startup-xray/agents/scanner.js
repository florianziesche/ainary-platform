import { callOpenAI, log } from '../utils.js';

export async function scan(startup) {
  log('SCANNER', `Pre-screening due diligence on ${startup}...`);
  return callOpenAI(
    `You are a VC analyst conducting pre-screening due diligence on a startup. Compile everything you can find from PUBLIC sources. For EACH data point, rate your confidence: VERIFIED (multiple reliable sources), LIKELY (one source or strongly implied), ESTIMATED (based on industry patterns), or UNKNOWN (no public data). Be HONEST about what you don't know. A VC respects honesty over bullshit.`,
    `Conduct pre-screening due diligence on: "${startup}"

Search for:
1. COMPANY: What they do, founding date, HQ, team size, product
2. FUNDING: Known rounds, investors, valuation (Crunchbase, press releases)
3. FOUNDERS: Backgrounds, previous companies, education, LinkedIn profiles
4. TRACTION: Any public metrics (users, revenue mentions, growth claims in press)
5. TECHNOLOGY: Tech stack (GitHub, job postings), patents, open source
6. HIRING: Current job openings → what roles tell us about strategy
7. PRESS: Recent coverage, partnerships, product launches
8. COMPETITORS: Direct and indirect competitors

CRITICAL: For EACH section, provide:
- The data you found
- confidence_level: "VERIFIED", "LIKELY", "ESTIMATED", or "UNKNOWN"
- source_count: number of distinct sources (for calculating confidence indicator)
- sources: list of where this data came from

Return as structured JSON with these fields for each section, plus an overall confidence_summary showing how many sources were used total.`,
    { json: true }
  );
}
