#!/usr/bin/env node
/**
 * Signal Ingest Pipeline v1.0
 * 
 * Fetches RSS/Atom feeds from sources.json, extracts signals,
 * maps to taxonomy topics, detects influence on existing claims,
 * and generates predictions from signal clusters.
 *
 * Usage:
 *   node ingest-signals.js              # Fetch all active RSS sources
 *   node ingest-signals.js --source X   # Fetch specific source id
 *   node ingest-signals.js --dry-run    # Preview without saving
 *   node ingest-signals.js --seed       # Seed from existing source headlines
 */

const fs = require('fs');
const path = require('path');

const SOURCES_FILE = path.join(__dirname, 'sources.json');
const SIGNALS_FILE = path.join(__dirname, 'graph/signals.json');
const GRAPH_FILE = path.join(__dirname, 'graph/knowledge-graph.json');
const TAX_FILE = path.join(__dirname, 'taxonomy.json');
const DOSSIERS_FILE = path.join(__dirname, 'graph/topic-dossiers.json');

function load(f) { try { return JSON.parse(fs.readFileSync(f, 'utf8')); } catch { return null; } }
function save(f, d) { fs.writeFileSync(f, JSON.stringify(d, null, 2), 'utf8'); }

const SOURCES = load(SOURCES_FILE);
const GRAPH = load(GRAPH_FILE);
const TAX = load(TAX_FILE);
const DOSSIERS = load(DOSSIERS_FILE);

// ═══ KEYWORD → TOPIC MAP ═══
// Two-tier: STRONG keywords (multi-word phrases, domain-specific) and WEAK (single generic words)
function buildTopicKeywords() {
  const strong = {}; // phrase → Set<topicId>  (worth 3 points)
  const weak = {};   // single word → Set<topicId> (worth 1 point)
  
  function walk(node) {
    const id = node.id;
    const label = (node.label || '').toLowerCase();
    
    // STRONG: full label as phrase (if >1 word)
    const labelWords = label.split(/[\s\/&()+,]+/).filter(w => w.length > 2);
    if (labelWords.length >= 2) {
      const phrase = labelWords.join(' ');
      if (!strong[phrase]) strong[phrase] = new Set();
      strong[phrase].add(id);
    }
    
    // STRONG: 2-word combos from label
    for (let i = 0; i < labelWords.length - 1; i++) {
      const bigram = labelWords[i] + ' ' + labelWords[i + 1];
      if (!strong[bigram]) strong[bigram] = new Set();
      strong[bigram].add(id);
    }
    
    // WEAK: individual words (only if domain-specific, not generic)
    labelWords.forEach(kw => {
      if (AMBIGUOUS_WORDS.has(kw)) return; // Skip words too generic for single-word matching
      if (!weak[kw]) weak[kw] = new Set();
      weak[kw].add(id);
    });
    
    (node.children || []).forEach(walk);
  }
  (TAX.domains || []).forEach(walk);
  return { strong, weak };
}

// Words that are TOO GENERIC for single-word topic matching
// These only count when part of a phrase match
const AMBIGUOUS_WORDS = new Set([
  'use', 'tool', 'function', 'calling', 'engineering', 'design', 'system', 'systems',
  'model', 'models', 'patterns', 'pattern', 'analysis', 'data', 'value', 'based',
  'building', 'build', 'search', 'planning', 'control', 'training', 'learning',
  'network', 'effects', 'world', 'simulation', 'quality', 'standards', 'methods',
  'reach', 'content', 'community', 'pricing', 'conversion', 'deployment', 'layer',
  'resolution', 'linking', 'extraction', 'construction', 'visualization',
  'framework', 'frameworks', 'protocol', 'principles', 'expressions',
  'shot', 'context', 'window', 'management', 'protection', 'act',
  'documents', 'questions', 'ideas', 'culture', 'architecture',
  'services', 'product', 'pivot', 'margin', 'economics', 'dynamics',
  'adoption', 'collaboration', 'loops', 'decay', 'consolidation',
  'critique', 'reflection', 'self', 'bias', 'fairness', 'transparency',
  'regulation', 'responsible', 'governance', 'safety', 'advisory',
  'commoditization', 'monitoring', 'landscape', 'intelligence',
  'enterprise', 'human', 'buy', 'pitch', 'deck', 'growth', 'expand', 'land'
]);

// ═══ STOPWORDS (skip entirely) ═══
const STOPS = new Set([
  'the','and','for','with','from','that','this','are','was','were','has','have',
  'will','would','could','into','about','new','how','why','what','can','its',
  'der','die','das','und','oder','ein','eine','ist','sind','mit','von','für',
  'auf','bei','als','nach','zum','zur','den','dem','des','sich','werden','wird'
]);

const TOPIC_KW = buildTopicKeywords();

// ═══ ENTITY → TOPIC BOOSTERS ═══
// Companies/products that clearly map to specific topics (2 points each)
const ENTITY_BOOSTERS = {
  'anthropic': ['t-alignment', 't-llm-foundations'],
  'claude': ['t-llm-foundations'],
  'openai': ['t-llm-foundations'],
  'gpt': ['t-llm-foundations'],
  'gpt-5': ['t-llm-foundations', 't-reasoning'],
  'chatgpt': ['t-llm-foundations'],
  'codex': ['t-tool-use', 'd-agent-systems'],
  'palantir': ['d-palantir'],
  'gotham': ['d-palantir', 't-palantir-gotham'],
  'foundry': ['d-palantir'],
  'aip': ['d-palantir', 't-oag'],
  'maven': ['d-palantir', 't-palantir-gotham'],
  'gemini': ['t-llm-foundations'],
  'llama': ['t-llm-foundations'],
  'mistral': ['t-llm-foundations'],
  'pentagon': ['t-market-dynamics', 't-alignment'],
  'defense': ['t-market-dynamics'],
  'defence': ['t-market-dynamics'],
  'enterprise': ['t-enterprise-ai'],
  'saas': ['t-market-dynamics', 't-services-to-product'],
  'revenue': ['t-market-dynamics'],
  'funding': ['t-market-dynamics'],
  'valuation': ['t-market-dynamics'],
  'vulnerability': ['t-alignment'],
  'vulnerabilities': ['t-alignment'],
  'security': ['t-alignment'],
  'agent': ['d-agent-systems'],
  'agents': ['d-agent-systems'],
  'agentic': ['d-agent-systems'],
  'rag': ['t-rag'],
  'ontology': ['t-ontology'],
  'knowledge graph': ['t-knowledge-graphs'],
};

// ═══ TOPIC CLASSIFIER (v3: Source-first, Palantir Foundry pattern) ═══
// 
// Design rationale (Palantir G-Cloud 14 Service Definition, Section 1.2):
// "Integrates and models data into a single, cohesive data asset."
// Classification is a SCHEMA problem, not a text problem.
// 
// Priority order:
// 1. SOURCE-LEVEL: Source config defines default topics (Foundry Transform equivalent)
// 2. PHRASE-MATCH: Multi-word domain phrases in text (high confidence)
// 3. ENTITY-BOOST: Known entities (companies, products) → topic mapping
// 4. WEAK-WORD: Single domain-specific words (low confidence, last resort)
//
// Sources:
// - Nabeel Qureshi (nabeelqu.co/palantir): "Classification is a schema problem"
// - Ted Mabrey (tedmabrey.substack.com): FDE model = human-configured pipelines
// - Palantir OAG Blog: Structured ontology > raw text classification

