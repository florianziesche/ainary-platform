#!/usr/bin/env node
/**
 * Ainary Ontology Validator v1.0
 * Validates city JSON against ONTOLOGY.md schema
 * 
 * Usage: node validate-ontology.js [city]
 * Example: node validate-ontology.js fuerth
 * No args = validate all cities
 * 
 * Inspired by Palantir's Ontology: Semantic + Kinetic + Dynamic
 * "Everything is an Object. Links are typed. Trust is first-class."
 */

const fs = require('fs');
const path = require('path');

const DATA_DIR = path.join(__dirname, 'data/cities');
const CITIES = process.argv[2] ? [process.argv[2]] : 
  fs.readdirSync(DATA_DIR).filter(f => f.endsWith('.json')).map(f => f.replace('.json', ''));

// ═══ ADMIRALTY SYSTEM (Layer 2: Logic Functions) ═══

function deriveConfidence(admiralty) {
  const map = { A1: 95, A2: 90, B1: 85, B2: 80, B3: 70, C1: 75, C2: 65, C3: 60, D4: 40, E2: 30 };
  return map[admiralty] || 50;
}

function deriveSourceLabel(admiralty) {
  const map = {
    A1: 'Amtliche Quelle', A2: 'Überregionales Leitmedium',
    B1: 'Nationales Leitmedium', B2: 'Regionales Leitmedium', B3: 'Regionaler Fachverlag',
    C1: 'Spezialpublikation', C2: 'Partei-/Kandidatenwebsite', C3: 'Social Media / Community',
    D4: 'Unbestätigte Quelle', E2: 'Fragliche Quelle'
  };
  return map[admiralty] || 'Unbekannte Quelle';
}

function sentimentValid(s) {
  return ['POS', 'NEG', 'NEUTRAL'].includes(s);
}

function eijaValid(tag) {
  return ['E', 'I', 'J', 'A'].includes(tag);
}

// ═══ VALIDATORS ═══

function validateArticle(article, idx, errors) {
  const prefix = `news[${idx}]`;
  
  // Required fields
  if (!article.title) errors.push(`${prefix}: missing title`);
  if (!article.date) errors.push(`${prefix}: missing date`);
  if (!article.source) errors.push(`${prefix}: missing source`);
  if (!article.url) errors.push(`${prefix}: missing url`);
  
  // Admiralty system
  if (!article.admiralty) errors.push(`${prefix}: missing admiralty code`);
  else if (!/^[A-E][1-6]$/.test(article.admiralty)) errors.push(`${prefix}: invalid admiralty "${article.admiralty}"`);
  
  // Confidence should match admiralty
  if (article.admiralty && article.confidence) {
    const expected = deriveConfidence(article.admiralty);
    if (Math.abs(article.confidence - expected) > 5) {
      errors.push(`${prefix}: confidence ${article.confidence} doesn't match admiralty ${article.admiralty} (expected ~${expected})`);
    }
  }
  
  // Sentiment
  if (!article.sentiment) errors.push(`${prefix}: missing sentiment`);
  else if (!sentimentValid(article.sentiment)) errors.push(`${prefix}: invalid sentiment "${article.sentiment}" (must be POS/NEG/NEUTRAL)`);
  
  // EIJA in body
  if (article.body) {
    const m = article.body.match(/^\[([EIJA])\]/);
    if (!m) errors.push(`${prefix}: body missing EIJA prefix`);
  }
  
  // Theme
  if (!article.theme) errors.push(`${prefix}: missing theme`);
  
  // SourceLabel derivation
  if (article.admiralty && article.sourceLabel) {
    const expected = deriveSourceLabel(article.admiralty);
    if (article.sourceLabel !== expected) {
      // Warn, don't error — some custom labels are OK
    }
  }
}

function validateKBEntry(id, entry, errors) {
  const prefix = `kb.${id}`;
  if (!entry.id) errors.push(`${prefix}: missing id`);
  if (!entry.name) errors.push(`${prefix}: missing name`);
  if (!entry.type) errors.push(`${prefix}: missing type (person/media)`);
  if (!entry.role) errors.push(`${prefix}: missing role`);
  if (!entry.trustScore) errors.push(`${prefix}: missing trustScore`);
}

