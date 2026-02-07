# Website Deployment Options — Monday Decision

## Option A: Vercel (Empfohlen ⭐)

**Was:** Free static hosting, CDN, custom domain, HTTPS
**Wie:** GitHub repo → Vercel auto-deploys on push
**Kosten:** $0 (Hobby Plan reicht)
**Custom Domain:** ainaryventures.com → DNS A-Record ändern
**Setup-Zeit:** ~15 Minuten
**Vorteile:**
- Schnellste Option
- Auto-Deploy bei Git Push
- Global CDN (schnell weltweit)
- Analytics built-in
- Preview URLs für Drafts
**Nachteile:**
- Braucht GitHub-Repo (privat möglich)

## Option B: Cloudflare Pages

**Was:** Free static hosting via Cloudflare
**Kosten:** $0 (unlimited bandwidth)
**Custom Domain:** Cloudflare DNS (wenn Domain dort liegt)
**Setup-Zeit:** ~20 Minuten
**Vorteile:**
- Unlimited bandwidth (even free)
- Cloudflare security/DDoS built-in
- Schnell
**Nachteile:**
- Domain muss zu Cloudflare DNS (Migration)

## Option C: GitHub Pages

**Was:** Free hosting direkt von GitHub
**Kosten:** $0
**Custom Domain:** CNAME record
**Setup-Zeit:** ~10 Minuten
**Vorteile:**
- Einfachste Option
- Direkt im Repo
**Nachteile:**
- Langsamer als Vercel/Cloudflare
- Kein Edge CDN
- Public repo required für free

## Empfehlung

**Vercel** — setup dauert 15 Min, kostet nichts, und auto-deployed bei jedem `git push`. Kann ich am Montag in der Session live machen.

### Schritte (wenn entschieden):
1. Private GitHub repo erstellen (`ainary-website`)
2. `assets/ainary-website/` Files pushen
3. Vercel-Account mit GitHub verbinden
4. Domain `ainaryventures.com` DNS → Vercel
5. HTTPS automatisch
6. Fertig — jeder `git push` = Live-Update

### Domain-Status:
- `ainaryventures.com` — aktiv (war kurz suspended, Feb 5 reaktiviert)
- DNS-Registrar: prüfen wo die Domain liegt (GoDaddy? Namecheap?)
- Email: `f.ziesche.us@gmail.com` temporär, `florian@ainaryventures.com` wenn MX konfiguriert

---

*Erstellt: 2026-02-07 15:00 CET*
