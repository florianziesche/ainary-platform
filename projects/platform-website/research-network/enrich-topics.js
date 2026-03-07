#!/usr/bin/env node
/**
 * Topic Dossier Enricher v2.0
 * Each topic = living knowledge dossier with:
 * - Management Summary (BLUF)
 * - Playbook (actionable implications)
 * - Claims categorized by EIJA + sorted by importance
 * - Cross-Learnings (shared claims between topics)
 * - Open Questions / Gaps
 * - Confidence + Momentum
 */

const fs = require('fs');
const path = require('path');

const GRAPH_FILE = path.join(__dirname, 'graph/knowledge-graph.json');
const TAX_FILE = path.join(__dirname, 'taxonomy.json');

function load(f) { return JSON.parse(fs.readFileSync(f, 'utf8')); }

const G = load(GRAPH_FILE);
const TAX = load(TAX_FILE);
const claims = Object.values(G.claims || {});
const reports = G.reports || {};

// ═══ KEYWORD INDEX ═══
function buildKeywordMap() {
  const map = {};
  function walk(node) {
    const id = node.id;
    const keywords = (node.label || '').toLowerCase().split(/[\s\/&()+,]+/).filter(w => w.length > 2);
    id.replace(/^[td]-/, '').split('-').forEach(w => { if (w.length > 2) keywords.push(w); });
    keywords.forEach(kw => {
      if (!map[kw]) map[kw] = new Set();
      map[kw].add(id);
    });
    (node.children || []).forEach(walk);
  }
  (TAX.domains || []).forEach(walk);
  return map;
}

// ═══ MAP CLAIMS TO TOPICS ═══
function mapClaims(keywordMap) {
  const topicClaims = {};
  claims.forEach(c => {
    const text = ((c.claim || '') + ' ' + (c.topics || []).join(' ') + ' ' + (c.soWhat || '')).toLowerCase();
    const matched = new Set();
    Object.entries(keywordMap).forEach(([kw, topicIds]) => {
      if (text.includes(kw)) topicIds.forEach(tid => matched.add(tid));
    });
    matched.forEach(tid => {
      if (!topicClaims[tid]) topicClaims[tid] = [];
      topicClaims[tid].push(c);
    });
  });
  return topicClaims;
}

// ═══ MANAGEMENT SUMMARY ═══
// BLUF from top 3 highest-importance claims
function generateSummary(topicClaims, topicId) {
  if (topicClaims.length === 0) return null;
  
  // Importance = trust × relevance
  const ranked = topicClaims
    .map(c => ({
      claim: c,
      importance: ((c.trustScore || {}).score || 50) * ((c.relevance || {})[topicId] || 5) / 100
    }))
    .sort((a, b) => b.importance - a.importance);
  
  const top3 = ranked.slice(0, 3);
  const avgTrust = Math.round(topicClaims.reduce((s, c) => s + ((c.trustScore || {}).score || 50), 0) / topicClaims.length);
  const sourceCount = new Set();
  topicClaims.forEach(c => (c.realSources || []).forEach(s => sourceCount.add(s.label)));
  const reportCount = new Set(topicClaims.map(c => c.reportId)).size;
  
  return {
    topClaims: top3.map(t => t.claim.claim),
    avgTrust,
    uniqueSources: sourceCount.size,
    reportCount,
    claimCount: topicClaims.length,
    evidenceCount: topicClaims.filter(c => c.eija === 'E').length,
    interpretationCount: topicClaims.filter(c => c.eija === 'I').length,
    judgmentCount: topicClaims.filter(c => c.eija === 'J').length,
    assumptionCount: topicClaims.filter(c => c.eija === 'A').length
  };
}

// ═══ PLAYBOOK ═══
// Actionable implications from soWhats + judgments
function generatePlaybook(topicClaims) {
  const actions = [];
  
  // From soWhats (strongest implications)
  const withSoWhat = topicClaims
    .filter(c => c.soWhat && ((c.trustScore || {}).score || 0) >= 70)
    .sort((a, b) => ((b.trustScore || {}).score || 0) - ((a.trustScore || {}).score || 0));
  
  withSoWhat.slice(0, 5).forEach(c => {
    actions.push({
      type: 'implication',
      text: c.soWhat,
      trust: (c.trustScore || {}).score || 0,
      sourceCount: (c.trustScore || {}).sourceCount || 0,
      from: c.claim.substring(0, 60),
      claimId: c.id || null,
      influencesTopics: (c.topics || []).slice()
    });
  });
  
  // From judgments (expert assessments)
  const judgments = topicClaims.filter(c => c.eija === 'J');
  judgments.slice(0, 3).forEach(c => {
    actions.push({
      type: 'judgment',
      text: c.claim,
      trust: (c.trustScore || {}).score || 0,
      sourceCount: (c.trustScore || {}).sourceCount || 0,
      claimId: c.id || null,
      influencesTopics: (c.topics || []).slice()
    });
  });
  
  return actions;
}

