import { readFileSync, writeFileSync, mkdirSync } from 'fs';
import { log, slugify } from './utils.js';
import { fileURLToPath } from 'url';
import { dirname, join } from 'path';

const __dirname = dirname(fileURLToPath(import.meta.url));

// Calculate radar chart polygon points for Deal Scorecard
// CORRECT parameters: cx=100, cy=100, r=75
function calcRadarPoints(scores, cx = 100, cy = 100, r = 75) {
  const dims = ['team', 'market', 'product', 'traction', 'timing'];
  const points = dims.map((dim, i) => {
    const angle = (Math.PI * 2 * i / 5) - Math.PI / 2; // Start at top
    const val = (scores[dim] || 50) / 100;
    const x = cx + r * val * Math.cos(angle);
    const y = cy + r * val * Math.sin(angle);
    return `${x.toFixed(1)},${y.toFixed(1)}`;
  });
  return points.join(' ');
}

// Generate Thesis Balance Scale SVG
function generateThesisBalanceScale(dealScore) {
  const score = dealScore || 50;
  // Scale tilts based on deal score (50 = balanced, >50 = bull, <50 = bear)
  const tiltAngle = (score - 50) * 0.3; // Max 15 degrees tilt
  
  return `
    <svg viewBox="0 0 500 300" width="500" height="300">
      <defs>
        <linearGradient id="bullGradient" x1="0%" y1="0%" x2="100%" y2="100%">
          <stop offset="0%" style="stop-color:#10b981;stop-opacity:1" />
          <stop offset="100%" style="stop-color:#059669;stop-opacity:1" />
        </linearGradient>
        <linearGradient id="bearGradient" x1="0%" y1="0%" x2="100%" y2="100%">
          <stop offset="0%" style="stop-color:#ef4444;stop-opacity:1" />
          <stop offset="100%" style="stop-color:#dc2626;stop-opacity:1" />
        </linearGradient>
      </defs>
      
      <!-- Base/Stand -->
      <rect x="220" y="200" width="60" height="80" fill="rgba(139,92,246,0.3)" stroke="#8b5cf6" stroke-width="2" rx="4"/>
      <rect x="180" y="275" width="140" height="15" fill="rgba(139,92,246,0.5)" stroke="#8b5cf6" stroke-width="2" rx="8"/>
      
      <!-- Center pole -->
      <line x1="250" y1="200" x2="250" y2="100" stroke="#8b5cf6" stroke-width="3"/>
      
      <!-- Balance beam (tilted based on score) -->
      <g transform="rotate(${tiltAngle}, 250, 100)">
        <rect x="100" y="95" width="300" height="10" fill="url(#gradient1)" stroke="#8b5cf6" stroke-width="2" rx="5"/>
        
        <!-- Left scale (Bull) -->
        <line x1="120" y1="100" x2="120" y2="120" stroke="#10b981" stroke-width="2"/>
        <line x1="120" y1="120" x2="100" y2="140" stroke="#10b981" stroke-width="2"/>
        <line x1="120" y1="120" x2="140" y2="140" stroke="#10b981" stroke-width="2"/>
        <line x1="100" y1="140" x2="140" y2="140" stroke="#10b981" stroke-width="2"/>
        <rect x="80" y="140" width="80" height="40" fill="url(#bullGradient)" stroke="#10b981" stroke-width="2" rx="4"/>
        <text x="120" y="165" text-anchor="middle" fill="white" font-size="14" font-weight="700">BULL</text>
        
        <!-- Right scale (Bear) -->
        <line x1="380" y1="100" x2="380" y2="120" stroke="#ef4444" stroke-width="2"/>
        <line x1="380" y1="120" x2="360" y2="140" stroke="#ef4444" stroke-width="2"/>
        <line x1="380" y1="120" x2="400" y2="140" stroke="#ef4444" stroke-width="2"/>
        <line x1="360" y1="140" x2="400" y2="140" stroke="#ef4444" stroke-width="2"/>
        <rect x="340" y="140" width="80" height="40" fill="url(#bearGradient)" stroke="#ef4444" stroke-width="2" rx="4"/>
        <text x="380" y="165" text-anchor="middle" fill="white" font-size="14" font-weight="700">BEAR</text>
      </g>
      
      <!-- Balance point indicator -->
      <circle cx="250" cy="100" r="8" fill="#8b5cf6" stroke="white" stroke-width="2"/>
      
      <!-- Score label -->
      <text x="250" y="50" text-anchor="middle" fill="#8b5cf6" font-size="16" font-weight="700">
        Deal Score: ${score}/100
      </text>
      <text x="250" y="70" text-anchor="middle" fill="#9ca3af" font-size="12">
        ${score > 60 ? 'Bull case dominates' : score < 40 ? 'Bear case dominates' : 'Balanced outlook'}
      </text>
    </svg>
  `;
}

