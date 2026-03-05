#!/usr/bin/env node
/**
 * Ainary Research Ontology Network — Claim Extractor v1.0
 * 
 * Extracts structured claims from research reports and links them
 * to a shared knowledge graph (Topics + Claims + Verified Truths).
 * 
 * "Whenever someone runs research, everyone that is part of it gets smarter."
 * 
 * Usage:
 *   node extract-claims.js <report.json>           — Extract claims from a report
 *   node extract-claims.js --ingest <report.json>  — Extract + merge into knowledge graph
 *   node extract-claims.js --status                — Show knowledge graph stats
 *   node extract-claims.js --topic <topic-id>      — Show topic detail with all claims
 *   node extract-claims.js --contradictions        — Show all contradictions
 * 
 * Report JSON format:
 * {
 *   "id": "rr-palantir-deep-2026-03",
 *   "title": "Palantir Deep Research",
 *   "date": "2026-03-05",
 *   "author": "mia",
 *   "domain": "agent-architecture",
 *   "admiralty": "B2",
 *   "sources": [...],
 *   "claims": [...]   // Can be pre-extracted or raw text
 * }
 */

const fs = require('fs');
const path = require('path');

const GRAPH_DIR = path.join(__dirname, 'graph');
const GRAPH_FILE = path.join(GRAPH_DIR, 'knowledge-graph.json');

// ═══ ADMIRALTY SYSTEM ═══

function deriveConfidence(admiralty) {
  const map = { A1: 95, A2: 90, B1: 85, B2: 80, B3: 70, C1: 75, C2: 65, C3: 60, D4: 40, E2: 30 };
  return map[admiralty] || 50;
}

function deriveSourceLabel(admiralty) {
  const map = {
    A1: 'Amtliche Quelle', A2: 'Überregionales Leitmedium',
    B1: 'Nationales Leitmedium', B2: 'Regionales Leitmedium', B3: 'Regionaler Fachverlag',
    C1: 'Spezialpublikation', C2: 'Partei-/Kandidatenwebsite', C3: 'Social Media / Community'
  };
  return map[admiralty] || 'Unbekannte Quelle';
}

// ═══ KNOWLEDGE GRAPH ═══

function loadGraph() {
  if (!fs.existsSync(GRAPH_DIR)) fs.mkdirSync(GRAPH_DIR, { recursive: true });
  if (!fs.existsSync(GRAPH_FILE)) {
    return {
      _meta: { version: '1.0', created: new Date().toISOString().split('T')[0], lastUpdated: null },
      reports: {},
      claims: {},
      topics: {},
      contradictions: [],
      verifiedTruths: []
    };
  }
  return JSON.parse(fs.readFileSync(GRAPH_FILE, 'utf8'));
}

function saveGraph(graph) {
  graph._meta.lastUpdated = new Date().toISOString().split('T')[0];
  fs.writeFileSync(GRAPH_FILE, JSON.stringify(graph, null, 2), 'utf8');
}

// ═══ CLAIM EXTRACTION ═══

function extractClaimsFromReport(report) {
  // If claims are already structured, use them
  if (report.claims && Array.isArray(report.claims)) {
    return report.claims.map((c, i) => ({
      id: `${report.id}-c${String(i + 1).padStart(3, '0')}`,
      reportId: report.id,
      claim: c.claim || c.text || c,
      eija: c.eija || 'A', // Default: Assumption until classified
      admiralty: c.admiralty || report.admiralty || 'C3',
      confidence: c.confidence || deriveConfidence(c.admiralty || report.admiralty || 'C3'),
      sources: c.sources || [],
      topics: c.topics || [],
      status: c.status || 'unverified',
      soWhat: c.soWhat || null,
      date: report.date,
      author: report.author
    }));
  }
  return [];
}

// ═══ TOPIC MANAGEMENT ═══

function ensureTopic(graph, topicId, label, domain) {
  if (!graph.topics[topicId]) {
    graph.topics[topicId] = {
      id: topicId,
      label: label || topicId,
      type: 'topic',
      domain: domain || 'general',
      claimIds: [],
      reportIds: [],
      verifiedClaimCount: 0,
      contradictionCount: 0,
      lastUpdated: new Date().toISOString().split('T')[0],
      executiveSummary: null,
      openQuestions: []
    };
  }
  return graph.topics[topicId];
}

