// Shared CTA + Footer — injected on all marketing pages
// Usage: <div id="shared-cta"></div> before </body>

document.addEventListener('DOMContentLoaded', function() {
  const el = document.getElementById('shared-cta');
  if (!el) return;

  // Dynamic page links — exclude current page
  const currentPath = window.location.pathname.split('/').pop() || 'landing.html';
  const pages = [
    { href: 'daily-brief.html', label: 'Daily Brief' },
    { href: 'blog.html', label: 'Blog' },
    { href: 'pricing.html', label: 'Pricing' },
    { href: 'tools.html', label: 'Use Cases' },
    { href: 'about.html', label: 'About' }
  ];
  const links = pages
    .filter(p => p.href !== currentPath)
    .map(p => `<a href="${p.href}" style="color:#55555e;font-size:0.8rem;text-decoration:none;transition:color 0.2s;" onmouseover="this.style.color='#c8aa50'" onmouseout="this.style.color='#8b8b95'">${p.label}</a>`)
    .join('<span style="color:#55555e;font-size:0.8rem;"> · </span>');

  el.innerHTML = `
    <!-- CTA Section -->
    <section style="padding:80px 0 60px;text-align:center;border-top:1px solid rgba(255,255,255,0.06);">
      <div style="max-width:800px;margin:0 auto;padding:0 24px;">
        <p style="color:#ededf0;font-size:1.5rem;font-weight:600;letter-spacing:-0.02em;margin-bottom:12px;">Better decisions start here.</p>
        <p style="color:#8b8b95;font-size:1.1rem;font-weight:500;margin-bottom:32px;">HUMAN × AI SYSTEMS = LEVERAGE</p>
        <div style="display:flex;gap:16px;justify-content:center;margin-bottom:32px;">
          <a href="contact.html" style="display:inline-flex;align-items:center;justify-content:center;padding:12px 32px;border-radius:8px;font-size:0.85rem;font-weight:500;text-decoration:none;background:#ededf0;color:#08080c;transition:background 0.15s;min-width:160px;">Contact me</a>
          <a href="signup.html" style="display:inline-flex;align-items:center;justify-content:center;padding:12px 32px;border-radius:8px;font-size:0.85rem;font-weight:500;text-decoration:none;background:#c8aa50;color:#08080c;transition:background 0.15s;min-width:160px;">Sign up</a>
        </div>
        <div style="display:flex;justify-content:center;gap:0;flex-wrap:wrap;margin-bottom:12px;">
          ${links}
        </div>
        <a href="https://finitematter.substack.com/" target="_blank" style="color:#55555e;font-size:0.7rem;text-decoration:none;">Also on Substack →</a>
      </div>
    </section>

    <!-- Footer -->
    <footer style="padding:40px 0 30px;border-top:1px solid rgba(255,255,255,0.06);">
      <div style="max-width:1200px;margin:0 auto;padding:0 24px;display:grid;grid-template-columns:repeat(4,1fr);gap:40px;margin-bottom:40px;">
        <div>
          <h4 style="font-size:0.75rem;font-weight:500;margin-bottom:16px;letter-spacing:0.04em;color:#ededf0;">Product</h4>
          <div style="display:flex;flex-direction:column;gap:10px;">
            <a href="tools.html" style="color:#55555e;text-decoration:none;font-size:0.8rem;">Use Cases</a>
            <a href="daily-brief.html" style="color:#55555e;text-decoration:none;font-size:0.8rem;">Daily Brief</a>
            <a href="pricing.html" style="color:#55555e;text-decoration:none;font-size:0.8rem;">Pricing</a>
          </div>
        </div>
        <div>
          <h4 style="font-size:0.75rem;font-weight:500;margin-bottom:16px;letter-spacing:0.04em;color:#ededf0;">Resources</h4>
          <div style="display:flex;flex-direction:column;gap:10px;">
            <a href="blog.html" style="color:#55555e;text-decoration:none;font-size:0.8rem;">Blog</a>
            <a href="quality.html" style="color:#55555e;text-decoration:none;font-size:0.8rem;">How I Build</a>
          </div>
        </div>
        <div>
          <h4 style="font-size:0.75rem;font-weight:500;margin-bottom:16px;letter-spacing:0.04em;color:#ededf0;">Company</h4>
          <div style="display:flex;flex-direction:column;gap:10px;">
            <a href="about.html" style="color:#55555e;text-decoration:none;font-size:0.8rem;">About</a>
            <a href="contact.html" style="color:#55555e;text-decoration:none;font-size:0.8rem;">Contact</a>
          </div>
        </div>
        <div>
          <h4 style="font-size:0.75rem;font-weight:500;margin-bottom:16px;letter-spacing:0.04em;color:#ededf0;">Legal</h4>
          <div style="display:flex;flex-direction:column;gap:10px;">
            <a href="privacy.html" style="color:#55555e;text-decoration:none;font-size:0.8rem;">Privacy</a>
            <a href="terms.html" style="color:#55555e;text-decoration:none;font-size:0.8rem;">Terms</a>
            <a href="imprint.html" style="color:#55555e;text-decoration:none;font-size:0.8rem;">Imprint</a>
          </div>
        </div>
      </div>
      <div style="max-width:1200px;margin:0 auto;padding:24px 24px 0;border-top:1px solid rgba(255,255,255,0.06);text-align:center;">
        <p style="color:#55555e;font-size:0.7rem;">© 2026 Ainary. All rights reserved.</p>
      </div>
    </footer>
  `;
});
