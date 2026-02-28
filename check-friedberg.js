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
  } catch(e) { console.log('No pw prompt'); }
  
  const checks = await page.evaluate(() => {
    var body = document.body.innerText;
    return {
      kandidatenCards: document.querySelectorAll('[onclick*="showEntity"]').length,
      hasEichmann: body.includes('Eichmann'),
      hasBoehm: body.includes('Böhm'),  
      has0Quellen: body.includes('0 Quellen'),
      hasUndefined: body.includes('undefined'),
      hasNaN: body.includes('NaN'),
      has0Kandidaten: body.includes('0 Kandidaten'),
      snippet: body.substring(0, 800)
    };
  });
  console.log(JSON.stringify(checks, null, 2));
  await page.screenshot({path: '/tmp/friedberg-main.png', fullPage: false});
  
  // Strategy tab
  await page.evaluate(() => { if(typeof switchView==='function') switchView('strategy'); });
  await page.waitForTimeout(2000);
  await page.screenshot({path: '/tmp/friedberg-strategy.png', fullPage: false});
  var strat = await page.evaluate(() => document.body.innerText.substring(0, 800));
  console.log('STRATEGY:', strat.substring(0, 500));
  
  await browser.close();
})().catch(e => console.error(e.message));
