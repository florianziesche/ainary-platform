// GitHub Trending Scraper
import axios from 'axios';
import * as cheerio from 'cheerio';

export async function fetchGitHub(daysBack = 2) {
  const results = [];
  const timeframes = daysBack <= 1 ? ['daily'] : daysBack <= 7 ? ['daily', 'weekly'] : ['daily', 'weekly', 'monthly'];

  try {
    for (const timeframe of timeframes) {
      const url = `https://github.com/trending?since=${timeframe}&spoken_language_code=en`;
      
      const response = await axios.get(url, {
        headers: {
          'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
        }
      });

      const $ = cheerio.load(response.data);
      
      $('article.Box-row').each((i, elem) => {
        const $elem = $(elem);
        
        const repoPath = $elem.find('h2 a').attr('href');
        if (!repoPath) return;

        const title = $elem.find('h2 a').text().replace(/\s+/g, ' ').trim();
        const description = $elem.find('p').text().trim() || 'No description';
        const language = $elem.find('[itemprop="programmingLanguage"]').text().trim() || 'Unknown';
        const stars = $elem.find('svg.octicon-star').parent().text().trim().replace(',', '');
        const todayStars = $elem.find('svg.octicon-star').closest('span').next().text().trim().replace(',', '').replace(' stars today', '').replace(' stars this week', '').replace(' stars this month', '');

        results.push({
          source: 'github',
          title: title.replace('/', ' / '),
          url: `https://github.com${repoPath}`,
          description,
          language,
          stars: parseInt(stars) || 0,
          todayStars: parseInt(todayStars) || 0,
          timeframe,
          published: new Date().toISOString() // Trending has no timestamp
        });
      });
    }

    // Remove duplicates (same repo in multiple timeframes)
    const unique = [];
    const seen = new Set();
    for (const item of results) {
      if (!seen.has(item.url)) {
        seen.add(item.url);
        unique.push(item);
      }
    }

    console.log(`✅ GitHub: ${unique.length} trending repos`);
    return unique.slice(0, 20); // Top 20
  } catch (error) {
    console.error('❌ GitHub fetch failed:', error.message);
    return [];
  }
}
