// RSS Feed Parser for VC Blogs
import Parser from 'rss-parser';

const VC_FEEDS = [
  { name: 'a16z', url: 'https://a16z.com/feed/' },
  { name: 'Sequoia', url: 'https://www.sequoiacap.com/blog/feed/' },
  { name: 'Y Combinator', url: 'https://www.ycombinator.com/blog/feed' },
  { name: 'Andreessen Horowitz', url: 'https://a16z.com/tag/artificial-intelligence/feed/' },
  { name: 'Greylock', url: 'https://greylock.com/feed/' }
];

export async function fetchRSS(daysBack = 7) {
  const results = [];
  const since = new Date();
  since.setDate(since.getDate() - daysBack);

  const parser = new Parser({
    timeout: 5000,
    customFields: {
      item: ['description', 'content:encoded']
    }
  });

  try {
    for (const feed of VC_FEEDS) {
      try {
        const parsed = await parser.parseURL(feed.url);
        
        for (const item of parsed.items) {
          const pubDate = new Date(item.pubDate || item.isoDate);
          if (pubDate < since) continue;

          // Filter AI/Tech keywords
          const text = `${item.title} ${item.contentSnippet || ''}`.toLowerCase();
          const hasAI = text.includes('ai') || text.includes('machine learning') || text.includes('llm') || text.includes('artificial intelligence');
          
          if (!hasAI) continue;

          results.push({
            source: 'rss',
            feed: feed.name,
            title: item.title,
            url: item.link,
            excerpt: (item.contentSnippet || item.description || '').substring(0, 300) + '...',
            published: item.pubDate || item.isoDate,
            author: item.creator || feed.name
          });
        }
      } catch (feedError) {
        console.error(`⚠️  ${feed.name} feed failed:`, feedError.message);
      }
    }

    console.log(`✅ RSS: ${results.length} VC blog posts from last ${daysBack} days`);
    return results;
  } catch (error) {
    console.error('❌ RSS fetch failed:', error.message);
    return [];
  }
}
