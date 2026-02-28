const { chromium } = require('playwright');
(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage();
  await page.goto('https://ainaryventures.com/dossier.html?city=friedberg');
  try {
    await page.waitForSelector('input[type="password"]', {timeout: 5000});
    await page.fill('input[type="password"]', 'stamp2026');
    await page.keyboard.press('Enter');
    await page.waitForTimeout(3000);
  } catch(e) {}
  
  // Briefing tab screenshot
  await page.screenshot({path: 'friedberg-briefing2.png', fullPage: false});
  
  // Strategy tab
  await page.evaluate(() => { if(typeof switchView==='function') switchView('strategy'); });
  await page.waitForTimeout(2000);
  await page.screenshot({path: 'friedberg-strategy2.png', fullPage: false});
  
  // Dossier tab (entity detail)
  await page.evaluate(() => { if(typeof switchView==='function') switchView('dossier'); });
  await page.waitForTimeout(2000);
  await page.screenshot({path: 'friedberg-dossier2.png', fullPage: false});
  
  // Netzwerk tab
  await page.evaluate(() => { if(typeof switchView==='function') switchView('graph'); });
  await page.waitForTimeout(2000);
  await page.screenshot({path: 'friedberg-graph2.png', fullPage: false});
  
  // Vergleich tab
  await page.evaluate(() => { if(typeof switchView==='function') switchView('vergleich'); });
  await page.waitForTimeout(2000);
  await page.screenshot({path: 'friedberg-vergleich2.png', fullPage: false});
  
  // Check all tabs for issues
  const issues = await page.evaluate(() => {
    var body = document.body.innerText;
    return {
      hasUndefined: body.includes('undefined'),
      hasNaN: body.includes('NaN'),
      has0Quellen: body.includes('0 Quellen'),
      has0Kandidaten: body.includes('0 Kandidaten'),
      nullCount: (body.match(/\bnull\b/g) || []).length,
      zeroPercent: (body.match(/0\.[\d]+%/g) || []),
    };
  });
  console.log('Issues:', JSON.stringify(issues));
  
  await browser.close();
})().catch(e => console.error(e.message));
