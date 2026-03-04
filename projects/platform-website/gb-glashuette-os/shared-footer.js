// Shared Footer — Unified across all portal pages
document.addEventListener("DOMContentLoaded", function () {
  var slot = document.getElementById("shared-footer");
  if (!slot) return;
  slot.style.maxWidth = 'var(--page-max, 820px)';
  slot.style.margin = '0 auto';
  slot.style.padding = '0 var(--page-pad, 48px)';
  slot.innerHTML =
    '<footer style="text-align:center;padding:24px 0;border-top:1px solid var(--border2);margin-top:48px;font-family:var(--m);font-size:7pt;color:#bbb">' +
      '© 2026 Ainary · ' +
      '<a href="methodik.html" style="color:#bbb">Methodik</a> · ' +
      '<a href="https://ainaryventures.com/de/privacy.html" target="_blank" style="color:#bbb">Datenschutz</a> · ' +
      '<a href="ueber-ainary.html" style="color:#bbb">Kontakt</a>' +
    '</footer>';
});
