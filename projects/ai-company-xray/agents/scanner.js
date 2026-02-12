import { callOpenAI, log } from '../utils.js';

export async function scan(company) {
  log('SCANNER', `Scanning ${company}...`);
  return callOpenAI(
    `You are a world-class business intelligence analyst. Your job is to compile a comprehensive company profile based on your training data. Be specific with real facts, numbers, and details. If you're uncertain about something, say so — never fabricate specific numbers.`,
    `Compile a detailed intelligence profile for: "${company}"

Cover ALL of these areas with specific details:
1. COMPANY OVERVIEW: What they do, industry, size (employees, revenue), HQ, key products/services
2. TECHNOLOGY & AI: Current tech stack, known AI/ML initiatives, digital transformation status, recent tech announcements
3. HIRING SIGNALS: What AI/ML/data roles are they hiring for? What does this tell us about their AI strategy?
4. COMPETITIVE LANDSCAPE: Top 3-5 competitors, relative positioning, market share if known
5. RECENT NEWS: Major developments in last 12 months (partnerships, acquisitions, product launches)
6. LEADERSHIP: CEO and key tech/AI leaders, their backgrounds and stated AI vision
7. STRENGTHS & WEAKNESSES: Based on public perception, analyst reports, employee reviews

Be factual. Use real data from your training. Flag uncertainty.
Return as structured JSON.`,
    { json: true }
  );
}
