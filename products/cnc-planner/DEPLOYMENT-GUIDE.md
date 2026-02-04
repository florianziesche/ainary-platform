# 🚀 CNC Planner Pro - Deployment Guide für SiteGround

**Ziel:** cnc.florianziesche.com als Subdomain auf SiteGround  
**Geschätzte Gesamtzeit:** 30-45 Minuten  
**Letzte Aktualisierung:** Februar 2026

---

## 📋 Übersicht

| Schritt | Beschreibung | Zeit |
|---------|--------------|------|
| 1 | Subdomain erstellen | 5 min |
| 2 | Dateien vorbereiten | 10 min |
| 3 | Dateien hochladen | 5 min |
| 4 | SSL aktivieren | 5 min |
| 5 | Testen | 10 min |

---

## 📁 Dateien-Mapping

| Quelldatei | Zieldatei | Pfad auf Server |
|------------|-----------|-----------------|
| `landing-page.html` | `index.html` | `/cnc/index.html` |
| `datenschutz.html` | `datenschutz.html` | `/cnc/datenschutz.html` |
| `demo-v12.html` | `demo.html` | `/cnc/demo.html` |

---

## Schritt 1: Subdomain in SiteGround erstellen

**⏱️ Geschätzte Zeit: 5 Minuten**

### 1.1 SiteGround Site Tools öffnen

