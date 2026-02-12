// ArXiv API Parser — Atom Feed
import axios from 'axios';
import { parseStringPromise } from 'xml2js';

const CATEGORIES = ['cs.AI', 'cs.CL', 'cs.MA', 'cs.LG'];

export async function fetchArxiv(daysBack = 2) {
  const results = [];
  const since = new Date();
  since.setDate(since.getDate() - daysBack);

  try {
    for (const category of CATEGORIES) {
      const query = `cat:${category}`;
      const url = `http://export.arxiv.org/api/query?search_query=${encodeURIComponent(query)}&sortBy=submittedDate&sortOrder=descending&max_results=50`;
      
      const response = await axios.get(url);
      const parsed = await parseStringPromise(response.data);
      
      if (!parsed.feed || !parsed.feed.entry) continue;

      for (const entry of parsed.feed.entry) {
        const published = new Date(entry.published[0]);
        if (published < since) continue;

        results.push({
          source: 'arxiv',
          title: entry.title[0].replace(/\s+/g, ' ').trim(),
          url: entry.id[0],
          abstract: entry.summary[0].replace(/\s+/g, ' ').trim().substring(0, 300) + '...',
          authors: entry.author?.map(a => a.name[0]).join(', ') || 'Unknown',
          category,
          published: entry.published[0],
          score: 0 // Will be calculated by analyzer
        });
      }
    }

    console.log(`✅ ArXiv: ${results.length} papers from last ${daysBack} days`);
    return results;
  } catch (error) {
    console.error('❌ ArXiv fetch failed:', error.message);
    return [];
  }
}
