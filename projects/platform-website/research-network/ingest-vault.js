#!/usr/bin/env node
/**
 * Ainary Vault Ingester v1.0
 * Crawls an Obsidian vault, extracts claims, builds knowledge graph.
 * 
 * Usage: node ingest-vault.js <vault-path> [--dry-run] [--limit N]
 */

const fs = require('fs');
const path = require('path');

const GRAPH_DIR = path.join(__dirname, 'graph');
const GRAPH_FILE = path.join(GRAPH_DIR, 'knowledge-graph.json');

const SKIP_DIRS = ['Installers', '.obsidian', '.trash', 'node_modules', '.git', 'Attachments'];
const SKIP_FILES = ['README.md', 'CHANGELOG.md', 'LICENSE.md'];
const MIN_SIZE = 200; // bytes — skip tiny stubs

// ═══ ADMIRALTY ═══
function deriveConfidence(adm) {
  return {A1:95,A2:90,B1:85,B2:80,B3:70,C1:75,C2:65,C3:60,D4:40,E2:30}[adm]||50;
}

// ═══ PHASE 1: CRAWL ═══
function crawlVault(vaultPath) {
  const files = [];
  
  function walk(dir, depth) {
    if (depth > 8) return;
    let entries;
    try { entries = fs.readdirSync(dir, {withFileTypes:true}); } catch(e) { return; }
    
    for (const ent of entries) {
      if (ent.name.startsWith('.')) continue;
      const full = path.join(dir, ent.name);
      
      if (ent.isDirectory()) {
        if (SKIP_DIRS.some(s => ent.name.includes(s))) continue;
        walk(full, depth + 1);
      } else if (ent.name.endsWith('.md') && !SKIP_FILES.includes(ent.name)) {
        const stat = fs.statSync(full);
        if (stat.size >= MIN_SIZE) {
          files.push({
            path: full,
            relativePath: path.relative(vaultPath, full),
            size: stat.size,
            modified: stat.mtime
          });
        }
      }
    }
  }
  
  walk(vaultPath, 0);
  return files.sort((a,b) => b.size - a.size);
}

// ═══ PHASE 2: CLASSIFY ═══
function classifyFile(file) {
  const rel = file.relativePath.toLowerCase();
  const parts = rel.split('/');
  
  if (parts.includes('installers') || parts.includes('node_modules')) return 'junk';
  if (rel.includes('readme') || rel.includes('changelog') || rel.includes('license')) return 'meta';
  if (parts.includes('projects')) return 'project';
  if (parts.includes('resources')) return 'resource';
  if (parts.includes('ai-conversations')) return 'conversation';
  if (parts.includes('brand')) return 'brand';
  if (rel.includes('moc') || rel.includes('index') || rel.includes('00-')) return 'index';
  return 'note';
}

// ═══ PHASE 3: EXTRACT ═══
function extractFromMarkdown(content, file) {
  const claims = [];
  const entities = new Set();
  const topics = new Set();
  const lines = content.split('\n');
  
  // Extract frontmatter tags
  const fmMatch = content.match(/^---\n([\s\S]*?)\n---/);
  if (fmMatch) {
    const tagMatch = fmMatch[1].match(/tags:\s*\[(.*?)\]/);
    if (tagMatch) tagMatch[1].split(',').forEach(t => topics.add(t.trim()));
  }
  
  // Extract wikilinks as entities
  const wikilinks = content.match(/\[\[([^\]]+)\]\]/g) || [];
  wikilinks.forEach(wl => {
    const name = wl.replace(/\[\[|\]\]/g, '').split('|')[0].trim();
    if (name.length > 2 && name.length < 80) entities.add(name);
  });
  
  // Extract topic from directory structure
  const dirParts = file.relativePath.split('/');
  if (dirParts.length > 1) {
    topics.add(dirParts.slice(0, -1).join('/').toLowerCase().replace(/\s+/g, '-'));
  }
  
  // Extract claims from content
  // Pattern 1: Lines with strong assertions (numbers, dates, "ist", "hat", "wird")
  // Pattern 2: Quoted text
  // Pattern 3: List items with substance
  // Pattern 4: Headers as topic indicators
  
  let currentHeader = '';
  
  for (let i = 0; i < lines.length; i++) {
    const line = lines[i].trim();
    
    // Track headers for context
    if (line.startsWith('#')) {
      currentHeader = line.replace(/^#+\s*/, '');
      if (currentHeader.length > 3 && currentHeader.length < 100) {
        topics.add('topic-' + currentHeader.toLowerCase().replace(/[^a-zäöü0-9]+/g, '-').substring(0, 40));
      }
      continue;
    }
    
    // Skip short lines, code blocks, empty
    if (line.length < 30) continue;
    if (line.startsWith('```') || line.startsWith('|')) continue;
    
    // Claim extraction: lines with factual content
    const isFactual = /\d{4}|\d+%|\$\d|\€\d|million|billion|mrd|mio/i.test(line);
    const isDecision = /entscheidung|decision|beschluss|gewählt|nominiert|gewonnen|verloren/i.test(line);
    const isQuote = /^>\s/.test(line) || /".*"/.test(line) || /„.*"/.test(line);
    const isAssertion = /\b(ist|hat|wird|muss|sollte|kann nicht|funktioniert|beweis|zeigt|bestätigt)\b/i.test(line);
    const isBullet = /^[-*]\s/.test(line) && line.length > 40;
    
    if (isFactual || isDecision || isQuote || (isAssertion && line.length > 50) || (isBullet && line.length > 60)) {
      // Clean the line
      let claimText = line
        .replace(/^[-*>\s]+/, '')
        .replace(/\[\[([^\]|]+)(\|[^\]]+)?\]\]/g, '$1') // Remove wikilink syntax
        .replace(/\*\*/g, '')  // Remove bold
        .replace(/\[([^\]]+)\]\([^)]+\)/g, '$1')  // Markdown links → text
        .trim();
      
      if (claimText.length < 20 || claimText.length > 500) continue;
      
      // Determine EIJA
      let eija = 'E'; // default
      if (/meinung|denke|glaube|vermutung|annahme|wahrscheinlich|vielleicht/i.test(claimText)) eija = 'A';
      else if (/bewertung|gut|schlecht|besser|falsch|richtig|sollte|muss/i.test(claimText)) eija = 'J';
      else if (/bedeutet|impliziert|daraus folgt|interpretation|einordnung/i.test(claimText)) eija = 'I';
      
      // Determine admiralty from source type
      let admiralty = 'C2'; // default: internal note
      if (isQuote) admiralty = 'B2'; // quoted from somewhere
      if (isFactual && /\d{4}/.test(claimText)) admiralty = 'B2'; // has specific dates/numbers
      
      claims.push({
        claim: claimText,
        eija: eija,
        admiralty: admiralty,
        confidence: deriveConfidence(admiralty),
        sources: [file.relativePath],
        topics: Array.from(topics).slice(0, 3),
        status: 'unverified',
        context: currentHeader || null,
        lineNumber: i + 1
      });
    }
  }
  
  return { claims, entities: Array.from(entities), topics: Array.from(topics) };
}

