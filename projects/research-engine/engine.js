#!/usr/bin/env node
// Research Engine — Main Orchestrator
import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';
import { fetchArxiv } from './sources/arxiv.js';
import { fetchHackerNews } from './sources/hackernews.js';
import { fetchReddit } from './sources/reddit.js';
import { fetchGitHub } from './sources/github.js';
import { fetchRSS } from './sources/rss.js';
import { analyze } from './analyzer.js';
import { render } from './renderer.js';

const __dirname = path.dirname(fileURLToPath(import.meta.url));

// Parse CLI args
const args = process.argv.slice(2);
const daysBack = parseInt(args.find(a => a.startsWith('--days='))?.split('=')[1]) || 2;
const sourceFilter = args.find(a => a.startsWith('--source='))?.split('=')[1];

console.log(`\n🚀 Research Engine — Scanning for bleeding-edge signals...\n`);
console.log(`📅 Timeframe: Last ${daysBack} days`);
if (sourceFilter) console.log(`🎯 Source filter: ${sourceFilter}`);
console.log('');

async function main() {
  const startTime = Date.now();

  try {
    // Phase 1: Fetch data from all sources (PARALLEL)
    console.log('📡 Phase 1: Fetching data...\n');

    const sources = {
      arxiv: !sourceFilter || sourceFilter === 'arxiv' ? fetchArxiv(daysBack) : Promise.resolve([]),
      hackernews: !sourceFilter || sourceFilter === 'hackernews' ? fetchHackerNews(daysBack) : Promise.resolve([]),
      reddit: !sourceFilter || sourceFilter === 'reddit' ? fetchReddit(daysBack) : Promise.resolve([]),
      github: !sourceFilter || sourceFilter === 'github' ? fetchGitHub(daysBack) : Promise.resolve([]),
      rss: !sourceFilter || sourceFilter === 'rss' ? fetchRSS(daysBack) : Promise.resolve([])
    };

    const rawData = {
      arxiv: await sources.arxiv,
      hackernews: await sources.hackernews,
      reddit: await sources.reddit,
      github: await sources.github,
      rss: await sources.rss
    };

    const totalItems = Object.values(rawData).reduce((sum, arr) => sum + arr.length, 0);
    console.log(`\n✅ Collected ${totalItems} items total\n`);

    if (totalItems === 0) {
      console.error('❌ No data collected. Exiting.');
      process.exit(1);
    }

    // Phase 2: Analyze with GPT-4o
    console.log('🧠 Phase 2: AI Analysis...\n');
    const analysis = await analyze(rawData);

    // Phase 3: Render HTML
    console.log('\n🎨 Phase 3: Rendering report...\n');
    const reportDate = new Date().toISOString().split('T')[0];
    const html = render(analysis, rawData, reportDate);

    // Phase 4: Save output
    const outputDir = path.join(__dirname, 'output');
    if (!fs.existsSync(outputDir)) {
      fs.mkdirSync(outputDir, { recursive: true });
    }

    const outputPath = path.join(outputDir, `research-${reportDate}.html`);
    fs.writeFileSync(outputPath, html, 'utf-8');

    // Also save raw data as JSON for debugging
    const jsonPath = path.join(outputDir, `research-${reportDate}.json`);
    fs.writeFileSync(jsonPath, JSON.stringify({
      meta: {
        generated: new Date().toISOString(),
        daysBack,
        totalItems
      },
      rawData,
      analysis
    }, null, 2), 'utf-8');

    const duration = ((Date.now() - startTime) / 1000).toFixed(1);
    console.log(`✅ Report generated in ${duration}s`);
    console.log(`📄 HTML: ${outputPath}`);
    console.log(`📊 JSON: ${jsonPath}`);
    console.log('');

    // Open in browser (macOS)
    if (process.platform === 'darwin') {
      console.log('🌐 Opening in browser...\n');
      const { exec } = await import('child_process');
      exec(`open "${outputPath}"`);
    }

  } catch (error) {
    console.error('\n❌ Engine failed:', error.message);
    console.error(error.stack);
    process.exit(1);
  }
}

main();