1. Gehe zu [my.siteground.com](https://my.siteground.com)
2. Klicke auf **"Websites"** im Menü
3. Wähle **florianziesche.com** aus der Liste
4. Klicke auf **"Site Tools"** (oranger Button)

### 1.2 Subdomain anlegen

1. In Site Tools: Linkes Menü → **"Domain"** → **"Subdomains"**
2. Klicke auf **"Create New Subdomain"**
3. Eingabe:
   - **Subdomain Name:** `cnc`
   - **Root Domain:** `florianziesche.com` (automatisch vorausgewählt)
4. Klicke **"Create"**

> ✅ **Ergebnis:** Die Subdomain `cnc.florianziesche.com` ist jetzt erstellt.  
> SiteGround legt automatisch einen Ordner an: `public_html/cnc/`

### 1.3 Prüfen

- Der neue Ordner erscheint unter **"Site"** → **"File Manager"** → `public_html/cnc/`
- DNS wird automatisch konfiguriert (keine manuelle Einrichtung nötig bei SiteGround)

---

## Schritt 2: Dateien vorbereiten

**⏱️ Geschätzte Zeit: 10 Minuten**

### 2.1 Arbeitsordner erstellen

```bash
# Terminal öffnen und Ordner erstellen
mkdir -p ~/Desktop/cnc-deploy
cd ~/Desktop/cnc-deploy
```

### 2.2 Dateien kopieren und umbenennen

```bash
# Landing Page → index.html
cp /Users/florianziesche/.openclaw/workspace/products/cnc-planner/landing-page.html ./index.html

# Datenschutz (bleibt gleich)
cp /Users/florianziesche/.openclaw/workspace/products/cnc-planner/datenschutz.html ./datenschutz.html

# Demo → demo.html
cp /Users/florianziesche/.openclaw/workspace/projects/cnc-planner/demo-v12.html ./demo.html
```

### 2.3 Links anpassen

Die folgenden Änderungen müssen in den Dateien vorgenommen werden:

#### In `index.html`:

1. **Canonical URL anpassen** (Zeile ~8):
```html
<!-- ALT -->
<link rel="canonical" href="https://cncplanner.de">

<!-- NEU -->
<link rel="canonical" href="https://cnc.florianziesche.com">
```

2. **OG-Meta Tags ergänzen** (nach den bestehenden Meta-Tags):
```html
<meta property="og:url" content="https://cnc.florianziesche.com">
```

3. **Datenschutz-Link prüfen** (im Footer):
   - Sicherstellen, dass er auf `datenschutz.html` verweist (sollte bereits korrekt sein)

#### In `datenschutz.html`:

1. **Logo-Link anpassen** (Zeile ~57):
```html
<!-- ALT -->
<a href="landing-page.html" class="logo">

<!-- NEU -->
<a href="index.html" class="logo">
```

2. **Zurück-Link anpassen** (Zeile ~62):
```html
<!-- ALT -->
<a href="landing-page.html" class="back-link">← Zurück zur Startseite</a>

<!-- NEU -->
<a href="index.html" class="back-link">← Zurück zur Startseite</a>
```

3. **Footer-Link anpassen** (am Ende):
```html
<!-- ALT -->
<a href="landing-page.html">Startseite</a> | <a href="landing-page.html#impressum">Impressum</a>

<!-- NEU -->
<a href="index.html">Startseite</a> | <a href="index.html#impressum">Impressum</a>
```

#### In `demo.html`:

1. **Link zur Landing Page hinzufügen** (optional, im Header):
```html
<!-- Im Header nach dem Logo einen "Zurück"-Link ergänzen -->
<a href="index.html" style="color: var(--gray-500); text-decoration: none; font-size: 0.9rem;">← Zurück zur Startseite</a>
```

### 2.4 Schnell-Änderung mit sed (macOS Terminal)

```bash
cd ~/Desktop/cnc-deploy

# index.html: Canonical URL ändern
sed -i '' 's|https://cncplanner.de|https://cnc.florianziesche.com|g' index.html

# datenschutz.html: landing-page.html → index.html
sed -i '' 's|landing-page.html|index.html|g' datenschutz.html
```

### 2.5 Finale Ordnerstruktur prüfen

```bash
ls -la ~/Desktop/cnc-deploy/
```

Erwartete Ausgabe:
```
index.html        # Landing Page (~50KB)
datenschutz.html  # Datenschutz (~8KB)
demo.html         # Demo (~120KB)
```

---

## Schritt 3: Dateien hochladen

**⏱️ Geschätzte Zeit: 5 Minuten**

### Option A: SiteGround File Manager (empfohlen)

1. **File Manager öffnen:**
   - Site Tools → **"Site"** → **"File Manager"**
   
2. **Zum Zielordner navigieren:**
   - Klicke auf `public_html`
   - Klicke auf `cnc`

3. **Dateien hochladen:**
   - Klicke oben auf **"File Upload"** (↑ Icon)
   - Wähle alle 3 Dateien aus `~/Desktop/cnc-deploy/`:
     - `index.html`
     - `datenschutz.html`
     - `demo.html`
   - Klicke **"Upload"**

4. **Bestätigen:**
   - Alle 3 Dateien sollten jetzt im Ordner `/public_html/cnc/` sichtbar sein

### Option B: FTP Upload

Falls du lieber FTP verwendest:

1. **FTP-Zugangsdaten holen:**
   - Site Tools → **"Site"** → **"FTP Accounts"**
   - Neuen FTP-Account erstellen oder bestehenden verwenden
   - Zugangsdaten notieren:
     - Host: `ftp.florianziesche.com` oder IP aus Site Tools
     - User: dein FTP-Username
     - Passwort: dein FTP-Passwort

2. **Mit FTP-Client verbinden:**
   ```bash
   # Terminal mit sftp
   sftp username@florianziesche.com
   
   # Oder mit Cyberduck/FileZilla
   ```

3. **Dateien hochladen:**
   ```bash
   cd public_html/cnc
   put index.html
   put datenschutz.html
   put demo.html
   ```

---

## Schritt 4: SSL aktivieren (Let's Encrypt)

**⏱️ Geschätzte Zeit: 5 Minuten**

### 4.1 SSL Manager öffnen

1. Site Tools → **"Security"** → **"SSL Manager"**

### 4.2 SSL für Subdomain installieren

1. Im Dropdown **"Select Domain"** wähle: `cnc.florianziesche.com`
2. Wähle **"Let's Encrypt"** als SSL-Typ
3. Klicke **"Get"** oder **"Install"**

> ⏳ SSL-Zertifikat wird automatisch generiert (1-2 Minuten)

### 4.3 HTTPS erzwingen

1. Site Tools → **"Security"** → **"HTTPS Enforce"**
2. Wähle `cnc.florianziesche.com`
3. Schalte **"HTTPS Enforce"** auf **ON**

> ✅ Alle HTTP-Anfragen werden automatisch zu HTTPS umgeleitet.

---

## Schritt 5: Testen

**⏱️ Geschätzte Zeit: 10 Minuten**

### 5.1 Basis-URLs testen

Öffne im Browser (am besten Inkognito-Modus):

| URL | Erwartung |
|-----|-----------|
| `https://cnc.florianziesche.com` | Landing Page lädt |
| `https://cnc.florianziesche.com/demo.html` | Demo lädt |
| `https://cnc.florianziesche.com/datenschutz.html` | Datenschutz lädt |
| `http://cnc.florianziesche.com` | Redirect zu HTTPS |

### 5.2 Funktions-Checkliste

#### Landing Page (`index.html`):
- [ ] Seite lädt ohne Fehler
- [ ] Logo und Styling korrekt
- [ ] Navigation Links funktionieren (Anker-Links)
- [ ] "Demo anfordern" Button scrollt zu Formular
- [ ] ROI-Rechner funktioniert (Eingabefelder + Live-Berechnung)
- [ ] Demo-Vorschau Tabs funktionieren
- [ ] Footer Links funktionieren
- [ ] Datenschutz-Link im Footer führt zu `/datenschutz.html`

#### Demo (`demo.html`):
- [ ] Seite lädt ohne Fehler
- [ ] Alle Tabs funktionieren (Angebot, Kalkulation, Werkzeuge, etc.)
- [ ] Beispielprojekte klickbar
- [ ] Rohmaß-Editor berechnet live
- [ ] PDF/CSV Export Buttons vorhanden

#### Datenschutz (`datenschutz.html`):
- [ ] Seite lädt ohne Fehler
- [ ] "Zurück zur Startseite" Link führt zu `index.html`
- [ ] Logo-Klick führt zu `index.html`

### 5.3 Mobile testen

- [ ] Landing Page mobil-responsiv (iPhone/Android)
- [ ] Navigation funktioniert auf Mobilgeräten
- [ ] Formulare nutzbar auf Touch-Devices

### 5.4 Performance prüfen (optional)

1. [PageSpeed Insights](https://pagespeed.web.dev/) → URL eingeben
2. [GTmetrix](https://gtmetrix.com/) → Performance messen

---

## 🔧 Troubleshooting

### Problem: "Seite nicht gefunden" (404)

**Mögliche Ursachen:**
- Subdomain noch nicht propagiert (DNS braucht manchmal bis zu 24h)
- Dateien im falschen Ordner

**Lösung:**
```bash
# Prüfen ob Ordner existiert
# In Site Tools → File Manager → public_html/cnc/
# Dateien sollten dort liegen
```

### Problem: SSL-Zertifikat nicht aktiv

**Mögliche Ursachen:**
- DNS noch nicht vollständig propagiert
- Let's Encrypt Rate Limit erreicht

**Lösung:**
1. 10-15 Minuten warten
2. SSL Manager erneut öffnen und "Renew" klicken
3. Falls Problem besteht: SiteGround Support kontaktieren

### Problem: Seite lädt, aber Styling fehlt

**Mögliche Ursachen:**
- CSS ist inline, also sollte das nicht passieren
- Browser-Cache

**Lösung:**
```bash
# Hard Refresh im Browser
# Mac: Cmd + Shift + R
# Windows: Ctrl + Shift + R
```

### Problem: Formular sendet nicht (Formspree)

**Mögliche Ursachen:**
- Formspree-Endpoint nicht korrekt konfiguriert

**Lösung:**
1. Bei [formspree.io](https://formspree.io) einloggen
2. Neues Formular erstellen für `cnc.florianziesche.com`
3. Endpoint-URL in `index.html` aktualisieren:
```html
<form action="https://formspree.io/f/DEIN_FORMULAR_ID" method="POST">
```

### Problem: Links intern führen zu falscher Seite

**Lösung:**
Alle Referenzen zu `landing-page.html` durch `index.html` ersetzen (siehe Schritt 2.3)

---

## 📝 Nach dem Deployment

### 1. Google Search Console hinzufügen (empfohlen)

1. [search.google.com/search-console](https://search.google.com/search-console)
2. Property hinzufügen: `https://cnc.florianziesche.com`
3. Verifizierung via DNS-Eintrag oder HTML-Tag

### 2. Analytics einrichten (optional)

Falls noch nicht vorhanden, Google Analytics oder Plausible einbinden.

### 3. Formspree aktivieren

1. Bei [formspree.io](https://formspree.io) registrieren
2. Formular erstellen
3. Endpoint in `index.html` eintragen
4. Bestätigungs-E-Mail konfigurieren

---

## 📂 Backup-Strategie

SiteGround erstellt automatische tägliche Backups. Zusätzlich:

```bash
# Lokales Backup der deploytes Dateien
cp -r ~/Desktop/cnc-deploy ~/Backups/cnc-planner-$(date +%Y%m%d)
```

---

## ✅ Deployment-Checkliste (zum Abhaken)

```
[ ] 1. SiteGround Login erfolgreich
[ ] 2. Subdomain cnc.florianziesche.com erstellt
[ ] 3. Dateien vorbereitet und umbenannt
[ ] 4. Links in Dateien angepasst
[ ] 5. Dateien hochgeladen in /public_html/cnc/
[ ] 6. SSL-Zertifikat installiert
[ ] 7. HTTPS Enforce aktiviert
[ ] 8. Alle Seiten laden korrekt
[ ] 9. Alle Links funktionieren
[ ] 10. Mobile Ansicht geprüft
```

---

## 🆘 Support

Bei Problemen:

- **SiteGround Support:** 24/7 Live Chat im Site Tools
- **Technische Fragen:** florian@florianziesche.com

---

*Guide erstellt: Februar 2026 | Version 1.0*
