#!/usr/bin/env node
/**
 * Ainary Demo Screen Recorder
 * Captures the BM Glashütte demo as a series of screenshots → MP4 video
 * 
 * Usage: node record-demo.js [--url URL] [--output FILE] [--fps 2]
 */

const puppeteer = require('puppeteer');
const { execSync } = require('child_process');
const path = require('path');
const fs = require('fs');

const BASE_URL = process.argv.includes('--url') 
  ? process.argv[process.argv.indexOf('--url') + 1]
  : 'https://florianziesche.github.io/ainary-demo-v7/index.html';

const OUTPUT = process.argv.includes('--output')
  ? process.argv[process.argv.indexOf('--output') + 1]
  : 'ainary-demo.mp4';

const FPS = 2; // frames per second for smooth enough video
const WIDTH = 1920;
const HEIGHT = 1080;
const FRAME_DIR = path.join(__dirname, 'frames');

// Demo scenes — what to show and for how long
const SCENES = [
  {
    name: 'title',
    action: async (page) => {
      // Just show the main page
      await page.waitForSelector('body', { timeout: 5000 });
    },
    holdSeconds: 3
  },
  {
    name: 'scroll-overview',
    action: async (page) => {
      // Smooth scroll down to show KPIs and content
      await autoScroll(page, 400, 8);
    },
    holdSeconds: 1
  },
  {
    name: 'scroll-more',
    action: async (page) => {
      await autoScroll(page, 800, 8);
    },
    holdSeconds: 2
  },
  {
    name: 'click-foerdermittel',
    action: async (page) => {
      // Try to find and click Fördermittel link
      const link = await page.$('a[href*="foerdermittel"], a[href*="fördermittel"]');
      if (link) {
        await link.click();
        await page.waitForTimeout(2000);
      } else {
        // Try text content
        const links = await page.$$('a');
        for (const l of links) {
          const text = await page.evaluate(el => el.textContent, l);
          if (text && text.toLowerCase().includes('förder')) {
            await l.click();
            await page.waitForTimeout(2000);
            break;
          }
        }
      }
    },
    holdSeconds: 3
  },
  {
    name: 'scroll-report',
    action: async (page) => {
      await autoScroll(page, 500, 8);
    },
    holdSeconds: 3
  },
  {
    name: 'back-to-overview',
    action: async (page) => {
      await page.goBack();
      await page.waitForTimeout(1500);
    },
    holdSeconds: 2
  },
  {
    name: 'click-daily-intel',
    action: async (page) => {
      const links = await page.$$('a');
      for (const l of links) {
        const text = await page.evaluate(el => el.textContent, l);
        if (text && (text.toLowerCase().includes('daily') || text.toLowerCase().includes('intel') || text.toLowerCase().includes('briefing'))) {
          await l.click();
          await page.waitForTimeout(2000);
          break;
        }
      }
    },
    holdSeconds: 3
  },
  {
    name: 'scroll-intel',
    action: async (page) => {
      await autoScroll(page, 600, 10);
    },
    holdSeconds: 3
  },
  {
    name: 'back-final',
    action: async (page) => {
      await page.goBack();
      await page.waitForTimeout(1500);
    },
    holdSeconds: 3
  }
];

async function autoScroll(page, distance, steps) {
  const stepSize = distance / steps;
  for (let i = 0; i < steps; i++) {
    await page.evaluate((s) => window.scrollBy(0, s), stepSize);
    await page.waitForTimeout(100);
  }
}

async function captureFrames(page, sceneName, holdSeconds, frameCounter) {
  const totalFrames = holdSeconds * FPS;
  for (let i = 0; i < totalFrames; i++) {
    const frameNum = String(frameCounter + i).padStart(5, '0');
    await page.screenshot({
      path: path.join(FRAME_DIR, `frame_${frameNum}.jpg`),
      type: 'jpeg',
      quality: 90
    });
    await page.waitForTimeout(1000 / FPS);
  }
  return frameCounter + totalFrames;
}

async function main() {
  console.log('🎬 Ainary Demo Recorder');
  console.log(`URL: ${BASE_URL}`);
  console.log(`Output: ${OUTPUT}`);
  console.log(`Resolution: ${WIDTH}x${HEIGHT}`);
  console.log('');

  // Clean/create frame directory
  if (fs.existsSync(FRAME_DIR)) {
    fs.rmSync(FRAME_DIR, { recursive: true });
  }
  fs.mkdirSync(FRAME_DIR, { recursive: true });

  // Launch browser
  console.log('Starting browser...');
  const browser = await puppeteer.launch({
    headless: 'new',
    args: [
      `--window-size=${WIDTH},${HEIGHT}`,
      '--no-sandbox',
      '--disable-setuid-sandbox'
    ]
  });

  const page = await browser.newPage();
  await page.setViewport({ width: WIDTH, height: HEIGHT });

  // Navigate
  console.log(`Loading ${BASE_URL}...`);
  try {
    await page.goto(BASE_URL, { waitUntil: 'networkidle2', timeout: 15000 });
  } catch (e) {
    console.log(`Navigation warning: ${e.message}`);
  }
  await page.waitForTimeout(1000);

  // Run scenes
  let frameCounter = 0;
  for (const scene of SCENES) {
    console.log(`📸 Scene: ${scene.name} (${scene.holdSeconds}s)`);
    
    try {
      await scene.action(page);
    } catch (e) {
      console.log(`  Action warning: ${e.message}`);
    }
    
    // Capture frames for this scene's hold duration
    frameCounter = await captureFrames(page, scene.name, scene.holdSeconds, frameCounter);
  }

  await browser.close();
  console.log(`\n✅ ${frameCounter} frames captured`);

  // Convert to video with ffmpeg
  console.log('\n🎥 Encoding video...');
  const ffmpegCmd = [
    'ffmpeg -y',
    `-framerate ${FPS}`,
    `-i "${FRAME_DIR}/frame_%05d.jpg"`,
    '-c:v libx264',
    '-pix_fmt yuv420p',
    '-crf 23',
    `-r 30`,  // output at 30fps for smooth playback
    `-vf "scale=${WIDTH}:${HEIGHT}"`,
    `"${path.join(__dirname, OUTPUT)}"`
  ].join(' ');

  try {
    execSync(ffmpegCmd, { stdio: 'pipe' });
    const stats = fs.statSync(path.join(__dirname, OUTPUT));
    console.log(`\n✅ Video saved: ${OUTPUT} (${(stats.size / 1024 / 1024).toFixed(1)} MB)`);
  } catch (e) {
    console.error(`ffmpeg error: ${e.stderr?.toString() || e.message}`);
  }

  // Cleanup frames
  fs.rmSync(FRAME_DIR, { recursive: true });
  console.log('Frames cleaned up.');
}

main().catch(console.error);