// Convert confidence level to dots
function confidenceDots(level) {
  const dots = {
    'HIGH': '●●●●●',
    'GOOD': '●●●●○',
    'MODERATE': '●●●○○',
    'LOW': '●●○○○',
    'SPECULATIVE': '●○○○○',
    'VERIFIED': '●●●●●',
    'LIKELY': '●●●●○',
    'ESTIMATED': '●●●○○',
    'UNKNOWN': '●○○○○'
  };
  return dots[level] || '●●●○○';
}

// Confidence label
function confidenceLabel(level) {
  const labels = {
    'HIGH': 'High Confidence',
    'GOOD': 'Good Confidence',
    'MODERATE': 'Moderate Confidence',
    'LOW': 'Low Confidence',
    'SPECULATIVE': 'Speculative',
    'VERIFIED': 'Verified',
    'LIKELY': 'Likely',
    'ESTIMATED': 'Estimated',
    'UNKNOWN': 'Unknown'
  };
  return labels[level] || level;
}

// Map confidence level to CSS class
function confidenceClass(level) {
  const mapping = {
    'HIGH': 'high',
    'GOOD': 'good',
    'MODERATE': 'moderate',
    'LOW': 'low',
    'SPECULATIVE': 'speculative',
    'VERIFIED': 'high',
    'LIKELY': 'good',
    'ESTIMATED': 'moderate',
    'UNKNOWN': 'low'
  };
  return mapping[level] || 'moderate';
}

// Render founders table
function renderFounders(founders) {
  if (!founders?.length) return '<p style="color: #9ca3af;">Founder data not available.</p>';
  return founders.map((f, i) => `
    <div style="margin-bottom: 16px; padding: 12px; background: rgba(255,255,255,0.02); border-radius: 8px;">
      <div style="display: flex; justify-content: space-between; align-items: start;">
        <div>
          <h4 style="margin: 0 0 4px 0; color: #8b5cf6;">${f.name || 'Founder ' + (i+1)}</h4>
          <p style="margin: 4px 0; color: #9ca3af; font-size: 0.9rem;">${f.background || ''}</p>
          <p style="margin: 4px 0; color: #d1d5db;"><strong>Assessment:</strong> ${f.strength || ''}</p>
        </div>
        <span style="font-size: 0.85rem; color: #9ca3af;" title="${confidenceLabel(f.confidence)}">
          ${confidenceDots(f.confidence)}
        </span>
      </div>
    </div>
  `).join('');
}

// Render founder network analysis
function renderFounderNetwork(analysis) {
  if (!analysis) return '';
  return `
    <h3 style="color: #8b5cf6; margin: 24px 0 12px 0;">Founder Network Analysis</h3>
    <p>${analysis}</p>
  `;
}

// Render timing analysis with timeline
function renderTimingAnalysis(text) {
  if (!text) return '<p>Market timing analysis not available.</p>';
  return `
    <div class="timing-timeline">
      <p>${text}</p>
    </div>
  `;
}

// Render competitors table
function renderCompetitors(competitors) {
  if (!competitors?.length) return '<p style="color: #9ca3af;">Competitor data not available.</p>';
  return `
    <table style="width: 100%; border-collapse: collapse; margin-top: 12px;">
      <thead>
        <tr style="border-bottom: 1px solid rgba(255,255,255,0.1);">
          <th style="padding: 8px; text-align: left; color: #9ca3af; font-weight: 600;">Competitor</th>
          <th style="padding: 8px; text-align: left; color: #9ca3af; font-weight: 600;">Position</th>
          <th style="padding: 8px; text-align: left; color: #9ca3af; font-weight: 600;">Threat Level</th>
        </tr>
      </thead>
      <tbody>
        ${competitors.map((c, i) => `
          <tr style="background: ${i % 2 === 0 ? 'rgba(255,255,255,0.02)' : 'transparent'};">
            <td style="padding: 10px 8px; font-weight: 600;">${c.name}</td>
            <td style="padding: 10px 8px; color: #d1d5db;">${c.position}</td>
            <td style="padding: 10px 8px;">
              <span style="padding: 2px 10px; border-radius: 12px; font-size: 0.8rem; background: ${
                c.threat_level === 'High' ? 'rgba(239,68,68,0.15); color: #ef4444' : 
                c.threat_level === 'Medium' ? 'rgba(251,191,36,0.15); color: #fbbf24' : 
                'rgba(16,185,129,0.15); color: #10b981'
              };">${c.threat_level}</span>
            </td>
          </tr>
        `).join('')}
      </tbody>
    </table>
  `;
}

