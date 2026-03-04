// Mia Chat — Shared across all pages, context-aware
function toggleMia(){const b=document.getElementById("mia-body"),l=document.getElementById("mia-toggle-label");if(b.classList.contains("open")){b.classList.remove("open");l.textContent="\u2193"}else{b.classList.add("open");l.textContent="\u2191";document.getElementById("mia-input").focus()}}

// ── Base responses ──
const MIA_R={
"fördermittel":["11 F\u00f6rderprogramme f\u00fcr Glash\u00fctte identifiziert. Top 3: Kulturraum (Frist 31.08.), Glasfaser-Bundesf\u00f6rderung, Smarte Regionen."],
"windkraft":["Windkraft: 46% der B\u00fcrgerdiskussionen, 78% negativ. 342 Posts analysiert."],
"digital":["Glash\u00fctte: 1/6 digitale Services vs. Dippoldiswalde 5/6. Gleicher Anbieter, 2\u20134 Wochen Umsetzung."],
"uhren":["Luxusuhrenmarkt stabil (+3.2%). Alle Glash\u00fctter Manufakturen im Luxussegment."],
"projektvorschlag":["Basierend auf Ihrem Profil:<br><br><strong>1. Tourismuskonzept Uhrenstadt</strong> (~85% Confidence)<br><strong>2. Fachkr\u00e4fte-Kampagne</strong> (~70% Confidence)<br><strong>3. Energie-Audit Kommune</strong> (~75% Confidence)"],
"termin":["Ich verbinde Sie mit Florian Ziesche.<br><a href='https://calendly.com/florian-ainaryventures/15-minutes-chat' style='color:var(--accent);font-weight:600;font-size:8pt' target='_blank'>30-Minuten-Termin buchen \u2192</a>"],
"danke":["Gern geschehen. Ich bin hier wenn Sie Fragen haben."],
"empfehlung":["Hier ist eine Vorlage f\u00fcr eine Empfehlung an einen Kollegen oder eine Kollegin:<br><br><div style='background:#fff;border:1px solid var(--border2);border-radius:6px;padding:12px;margin:8px 0;font-size:8pt;line-height:1.6;color:var(--text)'><strong>Betreff:</strong> Digitalisierungsanalyse f\u00fcr Ihre Kommune<br><br>Liebe Kollegin, lieber Kollege,<br><br>im Rahmen einer Standortanalyse wurde unsere Verwaltung hinsichtlich Digitalisierungspotenzial und F\u00f6rderm\u00f6glichkeiten untersucht \u2014 mit Vergleichsdaten zu anderen Kommunen und konkreten Handlungsfeldern.<br><br>Das Ergebnis war aufschlussreich. Ich denke, das k\u00f6nnte auch f\u00fcr Ihre Gemeinde interessant sein.<br><br>Link: https://florianziesche.github.io/ainary-demo-v11/<br><br>Bei Interesse kann ich den Kontakt herstellen.<br><br>Mit freundlichen Gr\u00fc\u00dfen<br><em>[Unterschrift B\u00fcrgermeister/in]</em></div><button onclick=\"navigator.clipboard.writeText('Betreff: Digitalisierungsanalyse f\\u00fcr Ihre Kommune\\n\\nLiebe Kollegin, lieber Kollege,\\n\\nim Rahmen einer Standortanalyse wurde unsere Verwaltung hinsichtlich Digitalisierungspotenzial und F\\u00f6rderm\\u00f6glichkeiten untersucht \\u2014 mit Vergleichsdaten zu anderen Kommunen und konkreten Handlungsfeldern.\\n\\nDas Ergebnis war aufschlussreich. Ich denke, das k\\u00f6nnte auch f\\u00fcr Ihre Gemeinde interessant sein.\\n\\nLink: https://florianziesche.github.io/ainary-demo-v11/\\n\\nBei Interesse kann ich den Kontakt herstellen.\\n\\nMit freundlichen Gr\\u00fc\\u00dfen\\n[Unterschrift B\\u00fcrgermeister/in]');this.textContent='\u2713 Kopiert';setTimeout(()=>this.textContent='Text kopieren',2000)\" style='margin-top:6px;padding:5px 12px;border:1px solid var(--border2);border-radius:4px;font-family:var(--m);font-size:7pt;color:var(--accent);cursor:pointer;background:none'>Text kopieren</button>"]
};

