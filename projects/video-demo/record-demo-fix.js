const puppeteer = require('puppeteer-core');
const { execSync } = require('child_process');
const path = require('path');
const fs = require('fs');

// Use system Chrome
const CHROME_PATH = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome';
const BASE_URL = 'https://florianziesche.github.io/ainary-demo-v7/index.html';
const OUTPUT = 'ainary-demo.mp4';
const FPS = 2;
const WIDTH = 1920;
const HEIGHT = 1080;
const FRAME_DIR = path.join(__dirname, 'frames');

async function autoScroll(page, distance, steps) {
  const stepSize = distance / steps;
  for (let i = 0; i < steps; i++) {
    await page.evaluate((s) => window.scrollBy(0, s), stepSize);
    await new Promise(r => setTimeout(r, 100));
  }
}

async function captureFrames(page, holdSeconds, frameCounter) {
  const totalFrames = holdSeconds * FPS;
  for (let i = 0; i < totalFrames; i++) {
    const frameNum = String(frameCounter + i).padStart(5, '0');
    await page.screenshot({
      path: path.join(FRAME_DIR, `frame_${frameNum}.jpg`),
      type: 'jpeg',
      quality: 90
    });
    await new Promise(r => setTimeout(r, 1000 / FPS));
  }
  return frameCounter + totalFrames;
}

async function main() {
  console.log('🎬 Ainary Demo Recorder (System Chrome)');
  
  if (fs.existsSync(FRAME_DIR)) fs.rmSync(FRAME_DIR, { recursive: true });
  fs.mkdirSync(FRAME_DIR, { recursive: true });

  const browser = await puppeteer.launch({
    executablePath: CHROME_PATH,
    headless: 'new',
    args: [`--window-size=${WIDTH},${HEIGHT}`, '--no-sandbox']
  });

  const page = await browser.newPage();
  await page.setViewport({ width: WIDTH, height: HEIGHT });

  console.log(`Loading ${BASE_URL}...`);
  await page.goto(BASE_URL, { waitUntil: 'networkidle2', timeout: 15000 }).catch(() => {});
  await new Promise(r => setTimeout(r, 2000));

  let fc = 0;

  // Scene 1: Dashboard (3s)
  console.log('📸 1/6 Dashboard');
  fc = await captureFrames(page, 3, fc);

  // Scene 2: Scroll down (3s)
  console.log('📸 2/6 Scroll Overview');
  await autoScroll(page, 600, 10);
  fc = await captureFrames(page, 3, fc);

  // Scene 3: Click a report link
  console.log('📸 3/6 Open Report');
  const links = await page.$$('a');
  for (const l of links) {
    const text = await page.evaluate(el => el.textContent, l);
    if (text && (text.includes('Förder') || text.includes('förder') || text.includes('Analyse'))) {
      await l.click().catch(() => {});
      await new Promise(r => setTimeout(r, 2000));
      break;
    }
  }
  fc = await captureFrames(page, 4, fc);

  // Scene 4: Scroll report
  console.log('📸 4/6 Scroll Report');
  await autoScroll(page, 800, 12);
  fc = await captureFrames(page, 3, fc);

  // Scene 5: Back + click daily intel
  console.log('📸 5/6 Daily Intel');
  await page.goBack().catch(() => {});
  await new Promise(r => setTimeout(r, 2000));
  const links2 = await page.$$('a');
  for (const l of links2) {
    const text = await page.evaluate(el => el.textContent, l);
    if (text && (text.includes('Daily') || text.includes('Intel') || text.includes('Briefing'))) {
      await l.click().catch(() => {});
      await new Promise(r => setTimeout(r, 2000));
      break;
    }
  }
  fc = await captureFrames(page, 4, fc);

  // Scene 6: Scroll intel + hold
  console.log('📸 6/6 Scroll Intel');
  await autoScroll(page, 600, 10);
  fc = await captureFrames(page, 3, fc);

  await browser.close();
  console.log(`\n✅ ${fc} frames captured`);

  // Encode
  console.log('🎥 Encoding...');
  const cmd = `ffmpeg -y -framerate ${FPS} -i "${FRAME_DIR}/frame_%05d.jpg" -c:v libx264 -pix_fmt yuv420p -crf 23 -r 30 -vf "scale=${WIDTH}:${HEIGHT}" "${path.join(__dirname, OUTPUT)}"`;
  try {
    execSync(cmd, { stdio: 'pipe' });
    const sz = fs.statSync(path.join(__dirname, OUTPUT));
    console.log(`✅ ${OUTPUT} (${(sz.size/1024/1024).toFixed(1)} MB)`);
  } catch(e) {
    console.error('ffmpeg error:', e.stderr?.toString().slice(0,200));
  }

  fs.rmSync(FRAME_DIR, { recursive: true });
}

main().catch(console.error);