// Render comparables table
function renderComparables(comparables) {
  if (!comparables?.length) return '<p style="color: #9ca3af;">Comparable deal data not available.</p>';
  return `
    <table style="width: 100%; border-collapse: collapse; margin-top: 12px;">
      <thead>
        <tr style="border-bottom: 1px solid rgba(255,255,255,0.1);">
          <th style="padding: 8px; text-align: left; color: #9ca3af; font-weight: 600;">Company</th>
          <th style="padding: 8px; text-align: left; color: #9ca3af; font-weight: 600;">Stage</th>
          <th style="padding: 8px; text-align: left; color: #9ca3af; font-weight: 600;">Valuation</th>
          <th style="padding: 8px; text-align: left; color: #9ca3af; font-weight: 600;">Outcome</th>
        </tr>
      </thead>
      <tbody>
        ${comparables.map((c, i) => `
          <tr style="background: ${i % 2 === 0 ? 'rgba(255,255,255,0.02)' : 'transparent'};">
            <td style="padding: 10px 8px; font-weight: 600;">${c.company}</td>
            <td style="padding: 10px 8px; color: #d1d5db;">${c.stage}</td>
            <td style="padding: 10px 8px; color: #10b981;">${c.valuation}</td>
            <td style="padding: 10px 8px; color: #9ca3af;">${c.outcome}</td>
          </tr>
        `).join('')}
      </tbody>
    </table>
  `;
}

// Render growth levers
function renderGrowthLevers(levers) {
  if (!levers?.length) return '<p style="color: #9ca3af;">No growth levers identified.</p>';
  return levers.map((l, i) => `
    <div style="margin-bottom: 16px; padding: 14px; background: rgba(139,92,246,0.05); border-left: 3px solid #8b5cf6; border-radius: 6px;">
      <div style="display: flex; justify-content: space-between; align-items: start; margin-bottom: 8px;">
        <h4 style="margin: 0; color: #8b5cf6;">${i+1}. ${l.lever}</h4>
        <span style="padding: 2px 10px; border-radius: 12px; font-size: 0.75rem; background: ${
          l.difficulty === 'Easy' ? 'rgba(16,185,129,0.15); color: #10b981' :
          l.difficulty === 'Hard' ? 'rgba(239,68,68,0.15); color: #ef4444' :
          'rgba(251,191,36,0.15); color: #fbbf24'
        };">${l.difficulty}</span>
      </div>
      <p style="margin: 6px 0; color: #10b981; font-weight: 600;">Impact: ${l.impact}</p>
      <p style="margin: 6px 0; color: #9ca3af; font-size: 0.9rem;">Timeline: ${l.timeline}</p>
      <p style="margin: 10px 0 0 0; color: #d1d5db; line-height: 1.6;">${l.detail}</p>
    </div>
  `).join('');
}

