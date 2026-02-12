import { readFileSync, writeFileSync, mkdirSync } from 'fs';
import { log, slugify } from './utils.js';
import { fileURLToPath } from 'url';
import { dirname, join } from 'path';

const __dirname = dirname(fileURLToPath(import.meta.url));

/**
 * Calculate radar chart polygon points
 * FIXED: Changed from cx=150, cy=150, r=120 to cx=100, cy=100, r=75
 * to fit within 200x200 viewBox
 */
function calcRadarPoints(scores, cx = 100, cy = 100, r = 75) {
  const dims = ['innovation', 'data_maturity', 'ai_adoption', 'talent', 'investment'];
  const points = dims.map((dim, i) => {
    const angle = (Math.PI * 2 * i / 5) - Math.PI / 2;
    const val = (scores[dim] || 50) / 100;
    const x = cx + r * val * Math.cos(angle);
    const y = cy + r * val * Math.sin(angle);
    return `${x.toFixed(1)},${y.toFixed(1)}`;
  });
  return points.join(' ');
}

/**
 * Render department table rows
 * FIXED: difficulty is now lowercase to match CSS classes
 */
function renderDeptRows(departments) {
  return departments.map((d, i) => {
    // Map difficulty to lowercase for CSS classes
    const difficultyLower = (d.difficulty || '').toLowerCase();
    
    return `
    <tr style="background: ${i % 2 === 0 ? 'rgba(255,255,255,0.02)' : 'transparent'}">
      <td style="padding: 12px 16px; font-weight: 600;">${d.department}</td>
      <td style="padding: 12px 16px; color: #9ca3af;">${d.current_state}</td>
      <td style="padding: 12px 16px; color: #a78bfa;">${d.ai_opportunity}</td>
      <td style="padding: 12px 16px; color: #10b981; font-weight: 600;">${d.estimated_impact}</td>
      <td style="padding: 12px 16px;"><span style="padding: 2px 10px; border-radius: 12px; font-size: 0.8rem; background: ${difficultyLower === 'easy' ? 'rgba(16,185,129,0.15); color: #10b981' : difficultyLower === 'hard' ? 'rgba(239,68,68,0.15); color: #ef4444' : 'rgba(251,191,36,0.15); color: #fbbf24'};">${d.difficulty}</span></td>
    </tr>`;
  }).join('\n');
}

/**
 * Render risk matrix items (circles)
 * FIXED: Clamp likelihood and impact from 1-5 to 1-3, and adjusted positioning
 * to fit within 200x200 viewBox with proper spacing
 */
function renderRiskItems(risks) {
  return risks.map(r => {
    // Clamp values to 1-3 range
    const clampedLikelihood = Math.min(3, Math.max(1, r.likelihood || 1));
    const clampedImpact = Math.min(3, Math.max(1, r.impact || 1));
    
    // Calculate position within 200x200 viewBox
    // x: 40 to 160 (3 columns with spacing)
    // y: 160 to 40 (inverted, 3 rows with spacing)
    const x = 40 + (clampedLikelihood - 1) * 60;
    const y = 160 - (clampedImpact - 1) * 60;
    
    // Color based on total risk score
    const totalRisk = clampedLikelihood + clampedImpact;
    const color = (totalRisk >= 5) ? '#ef4444' : (totalRisk >= 4) ? '#fbbf24' : '#10b981';
    
    return `<circle cx="${x}" cy="${y}" r="14" fill="${color}" opacity="0.8"/>
            <text x="${x}" y="${y + 4}" text-anchor="middle" fill="white" font-size="8" font-weight="600">${(r.name || '').substring(0, 6)}</text>`;
  }).join('\n');
}

/**
 * Render risk details list
 */
function renderRiskDetails(risks) {
  return risks.map(r => {
    const clampedLikelihood = Math.min(3, Math.max(1, r.likelihood || 1));
    const clampedImpact = Math.min(3, Math.max(1, r.impact || 1));
    
    return `
    <div style="margin-bottom: 8px; padding: 8px 12px; background: rgba(255,255,255,0.03); border-radius: 8px;">
      <strong>${r.name}</strong> <span style="color: #9ca3af;">— Likelihood: ${clampedLikelihood}/3, Impact: ${clampedImpact}/3</span>
      <div style="color: #9ca3af; font-size: 0.85rem; margin-top: 4px;">Mitigation: ${r.mitigation}</div>
    </div>`;
  }).join('\n');
}