// ═══ PHASE 4: RESOLVE (entity dedup) ═══
function resolveEntities(allEntities) {
  const normalized = {};
  
  for (const [name, files] of Object.entries(allEntities)) {
    // Normalize: lowercase, trim, remove common suffixes
    const key = name.toLowerCase().trim()
      .replace(/\s+/g, ' ')
      .replace(/\.(md|txt)$/, '');
    
    if (!normalized[key]) normalized[key] = { canonical: name, files: new Set(), count: 0 };
    files.forEach(f => normalized[key].files.add(f));
    normalized[key].count += files.length;
  }
  
  return normalized;
}

// ═══ PHASE 5: BUILD GRAPH ═══
function buildGraph(allClaims, allEntities, allTopics, files) {
  if (!fs.existsSync(GRAPH_DIR)) fs.mkdirSync(GRAPH_DIR, { recursive: true });
  
  let graph;
  if (fs.existsSync(GRAPH_FILE)) {
    graph = JSON.parse(fs.readFileSync(GRAPH_FILE, 'utf8'));
  } else {
    graph = { _meta: {version:'1.0',created:new Date().toISOString().split('T')[0]}, reports:{}, claims:{}, topics:{}, contradictions:[], verifiedTruths:[] };
  }
  
  // Register vault as a report
  const reportId = 'rr-vault-fz-' + new Date().toISOString().split('T')[0];
  graph.reports[reportId] = {
    id: reportId,
    title: 'Obsidian Vault FZ — Full Ingest',
    date: new Date().toISOString().split('T')[0],
    author: 'vault-ingester',
    domain: 'mixed',
    admiralty: 'C2',
    confidence: 65,
    sourceCount: files.length,
    claimCount: allClaims.length,
    status: 'published'
  };
  
  // Register claims
  let claimIdx = Object.keys(graph.claims).length;
  for (const claim of allClaims) {
    const cid = `${reportId}-c${String(++claimIdx).padStart(4, '0')}`;
    graph.claims[cid] = {
      id: cid,
      reportId: reportId,
      ...claim
    };
    
    // Ensure topics exist
    for (const topicId of (claim.topics || [])) {
      if (!graph.topics[topicId]) {
        graph.topics[topicId] = {
          id: topicId,
          label: topicId.replace(/^topic-/, '').replace(/-/g, ' '),
          type: 'topic',
          domain: 'mixed',
          claimIds: [],
          reportIds: [],
          verifiedClaimCount: 0,
          contradictionCount: 0,
          lastUpdated: new Date().toISOString().split('T')[0],
          openQuestions: []
        };
      }
      const topic = graph.topics[topicId];
      if (!topic.claimIds.includes(cid)) topic.claimIds.push(cid);
      if (!topic.reportIds.includes(reportId)) topic.reportIds.push(reportId);
    }
  }
  
  // Update topic stats
  for (const [tid, topic] of Object.entries(graph.topics)) {
    const tc = topic.claimIds.map(id => graph.claims[id]).filter(Boolean);
    topic.verifiedClaimCount = tc.filter(c => c.status === 'verified').length;
    
    const sources = new Set();
    tc.forEach(c => (c.sources||[]).forEach(s => sources.add(s)));
    const srcCount = sources.size;
    
    topic.konsistenz = srcCount >= 3 ? `◉ Bestätigt durch ${srcCount} unabhängige Quellen` :
                       srcCount >= 2 ? `◉ Bestätigt durch ${srcCount} Quellen` : '△ Wenige Quellen';
    topic.konsistenzLevel = srcCount >= 3 ? 'high' : srcCount >= 2 ? 'medium' : 'low';
    
    // Executive summary from top claims
    const top = tc.filter(c => c.eija === 'E' || c.eija === 'I')
      .sort((a,b) => (b.confidence||0) - (a.confidence||0)).slice(0, 5);
    if (top.length) topic.executiveSummary = top.map(c => c.claim).join(' ');
  }
  
  graph._meta.lastUpdated = new Date().toISOString().split('T')[0];
  return graph;
}

