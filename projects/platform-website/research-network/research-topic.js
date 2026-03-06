#!/usr/bin/env node
/**
 * Research Topic Pipeline v1.0
 * 
 * Takes a topic ID from the taxonomy, executes full research:
 * 1. Load topic context (existing claims, cross-learnings, gaps)
 * 2. Generate search queries
 * 3. Output structured report (JSON) ready for extract-claims.js
 * 4. Generate HTML report in AR-format (Beipackzettel, Claim Ledger, Sources)
 * 
 * Usage: node research-topic.js <topic-id> [--query "optional user question"]
 * 
 * NOTE: This script generates the STRUCTURE. The actual web research
 * must be executed by Mia (who has web_search + web_fetch tools).
 * 
 * Full execution command for Mia:
 *   "Führe Research aus für Topic <id>. Nutze research-topic.js als Template."
 */

const fs = require('fs');
const path = require('path');

const GRAPH = path.join(__dirname, 'graph/knowledge-graph.json');
const DOSSIERS = path.join(__dirname, 'graph/topic-dossiers.json');
const TAX = path.join(__dirname, 'taxonomy.json');
const REPORTS_DIR = path.join(__dirname, 'reports');
const HTML_DIR = path.join(__dirname, '../research');

function load(f) { return JSON.parse(fs.readFileSync(f, 'utf8')); }

function buildGraphSources(topic, graph) {
  const claims = Object.values(graph.claims || {}).filter(c => (c.topics || []).includes(topic));
  const sourceCounts = new Map();
  const sourceFallbacks = new Map();
  const reportCache = new Map();

  const loadReport = (reportId) => {
    if (reportCache.has(reportId)) return reportCache.get(reportId);
    const reportPath = path.join(REPORTS_DIR, `${reportId}.json`);
    if (!fs.existsSync(reportPath)) {
      reportCache.set(reportId, null);
      return null;
    }
    const report = load(reportPath);
    reportCache.set(reportId, report);
    return report;
  };

  claims.forEach(claim => {
    (claim.sources || []).forEach(sourceId => {
      const key = `${claim.reportId}::${sourceId}`;
      sourceCounts.set(key, (sourceCounts.get(key) || 0) + 1);
      if (claim.realSources) {
        const fallback = claim.realSources.find(s => s.id === sourceId);
        if (fallback) sourceFallbacks.set(key, fallback);
      }
    });
  });

  const sources = [];
  for (const [key, claimCount] of sourceCounts.entries()) {
    const [reportId, sourceId] = key.split('::');
    const report = loadReport(reportId);
    let source = report && (report.sources || []).find(s => s.id === sourceId);
    if (!source) source = sourceFallbacks.get(key) || null;
    if (!source) continue;
    sources.push({
      id: sourceId,
      reportId,
      label: source.label,
      url: source.url || '',
      admiralty: source.admiralty || 'B2',
      claimCount
    });
  }

  return sources.sort((a, b) => b.claimCount - a.claimCount);
}

const args = process.argv.slice(2);
const topicId = args[0];
const userQuery = args.find((a, i) => args[i - 1] === '--query') || null;

if (!topicId) {
  console.log('Usage: node research-topic.js <topic-id> [--query "question"]');
  console.log('\nAvailable gap topics:');
  const dos = load(DOSSIERS);
  Object.values(dos)
    .filter(d => d.isGap)
    .slice(0, 15)
    .forEach(d => console.log(`  △ ${d.id} — ${d.label}`));
  process.exit(1);
}

const G = load(GRAPH);
const DOS = load(DOSSIERS);
const dossier = DOS[topicId];

if (!dossier) {
  console.error(`Topic "${topicId}" not found in dossiers.`);
  process.exit(1);
}

