# CNC Planner Pro — Cloudflare Pages Setup

**Ziel:** cncplanner.de auf Cloudflare Pages (kostenlos)
**Geschätzte Zeit:** 20 Minuten

---

## Schritt 1: Cloudflare Account (2 min)

1. → https://dash.cloudflare.com/sign-up
2. Account erstellen (oder einloggen falls vorhanden)

---

## Schritt 2: Domain registrieren (5 min)

1. Dashboard → **Domain Registration** → **Register Domain**
2. Suche: `cncplanner.de`
3. Kaufen (~€5/Jahr, Cloudflare verkauft zum Selbstkostenpreis)
4. Kontaktdaten eingeben (DENIC braucht deutsche Adresse → Schloß-Berg-Str. 2, 81549 München)

> Falls cncplanner.de vergeben: `cnc-planner.de` als Alternative

---

## Schritt 3: Cloudflare Pages Projekt (5 min)

### Option A: Direct Upload (einfachste)

1. Dashboard → **Workers & Pages** → **Create**
2. Wähle **Pages** → **Upload assets**
3. Projektname: `cncplanner`
4. Ordner hochladen: alle Dateien aus `~/Desktop/cnc-deploy/`:
   - `index.html`
   - `demo.html`
   - `datenschutz.html`
   - `impressum.html`
   - `sitemap.xml`
   - `robots.txt`
5. **Deploy**

> Ergebnis: Seite läuft sofort auf `cncplanner.pages.dev`

### Option B: GitHub (für spätere Updates)

1. GitHub Repo erstellen: `cncplanner-website`
2. Files pushen
3. In Cloudflare: Pages → Connect to Git → Repo auswählen
4. Auto-Deploy bei jedem Push

---

## Schritt 4: Custom Domain verbinden (3 min)

1. Pages Projekt → **Custom domains** → **Set up a custom domain**
2. Eingabe: `cncplanner.de`
3. Cloudflare konfiguriert DNS automatisch (Domain ist ja schon bei CF)
4. Auch hinzufügen: `www.cncplanner.de` → Redirect auf `cncplanner.de`

> SSL wird automatisch aktiviert (kein manueller Schritt)

---

## Schritt 5: Links in Dateien anpassen

Vor dem Upload diese Änderungen:

```bash
cd ~/Desktop/cnc-deploy

# Canonical URL
sed -i '' 's|cnc.florianziesche.com|cncplanner.de|g' index.html

# Falls in anderen Dateien referenziert
sed -i '' 's|cnc.florianziesche.com|cncplanner.de|g' datenschutz.html
sed -i '' 's|cnc.florianziesche.com|cncplanner.de|g' impressum.html
```

---

## Schritt 6: Redirect von alter URL (optional)

Falls cnc.florianziesche.com weiter funktionieren soll:
- SiteGround: Redirect Rule `cnc.florianziesche.com → cncplanner.de` (301)
- Oder einfach abschalten

---

## Kosten-Vergleich

| | SiteGround | Cloudflare Pages |
|---|-----------|-----------------|
| Hosting | €27/Mo | €0 |
| Domain | (inkl.) | ~€5/Jahr |
| SSL | (inkl.) | (inkl.) |
| CDN | Basic | Global Edge |
| **Jahreskosten** | **€324** | **~€5** |
| **Ersparnis** | — | **€319/Jahr** |

---

## Checkliste

```
[ ] 1. Cloudflare Account erstellt
[ ] 2. cncplanner.de registriert
[ ] 3. Links in Dateien angepasst (sed-Befehle oben)
[ ] 4. Pages Projekt erstellt + Dateien hochgeladen
[ ] 5. Custom Domain verbunden
[ ] 6. Seite läuft auf https://cncplanner.de
[ ] 7. Google Search Console auf neue Domain umstellen
[ ] 8. Alte Subdomain weiterleiten oder abschalten
```

---

*Erstellt: 2026-02-03*
