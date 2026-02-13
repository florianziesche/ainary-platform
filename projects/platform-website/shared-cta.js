// Shared CTA + Footer — injected on all marketing pages
// Usage: <div id="shared-cta"></div> before </body>

document.addEventListener('DOMContentLoaded', function() {
  const el = document.getElementById('shared-cta');
  if (!el) return;

  el.innerHTML = `
    <!-- CTA Section -->
    <section style="padding:100px 0 80px;text-align:center;border-top:1px solid rgba(255,255,255,0.06);">
      <div style="max-width:800px;margin:0 auto;padding:0 24px;">
        <h2 style="font-size:2rem;font-weight:600;letter-spacing:-0.02em;color:#ededf0;margin-bottom:40px;">Better decisions start here.</h2>
        <div style="display:flex;gap:16px;justify-content:center;">
          <a href="contact.html" style="display:inline-flex;align-items:center;justify-content:center;padding:14px 36px;border-radius:8px;font-size:0.9rem;font-weight:500;text-decoration:none;background:rgba(255,255,255,0.9);color:#08080c;transition:background 0.15s;min-width:170px;">Contact me</a>
          <a href="signup.html" style="display:inline-flex;align-items:center;justify-content:center;padding:14px 36px;border-radius:8px;font-size:0.9rem;font-weight:500;text-decoration:none;background:rgba(255,255,255,0.9);color:#08080c;transition:background 0.15s;min-width:170px;">Sign up</a>
        </div>
      </div>
    </section>

    <!-- Footer -->
    <footer style="padding:60px 0 30px;border-top:1px solid rgba(255,255,255,0.06);">
      <div style="max-width:1200px;margin:0 auto;padding:0 24px;display:grid;grid-template-columns:1fr repeat(4,auto);gap:60px;margin-bottom:60px;">
        <div>
          <a href="landing.html" style="text-decoration:none;color:#ededf0;font-weight:600;font-size:0.95rem;display:flex;align-items:center;">
            <span style="display:inline-block;width:10px;height:10px;border-radius:50%;background:#c8aa50;margin-right:6px;"></span>Ainary
          </a>
        </div>
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
            <a href="https://finitematter.substack.com/" target="_blank" style="color:#55555e;text-decoration:none;font-size:0.8rem;">Substack</a>
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
      <div style="max-width:1200px;margin:0 auto;padding:16px 24px 0;border-top:1px solid rgba(255,255,255,0.06);text-align:left;">
        <p style="color:#55555e;font-size:0.7rem;">© 2026 Ainary. All rights reserved.</p>
      </div>
    </footer>
  `;
});
