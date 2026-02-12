import { callOpenAI, log } from '../utils.js';

export async function analyzeIndustry(company, scannerData) {
  log('INDUSTRY', `Analyzing industry context for ${company}...`);
  return callOpenAI(
    `You are an industry analyst specializing in AI adoption across sectors. You have deep knowledge of digital transformation benchmarks, AI maturity models, and industry-specific use cases.`,
    `Based on this company profile:
${JSON.stringify(scannerData, null, 2)}

Analyze the INDUSTRY context:
1. INDUSTRY IDENTIFICATION: What specific industry/sub-industry?
2. AI ADOPTION RATE: How far along is this industry in AI adoption? (percentile, maturity stage)
3. TOP AI USE CASES: The 5-7 most impactful AI applications in this industry RIGHT NOW
4. BENCHMARK: How does ${company} compare to industry average in AI adoption?
5. INDUSTRY LEADERS: Who are the AI leaders in this industry? What are they doing?
6. REGULATORY LANDSCAPE: Any AI-specific regulations or compliance requirements?
7. DISRUPTION RISK: How likely is this industry to be disrupted by AI? What's the timeline?
8. TALENT MARKET: How competitive is AI talent in this sector?

Be specific. Use real industry data and benchmarks.
Return as structured JSON.`,
    { json: true }
  );
}
