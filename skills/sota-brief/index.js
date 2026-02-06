/**
 * SOTA Brief Skill for OpenClaw
 * Generates weekly state-of-the-art briefs across 4 key verticals
 *
 * Invoked by cron job with taskDescription from SKILL.md
 */

const fs = require('fs');
const path = require('path');

/**
 * Get current week date (YYYY-MM-DD format)
 */
function getWeekDate() {
  const today = new Date();
  return today.toISOString().split('T')[0];
}

/**
 * Get next week date
 */
function getNextWeekDate() {
  const today = new Date();
  const nextWeek = new Date(today.getTime() + 7 * 24 * 60 * 60 * 1000);
  return nextWeek.toISOString().split('T')[0];
}

/**
 * Generate the SOTA brief prompt for OpenClaw agent
 */
function generateSOTAPrompt() {
  const weekDate = getWeekDate();
  const nextDate = getNextWeekDate();
  const timestamp = new Date().toISOString().replace('T', ' ').slice(0, -5) + ' UTC';

  return `# Weekly SOTA Brief Generation

Generate a comprehensive weekly SOTA brief for the week of ${weekDate}.

## Task Overview
Create a state-of-the-art brief covering the latest developments in:
1. **Legal AI** - Focus on EvenUp, CaseMark, Supio, Westlaw, LexisNexis, and regulatory changes
2. **Manufacturing AI** - CNC automation, Industry 4.0, AI in manufacturing processes
3. **VC/Investment** - Funding announcements, market movements, LP activity
4. **Agentic Systems** - New agent frameworks, Claude releases, reasoning models

## Research Process

### Step 1: Search Each Vertical
For Legal AI:
- Search: "Legal AI EvenUp CaseMark 2026"
- Search: "AI legal tech news January 2026"
- Search: "lawyer AI tools 2026"

For Manufacturing AI:
- Search: "CNC software AI 2026"
- Search: "Industry 4.0 AI 2026"
- Search: "manufacturing automation latest 2026"

For VC/Investment:
- Search: "AI startup funding 2026"
- Search: "venture capital news 2026"
- Search: "Series A AI companies 2026"

For Agentic Systems:
- Search: "Claude 3.5 release 2026"
- Search: "AI agent frameworks 2026"
- Search: "reasoning models latest 2026"

### Step 2: Validate Sources
- For each item found, fetch at least 2 independent sources
- Prioritize official announcements and primary sources
- Note publication dates (prioritize items <7 days old)
- Record confidence level based on source quality and agreement

### Step 3: Format Output

Save the brief to: \`/Users/florianziesche/.openclaw/workspace/sota-${weekDate}.md\`

Use this exact format:

\`\`\`markdown
# SOTA Brief — ${weekDate}

## Legal AI

### [Item Title]
- **What:** [1-2 sentence description]
- **Why it matters:** [1 sentence about business impact for Florian]
- **Sources:** [URL 1], [URL 2]
- **Confidence:** High / Medium / Low

[Include 3-5 items for this vertical]

## Manufacturing AI

[Same format as Legal AI, 3-5 items]

## VC/Investment

[Same format, 3-5 items]

## Agentic Systems

[Same format, 3-5 items]

---

## Summary

[2-3 sentence synthesis highlighting the biggest trend across all verticals and why it matters for Florian's business trajectory]

**Generated:** ${timestamp}
**Next brief:** ${nextDate}
**Confidence methodology:** Items marked "High" have 2+ independent sources. "Medium" have 1-2 sources with good authority. "Low" have single source or emerging reports.
\`\`\`

## Quality Criteria

Before finalizing:
- [ ] 16-20 total items (4-5 per vertical)
- [ ] All items have at least 1 source URL
- [ ] Confidence ratings are truthful (not optimistic)
- [ ] Each item explains business relevance (why Florian cares)
- [ ] File is 2-4 KB (concise and scannable)
- [ ] Items are sorted by confidence and recency within each vertical
- [ ] No duplicate items across verticals
- [ ] Summary ties findings together into narrative

## Confidence Rating Guide

- **High (2+ sources agreeing):** Official announcements, major publications, multiple confirmations
- **Medium (1-2 quality sources):** Single reputable source, or reports from good publications
- **Low (1 source or unconfirmed):** Emerging reports, single announcement, unofficial sources

## Priority Items to Look For

**Legal AI:** Regulatory changes, feature launches, competitive moves, pricing updates
**Manufacturing AI:** Product releases, customer wins, partnership announcements, technical breakthroughs
**VC/Investment:** Mega-rounds, sector trends, fund closures, LP movements
**Agentic Systems:** Model releases, benchmark improvements, new frameworks, reasoning advances

## Notes for This Week

- Include any breaking news even if <7 days old
- Flag acquisitions or partnerships in all verticals
- Note any moves by OpenAI, Google, Anthropic in manufacturing/legal spaces
- Look for convergence of technologies (e.g., agentic systems + legal AI)

---

**Now generate the brief. Start with your research, validate sources, then compile into the markdown format above.**
`;
}

/**
 * Main execution function
 * This is called by OpenClaw when the cron job runs
 */
async function main() {
  try {
    const weekDate = getWeekDate();
    const skillDir = path.join(
      process.env.HOME || '/Users/florianziesche',
      '.openclaw/workspace/skills/sota-brief'
    );

    // Ensure directory exists
    if (!fs.existsSync(skillDir)) {
      fs.mkdirSync(skillDir, { recursive: true });
    }

    // Log that we're starting
    console.log(`[SOTA] Starting SOTA brief generation for ${weekDate}`);

    // Generate and return the prompt for the agent to execute
    const prompt = generateSOTAPrompt();

    console.log(`[SOTA] Prompt generated. Length: ${prompt.length} characters`);
    console.log(`[SOTA] Expected output file: /Users/florianziesche/.openclaw/workspace/sota-${weekDate}.md`);

    // Return the prompt that the agent should execute
    // This will be printed to stdout and used as the agent's instruction
    console.log('\n' + prompt);

    return 0;
  } catch (error) {
    console.error('[SOTA] Error during SOTA generation:', error);
    return 1;
  }
}

// Export for OpenClaw to call
module.exports = { main, generateSOTAPrompt, getWeekDate, getNextWeekDate };

// Run if called directly
if (require.main === module) {
  main().then(code => process.exit(code));
}
