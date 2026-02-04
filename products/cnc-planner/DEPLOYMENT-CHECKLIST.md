# CNC Planner Pro — Deployment Checkliste

**Ziel-Domain:** cnc.florianziesche.com  
**Hosting:** SiteGround  
**Analysiert:** 2026-02-03  
**Status:** 🔴 NOCH NICHT BEREIT

---

## ✅ Was bereits funktioniert

| Item | Status |
|------|--------|
| Landing Page HTML vollständig | ✅ |
| Alle Links relativ (keine localhost URLs) | ✅ |
| ROI-Rechner funktional (JavaScript) | ✅ |
| Tab-Navigation funktional | ✅ |
| Responsive Design (CSS vorhanden) | ✅ |
| Impressum vorhanden | ✅ |
| FAQ Section vorhanden | ✅ |
| Feedback Widget integriert | ✅ |
| Login Modal implementiert | ✅ |

---

## 🔴 KRITISCH — Muss vor Go-Live behoben werden

### 1. **Demo-Datei fehlt**
- `demo-v12.html` wird im Code referenziert, existiert aber NICHT
- Betrifft:
  - Fertigungsanweisungen-Tab → "Vollständige Fertigungsanweisung in der Demo"
  - Login-Weiterleitung → `window.location.href = 'demo-v12.html'`
- **Lösung:** 
  - Option A: Demo-Seite erstellen
  - Option B: Links entfernen/ändern und auf Waitlist verweisen

### 2. **E-Mail-Adressen anpassen**
Aktuelle Adressen in der Datei (falsch für cnc.florianziesche.com):
- `kontakt@cncplanner.de`
- `support@cncplanner.de`

**Ändern zu:** `florian@florianziesche.com`

**Stellen zum Ändern:**
- Impressum Kontakt-Bereich (Zeile ~2123)
- Footer Support-Link (Zeile ~2162)

### 3. **Rechtliche Seiten fehlen**
Diese Seiten werden im Footer verlinkt, existieren aber nicht:
- `#datenschutz` → Datenschutzerklärung erstellen
- `#agb` → AGB erstellen

**Für MVP:** Mindestens Datenschutz ist PFLICHT (DSGVO)

### 4. **Formular-Backend fehlt**
Die Formulare sammeln E-Mails, aber es gibt kein Backend:
- Demo-Request-Formular (zeigt nur "Anfrage erhalten")
- Demo-Zugang-Formulare (mehrfach auf der Seite)
- Feedback-Widget (zeigt nur Alert)

**Lösungen:**
- Formspree.io (einfach, kostenlos)
- Netlify Forms
- Eigenes Backend (z.B. n8n Webhook)

---

## 🟡 EMPFOHLEN — Sollte vor Go-Live erledigt werden

### 5. **Meta-Tags für SEO**
Folgende Tags fehlen im `<head>`:
```html
<meta name="description" content="CNC Planner Pro — Präzise CNC-Kalkulation in Minuten. Fertigungszeiten, Maschinencode und Angebote automatisch.">
<meta name="keywords" content="CNC, Kalkulation, Fertigung, Maschinencode, Angebot, CAM">
<meta property="og:title" content="CNC Planner Pro — Intelligente Fertigungskalkulation">
<meta property="og:description" content="Präzise CNC-Kalkulation in Minuten, nicht Stunden.">
<meta property="og:image" content="https://cnc.florianziesche.com/og-image.png">
<meta property="og:url" content="https://cnc.florianziesche.com">
<link rel="canonical" href="https://cnc.florianziesche.com">
```

### 6. **Favicon fehlt**
Kein `<link rel="icon">` definiert → Browser zeigt Standard-Icon

### 7. **Analytics fehlen**
Kein Tracking eingebaut:
- Google Analytics oder
- Plausible (DSGVO-freundlich)
- Mindestens: UTM-Parameter für Links

### 8. **Cookie-Banner fehlt**
Falls Analytics eingebaut wird → Cookie-Banner PFLICHT (DSGVO)

---

## 📋 Deployment-Schritte

### Vor dem Upload:

1. [ ] E-Mail-Adressen ersetzen (`kontakt@cncplanner.de` → `florian@florianziesche.com`)
2. [ ] Demo-Links anpassen oder entfernen
3. [ ] Datenschutzerklärung als Section hinzufügen
4. [ ] Formular-Backend einrichten (Formspree empfohlen)
5. [ ] Meta-Tags hinzufügen
6. [ ] Favicon erstellen und einbinden

### Upload zu SiteGround:

1. [ ] Subdomain `cnc.florianziesche.com` in SiteGround erstellen
2. [ ] SSL-Zertifikat aktivieren (Let's Encrypt)
3. [ ] `landing-page.html` als `index.html` hochladen
4. [ ] Zusätzliche Assets hochladen (falls vorhanden)
5. [ ] HTTPS-Redirect aktivieren

### Nach Go-Live:

1. [ ] Alle Links testen
2. [ ] Formulare testen (E-Mail kommt an?)
3. [ ] Mobile-Ansicht prüfen
4. [ ] PageSpeed Insights checken
5. [ ] In Google Search Console anmelden

---

## 🔧 Notwendige Änderungen — Code-Snippets

### E-Mail ersetzen (Impressum, ~Zeile 2123):
```html
<!-- ALT -->
E-Mail: kontakt@cncplanner.de

<!-- NEU -->
E-Mail: florian@florianziesche.com
```

### E-Mail ersetzen (Footer, ~Zeile 2162):
```html
<!-- ALT -->
<a href="mailto:support@cncplanner.de">E-Mail Support</a>
<a href="mailto:kontakt@cncplanner.de">Kontakt</a>

<!-- NEU -->
<a href="mailto:florian@florianziesche.com">E-Mail Support</a>
<a href="mailto:florian@florianziesche.com">Kontakt</a>
```

### Demo-Link entfernen oder ändern (~Zeile 1994):
```html
<!-- ALT -->
<a href="demo-v12.html" class="btn btn-secondary">Vollständige Fertigungsanweisung in der Demo</a>

<!-- NEU (Waitlist-Version) -->
<a href="#demo" class="btn btn-secondary">Demo anfordern</a>
```

### Login-Redirect ändern (~Zeile 2296):
```javascript
// ALT
window.location.href = 'demo-v12.html';

// NEU (zeigt Message statt Redirect)
alert('Demo-Zugang wird innerhalb von 24h per E-Mail gesendet.');
hideLoginModal();
```

---

## 📁 Deployment-Struktur

Für SiteGround Upload:
```
cnc.florianziesche.com/
├── index.html          (= landing-page.html, umbenannt)
├── favicon.ico         (zu erstellen)
├── og-image.png        (zu erstellen, 1200x630px)
└── robots.txt          (optional)
```

---

## Geschätzter Aufwand

| Task | Zeit |
|------|------|
| E-Mail-Adressen ersetzen | 5 min |
| Demo-Links anpassen | 10 min |
| Datenschutz hinzufügen | 30 min |
| Meta-Tags hinzufügen | 10 min |
| Formspree einrichten | 20 min |
| SiteGround Setup | 15 min |
| **Gesamt** | **~1,5 Stunden** |

---

*Erstellt von BUILDER Sub-Agent, 2026-02-03*
