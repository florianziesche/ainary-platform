/**
 * HTML Renderer for AI Advisory Board v2
 * Research-Backed Edition with Knowledge Structure, Synthesis, and Sources
 */

const fs = require('fs');
const path = require('path');

function renderConfidenceIndicator(level) {
  // level: 1-5
  const filled = '●';
  const empty = '○';
  return filled.repeat(level) + empty.repeat(5 - level);
}

function renderHTML(question, advisors, responses, confidenceLevels, researchData, knowledgeStructure, synthesis, mode) {
  const timestamp = new Date().toLocaleDateString('en-US', { 
    year: 'numeric', 
    month: 'long', 
    day: 'numeric',
    hour: '2-digit',
    minute: '2-digit'
  });

  const isResearchMode = mode === 'research' && knowledgeStructure;

  // Render Research Context section
  const researchContextSection = isResearchMode ? `
    <details class="research-context" open>
      <summary>
        <div class="summary-header">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <circle cx="11" cy="11" r="8"/>
            <path d="M21 21l-4.35-4.35"/>
          </svg>
          <h3>Research Context</h3>
          <span class="toggle-indicator">▼</span>
        </div>
      </summary>
      <div class="research-content">
        <div class="research-meta">
          <div class="meta-item">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <rect x="3" y="4" width="18" height="18" rx="2" ry="2"/>
              <line x1="16" y1="2" x2="16" y2="6"/>
              <line x1="8" y1="2" x2="8" y2="6"/>
              <line x1="3" y1="10" x2="21" y2="10"/>
            </svg>
            <span>Last ${researchData?.keywords?.length || 2} days</span>
          </div>
          <div class="meta-item">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/>
              <circle cx="12" cy="7" r="4"/>
            </svg>
            <span>${researchData?.totalItems || 0} sources analyzed</span>
          </div>
          <div class="meta-item">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <polyline points="22 12 18 12 15 21 9 3 6 12 2 12"/>
            </svg>
            <span>Confidence: ${knowledgeStructure?.confidence || 'medium'}</span>
          </div>
        </div>

        ${renderKnowledgeStructure(knowledgeStructure)}
      </div>
    </details>
  ` : '';

  // Render Advisor cards
  const advisorCards = advisors.map((advisor, index) => `
    <div class="advisor-card">
      <div class="advisor-header">
        <div class="advisor-icon">${advisor.icon}</div>
        <div class="advisor-info">
          <h3>${advisor.name}</h3>
          <p class="advisor-role">${advisor.role}</p>
          ${isResearchMode ? `<div class="confidence">
            <span class="confidence-indicator">${renderConfidenceIndicator(confidenceLevels[index])}</span>
            <span class="confidence-label">Confidence</span>
          </div>` : ''}
        </div>
      </div>
      <div class="advisor-response">
        ${formatResponse(responses[index])}
      </div>
    </div>
  `).join('');

  // Render Synthesis section
  const synthesisSection = synthesis ? `
    <div class="synthesis-section">
      <div class="section-header">
        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
          <path d="M12 2L2 7l10 5 10-5-10-5z"/>
          <path d="M2 17l10 5 10-5"/>
          <path d="M2 12l10 5 10-5"/>
        </svg>
        <h2>Consensus & Action Items</h2>
      </div>

      <div class="synthesis-grid">
        <div class="synthesis-card consensus-card">
          <h3>
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/>
              <polyline points="22 4 12 14.01 9 11.01"/>
            </svg>
            Consensus
          </h3>
          <ul>
            ${synthesis.consensus.map(item => `<li>${item}</li>`).join('')}
          </ul>
        </div>

        <div class="synthesis-card dissent-card">
          <h3>
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <circle cx="12" cy="12" r="10"/>
              <line x1="15" y1="9" x2="9" y2="15"/>
              <line x1="9" y1="9" x2="15" y2="15"/>
            </svg>
            Key Debates
          </h3>
          <ul>
            ${synthesis.dissent.map(item => `<li>${item}</li>`).join('')}
          </ul>
        </div>
      </div>

      <div class="action-items">
        <h3>
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/>
            <polyline points="14 2 14 8 20 8"/>
            <line x1="9" y1="15" x2="15" y2="15"/>
          </svg>
          Top Action Items
        </h3>
        <ol class="action-list">
          ${synthesis.actionItems.map(item => `<li>${item}</li>`).join('')}
        </ol>
      </div>
    </div>
  ` : '';

  // Render Sources section
  const sourcesSection = researchData && researchData.totalItems > 0 ? `
    <div class="sources-section">
      <div class="section-header">
        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
          <path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/>
          <path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/>
        </svg>
        <h2>Research Sources</h2>
      </div>
      <div class="sources-grid">
        ${renderSources(researchData.sources)}
      </div>
    </div>
  ` : '';

  return `<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Advisory Board ${isResearchMode ? '• Research-Backed' : ''}: ${escapeHtml(question)}</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <style>
        ${getStyles(isResearchMode)}
    </style>
</head>
<body>
    <div class="container">
        <header>
            <div class="header-content">
                <h1>
                  <svg class="logo-icon" width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"/>
                    <polyline points="3.27 6.96 12 12.01 20.73 6.96"/>
                    <line x1="12" y1="22.08" x2="12" y2="12"/>
                  </svg>
                  AI Advisory Board
                </h1>
                ${isResearchMode ? '<span class="badge research-badge">Research-Backed</span>' : ''}
            </div>
            <p class="question">"${escapeHtml(question)}"</p>
            <p class="meta">Generated ${timestamp}${isResearchMode ? ' • Powered by GPT-4o + Multi-Source Research' : ''}</p>
        </header>

        <main>
            ${researchContextSection}

            <div class="advisors-section">
                <div class="section-header">
                    <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/>
                        <circle cx="9" cy="7" r="4"/>
                        <path d="M23 21v-2a4 4 0 0 0-3-3.87"/>
                        <path d="M16 3.13a4 4 0 0 1 0 7.75"/>
                    </svg>
                    <h2>Expert Perspectives</h2>
                </div>
                <div class="advisors-grid">
                    ${advisorCards}
                </div>
            </div>

            ${synthesisSection}

            ${sourcesSection}

            <div class="cta-banner">
                <h2>Want a Custom Deep-Dive?</h2>
                <p>Get a personalized strategic analysis with implementation roadmap, competitive analysis, and financial modeling.</p>
                <button class="btn btn-primary" onclick="openEmailGate()">Request Custom Analysis</button>
            </div>
        </main>

        <footer>
            <p>AI Advisory Board v2 • 6 Expert Perspectives, Research-Backed Insights</p>
            <p class="footer-links">
                <a href="#" onclick="window.print(); return false;">Print Report</a>
                <span>•</span>
                <a href="#" onclick="openEmailGate(); return false;">Get PDF</a>
            </p>
        </footer>
    </div>

    <!-- Email Gate Modal -->
    <div class="modal" id="email-modal">
        <div class="modal-overlay" onclick="closeEmailGate()"></div>
        <div class="modal-content">
            <button class="modal-close" onclick="closeEmailGate()">
                <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <line x1="18" y1="6" x2="6" y2="18"/>
                    <line x1="6" y1="6" x2="18" y2="18"/>
                </svg>
            </button>
            <h2>Get Your Custom Analysis</h2>
            <p class="modal-description">
                Receive a comprehensive strategic report including implementation frameworks, financial projections, and competitive landscape analysis.
            </p>
            <form class="email-form" onsubmit="submitEmail(event)">
                <input 
                    type="email" 
                    id="email-input" 
                    placeholder="your@email.com" 
                    required 
                />
                <button type="submit" class="btn btn-primary">
                    Get Custom Analysis
                </button>
            </form>
            <p class="modal-footer">
                No spam. Just high-value strategic insights delivered to your inbox.
            </p>
        </div>
    </div>

    <script>
        ${getScripts()}
    </script>
</body>
</html>`;
}