function updateTopicStats(graph, topicId) {
  const topic = graph.topics[topicId];
  if (!topic) return;

  const claims = topic.claimIds.map(id => graph.claims[id]).filter(Boolean);
  topic.verifiedClaimCount = claims.filter(c => c.status === 'verified').length;

  // Konsistenz badge
  const totalClaims = claims.length;
  const verifiedSources = new Set();
  claims.forEach(c => (c.sources || []).forEach(s => verifiedSources.add(s)));
  const sourceCount = verifiedSources.size;

  if (sourceCount >= 3) {
    topic.konsistenz = `◉ Bestätigt durch ${sourceCount} unabhängige Quellen`;
    topic.konsistenzLevel = 'high';
  } else if (sourceCount >= 2) {
    topic.konsistenz = `◉ Bestätigt durch ${sourceCount} Quellen`;
    topic.konsistenzLevel = 'medium';
  } else {
    topic.konsistenz = '△ Wenige Quellen';
    topic.konsistenzLevel = 'low';
  }

  // Count contradictions
  topic.contradictionCount = graph.contradictions.filter(
    c => c.topicId === topicId
  ).length;

  // Auto executive summary from top-confidence claims
  const topClaims = claims
    .filter(c => c.eija === 'E' || c.eija === 'I')
    .sort((a, b) => (b.confidence || 0) - (a.confidence || 0))
    .slice(0, 5);

  if (topClaims.length > 0) {
    topic.executiveSummary = topClaims.map(c => c.claim).join(' ');
  }

  // Open questions: high-A topics
  const assumptionRate = claims.filter(c => c.eija === 'A').length / Math.max(claims.length, 1);
  if (assumptionRate > 0.4) {
    topic.openQuestions = [`${Math.round(assumptionRate * 100)}% der Claims sind Annahmen — Verifikation nötig`];
  }

  topic.lastUpdated = new Date().toISOString().split('T')[0];
}

// ═══ CONTRADICTION DETECTION ═══

function detectContradictions(graph, newClaims) {
  const found = [];
  const existingClaims = Object.values(graph.claims);

  for (const nc of newClaims) {
    for (const ec of existingClaims) {
      if (nc.id === ec.id) continue;
      // Same topic, different conclusion — flag for review
      const sharedTopics = (nc.topics || []).filter(t => (ec.topics || []).includes(t));
      if (sharedTopics.length > 0 && nc.eija !== 'E' && ec.eija !== 'E') {
        // Simple heuristic: if both are judgments on same topic with different sentiment
        // Real implementation would use semantic similarity
        if (nc.eija === 'J' && ec.eija === 'J') {
          // Potential contradiction — flag for human review
          found.push({
            id: `contra-${nc.id}-${ec.id}`,
            claim1: nc.id,
            claim2: ec.id,
            topicId: sharedTopics[0],
            status: 'pending_review',
            detected: new Date().toISOString().split('T')[0]
          });
        }
      }
    }
  }
  return found;
}

// ═══ INGEST PIPELINE ═══

