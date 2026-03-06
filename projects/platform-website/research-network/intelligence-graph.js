#!/usr/bin/env node
/**
 * Ainary Intelligence Graph — Palantir-Style Enhancer
 *
 * Usage:
 *   node intelligence-graph.js
 *   node intelligence-graph.js --report <report-id>
 *   node intelligence-graph.js --contradictions
 *   node intelligence-graph.js --stale
 *   node intelligence-graph.js --decisions <topic-id>
 */

const fs = require('fs');
const path = require('path');

const GRAPH_FILE = path.join(__dirname, 'graph', 'knowledge-graph.json');
const REPORTS_DIR = path.join(__dirname, 'reports');

const ADMIRALTY_SCORES = {
  A1: 95, A2: 90, B1: 85, B2: 80, B3: 70,
  C2: 65, C3: 60
};

const STOPWORDS = new Set([
  'the','and','for','with','from','that','this','these','those','are','was','were','has','have','had',
  'will','shall','should','would','could','into','over','under','above','below','about','across','after',
  'before','between','during','within','without','not','kein','keine','nicht','und','oder','der','die','das',
  'ein','eine','einer','eines','im','in','an','auf','zu','von','mit','für','bei','als','ist','sind'
]);

const POSITIVE_WORDS = new Set([
  'increase','growth','improve','positive','benefit','gain','strong','success','effective','leading','dominant',
  'profitable','efficient','approved','compliant','secure','trusted','stable','boost'
]);

const NEGATIVE_WORDS = new Set([
  'decrease','decline','reduce','negative','risk','penalty','loss','weak','failure','ineffective','ban',
  'illegal','noncompliant','breach','unstable','controversy','lawsuit','fine','cut','drop','fall'
]);

const NEGATION_WORDS = new Set([
  'not','no','never','without','lack','lacking','kein','keine','nicht','ohne','wider','contra','against'
]);

function loadJson(filePath) {
  return JSON.parse(fs.readFileSync(filePath, 'utf8'));
}

function saveJson(filePath, data) {
  fs.writeFileSync(filePath, JSON.stringify(data, null, 2), 'utf8');
}

function loadGraph() {
  if (!fs.existsSync(GRAPH_FILE)) {
    throw new Error('knowledge-graph.json not found');
  }
  return loadJson(GRAPH_FILE);
}

function loadReport(reportId) {
  const reportPath = path.join(REPORTS_DIR, `${reportId}.json`);
  if (!fs.existsSync(reportPath)) return null;
  return loadJson(reportPath);
}

function tokenize(text) {
  return (text || '')
    .toLowerCase()
    .replace(/[^a-z0-9äöüß\s-]/g, ' ')
    .split(/\s+/)
    .map(t => t.trim())
    .filter(t => t.length > 3 && !STOPWORDS.has(t));
}

function sentimentScore(text) {
  const tokens = tokenize(text);
  let score = 0;
  tokens.forEach(t => {
    if (POSITIVE_WORDS.has(t)) score += 1;
    if (NEGATIVE_WORDS.has(t)) score -= 1;
  });
  return score;
}

function hasNegation(text) {
  const tokens = tokenize(text);
  return tokens.some(t => NEGATION_WORDS.has(t));
}

function keywordOverlap(a, b) {
  const aTokens = new Set(tokenize(a));
  const bTokens = new Set(tokenize(b));
  if (!aTokens.size || !bTokens.size) return 0;
  let shared = 0;
  aTokens.forEach(t => { if (bTokens.has(t)) shared += 1; });
  return shared / Math.min(aTokens.size, bTokens.size);
}

function detectContradictions(claims) {
  const list = [];
  const claimArray = claims;

  for (let i = 0; i < claimArray.length; i += 1) {
    for (let j = i + 1; j < claimArray.length; j += 1) {
      const c1 = claimArray[i];
      const c2 = claimArray[j];
      const overlap = keywordOverlap(c1.claim, c2.claim);
      if (overlap < 0.4) continue;

      const s1 = sentimentScore(c1.claim);
      const s2 = sentimentScore(c2.claim);
      const neg1 = hasNegation(c1.claim);
      const neg2 = hasNegation(c2.claim);

      const inversion = (s1 > 0 && s2 < 0) || (s1 < 0 && s2 > 0) || (neg1 !== neg2 && overlap >= 0.5);
      if (!inversion) continue;

      const sharedTopics = (c1.topics || []).filter(t => (c2.topics || []).includes(t));
      list.push({
        id: `contra-${c1.id}-${c2.id}`,
        claim1: c1.id,
        claim2: c2.id,
        topics: sharedTopics,
        detected: new Date().toISOString().slice(0, 10),
        reason: `overlap=${overlap.toFixed(2)} sentiment-inversion`
      });
    }
  }
  return list;
}

