// CTA Footer + Related Analyses — auto-inject on all pages
document.addEventListener("DOMContentLoaded",function(){
  const footer=document.querySelector(".footer,footer");
  if(!footer) return;

  // Determine page context for related analyses
  const p=location.pathname;
  let related=[];

  const ALL={
    "foerdermittel":{title:"Fördermittel-Komplettscan",desc:"11 Programme, 3 mit Frist in 8 Wochen.",url:"analyse-foerdermittel.html",meta:"78% Confidence"},
    "digitalisierung":{title:"Digitalisierungsstrategie",desc:"Glashütte 1/6 Services vs. Dippoldiswalde 5/6.",url:"analyse-digitalisierung.html",meta:"75% Confidence"},
    "buergerstimmung":{title:"Bürgerstimmung 90-Tage",desc:"Windkraft 46%, 78% negativ.",url:"analyse-buergerstimmung.html",meta:"65% Confidence"},
    "uhrenindustrie":{title:"Uhrenindustrie Marktbericht",desc:"Markt stabil (+3.2%).",url:"analyse-uhrenindustrie.html",meta:"60% Confidence"},
    "vergleich":{title:"Digitalisierungsvergleich",desc:"22 Kommunen, 3 Stufen.",url:"vergleich.html",meta:"72% Confidence"},
    "wirtschaft":{title:"Wirtschaftsstandort",desc:"167 Unternehmen, 12 Einzelanalysen.",url:"wirtschaft.html",meta:"12 Analysen"},
    "nomos":{title:"Firmenanalyse Nomos",desc:"Interessantester KI-Kandidat.",url:"analyse-nomos.html",meta:"72% Confidence"},
    "muehle":{title:"Firmenanalyse Mühle",desc:"BSH-Zertifizierung, EFRE 60%.",url:"analyse-muehle.html",meta:"68% Confidence"},
    "glashuette":{title:"Kommunalanalyse Glashütte",desc:"6.657 EW, Stufe Initial.",url:"analyse-glashuette.html",meta:"75% Confidence"},
    "badbelzig":{title:"Kommunalanalyse Bad Belzig",desc:"Strukturzwilling, Stufe Etabliert.",url:"analyse-badbelzig.html",meta:"80% Confidence"},
    "jena":{title:"Kommunalanalyse Jena",desc:"€17,5M Smart City.",url:"analyse-jena.html",meta:"85% Confidence"},
  };

  // Select 3 related based on context
  if(p.includes("analyse-nomos")||p.includes("analyse-muehle")||p.includes("analyse-lange")||p.includes("analyse-gurofa")||p.includes("analyse-loeffler")){
    // Firma → Fördermittel + Wirtschaft + another firma
    related=["foerdermittel","wirtschaft"];
    if(!p.includes("nomos")) related.push("nomos"); else related.push("muehle");
  } else if(p.includes("analyse-glashuette")||p.includes("analyse-dippoldi")||p.includes("analyse-jena")||p.includes("analyse-marburg")||p.includes("analyse-gersheim")||p.includes("analyse-badbelzig")||p.includes("analyse-smartregion")){
    // Kommune → Vergleich + other kommune + Fördermittel
    related=["vergleich","foerdermittel"];
    if(!p.includes("badbelzig")) related.push("badbelzig"); else related.push("glashuette");
  } else if(p.includes("vergleich")){
    related=["glashuette","badbelzig","foerdermittel"];
  } else if(p.includes("wirtschaft")){
    related=["nomos","vergleich","foerdermittel"];
  } else if(p.includes("analyse-foerdermittel")){
    related=["digitalisierung","vergleich","wirtschaft"];
  } else if(p.includes("analyse-digitalisierung")){
    related=["foerdermittel","vergleich","buergerstimmung"];
  } else if(p.includes("analyse-buergerstimmung")){
    related=["digitalisierung","foerdermittel","uhrenindustrie"];
  } else if(p.includes("analyse-uhrenindustrie")){
    related=["wirtschaft","nomos","foerdermittel"];
  } else if(p.includes("analyse.html")){
    related=["foerdermittel","vergleich","wirtschaft"];
  } else if(p.includes("projekte")){
    related=["foerdermittel","digitalisierung","vergleich"];
  } else if(p.includes("dokumente")){
    related=["foerdermittel","vergleich","wirtschaft"];
  } else {
    // index/default
    related=["foerdermittel","vergleich","wirtschaft"];
  }

  // Build related cards HTML
  let cardsHTML="";
  related.forEach(key=>{
    const a=ALL[key];
    if(!a) return;
    cardsHTML+=`<a href="${a.url}" style="display:block;border:1px solid var(--border2);border-radius:6px;padding:12px 16px;text-decoration:none;color:inherit;transition:border-color .12s">
      <div style="font-weight:600;font-size:9pt;margin-bottom:3px">${a.title}</div>
      <div style="font-size:7.5pt;color:var(--text2);margin-bottom:4px">${a.desc}</div>
      <div style="font-family:var(--m);font-size:6.5pt;color:var(--accent)">${a.meta} · Lesen \u2192</div>
    </a>`;
  });

  // Build CTA section
  const section=document.createElement("div");
  section.style.cssText="margin-top:32px;padding-top:24px;border-top:1px solid var(--border2,#e8e8e8)";
  section.innerHTML=`
    <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:12px;margin-bottom:24px">
      ${cardsHTML}
    </div>
    <div style="border:2px dashed var(--border2,#e8e8e8);border-radius:8px;padding:24px;text-align:center;margin-bottom:16px">
      <div style="font-size:9.5pt;color:var(--muted,#777);margin-bottom:12px">Eigene Analyse oder Projekt beauftragen</div>
      <div style="display:flex;justify-content:center;gap:24px;flex-wrap:wrap;font-size:8.5pt">
        <span style="color:var(--text2,#444);cursor:pointer" onclick="if(typeof sendChip==='function'){sendChip('Ich m\\u00f6chte ein eigenes Projekt anfragen.')}">&#9998; Projekt anfragen</span>
        <span style="color:var(--text2,#444);cursor:pointer" onclick="if(typeof sendChip==='function'){sendChip('Projektvorschlag')}">&#9673; Projektvorschlag</span>
        <span style="color:var(--text2,#444);cursor:pointer" onclick="if(typeof sendChip==='function'){sendChip('Dokument hochladen')}">&#8613; Dokument hochladen</span>
      </div>
      <div style="font-family:var(--m,monospace);font-size:6.5pt;color:var(--light,#bbb);margin-top:10px">Beispiele: Wahleinblicke 2026 \u00b7 Tourismuskonzept \u00b7 Fachkr\u00e4fte-Kampagne \u00b7 Energie-Audit \u00b7 Gemeinderatsprotokolle</div>
      <div style="display:flex;justify-content:center;gap:16px;margin-top:10px;font-family:var(--m,monospace);font-size:6.5pt"><a href="#" onclick="event.preventDefault();window.print()" style="color:var(--light,#bbb)">Druckversion</a><span style="color:var(--light,#bbb)">\u00b7</span><a href="#" onclick="event.preventDefault();if(typeof sendChip==='function'){sendChip('Weiterempfehlen')}" style="color:var(--light,#bbb)">Empfehlen</a></div>
    </div>
  `;

  footer.parentNode.insertBefore(section,footer);
});