// ── Page Facts: Real numbers from each page ──
const PAGE_FACTS={
"index":[
  "Auf dieser Seite: <strong>12 Arbeitstage</strong> bisher eingespart — das ist Woche 1 von 52.",
  "<strong>71% Confidence</strong> im Durchschnitt über alle Analysen, quellengewichtet aus 79 Quellen.",
  "Identifiziertes Potenzial: <strong>€215k–580k</strong> — davon €200-500k aus Fördermitteln, €15k/Jahr Verwaltungseinsparung."
],
"analyse":[
  "<strong>29 von 100 Mitarbeitern</strong> gehen bis 2036 in Rente. 9 davon sind voraussichtlich nicht nachbesetzbar (Nichtbesetzungsquote 31%, Demografieportal 2024). <span class='tag tag-i'>I</span>",
  "<strong>40% der Verwaltungsaufgaben</strong> sind Routine — potenziell automatisierbar.",
  "73% der Betriebe in Sachsen finden keine ausreichend qualifizierten Bewerber (DIHK Ausbildungsumfrage, 2025). <span class='tag tag-e'>E</span>"
],
"projekte":[
  "<strong>6 KI-Anwendungen</strong> sofort umsetzbar — Einsparpotenzial ~240 Std./Jahr über alle.",
  "Tages-Briefing spart <strong>8 Std./Woche</strong>. Bürgeranfragen: 5 Std./Woche.",
  "Phase 02 (Pilotbetrieb) dauert <strong>4–6 Wochen</strong> mit 3 Sachbearbeitern."
],
"dokumente":[
  "<strong>6 Dokumente</strong> verfügbar, basierend auf 79 Quellen. 3 weitere in Vorbereitung.",
  "Höchste Confidence: Fördermittel-Komplettscan (<strong>78%</strong>, 23 Quellen)."
],
"wirtschaft":[
  "<strong>167 Unternehmen</strong> in Glashütte erfasst. 5 Uhrenmanufakturen + 13 Gewerbe & Dienstleister detailliert.",
  "Uhrenindustrie: Luxussegment stabil (+3,2%), alle Glashütter Manufakturen im Hochpreisbereich. <span class='tag tag-e'>E</span>"
],
"vergleich":[
  "<strong>22 Kommunen</strong> im Vergleich — 3 Reifegradstufen nach DESI/CMMI.",
  "Glashütte: Stufe <strong>Initial</strong> (1/6 Online-Services). Dippoldiswalde: Stufe Entwicklung (5/6). <span class='tag tag-e'>E</span>",
  "Bad Belzig (11.436 EW) zeigt als Smart-City-Modellprojekt was möglich ist: €5,4M Förderung, eigene Bürger-App. <span class='tag tag-e'>E</span>"
],
"analyse-foerdermittel":[
  "<strong>11 Förderprogramme</strong> identifiziert — 3 mit Frist in den nächsten 8 Wochen.",
  "Geschätztes Fördervolumen bei Erfolg: <strong>€200.000–500.000</strong> über 2–3 Jahre. <span class='tag tag-a'>A</span>",
  "EFRE Sachsen: bis 50% Zuschuss für KMU — aber <strong>nicht für Kommunen direkt</strong>. Nur über kommunale Unternehmen oder KMU im Gemeindegebiet."
],
"analyse-digitalisierung":[
  "Glashütte bietet <strong>1 von 6</strong> Online-Services. Dippoldiswalde im selben Landkreis: 5 von 6. <span class='tag tag-e'>E</span>",
  "OZG-Umsetzung bundesweit: <strong>196 von 575</strong> Leistungen digitalisiert (BMI, Feb 2025). <span class='tag tag-e'>E</span>",
  "Gleicher IT-Dienstleister — Umsetzung in 2–4 Wochen möglich. <span class='tag tag-i'>I</span>"
],
"analyse-buergerstimmung":[
  "<strong>342 Posts</strong> analysiert. Windkraft dominiert mit 46% aller Diskussionen, 78% negativ.",
  "Bürgerthemen Top 3: <strong>Windkraft</strong> (46%), <strong>Infrastruktur</strong> (23%), <strong>Tourismus</strong> (15%). <span class='tag tag-e'>E</span>"
],
"analyse-uhrenindustrie":[
  "Globaler Luxusuhrenmarkt: <strong>+3,2% Wachstum</strong>. Schweizer Exporte €24,1 Mrd. (FH, 2024). <span class='tag tag-e'>E</span>",
  "Alle 5 Glashütter Manufakturen im Luxussegment (>€1.000). 3 von 5 mit eigenen Kalibern."
]
};

