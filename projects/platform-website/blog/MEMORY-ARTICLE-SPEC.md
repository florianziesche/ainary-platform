# Memory Article: IST → SOLL Änderungsliste

**Datei:** `blog/ai-agent-memory-what-anthropic-is-missing.html`
**Stand:** 2026-02-28
**Regel:** Jede Änderung hat eine Nummer. Jede wird programmatisch verifiziert.

---

## A. Farben (Non-Standard → Standard)

| # | IST | SOLL | Kontext | Warum |
|---|-----|------|---------|-------|
| A1 | `#5c6370` (11×) | `#55555e` | CSS-Fallback für --text-muted | Falsche Muted-Farbe. Standard ist #55555e. |
| A2 | `#8a8f98` (7×) | `#8b8b95` | CSS-Fallback für --text-secondary | Falsche Secondary-Farbe. Standard ist #8b8b95. |
| A3 | `#888` (2×) | `#55555e` | Inline Fallback | Shorthand, nicht im Standard. → text-muted. |
| A4 | `#e0e0e0` (2×) | `#ededf0` | Inline Fallback | Falsche White-Farbe. Standard ist #ededf0. |
| A5 | `#48AE6E` (1×) | `#238551` | Gradient endpoint für Score-Bar | Keine Gradient-Varianten. Nur Standardfarben. |
| A6 | `#d4b85c` (1×) | `#c8aa50` | Gold gradient endpoint | Keine Gold-Varianten. |
| A7 | `#ffffff` (1×) | KEEP | Ambient blob (gradient) | Blobs dürfen abweichen (physikalisches Licht). |
| A8 | `#e8f0ff` (1×) | KEEP | Ambient blob | Wie A7. |
| A9 | `#b0c4e8` (1×) | KEEP | Ambient blob | Wie A7. |
| A10 | `#a08030` (1×) | KEEP | Gold blob | Wie A7. |
| A11 | `#111` (2×) | `#111116` | Shorthand | Vollständige Hex-Notation. |

**Total Fixes: 7 (A1-A6, A11). 4 KEEP (Blobs).**

## B. Border-Radius (Non-Standard → Standard)

| # | IST | SOLL | Count | Warum |
|---|-----|------|-------|-------|
| B1 | `4px` | `3px` | 5× | Standard: 3px für kleine Badges. |
| B2 | `12px` | `8px` | 6× | Standard: 8px für Boxes. Kein 12px. |

## C. Cross-Synthesis Features (NEU)

| # | Feature | Beschreibung | Quelle |
|---|---------|--------------|--------|
| C1 | **Trust Bar** | Unter Hero: "21 Sources · 8 Systems Compared · EIJA-Verified" — eine Zeile, gold-border-left, --bg-surface | Insight 4 (Mobile-Trust) |
| C2 | **EIJA Legende prominenter** | Bestehende EIJA-Legende ÜBER den Artikel-Body verschieben, nicht drin versteckt | Insight 1 (Trust-Aesthetics) |
| C3 | **Gold Dot Motif** | ● vor jeder H2-Section als visueller Marker. ● vor Source-Citations. | Insight 5 (Motif-as-Data) |
| C4 | **Product Link** | In "What This Means for Builders" Section: Link zu `/de/article-agenttrust.html` + Radar-Dashboard als "See our system in action" | Insight 2 (Demo-Content Fusion) |
| C5 | **Number Counting** | Stats Row Zahlen (21, 8, 5) animieren beim Scroll-Reveal (0→Ziel in 400ms) | Insight 3 (Animation-Trust) |
| C6 | **CTA "See Analysis"** | Neben Newsletter-CTA: "See our election analysis live →" Link zu Radar/Demo | Insight 6 (Pricing-as-Proof) |

## D. Bestehende Probleme

| # | Problem | Fix |
|---|---------|-----|
| D1 | `#111` shorthand | → `#111116` (A11) |
| D2 | 0 EIJA-Badges im Body-Text | EIJA-Badges existieren bereits (5 gefunden in audit), aber als CSS-Klassen. Kein Fix nötig — sie sind da. |
| D3 | Keine Dashboard-Links | Fix via C4 + C6 |
| D4 | No `●` gold dots | Fix via C3 |

## E. NICHT ändern

| Item | Warum |
|---|---|
| Blob-Farben (A7-A10) | Physikalische Licht-Simulation, darf abweichen |
| Artikel-Text/Inhalt | Nur Design, kein Content-Rewrite |
| JSON-LD Schema | Bereits korrekt |
| OG/Twitter Tags | Bereits korrekt |
| Shared Components (nav/footer) | Werden separat gehandhabt |

---

## Verifikations-Script

Für jeden Punkt A1-A11, B1-B2, C1-C6 wird ein Python-Check geschrieben:
- A1-A11: `grep -c` für alte Hex-Werte → muss 0 sein (außer KEEP)
- B1-B2: `grep -c` für alte Radii → muss 0 sein
- C1-C6: Pattern-Match für neue Elemente → muss >0 sein

**Pass = ALLE Checks grün. Fail = Kein Deploy.**
