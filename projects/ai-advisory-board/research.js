/**
 * Research Phase - Knowledge Structure Builder
 * Imports sources from Research Engine and builds context for advisors
 */

const axios = require('axios');
const { parseStringPromise } = require('xml2js');
const cheerio = require('cheerio');

// Import Research Engine source patterns (adapted for CommonJS)
const AI_KEYWORDS = ['AI', 'GPT', 'LLM', 'machine learning', 'neural', 'transformer', 'diffusion', 'agent', 'AGI', 'anthropic', 'openai', 'claude', 'chatgpt'];

async function fetchArxiv(query, daysBack = 2) {
  const results = [];
  const since = new Date();
  since.setDate(since.getDate() - daysBack);

  try {
    const searchQuery = `all:${query}`;
    const url = `http://export.arxiv.org/api/query?search_query=${encodeURIComponent(searchQuery)}&sortBy=submittedDate&sortOrder=descending&max_results=20`;
    
    const response = await axios.get(url);
    const parsed = await parseStringPromise(response.data);
    
    if (!parsed.feed || !parsed.feed.entry) return [];

    for (const entry of parsed.feed.entry) {
      const published = new Date(entry.published[0]);
      if (published < since) continue;

      results.push({
        source: 'arxiv',
        title: entry.title[0].replace(/\s+/g, ' ').trim(),
        url: entry.id[0],
        abstract: entry.summary[0].replace(/\s+/g, ' ').trim().substring(0, 200),
        published: entry.published[0]
      });
    }

    return results;
  } catch (error) {
    console.error('⚠️  ArXiv fetch failed:', error.message);
    return [];
  }
}

async function fetchHackerNews(keywords, daysBack = 2) {
  const HN_API = 'https://hacker-news.firebaseio.com/v0';
  const results = [];
  const since = Date.now() - (daysBack * 24 * 60 * 60 * 1000);

  try {
    const topResponse = await axios.get(`${HN_API}/topstories.json`);
    const storyIds = topResponse.data.slice(0, 100);
    
    const batchSize = 20;
    for (let i = 0; i < Math.min(storyIds.length, 60); i += batchSize) {
      const batch = storyIds.slice(i, i + batchSize);
      const stories = await Promise.all(
        batch.map(id => axios.get(`${HN_API}/item/${id}.json`).catch(() => null))
      );

      for (const response of stories) {
        if (!response || !response.data) continue;
        const story = response.data;
        
        if (story.time * 1000 < since) continue;
        
        const text = `${story.title} ${story.text || ''}`.toLowerCase();
        const hasKeyword = keywords.some(kw => text.includes(kw.toLowerCase()));
        if (!hasKeyword) continue;

        results.push({
          source: 'hackernews',
          title: story.title,
          url: story.url || `https://news.ycombinator.com/item?id=${story.id}`,
          score: story.score || 0,
          published: new Date(story.time * 1000).toISOString()
        });
      }
    }

    return results.sort((a, b) => b.score - a.score).slice(0, 10);
  } catch (error) {
    console.error('⚠️  Hacker News fetch failed:', error.message);
    return [];
  }
}

async function fetchReddit(keywords, daysBack = 2) {
  const SUBREDDITS = ['MachineLearning', 'LocalLLaMA', 'artificial', 'startups', 'entrepreneur'];
  const results = [];
  const since = Date.now() - (daysBack * 24 * 60 * 60 * 1000);

  try {
    for (const subreddit of SUBREDDITS.slice(0, 3)) {
      const url = `https://www.reddit.com/r/${subreddit}/hot.json?limit=30`;
      
      const response = await axios.get(url, {
        headers: {
          'User-Agent': 'AdvisoryBoard/2.0 (Research-backed decision support)'
        }
      });

      const posts = response.data?.data?.children || [];

      for (const post of posts) {
        const data = post.data;
        const created = data.created_utc * 1000;
        
        if (created < since) continue;

        const text = `${data.title} ${data.selftext || ''}`.toLowerCase();
        const hasKeyword = keywords.some(kw => text.includes(kw.toLowerCase()));
        if (!hasKeyword) continue;

        results.push({
          source: 'reddit',
          title: data.title,
          url: `https://reddit.com${data.permalink}`,
          score: data.score,
          published: new Date(created).toISOString()
        });
      }
    }

    return results.sort((a, b) => b.score - a.score).slice(0, 10);
  } catch (error) {
    console.error('⚠️  Reddit fetch failed:', error.message);
    return [];
  }
}

async function fetchGitHub(keywords, daysBack = 2) {
  const results = [];

  try {
    const url = 'https://github.com/trending?since=daily&spoken_language_code=en';
    
    const response = await axios.get(url, {
      headers: {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
      }
    });

    const $ = cheerio.load(response.data);
    
    $('article.Box-row').slice(0, 15).each((i, elem) => {
      const $elem = $(elem);
      
      const repoPath = $elem.find('h2 a').attr('href');
      if (!repoPath) return;

      const title = $elem.find('h2 a').text().replace(/\s+/g, ' ').trim();
      const description = $elem.find('p').text().trim() || '';
      
      const text = `${title} ${description}`.toLowerCase();
      const hasKeyword = keywords.some(kw => text.includes(kw.toLowerCase()));
      if (!hasKeyword) return;

      results.push({
        source: 'github',
        title: title.replace('/', ' / '),
        url: `https://github.com${repoPath}`,
        description,
        published: new Date().toISOString()
      });
    });

    return results.slice(0, 8);
  } catch (error) {
    console.error('⚠️  GitHub fetch failed:', error.message);
    return [];
  }
}

