import puppeteer from 'puppeteer';

const browser = await puppeteer.launch({ headless: true, args: ['--no-sandbox'] });

async function snap(htmlFile, outFile) {
  const page = await browser.newPage();
  await page.setViewport({ width: 1000, height: 800, deviceScaleFactor: 2 });
  await page.goto(`file:///Users/florianziesche/.openclaw/workspace/projects/platform-website/assets/${htmlFile}`, { waitUntil: 'networkidle0' });
  await page.waitForFunction(() => document.fonts.ready);
  await new Promise(r => setTimeout(r, 1000));
  const card = await page.$('.card');
  await card.screenshot({ path: `/Users/florianziesche/.openclaw/workspace/projects/platform-website/assets/${outFile}`, type: 'png' });
  console.log(`✅ ${outFile}`);
  await page.close();
}

await snap('mockup-research.html', 'ai-research-visual.png');
await snap('mockup-systems.html', 'ai-systems-visual.png');
await browser.close();
