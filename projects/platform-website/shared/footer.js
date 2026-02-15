// Shared Footer — shared/footer.js
// Usage: <div id="site-footer"></div>

(function() {
  const el = document.getElementById('site-footer');
  if (!el) return;

  el.innerHTML = `
    <style>
      @keyframes subtle-pulse { 0%,100% { opacity:1; } 50% { opacity:0.85; } }
    </style>
    <!-- CTA Section -->
    <section style="padding:100px 0 80px;text-align:center;border-top:1px solid rgba(255,255,255,0.06);">
      <div style="max-width:800px;margin:0 auto;padding:0 24px;">
        <h2 style="font-size:2rem;font-weight:600;letter-spacing:-0.02em;color:#ededf0;margin-bottom:40px;">Better decisions start here.</h2>
        <div style="display:flex;gap:16px;justify-content:center;">
          <a href="https://calendly.com/florian-ainaryventures/15-minutes-chat" target="_blank" style="display:inline-flex;align-items:center;justify-content:center;padding:14px 36px;border-radius:8px;font-size:0.9rem;font-weight:500;text-decoration:none;background:transparent;color:#ededf0;border:1px solid rgba(255,255,255,0.5);transition:border-color 0.15s;min-width:170px;">Contact me</a>
          <a href="signup.html" style="display:inline-flex;align-items:center;justify-content:center;padding:14px 36px;border-radius:8px;font-size:0.9rem;font-weight:500;text-decoration:none;background:#c8aa50;color:#ffffff;transition:opacity 0.15s;min-width:170px;animation:subtle-pulse 4s ease-in-out infinite;">Sign up</a>
        </div>
      </div>
    </section>

    <!-- Footer -->
    <footer style="padding:60px 0 30px;border-top:1px solid rgba(255,255,255,0.06);">
      <div style="max-width:1200px;margin:0 auto;padding:0 24px;display:grid;grid-template-columns:1fr repeat(4,auto);gap:60px;margin-bottom:60px;">
        <div>
          <a href="/" style="text-decoration:none;color:#ededf0;font-weight:600;font-size:0.95rem;display:flex;align-items:center;">
            <span style="display:inline-block;width:10px;height:10px;border-radius:50%;background:#c8aa50;margin-right:6px;"></span>Ainary
          </a>
          <p style="color:#55555e;font-size:0.7rem;margin-top:12px;letter-spacing:0.02em;">HUMAN × AI SYSTEMS = LEVERAGE</p>
        </div>
        <div>
          <h4 style="font-size:0.75rem;font-weight:500;margin-bottom:16px;letter-spacing:0.04em;color:#ededf0;">Product</h4>
          <div style="display:flex;flex-direction:column;gap:10px;">
            <a href="tools.html" style="color:#55555e;text-decoration:none;font-size:0.8rem;">Use Cases</a>
            <a href="reports.html" style="color:#55555e;text-decoration:none;font-size:0.8rem;">AI Research & Brief</a>
            <a href="pricing.html" style="color:#55555e;text-decoration:none;font-size:0.8rem;">Pricing</a>
          </div>
        </div>
        <div>
          <h4 style="font-size:0.75rem;font-weight:500;margin-bottom:16px;letter-spacing:0.04em;color:#ededf0;">Resources</h4>
          <div style="display:flex;flex-direction:column;gap:10px;">
            <a href="blog.html" style="color:#55555e;text-decoration:none;font-size:0.8rem;">Blog</a>
            <a href="https://finitematter.substack.com/" target="_blank" style="color:#55555e;text-decoration:none;font-size:0.8rem;">Substack</a>
            <a href="https://linkedin.com/in/florianziesche" target="_blank" style="color:#55555e;text-decoration:none;font-size:0.8rem;">LinkedIn</a>
          </div>
        </div>
        <div>
          <h4 style="font-size:0.75rem;font-weight:500;margin-bottom:16px;letter-spacing:0.04em;color:#ededf0;">Company</h4>
          <div style="display:flex;flex-direction:column;gap:10px;">
            <a href="about.html" style="color:#55555e;text-decoration:none;font-size:0.8rem;">About</a>
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
})();