function renderKnowledgeStructure(knowledge) {
  if (!knowledge) return '';

  return `
    <div class="knowledge-grid">
      ${knowledge.keyFacts.length > 0 ? `
        <div class="knowledge-card">
          <h4>
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <circle cx="12" cy="12" r="10"/>
              <line x1="12" y1="16" x2="12" y2="12"/>
              <line x1="12" y1="8" x2="12.01" y2="8"/>
            </svg>
            Key Facts
          </h4>
          <ul>
            ${knowledge.keyFacts.map(fact => `<li>${fact}</li>`).join('')}
          </ul>
        </div>
      ` : ''}

      ${knowledge.recentDevelopments.length > 0 ? `
        <div class="knowledge-card">
          <h4>
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <polyline points="23 6 13.5 15.5 8.5 10.5 1 18"/>
              <polyline points="17 6 23 6 23 12"/>
            </svg>
            Recent Developments
          </h4>
          <ul>
            ${knowledge.recentDevelopments.map(dev => `<li>${dev}</li>`).join('')}
          </ul>
        </div>
      ` : ''}

      ${knowledge.openQuestions.length > 0 ? `
        <div class="knowledge-card">
          <h4>
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <circle cx="12" cy="12" r="10"/>
              <path d="M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3"/>
              <line x1="12" y1="17" x2="12.01" y2="17"/>
            </svg>
            Open Questions
          </h4>
          <ul>
            ${knowledge.openQuestions.map(q => `<li>${q}</li>`).join('')}
          </ul>
        </div>
      ` : ''}

      ${knowledge.counterArguments.length > 0 ? `
        <div class="knowledge-card">
          <h4>
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <path d="M10.29 3.86L1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z"/>
              <line x1="12" y1="9" x2="12" y2="13"/>
              <line x1="12" y1="17" x2="12.01" y2="17"/>
            </svg>
            Counter-Arguments
          </h4>
          <ul>
            ${knowledge.counterArguments.map(arg => `<li>${arg}</li>`).join('')}
          </ul>
        </div>
      ` : ''}
    </div>
  `;
}

