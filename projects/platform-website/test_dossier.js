/**
 * test_dossier.js — Comprehensive Product Spec Test (§7)
 * Tests ALL tabs, ALL sections, ALL cities against PRODUCT-SPEC.md
 * No deploy without ALL PASS.
 */

const http = require('http');
const fs = require('fs');
const path = require('path');

// ─── Local server ───
const server = http.createServer((req, res) => {
  let fp = '.' + new URL(req.url, 'http://localhost').pathname;
  const ext = path.extname(fp);
  const types = {'.html':'text/html','.json':'application/json','.css':'text/css','.js':'text/javascript'};
  fs.readFile(fp, (err, data) => {
    if (err) { res.writeHead(404); res.end('404'); return; }
    res.writeHead(200, {'Content-Type': types[ext]||'text/plain'});
    res.end(data);
  });
});

const cities = ['bamberg','regensburg','nuernberg','augsburg','erlangen','fuerth','passau','landshut'];
const PORT = 9994;

// ─── Apple Emoji regex (surrogate pairs in BMP + supplementary) ───
const APPLE_EMOJI_PATTERN = /[\u{1F300}-\u{1F9FF}\u{2600}-\u{26FF}\u{2700}-\u{27BF}\u{FE00}-\u{FE0F}\u{1FA00}-\u{1FA6F}\u{1FA70}-\u{1FAFF}]/u;