// ── Per-page context (firma/kommune) ──
const MIA_CTX={
"nomos":{type:"firma",name:"Nomos Glash\u00fctte",greeting:"Fragen zu Nomos Glash\u00fctte?",
  info:["Nomos ist als unabh\u00e4ngige Manufaktur mit eigenem Kaliber (DUW) der interessanteste Kandidat f\u00fcr KI-Beratung in Glash\u00fctte. F\u00f6rderf\u00e4hig \u00fcber EFRE (bis 50%) und ZIM (bis \u20ac380.000). <span class='tag tag-e'>E</span>"],
  brief:"Sehr geehrte Damen und Herren der Nomos Glash\u00fctte/SA Roland Schwertner KG,\\n\\nim Rahmen einer Standortanalyse f\u00fcr Glash\u00fctte wurden die ans\u00e4ssigen Unternehmen hinsichtlich Digitalisierungspotenzial und F\u00f6rderm\u00f6glichkeiten untersucht. F\u00fcr Ihr Unternehmen wurden folgende Ergebnisse ermittelt:\\n\\n\u2022 EFRE Sachsen: bis 50% Zuschuss f\u00fcr Digitalisierungsprojekte (KMU, unabh\u00e4ngig, Standort Sachsen)\\n\u2022 ZIM: bis \u20ac380.000 f\u00fcr F&E-Projekte (eigene Kaliber-Entwicklung qualifiziert)\\n\\nDie vollst\u00e4ndige Analyse ist einsehbar unter:\\nhttps://florianziesche.github.io/ainary-demo-v11/analyse-nomos.html\\n\\nF\u00fcr R\u00fcckfragen stehe ich Ihnen gern zur Verf\u00fcgung.\\n\\nMit freundlichen Gr\u00fc\u00dfen\\n[Unterschrift B\u00fcrgermeister/in]",
  briefHTML:"<strong>Betreff:</strong> Standortanalyse Glash\u00fctte \u2014 Ergebnisse f\u00fcr Nomos<br><br>Sehr geehrte Damen und Herren der Nomos Glash\u00fctte/SA Roland Schwertner KG,<br><br>im Rahmen einer Standortanalyse f\u00fcr Glash\u00fctte wurden die ans\u00e4ssigen Unternehmen hinsichtlich Digitalisierungspotenzial und F\u00f6rderm\u00f6glichkeiten untersucht. F\u00fcr Ihr Unternehmen wurden folgende Ergebnisse ermittelt:<br><br>\u2022 EFRE Sachsen: bis 50% Zuschuss f\u00fcr Digitalisierungsprojekte <span class='tag tag-e'>E</span><br>\u2022 ZIM: bis \u20ac380.000 f\u00fcr F&amp;E-Projekte <span class='tag tag-e'>E</span><br><br>Die vollst\u00e4ndige Analyse: <a href='analyse-nomos.html' style='color:var(--accent)'>analyse-nomos.html</a><br><br>F\u00fcr R\u00fcckfragen stehe ich Ihnen gern zur Verf\u00fcgung.<br><br>Mit freundlichen Gr\u00fc\u00dfen<br><em>[Unterschrift B\u00fcrgermeister/in]</em>"},
"muehle":{type:"firma",name:"M\u00fchle-Glash\u00fctte",greeting:"Fragen zu M\u00fchle-Glash\u00fctte?",
  info:["M\u00fchle-Glash\u00fctte ist ein Familienunternehmen seit 1869 mit BSH-Zertifizierung als Alleinstellungsmerkmal. F\u00f6rderf\u00e4hig \u00fcber EFRE Heranf\u00fchrung (60%) und ZIM Kooperationsprojekte. <span class='tag tag-e'>E</span>"],
  brief:"Sehr geehrte Damen und Herren der M\u00fchle-Glash\u00fctte GmbH nautische Instrumente und Feinmechanik,\\n\\nim Rahmen einer Standortanalyse f\u00fcr Glash\u00fctte wurden die ans\u00e4ssigen Unternehmen hinsichtlich Digitalisierungspotenzial und F\u00f6rderm\u00f6glichkeiten untersucht. F\u00fcr Ihr Unternehmen wurden folgende Ergebnisse ermittelt:\\n\\n\u2022 EFRE Heranf\u00fchrung: bis 60% Zuschuss als Familienunternehmen\\n\u2022 BSH-Zertifizierungsprozess: Potenzial f\u00fcr KI-gest\u00fctzte Qualit\u00e4tssicherung\\n\\nDie vollst\u00e4ndige Analyse ist einsehbar unter:\\nhttps://florianziesche.github.io/ainary-demo-v11/analyse-muehle.html\\n\\nF\u00fcr R\u00fcckfragen stehe ich Ihnen gern zur Verf\u00fcgung.\\n\\nMit freundlichen Gr\u00fc\u00dfen\\n[Unterschrift B\u00fcrgermeister/in]",
  briefHTML:"<strong>Betreff:</strong> Standortanalyse Glash\u00fctte \u2014 Ergebnisse f\u00fcr M\u00fchle<br><br>Sehr geehrte Damen und Herren der M\u00fchle-Glash\u00fctte GmbH,<br><br>im Rahmen einer Standortanalyse wurden folgende Ergebnisse ermittelt:<br><br>\u2022 EFRE Heranf\u00fchrung: bis 60% Zuschuss <span class='tag tag-e'>E</span><br>\u2022 BSH-Zertifizierung: Potenzial f\u00fcr KI-gest\u00fctzte Qualit\u00e4tssicherung <span class='tag tag-i'>I</span><br><br>Analyse: <a href='analyse-muehle.html' style='color:var(--accent)'>analyse-muehle.html</a><br><br>Mit freundlichen Gr\u00fc\u00dfen<br><em>[Unterschrift B\u00fcrgermeister/in]</em>"},
"lange":{type:"firma",name:"A. Lange & S\u00f6hne",greeting:"Fragen zu A. Lange & S\u00f6hne?",
  info:["A. Lange & S\u00f6hne geh\u00f6rt zum Richemont-Konzern und ist damit nicht KMU-f\u00f6rderf\u00e4hig. Die Forschungszulage nach \u00a735c EStG (25% auf F&E) ist die einzige relevante F\u00f6rderoption. <span class='tag tag-e'>E</span>"],
  brief:"Sehr geehrte Damen und Herren der Lange Uhren GmbH,\\n\\nim Rahmen einer Standortanalyse f\u00fcr Glash\u00fctte wurden die ans\u00e4ssigen Unternehmen untersucht. Als Teil des Richemont-Konzerns gelten f\u00fcr Ihr Unternehmen besondere Rahmenbedingungen:\\n\\n\u2022 KMU-F\u00f6rderprogramme (EFRE, ZIM): nicht anwendbar (Konzernzugeh\u00f6rigkeit)\\n\u2022 Forschungszulage \u00a735c EStG: 25% auf F&E-Aufwendungen\\n\\nDie vollst\u00e4ndige Analyse: https://florianziesche.github.io/ainary-demo-v11/analyse-lange.html\\n\\nMit freundlichen Gr\u00fc\u00dfen\\n[Unterschrift B\u00fcrgermeister/in]",
  briefHTML:"<strong>Betreff:</strong> Standortanalyse Glash\u00fctte \u2014 Ergebnisse f\u00fcr Lange<br><br>Sehr geehrte Damen und Herren der Lange Uhren GmbH,<br><br>\u2022 KMU-F\u00f6rderprogramme: nicht anwendbar (Richemont) <span class='tag tag-e'>E</span><br>\u2022 Forschungszulage \u00a735c EStG: 25% auf F&amp;E <span class='tag tag-e'>E</span><br><br>Analyse: <a href='analyse-lange.html' style='color:var(--accent)'>analyse-lange.html</a><br><br>Mit freundlichen Gr\u00fc\u00dfen<br><em>[Unterschrift B\u00fcrgermeister/in]</em>"},
"gurofa":{type:"firma",name:"Gurofa GmbH",greeting:"Fragen zu Gurofa?",
  info:["Zur Gurofa GmbH liegen nur eingeschr\u00e4nkte \u00f6ffentliche Daten vor. Die Analyse basiert \u00fcberwiegend auf Branchen-Ableitungen f\u00fcr Feinmechanik-Zulieferer. Confidence: 35%. <span class='tag tag-a'>A</span>"],
  brief:"Sehr geehrte Damen und Herren der Gurofa GmbH,\\n\\nim Rahmen einer Standortanalyse f\u00fcr Glash\u00fctte wurden die ans\u00e4ssigen Unternehmen untersucht. F\u00fcr Ihr Unternehmen liegen begrenzte \u00f6ffentliche Informationen vor:\\n\\n\u2022 Branche: Feinmechanik (Zulieferer)\\n\u2022 F\u00f6rderm\u00f6glichkeiten: EFRE Sachsen grunds\u00e4tzlich m\u00f6glich\\n\\nF\u00fcr eine fundierte Analyse w\u00e4ren weitere Informationen hilfreich. Die bisherigen Ergebnisse: https://florianziesche.github.io/ainary-demo-v11/analyse-gurofa.html\\n\\nMit freundlichen Gr\u00fc\u00dfen\\n[Unterschrift B\u00fcrgermeister/in]",
  briefHTML:"<strong>Betreff:</strong> Standortanalyse Glash\u00fctte \u2014 Gurofa GmbH<br><br>Sehr geehrte Damen und Herren der Gurofa GmbH,<br><br>\u2022 Branche: Feinmechanik (Zulieferer) <span class='tag tag-a'>A</span><br>\u2022 EFRE Sachsen: grunds\u00e4tzlich m\u00f6glich <span class='tag tag-i'>I</span><br><br>F\u00fcr eine fundierte Analyse w\u00e4ren weitere Informationen hilfreich.<br>Bisherige Ergebnisse: <a href='analyse-gurofa.html' style='color:var(--accent)'>analyse-gurofa.html</a><br><br>Mit freundlichen Gr\u00fc\u00dfen<br><em>[Unterschrift B\u00fcrgermeister/in]</em>"},
"loeffler":{type:"firma",name:"Ingo L\u00f6ffler Steuerberatung",greeting:"Fragen zur Steuerberatung L\u00f6ffler?",
  info:["Steuerberatung L\u00f6ffler ist als Freiberufler EFRE-f\u00f6rderf\u00e4hig (Heranf\u00fchrung 60%). Die Branche hat einen Fachkr\u00e4ftemangel von ~25.000 Stellen (DStV 2023). DATEV bietet seit 2024 KI-Belegerfassung. <span class='tag tag-e'>E</span>"],
  brief:"Sehr geehrter Herr L\u00f6ffler,\\n\\nim Rahmen einer Standortanalyse f\u00fcr Glash\u00fctte wurden die ans\u00e4ssigen Unternehmen untersucht. F\u00fcr Ihre Kanzlei wurden folgende Ergebnisse ermittelt:\\n\\n\u2022 EFRE Heranf\u00fchrung: 60% Zuschuss (auch f\u00fcr Freiberufler)\\n\u2022 Branche: ~25.000 fehlende Fachkr\u00e4fte bundesweit (DStV 2023)\\n\u2022 DATEV KI-Belegerfassung seit 2024 verf\u00fcgbar\\n\\nDie vollst\u00e4ndige Analyse: https://florianziesche.github.io/ainary-demo-v11/analyse-loeffler.html\\n\\nMit freundlichen Gr\u00fc\u00dfen\\n[Unterschrift B\u00fcrgermeister/in]",
  briefHTML:"<strong>Betreff:</strong> Standortanalyse Glash\u00fctte \u2014 Steuerberatung L\u00f6ffler<br><br>Sehr geehrter Herr L\u00f6ffler,<br><br>\u2022 EFRE Heranf\u00fchrung: 60% Zuschuss <span class='tag tag-e'>E</span><br>\u2022 ~25.000 fehlende Fachkr\u00e4fte bundesweit (DStV 2023) <span class='tag tag-e'>E</span><br>\u2022 DATEV KI-Belegerfassung seit 2024 <span class='tag tag-e'>E</span><br><br>Analyse: <a href='analyse-loeffler.html' style='color:var(--accent)'>analyse-loeffler.html</a><br><br>Mit freundlichen Gr\u00fc\u00dfen<br><em>[Unterschrift B\u00fcrgermeister/in]</em>"},
"glashuette":{type:"kommune",name:"Stadt Glash\u00fctte",greeting:"Fragen zur Analyse Glash\u00fctte?",
  info:["Glash\u00fctte (6.657 EW, 14 Ortsteile) befindet sich im Digitalisierungsvergleich auf der Digitalisierungs-Stufe Initial. Strukturzwillinge wie Bad Belzig (Stufe Etabliert) zeigen, dass vergleichbare Kommunen deutlich weiter sind. <span class='tag tag-i'>I</span>"]},
"jena":{type:"kommune",name:"Stadt Jena",greeting:"Fragen zur Analyse Jena?",
  info:["Jena (111.407 EW) ist BMI Smart City Modellprojekt mit \u20ac17,5M F\u00f6rderung und ~2.000 Besch\u00e4ftigten in der Kernverwaltung. Stufe: Etabliert. <span class='tag tag-e'>E</span>"]},
"marburg":{type:"kommune",name:"Universit\u00e4tsstadt Marburg",greeting:"Fragen zur Analyse Marburg?",
  info:["Marburg (76.401 EW, 1.444 VZ\u00c4) hat einen eigenen Fachdienst 19 Digitalisierung und plant 2026 einen Stellenabbau von 24 VZ\u00c4 im Rahmen der Haushaltskonsolidierung. <span class='tag tag-e'>E</span>"]},
"dippoldiswalde":{type:"kommune",name:"Gro\u00dfe Kreisstadt Dippoldiswalde",greeting:"Fragen zur Analyse Dippoldiswalde?",
  info:["Dippoldiswalde (14.560 EW, gleicher Landkreis SOE wie Glash\u00fctte) hat erst 2025 eine Online-Terminvergabe eingef\u00fchrt. Stufe: Entwicklung. <span class='tag tag-e'>E</span>"]},
"gersheim":{type:"kommune",name:"Gemeinde Gersheim",greeting:"Fragen zur Analyse Gersheim?",
  info:["Gersheim (~6.400 EW) setzt als eine der kleinsten Gemeinden bundesweit einen KI-gest\u00fctzten Chatbot (neuraflow GmbH) auf der Gemeinde-Website ein. <span class='tag tag-e'>E</span>"]},
"badbelzig":{type:"kommune",name:"Stadt Bad Belzig",greeting:"Fragen zur Analyse Bad Belzig?",
  info:["Bad Belzig (11.436 EW, 15 Ortsteile) ist BMI Smart City Modellprojekt (\u20ac5,4M) mit eigener B\u00fcrger-App, Klimadaten-Plattform, Beteiligungsportal und Buchungssystem. Stufe: Etabliert. <span class='tag tag-e'>E</span>"]},
"smartregion":{type:"kommune",name:"Smart Region AUF",greeting:"Fragen zur Smart Region AUF?",
  info:["Smart Region AUF (~6.000 EW, 3 bayerische Gemeinden) ist das kleinste BMI Smart City Modellprojekt bundesweit. Maßnahmen: virtuelles Kraftwerk, B\u00fcrger-App, Blackout-Vorsorge. <span class='tag tag-e'>E</span>"]}
};

