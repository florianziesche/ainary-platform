import { readFileSync, writeFileSync, mkdirSync } from 'fs';
import { log, slugify } from './utils.js';
import { fileURLToPath } from 'url';
import { dirname, join } from 'path';

const __dirname = dirname(fileURLToPath(import.meta.url));

// Calculate radar chart polygon points for Deal Scorecard
function calcRadarPoints(scores, cx = 100, cy = 100, r = 75) {
  const dims = ['team', 'market', 'product', 'traction', 'timing'];
  const points = dims.map((dim, i) => {
    const angle = (Math.PI * 2 * i / 5) - Math.PI / 2;
    const val = (scores[dim] || 50) / 100;
    const x = cx + r * val * Math.cos(angle);
    const y = cy + r * val * Math.sin(angle);
    return `${x.toFixed(1)},${y.toFixed(1)}`;
  });
  return points.join(' ');
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
    'ESTIMATED': '●●○○○',
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
    html += '<h4 style="color: #ef4444; margin: 0 0 12px 0;">🚩 Red Flags</h4>';
    devil.red_flags.forEach((flag, i) => {
      html += `<div style="margin-bottom: 10px; padding: 10px; background: rgba(239,68,68,0.05); border-radius: 6px;">
        <strong style="color: #ef4444;">Flag ${i+1}:</strong>
        <p style="margin: 6px 0 0 0; color: #d1d5db; line-height: 1.6;">${flag}</p>
      </div>`;
    });
  }
  
  if (devil.kill_shots?.length) {
    html += '<h4 style="color: #f97316; margin: 20px 0 12px 0;">💀 Kill Shots</h4>';
    devil.kill_shots.forEach((shot, i) => {
      html += `<div style="margin-bottom: 10px; padding: 10px; background: rgba(249,115,22,0.05); border-radius: 6px;">
        <strong style="color: #f97316;">Kill Shot ${i+1}:</strong>
        <p style="margin: 6px 0 0 0; color: #d1d5db; line-height: 1.6;">${shot}</p>
      </div>`;
    });
  }
  
  if (devil.uncomfortable_question) {
    html += `<h4 style="color: #fbbf24; margin: 20px 0 12px 0;">❓ The Uncomfortable Question</h4>
    <div style="padding: 12px; background: rgba(251,191,36,0.05); border-radius: 6px;">
      <p style="margin: 0 0 8px 0; color: #fbbf24; font-weight: 600; font-size: 1.05rem;">${devil.uncomfortable_question.question}</p>
      <p style="margin: 0; color: #9ca3af; line-height: 1.6;">${devil.uncomfortable_question.why_it_matters}</p>
    </div>`;
  }
  
  if (devil.pattern_matching) {
    html += `<h4 style="color: #a78bfa; margin: 20px 0 12px 0;">🔍 Pattern Matching</h4>
    <div style="padding: 12px; background: rgba(167,139,250,0.05); border-radius: 6px;">
      <p style="margin: 0 0 6px 0;"><strong>Failed comparable:</strong> ${devil.pattern_matching.failed_comparable}</p>
      <p style="margin: 6px 0; color: #d1d5db; line-height: 1.6;"><strong>Why similar:</strong> ${devil.pattern_matching.why_similar}</p>
      <p style="margin: 6px 0; color: #d1d5db; line-height: 1.6;"><strong>What must differ:</strong> ${devil.pattern_matching.what_must_differ}</p>
    </div>`;
  }
  
  if (devil.contrarian_take) {
    html += `<h4 style="color: #ec4899; margin: 20px 0 12px 0;">🎯 Contrarian Take</h4>
    <div style="padding: 12px; background: rgba(236,72,153,0.05); border-radius: 6px;">
      <p style="margin: 0; color: #d1d5db; line-height: 1.6;">${devil.contrarian_take}</p>
    </div>`;
  }
  
  return html;
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

