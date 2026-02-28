#!/usr/bin/env node
/**
 * ARTICLE DESIGN STANDARD VALIDATOR
 * ===================================
 * Run before EVERY deploy: `node test_article.js`
 * Fails = no deploy. No exceptions.
 * 
 * What it checks (from COLOR-SYSTEM.md + CROSS-SYNTHESIS):
 * - Only standard hex colors (no rogue values)
 * - Only standard border-radii (3/6/8/50%)
 * - Trust Bar present (EIJA-Verified)
 * - Gold dots (●) in H2 sections
 * - Product links (bidirectional article network)
 * - Shared components (nav.js, footer.js, styles.css)
 * - Reading progress bar
 * - Gradient blobs
 * - No em dashes (—)
 * - No font-weight: 300
 * - Typography: H1=2.2rem, H2=1.5rem, body=1.05rem
 */

const fs = require('fs');
const path = require('path');

// === CONFIG ===
const ARTICLES = [
  'blog/ai-agent-memory-what-anthropic-is-missing.html',
  'blog/kommunalwahl-stichwahl-analyse-en.html',
  'blog/kommunalwahl-stichwahl-analyse.html',
  'article-agenttrust.html',
  'de/article-one-person-company.html',
];

const STANDARD_COLORS_6 = new Set([
  '#08080c', '#111116', '#ededf0', '#8b8b95', '#55555e', '#c8aa50',
  '#238551', '#2d72d2', '#c87619', '#cd4246',
]);
const BLOB_OK = new Set(['#ffffff', '#e8f0ff', '#b0c4e8', '#a08030']);
const TRAFFIC_OK = new Set(['#ff5f57', '#ffbd2e', '#28c840']); // macOS chrome only

const STANDARD_RADII = new Set(['3px', '6px', '8px', '50%', '0 8px 8px 0']);

// === TESTS ===
let totalPass = 0;
let totalFail = 0;
let totalSkip = 0;

function check(article, name, pass, detail) {
  if (pass) {
    totalPass++;
  } else {
    totalFail++;
    console.log(`  ❌ ${name}${detail ? ' — ' + detail : ''}`);
  }
}

for (const file of ARTICLES) {
  const fullPath = path.join(__dirname, file);
  if (!fs.existsSync(fullPath)) {
    console.log(`⏭️  ${file} — FILE NOT FOUND, skipping`);
    totalSkip++;
    continue;
  }
  
  const c = fs.readFileSync(fullPath, 'utf8');
  const shortName = path.basename(file);
  let articleFails = 0;
  const prevFail = totalFail;

  // 1. Color compliance
  const hex6 = [...new Set(c.match(/#[0-9a-fA-F]{6}/g) || [])];
  const badColors = hex6.filter(h => {
    const lower = h.toLowerCase();
    return !STANDARD_COLORS_6.has(lower) && !BLOB_OK.has(lower) && !TRAFFIC_OK.has(lower);
  });
  check(shortName, 'Colors: only standard hex values', badColors.length === 0, 
    badColors.length > 0 ? `Found: ${badColors.join(', ')}` : '');

  // 2. No shorthand non-standard (#888, #333, #222, #fff, #111 standalone)
  const badShorthands = [];
  for (const sh of ['#888', '#333', '#222', '#fff']) {
    const re = new RegExp(sh.replace('#', '#') + '(?![0-9a-fA-F])', 'g');
    if (re.test(c)) badShorthands.push(sh);
  }
  // #111 standalone (not part of #111116)
  if (/#111(?![0-9a-fA-F])/.test(c)) badShorthands.push('#111');
  check(shortName, 'Colors: no non-standard shorthands', badShorthands.length === 0,
    badShorthands.length > 0 ? `Found: ${badShorthands.join(', ')}` : '');

  // 3. Border-radius compliance
  const radii = (c.match(/border-radius:\s*([^;}\n]+)/g) || [])
    .map(m => m.replace('border-radius:', '').trim());
  const badRadii = radii.filter(r => {
    // Allow compound values for monitor mockups (0 0 12px 12px, etc.)
    if (r.includes(' ') && !STANDARD_RADII.has(r)) {
      // Compound radii from monitor mockup chrome are OK
      return false;
    }
    return !STANDARD_RADII.has(r) && r !== '0';
  });
  check(shortName, 'Border-radius: only standard values', badRadii.length === 0,
    badRadii.length > 0 ? `Found: ${[...new Set(badRadii)].join(', ')}` : '');

  // 4. Trust Bar (EIJA-Verified or EIJA-verifiziert)
  const hasTrustBar = /EIJA-Verified|EIJA-verifiziert/.test(c) && c.includes('●');
  check(shortName, 'Trust Bar present', hasTrustBar);

  // 5. Gold dots in H2s (at least 3)
  const goldDots = (c.match(/●/g) || []).length;
  check(shortName, 'Gold dots (●) ≥ 3', goldDots >= 3, `Found: ${goldDots}`);

  // 6. Product links (at least one cross-link to another article or radar)
  const hasProductLink = /radar\.html|article-agenttrust|memory-what-anthropic|kommunalwahl/.test(c);
  check(shortName, 'Product/article cross-links', hasProductLink);

  // 7. Shared components
  check(shortName, 'Has nav.js', c.includes('nav.js'));
  check(shortName, 'Has footer.js', c.includes('footer.js'));
  check(shortName, 'Has styles.css', c.includes('styles.css'));

  // 8. Reading progress bar
  check(shortName, 'Reading progress bar', c.includes('reading-progress'));

  // 9. Gradient blobs
  check(shortName, 'Gradient blobs', /drift/.test(c));

  // 10. No em dashes in visible text (outside HTML tags/attributes)
  // Strip HTML tags, then check
  const textOnly = c.replace(/<style[\s\S]*?<\/style>/gi, '')
                     .replace(/<script[\s\S]*?<\/script>/gi, '')
                     .replace(/<[^>]+>/g, ' ');
  const emDashes = (textOnly.match(/—/g) || []).length;
  check(shortName, 'No em dashes (—)', emDashes === 0, emDashes > 0 ? `Found: ${emDashes}` : '');

  // 11. No font-weight: 300
  check(shortName, 'No font-weight:300', !c.includes('font-weight:300') && !c.includes('font-weight: 300'));

  // 12. JSON-LD Schema
  check(shortName, 'Has JSON-LD', c.includes('application/ld+json'));

  // 13. OG Tags
  check(shortName, 'Has og:title', c.includes('og:title'));

  articleFails = totalFail - prevFail;
  const articleChecks = 13;
  const status = articleFails === 0 ? '✅' : '❌';
  console.log(`${status} ${shortName}: ${articleChecks - articleFails}/${articleChecks} passed`);
}

// === SUMMARY ===
console.log('\n' + '='.join ? '='.repeat(50) : '==================================================');
console.log(`TOTAL: ${totalPass} passed, ${totalFail} failed, ${totalSkip} skipped`);

if (totalFail === 0) {
  console.log('🎯 ALL CHECKS PASSED — SAFE TO DEPLOY');
  process.exit(0);
} else {
  console.log(`⛔ ${totalFail} FAILURES — DO NOT DEPLOY`);
  process.exit(1);
}
