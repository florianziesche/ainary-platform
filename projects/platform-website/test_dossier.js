const http = require('http');
const fs = require('fs');
const path = require('path');

const server = http.createServer((req, res) => {
  let fp = '.' + new URL(req.url, 'http://localhost').pathname;
  const ext = path.extname(fp);
  const types = {'.html':'text/html','.json':'application/json','.css':'text/css'};
  fs.readFile(fp, (err, data) => {
    if (err) { res.writeHead(404); res.end('404'); return; }
    res.writeHead(200, {'Content-Type': types[ext]||'text/plain'});
    res.end(data);
  });
});

const cities = ['bamberg','regensburg','nuernberg','augsburg','erlangen','fuerth','passau','landshut'];

async function runTests() {
  const { chromium } = await import('playwright');
  const browser = await chromium.launch();
  let allPass = true;
  let results = [];
  
  for (const city of cities) {
    const page = await browser.newPage();
    const pageErrors = [];
    page.on('pageerror', err => pageErrors.push(err.message));
    
    await page.goto(`http://localhost:9994/dossier.html?city=${city}&admin`, { waitUntil: 'networkidle' });
    await page.waitForTimeout(2000);
    
    const checks = await page.evaluate(() => {
      const gate = document.getElementById('auth-gate');
      const authHidden = gate ? gate.style.display === 'none' : true;
      const topbar = document.getElementById('topbar-tenant');
      const topbarText = topbar ? topbar.textContent : '';
      const briefing = document.getElementById('briefing-view');
      const briefingText = briefing ? briefing.textContent : '';
      const ontology = document.getElementById('ontology-view');
      const ontologyText = ontology ? ontology.textContent : '';
      const mainContent = briefingText + ontologyText;
      const undefinedCount = (mainContent.match(/\bundefined\b/g) || []).length;
      const hasContent = mainContent.length > 100;
      return { authHidden, topbarText, undefinedCount, hasContent, contentLength: mainContent.length };
    });
    
    const pass = checks.authHidden && checks.hasContent && pageErrors.length === 0 && checks.undefinedCount === 0;
    if (!pass) allPass = false;
    
    const status = pass ? '✅' : '❌';
    let issues = [];
    if (!checks.authHidden) issues.push('auth gate visible');
    if (!checks.hasContent) issues.push('no content rendered');
    if (pageErrors.length) issues.push(pageErrors.length + ' JS errors');
    if (checks.undefinedCount) issues.push(checks.undefinedCount + 'x undefined');
    
    console.log(`${status} ${city.padEnd(12)} | ${checks.topbarText.substring(0,40).padEnd(40)} | ${issues.length ? issues.join(', ') : 'OK'}`);
    for (const e of pageErrors) console.log(`   💥 ${e.substring(0, 120)}`);
    
    results.push({ city, pass, issues });
    await page.close();
  }
  
  await browser.close();
  console.log('\n' + '='.repeat(70));
  const passed = results.filter(r => r.pass).length;
  console.log(`${passed}/${cities.length} cities pass`);
  if (allPass) console.log('✅ ALL PASS — safe to deploy');
  else console.log('❌ FAILED — fix before deploy');
  return allPass;
}

server.listen(9994, async () => {
  try { const p = await runTests(); server.close(); process.exit(p ? 0 : 1); }
  catch(e) { console.error('Error:', e.message); server.close(); process.exit(1); }
});
