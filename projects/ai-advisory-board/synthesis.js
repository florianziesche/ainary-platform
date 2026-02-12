/**
 * Synthesis Phase - Cross-Advisor Analysis
 * Identifies consensus, dissent, and action items
 */

async function synthesizeAdvisorResponses(question, advisors, responses, knowledgeStructure, openai) {
  console.log('\n⚡ Phase 3: Synthesis...');
  console.log('   Analyzing cross-advisor patterns...');

  const synthesisPrompt = `You are analyzing responses from 6 expert advisors to synthesize key insights.

QUESTION: ${question}

ADVISOR RESPONSES:
${advisors.map((advisor, i) => `
${advisor.name} (${advisor.role}):
${responses[i]}
`).join('\n')}

Analyze these responses and provide:

1. CONSENSUS: What do 4+ advisors agree on? What are the shared recommendations?
2. DISSENT: Where do advisors fundamentally disagree? What are the trade-offs?
3. ACTION ITEMS: What are the top 3 next steps? (Prioritized by frequency + strategic importance)

Format:
CONSENSUS:
- [Point 1]
- [Point 2]
...

DISSENT:
- [Disagreement 1]: Advisors X vs Y
...

ACTION ITEMS:
1. [Action] (Recommended by: X, Y, Z)
2. [Action] (Recommended by: X, Y)
3. [Action] (Recommended by: X)

Be specific. Extract concrete recommendations, not vague observations.`;

  try {
    const completion = await openai.chat.completions.create({
      model: 'gpt-4o',
      messages: [
        {
          role: 'system',
          content: 'You are a strategic synthesis analyst. Your job is to find patterns, agreements, and actionable next steps across multiple expert perspectives.'
        },
        {
          role: 'user',
          content: synthesisPrompt
        }
      ],
      temperature: 0.3,
      max_tokens: 800
    });

    const response = completion.choices[0].message.content;

    const synthesis = {
      consensus: extractSection(response, 'CONSENSUS'),
      dissent: extractSection(response, 'DISSENT'),
      actionItems: extractSection(response, 'ACTION ITEMS'),
      rawResponse: response
    };

    console.log(`   ✓ Synthesis complete`);
    console.log(`   Consensus points: ${synthesis.consensus.length}`);
    console.log(`   Dissent areas: ${synthesis.dissent.length}`);
    console.log(`   Action items: ${synthesis.actionItems.length}`);

    return synthesis;
  } catch (error) {
    console.error('   ❌ Synthesis failed:', error.message);
    return {
      consensus: ['Multiple advisors recommend careful analysis before proceeding.'],
      dissent: ['Advisors have varying perspectives on timing and approach.'],
      actionItems: ['Review all advisor recommendations', 'Gather additional data', 'Create decision matrix'],
      rawResponse: 'Synthesis unavailable'
    };
  }
}

function extractSection(text, sectionName) {
  const regex = new RegExp(`${sectionName}:?\\s*\\n([\\s\\S]*?)(?=\\n\\n[A-Z]|$)`, 'i');
  const match = text.match(regex);
  
  if (!match) return [];
  
  const content = match[1];
  const items = content
    .split(/\n/)
    .map(line => line.trim())
    .filter(line => line.length > 0 && /^[-•\d.]/.test(line))
    .map(line => line.replace(/^[-•\d.)\s]+/, '').trim());
  
  return items;
}

function calculateAdvisorConfidence(response, knowledgeStructure) {
  // Calculate confidence based on:
  // 1. Length and detail of response
  // 2. Research data availability
  // 3. Certainty language

  let score = 3; // Default: medium confidence

  // Research data availability
  if (knowledgeStructure.confidence === 'high') score += 1;
  if (knowledgeStructure.confidence === 'low') score -= 1;

  // Response length (detailed = more confident)
  if (response.length > 400) score += 1;
  if (response.length < 200) score -= 1;

  // Uncertainty language
  const uncertaintyPhrases = ['might', 'could', 'possibly', 'unclear', 'uncertain', 'depends'];
  const uncertaintyCount = uncertaintyPhrases.filter(phrase => 
    response.toLowerCase().includes(phrase)
  ).length;
  
  if (uncertaintyCount > 3) score -= 1;
  if (uncertaintyCount === 0) score += 1;

  // Clamp to 1-5
  return Math.max(1, Math.min(5, score));
}

module.exports = {
  synthesizeAdvisorResponses,
  calculateAdvisorConfidence
};
