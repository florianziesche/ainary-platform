#!/usr/bin/env node
import { log } from './utils.js';
import { scan } from './agents/scanner.js';
import { analyzeIndustry } from './agents/industry.js';
import { strategize } from './agents/strategist.js';
import { calculateFinancials } from './agents/financier.js';
import { provoke } from './agents/provocateur.js';
import { hyperthink } from './hyperthink.js';
import { render } from './renderer.js';
import { generatePDF } from './pdf-generator.js';

const company = process.argv[2];
if (!company) {
  console.error('Usage: node xray.js "Company Name"');
  process.exit(1);
}

console.log(`\n╔══════════════════════════════════════════════╗`);
console.log(`║  AI COMPANY X-RAY — Hyperthink Engine v1.0   ║`);
console.log(`║  5 Agents · 3 Rounds · 0 Politics            ║`);
console.log(`╚══════════════════════════════════════════════╝\n`);
console.log(`Target: ${company}\n`);

const t0 = Date.now();

try {
  // Phase 1: Data Collection (Parallel)
  log('PHASE 1', 'Data Collection — Scanner + Industry Analyst');
  const scannerData = await scan(company);
  const industryData = await analyzeIndustry(company, scannerData);
  log('PHASE 1', `Complete (${((Date.now() - t0) / 1000).toFixed(1)}s)`);

  // Phase 2: Deep Analysis (Parallel)
  log('PHASE 2', 'Deep Analysis — Strategist + Financier + Provocateur');
  const [strategistData, financierData, provocateurData] = await Promise.all([
    strategize(company, scannerData, industryData),
    calculateFinancials(company, scannerData, industryData),
    provoke(company, { scanner: scannerData, industry: industryData })
  ]);
  log('PHASE 2', `Complete (${((Date.now() - t0) / 1000).toFixed(1)}s)`);

  // Phase 3: Hyperthink — 3-Round Synthesis
  log('PHASE 3', 'Hyperthink — Synthesize → Critique → Finalize');
  const finalReport = await hyperthink(company, {
    scanner: scannerData,
    industry: industryData,
    strategist: strategistData,
    financier: financierData,
    provocateur: provocateurData
  });
  log('PHASE 3', `Complete (${((Date.now() - t0) / 1000).toFixed(1)}s)`);

  // Phase 4: Render
  log('PHASE 4', 'Rendering HTML report...');
  const outputPath = render(finalReport, company);
  
  // Phase 5: Generate PDF
  log('PHASE 5', 'Generating PDF...');
  const pdfPath = outputPath.replace('.html', '.pdf');
  await generatePDF(outputPath, pdfPath, company);
  
  const totalTime = ((Date.now() - t0) / 1000).toFixed(1);
  
  console.log(`\n╔══════════════════════════════════════════════╗`);
  console.log(`║  ✓ REPORT COMPLETE                           ║`);
  console.log(`╚══════════════════════════════════════════════╝`);
  console.log(`\n  Company:  ${company}`);
  console.log(`  Time:     ${totalTime}s`);
  console.log(`  Agents:   5 (Scanner, Industry, Strategist, Financier, Provocateur)`);
  console.log(`  Rounds:   3 (Synthesize → Critique → Finalize)`);
  console.log(`  HTML:     ${outputPath}`);
  console.log(`  PDF:      ${pdfPath}\n`);

} catch (err) {
  console.error('\n❌ Error:', err.message);
  if (err.response) console.error('API Response:', err.response?.data);
  process.exit(1);
}