function ingestReport(reportPath) {
  const report = JSON.parse(fs.readFileSync(reportPath, 'utf8'));
  const graph = loadGraph();

  console.log(`\n═══ INGESTING: ${report.title} ═══`);
  console.log(`ID: ${report.id} | Domain: ${report.domain} | Sources: ${(report.sources || []).length}`);

  // 1. Register report
  graph.reports[report.id] = {
    id: report.id,
    title: report.title,
    date: report.date,
    author: report.author,
    domain: report.domain,
    admiralty: report.admiralty,
    confidence: deriveConfidence(report.admiralty),
    sourceCount: (report.sources || []).length,
    status: 'published'
  };

  // 2. Extract claims
  const claims = extractClaimsFromReport(report);
  console.log(`Claims extracted: ${claims.length}`);

  // 3. Register claims + link to topics
  for (const claim of claims) {
    graph.claims[claim.id] = claim;

    // Ensure topics exist and link
    for (const topicRef of (claim.topics || [])) {
      const topicId = typeof topicRef === 'string' ? topicRef : topicRef.id;
      const topicLabel = typeof topicRef === 'string' ? topicRef : topicRef.label;
      const topic = ensureTopic(graph, topicId, topicLabel, report.domain);

      if (!topic.claimIds.includes(claim.id)) topic.claimIds.push(claim.id);
      if (!topic.reportIds.includes(report.id)) topic.reportIds.push(report.id);
    }
  }

  // 4. Detect contradictions
  const contras = detectContradictions(graph, claims);
  if (contras.length > 0) {
    console.log(`⚠️  ${contras.length} potential contradictions detected`);
    graph.contradictions.push(...contras);
  }

  // 5. Update topic stats
  for (const topicId of Object.keys(graph.topics)) {
    updateTopicStats(graph, topicId);
  }

  // 6. Check for new verified truths (≥3 independent confirmations)
  for (const [topicId, topic] of Object.entries(graph.topics)) {
    const topicClaims = topic.claimIds.map(id => graph.claims[id]).filter(Boolean);
    const evidenceClaims = topicClaims.filter(c => c.eija === 'E' && c.confidence >= 80);

    // Group by semantic similarity (simplified: same first 50 chars)
    const groups = {};
    evidenceClaims.forEach(c => {
      const key = c.claim.substring(0, 50).toLowerCase();
      if (!groups[key]) groups[key] = [];
      groups[key].push(c);
    });

    for (const [key, group] of Object.entries(groups)) {
      if (group.length >= 3) {
        const uniqueReports = new Set(group.map(c => c.reportId));
        if (uniqueReports.size >= 3) {
          const vtId = `VT-${topicId}-${graph.verifiedTruths.length + 1}`;
          if (!graph.verifiedTruths.find(vt => vt.claim === group[0].claim)) {
            graph.verifiedTruths.push({
              id: vtId,
              claim: group[0].claim,
              topicId,
              confirmedBy: group.map(c => c.id),
              reportCount: uniqueReports.size,
              confidence: Math.round(group.reduce((s, c) => s + c.confidence, 0) / group.length),
              date: new Date().toISOString().split('T')[0]
            });
            console.log(`✅ NEW VERIFIED TRUTH: ${vtId} — "${group[0].claim.substring(0, 60)}..."`);
          }
        }
      }
    }
  }

  // 7. Save
  saveGraph(graph);
  graph.reports[report.id].claimCount = claims.length;

  // 8. Summary
  console.log(`\n═══ GRAPH STATUS ═══`);
  printStatus(graph);

  return graph;
}

// ═══ STATUS ═══

function printStatus(graph) {
  if (!graph) graph = loadGraph();
  const reports = Object.values(graph.reports);
  const claims = Object.values(graph.claims);
  const topics = Object.values(graph.topics);

  console.log(`Reports: ${reports.length}`);
  console.log(`Claims:  ${claims.length}`);
  console.log(`Topics:  ${topics.length}`);
  console.log(`Verified Truths: ${graph.verifiedTruths.length}`);
  console.log(`Contradictions:  ${graph.contradictions.length}`);

  // EIJA distribution
  const eijaDist = { E: 0, I: 0, J: 0, A: 0 };
  claims.forEach(c => { if (eijaDist[c.eija] !== undefined) eijaDist[c.eija]++; });
  console.log(`EIJA: E=${eijaDist.E} I=${eijaDist.I} J=${eijaDist.J} A=${eijaDist.A}`);

  // Topic ranking
  if (topics.length > 0) {
    console.log(`\nTopics (by claim count):`);
    topics.sort((a, b) => (b.claimIds || []).length - (a.claimIds || []).length);
    topics.slice(0, 10).forEach(t => {
      const claimCount = (t.claimIds || []).length;
      const badge = t.konsistenzLevel === 'high' ? '◉' : t.konsistenzLevel === 'medium' ? '◈' : '△';
      console.log(`  ${badge} ${t.label} — ${claimCount} claims, ${t.verifiedClaimCount} verified, ${t.contradictionCount} contradictions`);
    });
  }

  // Compound metric
  if (reports.length > 1) {
    const avgClaimsPerReport = Math.round(claims.length / reports.length);
    const crossTopicClaims = claims.filter(c => (c.topics || []).length > 1).length;
    console.log(`\nCompound Effect:`);
    console.log(`  Avg claims/report: ${avgClaimsPerReport}`);
    console.log(`  Cross-topic claims: ${crossTopicClaims} (${Math.round(crossTopicClaims / Math.max(claims.length, 1) * 100)}%)`);
    console.log(`  Knowledge density: ${(claims.length / Math.max(topics.length, 1)).toFixed(1)} claims/topic`);
  }
}