/**
 * Render provocateur section
 */
function renderProvocateur(prov) {
  let html = '';
  
  if (prov.blind_spots?.length) {
    html += '<h4 style="color: #f97316; margin-bottom: 8px;">△ Blind Spots</h4><ul>';
    prov.blind_spots.forEach(b => html += `<li style="margin-bottom: 6px;">${b}</li>`);
    html += '</ul>';
  }
  
  if (prov.uncomfortable_truths?.length) {
    html += '<h4 style="color: #ef4444; margin: 16px 0 8px;">△ Uncomfortable Truths</h4><ul>';
    prov.uncomfortable_truths.forEach(t => html += `<li style="margin-bottom: 6px;">${t}</li>`);
    html += '</ul>';
  }
  
  if (prov.what_mckinsey_wont_say) {
    html += `<h4 style="color: #ef4444; margin: 16px 0 8px;">◈ What No Consultant Will Tell You</h4>
    <div style="font-family: 'Courier New', monospace; padding: 16px; background: rgba(239,68,68,0.08); border-left: 3px solid #ef4444; border-radius: 4px;">${prov.what_mckinsey_wont_say}</div>`;
  }
  
  if (prov.contrarian_bet) {
    html += `<h4 style="color: #f97316; margin: 16px 0 8px;">✦ Contrarian Bet</h4><p style="font-style: italic;">${prov.contrarian_bet}</p>`;
  }
  
  return html;
}

/**
 * Render critical questions section
 * NEW: Renders array of {question, why_it_matters}
 */
function renderCriticalQuestions(questions) {
  if (!questions || !Array.isArray(questions) || questions.length === 0) {
    return `
      <ol class="questions-list">
        <li class="question-item">
          <div class="question-text">What are the hidden organizational barriers to AI adoption that aren't visible in our analysis?</div>
          <div class="question-why">Why it matters: Cultural resistance often kills AI initiatives faster than technical limitations.</div>
        </li>
        <li class="question-item">
          <div class="question-text">Which of your competitors are making stealth AI investments we can't see from public data?</div>
          <div class="question-why">Why it matters: The real competitive threats might not be visible yet.</div>
        </li>
        <li class="question-item">
          <div class="question-text">How will regulatory changes in the next 12-24 months impact your AI roadmap?</div>
          <div class="question-why">Why it matters: Compliance can either accelerate or destroy your timeline.</div>
        </li>
        <li class="question-item">
          <div class="question-text">What percentage of your technical debt is AI-blocking vs. just AI-slowing?</div>
          <div class="question-why">Why it matters: Not all tech debt is created equal—some is existential to AI adoption.</div>
        </li>
        <li class="question-item">
          <div class="question-text">Who in your organization has the political capital to actually drive AI transformation?</div>
          <div class="question-why">Why it matters: Strategy without internal champions is just expensive consulting theater.</div>
        </li>
      </ol>
    `;
  }
  
  let html = '<ol class="questions-list">';
  questions.forEach(q => {
    html += `
      <li class="question-item">
        <div class="question-text">${q.question || ''}</div>
        <div class="question-why">Why it matters: ${q.why_it_matters || ''}</div>
      </li>
    `;
  });
  html += '</ol>';
  
  return html;
}

/**
 * Render sources & methodology section
 * NEW: Renders structured sources object with subsections
 */