// Render devil's advocate section
function renderDevilsAdvocate(devil) {
  let html = '';
  
  if (devil.red_flags?.length) {
    html += '<h4 style="color: #ef4444; margin: 0 0 12px 0; display: flex; align-items: center; gap: 8px;"><svg style="width: 20px; height: 20px;" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" d="M3 3v1.5M3 21v-6m0 0l2.77-.693a9 9 0 016.208.682l.108.054a9 9 0 006.086.71l3.114-.732a48.524 48.524 0 01-.005-10.499l-3.11.732a9 9 0 01-6.085-.711l-.108-.054a9 9 0 00-6.208-.682L3 4.5M3 15V4.5" /></svg> Red Flags</h4>';
    devil.red_flags.forEach((flag, i) => {
      html += `<div style="margin-bottom: 10px; padding: 10px; background: rgba(239,68,68,0.05); border-radius: 6px;">
        <strong style="color: #ef4444;">Flag ${i+1}:</strong>
        <p style="margin: 6px 0 0 0; color: #d1d5db; line-height: 1.6;">${flag}</p>
      </div>`;
    });
  }
  
  if (devil.kill_shots?.length) {
    html += '<h4 style="color: #f97316; margin: 20px 0 12px 0; display: flex; align-items: center; gap: 8px;"><svg style="width: 20px; height: 20px;" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" d="M12 9v3.75m-9.303 3.376c-.866 1.5.217 3.374 1.948 3.374h14.71c1.73 0 2.813-1.874 1.948-3.374L13.949 3.378c-.866-1.5-3.032-1.5-3.898 0L2.697 16.126zM12 15.75h.007v.008H12v-.008z" /></svg> Kill Shots</h4>';
    devil.kill_shots.forEach((shot, i) => {
      html += `<div style="margin-bottom: 10px; padding: 10px; background: rgba(249,115,22,0.05); border-radius: 6px;">
        <strong style="color: #f97316;">Kill Shot ${i+1}:</strong>
        <p style="margin: 6px 0 0 0; color: #d1d5db; line-height: 1.6;">${shot}</p>
      </div>`;
    });
  }
  
  if (devil.uncomfortable_question) {
    html += `<h4 style="color: #fbbf24; margin: 20px 0 12px 0; display: flex; align-items: center; gap: 8px;"><svg style="width: 20px; height: 20px;" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" d="M9.879 7.519c1.171-1.025 3.071-1.025 4.242 0 1.172 1.025 1.172 2.687 0 3.712-.203.179-.43.326-.67.442-.745.361-1.45.999-1.45 1.827v.75M21 12a9 9 0 11-18 0 9 9 0 0118 0zm-9 5.25h.008v.008H12v-.008z" /></svg> The Uncomfortable Question</h4>
    <div style="padding: 12px; background: rgba(251,191,36,0.05); border-radius: 6px;">
      <p style="margin: 0 0 8px 0; color: #fbbf24; font-weight: 600; font-size: 1.05rem;">${devil.uncomfortable_question.question}</p>
      <p style="margin: 0; color: #9ca3af; line-height: 1.6;">${devil.uncomfortable_question.why_it_matters}</p>
    </div>`;
  }
  
  if (devil.pattern_matching) {
    html += `<h4 style="color: #a78bfa; margin: 20px 0 12px 0; display: flex; align-items: center; gap: 8px;"><svg style="width: 20px; height: 20px;" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" d="M2.036 12.322a1.012 1.012 0 010-.639C3.423 7.51 7.36 4.5 12 4.5c4.638 0 8.573 3.007 9.963 7.178.07.207.07.431 0 .639C20.577 16.49 16.64 19.5 12 19.5c-4.638 0-8.573-3.007-9.963-7.178z" /><path stroke-linecap="round" stroke-linejoin="round" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z" /></svg> Pattern Matching</h4>
    <div style="padding: 12px; background: rgba(167,139,250,0.05); border-radius: 6px;">
      <p style="margin: 0 0 6px 0;"><strong>Failed comparable:</strong> ${devil.pattern_matching.failed_comparable}</p>
      <p style="margin: 6px 0; color: #d1d5db; line-height: 1.6;"><strong>Why similar:</strong> ${devil.pattern_matching.why_similar}</p>
      <p style="margin: 6px 0; color: #d1d5db; line-height: 1.6;"><strong>What must differ:</strong> ${devil.pattern_matching.what_must_differ}</p>
    </div>`;
  }
  
  if (devil.contrarian_take) {
    html += `<h4 style="color: #ec4899; margin: 20px 0 12px 0; display: flex; align-items: center; gap: 8px;"><svg style="width: 20px; height: 20px;" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" d="M3.75 13.5l10.5-11.25L12 10.5h8.25L9.75 21.75 12 13.5H3.75z" /></svg> Contrarian Take</h4>
    <div style="padding: 12px; background: rgba(236,72,153,0.05); border-radius: 6px;">
      <p style="margin: 0; color: #d1d5db; line-height: 1.6;">${devil.contrarian_take}</p>
    </div>`;
  }
  
  return html;
}

// Render unique insights
function renderUniqueInsights(insights) {
  if (!insights?.length) return '<p style="color: #9ca3af;">No unique insights identified.</p>';
  return `<div class="unique-insights-grid">
    ${insights.map(insight => `
      <div class="insight-card">
        <div class="insight-label">Insight:</div>
        <div class="insight-text">${insight}</div>
      </div>
    `).join('')}
  </div>`;
}

