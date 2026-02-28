const http = require('http');
const fs = require('fs');
const path = require('path');

const server = http.createServer((req, res) => {
  let filePath = '.' + new URL(req.url, 'http://localhost').pathname;
  const ext = path.extname(filePath);
  const types = {'.html':'text/html','.json':'application/json','.css':'text/css','.js':'text/javascript'};
  fs.readFile(filePath, (err, data) => {
    if (err) { res.writeHead(404); res.end('Not found: ' + filePath); return; }
    // Inject auth bypass into HTML
    if (ext === '.html') {
      let html = data.toString();
      html = html.replace('<head>', '<head><script>try{sessionStorage.setItem("ai-auth","1")}catch(e){}</script>');
      res.writeHead(200, {'Content-Type': 'text/html'});
      res.end(html);
    } else {
      res.writeHead(200, {'Content-Type': types[ext]||'text/plain'});
      res.end(data);
    }
  });
});

const cities = ['bamberg','regensburg','nuernberg','augsburg','erlangen','fuerth','passau','landshut'];

async function runTests() {
  const { chromium } = await import('playwright');
  const browser = await chromium.launch();
  let allPass = true;
  let errors = [];
  
  for (const city of cities) {
    const page = await browser.newPage();
    const pageErrors = [];
    
    page.on('pageerror', err => pageErrors.push(err.message));
    
    await page.goto(`http://localhost:9998/dossier.html?city=${city}`, { waitUntil: 'networkidle' });
    await page.waitForTimeout(2000);
    
    const bodyText = await page.textContent('body');
    const hasError = bodyText.includes('Stadt nicht gefunden');
    const undefinedMatches = bodyText.match(/\bundefined\b/g) || [];
    // Filter out "undefined" that might be in legitimate content
    const undefinedCount = undefinedMatches.length;
    
    const pass = !hasError && pageErrors.length === 0 && undefinedCount === 0;
    if (!pass) allPass = false;
    
    const status = pass ? '✅' : '❌';
    console.log(`${status} ${city.padEnd(12)} | JS: ${pageErrors.length} | undef: ${undefinedCount} | crash: ${hasError}`);
    for (const e of pageErrors) {
      console.log(`   💥 ${e.substring(0, 150)}`);
      errors.push(`${city}: ${e.substring(0, 150)}`);
    }
    if (hasError) errors.push(`${city}: Stadt nicht gefunden (catch block triggered)`);
    if (undefinedCount) errors.push(`${city}: ${undefinedCount}x undefined in text`);
    
    await page.close();
  }
  
  await browser.close();
  console.log('\n' + '='.repeat(60));
  if (allPass) { console.log('✅ ALL PASS'); } 
  else { console.log('❌ FAILED — ' + errors.length + ' errors'); for (const e of errors) console.log('  • ' + e); }
  return allPass;
}

server.listen(9998, async () => {
  try { const p = await runTests(); server.close(); process.exit(p ? 0 : 1); }
  catch(e) { console.error('Error:', e.message); server.close(); process.exit(1); }
});
