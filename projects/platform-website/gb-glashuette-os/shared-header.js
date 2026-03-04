// Shared Header — Unified across all portal pages
document.addEventListener("DOMContentLoaded", function () {
  const slot = document.getElementById("shared-header");
  if (!slot) return;

  const file = location.pathname.replace(/.*\//, "").replace(".html", "") || "index";

  // Navigation tabs with file mappings
  const tabs = [
    { label: "Übersicht", href: "index.html", keys: ["index"] },
    { label: "Analysen", href: "analyse.html", keys: ["analyse", "analyse-foerdermittel", "analyse-digitalisierung", "analyse-buergerstimmung", "analyse-uhrenindustrie", "analyse-glashuette", "analyse-nomos", "analyse-muehle", "analyse-lange", "analyse-gurofa", "analyse-loeffler", "analyse-badbelzig", "analyse-jena", "analyse-marburg", "analyse-dippoldiswalde", "analyse-gersheim", "analyse-smartregion-auf", "vergleich"] },
    { label: "Projekte", href: "projekte.html", keys: ["projekte"] },
    { label: "Wirtschaft", href: "wirtschaft.html", keys: ["wirtschaft", "firmen", "kommunen"] },
    { label: "Dokumente", href: "dokumente.html", keys: ["dokumente"] }
  ];

  // Time-based greeting
  const hour = new Date().getHours();
  const greet = hour < 12 ? "Guten Morgen" : hour < 18 ? "Guten Tag" : "Guten Abend";

  // Build nav tabs
  const navHTML = tabs.map(t => {
    const active = t.keys.includes(file);
    const style = active
      ? "padding:6px 14px;border-bottom:2px solid var(--accent);color:var(--accent);font-weight:500"
      : "padding:6px 14px;border-bottom:2px solid transparent;color:var(--light)";
    return '<a href="' + t.href + '" style="' + style + '" aria-label="' + t.label + '">' + t.label + '</a>';
  }).join("");

  slot.innerHTML =
    '<a href="#main-content" class="skip-link">Zum Inhalt springen</a>' +
    '<div class="portal-hdr" role="banner">' +
      '<div style="display:flex;align-items:center;gap:8px">' +
        '<a href="index.html" style="display:flex;align-items:center;gap:8px;text-decoration:none;color:inherit">' +
          '<span class="brand-dot"></span><span class="brand-name">Ainary</span>' +
        '</a>' +
        '<span style="color:var(--border2);margin:0 2px">·</span>' +
        '<span style="color:var(--light-text);cursor:default">Abmelden</span>' +
      '</div>' +
      '<div class="sh-center" style="display:flex;align-items:center;gap:8px;color:var(--muted);font-family:var(--m);font-size:8pt">' +
        '<span>Glashütte</span><span>☁ 3°C</span>' +
      '</div>' +
      '<div class="sh-right" style="display:flex;align-items:center;gap:8px;font-family:var(--m);font-size:8pt;color:var(--muted)">' +
        '<span id="live-date"></span> <span id="live-time"></span>' +
      '</div>' +
    '</div>' +
    '<div style="font-size:22pt;font-weight:700;letter-spacing:-.02em;margin-bottom:2px">' +
      '<span id="greeting">' + greet + '</span>, Herr Gleißberg.</div>' +
    '<div style="font-size:10pt;color:var(--text2);margin-bottom:4px">Ihre Wochen-Übersicht für Glashütte.</div>' +
    '<div style="height:1px;background:var(--border2);margin-bottom:8px"></div>' +
    '<div class="sh-nav" style="display:flex;gap:0;font-family:var(--m);font-size:7.5pt;margin-bottom:20px;overflow-x:auto;-webkit-overflow-scrolling:touch;white-space:nowrap">' +
      navHTML +
    '</div>';

  // Mark as loaded (prevents layout shift flash)
  slot.classList.add("loaded");

  // Live clock
  function updateClock() {
    const now = new Date();
    const days = ["So", "Mo", "Di", "Mi", "Do", "Fr", "Sa"];
    const months = ["01","02","03","04","05","06","07","08","09","10","11","12"];
    const d = document.getElementById("live-date");
    const t = document.getElementById("live-time");
    if (d) d.textContent = days[now.getDay()] + ", " + String(now.getDate()).padStart(2,"0") + "." + months[now.getMonth()] + "." + now.getFullYear();
    if (t) t.textContent = String(now.getHours()).padStart(2,"0") + ":" + String(now.getMinutes()).padStart(2,"0");
  }
  updateClock();
  setInterval(updateClock, 30000);
});