function showTopic(topicId) {
  const graph = loadGraph();
  const topic = graph.topics[topicId];
  if (!topic) { console.log(`Topic "${topicId}" not found`); return; }

  console.log(`\n═══ TOPIC: ${topic.label} ═══`);
  console.log(`Domain: ${topic.domain} | Claims: ${(topic.claimIds || []).length} | Reports: ${(topic.reportIds || []).length}`);
  console.log(`${topic.konsistenz || '△ No konsistenz data'}`);
  if (topic.executiveSummary) console.log(`\nSummary: ${topic.executiveSummary.substring(0, 200)}...`);

  const claims = (topic.claimIds || []).map(id => graph.claims[id]).filter(Boolean);
  claims.sort((a, b) => (b.confidence || 0) - (a.confidence || 0));

  console.log(`\nClaims:`);
  claims.forEach(c => {
    const eijaLabel = { E: 'EVIDENZ', I: 'INTERPRETATION', J: 'BEWERTUNG', A: 'ANNAHME' }[c.eija] || c.eija;
    console.log(`  [${c.eija}] ${c.confidence}% — ${c.claim.substring(0, 80)}${c.claim.length > 80 ? '...' : ''}`);
    console.log(`      ${eijaLabel} | ${c.status} | Report: ${c.reportId}`);
  });

  if (topic.openQuestions && topic.openQuestions.length > 0) {
    console.log(`\nOpen Questions:`);
    topic.openQuestions.forEach(q => console.log(`  ? ${q}`));
  }
}

function showContradictions() {
  const graph = loadGraph();
  if (graph.contradictions.length === 0) {
    console.log('No contradictions detected.');
    return;
  }
  console.log(`\n═══ ${graph.contradictions.length} CONTRADICTIONS ═══`);
  graph.contradictions.forEach(c => {
    const c1 = graph.claims[c.claim1];
    const c2 = graph.claims[c.claim2];
    console.log(`\n${c.id} [${c.status}]`);
    console.log(`  Topic: ${c.topicId}`);
    if (c1) console.log(`  Claim 1: [${c1.eija}] ${c1.claim.substring(0, 60)}...`);
    if (c2) console.log(`  Claim 2: [${c2.eija}] ${c2.claim.substring(0, 60)}...`);
  });
}

// ═══ MAIN ═══

const args = process.argv.slice(2);

if (args[0] === '--status') {
  printStatus();
} else if (args[0] === '--topic' && args[1]) {
  showTopic(args[1]);
} else if (args[0] === '--contradictions') {
  showContradictions();
} else if (args[0] === '--ingest' && args[1]) {
  ingestReport(args[1]);
} else if (args[0] && !args[0].startsWith('-')) {
  // Just extract, don't ingest
  const report = JSON.parse(fs.readFileSync(args[0], 'utf8'));
  const claims = extractClaimsFromReport(report);
  console.log(JSON.stringify(claims, null, 2));
} else {
  console.log('Ainary Research Ontology Network — Claim Extractor v1.0');
  console.log('');
  console.log('Usage:');
  console.log('  node extract-claims.js <report.json>           Extract claims (dry run)');
  console.log('  node extract-claims.js --ingest <report.json>  Extract + merge into graph');
  console.log('  node extract-claims.js --status                Show knowledge graph stats');
  console.log('  node extract-claims.js --topic <topic-id>      Show topic detail');
  console.log('  node extract-claims.js --contradictions        Show contradictions');
}
