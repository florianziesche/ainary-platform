import puppeteer from 'puppeteer';
import { readFileSync } from 'fs';
import { log } from './utils.js';

/**
 * Generate a McKinsey-grade PDF from HTML report
 * @param {string} htmlPath - Path to HTML file
 * @param {string} outputPath - Path to save PDF
 * @param {string} company - Company name
 */
export async function generatePDF(htmlPath, outputPath, company) {
  log('PDF', 'Launching Puppeteer...');
  
  const browser = await puppeteer.launch({
    headless: true,
    args: [
      '--no-sandbox',
      '--disable-setuid-sandbox',
      '--disable-dev-shm-usage',
      '--disable-gpu',
      '--single-process',
      '--no-zygote'
    ]
  });

  try {
    const page = await browser.newPage();
    
    // Load HTML file
    log('PDF', `Loading HTML: ${htmlPath}`);
    const htmlContent = readFileSync(htmlPath, 'utf-8');
    
    // Inject cover page, TOC, and print styles
    const enhancedHTML = injectPrintEnhancements(htmlContent, company);
    
    await page.setContent(enhancedHTML, {
      waitUntil: ['load', 'networkidle0']
    });

    // Wait for fonts to load
    log('PDF', 'Waiting for fonts and charts...');
    await page.waitForFunction(() => {
      return document.fonts.ready;
    }, { timeout: 10000 }).catch(() => {
      log('PDF', 'Warning: Font loading timeout (proceeding anyway)');
    });

    // Additional wait for charts/SVGs
    await new Promise(r => setTimeout(r, 2000));

    const today = new Date().toLocaleDateString('en-US', { 
      year: 'numeric', 
      month: 'short', 
      day: 'numeric' 
    });

    // Generate PDF
    log('PDF', 'Generating PDF...');
    await page.pdf({
      path: outputPath,
      format: 'A4',
      printBackground: true,
      margin: {
        top: '85px',
        bottom: '70px',
        left: '50px',
        right: '50px'
      },
      displayHeaderFooter: true,
      headerTemplate: `
        <div style="width: 100%; font-size: 9px; padding: 0 50px; margin-top: 20px; color: #6b7280; font-family: -apple-system, system-ui, sans-serif;">
          <div style="border-bottom: 1px solid #374151; padding-bottom: 8px; display: flex; justify-content: space-between;">
            <span style="font-weight: 600;">AI Company X-Ray</span>
            <span>${company}</span>
          </div>
        </div>
      `,
      footerTemplate: `
        <div style="width: 100%; font-size: 8px; padding: 0 50px; margin-bottom: 15px; color: #6b7280; font-family: -apple-system, system-ui, sans-serif; display: flex; justify-content: space-between; align-items: center;">
          <span style="color: #ef4444; font-weight: 600; letter-spacing: 0.5px;">CONFIDENTIAL</span>
          <span style="flex: 1; text-align: center;">Page <span class="pageNumber"></span> of <span class="totalPages"></span></span>
          <span>Generated ${today} | florian.ziesche@hotmail.com</span>
        </div>
      `
    });

    log('PDF', `✓ PDF saved to: ${outputPath}`);
  } finally {
    await browser.close();
  }
}

/**
 * Inject cover page, TOC, and print-optimized CSS
 */
