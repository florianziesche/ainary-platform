// Shared Footer — shared/footer.js
// Usage: <div id="site-footer"></div>
// Language-aware: checks document.documentElement.lang

(function() {
  const el = document.getElementById('site-footer');
  if (!el) return;

  const lang = (document.documentElement.lang || 'en').toLowerCase().slice(0,2);
  const isDE = lang === 'de';

  // Determine path prefix for links
  const path = window.location.pathname;
  const inDE = path.includes('/de/');
  const inBlog = path.includes('/blog/');
  // From /blog/ subdir, prefix must go up one level first
  const prefix = isDE
    ? (inDE ? '' : (inBlog ? '../de/' : 'de/'))
    : (inDE ? '../' : (inBlog ? '../' : ''));

  const t = {
    cta: isDE ? 'Bessere Entscheidungen fangen hier an.' : 'Better decisions start here.',
    ctaBtn: isDE ? 'Kontakt aufnehmen' : 'Get in touch',
    explore: isDE ? 'Entdecken' : 'Explore',
    blog: isDE ? 'Building in Public' : 'Building in Public',
    about: isDE ? 'Über uns' : 'About',
    resources: isDE ? 'Ressourcen' : 'Resources',
    connect: isDE ? 'Verbinden' : 'Connect',
    legal: isDE ? 'Rechtliches' : 'Legal',
    privacy: isDE ? 'Datenschutz' : 'Privacy',
    terms: isDE ? 'AGB' : 'Terms',
    imprint: isDE ? 'Impressum' : 'Imprint',
    rights: isDE ? '© 2026 Ainary. Alle Rechte vorbehalten.' : '© 2026 Ainary. All rights reserved.',
    switchLabel: isDE ? 'EN' : 'DE',
    switchLink: isDE ? (inDE ? '../' + path.split('/de/')[1] : path) : (inDE ? path : 'de/' + (path.split('/').pop() || 'index.html')),
  };

  // Build switch link more robustly
  let switchHref;
  const pageName = path.split('/').pop() || 'index.html';
  if (isDE) {
    // Link to English version
    switchHref = inDE ? '../' + pageName : pageName;
  } else {
    // Link to German version
    switchHref = inDE ? pageName : 'de/' + pageName;
  }

  const contactLink = prefix + 'contact.html';
  const blogLink = prefix + 'blog.html';
  const aboutLink = prefix + 'about.html';
  const resourcesLink = prefix + 'resources.html';
  const privacyLink = prefix + 'privacy.html';
  const termsLink = prefix + 'terms.html';
  const imprintLink = prefix + 'imprint.html';

  // Inject Vercel Web Analytics (once)
  if (!document.querySelector('script[src*="_vercel/insights"]')) {
    var s = document.createElement('script');
    s.defer = true;
    s.src = '/_vercel/insights/script.js';
    document.head.appendChild(s);
  }

  el.innerHTML = `
    <!-- CTA Section -->
    <section style="padding:100px 0 80px;text-align:center;border-top:1px solid rgba(255,255,255,0.06);">
      <div style="max-width:800px;margin:0 auto;padding:0 24px;">
        <h2 style="font-size:2rem;font-weight:600;letter-spacing:-0.02em;color:#ededf0;margin-bottom:40px;">${t.cta}</h2>
        <a href="${contactLink}" style="display:inline-flex;align-items:center;justify-content:center;padding:14px 36px;border-radius:8px;font-size:0.9rem;font-weight:500;text-decoration:none;background:transparent;color:#ededf0;border:1px solid rgba(255,255,255,0.5);transition:border-color 0.15s;min-width:170px;">${t.ctaBtn}</a>
      </div>
    </section>

    <!-- Footer -->
    <footer style="padding:60px 0 30px;border-top:1px solid rgba(255,255,255,0.06);">
      <div style="max-width:1200px;margin:0 auto;padding:0 24px;display:grid;grid-template-columns:1fr repeat(3,auto);gap:60px;margin-bottom:60px;">
        <div>
          <a href="${prefix}index.html" style="text-decoration:none;color:#ededf0;font-weight:600;font-size:0.95rem;display:flex;align-items:center;">
            <span style="display:inline-block;width:10px;height:10px;border-radius:50%;background:#c8aa50;margin-right:6px;"></span>Ainary
          </a>
          <p style="color:#55555e;font-size:0.7rem;margin-top:12px;letter-spacing:0.02em;">HUMAN × AI SYSTEMS = LEVERAGE</p>
        </div>
        <div>
          <h4 style="font-size:0.75rem;font-weight:500;margin-bottom:16px;letter-spacing:0.04em;color:#ededf0;">${t.explore}</h4>
          <div style="display:flex;flex-direction:column;gap:10px;">
            <a href="${blogLink}" style="color:#55555e;text-decoration:none;font-size:0.8rem;">${t.blog}</a>
            <a href="${aboutLink}" style="color:#55555e;text-decoration:none;font-size:0.8rem;">${t.about}</a>
            <a href="${resourcesLink}" style="color:#55555e;text-decoration:none;font-size:0.8rem;">${t.resources}</a>
          </div>
        </div>
        <div>
          <h4 style="font-size:0.75rem;font-weight:500;margin-bottom:16px;letter-spacing:0.04em;color:#ededf0;">${t.connect}</h4>
          <div style="display:flex;flex-direction:column;gap:10px;">
            <a href="https://www.linkedin.com/in/florian-ziesche-352b7249/" target="_blank" style="color:#55555e;text-decoration:none;font-size:0.8rem;">LinkedIn</a>
            <a href="https://finitematter.substack.com/" target="_blank" style="color:#55555e;text-decoration:none;font-size:0.8rem;">Substack</a>
            <a href="https://github.com/fziescheus-alt/agenttrust" target="_blank" style="color:#55555e;text-decoration:none;font-size:0.8rem;">GitHub</a>
          </div>
        </div>
        <div>
          <h4 style="font-size:0.75rem;font-weight:500;margin-bottom:16px;letter-spacing:0.04em;color:#ededf0;">${t.legal}</h4>
          <div style="display:flex;flex-direction:column;gap:10px;">
            <a href="${privacyLink}" style="color:#55555e;text-decoration:none;font-size:0.8rem;">${t.privacy}</a>
            <a href="${termsLink}" style="color:#55555e;text-decoration:none;font-size:0.8rem;">${t.terms}</a>
            <a href="${imprintLink}" style="color:#55555e;text-decoration:none;font-size:0.8rem;">${t.imprint}</a>
          </div>
        </div>
      </div>
      <div style="max-width:1200px;margin:0 auto;padding:16px 24px 0;border-top:1px solid rgba(255,255,255,0.06);display:flex;justify-content:space-between;align-items:center;">
        <p style="color:#55555e;font-size:0.7rem;">${t.rights}</p>
        <div style="display:flex;gap:12px;font-size:0.7rem;">
          <span style="color:${isDE ? '#55555e' : '#ededf0'};font-weight:${isDE ? '400' : '500'};${isDE ? '' : ''}"><a href="${isDE ? switchHref : '#'}" style="color:inherit;text-decoration:none;${isDE ? '' : 'pointer-events:none;'}">EN</a></span>
          <span style="color:${isDE ? '#ededf0' : '#55555e'};font-weight:${isDE ? '500' : '400'};"><a href="${isDE ? '#' : switchHref}" style="color:inherit;text-decoration:none;${isDE ? 'pointer-events:none;' : ''}">DE</a></span>
        </div>
      </div>
    </footer>
  `;
})();
