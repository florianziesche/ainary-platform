# Outreach Plan — Bayern Kommunalwahl 08.03.2026

**Status:** In Arbeit
**Deadline:** Emails müssen bis 26.02 raus (10 Tage vor Wahl)
**Ziel:** 50 personalisierte Outreach-Emails an Bayern-Kandidaten

---

## Priorisierung (ROI-basiert)

### Tier 1: OB tritt ab + Großstadt (HÖCHSTER Bedarf)
Offenes Rennen = viele Kandidaten = maximale Unsicherheit = maximale Zahlungsbereitschaft

| # | Stadt | EW | Abtr. OB | Top-Kandidaten | Analyse-Status |
|---|-------|-----|----------|----------------|----------------|
| 1 | **Bamberg** | 78K | Starke (SPD, 20J) | Huml (CSU), Glüsenkamp (Grüne), Niedermaier (SPD) | ✅ LIVE |
| 2 | **Regensburg** | 155K | Maltz-Schwarzfischer (SPD) | Freudenstein (CSU), Burger (SPD), Sigloch (Grüne) | ✅ LIVE |
| 3 | **Passau** | 53K | Dupper (SPD, 18J) | TBD — recherchieren | ❌ GENERIEREN |
| 4 | **Ottobrunn** | 22K | Loderer (CSU, 19J) | Schardt, Matella, Ulmer | ✅ LIVE |

### Tier 2: OB bleibt aber starke Herausforderer
Amtsinhaber = Vorteil, aber Herausforderer BRAUCHEN Intelligence

| # | Stadt | EW | Amtsinhaber | Herausforderer | Status |
|---|-------|-----|-------------|----------------|--------|
| 5 | **Nürnberg** | 520K | König (CSU) | Brehm (SPD), Grüne? | Pending |
| 6 | **München** | 1.5M | Reiter (SPD, 67) | CSU-Kandidat? | New |
| 7 | **Augsburg** | 300K | Weber (CSU) | SPD? Grüne? | New |
| 8 | **Erlangen** | 115K | Janik (Grüne, tritt ab?) | TBD | New |
| 9 | **Fürth** | 130K | Jung (SPD) | TBD | New |
| 10 | **Rosenheim** | 65K | TBD | TBD | New |

### Tier 3: Landkreise mit Landrats-Wechsel
Landräte die aufhören → offenes Rennen → Bedarf

| # | Landkreis | Abtr. Landrat | Status |
|---|-----------|---------------|--------|
| 11 | Kulmbach | Söllner (FW, 30J!) | New |
| 12 | Altötting | Schneider (CSU, 26J) | New |
| 13 | Bad Kissingen | Bold (CSU, 24J) | New |
| 14 | Donau-Ries | Rößle (CSU, 24J) | New |
| 15 | Bad Tölz-Wolfratshausen | Niedermaier (FW) | New |
| 16 | Landshut (LK) | Dreier (FW) | New |
| 17 | Oberallgäu | Baier-Müller (FW) | New |
| 18 | Miltenberg | Scherf (Grüne, einziger!) | New |

---

## Email-Template

### Betreff-Varianten (A/B Test):
A: "3 Erkenntnisse zu Ihrem Wahlkampf in {Stadt}"
B: "{Stadt}: Was Ihre Gegner planen"
C: "Datenbasierte Wahlkampf-Analyse für {Stadt} — kostenfrei"

### Email-Body:
```
Sehr geehrte/r {Anrede} {Name},

wir analysieren die Kommunalwahl am 8. März mit Methoden 
aus der politischen Intelligence — datenbasiert, quellengestützt, 
überparteilich.

Für {Stadt} haben wir {N} Quellen ausgewertet und dabei 
drei Erkenntnisse gewonnen, die Ihren Wahlkampf betreffen:

1. {Insight 1 — größtes Risiko/Chance}
2. {Insight 2 — Gegner-Dynamik}  
3. {Insight 3 — Strukturelles Pattern}

Die vollständige Analyse (Kandidaten-Dossiers, Netzwerk-Graph, 
Prognose, Handlungsempfehlungen):

→ {URL}

Kostenfrei bis zum Wahlabend. Vertraulich.

Mit freundlichen Grüßen,
Florian Ziesche
Ainary Intelligence
ainaryventures.com
```

---

## Kontakt-Recherche

Für jeden Kandidaten:
1. Offizielle Website (Impressum → Email)
2. Partei-Website (Ortsverband → Kontaktformular)
3. Rathaus-Website (wenn Amtsinhaber)
4. LinkedIn (falls vorhanden)
5. Wahlkampf-Website (kandidat2026.de Pattern)

---

## Metriken

- Emails gesendet: 0/50
- Öffnungsrate: TBD (Ziel: >40%)
- Link-Klicks: TBD (Ziel: >15%)
- Antworten: TBD (Ziel: >5%)
- Conversions (€490): TBD (Ziel: >3%)

---

## Blocker

- ❌ OpenAI API Quota leer → Dossier-Generierung per web_search + manuell
- ❌ Anthropic API Key nicht in Env → OpenClaw nutzen für LLM-Calls
- ✅ Voyage AI funktioniert (Embeddings)
- ✅ Pipeline funktioniert (validate + embed + deploy)
