import puppeteer from 'puppeteer';
import { resolve } from 'path';
const dir = resolve(import.meta.dirname);

const browser = await puppeteer.launch({ headless: true });

// Login screen
let page = await browser.newPage();
await page.setViewport({ width: 1200, height: 800 });
await page.goto(`file://${dir}/demo.html`, { waitUntil: 'networkidle0', timeout: 15000 });
await page.screenshot({ path: `${dir}/docs/screenshots/v5-login.png` });
console.log('✓ v5-login');

// Friedl dashboard
await page.evaluate(() => demoLogin('friedl'));
await new Promise(r => setTimeout(r, 500));
await page.screenshot({ path: `${dir}/docs/screenshots/v5-friedl.png`, fullPage: true });
console.log('✓ v5-friedl');
await page.close();

// Andreas dashboard
page = await browser.newPage();
await page.setViewport({ width: 1200, height: 800 });
await page.goto(`file://${dir}/demo.html`, { waitUntil: 'networkidle0', timeout: 15000 });
await page.evaluate(() => demoLogin('andreas'));
await new Promise(r => setTimeout(r, 500));
await page.screenshot({ path: `${dir}/docs/screenshots/v5-andreas.png`, fullPage: true });
console.log('✓ v5-andreas');
await page.close();

// Bürgermeister dashboard
page = await browser.newPage();
await page.setViewport({ width: 1200, height: 800 });
await page.goto(`file://${dir}/demo.html`, { waitUntil: 'networkidle0', timeout: 15000 });
await page.evaluate(() => demoLogin('buergermeister'));
await new Promise(r => setTimeout(r, 500));
await page.screenshot({ path: `${dir}/docs/screenshots/v5-buergermeister.png`, fullPage: true });
console.log('✓ v5-buergermeister');
await page.close();

await browser.close();
console.log('Done');