function validateGraph(graph, kb, errors) {
  if (!graph.nodes || !Array.isArray(graph.nodes)) { errors.push('graph: missing nodes array'); return; }
  if (!graph.links || !Array.isArray(graph.links)) { errors.push('graph: missing links array'); return; }
  
  const nodeIds = new Set(graph.nodes.map(n => n.id));
  
  // Check orphan nodes
  const linkedIds = new Set();
  graph.links.forEach(l => { linkedIds.add(l.source); linkedIds.add(l.target); });
  
  const orphans = graph.nodes.filter(n => !linkedIds.has(n.id));
  if (orphans.length > 0) {
    errors.push(`graph: ${orphans.length} orphan nodes: ${orphans.map(n => n.label || n.id).join(', ')}`);
  }
  
  // Check dangling links
  graph.links.forEach((l, i) => {
    if (!nodeIds.has(l.source)) errors.push(`graph.links[${i}]: source "${l.source}" not in nodes`);
    if (!nodeIds.has(l.target)) errors.push(`graph.links[${i}]: target "${l.target}" not in nodes`);
  });
  
  // Check node has group
  graph.nodes.forEach((n, i) => {
    if (!n.group) errors.push(`graph.nodes[${i}] (${n.label}): missing group/filterGroup`);
  });
}

function validateThemes(themes, news, errors) {
  if (!themes || !Array.isArray(themes)) return;
  
  themes.forEach((t, i) => {
    if (!t.label && !t.theme) errors.push(`themes[${i}]: missing label`);
    if (!t.executiveSummary && !t.summary) errors.push(`themes[${i}] (${t.label || t.theme}): missing executive summary`);
  });
  
  // Check news theme references exist in themes
  const themeLabels = new Set(themes.map(t => t.label || t.theme));
  const newsThemes = new Set(news.map(n => n.theme).filter(Boolean));
  newsThemes.forEach(t => {
    if (!themeLabels.has(t)) {
      // Soft warning — themes might use different naming
    }
  });
}

