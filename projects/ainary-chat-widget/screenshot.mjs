import puppeteer from 'puppeteer';
import { resolve } from 'path';

const dir = resolve(import.meta.dirname);
const versions = [
  { file: 'demo-v1-chat.html', name: 'v1-chat' },
  { file: 'demo-v2-credits.html', name: 'v2-credits' },
  { file: 'demo-v3-simplified.html', name: 'v3-simplified' },
  { file: 'demo-v4-recognition.html', name: 'v4-recognition' },
  { file: 'reports/goal-tensions-decarbonization.html', name: 'report-goal-tensions' },
];

const browser = await puppeteer.launch({ headless: true });

for (const v of versions) {
  const page = await browser.newPage();
  await page.setViewport({ width: 1200, height: 800 });
  await page.goto(`file://${dir}/${v.file}`, { waitUntil: 'networkidle0', timeout: 15000 });
  await page.screenshot({ path: `${dir}/docs/screenshots/${v.name}.png`, fullPage: false });
  console.log(`✓ ${v.name}`);
  await page.close();
}

await browser.close();
console.log('Done');