// ═══ MAIN ═══
const args = process.argv.slice(2);
const vaultPath = args.find(a => !a.startsWith('-'));
const dryRun = args.includes('--dry-run');
const limitArg = args.indexOf('--limit');
const limit = limitArg >= 0 ? parseInt(args[limitArg + 1]) : Infinity;

if (!vaultPath) {
  console.log('Usage: node ingest-vault.js <vault-path> [--dry-run] [--limit N]');
  process.exit(1);
}

console.log(`═══ VAULT INGESTER v1.0 ═══`);
console.log(`Vault: ${vaultPath}`);

// Phase 1: Crawl
console.log(`\n── Phase 1: CRAWL ──`);
const allFiles = crawlVault(vaultPath);
console.log(`Found: ${allFiles.length} markdown files`);

// Phase 2: Classify
console.log(`\n── Phase 2: CLASSIFY ──`);
const classified = {};
allFiles.forEach(f => {
  const type = classifyFile(f);
  if (!classified[type]) classified[type] = [];
  classified[type].push(f);
});
Object.entries(classified).sort((a,b) => b[1].length - a[1].length).forEach(([type, files]) => {
  console.log(`  ${type}: ${files.length} files (${Math.round(files.reduce((s,f) => s+f.size, 0)/1024)}KB)`);
});

// Filter out junk
const processable = allFiles.filter(f => classifyFile(f) !== 'junk').slice(0, limit);
console.log(`Processable: ${processable.length} files`);

// Phase 3: Extract
console.log(`\n── Phase 3: EXTRACT ──`);
let totalClaims = [];
let totalEntities = {};
let totalTopics = new Set();
let processed = 0;
let errors = 0;

for (const file of processable) {
  try {
    const content = fs.readFileSync(file.path, 'utf8');
    const result = extractFromMarkdown(content, file);
    
    totalClaims.push(...result.claims);
    result.entities.forEach(e => {
      if (!totalEntities[e]) totalEntities[e] = [];
      totalEntities[e].push(file.relativePath);
    });
    result.topics.forEach(t => totalTopics.add(t));
    processed++;
    
    if (result.claims.length > 0 && processed <= 10) {
      console.log(`  ${file.relativePath}: ${result.claims.length} claims, ${result.entities.length} entities`);
    }
  } catch(e) {
    errors++;
  }
}

console.log(`\nProcessed: ${processed}/${processable.length} files (${errors} errors)`);
console.log(`Claims: ${totalClaims.length}`);
console.log(`Entities: ${Object.keys(totalEntities).length}`);
console.log(`Topics: ${totalTopics.size}`);

// EIJA distribution
const eijaDist = {E:0,I:0,J:0,A:0};
totalClaims.forEach(c => { if(eijaDist[c.eija]!==undefined) eijaDist[c.eija]++; });
console.log(`EIJA: E=${eijaDist.E} I=${eijaDist.I} J=${eijaDist.J} A=${eijaDist.A}`);

// Phase 4: Resolve entities
console.log(`\n── Phase 4: RESOLVE ──`);
const resolved = resolveEntities(totalEntities);
const topEntities = Object.entries(resolved)
  .sort((a,b) => b[1].count - a[1].count)
  .slice(0, 20);
console.log(`Top entities:`);
topEntities.forEach(([key, data]) => {
  console.log(`  ${data.canonical} — ${data.files.size} files`);
});

// Phase 5: Build graph
if (!dryRun) {
  console.log(`\n── Phase 5: BUILD GRAPH ──`);
  const graph = buildGraph(totalClaims, totalEntities, totalTopics, processable);
  fs.writeFileSync(GRAPH_FILE, JSON.stringify(graph, null, 2));
  
  console.log(`Graph saved.`);
  console.log(`Total reports: ${Object.keys(graph.reports).length}`);
  console.log(`Total claims: ${Object.keys(graph.claims).length}`);
  console.log(`Total topics: ${Object.keys(graph.topics).length}`);
  console.log(`Verified truths: ${graph.verifiedTruths.length}`);
} else {
  console.log(`\n── DRY RUN — not saving ──`);
}

console.log(`\n═══ DONE ═══`);
