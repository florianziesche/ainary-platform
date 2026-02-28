#!/usr/bin/env node
/**
 * Ainary Demo Recorder v2 — Quality Edition
 * Higher FPS, smooth scrolling, cursor simulation, text overlays, transitions
 */

const puppeteer = require('puppeteer-core');
const { execSync } = require('child_process');
const path = require('path');
const fs = require('fs');

const CHROME_PATH = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome';
const BASE_URL = 'https://florianziesche.github.io/ainary-demo-v7/index.html';
const OUTPUT = 'ainary-demo-v2.mp4';
const FPS = 10; // 10fps capture → smooth at 30fps output
const WIDTH = 1920;
const HEIGHT = 1080;
const FRAME_DIR = path.join(__dirname, 'frames-v2');

// Cursor overlay — inject a fake cursor into the page
const CURSOR_CSS = `
  #mia-cursor {
    position: fixed;
    width: 24px;
    height: 24px;
    z-index: 999999;
    pointer-events: none;
    transition: all 0.3s cubic-bezier(0.25, 0.1, 0.25, 1);
    filter: drop-shadow(0 2px 4px rgba(0,0,0,0.3));
  }
  #mia-cursor svg {
    width: 24px;
    height: 24px;
  }
  #mia-click-ring {
    position: fixed;
    width: 40px;
    height: 40px;
    border-radius: 50%;
    border: 2px solid rgba(0,0,0,0.3);
    z-index: 999998;
    pointer-events: none;
    opacity: 0;
    transform: scale(0.5);
    transition: all 0.3s ease;
  }
  #mia-click-ring.active {
    opacity: 1;
    transform: scale(1.2);
  }
  #mia-overlay {
    position: fixed;
    bottom: 40px;
    left: 50%;
    transform: translateX(-50%);
    background: rgba(0,0,0,0.85);
    color: white;
    padding: 16px 32px;
    border-radius: 12px;
    font-family: 'Helvetica Neue', sans-serif;
    font-size: 20px;
    font-weight: 500;
    letter-spacing: -0.3px;
    z-index: 999999;
    opacity: 0;
    transition: opacity 0.5s ease;
    backdrop-filter: blur(10px);
    max-width: 700px;
    text-align: center;
    line-height: 1.4;
  }
  #mia-overlay.visible { opacity: 1; }
  #mia-brand {
    position: fixed;
    top: 20px;
    right: 24px;
    font-family: 'Helvetica Neue', sans-serif;
    font-size: 14px;
    font-weight: 600;
    letter-spacing: 2px;
    text-transform: uppercase;
    color: rgba(0,0,0,0.5);
    z-index: 999999;
  }
`;

const CURSOR_SVG = `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="black" stroke="white" stroke-width="1"><path d="M5.5 3.21V20.8c0 .45.54.67.85.35l4.86-4.86a.5.5 0 0 1 .35-.15h6.87c.45 0 .67-.54.35-.85L5.85 2.36a.5.5 0 0 0-.35.85z"/></svg>`;

async function injectUI(page) {
  await page.evaluate((css, svg) => {
    const style = document.createElement('style');
    style.textContent = css;
    document.head.appendChild(style);

    const cursor = document.createElement('div');
    cursor.id = 'mia-cursor';
    cursor.innerHTML = svg;
    cursor.style.left = '960px';
    cursor.style.top = '540px';
    document.body.appendChild(cursor);

    const ring = document.createElement('div');
    ring.id = 'mia-click-ring';
    document.body.appendChild(ring);

    const overlay = document.createElement('div');
    overlay.id = 'mia-overlay';
    document.body.appendChild(overlay);

    const brand = document.createElement('div');
    brand.id = 'mia-brand';
    brand.textContent = 'AINARY VENTURES';
    document.body.appendChild(brand);
  }, CURSOR_CSS, CURSOR_SVG);
}

async function moveCursor(page, x, y) {
  await page.evaluate((x, y) => {
    const c = document.getElementById('mia-cursor');
    if (c) { c.style.left = x + 'px'; c.style.top = y + 'px'; }
    const r = document.getElementById('mia-click-ring');
    if (r) { r.style.left = (x - 8) + 'px'; r.style.top = (y - 8) + 'px'; }
  }, x, y);
  await sleep(100);
}