function renderSources(sources) {
  let html = '';

  if (sources.arxiv?.length > 0) {
    html += `
      <div class="source-category">
        <h3>
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"/>
            <path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"/>
          </svg>
          ArXiv Papers
        </h3>
        <ul class="source-list">
          ${sources.arxiv.slice(0, 5).map(item => `
            <li>
              <a href="${item.url}" target="_blank" rel="noopener">
                ${escapeHtml(item.title)}
              </a>
              <p class="source-meta">${item.abstract || ''}</p>
            </li>
          `).join('')}
        </ul>
      </div>
    `;
  }

  if (sources.hackernews?.length > 0) {
    html += `
      <div class="source-category">
        <h3>
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <path d="M21 2l-2 2m-7.61 7.61a5.5 5.5 0 1 1-7.778 7.778 5.5 5.5 0 0 1 7.777-7.777zm0 0L15.5 7.5m0 0l3 3L22 7l-3-3m-3.5 3.5L19 4"/>
          </svg>
          Hacker News
        </h3>
        <ul class="source-list">
          ${sources.hackernews.slice(0, 5).map(item => `
            <li>
              <a href="${item.url}" target="_blank" rel="noopener">
                ${escapeHtml(item.title)}
              </a>
              <span class="score-badge">${item.score} points</span>
            </li>
          `).join('')}
        </ul>
      </div>
    `;
  }

  if (sources.reddit?.length > 0) {
    html += `
      <div class="source-category">
        <h3>
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z"/>
          </svg>
          Reddit Discussions
        </h3>
        <ul class="source-list">
          ${sources.reddit.slice(0, 5).map(item => `
            <li>
              <a href="${item.url}" target="_blank" rel="noopener">
                ${escapeHtml(item.title)}
              </a>
              <span class="score-badge">${item.score} upvotes</span>
            </li>
          `).join('')}
        </ul>
      </div>
    `;
  }

  if (sources.github?.length > 0) {
    html += `
      <div class="source-category">
        <h3>
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <path d="M9 19c-5 1.5-5-2.5-7-3m14 6v-3.87a3.37 3.37 0 0 0-.94-2.61c3.14-.35 6.44-1.54 6.44-7A5.44 5.44 0 0 0 20 4.77 5.07 5.07 0 0 0 19.91 1S18.73.65 16 2.48a13.38 13.38 0 0 0-7 0C6.27.65 5.09 1 5.09 1A5.07 5.07 0 0 0 5 4.77a5.44 5.44 0 0 0-1.5 3.78c0 5.42 3.3 6.61 6.44 7A3.37 3.37 0 0 0 9 18.13V22"/>
          </svg>
          GitHub Trending
        </h3>
        <ul class="source-list">
          ${sources.github.map(item => `
            <li>
              <a href="${item.url}" target="_blank" rel="noopener">
                ${escapeHtml(item.title)}
              </a>
              <p class="source-meta">${escapeHtml(item.description || '')}</p>
            </li>
          `).join('')}
        </ul>
      </div>
    `;
  }

  return html;
}

