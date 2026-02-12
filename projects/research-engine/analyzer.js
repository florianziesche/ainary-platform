// Analyzer — GPT-4o Intelligence Synthesis
import OpenAI from 'openai';

const openai = new OpenAI({
  apiKey: process.env.OPENAI_API_KEY
});

export async function analyze(allSources) {
  const { arxiv, hackernews, reddit, github, rss } = allSources;

  console.log('\n🧠 Analyzing signals...');

  const prompt = `You are an AI research analyst tracking bleeding-edge AI/Tech trends BEFORE they go mainstream.

You have collected data from 5 sources over the last 48-72 hours:

**ArXiv Papers (${arxiv.length}):**
${arxiv.map(p => `- ${p.title} (${p.category})\n  ${p.abstract}`).join('\n\n')}

**Hacker News (${hackernews.length}):**
${hackernews.map(h => `- ${h.title} (${h.score} points, ${h.comments} comments)\n  ${h.url}`).join('\n\n')}

**Reddit (${reddit.length}):**
${reddit.map(r => `- r/${r.subreddit}: ${r.title} (${r.score} upvotes, ${r.comments} comments)\n  ${r.selftext}`).join('\n\n')}

**GitHub Trending (${github.length}):**
${github.map(g => `- ${g.title} (${g.language}, ${g.todayStars} stars recently)\n  ${g.description}`).join('\n\n')}

**VC Blogs (${rss.length}):**
${rss.map(b => `- ${b.feed}: ${b.title}\n  ${b.excerpt}`).join('\n\n')}

---

Your task: Create a curated Intelligence Brief with the following sections:

1. **Top 5 "Emerging Signals"** — What's appearing NOW that most people haven't noticed yet? Look for:
   - New techniques/architectures in ArXiv
   - Projects gaining sudden traction on GitHub
   - Ideas getting discussed across multiple sources
   Format: { title, why_it_matters, signal_strength (1-5), sources: ["arxiv", "reddit"] }

2. **Top 3 "Deep Dives"** — What deserves closer investigation?
   - Technical breakthroughs that could shift the field
   - Products/companies gaining momentum
   - Contrarian takes that might be right
   Format: { title, summary, why_investigate, sources: [] }

3. **"Contrarian Corner"** — What is everyone IGNORING that could be important?
   - Unpopular opinions with strong reasoning
   - Old ideas becoming relevant again
   - Risks/limitations nobody talks about
   Format: { idea, why_ignored, why_might_matter }

4. **Cross-Source Patterns** — What themes appear in 2+ sources?
   - Same concept discussed in papers + Reddit
   - VC interest matching GitHub activity
   - Academic research → startup application
   Format: { pattern, sources: [], significance }

Return ONLY valid JSON with this exact structure:
{
  "emerging_signals": [{ title, why_it_matters, signal_strength, sources }],
  "deep_dives": [{ title, summary, why_investigate, sources }],
  "contrarian_corner": [{ idea, why_ignored, why_might_matter }],
  "cross_source_patterns": [{ pattern, sources, significance }],
  "meta": {
    "total_items_analyzed": ${arxiv.length + hackernews.length + reddit.length + github.length + rss.length},
    "timeframe": "last 48-72 hours",
    "confidence": "high|medium|low"
  }
}`;

  try {
    const response = await openai.chat.completions.create({
      model: 'gpt-4o',
      messages: [
        { role: 'system', content: 'You are an expert AI research analyst. Return only valid JSON.' },
        { role: 'user', content: prompt }
      ],
      temperature: 0.7,
      response_format: { type: 'json_object' }
    });

    const analysis = JSON.parse(response.choices[0].message.content);
    console.log('✅ Analysis complete');
    return analysis;
  } catch (error) {
    console.error('❌ Analysis failed:', error.message);
    throw error;
  }
}