async function clickEffect(page) {
  await page.evaluate(() => {
    const r = document.getElementById('mia-click-ring');
    if (r) { r.classList.add('active'); setTimeout(() => r.classList.remove('active'), 400); }
  });
  await sleep(400);
}

async function showOverlay(page, text) {
  await page.evaluate((t) => {
    const o = document.getElementById('mia-overlay');
    if (o) { o.textContent = t; o.classList.add('visible'); }
  }, text);
}

async function hideOverlay(page) {
  await page.evaluate(() => {
    const o = document.getElementById('mia-overlay');
    if (o) o.classList.remove('visible');
  });
}

async function smoothScroll(page, distance, durationMs) {
  const steps = Math.ceil(durationMs / (1000 / FPS));
  const stepSize = distance / steps;
  for (let i = 0; i < steps; i++) {
    await page.evaluate((s) => window.scrollBy({ top: s, behavior: 'instant' }), stepSize);
    await sleep(1000 / FPS);
  }
}

function sleep(ms) { return new Promise(r => setTimeout(r, ms)); }

async function captureFrames(page, seconds, frameCounter) {
  const total = Math.ceil(seconds * FPS);
  for (let i = 0; i < total; i++) {
    const num = String(frameCounter + i).padStart(5, '0');
    await page.screenshot({
      path: path.join(FRAME_DIR, `frame_${num}.jpg`),
      type: 'jpeg',
      quality: 92
    });
    await sleep(1000 / FPS);
  }
  return frameCounter + total;
}

async function scrollAndCapture(page, distance, durationSec, frameCounter) {
  const totalFrames = Math.ceil(durationSec * FPS);
  const stepSize = distance / totalFrames;
  for (let i = 0; i < totalFrames; i++) {
    await page.evaluate((s) => window.scrollBy({ top: s, behavior: 'instant' }), stepSize);
    const num = String(frameCounter + i).padStart(5, '0');
    await page.screenshot({
      path: path.join(FRAME_DIR, `frame_${num}.jpg`),
      type: 'jpeg',
      quality: 92
    });
    await sleep(1000 / FPS);
  }
  return frameCounter + totalFrames;
}

async function findAndClickLink(page, keywords) {
  const links = await page.$$('a');
  for (const l of links) {
    const text = await page.evaluate(el => el.textContent, l);
    const href = await page.evaluate(el => el.href, l);
    if (text && keywords.some(k => text.toLowerCase().includes(k.toLowerCase()))) {
      const box = await l.boundingBox();
      if (box) {
        await moveCursor(page, box.x + box.width / 2, box.y + box.height / 2);
        await sleep(300);
        await clickEffect(page);
        await l.click().catch(() => {});
        await sleep(2000);
        return true;
      }
    }
  }
  return false;
}

