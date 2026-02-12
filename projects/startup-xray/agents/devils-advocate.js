import { callOpenAI, log } from '../utils.js';

export async function critique(startup, allAnalysis) {
  log('DEVIL\'S ADVOCATE', `Finding every reason NOT to invest in ${startup}...`);
  return callOpenAI(
    `You are the most skeptical VC partner in the room. You've seen 10,000 pitches and funded 50. You know that 90% of startups fail. Your job is to find every reason NOT to invest. Be brutal. Be specific. A good 'no' is more valuable than a lazy 'yes'.`,
    `Find every reason NOT to invest in: "${startup}"

Based on ALL previous analysis:
Scanner: ${JSON.stringify(allAnalysis.scanner)}
Market: ${JSON.stringify(allAnalysis.market)}
Investor: ${JSON.stringify(allAnalysis.investor)}
Financier: ${JSON.stringify(allAnalysis.financier)}

Produce:
1. RED FLAGS (3-5): What specific warning signs do you see? (Team gaps, market risks, competitive threats, timing issues, execution risks)
   - Each flag should be a paragraph with specific evidence

2. KILL SHOTS (1-3): What single thing could kill this company? Not generic risks — specific to THIS startup.
   - Each kill shot should be 2-3 sentences explaining the mechanism of failure

3. THE UNCOMFORTABLE QUESTION: The one question you'd ask the founder that would make them squirm. The question that gets at the core risk.
   - The question itself
   - Why it matters (2-3 sentences)
   - What answer you're looking for

4. PATTERN MATCHING: What failed startup does this remind you of? Why? What's different this time?
   - Name the comparable failure
   - Why the pattern matches (2-3 sentences)
   - What would need to be different (2-3 sentences)

5. CONTRARIAN TAKE: If everyone loves this deal, what's the other side? If everyone hates it, what are they missing?
   - 2-3 paragraphs with the contrarian perspective

Return structured JSON with all sections. Be brutal but constructive.`,
    { json: true }
  );
}
