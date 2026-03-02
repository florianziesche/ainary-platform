// Shared Navigation — shared/nav.js
// Usage: <div id="site-nav"></div>
// Language-aware: checks document.documentElement.lang

(function() {
  const el = document.getElementById('site-nav');
  if (!el) return;

  const lang = (document.documentElement.lang || 'en').toLowerCase().slice(0,2);
  const isDE = lang === 'de';

  const pathname = window.location.pathname;
  const inDE = pathname.includes('/de/');
  // Count depth below site root (or /de/ root for DE pages)
  // /de/anwendungen/ki-mittelstand.html → depth 2 from root, 1 from /de/
  // /de/blog.html → depth 1 from root, 0 from /de/
  // /blog/article.html → depth 1 from root
  const segments = pathname.replace(/^\//, '').replace(/[^/]+$/, '').split('/').filter(Boolean);
  const deIndex = segments.indexOf('de');
  const depthFromLang = isDE && deIndex >= 0 ? segments.length - deIndex - 1 : (inDE ? segments.length - 1 : segments.length);
  const prefix = '../'.repeat(depthFromLang) + (isDE && !inDE ? 'de/' : '');
  const page = pathname.split('/').pop() || 'index.html';

  function activeClass(target) {
    return target === page ? ' active' : '';
  }

  // Language switch link — only works for top-level pages
  const rootPrefix = '../'.repeat(depthFromLang + (isDE && inDE ? 1 : 0));
  const switchHref = isDE
    ? rootPrefix + page
    : rootPrefix + 'de/' + page;
  const switchLabel = isDE ? 'EN' : 'DE';

  const t = {
    blog: 'Building in Public',
    useCases: isDE ? 'Anwendungen' : 'Use Cases',
    contact: isDE ? 'Kontakt aufnehmen' : 'Get in touch',
  };

  const blogLink = prefix + 'blog.html';
  const useCasesLink = isDE ? prefix + 'anwendungen.html' : prefix + 'de/anwendungen.html';
  const contactLink = prefix + 'contact.html';

  el.innerHTML = `
    <nav class="nav">
      <div class="nav-container">
        <a href="${prefix}index.html" class="nav-logo" style="text-decoration:none"><span class="logo-dot-wrap"><span class="logo-dot-ring2"></span><span class="logo-dot-ring1"></span><span class="logo-dot"></span></span>Ainary</a>
        <div class="nav-links">
          <a href="${blogLink}" class="nav-link${activeClass('blog.html')}" style="font-size:0.875rem;color:var(--text-secondary);text-decoration:none;">${t.blog}</a>
        </div>
        <div class="nav-auth" style="display:flex;align-items:center;gap:16px;">
          <a href="${switchHref}" style="color:#8b8b95;font-size:0.75rem;text-decoration:none;font-weight:400;margin-right:8px;">${switchLabel}</a>
          <a href="${contactLink}" class="btn-primary" style="padding:8px 16px;font-size:0.875rem;">${t.contact}</a>
        </div>
        <div class="hamburger" style="display:none;" onclick="this.classList.toggle('active');document.querySelector('.mobile-menu').classList.toggle('open');">
          <span></span><span></span><span></span>
        </div>
      </div>
    </nav>
    <div class="mobile-menu">
      <a href="${blogLink}" style="font-size:0.95rem;color:var(--text-secondary);text-decoration:none;">${t.blog}</a>
      <a href="${contactLink}" class="btn-primary">${t.contact}</a>
      <a href="${switchHref}" style="font-size:0.85rem;color:#55555e;">${isDE ? 'EN' : 'DE'}</a>
    </div>
  `;
})();