// Render data confidence report
function renderConfidenceReport(report) {
  let html = '';
  
  if (report.section_scores?.length) {
    html += '<table style="width: 100%; border-collapse: collapse; margin-top: 12px;"><thead><tr style="border-bottom: 1px solid rgba(255,255,255,0.1);"><th style="padding: 8px; text-align: left; color: #9ca3af;">Section</th><th style="padding: 8px; text-align: left; color: #9ca3af;">Confidence</th><th style="padding: 8px; text-align: left; color: #9ca3af;">Sources</th><th style="padding: 8px; text-align: left; color: #9ca3af;">Data Gaps</th></tr></thead><tbody>';
    
    report.section_scores.forEach((s, i) => {
      html += `<tr style="background: ${i % 2 === 0 ? 'rgba(255,255,255,0.02)' : 'transparent'};">
        <td style="padding: 10px 8px; font-weight: 600;">${s.section}</td>
        <td style="padding: 10px 8px;"><span title="${confidenceLabel(s.confidence)}">${confidenceDots(s.confidence)}</span> ${s.confidence}</td>
        <td style="padding: 10px 8px; color: #9ca3af;">${s.source_count || 0}</td>
        <td style="padding: 10px 8px; color: #ef4444; font-size: 0.85rem;">${(s.gaps || []).join(', ') || 'None'}</td>
      </tr>`;
    });
    
    html += '</tbody></table>';
  }
  
  if (report.critical_missing_data?.length) {
    html += '<h4 style="color: #ef4444; margin: 20px 0 8px 0;">⚠️ Critical Missing Data</h4><ul style="color: #d1d5db; line-height: 1.8;">';
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
  
  // Build HTML sections
  const foundersHtml = renderFounders(report.founder_xray?.founders);
  const competitorsHtml = renderCompetitors(report.competitive_landscape?.competitors);
  const comparablesHtml = renderComparables(report.financial_assessment?.comparables);
  const growthLeversHtml = renderGrowthLevers(report.growth_levers);
  const devilsAdvocateHtml = renderDevilsAdvocate(report.devils_advocate || {});
  const questionsHtml = renderQuestions(report.five_questions);
  const confidenceReportHtml = renderConfidenceReport(report.data_confidence_report || {});
  
  // Replace template variables
  let html = template
    .replace(/\{\{STARTUP_NAME\}\}/g, startup)
    .replace(/\{\{DATE\}\}/g, new Date().toLocaleDateString('en-US', { year: 'numeric', month: 'long', day: 'numeric' }))
    .replace(/\{\{DEAL_SCORE\}\}/g, scoreOverall)
    .replace(/\{\{DEAL_SCORE_TEAM\}\}/g, Math.round(report.deal_score?.team || 0))
    .replace(/\{\{DEAL_SCORE_MARKET\}\}/g, Math.round(report.deal_score?.market || 0))
    .replace(/\{\{DEAL_SCORE_PRODUCT\}\}/g, Math.round(report.deal_score?.product || 0))
    .replace(/\{\{DEAL_SCORE_TRACTION\}\}/g, Math.round(report.deal_score?.traction || 0))
    .replace(/\{\{DEAL_SCORE_TIMING\}\}/g, Math.round(report.deal_score?.timing || 0))
    .replace(/\{\{RADAR_POLYGON\}\}/g, radarPolygon)
    .replace(/\{\{TLDR\}\}/g, report.tldr || '')
    .replace(/\{\{TLDR_DETAIL\}\}/g, report.tldr_detail || '')
    .replace(/\{\{FOUNDERS_HTML\}\}/g, foundersHtml)
    .replace(/\{\{FOUNDER_MARKET_FIT\}\}/g, report.founder_xray?.founder_market_fit || '')
    .replace(/\{\{TAM\}\}/g, report.market_opportunity?.tam_sam_som?.tam || 'N/A')
    .replace(/\{\{SAM\}\}/g, report.market_opportunity?.tam_sam_som?.sam || 'N/A')
    .replace(/\{\{SOM\}\}/g, report.market_opportunity?.tam_sam_som?.som || 'N/A')
    .replace(/\{\{MARKET_TIMING\}\}/g, report.market_opportunity?.market_timing || '')
    .replace(/\{\{MARKET_DYNAMICS\}\}/g, report.market_opportunity?.dynamics || '')
    .replace(/\{\{COMPETITORS_HTML\}\}/g, competitorsHtml)
    .replace(/\{\{DEFENSIBILITY\}\}/g, report.competitive_landscape?.defensibility || '')
    .replace(/\{\{DEFENSIBILITY_SCORE\}\}/g, Math.round(report.competitive_landscape?.defensibility_score || 0))
    .replace(/\{\{TRACTION_ASSESSMENT\}\}/g, report.traction_growth?.assessment || '')
    .replace(/\{\{COMPARABLES_HTML\}\}/g, comparablesHtml)
    .replace(/\{\{VALUATION_LOW\}\}/g, report.financial_assessment?.valuation_estimate?.low || 'N/A')
    .replace(/\{\{VALUATION_HIGH\}\}/g, report.financial_assessment?.valuation_estimate?.high || 'N/A')
    .replace(/\{\{UNIT_ECONOMICS\}\}/g, report.financial_assessment?.unit_economics || '')
    .replace(/\{\{GROWTH_LEVERS_HTML\}\}/g, growthLeversHtml)
    .replace(/\{\{DEVILS_ADVOCATE_HTML\}\}/g, devilsAdvocateHtml)
    .replace(/\{\{BULL_CASE\}\}/g, report.investment_thesis?.bull_case || '')
    .replace(/\{\{BEAR_CASE\}\}/g, report.investment_thesis?.bear_case || '')
    .replace(/\{\{QUESTIONS_HTML\}\}/g, questionsHtml)
    .replace(/\{\{RECOMMENDATION\}\}/g, report.bottom_line?.recommendation || 'DIG_DEEPER')
    .replace(/\{\{BOTTOM_LINE_REASONING\}\}/g, report.bottom_line?.reasoning || '')
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