function classifyToTopics(text, sourceId) {
  const lower = text.toLowerCase();
  const scores = {};
  let method = 'none';
  
  // ═══ PASS 0: SOURCE-LEVEL CLASSIFICATION (Palantir Foundry Transform pattern) ═══
  // The source config tells us what topics this feed covers.
  // This is the most reliable signal — human-configured, not inferred.
  const src = (SOURCES.sources || []).find(s => s.id === sourceId);
  if (src && src.defaultTopics && src.defaultTopics.length) {
    src.defaultTopics.forEach(tid => { scores[tid] = (scores[tid] || 0) + 2; });
    method = 'source-config';
  }
  
  // ═══ PASS 1: STRONG phrase matches (3 points) ═══
  Object.entries(TOPIC_KW.strong).forEach(([phrase, topicSet]) => {
    if (lower.includes(phrase)) {
      topicSet.forEach(tid => { scores[tid] = (scores[tid] || 0) + 3; });
      if (method === 'none' || method === 'source-config') method = 'phrase+source';
    }
  });
  
  // ═══ PASS 1.5: ENTITY BOOSTERS (2 points) ═══
  Object.entries(ENTITY_BOOSTERS).forEach(([entity, topics]) => {
    const regex = new RegExp('\\b' + entity.replace(/[.*+?^${}()|[\]\\]/g, '\\$&') + '\\b', 'i');
    if (regex.test(lower)) {
      topics.forEach(tid => { scores[tid] = (scores[tid] || 0) + 2; });
    }
  });
  
  // ═══ PASS 2: WEAK single-word matches (1 point) ═══
  Object.entries(TOPIC_KW.weak).forEach(([kw, topicSet]) => {
    if (STOPS.has(kw)) return;
    const regex = new RegExp('\\b' + kw.replace(/[.*+?^${}()|[\]\\]/g, '\\$&') + '\\b', 'i');
    if (regex.test(lower)) {
      topicSet.forEach(tid => { scores[tid] = (scores[tid] || 0) + 1; });
    }
  });
  
  // ═══ THRESHOLD: minimum 2 points to classify ═══
  // Source-default (2pt) + anything = classified
  // Phrase match alone (3pt) = classified
  // Entity boost alone (2pt) = classified
  // Single weak word (1pt) = NOT classified (prevents garbage)
  const entries = Object.entries(scores).sort((a, b) => b[1] - a[1]);
  const results = [];
  
  entries.forEach(([tid, score]) => {
    if (score >= 2) {
      results.push(tid);
    } else if (score === 1 && results.length === 0) {
      results.push(tid);
    }
  });
  
  return { topics: results.slice(0, 3), method };
}

// ═══ ADMIRALTY SCORING (from AgentTrust) ═══
const ADMIRALTY_RELIABILITY = { A: 1.0, B: 0.8, C: 0.6, D: 0.4, E: 0.2 };
const ADMIRALTY_CREDIBILITY = { 1: 1.0, 2: 0.85, 3: 0.7, 4: 0.5 };

function computeTrustScore(sourceTrustFloor, matchScore, sourceCount) {
  // Parse Admiralty code (e.g. "A1" → reliability A, credibility 1)
  const rel = ADMIRALTY_RELIABILITY[(sourceTrustFloor || 'B3')[0]] || 0.6;
  const cred = ADMIRALTY_CREDIBILITY[(sourceTrustFloor || 'B3')[1]] || 0.7;
  const admiraltyBase = Math.round((rel * 50 + cred * 50));
  
  // Match score bonus (how well signal matches existing claims)
  const matchBonus = Math.min(matchScore * 0.15, 10);
  
  // Multi-source bonus (from AgentTrust: sourceCount > 1 = +4 per extra)
  const sourceBonus = Math.min((sourceCount - 1) * 4, 12);
  
  return Math.min(99, Math.round(admiraltyBase + matchBonus + sourceBonus));
}

function computeRiskLevel(confidence, hasContradiction, sourceCount) {
  // From Beipackzettel: high if <50 or ≥3 risks, low if ≥80 and no risks
  if (confidence < 50 || hasContradiction) return 'high';
  if (confidence >= 80 && sourceCount >= 2) return 'low';
  return 'medium';
}

// ═══ SO-WHAT GENERATOR ═══
// Palantir-style: "Why does this matter?" — must summarize CONTENT, not category.
// Rule: Headline = What happened. So-What = Why it matters for our knowledge graph.
function generateSoWhat(headline, summary, influences, topics) {
  const fullText = (headline + ' ' + summary).toLowerCase();
  const parts = [];
  
  // STEP 1: What does the signal SAY? (extract core insight from content)
  // Use the headline as the primary statement — it IS the signal content
  const insight = extractInsight(headline, summary);
  if (insight) parts.push(insight);
  
  // STEP 2: How does it affect our existing knowledge?
  const strengthened = influences.filter(i => i.direction === 'strengthens' && i.claimText);
  const weakened = influences.filter(i => i.direction === 'weakens' && i.claimText);
  
  if (strengthened.length) {
    parts.push('Bestätigt bestehenden Claim: "' + strengthened[0].claimText.substring(0, 50) + '…"');
  }
  if (weakened.length) {
    parts.push('⚠ Widerspricht: "' + weakened[0].claimText.substring(0, 50) + '…" — Prüfung nötig');
  }
  
  // STEP 3: What should we DO? (actionable implication)
  if (weakened.length) {
    parts.push('Handlung: Claims re-evaluieren');
  } else if (strengthened.length && strengthened[0].matchScore >= 50) {
    parts.push('Trust-Score für betroffene Claims erhöhen');
  } else {
    // Novel signal — what gap does it address?
    const gapTopics = topics.filter(tid => {
      const d = DOSSIERS ? DOSSIERS[tid] : null;
      return d && d.isGap;
    });
    if (gapTopics.length) {
      const d = DOSSIERS[gapTopics[0]];
      parts.push('Adressiert Knowledge Gap: "' + d.label + '" — Research-Chance');
    }
  }
  
  return parts.length ? parts.join('. ') + '.' : null;
}

// Extract the actual insight from headline + summary
function extractInsight(headline, summary) {
  // Remove quotes/attribution noise
  let clean = headline.replace(/^Quoting\s+/i, '').replace(/^RT:?\s+/i, '');
  
  // If summary adds real info beyond headline, append key part
  const sumLower = (summary || '').toLowerCase();
  const headLower = clean.toLowerCase();
  
  // Extract named entities / key phrases from summary that aren't in headline
  const sumWords = sumLower.split(/\s+/).filter(w => w.length > 4);
  const headWords = new Set(headLower.split(/\s+/));
  const newInfo = sumWords.filter(w => !headWords.has(w) && !STOPS.has(w));
  
  // If headline is very short or a quote, try to get substance from summary
  if (clean.length < 30 && summary && summary.length > clean.length) {
    // Use first sentence of summary
    const firstSentence = summary.replace(/<[^>]+>/g, '').split(/[.!?]/)[0];
    if (firstSentence && firstSentence.length > 20) {
      return firstSentence.substring(0, 120).trim();
    }
  }
  
  // Headline IS the insight — return it cleaned up
  if (clean.length > 15) {
    return clean.substring(0, 120);
  }
  
  return null;
}