// ═══ CATEGORIZED CLAIMS ═══
function categorizeClaims(topicClaims, topicId) {
  const categories = {
    evidence: [],
    interpretation: [],
    judgment: [],
    assumption: []
  };
  
  const sorted = topicClaims
    .map(c => ({
      ...c,
      importance: ((c.trustScore || {}).score || 50) * ((c.relevance || {})[topicId] || 5) / 100
    }))
    .sort((a, b) => b.importance - a.importance);
  
  sorted.forEach(c => {
    const cat = { E: 'evidence', I: 'interpretation', J: 'judgment', A: 'assumption' }[c.eija] || 'evidence';
    categories[cat].push(c);
  });
  
  return categories;
}

// ═══ CROSS-LEARNINGS ═══
function findCrossLearnings(topicId, topicClaims, allTopicClaims) {
  const crossLearnings = [];
  const myClaimIds = new Set(topicClaims.map(c => c.id));
  
  Object.entries(allTopicClaims).forEach(([otherId, otherClaims]) => {
    if (otherId === topicId) return;
    const shared = otherClaims.filter(c => myClaimIds.has(c.id));
    if (shared.length >= 1) {
      // Determine direction
      const myAvgTrust = topicClaims.reduce((s, c) => s + ((c.trustScore || {}).score || 50), 0) / topicClaims.length;
      const otherAvgTrust = otherClaims.reduce((s, c) => s + ((c.trustScore || {}).score || 50), 0) / otherClaims.length;
      
      crossLearnings.push({
        topicId: otherId,
        sharedClaims: shared.length,
        sharedClaimTexts: shared.slice(0, 2).map(c => c.claim.substring(0, 80)),
        direction: myAvgTrust > otherAvgTrust ? 'this→that' : otherAvgTrust > myAvgTrust ? 'that→this' : 'bidirectional',
        strengthDelta: Math.round(Math.abs(myAvgTrust - otherAvgTrust))
      });
    }
  });
  
  return crossLearnings.sort((a, b) => b.sharedClaims - a.sharedClaims).slice(0, 8);
}

// ═══ ADJACENT TOPICS ═══
function findAdjacentTopics(topicId) {
  const adjacent = [];
  function walk(node, parent, siblings) {
    if (node.id === topicId) {
      if (parent) adjacent.push({ id: parent.id, label: parent.label, relation: 'parent' });
      siblings.filter(s => s.id !== topicId).forEach(s => {
        adjacent.push({ id: s.id, label: s.label, relation: 'sibling' });
      });
      (node.children || []).forEach(c => {
        adjacent.push({ id: c.id, label: c.label, relation: 'child' });
      });
    }
    (node.children || []).forEach(c => walk(c, node, node.children || []));
  }
  (TAX.domains || []).forEach(d => walk(d, null, TAX.domains));
  return adjacent;
}

// ═══ OPEN QUESTIONS ═══
function findOpenQuestions(topicClaims) {
  const questions = [];
  
  // Assumptions
  const assumptions = topicClaims.filter(c => c.eija === 'A');
  assumptions.forEach(a => {
    questions.push({ type: 'assumption', text: a.claim, trust: (a.trustScore || {}).score || 0 });
  });
  
  // Disputed
  topicClaims.filter(c => c.status === 'disputed').forEach(d => {
    questions.push({ type: 'disputed', text: d.claim, trust: (d.trustScore || {}).score || 0 });
  });
  
  // Low confidence (<70)
  const lowConf = topicClaims.filter(c => ((c.trustScore || {}).score || 50) < 70);
  if (lowConf.length > 0) {
    questions.push({ type: 'weak', text: lowConf.length + ' Claims mit Trust <70% — Verifikation nötig' });
  }
  
  // Few sources
  const allSources = new Set();
  topicClaims.forEach(c => (c.realSources || []).forEach(s => allSources.add(s.label)));
  if (allSources.size < 3 && topicClaims.length > 0) {
    questions.push({ type: 'source-gap', text: 'Nur ' + allSources.size + ' unabhängige Quellen' });
  }
  
  return questions;
}