async function runTests() {
  const { chromium } = await import('playwright');
  const browser = await chromium.launch();
  const allResults = [];

  for (const city of cities) {
    const page = await browser.newPage();
    const jsErrors = [];
    page.on('pageerror', err => jsErrors.push(err.message));

    const cityResult = { city, sections: {}, jsErrors: [], pass: true };

    try {
      await page.goto(`http://localhost:${PORT}/dossier.html?city=${city}&admin`, { waitUntil: 'networkidle' });
      await page.waitForTimeout(2500);

      // ═══ §7.1 GLOBAL CHECKS ═══
      const global = await page.evaluate(() => {
        const gate = document.getElementById('auth-gate');
        const authHidden = gate ? gate.style.display === 'none' : true;
        const topbar = document.getElementById('topbar-tenant');
        const topbarText = topbar ? topbar.textContent.trim() : '';
        const bcCity = document.getElementById('bc-city');
        const breadcrumb = bcCity ? bcCity.textContent.trim() : '';
        return { authHidden, topbarText, breadcrumb };
      });

      cityResult.sections['§7.1 Global'] = [];
      if (!global.authHidden) cityResult.sections['§7.1 Global'].push('Auth gate visible');
      if (!global.topbarText) cityResult.sections['§7.1 Global'].push('No topbar text');
      if (!global.breadcrumb) cityResult.sections['§7.1 Global'].push('No breadcrumb');

      // ═══ §7.2 BRIEFING TAB ═══
      const briefing = await page.evaluate(() => {
        const el = document.getElementById('briefing-view');
        if (!el) return { error: 'briefing-view not found' };
        const text = el.textContent || '';
        const html = el.innerHTML || '';
        const undefs = (text.match(/\bundefined\b/g) || []).length;
        const nans = (text.match(/\bNaN\b/g) || []).length;
        const truncated = (text.match(/\w\.\.\.(?:\s|$)/g) || []).length; // words ending in ...

        // §1.1 Weekly Brief
        const hasWeeklyBrief = html.includes('Lage-Briefing') || html.includes('Weekly Brief') || html.includes('Priorität');
        const hasPriorities = !text.includes('0 Prioritäten');

        // §1.2 KPI Cards
        const statCards = el.querySelectorAll('.stat-card, [onclick*="switchView"]');

        // §1.4 Entity Cards — check summary truncation
        const summaryTruncations = [];
        el.querySelectorAll('[style*="cursor:pointer"]').forEach(card => {
          const t = card.textContent;
          if (t && /\w{3}\.\.\./.test(t)) summaryTruncations.push(t.substring(0, 40));
        });

        // §1.5 Wahlprognose
        const hasPrognose = html.includes('Wahlprognose') || html.includes('PROGNOSE');

        // §1.6 News
        const newsCount = (html.match(/class="news-item/g) || html.match(/Aktuelle Lage/g) || []).length;

        // §1.9 Social Intelligence
        const hasSocial = html.includes('Social') || html.includes('Instagram') || html.includes('Momentum');
        const hasSoWhat = html.includes('soWhat') || html.includes('Für Sie') || html.includes('bedeutet');

        // §1.12 Sentiment Topics OR Themen-Radar (one must exist)
        const sentimentTopics = el.querySelectorAll('.sent-topic');
        const sentTopicsWith0Posts = [];
        sentimentTopics.forEach(st => {
          const t = st.textContent;
          if (t && t.includes('0 Beiträge')) sentTopicsWith0Posts.push(t.substring(0, 30));
        });
        // Also check for Themen-Radar section as alternative
        const hasThemenRadar = html.includes('Themen-Radar') || html.includes('themen-radar');

        // Apple Emojis (only supplementary plane — ✕★☆✓ are fine cross-platform)
        const emojiMatches = text.match(/[\u{1F300}-\u{1F9FF}\u{1FA00}-\u{1FAFF}]/gu) || [];

        return {
          length: html.length,
          textLength: text.length,
          undefs, nans, truncated,
          hasWeeklyBrief, hasPriorities,
          statCardCount: statCards.length,
          summaryTruncations,
          hasPrognose,
          newsCount,
          hasSocial, hasSoWhat,
          sentimentTopicCount: sentimentTopics.length,
          sentTopicsWith0Posts,
          hasThemenRadar,
          emojiCount: emojiMatches.length
        };
      });

      cityResult.sections['§1 Briefing'] = [];
      const b = cityResult.sections['§1 Briefing'];
      if (briefing.error) { b.push(briefing.error); }
      else {
        if (briefing.length < 500) b.push(`§1 Too little content (${briefing.length} chars)`);
        if (briefing.undefs > 0) b.push(`§1 ${briefing.undefs}x "undefined" in text`);
        if (briefing.nans > 0) b.push(`§1 ${briefing.nans}x "NaN" in text`);
        if (!briefing.hasPriorities) b.push('§1.1 Shows "0 Prioritäten"');
        if (!briefing.hasWeeklyBrief) b.push('§1.1 No weekly brief section');
        if (!briefing.hasPrognose) b.push('§1.5 No Wahlprognose section');
        if (briefing.sentimentTopicCount < 3 && !briefing.hasThemenRadar) b.push(`§1.12 No Themen-Radar and only ${briefing.sentimentTopicCount} sentiment topics (need ≥3 or Themen-Radar)`);
        if (briefing.sentTopicsWith0Posts.length > 0) b.push(`§1.12 Topics with 0 posts: ${briefing.sentTopicsWith0Posts.join(', ')}`);
        if (briefing.summaryTruncations.length > 0) b.push(`§1.4 Truncated summaries: ${briefing.summaryTruncations.length}`);
        if (briefing.emojiCount > 0) b.push(`§6.4 ${briefing.emojiCount} Apple emojis found`);
      }

      // ═══ §7.2 COMPARE TAB ═══
      let compareError = null;
      try {
        await page.evaluate(() => switchView('compare'));
        await page.waitForTimeout(800);
      } catch (e) {
        compareError = e.message.substring(0, 100);
      }

      const compare = await page.evaluate(() => {
        const el = document.getElementById('compare-view');
        if (!el) return { error: 'compare-view not found' };
        const text = el.textContent || '';
        const html = el.innerHTML || '';
        const undefs = (text.match(/\bundefined\b/g) || []).length;
        const nans = (text.match(/\bNaN\b/g) || []).length;
        const hasMatrix = html.includes('matrix-table') || html.includes('Vergleichs-Matrix');
        const hasHeatmap = html.includes('Risikosignal-Heatmap');
        const hasHypotheses = html.includes('Hypothesen');

        // Count matrix cells with "—" vs "undefined"
        const matrixCells = el.querySelectorAll('td');
        let dashCells = 0;
        matrixCells.forEach(td => { if (td.textContent.trim() === '—') dashCells++; });

        return {
          length: html.length,
          undefs, nans,
          hasMatrix, hasHeatmap, hasHypotheses,
          dashCells,
          cellCount: matrixCells.length
        };
      });

      cityResult.sections['§2 Vergleich'] = [];
      const c = cityResult.sections['§2 Vergleich'];
      if (compareError) c.push(`§2 JS crash: ${compareError}`);
      if (compare.error) { c.push(compare.error); }
      else {
        if (compare.length < 500) c.push(`§2 Too little content (${compare.length} chars)`);
        if (compare.undefs > 0) c.push(`§2.1 ${compare.undefs}x "undefined"`);
        if (compare.nans > 0) c.push(`§2.1 ${compare.nans}x "NaN"`);
        if (!compare.hasMatrix) c.push('§2.1 No matrix table');
        if (!compare.hasHeatmap) c.push('§2.2 No heatmap');
        if (!compare.hasHypotheses) c.push('§2.3 No hypotheses section');
      }

      // ═══ §7.2 STRATEGY TAB ═══
      let strategyError = null;
      try {
        await page.evaluate(() => switchView('strategy'));
        await page.waitForTimeout(800);
      } catch (e) {
        strategyError = e.message.substring(0, 100);
      }

      const strategy = await page.evaluate(() => {
        const el = document.getElementById('strategy-view');
        if (!el) return { error: 'strategy-view not found' };
        const text = el.textContent || '';
        const html = el.innerHTML || '';
        const undefs = (text.match(/\bundefined\b/g) || []).length;
        const nans = (text.match(/\bNaN\b/g) || []).length;

        // §3.1 Talking Points
        const hasTalkingPoints = html.includes('Talking') || html.includes('talking') || html.includes('Gesprächspunkte');

        // §3.2 Scenarios
        const hasScenarios = html.includes('Szenari') || html.includes('scenario');

        // §3.3 Patterns
        const hasPatterns = html.includes('Muster') || html.includes('Pattern') || html.includes('pattern');
        const hasSoWhat = html.includes('Für Sie') || html.includes('soWhat') || html.includes('Cross-City');

        // Truncation check
        const truncatedTexts = [];
        el.querySelectorAll('div').forEach(div => {
          const t = div.textContent;
          // Find text that ends mid-word (3+ word chars then ...)
          if (t && /\w{3}\.\.\.\s*$/.test(t.trim()) && t.trim().length < 200) {
            truncatedTexts.push(t.trim().substring(0, 50));
          }
        });

        // Apple Emojis (only supplementary plane)
        const emojiMatches = text.match(/[\u{1F300}-\u{1F9FF}\u{1FA00}-\u{1FAFF}]/gu) || [];

        return {
          length: html.length,
          undefs, nans,
          hasTalkingPoints, hasScenarios, hasPatterns, hasSoWhat,
          truncatedTexts,
          emojiCount: emojiMatches.length
        };
      });

      cityResult.sections['§3 Strategie'] = [];
      const s = cityResult.sections['§3 Strategie'];
      if (strategyError) s.push(`§3 JS crash: ${strategyError}`);
      if (strategy.error) { s.push(strategy.error); }
      else {
        if (strategy.length < 500) s.push(`§3 Too little content (${strategy.length} chars)`);
        if (strategy.undefs > 0) s.push(`§3 ${strategy.undefs}x "undefined"`);
        if (strategy.nans > 0) s.push(`§3 ${strategy.nans}x "NaN"`);
        if (!strategy.hasTalkingPoints) s.push('§3.1 No talking points');
        if (!strategy.hasScenarios) s.push('§3.2 No scenarios');
        if (!strategy.hasPatterns) s.push('§3.3 No patterns');
        if (!strategy.hasSoWhat) s.push('§3.3 No "Für Sie"/soWhat visible');
        if (strategy.truncatedTexts.length > 0) s.push(`§6.5 ${strategy.truncatedTexts.length} truncated texts: ${strategy.truncatedTexts[0]}`);
        if (strategy.emojiCount > 0) s.push(`§6.4 ${strategy.emojiCount} Apple emojis`);
      }

      // ═══ §7.2 NETWORK TAB ═══
      let graphError = null;
      try {
        await page.evaluate(() => switchView('graph'));
        await page.waitForTimeout(800);
      } catch (e) {
        graphError = e.message.substring(0, 100);
      }

      const graph = await page.evaluate(() => {
        const el = document.getElementById('graph-view');
        if (!el) return { error: 'graph-view not found' };
        const hasSvg = !!el.querySelector('svg');
        const hasCanvas = !!el.querySelector('canvas');
        return { hasSvg, hasCanvas };
      });

      cityResult.sections['§4 Netzwerk'] = [];
      if (graphError) cityResult.sections['§4 Netzwerk'].push(`§4 JS crash: ${graphError}`);
      if (graph.error) cityResult.sections['§4 Netzwerk'].push(graph.error);
      else if (!graph.hasSvg && !graph.hasCanvas) cityResult.sections['§4 Netzwerk'].push('§4.1 No SVG or Canvas (graph not rendered)');

      // ═══ §7.2 DOSSIER TAB (Entity Detail) ═══
      let entityError = null;
      try {
        const firstKey = await page.evaluate(() => Object.keys(KB)[0]);
        if (firstKey) {
          await page.evaluate((k) => showEntity(k), firstKey);
          await page.waitForTimeout(500);
        }
      } catch (e) {
        entityError = e.message.substring(0, 100);
      }

      const entity = await page.evaluate(() => {
        const el = document.getElementById('entity-view');
        if (!el) return { error: 'entity-view not found' };
        const text = el.textContent || '';
        const html = el.innerHTML || '';
        const undefs = (text.match(/\bundefined\b/g) || []).length;
        return { length: html.length, undefs, hasContent: html.length > 100 };
      });

      cityResult.sections['§5 Dossier'] = [];
      if (entityError) cityResult.sections['§5 Dossier'].push(`§5 JS crash: ${entityError}`);
      if (entity.error) cityResult.sections['§5 Dossier'].push(entity.error);
      else {
        if (!entity.hasContent) cityResult.sections['§5 Dossier'].push('§5.1 Entity view empty');
        if (entity.undefs > 0) cityResult.sections['§5 Dossier'].push(`§5.1 ${entity.undefs}x "undefined"`);
      }

      // ═══ §7.3 DATA COMPLETENESS ═══
      const data = await page.evaluate(() => {
        return {
          kbCount: Object.keys(KB).length,
          newsCount: NEWS.length,
          patternsCount: PATTERNS.length,
          hypothesesCount: HYPOTHESES.length,
          forecastKandidaten: (FORECAST.kandidaten || []).length,
          sentimentTopics: (SENTIMENT.topics || []).length,
          sentimentTopicsWithPosts: (SENTIMENT.topics || []).filter(t => (t.posts || []).length > 0).length,
          socialInsights: (SOCIAL.insights || []).length,
          socialInsightsWithSoWhat: (SOCIAL.insights || []).filter(i => i.soWhat).length,
          talkingPoints: (typeof TALKINGPOINTS !== 'undefined' ? TALKINGPOINTS : []).length,
          scenarios: (typeof SCENARIOS !== 'undefined' ? SCENARIOS : []).length,
          graphNodes: (GRAPH.nodes || []).length,
          graphLinks: (GRAPH.links || []).length,
          weeklyBriefPriorities: (typeof WEEKLYBRIEF !== 'undefined' && WEEKLYBRIEF.priorities ? WEEKLYBRIEF.priorities.length : 0),
          weeklyBriefSummary: (typeof WEEKLYBRIEF !== 'undefined' && WEEKLYBRIEF.summary ? WEEKLYBRIEF.summary.length : 0),
          themenRadar: (typeof THEMEN !== 'undefined' && THEMEN.radar ? THEMEN.radar.length : 0),
        };
      });

      cityResult.sections['§7.3 Data'] = [];
      const d = cityResult.sections['§7.3 Data'];
      if (data.kbCount < 3) d.push(`KB entities: ${data.kbCount} (need ≥3)`);
      if (data.newsCount < 5) d.push(`News: ${data.newsCount} (need ≥5)`);
      if (data.patternsCount < 2) d.push(`Patterns: ${data.patternsCount} (need ≥2)`);
      if (data.hypothesesCount < 1) d.push(`Hypotheses: ${data.hypothesesCount} (need ≥1)`);
      if (data.forecastKandidaten < 2) d.push(`Forecast kandidaten: ${data.forecastKandidaten} (need ≥2)`);
      if (data.sentimentTopics < 3) d.push(`Sentiment topics: ${data.sentimentTopics} (need ≥3)`);
      if (data.sentimentTopicsWithPosts < data.sentimentTopics) d.push(`Sentiment topics missing posts: ${data.sentimentTopics - data.sentimentTopicsWithPosts}/${data.sentimentTopics}`);
      if (data.socialInsights < 1) d.push(`Social insights: ${data.socialInsights} (need ≥1)`);
      if (data.socialInsightsWithSoWhat < data.socialInsights) d.push(`Social insights missing soWhat: ${data.socialInsights - data.socialInsightsWithSoWhat}/${data.socialInsights}`);
      if (data.talkingPoints < 3) d.push(`Talking points: ${data.talkingPoints} (need ≥3)`);
      if (data.scenarios < 2) d.push(`Scenarios: ${data.scenarios} (need ≥2)`);
      if (data.graphNodes < 8) d.push(`Graph nodes: ${data.graphNodes} (need ≥8)`);
      if (data.weeklyBriefPriorities < 2) d.push(`Weekly brief priorities: ${data.weeklyBriefPriorities} (need ≥2)`);
      if (data.weeklyBriefSummary < 50) d.push(`Weekly brief summary too short: ${data.weeklyBriefSummary} chars`);
      if (data.themenRadar < 3) d.push(`Themen radar: ${data.themenRadar} (need ≥3)`);

    } catch (e) {
      cityResult.sections['FATAL'] = [e.message.substring(0, 200)];
    }

    // ─── Collect JS errors ───
    cityResult.jsErrors = jsErrors;
    if (jsErrors.length > 0) {
      cityResult.sections['§7.1 Global'] = cityResult.sections['§7.1 Global'] || [];
      cityResult.sections['§7.1 Global'].push(`${jsErrors.length} JS error(s)`);
    }

    // ─── Determine pass/fail ───
    let totalIssues = 0;
    for (const [section, issues] of Object.entries(cityResult.sections)) {
      totalIssues += issues.length;
    }
    cityResult.totalIssues = totalIssues;
    cityResult.pass = totalIssues === 0;

    allResults.push(cityResult);
    await page.close();
  }

  await browser.close();

  // ═══ REPORT ═══
  console.log('\n' + '═'.repeat(80));
  console.log('  PRODUCT SPEC TEST — §7 Full Validation');
  console.log('═'.repeat(80) + '\n');

  let totalPassed = 0;
  let totalIssues = 0;
  const issuesBySection = {};

  for (const r of allResults) {
    const icon = r.pass ? '✅' : '❌';
    console.log(`${icon} ${r.city.toUpperCase().padEnd(12)} | ${r.totalIssues} issues`);

    for (const [section, issues] of Object.entries(r.sections)) {
      for (const issue of issues) {
        console.log(`   ${section.padEnd(16)} | ${issue}`);
        const sKey = section.split(' ')[0]; // §1, §2, etc.
        issuesBySection[sKey] = (issuesBySection[sKey] || 0) + 1;
      }
    }

    if (r.jsErrors.length > 0) {
      for (const e of r.jsErrors) console.log(`   💥 JS ERROR   | ${e.substring(0, 100)}`);
    }

    if (r.pass) totalPassed++;
    totalIssues += r.totalIssues;
    console.log('');
  }

  // ─── SUMMARY ───
  console.log('═'.repeat(80));
  console.log(`  RESULT: ${totalPassed}/${allResults.length} cities pass | ${totalIssues} total issues`);
  console.log('');
  console.log('  Issues by section:');
  for (const [section, count] of Object.entries(issuesBySection).sort((a,b) => b[1] - a[1])) {
    console.log(`    ${section.padEnd(8)} ${count} issue(s)`);
  }
  console.log('');
  if (totalPassed === allResults.length) {
    console.log('  ✅ ALL PASS — safe to deploy');
  } else {
    console.log('  ❌ FAILED — fix issues before deploy');
  }
  console.log('═'.repeat(80));

  return totalPassed === allResults.length;
}

server.listen(PORT, async () => {
  try {
    const pass = await runTests();
    server.close();
    process.exit(pass ? 0 : 1);
  } catch(e) {
    console.error('FATAL:', e.message);
    server.close();
    process.exit(1);
  }
});
