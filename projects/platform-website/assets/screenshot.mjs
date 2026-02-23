import puppeteer from 'puppeteer';

const browser = await puppeteer.launch({ headless: true, args: ['--no-sandbox'] });
const page = await browser.newPage();
await page.setViewport({ width: 1000, height: 800, deviceScaleFactor: 2 });
await page.goto('file:///Users/florianziesche/.openclaw/workspace/projects/platform-website/assets/mockup-research.html', { waitUntil: 'networkidle0' });

// Wait for fonts
await page.waitForFunction(() => document.fonts.ready);
await new Promise(r => setTimeout(r, 1000));

const card = await page.$('.card');
await card.screenshot({ path: '/Users/florianziesche/.openclaw/workspace/projects/platform-website/assets/ai-research-visual.png', type: 'png' });

console.log('✅ Research visual saved');
await browser.close();
