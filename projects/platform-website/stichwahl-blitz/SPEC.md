# Stichwahl-Blitz — SPEC

## Mission
Am 8. März 2026 um ~22:00 Uhr stehen die Ergebnisse fest.
~300 Gemeinden gehen in Stichwahl (15% von 2.056).
Jeder Stichwahl-Kandidat hat 14 Tage und KEINE Gegner-Analyse.

**Wir liefern sie — bevor sie danach suchen.**

## Timeline
- **JETZT → 7. März**: Infrastruktur bauen + testen
- **8. März 18:00**: Wahllokale schließen
- **8. März ~20:00**: Erste Ergebnisse auf BR24 / Landesamt
- **8. März 22:00-24:00**: Scraper läuft, Stichwahl-Paarungen erkannt
- **9. März 08:00**: 300 personalisierte Emails raus
- **9.-22. März**: Follow-up Sequenz, Self-Service-Käufe

## 4 Komponenten

### 1. Wahlergebnis-Scraper (`scraper/`)
**Quelle**: wahlen.bayern.de (Bayerisches Landesamt für Statistik)
- Alternativ: BR24 Liveticker, kommunalwahl.bayern.de
- Parse: Gemeinde, Kandidaten, Stimmen, %, Stichwahl ja/nein
- Output: `results/2026-03-08.json`

**Stichwahl-Erkennung:**
- Kein Kandidat >50% im 1. Wahlgang = Stichwahl
- Top 2 Kandidaten → Stichwahl-Paarung
- Output pro Stichwahl: `{gemeinde, kandidat1, kandidat2, stimmen1, stimmen2, diff}`

**Frequenz**: Alle 5 Minuten ab 18:00, bis alle Gemeinden gemeldet

### 2. Stichwahl-Template (`templates/`)
**Input**: Stichwahl-Paarung + Ontology-Daten (wenn vorhanden) + Wahlergebnis
**Output**: Personalisierte Email + Mini-Dossier

**Template-Varianten:**
- **A: Bekannte Stadt** (9 Dossier-Städte) — Voll personalisiert mit Follower-Daten, Patterns, Insights
- **B: Top-50 Stadt** (weitere 22 im Radar) — Basis-Intel + generische Patterns
- **C: Unbekannte Gemeinde** (restliche ~270) — Nur Wahlergebnis + generische Cross-City-Patterns

**Email-Struktur:**
```
Betreff: {Vorname}, Ihre Stichwahl-Analyse für {Gemeinde} — 14 Tage

Herr/Frau {Name},

Sie haben {X}% erreicht. Ihr Gegner {Gegner} hat {Y}%.
{Diff}% trennen Sie. 14 Tage entscheiden.

[Wenn bekannte Stadt:]
Unser Intelligence-System analysiert {Gemeinde} seit Wochen:
- {Gegner} hat {Follower} Instagram-Follower (Sie: {eigene_Follower})
- {Pattern-Insight aus Ontology}
- {Schwäche des Gegners}

[Für alle:]
Wir haben für die Kommunalwahl 2026 ein datengetriebenes Analyse-System gebaut.
Ihre kostenlose Kurzanalyse: {Link zu Dossier oder Mini-Report}

Die volle Stichwahl-Analyse — Gegner-Profil, Wähler-Wanderung, 
Mobilisierungs-Strategie — für €490 (einmalig, sofort verfügbar).

→ {Self-Service-Link}

Florian Ziesche
Ainary Intelligence
```

### 3. Email-Versand (`sender/`)
- Kontakt-Quellen: Partei-Fraktionen, Stadt-Websites, Wahlvorschläge (öffentlich)
- Tool: gog (Gmail API) oder Himalaya (IMAP/SMTP)
- Rate: Max 50/Stunde (Gmail-Limit), gestaffelt über 6 Stunden
- Tracking: Öffnungsrate, Klicks, Replies
- Follow-up: Tag 3 + Tag 7 automatisch (wenn keine Antwort)

### 4. Self-Service Landing Page (`stichwahl.html`)
- URL: ainaryventures.com/stichwahl
- Passwort: keins (öffentlich, Conversion > Exklusivität)
- Inhalt:
  - "Ihre Stichwahl-Analyse in 24 Stunden"
  - Preis: €490 einmalig
  - Was enthalten: Gegner-Profil, Social-Media-Audit, Wähler-Analyse, 3 Handlungsempfehlungen
  - Vertrauens-Signale: "9 Städte analysiert, 37 Kandidaten-Profile, Cross-City-Patterns aus 31 Quellen"
  - CTA: Stripe/PayPal Button oder Kontaktformular
  - FAQ: Datenschutz, Methodik, Lieferzeit

## Pricing
- **€490**: Volle Stichwahl-Analyse (Gegner-Profil + Strategie)
- **€0**: Kurzanalyse (3 Insights, Link im Email) — Lead Magnet
- **€1.470**: Franken-Bundle (3 Städte) — für Partei-Geschäftsstellen

## Zahlen
- ~2.056 Gemeinden wählen am 8.03
- ~15% gehen in Stichwahl = ~300 Gemeinden
- ~600 Kandidaten (je 2 pro Stichwahl)
- Email: 300-600 Emails (je nach ob beide Kandidaten)
- 5% Conversion = 15-30 Kunden × €490 = **€7.350 - €14.700**
- 1% Conversion = 3-6 Kunden × €490 = **€1.470 - €2.940**

## Data Sources für Scraper
1. **wahlen.bayern.de** — Offizielle Ergebnisse (Landesamt für Statistik)
2. **BR24** — Liveticker mit Ergebnissen
3. **kommunalwahl.bayern.de** — Wahlvorschläge (Kandidaten-Listen vorab!)
4. **Partei-Websites** — Email-Adressen der Kandidaten

## Pre-8.03 Vorbereitung
- [ ] Scraper bauen + testen mit 2020-Ergebnissen
- [ ] Template-Engine bauen (A/B/C Varianten)
- [ ] Stichwahl-Landing-Page live
- [ ] Email-Kontakte vorrecherchieren (Top-50 Städte)
- [ ] Stripe/PayPal Integration oder manueller Prozess
- [ ] Test-Run mit 2020-Daten simulieren
- [ ] Follow-up Sequenz vorbereiten

## Risiken
- Gmail 500/Tag Limit → gestaffelt über 2 Tage
- Kandidaten-Emails nicht öffentlich → Partei-Fraktionen als Fallback
- Wahlergebnisse erst spät (manche Gemeinden zählen langsam) → Batch-Versand
- €490 zu hoch für kleine Gemeinden → €290 Lite-Variante?
- DSGVO: Kaltakquise per Email an Politiker = zulässig (berechtigtes Interesse, öffentliche Personen)