function renderSources(sources) {
  if (!sources || typeof sources !== 'object') {
    return `
      <div class="sources-subsection">
        <h4>Data Sources</h4>
        <p>This analysis was compiled from publicly available information including company websites, press releases, LinkedIn profiles, industry reports, and news articles. We analyzed organizational structure, job postings, technology stack indicators, and publicly stated AI initiatives.</p>
      </div>
      
      <div class="sources-subsection">
        <h4>Methodology</h4>
        <p><strong>Hyperthink</strong> is our proprietary multi-agent analysis framework. Here's how it works:</p>
        <ul>
          <li><strong>Agent 1: Data Collector</strong> — Gathers all available public information about the company</li>
          <li><strong>Agent 2: Strategic Analyst</strong> — Evaluates AI readiness across 4 key dimensions</li>
          <li><strong>Agent 3: Competitive Researcher</strong> — Maps your position vs. industry peers</li>
          <li><strong>Agent 4: Risk Assessor</strong> — Identifies blind spots and failure modes</li>
          <li><strong>Agent 5: The Provocateur</strong> — Challenges assumptions and surfaces uncomfortable truths</li>
        </ul>
        <p>Each agent reviews the others' work across 3 rounds of critical analysis, ensuring no stone is left unturned.</p>
      </div>
      
      <div class="sources-subsection">
        <h4>Limitations</h4>
        <p>This is a <strong>public data analysis</strong>. We don't have access to your internal systems, proprietary data, roadmaps, or employee interviews. The AI Readiness Score is comparative (based on industry benchmarks), not absolute. Risk assessments are probabilistic, not deterministic. For a truly comprehensive analysis, we'd need access to internal stakeholders and proprietary metrics.</p>
      </div>
      
      <div class="sources-subsection">
        <h4>Want More?</h4>
        <p>This free X-Ray is just the surface. A custom analysis with your internal data can be 10x more actionable. Interested? Reach out at <a href="https://finitematter.substack.com" style="color: #6366f1;">finitematter.substack.com</a></p>
      </div>
    `;
  }
  
  let html = '';
  
  // Data Sources
  if (sources.data_sources) {
    html += `
      <div class="sources-subsection">
        <h4>Data Sources</h4>
        <p>${sources.data_sources}</p>
      </div>
    `;
  }
  
  // Methodology
  if (sources.methodology) {
    html += `
      <div class="sources-subsection">
        <h4>Methodology</h4>
        ${sources.methodology}
      </div>
    `;
  }
  
  // Limitations
  if (sources.limitations) {
    html += `
      <div class="sources-subsection">
        <h4>Limitations</h4>
        <p>${sources.limitations}</p>
      </div>
    `;
  }
  
  // Source Links
  if (sources.links && sources.links.length > 0) {
    html += `
      <div class="sources-subsection">
        <h4>Source Links</h4>
        <div class="source-links">
    `;
    sources.links.forEach(link => {
      html += `<a href="${link.url}" target="_blank" rel="noopener">${link.title || link.url}</a>`;
    });
    html += `
        </div>
      </div>
    `;
  }
  
  return html;
}

/**
 * Main render function
 * Processes report data and generates HTML from template
 */