function computeBaseQuality(claim, report) {
  const sources = (claim.sources || []).map(sourceId => {
    const reportSource = report && (report.sources || []).find(s => s.id === sourceId);
    if (reportSource) return reportSource;
    if (claim.realSources) return claim.realSources.find(s => s.id === sourceId);
    return null;
  }).filter(Boolean);

  if (!sources.length) {
    const fallback = ADMIRALTY_SCORES[claim.admiralty] || 50;
    return { base: fallback, sourceCount: 0, sources: [] };
  }

  const scores = sources.map(s => ADMIRALTY_SCORES[s.admiralty] || 50);
  const base = scores.reduce((a, b) => a + b, 0) / scores.length;
  return { base, sourceCount: new Set(claim.sources || []).size, sources };
}

function applyRecencyPenalty(dateStr, score) {
  if (!dateStr) return score;
  const date = new Date(dateStr);
  if (Number.isNaN(date.getTime())) return score;
  const now = new Date();
  const months = (now - date) / (1000 * 60 * 60 * 24 * 30);
  if (months > 24) return score * 0.85;
  if (months > 12) return score * 0.95;
  return score;
}

function computeConfidence(claim, report) {
  const quality = computeBaseQuality(claim, report);
  let score = quality.base;

  if (quality.sourceCount >= 3) score *= 1.15;
  else if (quality.sourceCount >= 2) score *= 1.1;

  const dateStr = claim.date || (report && report.date) || null;
  score = applyRecencyPenalty(dateStr, score);

  return {
    base: quality.base,
    score,
    sourceCount: quality.sourceCount,
    sources: quality.sources
  };
}

function buildProvenance(claim) {
  const topicId = (claim.topics || [])[0] || 'unknown-topic';
  const sourceId = (claim.sources || [])[0] || 'unknown-source';
  return {
    source_id: sourceId,
    report_id: claim.reportId || 'unknown-report',
    extraction_date: claim.date || new Date().toISOString().slice(0, 10),
    verification_status: claim.status || 'unverified',
    graph_path: `${topicId} -> ${claim.id} -> ${sourceId}`
  };
}

function detectStaleReports(graph) {
  const staleReports = [];
  const claims = Object.values(graph.claims || {});

  Object.keys(graph.reports || {}).forEach(reportId => {
    const report = loadReport(reportId);
    const reportClaims = claims.filter(c => c.reportId === reportId);
    const reportTopics = new Set();

    if (report && Array.isArray(report.claims)) {
      report.claims.forEach(c => (c.topics || []).forEach(t => reportTopics.add(t)));
    } else {
      reportClaims.forEach(c => (c.topics || []).forEach(t => reportTopics.add(t)));
    }

    if (!reportTopics.size) return;

    const newClaims = claims.filter(c => c.reportId !== reportId && (c.topics || []).some(t => reportTopics.has(t)));
    if (newClaims.length > 0) {
      staleReports.push({
        report_id: reportId,
        newClaimsAvailable: newClaims.length,
        suggestedUpdate: true
      });
    }
  });

  return staleReports;
}

function deriveRisk(text) {
  const lower = (text || '').toLowerCase();
  if (lower.includes('regulat') || lower.includes('compliance') || lower.includes('law')) return 'regulatory penalty';
  if (lower.includes('reputation') || lower.includes('trust')) return 'reputational';
  if (lower.includes('security') || lower.includes('breach')) return 'security';
  if (lower.includes('cost') || lower.includes('revenue') || lower.includes('profit')) return 'financial';
  return 'execution';
}

function deriveAction(claims) {
  const withSoWhat = claims.find(c => c.soWhat && c.soWhat.length > 8);
  if (withSoWhat) return withSoWhat.soWhat;
  const top = claims[0];
  return `Act on: ${top.claim}`;
}

function buildDecisionBlock(topicId, topicLabel, claims) {
  if (claims.length <= 5) return null;
  const ranked = claims.slice().sort((a, b) => (b.confidence || 0) - (a.confidence || 0));
  const decisions = [];

  for (let i = 0; i < Math.min(2, ranked.length); i += 1) {
    const supporting = ranked.slice(i * 3, i * 3 + 3).filter(Boolean);
    if (!supporting.length) continue;

    const confidence = Math.round(supporting.reduce((sum, c) => sum + (c.confidence || 0), 0) / supporting.length);
    decisions.push({
      action: deriveAction(supporting),
      confidence,
      supportingClaims: supporting.length,
      risk: deriveRisk(supporting.map(c => c.claim).join(' '))
    });
  }

  return {
    topic: topicId,
    label: topicLabel || topicId,
    decisions
  };
}

