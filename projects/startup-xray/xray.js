#!/usr/bin/env node
import { log } from './utils.js';
import { scan } from './agents/scanner.js';
import { analyzeMarket } from './agents/market.js';
import { evaluateInvestment } from './agents/investor.js';
import { analyzeFinancials } from './agents/financier.js';
import { critique } from './agents/devils-advocate.js';
import { hyperthink } from './hyperthink.js';
import { render } from './renderer.js';

const startup = process.argv[2];
if (!startup) {
  console.error('Usage: node xray.js "Startup Name"');
  process.exit(1);
}

console.log(`\n╔══════════════════════════════════════════════╗`);
console.log(`║  STARTUP X-RAY — VC Due Diligence Engine    ║`);
console.log(`║  5 Agents · 3 Rounds · Honest Confidence     ║`);
console.log(`╚══════════════════════════════════════════════╝\n`);
console.log(`Target: ${startup}\n`);

const t0 = Date.now();

try {
  // Phase 1: Data Collection (Parallel)
  log('PHASE 1', 'Data Collection — Scanner + Market Analyst');
  const scannerData = await scan(startup);
  const marketData = await analyzeMarket(startup, scannerData);
  log('PHASE 1', `Complete (${((Date.now() - t0) / 1000).toFixed(1)}s)`);

  // Phase 2: Deep Analysis (Parallel)
  log('PHASE 2', 'Deep Analysis — Investor + Financier + Devil\'s Advocate');
  const [investorData, financierData, devilsAdvocateData] = await Promise.all([
    evaluateInvestment(startup, scannerData, marketData),
    analyzeFinancials(startup, scannerData, marketData),
    critique(startup, { scanner: scannerData, market: marketData })
  ]);
  log('PHASE 2', `Complete (${((Date.now() - t0) / 1000).toFixed(1)}s)`);

  // Phase 3: Hyperthink — 3-Round Synthesis
  log('PHASE 3', 'Hyperthink — Synthesize → Critique → Finalize');
  const finalReport = await hyperthink(startup, {
    scanner: scannerData,
    market: marketData,
    investor: investorData,
    financier: financierData,
    devilsAdvocate: devilsAdvocateData
  });
  log('PHASE 3', `Complete (${((Date.now() - t0) / 1000).toFixed(1)}s)`);

  // Phase 4: Render
  log('PHASE 4', 'Rendering HTML + PDF report...');
  const outputPath = render(finalReport, startup);
  
  const totalTime = ((Date.now() - t0) / 1000).toFixed(1);
  
  console.log(`\n╔══════════════════════════════════════════════╗`);
  console.log(`║  ✓ DUE DILIGENCE COMPLETE                    ║`);
  console.log(`╚══════════════════════════════════════════════╝`);
  console.log(`\n  Startup:  ${startup}`);
  console.log(`  Time:     ${totalTime}s`);
  console.log(`  Agents:   5 (Scanner, Market, Investor, Financier, Devil's Advocate)`);
  console.log(`  Rounds:   3 (Synthesize → Critique → Finalize)`);
  console.log(`  Output:   ${outputPath}\n`);

} catch (err) {
  console.error('\n❌ Error:', err.message);
  if (err.response) console.error('API Response:', err.response?.data);
  process.exit(1);
}