// Render hidden signals
function renderHiddenSignals(signals) {
  if (!signals) return '';
  return {
    hiring: signals.hiring_signal || 'No hiring signal data available.',
    tech: signals.tech_signal || 'No tech stack signal available.',
    competitive: signals.competitive_signal || 'No competitive signal available.',
    funding: signals.funding_signal || 'No funding signal available.'
  };
}

// Render five questions
function renderQuestions(questions) {
  if (!questions?.length) return '<p style="color: #9ca3af;">No questions available.</p>';
  return questions.map((q, i) => `
    <div style="margin-bottom: 12px; padding: 12px; background: rgba(255,255,255,0.02); border-left: 3px solid #8b5cf6; border-radius: 6px;">
      <p style="margin: 0 0 6px 0; color: #8b5cf6; font-weight: 600; font-size: 1.02rem;">${i+1}. ${q.question}</p>
      <p style="margin: 0; color: #9ca3af; font-size: 0.9rem; line-height: 1.5;">${q.why_it_matters}</p>
    </div>
  `).join('');
}

// Render confidence heatmap
function renderConfidenceHeatmap(report) {
  if (!report.section_scores?.length) return '<p style="color: #9ca3af;">Confidence data not available.</p>';
  
  let html = '<table><thead><tr><th>Section</th><th>Confidence Level</th><th>Sources</th><th>Data Gaps</th></tr></thead><tbody>';
  
  report.section_scores.forEach((s, i) => {
    const cssClass = confidenceClass(s.confidence);
    html += `<tr style="background: ${i % 2 === 0 ? 'rgba(255,255,255,0.02)' : 'transparent'};">
      <td style="font-weight: 600;">${s.section}</td>
      <td><span class="confidence-cell ${cssClass}">${s.confidence}</span></td>
      <td style="color: #9ca3af;">${s.source_count || 0} sources</td>
      <td style="color: #ef4444; font-size: 0.85rem;">${(s.gaps || []).join(', ') || 'None'}</td>
    </tr>`;
  });
  
  html += '</tbody></table>';
  return html;
}

// Render data confidence report
function renderConfidenceReport(report) {
  let html = '';
  
  if (report.critical_missing_data?.length) {
    html += '<h4 style="color: #ef4444; margin: 20px 0 8px 0; display: flex; align-items: center; gap: 8px;"><svg style="width: 20px; height: 20px;" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" d="M12 9v3.75m-9.303 3.376c-.866 1.5.217 3.374 1.948 3.374h14.71c1.73 0 2.813-1.874 1.948-3.374L13.949 3.378c-.866-1.5-3.032-1.5-3.898 0L2.697 16.126zM12 15.75h.007v.008H12v-.008z" /></svg> Critical Missing Data</h4><ul style="color: #d1d5db; line-height: 1.8;">';
    report.critical_missing_data.forEach(d => html += `<li>${d}</li>`);
    html += '</ul>';
  }
  
  return html;
}