// ── Detect page context from mia-slot data attribute or URL ──
// --- Mia Memory: track page visits (no content, no user data) ---
const MIA_VISITS_KEY="ainary_visits";
function trackVisit(){
  const p=location.pathname.replace(/.*\//,"").replace(".html","");
  if(!p||p==="index") return;
  try{
    let v=JSON.parse(localStorage.getItem(MIA_VISITS_KEY)||"[]");
    v=v.filter(x=>x.p!==p); // dedupe
    v.unshift({p:p,ts:Date.now()});
    if(v.length>5) v=v.slice(0,5);
    localStorage.setItem(MIA_VISITS_KEY,JSON.stringify(v));
  }catch(e){}
}
function getMemoryGreeting(){
  try{
    const v=JSON.parse(localStorage.getItem(MIA_VISITS_KEY)||"[]");
    if(v.length===0) return null;
    const last=v[0];
    const ago=Date.now()-last.ts;
    const mins=Math.floor(ago/60000);
    const hrs=Math.floor(ago/3600000);
    const days=Math.floor(ago/86400000);
    let zeit=mins<60?(mins+" Minuten"):hrs<24?(hrs+" Stunden"):(days+" Tagen");
    const names={
      "analyse-foerdermittel":"Fördermittel-Analyse","analyse-digitalisierung":"Digitalisierungsstrategie",
      "analyse-buergerstimmung":"Bürgerstimmung","analyse-uhrenindustrie":"Uhrenindustrie-Bericht",
      "analyse-nomos":"Nomos-Analyse","analyse-muehle":"Mühle-Analyse","analyse-lange":"Lange-Analyse",
      "analyse-gurofa":"Gurofa-Analyse","analyse-loeffler":"Löffler-Analyse",
      "analyse-glashuette":"Glashütte-Analyse","analyse-badbelzig":"Bad Belzig-Analyse",
      "analyse-jena":"Jena-Analyse","analyse-marburg":"Marburg-Analyse",
      "analyse-dippoldiswalde":"Dippoldiswalde-Analyse","analyse-gersheim":"Gersheim-Analyse",
      "analyse-smartregion-auf":"Smart Region AUF","vergleich":"Kommunen-Vergleich",
      "wirtschaft":"Wirtschaftsverzeichnis","analyse":"Personalanalyse","projekte":"Projekte","dokumente":"Dokumente"
    };
    const followups={
      "analyse-foerdermittel":"Die EFRE-Frist läuft in 6 Wochen — soll ich die Unterlagen vorbereiten?",
      "analyse-digitalisierung":"Dippoldiswalde hat denselben Anbieter — soll ich den Kontakt herstellen?",
      "analyse-buergerstimmung":"Das Windkraft-Thema entwickelt sich weiter — soll ich ein Update erstellen?",
      "analyse-uhrenindustrie":"Soll ich die Analyse mit aktuellen Exportzahlen ergänzen?",
      "vergleich":"Glashütte steht bei Initial — soll ich Quick Wins identifizieren?",
      "wirtschaft":"Soll ich für weitere Unternehmen Analysen erstellen?"
    };
    const name=names[last.p]||last.p;
    const followup=followups[last.p]||"Soll ich dort weitermachen?";
    return "Sie haben sich vor "+zeit+" die <strong>"+name+"</strong> angesehen. "+followup;
  }catch(e){return null;}
}
trackVisit();

function getMiaCtx(){
  const slot=document.getElementById("mia-slot");
  if(slot&&slot.dataset.ctx) return MIA_CTX[slot.dataset.ctx]||null;
  const p=location.pathname;
  if(p.includes("analyse-nomos")) return MIA_CTX["nomos"];
  if(p.includes("analyse-muehle")) return MIA_CTX["muehle"];
  if(p.includes("analyse-lange")) return MIA_CTX["lange"];
  if(p.includes("analyse-gurofa")) return MIA_CTX["gurofa"];
  if(p.includes("analyse-loeffler")) return MIA_CTX["loeffler"];
  if(p.includes("analyse-glashuette")&&!p.includes("uhren")) return MIA_CTX["glashuette"];
  if(p.includes("analyse-jena")) return MIA_CTX["jena"];
  if(p.includes("analyse-marburg")) return MIA_CTX["marburg"];
  if(p.includes("analyse-dippoldiswalde")) return MIA_CTX["dippoldiswalde"];
  if(p.includes("analyse-gersheim")) return MIA_CTX["gersheim"];
  if(p.includes("analyse-badbelzig")) return MIA_CTX["badbelzig"];
  if(p.includes("analyse-smartregion")) return MIA_CTX["smartregion"];
  return null;
}

function makeBoldClickable(){
  document.querySelectorAll(".mia-msg-t strong").forEach(el=>{
    if(el.dataset.chip) return; // already wired
    el.dataset.chip="1";
    el.style.cssText="cursor:pointer;color:var(--accent);border-bottom:1px dotted var(--accent);transition:opacity .12s";
    el.addEventListener("click",function(e){
      e.stopPropagation();
      sendChip(el.textContent);
    });
  });
}

function miaFind(t){
  t=t.toLowerCase();
  const ctx=getMiaCtx();
  // Context-specific responses
  if(ctx){
    if(t.includes("info")||t.includes("zusammenfassung")||t.includes("ergebnis")||t===ctx.name.toLowerCase()) return ctx.info;
    if((t.includes("brief")||t.includes("schreiben")||t.includes("anschreiben"))&&ctx.brief){
      return ["Hier ist eine Briefvorlage f\u00fcr "+ctx.name+":<br><br><div style='background:#fff;border:1px solid var(--border2);border-radius:6px;padding:12px;margin:8px 0;font-size:8pt;line-height:1.6;color:var(--text)'>"+ctx.briefHTML+"</div><button onclick=\"navigator.clipboard.writeText('"+ctx.brief.replace(/'/g,"\\'")+"');this.textContent='\u2713 Kopiert';setTimeout(()=>this.textContent='Text kopieren',2000)\" style='margin-top:6px;padding:5px 12px;border:1px solid var(--border2);border-radius:4px;font-family:var(--m);font-size:7pt;color:var(--accent);cursor:pointer;background:none'>Text kopieren</button>"];
    }
  }
  // Global responses
  if(t.includes("analyse anfordern")||t.includes("analyse f\u00fcr mein")||t.includes("mein unternehmen")) return["Gerne! Welches Unternehmen soll ich analysieren? Nennen Sie mir den <strong>Firmennamen</strong> und den <strong>Standort</strong> \u2014 ich erstelle eine Kurz-Analyse mit F\u00f6rdermittel-Check und KI-Potenzial.<br><br><span style='font-family:var(--m);font-size:7pt;color:var(--muted)'>Bearbeitungszeit: 2 Werktage. Kostenlos f\u00fcr Glash\u00fctter Betriebe.</span>"];
  if(t.includes("empfehl")||t.includes("weiterempfehl")||t.includes("teilen")||t.includes("kollege")) return MIA_R["empfehlung"];
  if(t.includes("f\u00f6rder")||t.includes("geld")||t.includes("antrag")) return MIA_R["fördermittel"];
  if(t.includes("wind")) return MIA_R["windkraft"];
  if(t.includes("digital")||t.includes("online")) return MIA_R["digital"];
  if(t.includes("uhr")||t.includes("lange")||t.includes("nomos")) return MIA_R["uhren"];
  if(t.includes("vorschlag")) return MIA_R["projektvorschlag"];
  if(t.includes("termin")||t.includes("florian")) return MIA_R["termin"];
  if(t.includes("danke")||t.includes("super")) return MIA_R["danke"];
  if(ctx) return ctx.info; // Default to page info if on analyse page
  // Fact-based response from current page
  const pk=location.pathname.replace(/.*\//,"").replace(".html","");
  const facts=PAGE_FACTS[pk]||PAGE_FACTS["index"];
  if(t.includes("fakt")||t.includes("zahl")||t.includes("detail")||t.includes("mehr")) return [facts[0]+" Möchten Sie mehr zu <strong>Fördermitteln</strong> oder <strong>Projekten</strong> erfahren?"];
  // New BM-relevant keywords
  if(t.includes("kosten")||t.includes("preis")||t.includes("budget")) return ["Die Kosten hängen vom Umfang ab. Phase 1 (Analyse) ist kostenlos. Für Details: <strong>Termin</strong> mit Florian Ziesche vereinbaren. Soll ich einen <strong>Termin</strong> vorschlagen?"];
  if(t.includes("dauer")||t.includes("zeit")||t.includes("wann")||t.includes("wie lange")) return ["Phase 1: 1–2 Wochen Analyse. Phase 2: 4–6 Wochen Pilotbetrieb. Erster Nutzen ab Woche 1. Möchten Sie mehr zu den <strong>Projekten</strong> erfahren?"];
  if(t.includes("datenschutz")||t.includes("dsgvo")||t.includes("sicher")) return ["Alle Daten bleiben lokal — kein Cloud, keine externen Server. DSGVO-konform, kompatibel mit sächsischem Datenschutz. Möchten Sie die <strong>Methodik</strong> einsehen?"];
  if(t.includes("personal")||t.includes("rente")||t.includes("stellen")||t.includes("mitarbeiter")) return ["<strong>29 von 100 Mitarbeitern</strong> gehen bis 2036 in Rente. 9 davon sind voraussichtlich nicht nachbesetzbar (Nichtbesetzungsquote 31%). Geschätzte Mehrkosten: <strong>€1,36 Mio./Jahr</strong>. <a href='analyse.html' style='color:var(--accent);font-weight:600;font-size:8pt'>Personalanalyse →</a> Soll ich einen <strong>Termin</strong> vorschlagen?"];
  if(t.includes("bürger")||t.includes("feedback")||t.includes("meldung")||t.includes("beschwerde")) return ["Der <strong>Bürger-Feedback-Kanal</strong> erfasst und kategorisiert Meldungen automatisch. 342 Posts bereits analysiert — Top-Themen: Windkraft (46%), Infrastruktur (23%), Tourismus (15%). <a href='analyse-buergerstimmung.html' style='color:var(--accent);font-weight:600;font-size:8pt'>Bürgerstimmung →</a> Möchten Sie mehr zu <strong>Digitalisierung</strong> erfahren?"];
  if(t.includes("amtsblatt")||t.includes("presse")||t.includes("kommunikation")) return ["Ainary kann <strong>Amtsblätter</strong>, Pressemitteilungen und Social Media aus einer Quelle bespielen — Multi-Kanal-Kommunikation mit einheitlicher Tonalität und automatischer Archivierung. Soll ich einen <strong>Termin</strong> vorschlagen?"];
  if(t.includes("protokoll")||t.includes("sitzung")||t.includes("stadtrat")) return ["<strong>Sitzungsprotokolle</strong> können automatisch erstellt, zusammengefasst und durchsuchbar archiviert werden. Inklusive Beschluss-Tracking und Aufgaben-Ableitung. Möchten Sie mehr zu den <strong>Projekten</strong> erfahren?"];
  
  // Page-specific contextual keywords (5 per main page)
  // index.html
  if(t.includes("dashboard")||t.includes("übersicht")||t.includes("kpi")||t.includes("woche")||t.includes("aktuell")) return ["Das <strong>Dashboard</strong> zeigt: <strong>~93 Std. gespart</strong>, <strong>40% Routineanteil</strong> automatisierbar, <strong>€215k–580k Potenzial</strong> identifiziert. Woche 1 von 52. Möchten Sie Details zu <strong>Fördermitteln</strong> oder <strong>Projekten</strong>?"];
  // analyse.html
  if(t.includes("routine")||t.includes("waffle")||t.includes("40%")) return ["<strong>40% der Verwaltungsaufgaben</strong> sind Routine — potenziell automatisierbar. <strong>29 von 100 Mitarbeitern</strong> gehen bis 2036 in Rente, 9 davon nicht nachbesetzbar. <a href='analyse.html' style='color:var(--accent);font-weight:600;font-size:8pt'>Personalanalyse →</a>"];
  // projekte.html
  if(t.includes("projekt")||t.includes("eigene")||t.includes("anfragen")||t.includes("vorschlag")||t.includes("dokument")) return ["Sie können <strong>eigene Projekte anfragen</strong> — z.B. Wahleinblicke 2026, Tourismuskonzept, Fachkräfte-Kampagne. Beschreiben Sie was Sie brauchen, ich erstelle ein Angebot. Lieferung: 2 Werktage. <a href='projekte.html' style='color:var(--accent);font-weight:600;font-size:8pt'>Projekte →</a>"];
  // wirtschaft.html
  if(t.includes("firma")||t.includes("unternehmen")||t.includes("lange")) return ["<strong>167 Unternehmen</strong> in Glashütte erfasst. 5 Uhrenmanufakturen im Detail: <strong>Nomos</strong>, <strong>Lange</strong>, <strong>Mühle</strong>, <strong>Glashütte Original</strong>, <strong>Tutima</strong>. Möchten Sie eine Analyse anfordern? <a href='wirtschaft.html' style='color:var(--accent);font-weight:600;font-size:8pt'>Wirtschaft →</a>"];
  // dokumente.html
  if(t.includes("bericht")||t.includes("download")||t.includes("pdf")) return ["<strong>6 Dokumente</strong> verfügbar, basierend auf 79 Quellen. Höchste Confidence: <strong>Fördermittel-Komplettscan</strong> (78%, 23 Quellen). Alle druckbar und teilbar. <a href='dokumente.html' style='color:var(--accent);font-weight:600;font-size:8pt'>Dokumente →</a>"];
  
  // Honest fallback for off-topic
  return ["Das liegt außerhalb meiner aktuellen Datenbasis. Fragen Sie gerne Florian Ziesche direkt — <a href='mailto:florian@ainaryventures.com' style='color:var(--accent);font-weight:600'>florian@ainaryventures.com</a><br><br>Ich kann Ihnen zu <strong>Fördermitteln</strong>, <strong>Digitalisierung</strong>, <strong>Personalanalyse</strong> und <strong>Bürgerstimmung</strong> helfen — jeweils mit Quellen."];
}

function miaAddMsg(t,u){const m=document.getElementById("mia-messages"),d=document.createElement("div");d.className="mia-msg"+(u?" user":"");if(u){d.innerHTML='<div class="mia-msg-t">'+t+"</div>";m.appendChild(d);m.scrollTop=m.scrollHeight}else{const av=document.createElement("div");av.className="mia-msg-a";av.textContent="M";const tb=document.createElement("div");tb.className="mia-msg-t";d.appendChild(av);d.appendChild(tb);m.appendChild(d);m.scrollTop=m.scrollHeight;const chars=t.split("");let i=0,buf="",inTag=false;(function tick(){if(i>=chars.length){tb.innerHTML=t;m.scrollTop=m.scrollHeight;makeBoldClickable();return}buf+=chars[i];if(chars[i]==="<")inTag=true;if(chars[i]===">")inTag=false;i++;if(inTag){tick()}else{tb.innerHTML=buf;m.scrollTop=m.scrollHeight;setTimeout(tick,14+Math.random()*10)}})()}}
function sendChip(t){const b=document.getElementById("mia-body"),l=document.getElementById("mia-toggle-label");if(!b.classList.contains("open")){b.classList.add("open");l.textContent="\u2191"}miaAddMsg(t,true);setTimeout(()=>{const[r]=miaFind(t);miaAddMsg(r,false)},600+Math.random()*600)}
function sendMia(){const i=document.getElementById("mia-input"),t=i.value.trim();if(!t)return;miaAddMsg(t,true);i.value="";setTimeout(()=>{const[r]=miaFind(t);miaAddMsg(r,false)},600+Math.random()*800)}

// ── Auto-inject Mia HTML with context-aware greeting + chips ──
document.addEventListener("DOMContentLoaded",function(){
  const slot=document.getElementById("mia-slot");
  if(!slot) return;
  const ctx=getMiaCtx();
  const memGreet=getMemoryGreeting();
  const greeting=memGreet||( ctx?ctx.greeting:"Kann ich Ihnen weiterhelfen?");
  // Context-aware first message
  const pageMsgs={
    "wirtschaft":"Fragen Sie mich zu <strong>Unternehmen</strong>, <strong>F\u00f6rdermitteln</strong> oder lassen Sie eine <strong>Analyse anfordern</strong>.",
    "projekte":"Fragen Sie mich zu <strong>Projekten</strong>, <strong>F\u00f6rdermitteln</strong> oder sagen Sie <strong>Projektvorschlag</strong>.",
    "dokumente":"Fragen Sie mich zu <strong>Pr\u00e4sentationen</strong>, <strong>Analysen</strong> oder <strong>F\u00f6rdermitteln</strong>.",
    "vergleich":"Fragen Sie mich zum <strong>Vergleich</strong>, zu <strong>Kommunen</strong> oder zur <strong>Methodik</strong>.",
    "analyse":"Fragen Sie mich zu <strong>Personal</strong>, <strong>F\u00f6rdermitteln</strong>, <strong>Digitalisierung</strong> oder <strong>B\u00fcrgerstimmung</strong>.",
  };
  const pageKey=location.pathname.replace(/.*\//,"").replace(".html","");
  const pf=PAGE_FACTS[pageKey];
  const firstMsg=ctx?ctx.info[0]:pf?pf[0]:(pageMsgs[pageKey]||"Fragen Sie mich zu <strong>F\u00f6rdermitteln</strong>, <strong>Digitalisierung</strong>, <strong>B\u00fcrgerstimmung</strong> oder <strong>Uhrenindustrie</strong>.");

  // Build chips matching page context
  const pageChips={
    "wirtschaft":["Analyse anfordern","F\u00f6rdermittel","Uhrenindustrie","Weiterempfehlen"],
    "projekte":["Projektvorschlag","F\u00f6rdermittel","Digitalisierung","Weiterempfehlen"],
    "dokumente":["Analysen","F\u00f6rdermittel","Pr\u00e4sentationen","Weiterempfehlen"],
    "vergleich":["Methodik","Kommunen","F\u00f6rdermittel","Weiterempfehlen"],
    "analyse":["F\u00f6rdermittel","Digitalisierung","B\u00fcrgerstimmung","Weiterempfehlen"],
    "index":["F\u00f6rdermittel","Digitalisierung","Projektvorschlag","Weiterempfehlen"],
  };
  let chipList;
  if(ctx){
    chipList=["Zusammenfassung"];
    if(ctx.type==="firma"&&ctx.brief) chipList.push("Anschreiben erstellen");
    chipList.push("F\u00f6rdermittel","Weiterempfehlen");
  } else {
    chipList=pageChips[pageKey]||pageChips["index"];
  }
  let chips=chipList.map(c=>'<span class="mia-chip" onclick="sendChip(\''+c.replace(/'/g,"\\'")+'\')">'+c+'</span>').join("");

  slot.innerHTML='<div class="mia" id="mia"><div class="mia-header" onclick="toggleMia()"><div class="mia-av">M</div><div class="mia-greeting"><strong>Mia:</strong> '+greeting+'</div><span class="mia-toggle" id="mia-toggle-label">\u2193</span></div><div class="mia-body" id="mia-body"><div class="mia-messages" id="mia-messages"><div class="mia-msg"><div class="mia-msg-a">M</div><div class="mia-msg-t">'+firstMsg+'</div></div></div><div class="mia-input-row"><input class="mia-input" id="mia-input" type="text" placeholder="Frage stellen..." onkeydown="if(event.key===\'Enter\')sendMia()"><button class="mia-send" onclick="sendMia()">Senden</button></div><div class="mia-chips">'+chips+'</div><div class="mia-badge">Mia ist eine KI-Assistentin \u00b7 Antworten basieren auf Ihren Reports</div></div></div>';

  // Make <strong> tags in Mia messages clickable
  makeBoldClickable();
});