// ═══ BEIPACKZETTEL GENERATOR ═══
// From agenttrust/core/beipackzettel.py — adapted for signals
function generateBeipackzettel(src, influences, topics, matchScore) {
  const sourceCount = 1; // RSS = single source per signal
  const trustScore = computeTrustScore(src.trustFloor, matchScore, sourceCount);
  const hasContradiction = influences.some(i => i.direction === 'weakens');
  const riskLevel = computeRiskLevel(trustScore, hasContradiction, sourceCount);
  
  const uncertainties = [];
  const risks = [];
  const notChecked = [];
  
  // Assess uncertainties
  if (sourceCount < 2) uncertainties.push('Einzelquelle — keine unabhängige Bestätigung');
  if (matchScore < 30) uncertainties.push('Schwache Übereinstimmung mit existierendem Wissen');
  if (hasContradiction) uncertainties.push('Widerspricht existierendem Claim');
  
  // Assess risks
  if (riskLevel === 'high') risks.push('Hohe Unsicherheit — manuelle Prüfung empfohlen');
  if (src.trustFloor && src.trustFloor[0] >= 'C') risks.push('Quelle mit niedrigem Vertrauenslevel');
  
  // Not checked
  notChecked.push('Keine Gegenrecherche durchgeführt');
  if (influences.some(i => i.direction === 'new')) notChecked.push('Kein Abgleich mit bestehender Evidenz möglich');
  
  // Trust level (from AgentTrust TrustLevel enum)
  let trustLevel;
  if (trustScore >= 81) trustLevel = 'autonomous';
  else if (trustScore >= 61) trustLevel = 'spot_check';
  else if (trustScore >= 31) trustLevel = 'supervised';
  else trustLevel = 'untrusted';
  
  return {
    confidence: trustScore,
    admiralty: src.trustFloor || 'B3',
    riskLevel,
    trustLevel,
    sourceCount,
    uncertainties,
    risks,
    notChecked,
    isGrounded: !!src.url,
    calibrationNote: trustScore >= 80 
      ? 'Hohe Quellen-Reliabilität. Trotzdem Einzelquelle.'
      : trustScore >= 60 
        ? 'Mittlere Confidence. Kreuzvalidierung empfohlen.'
        : 'Niedrige Confidence. Nicht ohne Prüfung verwenden.'
  };
}

// ═══ INFLUENCE DETECTOR ═══
// Palantir-style: structured analysis, not just keyword matching
function detectInfluence(signalText, topics) {
  const influences = [];
  const claims = Object.values(GRAPH.claims || {});
  const lower = signalText.toLowerCase();
  
  topics.forEach(tid => {
    const topicClaims = claims.filter(c => (c.topics || []).includes(tid));
    
    let bestMatch = null;
    let bestScore = 0;
    
    topicClaims.forEach(c => {
      const claimWords = (c.claim || '').toLowerCase().split(/\s+/).filter(w => w.length > 3 && !STOPS.has(w));
      const hits = claimWords.filter(w => lower.includes(w)).length;
      const score = claimWords.length > 0 ? hits / claimWords.length : 0;
      if (score > bestScore && score > 0.2) {
        bestScore = score;
        bestMatch = c;
      }
    });
    
    if (bestMatch) {
      // Sentiment analysis with negation handling
      const negWords = ['not','no','fail','wrong','decline','drop','fall','gegen','nicht','kein','problem','risk','ban','stop','lose','cut','end','halt','block'];
      const posWords = ['confirm','prove','grow','increase','success','improve','launch','release','announce','new','achieve','expand','gain','win','boost','lead'];
      const hasNeg = negWords.some(w => lower.includes(w));
      const hasPos = posWords.some(w => lower.includes(w));
      const direction = hasNeg && !hasPos ? 'weakens' : 'strengthens';
      
      // Reasoning trace (Palantir ACH-style)
      const reasoning = direction === 'strengthens'
        ? `Signal unterstützt: "${bestMatch.claim.substring(0, 50)}…" (${Math.round(bestScore * 100)}% Übereinstimmung)`
        : `Signal widerspricht: "${bestMatch.claim.substring(0, 50)}…" — Gegenrecherche nötig`;
      
      influences.push({
        topicId: tid,
        direction,
        claimId: bestMatch.id,
        claimText: bestMatch.claim.substring(0, 80),
        claimTrust: (bestMatch.trustScore || {}).score || 50,
        matchScore: Math.round(bestScore * 100),
        reasoning
      });
    } else {
      const dossier = DOSSIERS ? DOSSIERS[tid] : null;
      influences.push({
        topicId: tid,
        direction: 'new',
        claimId: null,
        claimText: null,
        claimTrust: 0,
        matchScore: 0,
        reasoning: dossier && dossier.isGap 
          ? `Neues Signal für Gap-Topic "${dossier.label}" — Research-Chance`
          : `Kein direkter Claim-Match. Möglicherweise neuer Aspekt.`
      });
    }
  });
  
  return influences;
}

// ═══ RSS/ATOM PARSER ═══
// Lightweight XML extraction without dependencies
function parseRSSItems(xml) {
  const items = [];
  
  // Try RSS <item> first
  const rssItems = xml.match(/<item[^>]*>([\s\S]*?)<\/item>/gi) || [];
  rssItems.forEach(itemXml => {
    const title = extractTag(itemXml, 'title');
    const link = extractTag(itemXml, 'link') || extractAttr(itemXml, 'link', 'href');
    const desc = extractTag(itemXml, 'description') || extractTag(itemXml, 'content:encoded') || '';
    const pubDate = extractTag(itemXml, 'pubDate') || extractTag(itemXml, 'dc:date') || '';
    
    if (title) items.push({ title: cleanHtml(title), url: cleanHtml(link || ''), summary: cleanHtml(desc).substring(0, 300), date: pubDate });
  });
  
  // Try Atom <entry>
  if (items.length === 0) {
    const atomEntries = xml.match(/<entry[^>]*>([\s\S]*?)<\/entry>/gi) || [];
    atomEntries.forEach(entryXml => {
      const title = extractTag(entryXml, 'title');
      const link = extractAttr(entryXml, 'link', 'href') || extractTag(entryXml, 'link');
      const summary = extractTag(entryXml, 'summary') || extractTag(entryXml, 'content') || '';
      const updated = extractTag(entryXml, 'updated') || extractTag(entryXml, 'published') || '';
      
      if (title) items.push({ title: cleanHtml(title), url: cleanHtml(link || ''), summary: cleanHtml(summary).substring(0, 300), date: updated });
    });
  }
  
  return items;
}

function extractTag(xml, tag) {
  // Handle CDATA
  const cdataMatch = xml.match(new RegExp('<' + tag + '[^>]*><!\\[CDATA\\[([\\s\\S]*?)\\]\\]></' + tag + '>', 'i'));
  if (cdataMatch) return cdataMatch[1];
  const match = xml.match(new RegExp('<' + tag + '[^>]*>([\\s\\S]*?)</' + tag + '>', 'i'));
  return match ? match[1].trim() : null;
}

function extractAttr(xml, tag, attr) {
  const match = xml.match(new RegExp('<' + tag + '[^>]*' + attr + '=["\']([^"\']*)["\']', 'i'));
  return match ? match[1] : null;
}