// ═══ BUILD RESEARCH CONTEXT ═══
const sug = dossier.suggestions || { sources: [], claims: [], researchQuestions: [] };
const existing = dossier.categorizedClaims || {};
const cross = dossier.crossLearnings || [];
const conf = dossier.confidence || { score: 0, reason: 'No data' };
const graphSources = buildGraphSources(topicId, G);
const adjacentSources = (sug.sources || []).map(s => ({
  ...s,
  label: `[ADJACENT] ${s.label}`
}));
const usedGraphSourceKeys = new Set(graphSources.map(s => `${s.label}::${s.url || ''}`));
const fallbackAdj = adjacentSources.filter(s => {
  const baseLabel = s.label.replace(/^\[ADJACENT\] /, '');
  return !usedGraphSourceKeys.has(`${baseLabel}::${s.url || ''}`);
});
const suggestedSources = graphSources.length >= 3
  ? graphSources
  : graphSources.concat(fallbackAdj.slice(0, Math.max(3 - graphSources.length, 0)));

// Generate report ID
const reportId = 'rr-' + topicId.replace(/^t-|^topic-/, '') + '-' + new Date().toISOString().slice(0, 7);

// ═══ GENERATE MIA EXECUTION PROMPT ═══
let prompt = `# RESEARCH EXECUTION: ${dossier.label}
# Report ID: ${reportId}
# Generated: ${new Date().toISOString().slice(0, 10)}

## AUFTRAG
Erstelle einen vollständigen Research Report für Topic "${dossier.label}".
Standard: AR-Format (wie AR-020). Mind. 20 Tier-1 Quellen.
${userQuery ? `\nUser-Frage: "${userQuery}"` : ''}

## KONTEXT (was wir wissen)
Current Confidence: ${conf.score}% — ${conf.reason}
`;

// Existing claims
const allExisting = [
  ...(existing.evidence || []),
  ...(existing.interpretation || []),
  ...(existing.judgment || []),
  ...(existing.assumption || [])
];
if (allExisting.length) {
  prompt += `\nExistierende Claims (${allExisting.length}):\n`;
  allExisting.slice(0, 10).forEach(c => {
    prompt += `- [${c.eija}] ${c.claim}\n`;
    if (c.soWhat) prompt += `  → ${c.soWhat}\n`;
  });
}

// Cross-learnings
if (cross.length) {
  prompt += `\nCross-Learnings:\n`;
  cross.slice(0, 5).forEach(cl => {
    prompt += `- ${cl.topicId}: ${cl.sharedClaims} shared claims\n`;
    (cl.sharedClaimTexts || []).forEach(t => prompt += `  "${t}"\n`);
  });
}

// Research questions
prompt += `\n## FORSCHUNGSFRAGEN\n`;
(sug.researchQuestions || []).forEach(q => prompt += `- ${q}\n`);
if (userQuery) prompt += `- ${userQuery}\n`;

// Open questions from dossier
const oq = dossier.openQuestions || [];
if (oq.length) {
  prompt += `\nOffene Fragen:\n`;
  oq.forEach(q => prompt += `- ${q.text}\n`);
}

// Suggested sources
prompt += `\n## QUELLEN (starte hier, dann erweitere auf 20+)\n`;
suggestedSources.forEach(s => {
  prompt += `- [${s.admiralty}] ${s.label}`;
  if (s.url) prompt += ` → ${s.url}`;
  prompt += `\n`;
});

// Execution instructions
prompt += `
## EXECUTION STEPS
1. BLUF zuerst: 2–4 Sätze/Bullets ganz am Anfang des Reports, vor allen anderen Sektionen.
2. Hypothese VOR dem Suchen formulieren (1–2 Sätze). Danach gezielt widerlegen.
3. MECE-Decomposition: Zerlege die Hauptfrage in 3–7 Sub-Fragen (nicht überlappend).
4. Für jede Sub-Frage: web_search (mind. 3 Searches) + web_fetch der besten Ergebnisse.
5. Disconfirmation: Suche aktiv nach Gegenbelegen (kritisch/kontra/negative keywords).
6. Stopping Criteria: Wenn 3 konsekutive Sources keine neue Info liefern → STOP für diese Sub-Frage.
7. Für jede Quelle: Admiralty-Code vergeben (A1/A2/B2/B3/C2/C3).
8. Claims extrahieren: EIJA-Tag (E/I/J/A) + Admiralty + soWhat pro Claim.
9. Widersprüche zu existierenden Claims identifizieren (beide Seiten dokumentieren).
10. Beipackzettel erstellen (Pflicht):
   - STARK BELEGT
   - UNSICHER
   - WIDERSPRÜCHE
   - NICHT GEFUNDEN
11. Follow-Up Fragen (3-5) + angrenzende Topics die profitieren.

## OUTPUT
1. JSON Report: research-network/reports/${reportId}.json
2. HTML Report: research/${reportId}.html (AR-Format)
3. Ingest: node extract-claims.js --ingest && node enrich-topics.js
`;

