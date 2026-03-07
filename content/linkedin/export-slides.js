const { chromium } = require('playwright');
const path = require('path');
const file = process.argv[2] || 'carousel.html';
const prefix = process.argv[3] || 'slide';

(async () => {
  const browser = await chromium.launch();
  const height = (file.includes('v5') || file.includes('v6')) ? 1350 : 1080;
  const page = await browser.newPage({ viewport: { width: 1080, height } });
  await page.goto('file://' + path.join(__dirname, file));
  await page.waitForTimeout(1500);

  // Find all .slide elements
  const slides = await page.$$('.slide');
  let i = 0;
  for (const el of slides) {
    i++;
    const id = await el.getAttribute('id');
    const name = id || `${prefix}-${i}`;
    await el.screenshot({ path: path.join(__dirname, `slides/${name}.png`), type: 'png' });
    console.log(`Exported ${name}.png`);
  }

  await browser.close();
  console.log(`Done. ${i} slides exported.`);
})();
