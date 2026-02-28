# WEBSITE-RULES.md — Ainary Website Standard
*Single Source of Truth for ainaryventures.com. Vor JEDEM Website-Edit konsultieren.*
*Updated: 2026-02-21*

## 1. Seitenstruktur (JEDE Seite)
- `shared/nav.js` (EN: `shared/`, DE: `../shared/`)
- `shared/footer.js`
- `shared/styles.css`
- `<div id="site-nav"></div>` vor Content
- Binary Star Background nach `<body>`
- Title: `Seitenname | Ainary` (kein "Blog" Suffix)
- Canonical URL + OG Tags + hreflang EN/DE

## 2. Binary Star Background (Copy-Paste Block)
```html
<!-- Binary Star background -->
<div style="position:fixed;inset:0;pointer-events:none;z-index:0;overflow:hidden;">
  <div style="position:absolute;width:300px;height:300px;border-radius:50%;background:radial-gradient(circle at 45% 45%,#e8c84a 0%,#c8aa50 25%,#a08030 50%,transparent 72%);filter:blur(80px);mix-blend-mode:screen;opacity:0.18;top:15%;left:60%;animation:drift-gold 90s ease-in-out infinite;"></div>
  <div style="position:absolute;width:250px;height:250px;border-radius:50%;background:radial-gradient(circle at 55% 45%,#ffffff 0%,#e8f0ff 20%,#b0c4e8 45%,transparent 70%);filter:blur(72px);mix-blend-mode:screen;opacity:0.12;top:50%;left:15%;animation:drift-silver 90s ease-in-out infinite;"></div>
</div>
<style>
  @keyframes drift-gold { 0%,100%{transform:translate(0,0) scale(1)} 33%{transform:translate(-40px,25px) scale(1.06)} 66%{transform:translate(20px,-15px) scale(0.97)} }
  @keyframes drift-silver { 0%,100%{transform:translate(0,0) scale(1)} 33%{transform:translate(25px,-20px) scale(0.95)} 66%{transform:translate(-15px,30px) scale(1.04)} }
</style>
```

## 3. Dark vs Light
| Seitentyp | Modus | Background |
|-----------|-------|------------|
| Landing (index.html) | Dark | #0a0a0a |
| Navigation/Pricing | Dark | #0a0a0a |
| Tools | Dark | #0a0a0a |
| Blog-Listing | Dark | #0a0a0a |
| Artikel/Longform | Light | #faf8f4 |
| Daily Brief | Light | #faf8f4 |
| Research Reports | Light | #faf8f4 |
| Legal (Privacy/Terms/Imprint) | Dark | #0a0a0a |
| Resources | Dark | #0a0a0a |
| Contact | Dark | #0a0a0a |

**Regel:** Dark = Brand/Navigation. Light = Lesen ("wie ein Buch oeffnen").

## 4. Fonts
```css
/* Google Fonts — exakt diese URL auf JEDER Seite */
https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600&family=JetBrains+Mono:wght@400;500&display=swap&font-display=swap

/* KEIN Geist Font. KEIN wght 700. */
--font-body: 'Inter', sans-serif;
--font-mono: 'JetBrains Mono', monospace;
```

## 5. Farben
```css
/* Dark Mode */
--bg: #0a0a0a;
--surface: #111111;
--elevated: #1a1a1a;
--text: #ffffff;
--text-secondary: #999999;
--text-muted: #55555e;

/* Light Mode (Artikel) */
--bg: #faf8f4;
--surface: #ffffff;
--text: #1a1a1a;
--text-secondary: #555555;

/* Accent — UEBERALL gleich */
--gold: #c8aa50;
--gold-hover: #a38a3a;

/* VERBOTEN: #8b6914 (Pitch Deck only, nicht Brand) */
```

## 6. Artikel-Template
- Max-width: 680px
- Author Block am Ende (Florian Ziesche, Foto, Bio)
- Related Articles Grid (3 Cards)
- KEIN "Erstellt mit Ainary" CTA
- KEIN Tool CTA Block
- E/I/J/A Badges auf Zahlen (Daily Brief + Reports)

## 7. Content-Regeln
- "ich/I" statt "Ainary" in Prosa (Florian IST Ainary)
- Legal: "Florian Ziesche" + Muenchner Adresse
- Anti-LLM Check vor Publish (CONTENT-VOICE.md)
- Preis Daily Brief: 99 Euro/Monat
- Newsletter CTA → finitematter.substack.com
- Contact → /de/contact.html oder /contact.html

## 8. SEO (jede Seite)
- `<title>` unter 60 Zeichen
- `<meta name="description">` unter 160 Zeichen
- `<link rel="canonical">`
- `<meta property="og:title/description/image/url">`
- `<link rel="alternate" hreflang="en/de">`
- Sitemap: sitemap.xml (manuell updaten bei neuen Seiten)

## 9. Deploy
```bash
cd ~/.openclaw/workspace/projects/platform-website
npx vercel --yes --prod
```
Aliased to: ainaryventures.com

## 10. Checkliste vor Deploy
- [ ] Shared nav/footer/CSS eingebunden?
- [ ] Binary Star Background vorhanden?
- [ ] Dark/Light korrekt fuer Seitentyp?
- [ ] Title Format: "Name | Ainary"?
- [ ] Canonical + OG Tags?
- [ ] Alle internen Links getestet?
- [ ] Mobile responsive? (Nav collapsed)
- [ ] Kein Geist Font, kein wght 700?
- [ ] Gold = #c8aa50?