// ═══ CONFIDENCE ═══
function calculateConfidence(topicClaims) {
  if (topicClaims.length === 0) return { score: 0, reason: 'Keine Claims', details: {} };
  
  const avgTrust = Math.round(topicClaims.reduce((s, c) => s + ((c.trustScore || {}).score || 50), 0) / topicClaims.length);
  const evidenceRatio = Math.round(topicClaims.filter(c => c.eija === 'E').length / topicClaims.length * 100);
  const verifiedRatio = Math.round(topicClaims.filter(c => c.status === 'verified').length / topicClaims.length * 100);
  const reportCount = new Set(topicClaims.map(c => c.reportId)).size;
  const multiSource = topicClaims.filter(c => ((c.trustScore || {}).sourceCount || 0) > 1).length;
  
  const score = Math.round(avgTrust * 0.4 + evidenceRatio * 0.3 + verifiedRatio * 0.2 + Math.min(reportCount * 20, 100) * 0.1);
  
  let reason;
  if (score >= 80) reason = 'Hohe Evidenzdichte, multi-source bestätigt';
  else if (score >= 60) reason = 'Solide Basis, einzelne Lücken';
  else if (score >= 40) reason = 'Erste Datenpunkte, braucht Vertiefung';
  else reason = 'Kaum Daten, Research nötig';
  
  return { score, reason, details: { avgTrust, evidenceRatio, verifiedRatio, reportCount, multiSource } };
}

// ═══ RESEARCH DOCS ═══
function getResearchDocs(topicClaims) {
  const reportIds = new Set(topicClaims.map(c => c.reportId));
  return Array.from(reportIds).map(rid => {
    const report = reports[rid];
    if (!report) return null;
    return {
      id: rid,
      title: report.title,
      date: report.date,
      admiralty: report.admiralty,
      claimCount: topicClaims.filter(c => c.reportId === rid).length
    };
  }).filter(Boolean);
}

// ═══ RESEARCH SUGGESTIONS (for gap topics + report builder) ═══
function generateSuggestions(topicId, topicClaims, allTopicClaims, adjacentTopics) {
  // Collect sources from adjacent topics that have data
  const suggestedSources = [];
  const seenSourceLabels = new Set();
  
  adjacentTopics.forEach(adj => {
    const adjClaims = allTopicClaims[adj.id] || [];
    adjClaims.forEach(c => {
      (c.realSources || []).forEach(src => {
        if (src.label && !seenSourceLabels.has(src.label)) {
          seenSourceLabels.add(src.label);
          suggestedSources.push({
            label: src.label,
            url: src.url || '',
            admiralty: src.admiralty || 'B2',
            reason: 'Used in adjacent topic: ' + (adj.label || adj.id)
          });
        }
      });
    });
  });
  
  // Domain-specific standard sources based on topic keywords
  const topicText = topicId.toLowerCase();
  const domainSources = [];
  
  if (topicText.match(/agent|memory|tool|reflection|architecture/)) {
    domainSources.push(
      { label: 'Anthropic Research Blog', url: 'https://www.anthropic.com/research', admiralty: 'A1', reason: 'Primary source for agent architecture' },
      { label: 'OpenAI Cookbook', url: 'https://cookbook.openai.com/', admiralty: 'A2', reason: 'Implementation patterns for agents' },
      { label: 'LangChain Docs', url: 'https://docs.langchain.com/', admiralty: 'B2', reason: 'Agent framework documentation' }
    );
  }
  if (topicText.match(/ontology|knowledge|graph|entity|semantic/)) {
    domainSources.push(
      { label: 'Palantir Ontology Blog', url: 'https://blog.palantir.com/', admiralty: 'A2', reason: 'Ontology design patterns' },
      { label: 'W3C Knowledge Graphs', url: 'https://www.w3.org/standards/', admiralty: 'A1', reason: 'Semantic web standards' }
    );
  }
  if (topicText.match(/llm|prompt|reasoning|training|embedding/)) {
    domainSources.push(
      { label: 'arXiv cs.CL', url: 'https://arxiv.org/list/cs.CL/recent', admiralty: 'A2', reason: 'Latest research papers' },
      { label: 'Simon Willison\'s Weblog', url: 'https://simonwillison.net/', admiralty: 'B2', reason: 'LLM practitioner insights' }
    );
  }
  if (topicText.match(/governance|safety|alignment|bias|regulation|transparen/)) {
    domainSources.push(
      { label: 'EU AI Act Full Text', url: 'https://eur-lex.europa.eu/eli/reg/2024/1689/oj', admiralty: 'A1', reason: 'Legal framework' },
      { label: 'NIST AI Risk Management', url: 'https://airc.nist.gov/AI_RMF_Interactivity', admiralty: 'A1', reason: 'US risk framework' },
      { label: 'Anthropic Safety Research', url: 'https://www.anthropic.com/research#safety', admiralty: 'A1', reason: 'Alignment research' }
    );
  }
  if (topicText.match(/market|consulting|pricing|distribution|gtm|sales/)) {
    domainSources.push(
      { label: 'Stratechery', url: 'https://stratechery.com/', admiralty: 'B2', reason: 'Tech strategy analysis' },
      { label: 'a16z Blog', url: 'https://a16z.com/blog/', admiralty: 'B2', reason: 'VC/market perspective' }
    );
  }
  if (topicText.match(/palantir|foundry|gotham|fde|oag/)) {
    domainSources.push(
      { label: 'Palantir SEC 10-K', url: 'https://investors.palantir.com/sec-filings', admiralty: 'A1', reason: 'Financial data' },
      { label: 'Palantir Docs', url: 'https://www.palantir.com/docs/foundry/', admiralty: 'A2', reason: 'Technical documentation' }
    );
  }
  
  // Deduplicate domain sources against already found
  domainSources.forEach(ds => {
    if (!seenSourceLabels.has(ds.label)) {
      seenSourceLabels.add(ds.label);
      suggestedSources.push(ds);
    }
  });
  
  // Suggested claims from adjacent topics (claims that partially relate)
  const suggestedClaims = [];
  const seenClaims = new Set();
  
  adjacentTopics.forEach(adj => {
    const adjClaims = allTopicClaims[adj.id] || [];
    adjClaims.forEach(c => {
      if (seenClaims.has(c.id)) return;
      // Check if claim text contains topic keywords
      const topicKws = topicId.replace(/^t-|^topic-/, '').split('-').filter(w => w.length > 2);
      const claimText = (c.claim || '').toLowerCase();
      const hits = topicKws.filter(kw => claimText.includes(kw)).length;
      if (hits > 0) {
        seenClaims.add(c.id);
        suggestedClaims.push({
          claim: c.claim,
          eija: c.eija || 'E',
          admiralty: c.admiralty || 'B2',
          soWhat: c.soWhat || '',
          reason: 'Related claim from: ' + (adj.label || adj.id),
          trust: (c.trustScore || {}).score || 50
        });
      }
    });
  });
  
  // Research questions derived from the topic + gaps
  const researchQuestions = [];
  const topicLabel = topicId.replace(/^t-|^topic-/, '').replace(/-/g, ' ');
  researchQuestions.push('What are the current best practices for ' + topicLabel + '?');
  researchQuestions.push('What are the main trade-offs and limitations of ' + topicLabel + '?');
  researchQuestions.push('How does ' + topicLabel + ' compare across different implementations?');
  
  return {
    sources: suggestedSources.slice(0, 10),
    claims: suggestedClaims.sort((a, b) => b.trust - a.trust).slice(0, 5),
    researchQuestions
  };
}

