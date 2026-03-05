#!/usr/bin/env node
/**
 * Topic Dossier Enricher v1.0
 * Transforms flat topics into living knowledge dossiers.
 * 
 * Each topic gets: claims, insights, cross-learnings, adjacent topics,
 * influencing topics, research docs, open questions, confidence, momentum.
 * 
 * Usage: node enrich-topics.js
 */

const fs = require('fs');
const path = require('path');

const GRAPH_FILE = path.join(__dirname, 'graph/knowledge-graph.json');
const TAX_FILE = path.join(__dirname, 'taxonomy.json');

function load(f) { return JSON.parse(fs.readFileSync(f, 'utf8')); }

// ═══ MAIN ═══

const G = load(GRAPH_FILE);
const TAX = load(TAX_FILE);
const claims = Object.values(G.claims || {});
const reports = G.reports || {};

// Build keyword index for taxonomy
function buildKeywordMap() {
  const map = {}; // keyword → [topicId]
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

// Map claims to taxonomy topics
function mapClaims(keywordMap) {
  const topicClaims = {}; // topicId → [claim]
  
  claims.forEach(c => {
    const text = ((c.claim || '') + ' ' + (c.topics || []).join(' ') + ' ' + (c.soWhat || '')).toLowerCase();
    const matched = new Set();
    
    Object.entries(keywordMap).forEach(([kw, topicIds]) => {
      if (text.includes(kw)) {
        topicIds.forEach(tid => matched.add(tid));
      }
    });
    
    matched.forEach(tid => {
      if (!topicClaims[tid]) topicClaims[tid] = [];
      topicClaims[tid].push(c);
    });
  });
  
  return topicClaims;
}

// Generate insights from claims (→ Daher... derivations)
function generateInsights(topicClaims) {
  const evidenceClaims = topicClaims.filter(c => c.eija === 'E' && c.confidence >= 80);
  const insights = [];
  
  if (evidenceClaims.length >= 2) {
    // Find patterns across evidence claims
    const hasNumbers = evidenceClaims.filter(c => /\d+%|\$\d|€\d|\d+×/.test(c.claim));
    if (hasNumbers.length >= 2) {
      insights.push({
        type: 'pattern',
        text: '→ Daher: ' + hasNumbers.length + ' quantifizierte Evidenzen stützen dieses Topic. Hohe Datendichte.',
        confidence: Math.round(hasNumbers.reduce((s, c) => s + c.confidence, 0) / hasNumbers.length)
      });
    }
    
    // Check if multiple reports confirm
    const reportIds = new Set(evidenceClaims.map(c => c.reportId));
    if (reportIds.size >= 2) {
      insights.push({
        type: 'cross-validation',
        text: '→ Daher: Bestätigt durch ' + reportIds.size + ' unabhängige Research Reports. Cross-validated.',
        confidence: 85
      });
    }
  }
  
  // Check for high-J content (judgments)
  const judgments = topicClaims.filter(c => c.eija === 'J');
  if (judgments.length > 0 && evidenceClaims.length > 0) {
    insights.push({
      type: 'evidence-vs-judgment',
      text: '→ Einordnung: ' + evidenceClaims.length + ' Evidenzen + ' + judgments.length + ' Bewertungen. Evidenz-Basis solide.',
      confidence: 75
    });
  }
  
  // soWhat aggregation
  const soWhats = topicClaims.filter(c => c.soWhat).map(c => c.soWhat);
  if (soWhats.length >= 2) {
    insights.push({
      type: 'implications',
      text: '→ Implikationen: ' + soWhats.slice(0, 2).join(' '),
      confidence: 70
    });
  }
  
  return insights;
}

// Find cross-learnings between topics
function findCrossLearnings(topicId, topicClaims, allTopicClaims) {
  const crossLearnings = [];
  const myClaimIds = new Set(topicClaims.map(c => c.id));
  
  Object.entries(allTopicClaims).forEach(([otherId, otherClaims]) => {
    if (otherId === topicId) return;
    
    // Find shared claims
    const shared = otherClaims.filter(c => myClaimIds.has(c.id));
    if (shared.length >= 1) {
      crossLearnings.push({
        topicId: otherId,
        sharedClaims: shared.length,
        direction: 'bidirectional',
        text: shared.length + ' geteilte Claims mit ' + otherId.replace(/^t-|^topic-/, '')
      });
    }
  });
  
  return crossLearnings.sort((a, b) => b.sharedClaims - a.sharedClaims).slice(0, 5);
}

// Find adjacent topics (taxonomy neighbors)
function findAdjacentTopics(topicId) {
  const adjacent = [];
  
  function walk(node, parent, siblings) {
    if (node.id === topicId) {
      // Parent is adjacent
      if (parent) adjacent.push({ id: parent.id, label: parent.label, relation: 'parent' });
      // Siblings are adjacent
      siblings.filter(s => s.id !== topicId).forEach(s => {
        adjacent.push({ id: s.id, label: s.label, relation: 'sibling' });
      });
      // Children are adjacent
      (node.children || []).forEach(c => {
        adjacent.push({ id: c.id, label: c.label, relation: 'child' });
      });
    }
    (node.children || []).forEach(c => walk(c, node, node.children || []));
  }
  
  (TAX.domains || []).forEach(d => walk(d, null, TAX.domains));
  return adjacent;
}

// Calculate confidence score
function calculateConfidence(topicClaims) {
  if (topicClaims.length === 0) return { score: 0, reason: 'Keine Claims' };
  
  const avgConf = Math.round(topicClaims.reduce((s, c) => s + (c.confidence || 50), 0) / topicClaims.length);
  const evidenceRatio = topicClaims.filter(c => c.eija === 'E').length / topicClaims.length;
  const verifiedRatio = topicClaims.filter(c => c.status === 'verified').length / topicClaims.length;
  const reportCount = new Set(topicClaims.map(c => c.reportId)).size;
  
  // Weighted score
  const score = Math.round(avgConf * 0.4 + evidenceRatio * 100 * 0.3 + verifiedRatio * 100 * 0.2 + Math.min(reportCount * 20, 100) * 0.1);
  
  let reason = '';
  if (score >= 80) reason = 'Hohe Evidenzdichte, multi-source bestätigt';
  else if (score >= 60) reason = 'Solide Basis, einzelne Lücken';
  else if (score >= 40) reason = 'Erste Datenpunkte, braucht Vertiefung';
  else reason = 'Kaum Daten, Research nötig';
  
  return { score, reason, avgConfidence: avgConf, evidenceRatio: Math.round(evidenceRatio * 100), verifiedRatio: Math.round(verifiedRatio * 100), reportCount };
}

// Identify open questions
function findOpenQuestions(topicClaims, topicId) {
  const questions = [];
  
  // High assumption ratio
  const assumptions = topicClaims.filter(c => c.eija === 'A');
  if (assumptions.length > 0) {
    questions.push('? ' + assumptions.length + ' Annahmen noch nicht verifiziert');
    assumptions.forEach(a => {
      questions.push('  → "' + a.claim.substring(0, 80) + '..."');
    });
  }
  
  // Disputed claims
  const disputed = topicClaims.filter(c => c.status === 'disputed');
  disputed.forEach(d => {
    questions.push('? Umstritten: "' + d.claim.substring(0, 80) + '..."');
  });
  
  // Unverified with low confidence
  const lowConf = topicClaims.filter(c => c.status === 'unverified' && (c.confidence || 50) < 70);
  if (lowConf.length > 0) {
    questions.push('? ' + lowConf.length + ' Claims mit Confidence <70% — Verifikation nötig');
  }
  
  // Few sources
  const allSources = new Set();
  topicClaims.forEach(c => (c.sources || []).forEach(s => allSources.add(s)));
  if (allSources.size < 3 && topicClaims.length > 0) {
    questions.push('? Nur ' + allSources.size + ' Quellen — braucht mehr unabhängige Bestätigung');
  }
  
  return questions;
}

// Get research documents for topic
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
      claimCount: topicClaims.filter(c => c.reportId === rid).length,
      sources: (report.sources || []).slice(0, 5)
    };
  }).filter(Boolean);
}