function updateGraph(graph) {
  const claims = Object.values(graph.claims || {});
  const reportCache = new Map();

  const loadReportCached = (reportId) => {
    if (reportCache.has(reportId)) return reportCache.get(reportId);
    const report = loadReport(reportId);
    reportCache.set(reportId, report);
    return report;
  };

  const confidenceMap = new Map();
  claims.forEach(claim => {
    const report = loadReportCached(claim.reportId);
    const computed = computeConfidence(claim, report);
    confidenceMap.set(claim.id, computed);
  });

  const contradictions = detectContradictions(claims);
  const contradictionMap = new Map();
  contradictions.forEach(c => {
    if (!contradictionMap.has(c.claim1)) contradictionMap.set(c.claim1, []);
    if (!contradictionMap.has(c.claim2)) contradictionMap.set(c.claim2, []);
    contradictionMap.get(c.claim1).push(c.claim2);
    contradictionMap.get(c.claim2).push(c.claim1);
  });

  contradictions.forEach(c => {
    const c1 = confidenceMap.get(c.claim1);
    const c2 = confidenceMap.get(c.claim2);
    if (!c1 || !c2) return;
    if (c1.score === c2.score) {
      c1.score *= 0.8;
      c2.score *= 0.8;
      return;
    }
    if (c1.score < c2.score) c1.score *= 0.8;
    else c2.score *= 0.8;
  });

  claims.forEach(claim => {
    const computed = confidenceMap.get(claim.id);
    const contradictionsForClaim = contradictionMap.get(claim.id) || [];
    claim.confidence = Math.round(computed.score);
    claim.computedConfidence = {
      base: Math.round(computed.base),
      score: Math.round(computed.score),
      sourceCount: computed.sourceCount
    };
    claim.contradicts = contradictionsForClaim;
    claim.provenance = buildProvenance(claim);
  });

  graph.contradictions = contradictions;
  graph.staleReports = detectStaleReports(graph);

  const decisionBlocks = [];
  Object.keys(graph.topics || {}).forEach(topicId => {
    const topic = graph.topics[topicId];
    const topicClaims = (topic.claimIds || []).map(id => graph.claims[id]).filter(Boolean);
    const block = buildDecisionBlock(topicId, topic.label, topicClaims);
    if (block) decisionBlocks.push(block);
  });
  graph.decisionSupport = decisionBlocks;

  return { contradictions, decisionBlocks };
}

function analyzeReport(reportId) {
  const report = loadReport(reportId);
  if (!report) {
    console.error(`Report not found: ${reportId}`);
    process.exit(1);
  }
  const claims = (report.claims || []).map((c, i) => ({
    id: `${reportId}-c${String(i + 1).padStart(3, '0')}`,
    reportId,
    claim: c.claim || c.text || c,
    topics: c.topics || [],
    sources: c.sources || [],
    admiralty: c.admiralty || report.admiralty || 'B2',
    status: c.status || 'unverified',
    date: report.date,
    soWhat: c.soWhat || null
  }));

  const contradictions = detectContradictions(claims);
  console.log(JSON.stringify({ reportId, claimCount: claims.length, contradictions }, null, 2));
}

const args = process.argv.slice(2);
const command = args[0];

if (command === '--report') {
  analyzeReport(args[1]);
  process.exit(0);
}

if (command === '--contradictions') {
  const graph = loadGraph();
  const { contradictions } = updateGraph(graph);
  saveJson(GRAPH_FILE, graph);
  console.log(JSON.stringify(contradictions, null, 2));
  process.exit(0);
}

if (command === '--stale') {
  const graph = loadGraph();
  updateGraph(graph);
  saveJson(GRAPH_FILE, graph);
  console.log(JSON.stringify(graph.staleReports || [], null, 2));
  process.exit(0);
}

if (command === '--decisions') {
  const graph = loadGraph();
  updateGraph(graph);
  saveJson(GRAPH_FILE, graph);
  const topicId = args[1];
  const block = (graph.decisionSupport || []).find(b => b.topic === topicId);
  console.log(JSON.stringify(block || { topic: topicId, decisions: [] }, null, 2));
  process.exit(0);
}

const graph = loadGraph();
const { contradictions, decisionBlocks } = updateGraph(graph);
saveJson(GRAPH_FILE, graph);
console.log(`Updated graph: ${Object.keys(graph.claims || {}).length} claims`);
console.log(`Contradictions found: ${contradictions.length}`);
console.log(`Decision blocks: ${decisionBlocks.length}`);