// ═══ BUILD ALL DOSSIERS ═══
const keywordMap = buildKeywordMap();
const allTopicClaims = mapClaims(keywordMap);
const dossiers = {};
let stats = { total: 0, withClaims: 0, gaps: 0 };

function processTopic(node) {
  stats.total++;
  const tc = allTopicClaims[node.id] || [];
  if (tc.length > 0) stats.withClaims++; else stats.gaps++;
  
  const adjTopics = findAdjacentTopics(node.id);
  
  dossiers[node.id] = {
    id: node.id,
    label: node.label,
    claimCount: tc.length,
    isGap: tc.length === 0,
    summary: generateSummary(tc, node.id),
    playbook: generatePlaybook(tc),
    categorizedClaims: categorizeClaims(tc, node.id),
    crossLearnings: findCrossLearnings(node.id, tc, allTopicClaims),
    adjacentTopics: adjTopics,
    openQuestions: findOpenQuestions(tc),
    researchDocs: getResearchDocs(tc),
    confidence: calculateConfidence(tc),
    suggestions: generateSuggestions(node.id, tc, allTopicClaims, adjTopics)
  };
  
  (node.children || []).forEach(processTopic);
}

(TAX.domains || []).forEach(d => {
  processTopic(d);
  (d.children || []).forEach(processTopic);
});

// Save
const outFile = path.join(__dirname, 'graph/topic-dossiers.json');
fs.writeFileSync(outFile, JSON.stringify(dossiers, null, 2));

// Report
console.log(`═══ TOPIC DOSSIERS v2.0 ═══`);
console.log(`Total: ${stats.total} | With data: ${stats.withClaims} | Gaps: ${stats.gaps}`);
console.log(`\nTop by confidence:`);
Object.values(dossiers)
  .filter(d => d.claimCount > 0)
  .sort((a, b) => b.confidence.score - a.confidence.score)
  .slice(0, 8)
  .forEach(d => {
    const cats = d.categorizedClaims;
    const e = cats.evidence.length, i = cats.interpretation.length, j = cats.judgment.length, a = cats.assumption.length;
    console.log(`  ${d.confidence.score}% | ${d.claimCount}c (E${e} I${i} J${j} A${a}) | ${d.playbook.length} playbook | ${d.crossLearnings.length} cross | ${d.label}`);
  });
console.log(`\nTop gaps:`);
Object.values(dossiers).filter(d => d.isGap).slice(0, 5).forEach(d => {
  console.log(`  △ ${d.label}`);
});