export function render(report, startup) {
  log('RENDERER', 'Loading template...');
  const template = readFileSync(join(__dirname, 'template.html'), 'utf-8');
  
  // Generate SVG data
  const radarPolygon = calcRadarPoints(report.deal_score || {});
  const scoreOverall = Math.round(report.deal_score?.overall || 0);
  
  // Deal Score Donut calculations
  const circumference = 2 * Math.PI * 80; // r=80
  const scorePercent = scoreOverall / 100;
  const dashOffset = circumference * (1 - scorePercent);
  const percentile = scoreOverall >= 80 ? 'Top 10% of startups analyzed' :
                     scoreOverall >= 70 ? 'Top 25% of startups analyzed' :
                     scoreOverall >= 60 ? 'Top 40% of startups analyzed' :
                     'Below median startup performance';
  
  // Valuation range calculations
  const valuationMin = report.financial_assessment?.valuation_range?.min || report.financial_assessment?.valuation_estimate?.low || 'N/A';
  const valuationMax = report.financial_assessment?.valuation_range?.max || report.financial_assessment?.valuation_estimate?.high || 'N/A';
  const valuationEstimated = report.financial_assessment?.valuation_range?.estimated || valuationMin;
  const valuationMethodology = report.financial_assessment?.valuation_range?.methodology || report.financial_assessment?.valuation_estimate?.methodology || 'Based on comparable transactions and market multiples.';
  
  // Calculate valuation marker position (as percentage)
  // This is a rough estimate - in production, parse the dollar amounts
  const valuationEstimatedPercent = 50; // Default to middle
  
  // Generate Thesis Balance Scale
  const thesisBalanceScale = generateThesisBalanceScale(scoreOverall);
  
  // Render HTML sections
  const foundersHtml = renderFounders(report.founder_xray?.founders);
  const founderNetworkHtml = renderFounderNetwork(report.founder_network_analysis);
  const timingAnalysisHtml = renderTimingAnalysis(report.timing_analysis);
  const competitorsHtml = renderCompetitors(report.competitive_landscape?.competitors);
  const comparablesHtml = renderComparables(report.financial_assessment?.comparables);
  const growthLeversHtml = renderGrowthLevers(report.growth_levers);
  const devilsAdvocateHtml = renderDevilsAdvocate(report.devils_advocate || {});
  const uniqueInsightsHtml = renderUniqueInsights(report.unique_insights);
  const questionsHtml = renderQuestions(report.five_questions);
  const confidenceHeatmapHtml = renderConfidenceHeatmap(report.data_confidence_report || {});
  const confidenceReportHtml = renderConfidenceReport(report.data_confidence_report || {});
  
  // Hidden signals
  const hiddenSignals = renderHiddenSignals(report.hidden_signals);
  
  // Replace template variables
  let html = template
    .replace(/\{\{STARTUP_NAME\}\}/g, startup)
    .replace(/\{\{DATE\}\}/g, new Date().toLocaleDateString('en-US', { year: 'numeric', month: 'long', day: 'numeric' }))
    
    // Deal Score
    .replace(/\{\{DEAL_SCORE\}\}/g, scoreOverall)
    .replace(/\{\{DEAL_SCORE_CIRCUMFERENCE\}\}/g, circumference.toFixed(2))
    .replace(/\{\{DEAL_SCORE_OFFSET\}\}/g, dashOffset.toFixed(2))
    .replace(/\{\{DEAL_SCORE_PERCENTILE\}\}/g, percentile)
    .replace(/\{\{DEAL_SCORE_TEAM\}\}/g, Math.round(report.deal_score?.team || 0))
    .replace(/\{\{DEAL_SCORE_MARKET\}\}/g, Math.round(report.deal_score?.market || 0))
    .replace(/\{\{DEAL_SCORE_PRODUCT\}\}/g, Math.round(report.deal_score?.product || 0))
    .replace(/\{\{DEAL_SCORE_TRACTION\}\}/g, Math.round(report.deal_score?.traction || 0))
    .replace(/\{\{DEAL_SCORE_TIMING\}\}/g, Math.round(report.deal_score?.timing || 0))
    .replace(/\{\{RADAR_POLYGON\}\}/g, radarPolygon)
    
    // TL;DR
    .replace(/\{\{TLDR\}\}/g, report.tldr || '')
    .replace(/\{\{TLDR_DETAIL\}\}/g, report.tldr_detail || '')
    
    // Founders
    .replace(/\{\{FOUNDERS_HTML\}\}/g, foundersHtml)
    .replace(/\{\{FOUNDER_MARKET_FIT\}\}/g, report.founder_xray?.founder_market_fit || '')
    .replace(/\{\{FOUNDER_NETWORK_HTML\}\}/g, founderNetworkHtml)
    
    // Market
    .replace(/\{\{TAM\}\}/g, report.tam_sam_som?.tam || report.market_opportunity?.tam_sam_som?.tam || 'N/A')
    .replace(/\{\{SAM\}\}/g, report.tam_sam_som?.sam || report.market_opportunity?.tam_sam_som?.sam || 'N/A')
    .replace(/\{\{SOM\}\}/g, report.tam_sam_som?.som || report.market_opportunity?.tam_sam_som?.som || 'N/A')
    .replace(/\{\{TIMING_ANALYSIS_HTML\}\}/g, timingAnalysisHtml)
    .replace(/\{\{MARKET_DYNAMICS\}\}/g, report.market_opportunity?.dynamics || '')
    
    // Competitive
    .replace(/\{\{COMPETITORS_HTML\}\}/g, competitorsHtml)
    .replace(/\{\{DEFENSIBILITY\}\}/g, report.competitive_landscape?.defensibility || '')
    .replace(/\{\{DEFENSIBILITY_SCORE\}\}/g, Math.round(report.competitive_landscape?.defensibility_score || 0))
    
    // Traction
    .replace(/\{\{TRACTION_ASSESSMENT\}\}/g, report.traction_growth?.assessment || '')
    
    // Hidden Signals (NEW)
    .replace(/\{\{HIRING_SIGNAL\}\}/g, hiddenSignals.hiring)
    .replace(/\{\{TECH_SIGNAL\}\}/g, hiddenSignals.tech)
    .replace(/\{\{COMPETITIVE_SIGNAL\}\}/g, hiddenSignals.competitive)
    .replace(/\{\{FUNDING_SIGNAL\}\}/g, hiddenSignals.funding)
    
    // Financial
    .replace(/\{\{VALUATION_MIN\}\}/g, valuationMin)
    .replace(/\{\{VALUATION_MAX\}\}/g, valuationMax)
    .replace(/\{\{VALUATION_ESTIMATED\}\}/g, valuationEstimated)
    .replace(/\{\{VALUATION_ESTIMATED_PERCENT\}\}/g, valuationEstimatedPercent)
    .replace(/\{\{VALUATION_METHODOLOGY\}\}/g, valuationMethodology)
    .replace(/\{\{COMPARABLES_HTML\}\}/g, comparablesHtml)
    .replace(/\{\{UNIT_ECONOMICS\}\}/g, report.financial_assessment?.unit_economics || '')
    
    // Growth & Strategy
    .replace(/\{\{GROWTH_LEVERS_HTML\}\}/g, growthLeversHtml)
    .replace(/\{\{DEVILS_ADVOCATE_HTML\}\}/g, devilsAdvocateHtml)
    
    // Unique Insights (NEW)
    .replace(/\{\{UNIQUE_INSIGHTS_HTML\}\}/g, uniqueInsightsHtml)
    
    // Thesis
    .replace(/\{\{THESIS_BALANCE_SCALE_SVG\}\}/g, thesisBalanceScale)
    .replace(/\{\{BULL_CASE\}\}/g, report.investment_thesis?.bull_case || '')
    .replace(/\{\{BEAR_CASE\}\}/g, report.investment_thesis?.bear_case || '')
    
    // Questions & Bottom Line
    .replace(/\{\{QUESTIONS_HTML\}\}/g, questionsHtml)
    .replace(/\{\{RECOMMENDATION\}\}/g, report.bottom_line?.recommendation || 'DIG_DEEPER')
    .replace(/\{\{BOTTOM_LINE_REASONING\}\}/g, report.bottom_line?.reasoning || '')
    
    // Data Confidence
    .replace(/\{\{CONFIDENCE_HEATMAP_HTML\}\}/g, confidenceHeatmapHtml)
    .replace(/\{\{CONFIDENCE_REPORT_HTML\}\}/g, confidenceReportHtml)
    .replace(/\{\{OVERALL_CONFIDENCE\}\}/g, confidenceDots(report.data_confidence_report?.overall_confidence))
    .replace(/\{\{OVERALL_CONFIDENCE_LABEL\}\}/g, confidenceLabel(report.data_confidence_report?.overall_confidence));
  
  // Add confidence indicators to section headers
  html = html.replace(/\{\{CONFIDENCE_FOUNDERS\}\}/g, confidenceDots(report.founder_xray?.confidence || 'MODERATE'))
    .replace(/\{\{CONFIDENCE_MARKET\}\}/g, confidenceDots(report.market_opportunity?.confidence || 'MODERATE'))
    .replace(/\{\{CONFIDENCE_COMPETITIVE\}\}/g, confidenceDots(report.competitive_landscape?.confidence || 'MODERATE'))
    .replace(/\{\{CONFIDENCE_TRACTION\}\}/g, confidenceDots(report.traction_growth?.confidence || 'LOW'))
    .replace(/\{\{CONFIDENCE_FINANCIAL\}\}/g, confidenceDots(report.financial_assessment?.confidence || 'LOW'))
    .replace(/\{\{CONFIDENCE_THESIS\}\}/g, confidenceDots(report.investment_thesis?.confidence || 'MODERATE'));
  
  // Write output
  mkdirSync(join(__dirname, 'output'), { recursive: true });
  const fileName = `${slugify(startup)}-xray.html`;
  const outputPath = join(__dirname, 'output', fileName);
  writeFileSync(outputPath, html, 'utf-8');
  
  log('RENDERER', `Report saved: ${outputPath}`);
  return outputPath;
}