function extractKeywords(question) {
  // Extract meaningful keywords from the question
  const commonWords = ['should', 'can', 'what', 'how', 'why', 'when', 'where', 'the', 'a', 'an', 'is', 'are', 'do', 'does', 'my', 'i', 'we', 'or', 'and', 'to', 'in', 'on', 'at'];
  
  const words = question
    .toLowerCase()
    .replace(/[^\w\s]/g, ' ')
    .split(/\s+/)
    .filter(w => w.length > 3 && !commonWords.includes(w));

  // Add AI/ML keywords if relevant
  const lowerQuestion = question.toLowerCase();
  const extraKeywords = [];
  if (lowerQuestion.includes('ai') || lowerQuestion.includes('artificial intelligence')) {
    extraKeywords.push('AI', 'artificial intelligence', 'machine learning');
  }
  if (lowerQuestion.includes('business') || lowerQuestion.includes('startup')) {
    extraKeywords.push('startup', 'business', 'entrepreneur');
  }
  if (lowerQuestion.includes('consulting')) {
    extraKeywords.push('consulting', 'freelance', 'agency');
  }

  return [...new Set([...words, ...extraKeywords])];
}

async function runResearch(question, daysBack = 2) {
  console.log('🔍 Phase 1: Research...');
  console.log('   Extracting keywords...');
  
  const keywords = extractKeywords(question);
  console.log(`   Keywords: ${keywords.slice(0, 5).join(', ')}${keywords.length > 5 ? '...' : ''}`);
  
  console.log('   Scanning sources (parallel)...');
  
  const startTime = Date.now();

  // Fetch from all sources in parallel
  const [arxivResults, hnResults, redditResults, githubResults] = await Promise.all([
    fetchArxiv(keywords.join(' OR '), daysBack),
    fetchHackerNews(keywords, daysBack),
    fetchReddit(keywords, daysBack),
    fetchGitHub(keywords, daysBack)
  ]);

  const allResults = {
    arxiv: arxivResults,
    hackernews: hnResults,
    reddit: redditResults,
    github: githubResults
  };

  const totalItems = Object.values(allResults).reduce((sum, arr) => sum + arr.length, 0);
  const duration = ((Date.now() - startTime) / 1000).toFixed(1);

  console.log(`   ✓ Collected ${totalItems} items in ${duration}s`);
  console.log(`   ArXiv: ${arxivResults.length} | HN: ${hnResults.length} | Reddit: ${redditResults.length} | GitHub: ${githubResults.length}`);

  return {
    keywords,
    sources: allResults,
    totalItems,
    timestamp: new Date().toISOString()
  };
}

async function buildKnowledgeStructure(question, researchData, openai) {
  console.log('\n🧠 Building Knowledge Structure with GPT-4o...');

  if (researchData.totalItems === 0) {
    console.log('   ⚠️  No research data - skipping knowledge structure');
    return {
      keyFacts: ['Limited recent research data available for this topic.'],
      recentDevelopments: [],
      openQuestions: [],
      counterArguments: [],
      confidence: 'low'
    };
  }

  // Prepare research summary for GPT
  const researchSummary = `
QUESTION: ${question}

RECENT RESEARCH FINDINGS (last ${researchData.keywords.length} days):

ArXiv Papers (${researchData.sources.arxiv.length}):
${researchData.sources.arxiv.map(r => `- ${r.title}\n  ${r.abstract}`).join('\n')}

Hacker News (${researchData.sources.hackernews.length}):
${researchData.sources.hackernews.slice(0, 5).map(r => `- ${r.title} (${r.score} pts)`).join('\n')}

Reddit Discussions (${researchData.sources.reddit.length}):
${researchData.sources.reddit.slice(0, 5).map(r => `- ${r.title} (${r.score} pts)`).join('\n')}

GitHub Trending (${researchData.sources.github.length}):
${researchData.sources.github.map(r => `- ${r.title}: ${r.description}`).join('\n')}
`.trim();

  try {
    const completion = await openai.chat.completions.create({
      model: 'gpt-4o',
      messages: [
        {
          role: 'system',
          content: `You are a research analyst building a knowledge structure from recent data.

Analyze the research findings and create a structured summary with:
1. KEY FACTS: 3-5 established facts relevant to the question
2. RECENT DEVELOPMENTS: 2-4 new trends or changes in the last week
3. OPEN QUESTIONS: 2-3 uncertainties or debated topics
4. COUNTER-ARGUMENTS: 2-3 opposing viewpoints or risks

Be concise. Each point should be 1-2 sentences max. Focus on insights that would help advisors give informed recommendations.`
        },
        {
          role: 'user',
          content: researchSummary
        }
      ],
      temperature: 0.3,
      max_tokens: 800
    });

    const response = completion.choices[0].message.content;
    
    // Parse the response into structured data
    const sections = {
      keyFacts: extractSection(response, 'KEY FACTS'),
      recentDevelopments: extractSection(response, 'RECENT DEVELOPMENTS'),
      openQuestions: extractSection(response, 'OPEN QUESTIONS'),
      counterArguments: extractSection(response, 'COUNTER'),
      rawResponse: response,
      confidence: researchData.totalItems > 10 ? 'high' : researchData.totalItems > 5 ? 'medium' : 'low'
    };

    console.log(`   ✓ Knowledge structure built (confidence: ${sections.confidence})`);

    return sections;
  } catch (error) {
    console.error('   ❌ Knowledge structure build failed:', error.message);
    return {
      keyFacts: ['Research analysis unavailable'],
      recentDevelopments: [],
      openQuestions: [],
      counterArguments: [],
      rawResponse: 'Error building knowledge structure',
      confidence: 'low'
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

module.exports = {
  runResearch,
  buildKnowledgeStructure,
  extractKeywords
};