export function render(report, company) {
  log('RENDERER', 'Rendering HTML report...');
  
  let template = readFileSync(join(__dirname, 'template.html'), 'utf-8');
  
  const r = report;
  const ai = r.ai_readiness || {};
  const radar = ai.radar || r.competitive_position?.radar || {};
  const recs = r.recommendations || [{}, {}, {}];
  const road = r.roadmap || {};
  
  // Calculate donut chart dash array values
  const aiScore = ai.overall || 0;
  const dashArrayFilled = (aiScore * 2.83).toFixed(1);
  const dashArrayEmpty = (283 - aiScore * 2.83).toFixed(1);
  
  // Map difficulty values to lowercase for all recommendations
  const mapDifficulty = (difficulty) => {
    if (!difficulty) return 'medium';
    const d = difficulty.toString().toLowerCase();
    if (d.includes('easy') || d.includes('low')) return 'easy';
    if (d.includes('hard') || d.includes('high')) return 'hard';
    return 'medium';
  };
  
  const replacements = {
    'company_name': company,
    'generated_date': new Date().toLocaleDateString('en-US', { year: 'numeric', month: 'long', day: 'numeric' }),
    
    // Executive Summary
    'executive_summary': r.executive_summary || '',
    'executive_detail': r.executive_detail || '',
    
    // AI Readiness
    'ai_score_overall': ai.overall || 0,
    'ai_score_data': ai.data_infrastructure || 0,
    'ai_score_talent': ai.talent || 0,
    'ai_score_strategy': ai.strategy || 0,
    'ai_score_culture': ai.culture || 0,
    'ai_percentile': ai.percentile || 0,
    'ai_dasharray_filled': dashArrayFilled,
    'ai_dasharray_empty': dashArrayEmpty,
    'readiness_analysis': r.readiness_analysis || '',
    
    // Department Opportunities
    'department_analysis': r.department_analysis || '',
    'department_table_rows': renderDeptRows(r.department_opportunities || []),
    
    // Competitive Position
    'competitive_narrative': r.competitive_narrative || '',
    'radar_polygon_points': calcRadarPoints(radar),
    'radar_innovation': radar.innovation || 0,
    'radar_data_maturity': radar.data_maturity || 0,
    'radar_ai_adoption': radar.ai_adoption || 0,
    'radar_talent': radar.talent || 0,
    'radar_investment': radar.investment || 0,
    'competitive_insights': (r.competitive_position?.insights || []).map(i => `<li>${i}</li>`).join(''),
    
    // Recommendations
    'recommendation_1_title': recs[0]?.title || '',
    'recommendation_1_detail': recs[0]?.detail || '',
    'recommendation_1_why': recs[0]?.why || '',
    'recommendation_1_roi': recs[0]?.roi || '',
    'recommendation_1_timeline': recs[0]?.timeline || '',
    'recommendation_1_difficulty': mapDifficulty(recs[0]?.difficulty),
    
    'recommendation_2_title': recs[1]?.title || '',
    'recommendation_2_detail': recs[1]?.detail || '',
    'recommendation_2_why': recs[1]?.why || '',
    'recommendation_2_roi': recs[1]?.roi || '',
    'recommendation_2_timeline': recs[1]?.timeline || '',
    'recommendation_2_difficulty': mapDifficulty(recs[1]?.difficulty),
    
    'recommendation_3_title': recs[2]?.title || '',
    'recommendation_3_detail': recs[2]?.detail || '',
    'recommendation_3_why': recs[2]?.why || '',
    'recommendation_3_roi': recs[2]?.roi || '',
    'recommendation_3_timeline': recs[2]?.timeline || '',
    'recommendation_3_difficulty': mapDifficulty(recs[2]?.difficulty),
    
    // Roadmap
    'roadmap_narrative': r.roadmap_narrative || '',
    'roadmap_phase1': typeof road.phase1 === 'string' ? road.phase1 : JSON.stringify(road.phase1 || ''),
    'roadmap_phase2': typeof road.phase2 === 'string' ? road.phase2 : JSON.stringify(road.phase2 || ''),
    'roadmap_phase3': typeof road.phase3 === 'string' ? road.phase3 : JSON.stringify(road.phase3 || ''),
    
    // Risk Analysis
    'risk_narrative': r.risk_narrative || '',
    'risk_items': renderRiskItems(r.risks || []),
    'risk_details': renderRiskDetails(r.risks || []),
    
    // Provocateur
    'provocateur_section': renderProvocateur(r.provocateur || {}),
    
    // Critical Questions (NEW)
    'critical_questions': renderCriticalQuestions(r.critical_questions),
    
    // Bottom Line
    'total_opportunity': r.bottom_line?.total_opportunity || 'N/A',
    'investment_required': r.bottom_line?.investment_required || 'N/A',
    'payback_period': r.bottom_line?.payback_period || 'N/A',
    'bottom_line_summary': r.bottom_line?.summary || '',
    'bottom_line_detail': r.bottom_line?.detail || '',
    
    // Sources & Methodology (NEW)
    'sources_section': renderSources(r.sources),
  };

  // Replace all placeholders
  for (const [key, value] of Object.entries(replacements)) {
    template = template.replaceAll(`{{${key}}}`, String(value));
  }

  // Save to file
  const slug = slugify(company);
  mkdirSync(join(__dirname, 'output'), { recursive: true });
  const outPath = join(__dirname, 'output', `${slug}-xray.html`);
  writeFileSync(outPath, template);
  
  log('RENDERER', `✓ Report saved to: ${outPath}`);
  return outPath;
}
