// Reddit JSON API (no auth needed)
import axios from 'axios';

const SUBREDDITS = ['MachineLearning', 'LocalLLaMA', 'artificial'];

export async function fetchReddit(daysBack = 2) {
  const results = [];
  const since = Date.now() - (daysBack * 24 * 60 * 60 * 1000);

  try {
    for (const subreddit of SUBREDDITS) {
      const url = `https://www.reddit.com/r/${subreddit}/hot.json?limit=50`;
      
      const response = await axios.get(url, {
        headers: {
          'User-Agent': 'ResearchEngine/1.0 (Early warning system for AI trends)'
        }
      });

      const posts = response.data?.data?.children || [];

      for (const post of posts) {
        const data = post.data;
        const created = data.created_utc * 1000;
        
        if (created < since) continue;

        results.push({
          source: 'reddit',
          subreddit: data.subreddit,
          title: data.title,
          url: data.url,
          selftext: data.selftext?.substring(0, 300) || '',
          score: data.score,
          comments: data.num_comments,
          published: new Date(created).toISOString(),
          reddit_url: `https://reddit.com${data.permalink}`
        });
      }
    }

    // Sort by score
    results.sort((a, b) => b.score - a.score);

    console.log(`✅ Reddit: ${results.length} hot posts from last ${daysBack} days`);
    return results.slice(0, 30); // Top 30
  } catch (error) {
    console.error('❌ Reddit fetch failed:', error.message);
    return [];
  }
}