// ═══ GENERATE REPORT TEMPLATE (JSON) ═══
const reportTemplate = {
  id: reportId,
  title: `Research Report: ${dossier.label}`,
  date: new Date().toISOString().slice(0, 10),
  author: 'Ainary Research Network',
  domain: topicId,
  admiralty: 'B2',
  confidence: 0,
  sourceCount: 0,
  status: 'template',
  topics: [topicId],
  sources: suggestedSources.map((s, i) => ({
    id: 's' + (i + 1),
    label: s.label,
    url: s.url || '',
    admiralty: s.admiralty || 'B2'
  })),
  claims: [],
  beipackzettel: {
    starkBelegt: [],
    unsicher: [],
    nichtGefunden: (sug.researchQuestions || []),
    widersprueche: [],
    followUp: []
  }
};

// ═══ GENERATE HTML TEMPLATE ═══
const htmlTemplate = `<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>${reportId} — ${dossier.label}</title>
<style>
  @page { size: A4; margin: 2.5cm 2cm; }
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body { font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 11pt; line-height: 1.6; color: #1a1a1a; max-width: 210mm; margin: 0 auto; padding: 40px 48px; background: #fff; }
  h1 { font-size: 22pt; font-weight: 700; letter-spacing: -0.5px; margin: 0 0 4px; }
  .subtitle { font-size: 13pt; color: #444; margin-bottom: 4px; }
  .meta-line { font-size: 9pt; color: #888; margin-bottom: 24px; }
  h2 { font-size: 15pt; font-weight: 700; margin: 32px 0 12px; padding-bottom: 4px; border-bottom: 2px solid #0a0a0a; }
  h3 { font-size: 12pt; font-weight: 700; color: #222; margin: 20px 0 8px; }
  p { margin: 0 0 10px; }
  ul, ol { margin: 0 0 12px 20px; }
  li { margin-bottom: 4px; }
  table { width: 100%; border-collapse: collapse; margin: 12px 0 20px; font-size: 10pt; }
  th { background: #0a0a0a; color: #fff; font-weight: 600; text-align: left; padding: 8px 10px; }
  td { border-bottom: 1px solid #e0e0e0; padding: 7px 10px; vertical-align: top; }
  tr:nth-child(even) td { background: #fafafa; }
  .beipackzettel { background: #f0f4f8; border: 1px solid #c8d6e5; border-radius: 6px; padding: 20px; margin: 0 0 28px; }
  .beipackzettel h2 { font-size: 13pt; border-bottom: 1px solid #c8d6e5; color: #2c3e50; margin-top: 0; }
  .beipackzettel table { font-size: 9.5pt; }
  .beipackzettel th { background: #2c3e50; }
  .finding-block { background: #fff; border: 1px solid #e0e0e0; border-left: 4px solid #2c3e50; border-radius: 4px; padding: 16px; margin: 12px 0; }
  .label { font-size: 9pt; font-weight: 700; text-transform: uppercase; letter-spacing: 0.5px; margin-bottom: 4px; }
  .label.evidence { color: #27ae60; }
  .label.interpretation { color: #2980b9; }
  .label.judgment { color: #e67e22; }
  .label.assumption { color: #e74c3c; }
  .tag { display: inline-block; font-size: 8pt; padding: 2px 6px; border-radius: 3px; margin: 1px 2px; }
  .tag-high { background: #d4edda; color: #155724; }
  .tag-med { background: #fff3cd; color: #856404; }
  .tag-low { background: #f8d7da; color: #721c24; }
  .back-cover { margin-top: 48px; padding-top: 24px; border-top: 2px solid #0a0a0a; text-align: center; font-size: 10pt; color: #666; }
</style>
</head>
<body>

<h1>${reportId.toUpperCase()}: ${dossier.label}</h1>
<p class="subtitle">Ainary Research Report</p>
<p class="meta-line">${new Date().toISOString().slice(0, 10)} · Ainary Ventures · Florian Ziesche</p>

<div class="beipackzettel">
<h2>BEIPACKZETTEL</h2>
<table>
<thead><tr><th>Field</th><th>Value</th></tr></thead>
<tbody>
<tr><td>Report ID</td><td>${reportId}</td></tr>
<tr><td>Topic</td><td>${dossier.label}</td></tr>
<tr><td>Confidence</td><td>__% (to be filled after research)</td></tr>
<tr><td>Sources</td><td>__ numbered [S1]-[S__]</td></tr>
<tr><td>Load-Bearing Claims</td><td>__ (see Claim Ledger)</td></tr>
<tr><td>Contradictions</td><td>__ (see below)</td></tr>
<tr><td>Pre-existing Knowledge</td><td>${allExisting.length} claims, ${conf.score}% confidence</td></tr>
<tr><td>Adjacent Topics</td><td>${(dossier.adjacentTopics || []).map(a => a.label).join(', ')}</td></tr>
<tr><td>Known Limitations</td><td>[to be filled]</td></tr>
</tbody>
</table>
</div>

<h2>ASSUMPTION REGISTER</h2>
<p>[To be filled during research — list every assumption that underlies the findings]</p>

<h2>EXECUTIVE SUMMARY</h2>
<p>[SCR Framework: Situation — Complication — Resolution]</p>

<h2>KEY FINDINGS</h2>
<!-- Finding blocks with EIJA labels -->

<h2>CLAIM LEDGER</h2>
<table>
<thead><tr><th>#</th><th>Claim</th><th>EIJA</th><th>Admiralty</th><th>Trust</th><th>Sources</th><th>So What</th></tr></thead>
<tbody>
<!-- Claims go here -->
</tbody>
</table>

<h2>SOURCES</h2>
<table>
<thead><tr><th>#</th><th>Source</th><th>Admiralty</th><th>URL</th></tr></thead>
<tbody>
<!-- Sources go here -->
</tbody>
</table>

<h2>BEIPACKZETTEL — TRANSPARENZ</h2>
<h3>Stark Belegt</h3>
<p>[Claims with ≥2 independent sources, Trust ≥85%]</p>
<h3>Unsicher</h3>
<p>[Claims with 1 source or Trust <70%]</p>
<h3>Nicht Gefunden</h3>
<p>[Research questions that remained unanswered]</p>
<h3>Widersprüche</h3>
<p>[Where new knowledge conflicts with existing claims]</p>

<h2>FOLLOW-UP QUESTIONS</h2>
<ol>
<li>[Question 1]</li>
<li>[Question 2]</li>
<li>[Question 3]</li>
</ol>

<div class="back-cover">
  <strong>Ainary Ventures</strong><br>
  AI Strategy &middot; Research &middot; System Design<br>
  <span style="font-size:9pt; color:#999;">Florian Ziesche &middot; florian@ainaryventures.com</span>
</div>
</body>
</html>`;

