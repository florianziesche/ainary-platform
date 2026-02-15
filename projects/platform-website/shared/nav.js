// Shared Navigation — shared/nav.js
// Usage: <div id="site-nav"></div>

(function() {
  const el = document.getElementById('site-nav');
  if (!el) return;

  const path = window.location.pathname;
  const page = path.split('/').pop() || 'index.html';
  const isIndex = (page === 'index.html' || page === '' || page === 'landing.html');
  const researchHref = isIndex ? '#research' : 'reports.html';

  function activeClass(target) {
    if (target === page) return ' active';
    if (target === 'reports.html' && page === 'reports.html') return ' active';
    return '';
  }

  el.innerHTML = `
    <nav class="nav">
      <div class="nav-container">
        <a href="/" class="nav-logo"><span class="logo-dot-wrap"><span class="logo-dot-ring2"></span><span class="logo-dot-ring1"></span><span class="logo-dot"></span></span>Ainary</a>
        <div class="nav-links">
          <a href="${researchHref}" class="nav-link${activeClass('reports.html')}">Research</a>
          <a href="use-cases.html" class="nav-link${activeClass('use-cases.html')}">Use Cases</a>
          <a href="blog.html" class="nav-link${activeClass('blog.html')}">Blog</a>
        </div>
        <div class="nav-auth" style="display:flex;align-items:center;gap:16px;">
          <a href="https://calendly.com/florian-ainaryventures/15-minutes-chat" class="btn-primary" style="padding:8px 16px;font-size:0.8rem;">Get in touch</a>
        </div>
        <div class="hamburger" style="display:none;" onclick="this.classList.toggle('active');document.querySelector('.mobile-menu').classList.toggle('open');">
          <span></span><span></span><span></span>
        </div>
      </div>
    </nav>
    <div class="mobile-menu">
      <a href="${researchHref}">Research</a>
      <a href="use-cases.html">Use Cases</a>
      <a href="blog.html">Blog</a>
      <a href="https://calendly.com/florian-ainaryventures/15-minutes-chat" class="btn-primary" style="padding:12px 24px;font-size:0.9rem;">Get in touch</a>
    </div>
  `;
})();
