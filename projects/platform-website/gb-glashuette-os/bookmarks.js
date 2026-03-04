// Bookmark System — localStorage, no server
const BM_KEY="ainary_bookmarks";

function getBookmarks(){
  try{return JSON.parse(localStorage.getItem(BM_KEY))||[];}
  catch(e){return[];}
}
function isBookmarked(id){return getBookmarks().includes(id);}
function toggleBookmark(id){
  let bm=getBookmarks();
  if(bm.includes(id)){bm=bm.filter(b=>b!==id);}
  else{bm.push(id);}
  localStorage.setItem(BM_KEY,JSON.stringify(bm));
  updateBookmarkIcons();
  updateBookmarkSection();
  return bm.includes(id);
}

// All available analyses with metadata
const ANALYSES={
  "analyse-foerdermittel":{title:"Fördermittel-Komplettscan",desc:"11 Programme identifiziert, 3 mit Frist in 8 Wochen.",meta:"23 Quellen · 14 Seiten · 78% Confidence",aufwand:"~24–40 Std. · Einsparpotenzial €1.320–2.200",url:"analyse-foerdermittel.html"},
  "analyse-digitalisierung":{title:"Digitalisierungsstrategie",desc:"Glashütte 1/6 Services vs. Dippoldiswalde 5/6. Quick Win möglich.",meta:"18 Quellen · 11 Seiten · 75% Confidence",aufwand:"~14–22 Std. · Einsparpotenzial €770–1.210",url:"analyse-digitalisierung.html"},
  "analyse-buergerstimmung":{title:"Bürgerstimmung 90-Tage",desc:"Windkraft dominiert 46% der Diskussion, 78% negativ.",meta:"15 Quellen · 9 Seiten · 65% Confidence",aufwand:"~18–30 Std. · Einsparpotenzial €990–1.650",url:"analyse-buergerstimmung.html"},
  "analyse-uhrenindustrie":{title:"Uhrenindustrie Marktbericht",desc:"Markt stabil (+3.2%). Kein Gegenwind. Leichte Sorge Mittelsegment.",meta:"11 Quellen · 8 Seiten · 60% Confidence",aufwand:"~9–15 Std. · Einsparpotenzial €495–825",url:"analyse-uhrenindustrie.html"},
  "vergleich":{title:"Digitalisierungsvergleich",desc:"22 Kommunen im Querschnitt. 3 Stufen: Initial, Entwicklung, Etabliert.",meta:"34 Quellen · 72% Confidence",aufwand:"~40–60 Std. · Einsparpotenzial €2.200–3.300",url:"vergleich.html"},
  "analyse-nomos":{title:"Firmenanalyse Nomos",desc:"Interessantester KI-Kandidat. EFRE + ZIM förderfähig.",meta:"5 Quellen · 72% Confidence",aufwand:"~8–12 Std. · Einsparpotenzial €440–660",url:"analyse-nomos.html"},
  "analyse-glashuette":{title:"Kommunalanalyse Glashütte",desc:"6.657 EW, 14 Ortsteile. Digitalisierungs-Stufe: Initial.",meta:"8 Quellen · 75% Confidence",aufwand:"~15–25 Std. · Einsparpotenzial €825–1.375",url:"analyse-glashuette.html"},
  "analyse-badbelzig":{title:"Kommunalanalyse Bad Belzig",desc:"Strukturzwilling. €5,4M Smart City. Stufe: Etabliert.",meta:"6 Quellen · 80% Confidence",aufwand:"~12–18 Std. · Einsparpotenzial €660–990",url:"analyse-badbelzig.html"}
};

function updateBookmarkIcons(){
  document.querySelectorAll("[data-bookmark]").forEach(el=>{
    const id=el.dataset.bookmark;
    const active=isBookmarked(id);
    el.innerHTML=active
      ?'<span style="display:inline-block;width:12px;height:12px;border-radius:50%;background:var(--accent,#9d7f3b);box-shadow:0 0 6px rgba(157,127,59,.45)"></span>'
      :'<span style="display:inline-block;width:12px;height:12px;border-radius:50%;border:1.5px solid var(--light,#bbb);background:transparent"></span>';
    el.title=active?"Lesezeichen entfernen":"Lesezeichen setzen";
  });
}

function updateBookmarkSection(){
  const container=document.getElementById("bookmarks-list");
  if(!container) return;
  const bm=getBookmarks();
  if(bm.length===0){
    container.innerHTML='<div style="font-size:8.5pt;color:var(--light);padding:12px 0">Noch keine Lesezeichen gesetzt. Klicken Sie \u2606 auf einer Analyse-Seite.</div>';
    return;
  }
  let html="";
  bm.forEach(id=>{
    const a=ANALYSES[id];
    if(!a) return;
    html+=`<a href="${a.url}" style="display:flex;align-items:center;gap:12px;padding:10px 14px;border:1px solid var(--border2);border-radius:6px;margin-bottom:6px;transition:background .12s;text-decoration:none;color:inherit">
      <span style="display:inline-block;width:10px;height:10px;border-radius:50%;background:var(--accent);box-shadow:0 0 5px rgba(157,127,59,.4)"></span>
      <div style="flex:1">
        <div style="font-weight:600;font-size:9pt">${a.title}</div>
        <div style="font-family:var(--m);font-size:7pt;color:var(--muted)">${a.meta}</div>
      </div>
      <span style="font-family:var(--m);font-size:7pt;color:var(--accent)">Öffnen \u2192</span>
    </a>`;
  });
  container.innerHTML=html;
}

document.addEventListener("DOMContentLoaded",function(){
  updateBookmarkIcons();
  updateBookmarkSection();
});
