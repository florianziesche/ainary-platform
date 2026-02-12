# florianziesche.de — KI Beratung Landing Page

**Status:** ✅ Build Complete (10.02.2026)
**Tech Stack:** Single HTML file, Pure CSS, Google Fonts (Inter)
**Dependencies:** None (außer Google Fonts)

---

## 📋 Was wurde gebaut

Eine **single-page HTML Landing Page** für Florian Ziesches AI Consulting Business:

### Struktur
1. **Hero Section** — "KI-Systeme für den Mittelstand — von der Idee zum ROI in 8 Wochen"
2. **Use Cases** — 3 Karten (CNC/Fertigung, Qualitätskontrolle, Prozessautomation)
3. **Funding Banner** — Bayern Digitalbonus Plus Hook (50% Förderung)
4. **Social Proof** — BMW, Siemens, Bosch + MBS Case Study Zahlen
5. **About Section** — Kurz-Bio mit Credentials
6. **Footer CTA** — Kontakt (Email, Telefon, LinkedIn)

### Design
- **Mobile-first, responsive** (funktioniert auf allen Devices)
- **Dark Theme** mit Gold Accent (#c8aa50)
- **Inter Font** (Google Fonts)
- **Pure CSS** — keine externen Dependencies außer Fonts
- **Smooth Scroll** und subtile Hover-Animationen
- **Professional** — deutsch, direkt, Mittelstand-gerecht

---

## 🚀 Deployment

### Option 1: GitHub Pages (empfohlen, kostenlos)

```bash
# 1. GitHub Repo erstellen
# 2. Files hochladen
git init
git add index.html README.md
git commit -m "Initial commit: florianziesche.de landing page"
git branch -M main
git remote add origin [DEINE_REPO_URL]
git push -u origin main

# 3. GitHub Pages aktivieren
# Settings → Pages → Source: main branch, root folder
# URL wird automatisch generiert: [username].github.io/[repo-name]

# 4. Custom Domain (optional)
# Domain-Provider: CNAME Record erstellen
# Ziel: [username].github.io
# GitHub Settings → Pages → Custom domain: florianziesche.de
```

### Option 2: Netlify (noch einfacher)

```bash
# 1. Account erstellen: netlify.com
# 2. Drag & Drop das index.html in Netlify Drop Zone
# 3. Fertig! URL wird automatisch generiert
# 4. Custom Domain: Settings → Domain Management → Add custom domain
```

### Option 3: Vercel (Alternative)

```bash
# 1. Account erstellen: vercel.com
# 2. Import from Git (oder Drag & Drop)
# 3. Deploy
# 4. Custom Domain: Settings → Domains
```

---

## 🛠️ Anpassungen

### Foto hinzufügen

Ersetze den Platzhalter in der About-Section:

```html
<!-- ALT (Zeile ~390): -->
<div class="photo-placeholder">
  [Foto folgt]
</div>

<!-- NEU: -->
<img src="florian-ziesche.jpg" alt="Florian Ziesche" style="width: 100%; border-radius: var(--radius); border: 2px solid var(--accent);">
```

### Kontaktdaten ändern

Suche nach:
- `florian@ainaryventures.com` → durch deine Email ersetzen
- `+49 151 2303 9208` → durch deine Telefonnummer ersetzen
- LinkedIn URL anpassen

### Farben anpassen

Falls du das Farbschema ändern willst (`:root` Bereich, Zeile ~14):

```css
--accent: #c8aa50;       /* Gold */
--accent-dark: #9d7f3b;  /* Dunkleres Gold */
--accent-pale: #e8d89f;  /* Helles Gold */
```

### Text anpassen

Alle Texte sind inline im HTML. Einfach durchsuchen und ersetzen.

---

## ✅ SEO & Meta Tags

**Bereits enthalten:**
- `<title>` Tag
- `<meta description>` Tag
- `lang="de"` Attribut
- Viewport Meta Tag (Mobile-optimiert)

**Noch zu tun (optional):**
- Open Graph Tags für Social Media Previews
- Favicon hinzufügen
- robots.txt (wenn nötig)
- sitemap.xml (wenn mehrere Seiten)

### Open Graph Tags hinzufügen (optional)

Füge in `<head>` ein:

```html
<!-- Open Graph / Facebook -->
<meta property="og:type" content="website">
<meta property="og:url" content="https://florianziesche.de/">
<meta property="og:title" content="Florian Ziesche — KI-Beratung für den Mittelstand">
<meta property="og:description" content="KI-Systeme für den deutschen Mittelstand. Von der Idee zum ROI in 8 Wochen.">
<meta property="og:image" content="https://florianziesche.de/og-image.jpg">

<!-- Twitter -->
<meta property="twitter:card" content="summary_large_image">
<meta property="twitter:url" content="https://florianziesche.de/">
<meta property="twitter:title" content="Florian Ziesche — KI-Beratung für den Mittelstand">
<meta property="twitter:description" content="KI-Systeme für den deutschen Mittelstand. Von der Idee zum ROI in 8 Wochen.">
<meta property="twitter:image" content="https://florianziesche.de/og-image.jpg">
```

---

## 📄 Rechtliches (Deutschland)

**Wichtig:** In Deutschland sind **Impressum** und **Datenschutzerklärung** Pflicht!

### Impressum erstellen

1. Generator nutzen: https://www.e-recht24.de/impressum-generator.html
2. Neue Datei erstellen: `impressum.html`
3. Footer-Link anpassen: `<a href="impressum.html">Impressum</a>`

### Datenschutzerklärung erstellen

1. Generator nutzen: https://www.e-recht24.de/dsgvo/datenschutzerklaerung/
2. Neue Datei erstellen: `datenschutz.html`
3. Footer-Link anpassen: `<a href="datenschutz.html">Datenschutz</a>`

**ACHTUNG:** Google Fonts aus EU datenschutzrechtlich problematisch!

**Lösung 1:** Fonts lokal hosten (DSGVO-konform)
**Lösung 2:** Consent-Banner (Cookie-Einwilligung)

Mehr Infos: https://www.e-recht24.de/news/datenschutz/13222-google-fonts-datenschutz.html

---

## 🧪 Testing

### Vor Go-Live testen:

- [ ] **Mobile:** iPhone, Android (Chrome Dev Tools)
- [ ] **Desktop:** Chrome, Firefox, Safari
- [ ] **Links:** Alle CTAs und Footer-Links funktionieren
- [ ] **Performance:** PageSpeed Insights (https://pagespeed.web.dev/)
- [ ] **Accessibility:** WAVE Tool (https://wave.webaim.org/)
- [ ] **SEO:** Google Search Console einrichten

---

## 📊 Analytics (optional)

### Google Analytics 4 einbinden

In `<head>` einfügen:

```html
<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXXXXX"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-XXXXXXXXXX');
</script>
```

**Wichtig:** DSGVO-konform! Cookie-Banner nötig.

---

## 📈 Next Steps

### Kurzfristig (vor Launch)
- [ ] Eigenes Foto hinzufügen (About Section)
- [ ] Impressum & Datenschutz erstellen
- [ ] Domain registrieren (falls noch nicht geschehen)
- [ ] Deployment (GitHub Pages / Netlify / Vercel)
- [ ] Custom Domain verbinden

### Mittelfristig (nach Launch)
- [ ] Google Analytics einrichten
- [ ] Open Graph Tags hinzufügen
- [ ] Favicon erstellen
- [ ] Email-Tracking einrichten (ConvertKit / Mailchimp)
- [ ] A/B Testing (verschiedene Headlines testen)

### Langfristig
- [ ] Blog hinzufügen (Case Studies, Insights)
- [ ] Portfolio-Seite (weitere Referenzen)
- [ ] Kontaktformular (statt nur mailto:)
- [ ] Lead Magnet (z.B. "KI-Readiness Check" als PDF)

---

## 📧 Outreach Integration

Diese Landing Page ist **optimiert für Outreach-Emails**:

### Email-Template Beispiel

```
Betreff: €15.000 statt €30.000 — KI-Projekt mit Bayern Digitalbonus Plus

Sehr geehrter Herr [NAME],

die meisten KI-Projekte im Mittelstand scheitern nicht an der Technik, 
sondern an der Umsetzung — und manchmal am Budget.

Gute Nachricht: Mit dem Bayern Digitalbonus Plus übernimmt der Freistaat 
50% Ihrer KI-Investition.

Mehr Details: https://florianziesche.de

Kurzes Gespräch? [CALENDLY LINK]

Mit besten Grüßen,
Florian Ziesche
```

**Hook:** Förderung + konkrete Zahlen + Referenz (MBS) = starke Kombi.

---

## 🎨 Design-Entscheidungen

### Warum Dark Theme?
- Professioneller Look
- Unterscheidet sich von Standard-Business-Websites
- Gold Accent kommt besser zur Geltung
- Modern, hochwertig

### Warum keine Preise?
- Zielgruppe erwartet individuelle Angebote
- Förderung verändert effektive Preise (50% Rabatt)
- "Details auf Anfrage" erhöht Gesprächsrate

### Warum nur 3 Use Cases?
- Fokus > Feature-Liste
- Mittelstand-Entscheider wollen konkrete Beispiele
- Jeder Use Case hat messbare Zahlen (92%, €22.900)

---

## 💾 File Structure

```
/website/florianziesche-de/
├── index.html           # Main Landing Page
├── README.md            # Diese Datei
├── impressum.html       # TODO: Erstellen (Pflicht DE)
├── datenschutz.html     # TODO: Erstellen (Pflicht DE)
└── assets/              # Optional: Bilder, Favicon
    ├── florian.jpg
    ├── favicon.ico
    └── og-image.jpg
```

---

## 📞 Support & Feedback

Falls Änderungen oder Fragen:
1. Issue öffnen im GitHub Repo
2. Mich direkt kontaktieren: florian@ainaryventures.com
3. Bei technischen Problemen: Screenshots + Browser Info hilfreich

---

*Built: 10.02.2026*  
*Version: 1.0*  
*Status: Ready for Deployment*
