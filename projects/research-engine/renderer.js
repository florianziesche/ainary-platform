// Renderer — JSON to HTML
import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));

export function render(analysis, rawData, reportDate) {
  const template = fs.readFileSync(path.join(__dirname, 'template.html'), 'utf-8');

  // Render Emerging Signals
  const signalsHTML = analysis.emerging_signals.map(signal => `
    <div class="signal-card">
      <div class="signal-header">
        <h3>${escapeHTML(signal.title)}</h3>
        <div class="signal-strength">
          <span class="strength-label">Signal Strength:</span>
          <div class="strength-bar">
            ${Array.from({length: 5}, (_, i) => `<div class="bar ${i < signal.signal_strength ? 'active' : ''}"></div>`).join('')}
          </div>
        </div>
      </div>
      <p class="signal-why">${escapeHTML(signal.why_it_matters)}</p>
      <div class="signal-sources">
        ${signal.sources.map(s => `<span class="source-tag">${s}</span>`).join('')}
      </div>
    </div>
  `).join('');

  // Render Deep Dives
  const deepDivesHTML = analysis.deep_dives.map(dive => `
    <div class="dive-card">
      <h3>${escapeHTML(dive.title)}</h3>
      <p class="dive-summary">${escapeHTML(dive.summary)}</p>
      <div class="dive-investigate">
        <strong>Why investigate:</strong> ${escapeHTML(dive.why_investigate)}
      </div>
      <div class="signal-sources">
        ${dive.sources.map(s => `<span class="source-tag">${s}</span>`).join('')}
      </div>
    </div>
  `).join('');

  // Render Contrarian Corner
  const contrarianHTML = analysis.contrarian_corner.map(item => `
    <div class="contrarian-card">
      <h4>${escapeHTML(item.idea)}</h4>
      <div class="contrarian-row">
        <div class="contrarian-col">
          <strong>Why it's ignored:</strong>
          <p>${escapeHTML(item.why_ignored)}</p>
        </div>
        <div class="contrarian-col">
          <strong>Why it might matter:</strong>
          <p>${escapeHTML(item.why_might_matter)}</p>
        </div>
      </div>
    </div>
  `).join('');

  // Render Cross-Source Patterns
  const patternsHTML = analysis.cross_source_patterns.map(pattern => `
    <div class="pattern-card">
      <h4>${escapeHTML(pattern.pattern)}</h4>
      <p>${escapeHTML(pattern.significance)}</p>
      <div class="signal-sources">
        ${pattern.sources.map(s => `<span class="source-tag">${s}</span>`).join('')}
      </div>
    </div>
  `).join('');

  // SVG Icons for sources
  const icons = {
    arxiv: `<svg viewBox="0 0 24 24" fill="none" stroke="#10b981" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="width: 32px; height: 32px;"><path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"/><path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"/></svg>`,
    hackernews: `<svg viewBox="0 0 24 24" fill="none" stroke="#10b981" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="width: 32px; height: 32px;"><path d="M8.84 3l4.16 7.5L17.16 3"/><line x1="13" y1="10.5" x2="13" y2="21"/></svg>`,
    reddit: `<svg viewBox="0 0 24 24" fill="none" stroke="#10b981" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="width: 32px; height: 32px;"><path d="M12 2L2 7l10 5 10-5-10-5z"/><path d="M2 17l10 5 10-5"/><path d="M2 12l10 5 10-5"/></svg>`,
    github: `<svg viewBox="0 0 24 24" fill="none" stroke="#10b981" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="width: 32px; height: 32px;"><polyline points="16 18 22 12 16 6"/><polyline points="8 6 2 12 8 18"/></svg>`,
    rss: `<svg viewBox="0 0 24 24" fill="none" stroke="#10b981" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="width: 32px; height: 32px;"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="16" y1="13" x2="8" y2="13"/><line x1="16" y1="17" x2="8" y2="17"/><polyline points="10 9 9 9 8 9"/></svg>`
  };

  // Icons for source sections
  const sectionIcons = {
    arxiv: `<svg viewBox="0 0 24 24" fill="none" stroke="#10b981" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="width: 24px; height: 24px; display: inline-block; vertical-align: middle; margin-right: 0.5rem;"><path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"/><path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"/></svg>`,
    hackernews: `<svg viewBox="0 0 24 24" fill="none" stroke="#10b981" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="width: 24px; height: 24px; display: inline-block; vertical-align: middle; margin-right: 0.5rem;"><path d="M8.84 3l4.16 7.5L17.16 3"/><line x1="13" y1="10.5" x2="13" y2="21"/></svg>`,
    reddit: `<svg viewBox="0 0 24 24" fill="none" stroke="#10b981" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="width: 24px; height: 24px; display: inline-block; vertical-align: middle; margin-right: 0.5rem;"><path d="M12 2L2 7l10 5 10-5-10-5z"/><path d="M2 17l10 5 10-5"/><path d="M2 12l10 5 10-5"/></svg>`,
    github: `<svg viewBox="0 0 24 24" fill="none" stroke="#10b981" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="width: 24px; height: 24px; display: inline-block; vertical-align: middle; margin-right: 0.5rem;"><polyline points="16 18 22 12 16 6"/><polyline points="8 6 2 12 8 18"/></svg>`,
    rss: `<svg viewBox="0 0 24 24" fill="none" stroke="#10b981" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="width: 24px; height: 24px; display: inline-block; vertical-align: middle; margin-right: 0.5rem;"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="16" y1="13" x2="8" y2="13"/><line x1="16" y1="17" x2="8" y2="17"/><polyline points="10 9 9 9 8 9"/></svg>`
  };

  // Render raw data counts
  const { arxiv, hackernews, reddit, github, rss } = rawData;
  const sourceStats = `
    <div class="source-stats">
      <div class="stat">
        <span class="stat-icon">${icons.arxiv}</span>
        <span class="stat-label">ArXiv Papers</span>
        <span class="stat-value">${arxiv.length}</span>
      </div>
      <div class="stat">
        <span class="stat-icon">${icons.hackernews}</span>
        <span class="stat-label">Hacker News</span>
        <span class="stat-value">${hackernews.length}</span>
      </div>
      <div class="stat">
        <span class="stat-icon">${icons.reddit}</span>
        <span class="stat-label">Reddit Posts</span>
        <span class="stat-value">${reddit.length}</span>
      </div>
      <div class="stat">
        <span class="stat-icon">${icons.github}</span>
        <span class="stat-label">GitHub Repos</span>
        <span class="stat-value">${github.length}</span>
      </div>
      <div class="stat">
        <span class="stat-icon">${icons.rss}</span>
        <span class="stat-label">VC Blog Posts</span>
        <span class="stat-value">${rss.length}</span>
      </div>
    </div>
  `;

  // Render Source Insights
  const sourceInsights = rawData.source_insights || {};
  const sourceInsightsHTML = `
    ${sourceInsights.arxiv ? `
      <div class="section">
        <div class="section-header">
          ${sectionIcons.arxiv}
          <h2>ArXiv Research Insights</h2>
        </div>
        <div class="source-insight">
          <strong>AI Analysis</strong>
          <p>${escapeHTML(sourceInsights.arxiv)}</p>
        </div>
      </div>
    ` : ''}
    ${sourceInsights.hackernews ? `
      <div class="section">
        <div class="section-header">
          ${sectionIcons.hackernews}
          <h2>Hacker News Insights</h2>
        </div>
        <div class="source-insight">
          <strong>AI Analysis</strong>
          <p>${escapeHTML(sourceInsights.hackernews)}</p>
        </div>
      </div>
    ` : ''}
    ${sourceInsights.reddit ? `
      <div class="section">
        <div class="section-header">
          ${sectionIcons.reddit}
          <h2>Reddit Discussion Insights</h2>
        </div>
        <div class="source-insight">
          <strong>AI Analysis</strong>
          <p>${escapeHTML(sourceInsights.reddit)}</p>
        </div>
      </div>
    ` : ''}
    ${sourceInsights.github ? `
      <div class="section">
        <div class="section-header">
          ${sectionIcons.github}
          <h2>GitHub Repository Insights</h2>
        </div>
        <div class="source-insight">
          <strong>AI Analysis</strong>
          <p>${escapeHTML(sourceInsights.github)}</p>
        </div>
      </div>
    ` : ''}
    ${sourceInsights.rss ? `
      <div class="section">
        <div class="section-header">
          ${sectionIcons.rss}
          <h2>VC Blog Insights</h2>
        </div>
        <div class="source-insight">
          <strong>AI Analysis</strong>
          <p>${escapeHTML(sourceInsights.rss)}</p>
        </div>
      </div>
    ` : ''}
  `;

  // Replace placeholders
  let html = template
    .replace('{{REPORT_DATE}}', reportDate)
    .replace('{{EMERGING_SIGNALS}}', signalsHTML)
    .replace('{{DEEP_DIVES}}', deepDivesHTML)
    .replace('{{CONTRARIAN_CORNER}}', contrarianHTML)
    .replace('{{CROSS_SOURCE_PATTERNS}}', patternsHTML)
    .replace('{{SOURCE_STATS}}', sourceStats)
    .replace('{{SOURCE_INSIGHTS}}', sourceInsightsHTML)
    .replace('{{TOTAL_ITEMS}}', analysis.meta.total_items_analyzed)
    .replace('{{TIMEFRAME}}', analysis.meta.timeframe)
    .replace('{{CONFIDENCE}}', analysis.meta.confidence.toUpperCase());

  return html;
}

function escapeHTML(str) {
  if (!str) return '';
  return str
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&#039;');
}