// ═══ BUILD DOSSIERS ═══

const keywordMap = buildKeywordMap();
const allTopicClaims = mapClaims(keywordMap);

const dossiers = {};
let totalTopics = 0;
let withClaims = 0;
let gaps = 0;

function processTopic(node) {
  totalTopics++;
  const tc = allTopicClaims[node.id] || [];
  
  if (tc.length > 0) withClaims++;
  else gaps++;
  
  dossiers[node.id] = {
    id: node.id,
    label: node.label,
    claimCount: tc.length,
    claims: tc.sort((a, b) => (b.confidence || 0) - (a.confidence || 0)),
    insights: generateInsights(tc),
    crossLearnings: findCrossLearnings(node.id, tc, allTopicClaims),
    adjacentTopics: findAdjacentTopics(node.id),
    openQuestions: findOpenQuestions(tc, node.id),
    researchDocs: getResearchDocs(tc),
    confidence: calculateConfidence(tc),
    isGap: tc.length === 0
  };
  
  (node.children || []).forEach(processTopic);
}

(TAX.domains || []).forEach(d => {
  processTopic(d);
  (d.children || []).forEach(processTopic);
});

// Save
const dossierFile = path.join(__dirname, 'graph/topic-dossiers.json');
fs.writeFileSync(dossierFile, JSON.stringify(dossiers, null, 2));

console.log(`═══ TOPIC DOSSIERS ═══`);
console.log(`Total topics: ${totalTopics}`);
console.log(`With claims: ${withClaims}`);
console.log(`Gaps: ${gaps}`);
console.log(`\nTop topics by claim count:`);
Object.values(dossiers)
  .filter(d => d.claimCount > 0)
  .sort((a, b) => b.claimCount - a.claimCount)
  .slice(0, 10)
  .forEach(d => {
    console.log(`  ${d.confidence.score}% | ${d.claimCount} claims | ${d.insights.length} insights | ${d.crossLearnings.length} cross | ${d.openQuestions.length} open | ${d.label}`);
  });
console.log(`\nTop gaps (need research):`);
Object.values(dossiers)
  .filter(d => d.isGap)
  .slice(0, 10)
  .forEach(d => {
    const adj = d.adjacentTopics.filter(a => !dossiers[a.id]?.isGap).map(a => a.label).slice(0, 2);
    console.log(`  △ ${d.label}${adj.length ? ' (near: ' + adj.join(', ') + ')' : ''}`);
  });