function formatResponse(text) {
  return text
    .split('\n\n')
    .map(para => `<p>${escapeHtml(para.trim())}</p>`)
    .join('');
}

function escapeHtml(text) {
  const map = {
    '&': '&amp;',
    '<': '&lt;',
    '>': '&gt;',
    '"': '&quot;',
    "'": '&#039;'
  };
  return text.replace(/[&<>"']/g, m => map[m]);
}

function getStyles(isResearchMode) {
  return `
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        :root {
            --gold: #c8aa50;
            --gold-light: #d4b960;
            --emerald: #10b981;
            --bg-dark: #0a0a0a;
            --bg-card: rgba(20, 20, 20, 0.8);
            --bg-glass: rgba(255, 255, 255, 0.05);
            --border-glass: rgba(255, 255, 255, 0.1);
            --text-primary: #ffffff;
            --text-secondary: #a0a0a0;
            --text-muted: #666666;
        }

        body {
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
            background: var(--bg-dark);
            color: var(--text-primary);
            line-height: 1.6;
            min-height: 100vh;
            padding: 2rem 1rem;
        }

        .container {
            max-width: 1200px;
            margin: 0 auto;
        }

        header {
            text-align: center;
            margin-bottom: 3rem;
            padding-bottom: 2rem;
            border-bottom: 1px solid var(--border-glass);
        }

        .header-content {
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 1rem;
            margin-bottom: 1rem;
        }

        .logo-icon {
            color: var(--gold);
        }

        h1 {
            font-size: 2.5rem;
            font-weight: 700;
            background: linear-gradient(135deg, var(--gold) 0%, var(--gold-light) 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            display: flex;
            align-items: center;
            gap: 0.75rem;
        }

        .badge {
            display: inline-block;
            padding: 0.375rem 0.75rem;
            border-radius: 6px;
            font-size: 0.875rem;
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 0.05em;
        }

        .research-badge {
            background: linear-gradient(135deg, var(--emerald) 0%, #059669 100%);
            color: white;
        }

        .question {
            font-size: 1.5rem;
            font-weight: 500;
            margin-bottom: 0.5rem;
            color: var(--text-primary);
        }

        .meta {
            font-size: 0.9rem;
            color: var(--text-muted);
        }

        .section-header {
            display: flex;
            align-items: center;
            gap: 0.75rem;
            margin-bottom: 1.5rem;
        }

        .section-header svg {
            color: var(--gold);
        }

        .section-header h2 {
            font-size: 1.75rem;
            font-weight: 600;
        }

        /* Research Context */
        .research-context {
            background: var(--bg-glass);
            backdrop-filter: blur(10px);
            border: 1px solid var(--border-glass);
            border-radius: 16px;
            padding: 1.5rem;
            margin-bottom: 3rem;
        }

        .research-context summary {
            cursor: pointer;
            list-style: none;
            user-select: none;
        }

        .research-context summary::-webkit-details-marker {
            display: none;
        }

        .summary-header {
            display: flex;
            align-items: center;
            gap: 0.75rem;
        }

        .summary-header svg {
            color: var(--emerald);
        }

        .summary-header h3 {
            font-size: 1.25rem;
            font-weight: 600;
            flex: 1;
        }

        .toggle-indicator {
            color: var(--text-muted);
            transition: transform 0.3s ease;
        }

        .research-context[open] .toggle-indicator {
            transform: rotate(180deg);
        }

        .research-content {
            margin-top: 1.5rem;
            padding-top: 1.5rem;
            border-top: 1px solid var(--border-glass);
        }

        .research-meta {
            display: flex;
            gap: 2rem;
            margin-bottom: 1.5rem;
            flex-wrap: wrap;
        }

        .meta-item {
            display: flex;
            align-items: center;
            gap: 0.5rem;
            color: var(--text-secondary);
            font-size: 0.9rem;
        }

        .meta-item svg {
            color: var(--emerald);
        }

        .knowledge-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 1rem;
        }

        .knowledge-card {
            background: rgba(16, 185, 129, 0.05);
            border: 1px solid rgba(16, 185, 129, 0.2);
            border-radius: 12px;
            padding: 1.25rem;
        }

        .knowledge-card h4 {
            display: flex;
            align-items: center;
            gap: 0.5rem;
            font-size: 1rem;
            font-weight: 600;
            margin-bottom: 0.75rem;
            color: var(--emerald);
        }

        .knowledge-card h4 svg {
            flex-shrink: 0;
        }

        .knowledge-card ul {
            list-style: none;
        }

        .knowledge-card li {
            font-size: 0.9rem;
            color: var(--text-secondary);
            margin-bottom: 0.5rem;
            padding-left: 1.25rem;
            position: relative;
        }

        .knowledge-card li:before {
            content: "•";
            position: absolute;
            left: 0;
            color: var(--emerald);
        }

        /* Advisors */
        .advisors-section {
            margin-bottom: 3rem;
        }

        .advisors-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(500px, 1fr));
            gap: 2rem;
        }

        .advisor-card {
            background: var(--bg-glass);
            backdrop-filter: blur(10px);
            border: 1px solid var(--border-glass);
            border-radius: 16px;
            padding: 2rem;
            transition: all 0.3s ease;
        }

        .advisor-card:hover {
            border-color: var(--gold);
            box-shadow: 0 8px 32px rgba(200, 170, 80, 0.1);
            transform: translateY(-2px);
        }

        .advisor-header {
            display: flex;
            align-items: flex-start;
            gap: 1rem;
            margin-bottom: 1.5rem;
            padding-bottom: 1rem;
            border-bottom: 1px solid var(--border-glass);
        }

        .advisor-icon {
            width: 48px;
            height: 48px;
            display: flex;
            align-items: center;
            justify-content: center;
            background: rgba(200, 170, 80, 0.1);
            border-radius: 12px;
            color: var(--gold);
            flex-shrink: 0;
        }

        .advisor-info {
            flex: 1;
        }

        .advisor-info h3 {
            font-size: 1.25rem;
            font-weight: 600;
            margin-bottom: 0.25rem;
        }

        .advisor-role {
            font-size: 0.9rem;
            color: var(--text-secondary);
            margin-bottom: 0.5rem;
        }

        .confidence {
            display: flex;
            align-items: center;
            gap: 0.5rem;
            margin-top: 0.5rem;
        }

        .confidence-indicator {
            font-size: 0.9rem;
            letter-spacing: 0.1em;
            color: var(--gold);
        }

        .confidence-label {
            font-size: 0.75rem;
            color: var(--text-muted);
            text-transform: uppercase;
            letter-spacing: 0.05em;
        }

        .advisor-response {
            font-size: 1rem;
            color: var(--text-secondary);
            line-height: 1.8;
        }

        .advisor-response p {
            margin-bottom: 1rem;
        }

        .advisor-response p:last-child {
            margin-bottom: 0;
        }

        /* Synthesis */
        .synthesis-section {
            background: var(--bg-glass);
            backdrop-filter: blur(10px);
            border: 1px solid var(--border-glass);
            border-radius: 16px;
            padding: 2rem;
            margin-bottom: 3rem;
        }

        .synthesis-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 1.5rem;
            margin-bottom: 2rem;
        }

        .synthesis-card {
            background: rgba(255, 255, 255, 0.02);
            border: 1px solid var(--border-glass);
            border-radius: 12px;
            padding: 1.5rem;
        }

        .synthesis-card h3 {
            display: flex;
            align-items: center;
            gap: 0.5rem;
            font-size: 1.125rem;
            font-weight: 600;
            margin-bottom: 1rem;
        }

        .consensus-card h3 {
            color: var(--emerald);
        }

        .consensus-card h3 svg {
            color: var(--emerald);
        }

        .dissent-card h3 {
            color: #f59e0b;
        }

        .dissent-card h3 svg {
            color: #f59e0b;
        }

        .synthesis-card ul {
            list-style: none;
        }

        .synthesis-card li {
            font-size: 0.95rem;
            color: var(--text-secondary);
            margin-bottom: 0.75rem;
            padding-left: 1.25rem;
            position: relative;
            line-height: 1.6;
        }

        .consensus-card li:before {
            content: "✓";
            position: absolute;
            left: 0;
            color: var(--emerald);
            font-weight: 600;
        }

        .dissent-card li:before {
            content: "⚠";
            position: absolute;
            left: 0;
        }

        .action-items {
            background: rgba(200, 170, 80, 0.05);
            border: 1px solid rgba(200, 170, 80, 0.2);
            border-radius: 12px;
            padding: 1.5rem;
        }

        .action-items h3 {
            display: flex;
            align-items: center;
            gap: 0.5rem;
            font-size: 1.125rem;
            font-weight: 600;
            margin-bottom: 1rem;
            color: var(--gold);
        }

        .action-items h3 svg {
            color: var(--gold);
        }

        .action-list {
            list-style: none;
            counter-reset: action-counter;
        }

        .action-list li {
            font-size: 0.95rem;
            color: var(--text-secondary);
            margin-bottom: 0.75rem;
            padding-left: 2rem;
            position: relative;
            line-height: 1.6;
            counter-increment: action-counter;
        }

        .action-list li:before {
            content: counter(action-counter);
            position: absolute;
            left: 0;
            width: 1.5rem;
            height: 1.5rem;
            background: var(--gold);
            color: var(--bg-dark);
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 0.8rem;
            font-weight: 700;
        }

        /* Sources */
        .sources-section {
            margin-bottom: 3rem;
        }

        .sources-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 2rem;
        }

        .source-category {
            background: var(--bg-glass);
            backdrop-filter: blur(10px);
            border: 1px solid var(--border-glass);
            border-radius: 12px;
            padding: 1.5rem;
        }

        .source-category h3 {
            display: flex;
            align-items: center;
            gap: 0.5rem;
            font-size: 1rem;
            font-weight: 600;
            margin-bottom: 1rem;
            color: var(--gold);
        }

        .source-category h3 svg {
            color: var(--gold);
        }

        .source-list {
            list-style: none;
        }

        .source-list li {
            margin-bottom: 1rem;
            padding-bottom: 1rem;
            border-bottom: 1px solid var(--border-glass);
        }

        .source-list li:last-child {
            margin-bottom: 0;
            padding-bottom: 0;
            border-bottom: none;
        }

        .source-list a {
            color: var(--text-primary);
            text-decoration: none;
            font-weight: 500;
            transition: color 0.2s ease;
            display: block;
            margin-bottom: 0.25rem;
        }

        .source-list a:hover {
            color: var(--gold);
        }

        .source-meta {
            font-size: 0.85rem;
            color: var(--text-muted);
            margin-top: 0.25rem;
        }

        .score-badge {
            display: inline-block;
            padding: 0.25rem 0.5rem;
            background: rgba(200, 170, 80, 0.1);
            border: 1px solid rgba(200, 170, 80, 0.3);
            border-radius: 4px;
            font-size: 0.75rem;
            color: var(--gold);
            margin-top: 0.25rem;
        }

        /* CTA Banner */
        .cta-banner {
            background: linear-gradient(135deg, rgba(200, 170, 80, 0.1) 0%, rgba(200, 170, 80, 0.05) 100%);
            border: 1px solid var(--gold);
            border-radius: 16px;
            padding: 2rem;
            text-align: center;
            margin-bottom: 3rem;
        }

        .cta-banner h2 {
            font-size: 1.5rem;
            font-weight: 600;
            margin-bottom: 0.75rem;
            color: var(--gold);
        }

        .cta-banner p {
            color: var(--text-secondary);
            margin-bottom: 1.5rem;
            max-width: 600px;
            margin-left: auto;
            margin-right: auto;
        }

        .btn {
            display: inline-block;
            padding: 0.75rem 2rem;
            font-weight: 600;
            text-decoration: none;
            border-radius: 8px;
            border: none;
            cursor: pointer;
            transition: all 0.3s ease;
            font-size: 1rem;
            font-family: 'Inter', sans-serif;
        }

        .btn-primary {
            background: var(--gold);
            color: var(--bg-dark);
        }

        .btn-primary:hover {
            background: var(--gold-light);
            transform: scale(1.05);
        }

        /* Modal */
        .modal {
            display: none;
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            z-index: 1000;
            align-items: center;
            justify-content: center;
        }

        .modal.active {
            display: flex;
        }

        .modal-overlay {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(0, 0, 0, 0.8);
            backdrop-filter: blur(5px);
        }

        .modal-content {
            position: relative;
            background: var(--bg-card);
            border: 1px solid var(--border-glass);
            border-radius: 16px;
            padding: 2rem;
            max-width: 500px;
            width: 90%;
            z-index: 1001;
        }

        .modal-close {
            position: absolute;
            top: 1rem;
            right: 1rem;
            background: none;
            border: none;
            color: var(--text-muted);
            cursor: pointer;
            padding: 0.5rem;
            border-radius: 8px;
            transition: all 0.2s ease;
        }

        .modal-close:hover {
            background: var(--bg-glass);
            color: var(--text-primary);
        }

        .modal-content h2 {
            font-size: 1.75rem;
            margin-bottom: 1rem;
            color: var(--gold);
        }

        .modal-description {
            color: var(--text-secondary);
            margin-bottom: 1.5rem;
            line-height: 1.6;
        }

        .email-form {
            display: flex;
            flex-direction: column;
            gap: 1rem;
        }

        .email-form input {
            width: 100%;
            padding: 0.75rem;
            background: var(--bg-glass);
            border: 1px solid var(--border-glass);
            border-radius: 8px;
            color: var(--text-primary);
            font-family: 'Inter', sans-serif;
            font-size: 1rem;
        }

        .email-form input:focus {
            outline: none;
            border-color: var(--gold);
        }

        .modal-footer {
            font-size: 0.85rem;
            color: var(--text-muted);
            text-align: center;
            margin-top: 1rem;
        }

        /* Footer */
        footer {
            text-align: center;
            padding-top: 2rem;
            border-top: 1px solid var(--border-glass);
            color: var(--text-muted);
            font-size: 0.9rem;
        }

        footer p {
            margin-bottom: 0.5rem;
        }

        .footer-links {
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 1rem;
        }

        .footer-links a {
            color: var(--text-secondary);
            text-decoration: none;
            transition: color 0.2s ease;
        }

        .footer-links a:hover {
            color: var(--gold);
        }

        /* Print Styles */
        @media print {
            body {
                background: white;
                color: black;
            }

            .cta-banner, footer, .modal {
                display: none;
            }

            .advisor-card, .synthesis-section, .sources-section {
                break-inside: avoid;
                border: 1px solid #ddd;
                background: white;
            }

            .advisor-icon, .section-header svg {
                color: #c8aa50 !important;
            }

            h1 {
                color: #c8aa50;
                -webkit-text-fill-color: #c8aa50;
            }
        }

        @media (max-width: 768px) {
            .advisors-grid {
                grid-template-columns: 1fr;
            }

            .synthesis-grid {
                grid-template-columns: 1fr;
            }

            .sources-grid {
                grid-template-columns: 1fr;
            }

            h1 {
                font-size: 2rem;
            }

            .question {
                font-size: 1.25rem;
            }

            .header-content {
                flex-direction: column;
            }
        }
  `;
}

function getScripts() {
  return `
        function openEmailGate() {
            document.getElementById('email-modal').classList.add('active');
        }

        function closeEmailGate() {
            document.getElementById('email-modal').classList.remove('active');
        }

        function submitEmail(event) {
            event.preventDefault();
            const email = document.getElementById('email-input').value;
            
            if (email && email.includes('@')) {
                alert('Thank you! Your custom analysis will be sent to ' + email + '\\n\\nThis is a demo. In production, this would trigger an email workflow.');
                console.log('Email submitted:', email);
                closeEmailGate();
            } else {
                alert('Please enter a valid email address');
            }
            
            return false;
        }
  `;
}

module.exports = { renderHTML };
