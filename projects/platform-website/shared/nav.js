// Shared Navigation — shared/nav.js
// Usage: <div id="site-nav"></div>

(function() {
  const el = document.getElementById('site-nav');
  if (!el) return;

  const path = window.location.pathname;
  const page = path.split('/').pop() || 'index.html';

  function activeClass(target) {
    return target === page ? ' active' : '';
  }

  el.innerHTML = `
    <nav class="nav">
      <div class="nav-container">
        <a href="index.html" class="nav-logo"><span class="logo-dot-wrap"><span class="logo-dot-ring2"></span><span class="logo-dot-ring1"></span><span class="logo-dot"></span></span>Ainary</a>
        <div class="nav-links">
          <a href="daily-brief.html" class="nav-link${activeClass('daily-brief.html')}">Daily Briefing</a>
          <a href="blog.html" class="nav-link${activeClass('blog.html')}">Building in Public</a>
        </div>
        <div class="nav-auth" style="display:flex;align-items:center;gap:16px;">
          <a href="https://calendly.com/florian-ainaryventures/15-minutes-chat" class="btn-primary" style="padding:8px 16px;font-size:0.875rem;">Get in touch</a>
        </div>
        <div class="hamburger" style="display:none;" onclick="this.classList.toggle('active');document.querySelector('.mobile-menu').classList.toggle('open');">
          <span></span><span></span><span></span>
        </div>
      </div>
    </nav>
    <div class="mobile-menu">
      <a href="daily-brief.html">Daily Briefing</a>
      <a href="blog.html">Building in Public</a>
      <a href="https://calendly.com/florian-ainaryventures/15-minutes-chat" class="btn-primary">Get in touch</a>
    </div>
  `;
})();