function cleanHtml(str) {
  return (str || '')
    .replace(/<[^>]+>/g, '')
    .replace(/&amp;/g, '&').replace(/&lt;/g, '<').replace(/&gt;/g, '>').replace(/&quot;/g, '"').replace(/&#39;/g, "'")
    .replace(/&#8217;/g, "'").replace(/&#8216;/g, "'").replace(/&#8220;/g, '"').replace(/&#8221;/g, '"')
    .replace(/&#8211;/g, '–').replace(/&#8212;/g, '—').replace(/&#8230;/g, '…')
    .replace(/&#\d+;/g, '') // catch remaining numeric entities
    .replace(/\s+/g, ' ')
    .trim();
}

// ═══ RESEARCH GAP DETECTOR ═══
function findResearchGaps(topics) {
  const gaps = [];
  topics.forEach(tid => {
    const dossier = DOSSIERS ? DOSSIERS[tid] : null;
    if (!dossier) return;
    
    // Gap topic = no claims
    if (dossier.isGap) {
      gaps.push({ topicId: tid, question: 'Topic "' + dossier.label + '" has no research data yet' });
    }
    // Low confidence
    else if (dossier.confidence && dossier.confidence.score < 60) {
      gaps.push({ topicId: tid, question: dossier.label + ': Confidence ' + dossier.confidence.score + '% — needs more sources' });
    }
    // Open questions
    (dossier.openQuestions || []).slice(0, 1).forEach(oq => {
      gaps.push({ topicId: tid, question: oq.text });
    });
  });
  return gaps.slice(0, 3);
}

// ═══ PREDICTION ENGINE ═══
// Detect trends: ≥3 signals in same direction for same topic within 30 days
function generatePredictions(signals) {
  const predictions = [];
  const now = Date.now();
  const thirtyDays = 30 * 24 * 60 * 60 * 1000;
  
  // Group recent signals by topic
  const topicSignals = {};
  signals.filter(s => {
    const ts = new Date(s.timestamp).getTime();
    return now - ts < thirtyDays;
  }).forEach(s => {
    (s.influences || []).forEach(inf => {
      const key = inf.topicId + ':' + inf.direction;
      if (!topicSignals[key]) topicSignals[key] = [];
      topicSignals[key].push(s);
    });
  });
  
  // ≥3 signals same direction = trend → prediction (Palantir I&W style)
  Object.entries(topicSignals).forEach(([key, sigs]) => {
    if (sigs.length < 3) return;
    const [topicId, direction] = key.split(':');
    const dossier = DOSSIERS ? DOSSIERS[topicId] : null;
    const topicLabel = dossier ? dossier.label : topicId;
    
    const predId = 'pred-' + topicId.replace(/^t-|^topic-/, '') + '-' + new Date().toISOString().slice(0, 7);
    
    // Unique source count (independence check)
    const uniqueSources = new Set(sigs.map(s => s.sourceId)).size;
    const sourceBonus = Math.min((uniqueSources - 1) * 5, 15);
    
    // AgentTrust: matchScore determines signal quality, not just count
    // avgMatch < 10 → signals don't actually match topic claims → heavy penalty
    const avgMatchRaw = sigs.reduce((sum, s) => {
      const inf = (s.influences || []).find(i => i.topicId === topicId);
      return sum + (inf ? inf.matchScore : 0);
    }, 0) / sigs.length;
    // AgentTrust calibration: matchScore=0 means NO claim alignment → hard cap
    const matchMultiplier = avgMatchRaw >= 50 ? 1.0 : avgMatchRaw >= 30 ? 0.7 : avgMatchRaw >= 10 ? 0.5 : 0.25;
    const matchCap = avgMatchRaw >= 50 ? 90 : avgMatchRaw >= 30 ? 70 : avgMatchRaw >= 10 ? 55 : 40;
    
    let text, confidence, managementSummary, recommendedAction;
    if (direction === 'strengthens') {
      confidence = Math.round(Math.min(50 + sigs.length * 8 * matchMultiplier + sourceBonus, matchCap));
      text = topicLabel + ': Trend bestätigt sich — ' + sigs.length + ' Signale aus ' + uniqueSources + ' unabhängigen Quellen';
      managementSummary = 'Bestehende Claims zu "' + topicLabel + '" werden durch aktuelle Signale gestärkt. '
        + uniqueSources + ' unabhängige Quellen zeigen konsistente Richtung. '
        + 'Confidence ' + confidence + '% — ' + (confidence >= 75 ? 'handlungsrelevant.' : 'beobachten.');
      recommendedAction = confidence >= 75
        ? { type: 'act', label: 'Claims als bestätigt markieren', topicId, prompt: null }
        : { type: 'monitor', label: 'Trend beobachten', topicId, prompt: null };
    } else if (direction === 'weakens') {
      confidence = Math.round(Math.min(40 + sigs.length * 8 * matchMultiplier + sourceBonus, Math.min(80, matchCap)));
      text = topicLabel + ': Gegentrend — ' + sigs.length + ' widersprüchliche Signale';
      managementSummary = '⚠️ Bestehende Claims zu "' + topicLabel + '" werden in Frage gestellt. '
        + sigs.length + ' Signale deuten auf Richtungsänderung.';
      recommendedAction = {
        type: 'review-claims',
        label: 'Claims prüfen & Trust-Score anpassen',
        topicId,
        prompt: 'Überprüfe Claims zu "' + topicLabel + '". ' + sigs.length + ' Signale widersprechen bestehenden Annahmen. '
          + 'Prüfe: Sind die Claims noch gültig? Quellen aktuell? Trust-Score anpassen?'
      };
    } else {
      confidence = Math.round(Math.min(30 + sigs.length * 8 * matchMultiplier + sourceBonus, Math.min(75, matchCap)));
      text = topicLabel + ': Neue Entwicklung — ' + sigs.length + ' Signale zu bisher unbekanntem Aspekt';
      const topHeadlines = sigs.slice(0, 5).map(s => '- ' + s.headline.substring(0, 80)).join('\n');
      managementSummary = 'Mehrere Quellen berichten über neue Entwicklungen in "' + topicLabel + '". '
        + 'Keine bestehenden Claims betroffen. Knowledge Gap identifiziert.';
      recommendedAction = {
        type: 'deep-research',
        label: 'Deep Research starten',
        topicId,
        prompt: 'Deep Research: ' + topicLabel + '\n\n'
          + 'Knowledge Gap: ' + sigs.length + ' Signale aus ' + uniqueSources + ' Quellen, aber kein Claim-Match.\n\n'
          + 'Top-Signale:\n' + topHeadlines + '\n\n'
          + 'Aufgabe:\n'
          + '1. Was ist die Kernentwicklung?\n'
          + '2. Welche neuen Claims sollten angelegt werden?\n'
          + '3. Welche bestehenden Topics sind betroffen?\n'
          + '4. Confidence-Einschätzung mit Quellen'
      };
    }
    
    // Supporting evidence (top 3 signals with reasoning)
    const supportingEvidence = sigs.slice(0, 5).map(s => ({
      signalId: s.id,
      headline: s.headline.substring(0, 80),
      source: s.sourceLabel,
      timestamp: s.timestamp,
      soWhat: s.soWhat || null,
      influence: (s.influences || []).find(i => i.topicId === topicId) || null
    }));
    
    // Beipackzettel for prediction (reuse avgMatchRaw from above)
    const avgMatch = avgMatchRaw;
    
    const predBpz = {
      confidence,
      riskLevel: confidence >= 75 ? 'low' : confidence >= 50 ? 'medium' : 'high',
      sourceCount: uniqueSources,
      signalCount: sigs.length,
      avgMatchScore: Math.round(avgMatch),
      uncertainties: [],
      indicators: [],
      competingHypotheses: []
    };
    
    // Uncertainties
    if (uniqueSources < 3) predBpz.uncertainties.push('Weniger als 3 unabhängige Quellen');
    if (avgMatch < 30) predBpz.uncertainties.push('Schwache semantische Übereinstimmung mit existierenden Claims');
    if (sigs.length < 5) predBpz.uncertainties.push('Kleine Signalbasis — Trend könnte Rauschen sein');
    
    // Indicators (Palantir I&W: what to watch for confirmation)
    predBpz.indicators.push('Weitere ' + (direction === 'strengthens' ? 'bestätigende' : 'widersprechende') + ' Signale aus neuen Quellen');
    if (dossier && dossier.openQuestions && dossier.openQuestions.length) {
      predBpz.indicators.push('Offene Frage beantwortet: ' + dossier.openQuestions[0].text.substring(0, 60));
    }
    predBpz.indicators.push('Primärquelle veröffentlicht Daten/Paper zum Thema');
    
    // Competing hypotheses (ACH-lite)
    if (direction === 'strengthens') {
      predBpz.competingHypotheses.push({ h: 'Echter Trend — Feld konvergiert', support: sigs.length, against: 0 });
      predBpz.competingHypotheses.push({ h: 'Echo-Effekt — gleiche Primärquelle wird wiederholt', support: 0, against: uniqueSources });
    } else if (direction === 'weakens') {
      predBpz.competingHypotheses.push({ h: 'Paradigmenwechsel — alte Claims veraltet', support: sigs.length, against: 0 });
      predBpz.competingHypotheses.push({ h: 'Temporärer Gegenwind — Grundthese bleibt', support: 0, against: 0 });
    }
    
    // Raw confidence = what signal count alone would give (without matchScore penalty)
    var rawConf;
    if (direction === 'strengthens') rawConf = Math.min(50 + sigs.length * 8 + sourceBonus, 90);
    else if (direction === 'weakens') rawConf = Math.min(40 + sigs.length * 8 + sourceBonus, 80);
    else rawConf = Math.min(30 + sigs.length * 8 + sourceBonus, 75);

    predictions.push({
      id: predId,
      text,
      managementSummary,
      confidence,
      rawConfidence: rawConf,
      matchQuality: Math.round(avgMatchRaw),
      horizon: '90d',
      createdAt: new Date().toISOString(),
      basis: sigs.map(s => s.id),
      supportingEvidence,
      beipackzettel: predBpz,
      recommendedAction,
      topicId,
      direction,
      signalCount: sigs.length,
      uniqueSources,
      status: 'open'
    });
  });
  
  return predictions;
}

// ═══ TREND DETECTOR ═══
function detectTrends(signals) {
  const trends = [];
  const now = Date.now();
  const sevenDays = 7 * 24 * 60 * 60 * 1000;
  
  // Count signals per topic in last 7 days
  const topicActivity = {};
  signals.filter(s => now - new Date(s.timestamp).getTime() < sevenDays).forEach(s => {
    (s.topics || []).forEach(tid => {
      topicActivity[tid] = (topicActivity[tid] || 0) + 1;
    });
  });
  
  // Topics with ≥2 signals in 7 days = trending
  Object.entries(topicActivity)
    .filter(([, count]) => count >= 2)
    .sort((a, b) => b[1] - a[1])
    .slice(0, 5)
    .forEach(([tid, count]) => {
      const dossier = DOSSIERS ? DOSSIERS[tid] : null;
      trends.push({
        topicId: tid,
        label: dossier ? dossier.label : tid,
        signalCount: count,
        period: '7d'
      });
    });
  
  return trends;
}

// ═══ MAIN INGEST ═══
async function ingest(opts = {}) {
  const { sourceFilter, dryRun, seed } = opts;
  const signalData = load(SIGNALS_FILE) || { _meta: {}, signals: [], predictions: [], trends: [] };
  const existingUrls = new Set(signalData.signals.map(s => s.url));
  const existingIds = new Set(signalData.signals.map(s => s.id));
  
  const sources = (SOURCES.sources || []).filter(s => {
    if (sourceFilter && s.id !== sourceFilter) return false;
    if (s.type !== 'rss' && !seed) return false;
    if (s.status !== 'active') return false;
    return true;
  });
  
  let newSignals = [];
  let counter = signalData.signals.length;
  
  if (seed) {
    // Seed mode: create signals from existing lastHeadline data in sources
    console.log('═══ SEED MODE ═══');
    (SOURCES.sources || []).filter(s => s.lastHeadline && s.status === 'active').forEach(src => {
      const text = src.lastHeadline;
      const classified = classifyToTopics(text, src.id);
      const topics = classified.topics.length ? classified.topics 
        : (src.feedsTopics && src.feedsTopics[0] !== '*' ? src.feedsTopics.slice(0, 3) : []);
      
      const signal = buildSignal(++counter, src, text, text, '', src.lastInput || new Date().toISOString().slice(0, 10), topics);
      if (!existingUrls.has(signal.url)) {
        newSignals.push(signal);
      }
    });
  } else {
    // Live RSS fetch
    console.log('═══ SIGNAL INGEST ═══');
    console.log(`Sources: ${sources.length} RSS feeds\n`);
    
    for (const src of sources) {
      if (!src.url) continue;
      console.log(`Fetching: ${src.label} (${src.url})`);
      
      try {
        const resp = await fetch(src.url, {
          headers: { 'User-Agent': 'Ainary-Research-Bot/1.0' },
          signal: AbortSignal.timeout(10000)
        });
        
        if (!resp.ok) {
          console.log(`  ✗ HTTP ${resp.status}`);
          continue;
        }
        
        const xml = await resp.text();
        const items = parseRSSItems(xml);
        console.log(`  ${items.length} items found`);
        
        // Take latest 5 items
        items.slice(0, 5).forEach(item => {
          if (existingUrls.has(item.url)) return;
          
          const text = item.title + ' ' + item.summary;
          const classified = classifyToTopics(text, src.id);
          const topics = classified.topics;
          
          const signal = buildSignal(++counter, src, item.title, item.summary, item.url, item.date, topics);
          signal._classificationMethod = classified.method; // Track for Beipackzettel
          newSignals.push(signal);
          existingUrls.add(item.url);
        });
        
      } catch (e) {
        console.log(`  ✗ ${e.message}`);
      }
    }
  }
  
  console.log(`\nNew signals: ${newSignals.length}`);
  
  if (newSignals.length === 0) {
    console.log('Nothing new to ingest.');
    return;
  }
  
  // Add to signal data
  signalData.signals = [...signalData.signals, ...newSignals];
  
  // Sort by timestamp (newest first)
  signalData.signals.sort((a, b) => new Date(b.timestamp) - new Date(a.timestamp));
  
  // Generate predictions
  signalData.predictions = generatePredictions(signalData.signals);
  
  // Detect trends
  signalData.trends = detectTrends(signalData.signals);
  
  // Update meta
  signalData._meta.updated = new Date().toISOString();
  signalData._meta.totalSignals = signalData.signals.length;
  signalData._meta.totalPredictions = signalData.predictions.length;
  signalData._meta.totalTrends = signalData.trends.length;
  
  // Generate audience briefings (Common Operating Picture)
  signalData.briefings = generateBriefings(signalData.signals, signalData.predictions, signalData.trends);
  
  // Generate D3 graph data
  generateD3Graph(signalData.signals);
  
  if (dryRun) {
    console.log('\n═══ DRY RUN — not saving ═══');
    newSignals.forEach(s => {
      console.log(`  [${s.sourceLabel}] ${s.headline}`);
      console.log(`    Topics: ${s.topics.join(', ')}`);
      console.log(`    Influences: ${s.influences.map(i => i.direction + ' ' + i.topicId).join(', ')}`);
      if (s.researchGaps.length) console.log(`    Gaps: ${s.researchGaps.map(g => g.question).join(', ')}`);
    });
  } else {
    save(SIGNALS_FILE, signalData);
    console.log(`Saved to ${SIGNALS_FILE}`);
  }
  
  // Summary
  console.log(`\n═══ SUMMARY ═══`);
  console.log(`Total signals: ${signalData.signals.length}`);
  console.log(`Predictions: ${signalData.predictions.length}`);
  console.log(`Trends: ${signalData.trends.length}`);
  
  if (signalData.trends.length) {
    console.log('\nTrending topics:');
    signalData.trends.forEach(t => console.log(`  📈 ${t.label} (${t.signalCount} signals in ${t.period})`));
  }
  if (signalData.predictions.length) {
    console.log('\nPredictions:');
    signalData.predictions.forEach(p => console.log(`  🔮 ${p.text} [${p.confidence}%]`));
  }
}

function buildSignal(num, src, headline, summary, url, dateStr, topics) {
  const id = 'sig-' + new Date().toISOString().slice(0, 10).replace(/-/g, '') + '-' + String(num).padStart(3, '0');
  const timestamp = dateStr ? new Date(dateStr).toISOString() : new Date().toISOString();
  const fullText = headline + ' ' + summary;
  
  const influences = detectInfluence(fullText, topics);
  const maxMatch = Math.max(0, ...influences.map(i => i.matchScore));
  const soWhat = generateSoWhat(headline, summary, influences, topics);
  const beipackzettel = generateBeipackzettel(src, influences, topics, maxMatch);
  const researchGaps = findResearchGaps(topics);
  
  return {
    id,
    timestamp,
    sourceId: src.id,
    sourceLabel: src.label,
    sourceTrustFloor: src.trustFloor || 'B3',
    headline,
    summary: summary.substring(0, 300),
    url: url || '',
    topics,
    soWhat,
    beipackzettel,
    influences,
    researchGaps,
    prediction: null
  };
}

// ═══ D3 GRAPH DATA GENERATOR ═══
function generateD3Graph(signals) {
  const kgPath = path.join(__dirname, 'graph', 'knowledge-graph.json');
  if (!fs.existsSync(kgPath)) return;
  const kg = JSON.parse(fs.readFileSync(kgPath, 'utf8'));
  
  const nodes = [];
  const edges = [];
  const nodeMap = new Set();
  
  // Topics
  Object.entries(kg.topics || {}).forEach(([id, t]) => {
    nodes.push({ id, type: 'topic', label: t.label, domain: t.domain, claims: (t.claimIds || []).length, verified: t.verifiedClaimCount || 0 });
    nodeMap.add(id);
  });
  
  // Claims
  Object.entries(kg.claims || {}).forEach(([id, c]) => {
    nodes.push({ id, type: 'claim', label: (c.claim || '').substring(0, 60), confidence: c.computedConfidence || c.confidence, admiralty: c.admiralty, eija: c.eija, trustScore: c.trustScore });
    nodeMap.add(id);
    (c.topics || []).forEach(tid => {
      if (nodeMap.has(tid) || (kg.topics || {})[tid]) edges.push({ source: id, target: tid, type: 'belongs_to' });
    });
    if (c.contradicts) edges.push({ source: id, target: c.contradicts, type: 'contradicts' });
  });
  
  // Reports
  Object.entries(kg.reports || {}).forEach(([id]) => {
    nodes.push({ id, type: 'report', label: id.replace(/^rr-/, '').replace(/-/g, ' ') });
  });
  
  // Signals (latest 20)
  signals.slice(0, 20).forEach(s => {
    nodes.push({ id: s.id, type: 'signal', label: (s.headline || '').substring(0, 50) });
    (s.topics || []).slice(0, 2).forEach(tid => {
      edges.push({ source: s.id, target: tid, type: 'evidences' });
    });
  });
  
  const outPath = path.join(__dirname, 'graph', 'd3-graph.json');
  fs.writeFileSync(outPath, JSON.stringify({ nodes, edges }));
  console.log(`  📊 D3 graph: ${nodes.length} nodes, ${edges.length} edges`);
}

// ═══ AUDIENCE BRIEFINGS (Common Operating Picture) ═══
// Palantir "Gist" pattern: same data, different view per audience
function generateBriefings(signals, predictions, trends) {
  const now = Date.now();
  const sevenDays = 7 * 24 * 60 * 60 * 1000;
  const recent = signals.filter(s => now - new Date(s.timestamp).getTime() < sevenDays);
  
  // Domain classification for audience mapping
  const AUDIENCE_DOMAINS = {
    founders: ['d-gtm-academic', 'd-industry-transformation', 'd-palantir', 't-market-dynamics', 't-distribution', 't-product-led', 't-land-expand', 't-services-to-product', 't-enterprise-ai', 't-value-pricing', 't-fde-model'],
    developers: ['d-agent-systems', 'd-llm-foundations', 'd-knowledge-engineering', 't-agent-architecture', 't-tool-use', 't-prompting', 't-rag', 't-reasoning', 't-memory-systems', 't-llm-foundations'],
    vcs: ['d-industry-transformation', 'd-palantir', 'd-gtm-academic', 't-market-dynamics', 't-winner-takes-all', 't-moat-analysis', 't-margin-economics', 't-palantir-financials', 't-enterprise-ai'],
    smes: ['d-industry-transformation', 't-enterprise-ai', 't-ai-deployment-patterns', 't-build-vs-buy', 't-human-ai-collaboration', 't-consulting-evolution', 't-ai-governance', 't-regulation']
  };
  
  // Count signals per audience
  function countForAudience(audienceKey) {
    const domains = new Set(AUDIENCE_DOMAINS[audienceKey]);
    return recent.filter(s => (s.topics || []).some(t => domains.has(t))).length;
  }
  
  // Get top signals for audience
  function topSignals(audienceKey, limit) {
    const domains = new Set(AUDIENCE_DOMAINS[audienceKey]);
    return recent
      .filter(s => (s.topics || []).some(t => domains.has(t)))
      .sort((a, b) => (b.beipackzettel || {}).confidence - (a.beipackzettel || {}).confidence)
      .slice(0, limit);
  }
  
  // Get relevant predictions for audience
  function relevantPredictions(audienceKey) {
    const domains = new Set(AUDIENCE_DOMAINS[audienceKey]);
    return predictions.filter(p => domains.has(p.topicId));
  }
  
  // Get trend direction
  function trendSummary(audienceKey) {
    const domains = new Set(AUDIENCE_DOMAINS[audienceKey]);
    return trends.filter(t => domains.has(t.topicId));
  }
  
  // Detect dominant themes from headlines
  function extractThemes(sigs) {
    const themes = {};
    const themeWords = {
      'security': ['security','vulnerability','breach','hack','attack','risk'],
      'regulation': ['regulation','policy','compliance','government','ban','law','eu','act'],
      'competition': ['competition','competitor','market','growth','share','versus','vs'],
      'product_launch': ['launch','release','announce','ship','deploy','new','introduce','update'],
      'research': ['research','paper','study','finding','breakthrough','model','benchmark'],
      'funding': ['funding','investment','raise','valuation','acquire','deal','ipo'],
      'adoption': ['adoption','enterprise','customer','deploy','implement','scale','usage'],
      'infrastructure': ['infrastructure','platform','api','tool','framework','sdk','open-source']
    };
    sigs.forEach(s => {
      const text = (s.headline + ' ' + (s.summary || '')).toLowerCase();
      Object.entries(themeWords).forEach(([theme, words]) => {
        if (words.some(w => text.includes(w))) {
          themes[theme] = (themes[theme] || 0) + 1;
        }
      });
    });
    return Object.entries(themes).sort((a, b) => b[1] - a[1]).slice(0, 3).map(([t, c]) => ({ theme: t, count: c }));
  }
  
  // Theme labels
  const THEME_LABELS = {
    security: 'Sicherheit & Vulnerabilities',
    regulation: 'Regulierung & Policy',
    competition: 'Wettbewerb & Marktdynamik',
    product_launch: 'Neue Produkte & Releases',
    research: 'Forschung & Durchbrüche',
    funding: 'Funding & M&A',
    adoption: 'Enterprise Adoption',
    infrastructure: 'Infrastruktur & Tools'
  };
  
  const briefings = {};
  
  // ═══ FOUNDERS BRIEFING ═══
  const fSigs = topSignals('founders', 5);
  const fPreds = relevantPredictions('founders');
  const fThemes = extractThemes(fSigs);
  const fTrends = trendSummary('founders');
  
  briefings.founders = {
    audience: 'Startup Founders',
    icon: '◉',
    question: 'Was sollte ich bauen? Wo ist die Chance?',
    signalCount: countForAudience('founders'),
    summary: buildFoundersSummary(fSigs, fPreds, fThemes, fTrends),
    topSignals: fSigs.slice(0, 3).map(s => ({ headline: s.headline, soWhat: s.soWhat, confidence: (s.beipackzettel || {}).confidence || 0 })),
    themes: fThemes.map(t => THEME_LABELS[t.theme] || t.theme),
    predictionCount: fPreds.length,
    trendDirection: fTrends.length > 0 ? 'active' : 'quiet'
  };
  
  // ═══ DEVELOPERS BRIEFING ═══
  const dSigs = topSignals('developers', 5);
  const dPreds = relevantPredictions('developers');
  const dThemes = extractThemes(dSigs);
  const dTrends = trendSummary('developers');
  
  briefings.developers = {
    audience: 'Developers & Engineers',
    icon: '◈',
    question: 'Was ändert sich technisch? Was sollte ich lernen?',
    signalCount: countForAudience('developers'),
    summary: buildDevelopersSummary(dSigs, dPreds, dThemes, dTrends),
    topSignals: dSigs.slice(0, 3).map(s => ({ headline: s.headline, soWhat: s.soWhat, confidence: (s.beipackzettel || {}).confidence || 0 })),
    themes: dThemes.map(t => THEME_LABELS[t.theme] || t.theme),
    predictionCount: dPreds.length,
    trendDirection: dTrends.length > 0 ? 'active' : 'quiet'
  };
  
  // ═══ VC BRIEFING ═══
  const vSigs = topSignals('vcs', 5);
  const vPreds = relevantPredictions('vcs');
  const vThemes = extractThemes(vSigs);
  const vTrends = trendSummary('vcs');
  
  briefings.vcs = {
    audience: 'VCs & Investors',
    icon: '○',
    question: 'Wo ist der Alpha? Was ist over/underhyped?',
    signalCount: countForAudience('vcs'),
    summary: buildVCSummary(vSigs, vPreds, vThemes, vTrends),
    topSignals: vSigs.slice(0, 3).map(s => ({ headline: s.headline, soWhat: s.soWhat, confidence: (s.beipackzettel || {}).confidence || 0 })),
    themes: vThemes.map(t => THEME_LABELS[t.theme] || t.theme),
    predictionCount: vPreds.length,
    trendDirection: vTrends.length > 0 ? 'active' : 'quiet'
  };
  
  // ═══ SME BRIEFING ═══
  const sSigs = topSignals('smes', 5);
  const sPreds = relevantPredictions('smes');
  const sThemes = extractThemes(sSigs);
  const sTrends = trendSummary('smes');
  
  briefings.smes = {
    audience: 'SMEs & Mittelstand',
    icon: '▣',
    question: 'Betrifft mich das? Was sollte ich jetzt tun?',
    signalCount: countForAudience('smes'),
    summary: buildSMESummary(sSigs, sPreds, sThemes, sTrends),
    topSignals: sSigs.slice(0, 3).map(s => ({ headline: s.headline, soWhat: s.soWhat, confidence: (s.beipackzettel || {}).confidence || 0 })),
    themes: sThemes.map(t => THEME_LABELS[t.theme] || t.theme),
    predictionCount: sPreds.length,
    trendDirection: sTrends.length > 0 ? 'active' : 'quiet'
  };
  
  // Meta
  briefings._meta = {
    generated: new Date().toISOString(),
    period: '7d',
    totalSignals: recent.length,
    totalPredictions: predictions.length,
    beipackzettel: {
      confidence: 65,
      riskLevel: 'medium',
      method: 'Automated extraction from RSS signals. No LLM synthesis. Keyword-based theme detection.',
      uncertainties: [
        'Summaries sind regelbasiert, nicht LLM-generiert — Nuancen können fehlen',
        'Audience-Zuordnung basiert auf Topic-Domain-Mapping, nicht auf echtem User-Profiling',
        'Signale aus 6 RSS-Quellen — kein Anspruch auf Vollständigkeit'
      ],
      notChecked: [
        'Keine Gegenrecherche der Signale',
        'Keine manuelle Kuratierung der Top-Signale',
        'Kein Abgleich mit proprietären Datenquellen'
      ]
    }
  };
  
  return briefings;
}

// ═══ AUDIENCE-SPECIFIC SUMMARY BUILDERS ═══
// Each returns a data-grounded summary string. No hallucination. Every claim traceable.

function buildFoundersSummary(sigs, preds, themes, trends) {
  const parts = [];
  
  if (sigs.length === 0) return 'Keine relevanten Signale in den letzten 7 Tagen.';
  
  // Lead with what's happening
  parts.push(sigs.length + ' Signale in den letzten 7 Tagen relevant für Gründer.');
  
  // Theme-based insight
  if (themes.length > 0) {
    const themeLabels = { security: 'Sicherheitsthemen', regulation: 'Regulierung', competition: 'Wettbewerbsdynamik', product_launch: 'neue Produkt-Launches', research: 'Forschungsergebnisse', funding: 'Funding & M&A', adoption: 'Enterprise-Adoption', infrastructure: 'Infrastruktur-Entwicklung' };
    const topTheme = themeLabels[themes[0].theme] || themes[0].theme;
    parts.push('Dominantes Thema: ' + topTheme + ' (' + themes[0].count + ' Signale).');
  }
  
  // Top signal as concrete example
  if (sigs[0]) {
    parts.push('Wichtigstes Signal: "' + sigs[0].headline.substring(0, 80) + '"');
    if (sigs[0].soWhat) parts.push('→ ' + sigs[0].soWhat.split('.')[0] + '.');
  }
  
  // Predictions
  if (preds.length > 0) {
    const topPred = preds.sort((a, b) => b.confidence - a.confidence)[0];
    parts.push('Prediction: ' + topPred.text.substring(0, 80) + ' (' + topPred.confidence + '% Confidence).');
  }
  
  // Actionable
  parts.push('Empfehlung: ' + (themes.some(t => t.theme === 'product_launch') ? 'Wettbewerber beobachten, Differenzierung prüfen.' : themes.some(t => t.theme === 'adoption') ? 'Enterprise-Bedarf validieren, Pilot-Kunden ansprechen.' : 'Signal-Lage beobachten, keine unmittelbare Handlung nötig.'));
  
  return parts.join(' ');
}

function buildDevelopersSummary(sigs, preds, themes, trends) {
  const parts = [];
  
  if (sigs.length === 0) return 'Keine relevanten technischen Signale in den letzten 7 Tagen.';
  
  parts.push(sigs.length + ' technische Signale in den letzten 7 Tagen.');
  
  if (themes.length > 0) {
    const themeLabels = { security: 'Security-Vulnerabilities', regulation: 'Compliance-Anforderungen', competition: 'Tool-Wettbewerb', product_launch: 'neue Releases & APIs', research: 'Paper & Benchmarks', funding: 'Startup-Funding', adoption: 'Adoption-Patterns', infrastructure: 'Infrastruktur & Frameworks' };
    const topTheme = themeLabels[themes[0].theme] || themes[0].theme;
    parts.push('Fokus diese Woche: ' + topTheme + '.');
  }
  
  if (sigs[0]) {
    parts.push('Top: "' + sigs[0].headline.substring(0, 80) + '"');
    if (sigs[0].soWhat) parts.push('→ ' + sigs[0].soWhat.split('.')[0] + '.');
  }
  
  if (trends.length > 0) {
    parts.push('Trending: ' + trends.map(t => t.label).join(', ') + '.');
  }
  
  parts.push('Empfehlung: ' + (themes.some(t => t.theme === 'security') ? 'Dependencies prüfen, Security-Patches einspielen.' : themes.some(t => t.theme === 'research') ? 'Neue Paper lesen, Architektur-Impact bewerten.' : 'Stack stabil, keine dringenden Änderungen.'));
  
  return parts.join(' ');
}

function buildVCSummary(sigs, preds, themes, trends) {
  const parts = [];
  
  if (sigs.length === 0) return 'Keine marktrelevanten Signale in den letzten 7 Tagen.';
  
  parts.push(sigs.length + ' marktrelevante Signale.');
  
  if (themes.length > 0) {
    const themeLabels = { security: 'Cybersecurity (Risiko + Chance)', regulation: 'Regulierungsdynamik', competition: 'Marktkonsolidierung', product_launch: 'Produkt-Momentum', research: 'Deep Tech Breakthroughs', funding: 'Funding-Aktivität', adoption: 'Enterprise-Adoption', infrastructure: 'Infrastruktur-Shift' };
    const topTheme = themeLabels[themes[0].theme] || themes[0].theme;
    parts.push('Dominanter Vektor: ' + topTheme + '.');
  }
  
  if (sigs[0]) {
    parts.push('Key Signal: "' + sigs[0].headline.substring(0, 80) + '"');
  }
  
  if (preds.length > 0) {
    const highConf = preds.filter(p => p.confidence >= 70);
    if (highConf.length) parts.push(highConf.length + ' High-Confidence Predictions (≥70%).');
  }
  
  parts.push('Alpha-Indikator: ' + (themes.some(t => t.theme === 'adoption') ? 'Enterprise-Adoption beschleunigt sich — Timing für B2B AI stimmt.' : themes.some(t => t.theme === 'competition') ? 'Markt konsolidiert — Winner-takes-all Dynamik beachten.' : 'Keine klaren Alpha-Signale diese Woche.'));
  
  return parts.join(' ');
}

function buildSMESummary(sigs, preds, themes, trends) {
  const parts = [];
  
  if (sigs.length === 0) return 'Keine unmittelbar geschäftsrelevanten Signale in den letzten 7 Tagen.';
  
  parts.push(sigs.length + ' Signale relevant für Unternehmen.');
  
  if (themes.length > 0) {
    const themeLabels = { security: 'Sicherheitsrisiken für Unternehmen', regulation: 'Neue Regulierung (Compliance prüfen)', competition: 'Wettbewerbsveränderungen', product_launch: 'Neue Tools verfügbar', research: 'Technologie-Entwicklung', funding: 'Marktbewegungen', adoption: 'AI-Adoption im Mittelstand', infrastructure: 'Infrastruktur-Updates' };
    const topTheme = themeLabels[themes[0].theme] || themes[0].theme;
    parts.push('Wichtigstes Thema: ' + topTheme + '.');
  }
  
  if (sigs[0]) {
    parts.push('Beachten: "' + sigs[0].headline.substring(0, 80) + '"');
  }
  
  parts.push('Handlungsempfehlung: ' + (themes.some(t => t.theme === 'security') ? 'IT-Sicherheit prüfen, Mitarbeiter sensibilisieren.' : themes.some(t => t.theme === 'regulation') ? 'Compliance-Status prüfen, ggf. Rechtsberatung einholen.' : themes.some(t => t.theme === 'adoption') ? 'AI-Pilotprojekt evaluieren — Kosten sinken, Nutzen steigt.' : 'Beobachten, keine unmittelbare Handlung nötig.'));
  
  return parts.join(' ');
}

// ═══ CLI ═══
const args = process.argv.slice(2);
const opts = {
  sourceFilter: args.includes('--source') ? args[args.indexOf('--source') + 1] : null,
  dryRun: args.includes('--dry-run'),
  seed: args.includes('--seed'),
  regen: args.includes('--regen')
};

if (opts.regen) {
  // Regenerate predictions/trends/briefings from existing signals without fetching
  const signalData = load(SIGNALS_FILE) || { signals: [], predictions: [], trends: [] };
  console.log('═══ REGENERATE ═══');
  console.log('Existing signals: ' + signalData.signals.length);
  signalData.predictions = generatePredictions(signalData.signals);
  signalData.trends = detectTrends(signalData.signals);
  signalData._meta = signalData._meta || {};
  signalData._meta.updated = new Date().toISOString();
  signalData._meta.totalPredictions = signalData.predictions.length;
  signalData._meta.totalTrends = signalData.trends.length;
  signalData.briefings = generateBriefings(signalData.signals, signalData.predictions, signalData.trends);
  save(SIGNALS_FILE, signalData);
  console.log('Predictions: ' + signalData.predictions.length);
  signalData.predictions.forEach(p => console.log('  🔮 ' + p.text + ' [' + p.confidence + '% / raw:' + (p.rawConfidence||'?') + '% / match:' + (p.matchQuality||0) + '%]'));
  console.log('\nSaved to ' + SIGNALS_FILE);
} else {
  ingest(opts).catch(e => { console.error(e); process.exit(1); });
}
