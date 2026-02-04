# 🚀 CNC Planer Pro Website → Cloudflare Pages deployen

> **Zeitaufwand:** 5 Minuten aktiv + warten auf DNS
> **Was du brauchst:** Cloudflare-Account, INWX-Login, die Dateien in `~/Desktop/cnc-deploy/`
> **Domain:** cnc-planer.de (bereits bei INWX gekauft)

---

## Schritt 1: Cloudflare Pages Projekt erstellen

1. Öffne **[dash.cloudflare.com](https://dash.cloudflare.com)**
2. Links im Menü: **Workers & Pages** → **Pages**
3. Klick auf **"Create a project"** → **"Direct Upload"** wählen (nicht Git)
4. Projektname eingeben: `cnc-planer` (wird Teil der Preview-URL)
5. Klick **"Create project"**

## Schritt 2: Dateien hochladen

1. Klick auf **"Upload"** oder drag & drop
2. **Alle Dateien** aus `~/Desktop/cnc-deploy/` hochladen
   - Am einfachsten: Im Finder den Ordnerinhalt markieren (⌘+A) und in den Browser ziehen
   - ⚠️ Den **Inhalt** des Ordners hochladen, nicht den Ordner selbst
3. Warten bis alles grün ist
4. Klick **"Deploy site"**

## Schritt 3: Preview testen

1. Du bekommst eine URL wie `cnc-planer.pages.dev`
2. **Öffne die URL** und prüfe ob alles aussieht wie gewollt
3. Wenn was kaputt ist: Dateien fixen, neues Deployment machen (dauert 30 Sek)

## Schritt 4: Custom Domain hinzufügen (cnc-planer.de)

1. Im Cloudflare Pages Projekt: Tab **"Custom domains"**
2. Klick **"Set up a custom domain"**
3. Eingeben: `cnc-planer.de`
4. Cloudflare wird dich fragen, die Domain zu Cloudflare hinzuzufügen
5. **Free Plan** auswählen → weiter

Cloudflare gibt dir jetzt **zwei Nameserver**, z.B.:
```
anna.ns.cloudflare.com
bob.ns.cloudflare.com
```
**Diese kopieren!** Du brauchst sie im nächsten Schritt.

## Schritt 5: INWX Nameserver ändern

1. Öffne **[inwx.de](https://www.inwx.de)** → Login
2. Gehe zu **Domainliste** → `cnc-planer.de` anklicken
3. Unter **Nameserver** → auf **Bearbeiten** klicken
4. Die bestehenden Nameserver **löschen**
5. Die **Cloudflare-Nameserver** eintragen (die beiden aus Schritt 4)
6. **Speichern**

## Schritt 6: Warten + Verifizieren

1. Zurück zu **Cloudflare Dashboard** → die Domain sollte auf "Pending" stehen
2. DNS-Propagation dauert **5 Min bis 24h** (meist unter 1h)
3. Cloudflare schickt eine **E-Mail** wenn die Domain aktiv ist
4. Dann: `https://cnc-planer.de` aufrufen → 🎉

> **Bonus:** Cloudflare aktiviert automatisch HTTPS (SSL) – du musst nichts extra machen.

---

## Falls was schiefgeht

| Problem | Lösung |
|---|---|
| "Domain not yet active" | Nameserver-Änderung braucht noch Zeit. Warte 1-2h. |
| Seite zeigt 404 | Falscher Ordner hochgeladen? Muss `index.html` im Root sein. |
| CSS/Bilder fehlen | Pfade prüfen – relative Pfade verwenden (`./style.css` nicht `/style.css`) |
| INWX zeigt alte Nameserver | Hard-Refresh (⌘+Shift+R), oder 5 Min warten |

## Auch `www.cnc-planer.de` einrichten?

1. In Cloudflare Pages → Custom domains → **"Set up a custom domain"**
2. Eingeben: `www.cnc-planer.de`
3. Cloudflare erstellt automatisch den CNAME-Record
4. Fertig – leitet automatisch auf die Hauptdomain weiter

---

*Erstellt: 2026-02-04*
