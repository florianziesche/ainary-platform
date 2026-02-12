# 🚀 Quick Preview & Testing

## Lokale Vorschau (sofort)

### Option 1: Python SimpleHTTPServer (empfohlen)

```bash
cd /Users/florianziesche/.openclaw/workspace/website/florianziesche-de
python3 -m http.server 8000
```

Dann öffne: **http://localhost:8000**

### Option 2: PHP Built-in Server

```bash
cd /Users/florianziesche/.openclaw/workspace/website/florianziesche-de
php -S localhost:8000
```

### Option 3: VS Code Live Server

1. VS Code öffnen
2. Extension installieren: "Live Server"
3. Rechtsklick auf `index.html` → "Open with Live Server"

### Option 4: Direkt im Browser

```bash
open index.html
```

(Funktioniert auch ohne Server, da keine externen Dependencies außer Google Fonts)

---

## 📱 Mobile Testing

### Chrome DevTools

1. Chrome öffnen: `http://localhost:8000`
2. DevTools öffnen: `Cmd+Option+I` (Mac) / `F12` (Windows)
3. Toggle Device Toolbar: `Cmd+Shift+M` (Mac) / `Ctrl+Shift+M` (Windows)
4. Verschiedene Devices testen:
   - iPhone 14 Pro
   - Samsung Galaxy S21
   - iPad Pro

### Real Device Testing

- **iPhone:** Safari + Chrome
- **Android:** Chrome + Firefox
- **Tablet:** iPad Safari

**Wichtig:** Auf echten Geräten testen, nicht nur Simulator!

---

## ✅ Checklist vor Go-Live

### Content
- [ ] Alle Platzhalter ersetzt (Foto, Kontakt)
- [ ] Rechtschreibung gecheckt
- [ ] Alle Links funktionieren

### Legal (Deutschland!)
- [ ] Impressum erstellt und verlinkt
- [ ] Datenschutzerklärung erstellt und verlinkt
- [ ] Google Fonts DSGVO-konform (lokal hosten ODER Consent-Banner)

### Performance
- [ ] PageSpeed Insights: https://pagespeed.web.dev/
- [ ] Lighthouse Score (Chrome DevTools):
  - Performance: >90
  - Accessibility: >90
  - Best Practices: >90
  - SEO: >90

### Cross-Browser
- [ ] Chrome ✅
- [ ] Firefox ✅
- [ ] Safari ✅
- [ ] Edge ✅

### Mobile
- [ ] iPhone Safari ✅
- [ ] Android Chrome ✅
- [ ] iPad ✅

### Links
- [ ] `mailto:` Links funktionieren
- [ ] `tel:` Links funktionieren (Mobile)
- [ ] LinkedIn Link funktioniert
- [ ] Smooth Scroll zu Sections funktioniert

---

## 🎨 Schnelle Änderungen

### Farbe ändern

In `<style>` Block finden:

```css
--accent: #c8aa50;  /* Deine Farbe hier */
```

Online Color Picker: https://htmlcolorcodes.com/

### Schriftgröße anpassen

```css
--text-base: 1rem;     /* Body Text */
--text-4xl: 2.5rem;    /* Hero Headline */
```

### Spacing ändern

```css
--padding-section: 80px;  /* Section Abstände */
--radius: 12px;           /* Ecken-Radius */
```

---

## 🐛 Bekannte Issues / Todos

### Noch zu erledigen:
- [ ] Foto hinzufügen (About Section)
- [ ] Impressum & Datenschutz Seiten erstellen
- [ ] Favicon hinzufügen
- [ ] Open Graph Tags (Social Media Preview)

### Bekannte Browser-Quirks:
- **Safari:** Smooth scroll funktioniert nicht auf iOS 14 und älter (kein Problem, fällt zurück auf normales Scrollen)
- **IE11:** NICHT unterstützt (aber IE ist seit 2022 tot)

---

## 📊 Performance Optimierung (optional)

### Fonts lokal hosten (DSGVO + schneller)

1. Fonts downloaden: https://google-webfonts-helper.herokuapp.com/fonts/inter
2. In `/assets/fonts/` Ordner speichern
3. In HTML ersetzen:

```css
/* ALT: */
@import url('https://fonts.googleapis.com/...');

/* NEU: */
@font-face {
  font-family: 'Inter';
  src: url('assets/fonts/inter-v13-latin-regular.woff2') format('woff2');
  font-weight: 400;
  font-display: swap;
}
```

### Bilder optimieren

Wenn du Fotos hinzufügst:

1. **Format:** WebP (modern, klein) + JPEG (Fallback)
2. **Größe:** Max. 1200px Breite
3. **Kompression:** TinyPNG (https://tinypng.com/)

**Beispiel:**

```html
<picture>
  <source srcset="florian.webp" type="image/webp">
  <img src="florian.jpg" alt="Florian Ziesche">
</picture>
```

---

## 🔗 Nützliche Tools

| Tool | URL | Zweck |
|------|-----|-------|
| PageSpeed Insights | https://pagespeed.web.dev/ | Performance messen |
| Google Search Console | https://search.google.com/search-console | SEO tracking |
| WAVE | https://wave.webaim.org/ | Accessibility check |
| Can I Use | https://caniuse.com/ | Browser-Support prüfen |
| HTML Validator | https://validator.w3.org/ | HTML validieren |
| Impressum Generator | https://www.e-recht24.de/impressum-generator.html | Impressum erstellen |
| DSGVO Generator | https://www.e-recht24.de/dsgvo/datenschutzerklaerung/ | Datenschutz erstellen |

---

## 💬 Feedback & Iteration

Nach Launch:

1. **Analytics einrichten** (Google Analytics / Plausible)
2. **Conversion Rate tracken** (Email clicks / Calls)
3. **Heatmaps** (Hotjar / Microsoft Clarity) — wo klicken User?
4. **A/B Testing** — verschiedene Headlines testen

### Verbesserungs-Ideen:

- [ ] Testimonials (mehr als nur MBS)
- [ ] Video-Intro (Florian spricht 30 Sek über KI)
- [ ] Lead Magnet (PDF: "KI-Readiness Check")
- [ ] Kalender-Integration (Calendly für Erstgespräche)
- [ ] Chat-Widget (falls viele Fragen kommen)

---

**Last updated:** 10.02.2026  
**Version:** 1.0  
**Status:** ✅ Ready for Preview