function injectPrintEnhancements(html, company) {
  const today = new Date().toLocaleDateString('en-US', { 
    year: 'numeric', 
    month: 'long', 
    day: 'numeric' 
  });

  // Print-optimized CSS
  const printCSS = `
    <style>
      @media print {
        /* Cover page takes full page */
        .cover-page {
          height: 100vh;
          display: flex;
          align-items: center;
          justify-content: center;
          page-break-after: always;
          background: linear-gradient(135deg, #0f172a 0%, #1e1b4b 100%);
          position: relative;
          overflow: hidden;
        }

        .cover-content {
          text-align: center;
          z-index: 2;
          max-width: 600px;
          padding: 40px;
        }

        .cover-badge {
          display: inline-block;
          padding: 8px 24px;
          background: rgba(239, 68, 68, 0.15);
          border: 2px solid #ef4444;
          border-radius: 24px;
          color: #ef4444;
          font-size: 11px;
          font-weight: 700;
          letter-spacing: 2px;
          margin-bottom: 40px;
        }

        .cover-company {
          font-size: 56px;
          font-weight: 800;
          color: #ffffff;
          margin: 0 0 20px 0;
          line-height: 1.1;
        }

        .cover-divider {
          width: 120px;
          height: 3px;
          background: linear-gradient(90deg, transparent, #6366f1, transparent);
          margin: 30px auto;
        }

        .cover-title {
          font-size: 36px;
          font-weight: 700;
          background: linear-gradient(135deg, #6366f1, #a78bfa);
          -webkit-background-clip: text;
          -webkit-text-fill-color: transparent;
          background-clip: text;
          margin: 20px 0 10px 0;
        }

        .cover-subtitle {
          font-size: 16px;
          color: #9ca3af;
          font-weight: 400;
          margin: 0 0 50px 0;
        }

        .cover-meta {
          color: #6b7280;
          font-size: 13px;
          line-height: 1.8;
          margin: 40px 0;
        }

        .cover-footer {
          position: absolute;
          bottom: 50px;
          left: 0;
          right: 0;
          text-align: center;
          color: #6b7280;
          font-size: 12px;
          line-height: 1.8;
        }

        /* Watermark */
        .cover-page::before {
          content: "CONFIDENTIAL";
          position: absolute;
          top: 50%;
          left: 50%;
          transform: translate(-50%, -50%) rotate(-45deg);
          font-size: 120px;
          font-weight: 900;
          color: rgba(239, 68, 68, 0.05);
          letter-spacing: 10px;
          z-index: 1;
          white-space: nowrap;
        }

        /* Table of Contents */
        .toc-page {
          page-break-after: always;
          padding: 60px 0;
          background: #0f172a;
          min-height: 100vh;
        }

        .toc-page h2 {
          font-size: 32px;
          font-weight: 700;
          color: #ffffff;
          margin-bottom: 40px;
          border-bottom: 2px solid #374151;
          padding-bottom: 16px;
        }

        .toc-item {
          display: flex;
          align-items: baseline;
          padding: 14px 0;
          border-bottom: 1px solid rgba(255, 255, 255, 0.05);
          color: #d1d5db;
          font-size: 14px;
        }

        .toc-item span:first-child {
          color: #6366f1;
          font-weight: 700;
          margin-right: 16px;
          font-variant-numeric: tabular-nums;
        }

        .toc-dots {
          flex: 1;
          border-bottom: 1px dotted #374151;
          margin: 0 12px 4px 12px;
        }

        .toc-item span:last-child {
          color: #9ca3af;
          font-weight: 600;
          font-variant-numeric: tabular-nums;
        }

        /* Content cards - page breaks */
        .card {
          page-break-before: always;
          page-break-inside: avoid;
          background: #0f172a !important;
          padding: 30px !important;
          margin-bottom: 0 !important;
        }

        .card:first-of-type {
          page-break-before: avoid; /* First card doesn't need break */
        }

        /* Tables */
        table {
          page-break-inside: avoid;
        }

        /* Charts */
        svg {
          page-break-inside: avoid;
        }

        /* Hide lead capture */
        .lead-capture,
        #lead-capture,
        [class*="lead"],
        [class*="cta"] {
          display: none !important;
        }

        /* Ensure dark background */
        body {
          background: #0f172a !important;
          color: #e5e7eb !important;
        }

        /* Remove animations */
        * {
          animation: none !important;
          transition: none !important;
        }

        /* Watermark on every page */
        body::before {
          content: "CONFIDENTIAL";
          position: fixed;
          top: 50%;
          left: 50%;
          transform: translate(-50%, -50%) rotate(-45deg);
          font-size: 100px;
          font-weight: 900;
          color: rgba(239, 68, 68, 0.04);
          letter-spacing: 8px;
          z-index: -1;
          pointer-events: none;
        }
      }
    </style>
  `;

  // Cover page HTML
  const coverPage = `
    <div class="cover-page">
      <div class="cover-content">
        <div class="cover-badge">CONFIDENTIAL</div>
        <h1 class="cover-company">${company}</h1>
        <div class="cover-divider"></div>
        <h2 class="cover-title">AI Company X-Ray</h2>
        <h3 class="cover-subtitle">Strategic AI Assessment & Readiness Report</h3>
        <div class="cover-meta">
          <div>Generated: ${today}</div>
          <div>Methodology: Hyperthink — 5 AI Agents, 3 Rounds of Critical Analysis</div>
        </div>
        <div class="cover-footer">
          <div>Prepared by Florian Ziesche</div>
          <div>finitematter.substack.com</div>
        </div>
      </div>
    </div>
  `;

  // Table of Contents
  const toc = `
    <div class="toc-page">
      <h2>Table of Contents</h2>
      <div class="toc-item">
        <span>01</span>
        Executive Summary
        <span class="toc-dots"></span>
        <span>3</span>
      </div>
      <div class="toc-item">
        <span>02</span>
        AI Readiness Score
        <span class="toc-dots"></span>
        <span>4</span>
      </div>
      <div class="toc-item">
        <span>03</span>
        Department-by-Department Opportunities
        <span class="toc-dots"></span>
        <span>5</span>
      </div>
      <div class="toc-item">
        <span>04</span>
        Competitive Position
        <span class="toc-dots"></span>
        <span>6</span>
      </div>
      <div class="toc-item">
        <span>05</span>
        Strategic Recommendations
        <span class="toc-dots"></span>
        <span>7</span>
      </div>
      <div class="toc-item">
        <span>06</span>
        Implementation Roadmap
        <span class="toc-dots"></span>
        <span>10</span>
      </div>
      <div class="toc-item">
        <span>07</span>
        Risk Analysis
        <span class="toc-dots"></span>
        <span>11</span>
      </div>
      <div class="toc-item">
        <span>08</span>
        Provocateur Insights
        <span class="toc-dots"></span>
        <span>12</span>
      </div>
      <div class="toc-item">
        <span>09</span>
        Bottom Line
        <span class="toc-dots"></span>
        <span>13</span>
      </div>
    </div>
  `;

  // Inject everything
  const bodyIndex = html.indexOf('<body');
  const bodyEndIndex = html.indexOf('>', bodyIndex) + 1;
  
  const enhanced = 
    html.slice(0, bodyEndIndex) + 
    printCSS +
    coverPage +
    toc +
    html.slice(bodyEndIndex);

  return enhanced;
}