// ═══ SAVE OUTPUTS ═══
if (!fs.existsSync(REPORTS_DIR)) fs.mkdirSync(REPORTS_DIR, { recursive: true });

// Save JSON template
fs.writeFileSync(path.join(REPORTS_DIR, reportId + '.json'), JSON.stringify(reportTemplate, null, 2));
console.log(`✓ JSON template: reports/${reportId}.json`);

// Save HTML template
const researchDir = path.join(__dirname, '..', 'research');
if (!fs.existsSync(researchDir)) fs.mkdirSync(researchDir, { recursive: true });
fs.writeFileSync(path.join(researchDir, reportId + '.html'), htmlTemplate);
console.log(`✓ HTML template: research/${reportId}.html`);

// Save execution prompt
fs.writeFileSync(path.join(REPORTS_DIR, reportId + '-prompt.md'), prompt);
console.log(`✓ Execution prompt: reports/${reportId}-prompt.md`);

console.log(`\n═══ NEXT STEP ═══`);
console.log(`Send to Mia: "Führe aus: research-network/reports/${reportId}-prompt.md"`);
console.log(`Or paste the prompt directly.`);
console.log(`\nAfter completion:`);
console.log(`  node extract-claims.js --ingest`);
console.log(`  node enrich-topics.js`);