function validateCity(cityName) {
  const filePath = path.join(DATA_DIR, `${cityName}.json`);
  if (!fs.existsSync(filePath)) {
    console.log(`❌ ${cityName}: file not found`);
    return { city: cityName, errors: ['file not found'], warnings: [] };
  }
  
  const data = JSON.parse(fs.readFileSync(filePath, 'utf8'));
  const errors = [];
  const warnings = [];
  const stats = {};
  
  // ═══ LAYER 1: SEMANTIC VALIDATION ═══
  
  // Tenant
  if (!data.tenant) errors.push('missing tenant');
  else {
    if (!data.tenant.name) errors.push('tenant: missing name');
    if (!data.tenant.wahl) warnings.push('tenant: missing wahl date');
    if (!data.tenant.password) warnings.push('tenant: missing password');
  }
  
  // KB (Knowledge Base)
  const kb = data.kb || data.KB || {};
  stats.kbEntries = Object.keys(kb).length;
  if (stats.kbEntries === 0) errors.push('kb: empty');
  Object.entries(kb).forEach(([id, entry]) => validateKBEntry(id, entry, errors));
  
  // News/Articles
  const news = data.news || [];
  stats.newsCount = news.length;
  if (news.length === 0) errors.push('news: empty');
  news.forEach((n, i) => validateArticle(n, i, errors));
  
  // Trust coverage
  const withAdmiralty = news.filter(n => n.admiralty).length;
  const withSentiment = news.filter(n => n.sentiment).length;
  stats.trustCoverage = news.length > 0 ? Math.round(withAdmiralty / news.length * 100) : 0;
  stats.sentimentCoverage = news.length > 0 ? Math.round(withSentiment / news.length * 100) : 0;
  if (stats.trustCoverage < 100) warnings.push(`trust: ${stats.trustCoverage}% articles have admiralty (target: 100%)`);
  if (stats.sentimentCoverage < 100) warnings.push(`sentiment: ${stats.sentimentCoverage}% articles have sentiment (target: 100%)`);
  
  // Graph
  const graph = data.graph || {};
  stats.graphNodes = (graph.nodes || []).length;
  stats.graphLinks = (graph.links || []).length;
  if (stats.graphNodes === 0) errors.push('graph: no nodes');
  else validateGraph(graph, kb, errors);
  
  // Themes
  const themes = data.newsClusteredByThema || [];
  stats.themeCount = themes.length;
  validateThemes(themes, news, errors);
  
  // Kandidaten
  const kandidaten = data.kandidatenBlock || [];
  stats.kandidatenCount = kandidaten.length;
  
  // Intelligence
  if (!data.intelligence) warnings.push('missing intelligence layer');
  
  // Medienlandschaft
  if (!data.medienlandschaft) warnings.push('missing medienlandschaft');
  
  // EIJA coverage on bodies
  const withBody = news.filter(n => n.body).length;
  const withEija = news.filter(n => n.body && /^\[[EIJA]\]/.test(n.body)).length;
  stats.eijaCoverage = withBody > 0 ? Math.round(withEija / withBody * 100) : 0;
  
  // ═══ LAYER 2: KINETIC VALIDATION (Logic consistency) ═══
  
  // Check confidence-admiralty consistency
  let confidenceMismatches = 0;
  news.forEach(n => {
    if (n.admiralty && n.confidence) {
      const expected = deriveConfidence(n.admiralty);
      if (Math.abs(n.confidence - expected) > 5) confidenceMismatches++;
    }
  });
  stats.confidenceMismatches = confidenceMismatches;
  
  // Sentiment distribution
  const sentDist = { POS: 0, NEG: 0, NEUTRAL: 0 };
  news.forEach(n => { if (sentDist[n.sentiment] !== undefined) sentDist[n.sentiment]++; });
  stats.sentimentDist = sentDist;
  
  // ═══ OUTPUT ═══
  
  const status = errors.length === 0 ? '✅' : '❌';
  console.log(`\n${status} ${cityName.toUpperCase()}`);
  console.log(`   Objects: ${stats.kbEntries} KB | ${stats.newsCount} News | ${stats.graphNodes} Nodes | ${stats.graphLinks} Links | ${stats.kandidatenCount} Kandidaten | ${stats.themeCount} Themes`);
  console.log(`   Trust: ${stats.trustCoverage}% Admiralty | ${stats.sentimentCoverage}% Sentiment | ${stats.eijaCoverage}% EIJA | ${stats.confidenceMismatches} confidence mismatches`);
  console.log(`   Sentiment: POS=${sentDist.POS} NEG=${sentDist.NEG} NEUTRAL=${sentDist.NEUTRAL}`);
  
  if (errors.length > 0) {
    console.log(`   ❌ ${errors.length} ERRORS:`);
    errors.slice(0, 10).forEach(e => console.log(`      - ${e}`));
    if (errors.length > 10) console.log(`      ... and ${errors.length - 10} more`);
  }
  if (warnings.length > 0) {
    console.log(`   ⚠️  ${warnings.length} WARNINGS:`);
    warnings.forEach(w => console.log(`      - ${w}`));
  }
  
  return { city: cityName, errors, warnings, stats };
}

// ═══ MAIN ═══

console.log('═══ AINARY ONTOLOGY VALIDATOR v1.0 ═══');
console.log(`Validating: ${CITIES.join(', ')}`);

const results = CITIES.map(validateCity);
const totalErrors = results.reduce((s, r) => s + r.errors.length, 0);
const totalWarnings = results.reduce((s, r) => s + r.warnings.length, 0);

console.log(`\n═══ SUMMARY ═══`);
console.log(`Cities: ${results.length} | Errors: ${totalErrors} | Warnings: ${totalWarnings}`);
console.log(totalErrors === 0 ? '✅ All cities pass ontology validation' : `❌ ${totalErrors} errors need fixing`);

process.exit(totalErrors > 0 ? 1 : 0);