async function main() {
  console.log('🎬 Ainary Demo Recorder v2 — Quality Edition');
  console.log(`${WIDTH}x${HEIGHT} @ ${FPS}fps capture → 30fps output\n`);

  if (fs.existsSync(FRAME_DIR)) fs.rmSync(FRAME_DIR, { recursive: true });
  fs.mkdirSync(FRAME_DIR, { recursive: true });

  const browser = await puppeteer.launch({
    executablePath: CHROME_PATH,
    headless: 'new',
    args: [`--window-size=${WIDTH},${HEIGHT}`, '--no-sandbox', '--force-device-scale-factor=1']
  });

  const page = await browser.newPage();
  await page.setViewport({ width: WIDTH, height: HEIGHT, deviceScaleFactor: 1 });

  // Load page
  console.log('Loading demo...');
  await page.goto(BASE_URL, { waitUntil: 'networkidle2', timeout: 15000 }).catch(() => {});
  await sleep(2000);
  await injectUI(page);
  await sleep(500);

  let fc = 0;

  // === SCENE 1: Dashboard Hero (4s) ===
  console.log('📸 1/8 Dashboard — "Jeden Morgen. Automatisch."');
  await moveCursor(page, 960, 540);
  await showOverlay(page, 'KI-Assistenz für Ihre Kommune. Jeden Morgen. Automatisch.');
  fc = await captureFrames(page, 4, fc);
  await hideOverlay(page);
  await sleep(300);

  // === SCENE 2: Scroll Dashboard (3s) ===
  console.log('📸 2/8 Scroll Dashboard');
  fc = await scrollAndCapture(page, 500, 3, fc);

  // === SCENE 3: Show KPI area (2s) ===
  console.log('📸 3/8 KPIs');
  await showOverlay(page, '12 Dokumenttypen. 80% automatisierbar. Ab €49/Monat.');
  fc = await captureFrames(page, 3, fc);
  await hideOverlay(page);

  // === SCENE 4: Click Fördermittel (5s) ===
  console.log('📸 4/8 Open Fördermittel Report');
  await page.evaluate(() => window.scrollTo(0, 0));
  await sleep(500);
  fc = await captureFrames(page, 1, fc);
  const found = await findAndClickLink(page, ['Förder', 'förder', 'Fördermittel']);
  if (!found) await findAndClickLink(page, ['Analyse', 'Report', 'Recherche']);
  await showOverlay(page, 'Fördermittel-Recherche: Sonst €5.000–25.000 extern.');
  fc = await captureFrames(page, 4, fc);
  await hideOverlay(page);

  // === SCENE 5: Scroll Report (3s) ===
  console.log('📸 5/8 Scroll Report');
  fc = await scrollAndCapture(page, 600, 3, fc);

  // === SCENE 6: Back + Daily Intel (5s) ===
  console.log('📸 6/8 Daily Intel');
  await page.goBack().catch(() => {});
  await sleep(2000);
  await injectUI(page); // re-inject after navigation
  await sleep(500);
  await findAndClickLink(page, ['Daily', 'Intel', 'Briefing', 'Tages']);
  await showOverlay(page, 'Tägliches Briefing. Bürgerthemen. Fördermittel. Wettbewerb.');
  fc = await captureFrames(page, 4, fc);
  await hideOverlay(page);

  // === SCENE 7: Scroll Intel (3s) ===
  console.log('📸 7/8 Scroll Intel');
  fc = await scrollAndCapture(page, 500, 3, fc);

  // === SCENE 8: CTA (4s) ===
  console.log('📸 8/8 CTA');
  await showOverlay(page, 'Pilotprojekt starten → florian@ainaryventures.com');
  fc = await captureFrames(page, 4, fc);

  await browser.close();
  console.log(`\n✅ ${fc} frames captured (${(fc/FPS).toFixed(0)}s video)`);

  // === ENCODE ===
  console.log('🎥 Encoding high-quality MP4...');
  
  // Add fade in/out with ffmpeg
  const totalDuration = fc / FPS;
  const cmd = [
    'ffmpeg -y',
    `-framerate ${FPS}`,
    `-i "${FRAME_DIR}/frame_%05d.jpg"`,
    '-c:v libx264',
    '-preset slow',        // better compression
    '-crf 18',             // higher quality (lower = better, 18 = visually lossless)
    '-pix_fmt yuv420p',
    '-r 30',
    `-vf "scale=${WIDTH}:${HEIGHT},fade=in:0:${FPS},fade=out:${fc - FPS}:${FPS}"`,
    `"${path.join(__dirname, OUTPUT)}"`
  ].join(' ');

  try {
    execSync(cmd, { stdio: 'pipe' });
    const sz = fs.statSync(path.join(__dirname, OUTPUT));
    console.log(`\n✅ ${OUTPUT} (${(sz.size/1024/1024).toFixed(1)} MB, ${totalDuration.toFixed(0)}s)`);
  } catch(e) {
    console.error('ffmpeg error:', e.stderr?.toString().slice(0, 300));
  }

  fs.rmSync(FRAME_DIR, { recursive: true });
  console.log('Done.');
}

main().catch(console.error);
