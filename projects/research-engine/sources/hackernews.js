// Hacker News Firebase API
import axios from 'axios';

const HN_API = 'https://hacker-news.firebaseio.com/v0';
const AI_KEYWORDS = ['AI', 'GPT', 'LLM', 'machine learning', 'neural', 'transformer', 'diffusion', 'agent', 'AGI', 'anthropic', 'openai', 'claude', 'chatgpt'];

export async function fetchHackerNews(daysBack = 2) {
  const results = [];
  const since = Date.now() - (daysBack * 24 * 60 * 60 * 1000);

  try {
    // Fetch top stories + show HN
    const [topResponse, showResponse] = await Promise.all([
      axios.get(`${HN_API}/topstories.json`),
      axios.get(`${HN_API}/showstories.json`)
    ]);

    const storyIds = [...topResponse.data.slice(0, 100), ...showResponse.data.slice(0, 50)];
    
    // Fetch story details in parallel (batches of 20)
    const batchSize = 20;
    for (let i = 0; i < storyIds.length; i += batchSize) {
      const batch = storyIds.slice(i, i + batchSize);
      const stories = await Promise.all(
        batch.map(id => axios.get(`${HN_API}/item/${id}.json`).catch(() => null))
      );

      for (const response of stories) {
        if (!response || !response.data) continue;
        const story = response.data;
        
        // Filter by time
        if (story.time * 1000 < since) continue;
        
        // Filter by AI/ML keywords
        const text = `${story.title} ${story.text || ''}`.toLowerCase();
        const hasKeyword = AI_KEYWORDS.some(kw => text.includes(kw.toLowerCase()));
        if (!hasKeyword) continue;

        results.push({
          source: 'hackernews',
          title: story.title,
          url: story.url || `https://news.ycombinator.com/item?id=${story.id}`,
          text: story.text || '',
          score: story.score || 0,
          comments: story.descendants || 0,
          published: new Date(story.time * 1000).toISOString(),
          hn_url: `https://news.ycombinator.com/item?id=${story.id}`
        });
      }
    }

    // Sort by score
    results.sort((a, b) => b.score - a.score);

    console.log(`✅ Hacker News: ${results.length} AI/ML stories from last ${daysBack} days`);
    return results.slice(0, 30); // Top 30
  } catch (error) {
    console.error('❌ Hacker News fetch failed:', error.message);
    return [];
  }
}
