# Corporate Identity — 3 Optionen zur Auswahl

*Erstellt nach Analyse von: Perplexity, Linear, Clay, Superhuman, Anthropic, v0.dev, GAI Insights + unsere existierende CI*

---

## Was ich gelernt habe (Research)

| Site | Stärke | Schwäche | Lesson für uns |
|------|--------|----------|----------------|
| **Perplexity** | Clean, centered, Input zuerst | Warm beige fühlt sich "soft" an | Chat-first UI funktioniert — Input im Zentrum |
| **Linear** | Dark mode excellence, Premium-Gefühl | Kann kalt/technisch wirken | Dark + subtile Animationen = "serious tool" |
| **Clay** | Light mode, verspielt, illustriert | Zu bunt, zu viele Elemente | Social Proof + Use Cases verkaufen |
| **Superhuman** | Purple brand, klar, confident | Fast zu minimalistisch | Einheitliche Akzentfarbe = Brand-Erkennung |
| **Anthropic** | Intellektuell, warm-neutral, editorial | Kein SaaS-Gefühl | Typography-driven statt Farb-driven |
| **v0.dev** | Input-zentriert, Templates als Starter | Sehr neutral/generic | Template-Galerie = Engagement |
| **GAI Insights** | Content-heavy, Newsletter-Push | Veraltet, kein Tool-Erlebnis | Daily News = Traffic, aber Design muss modern sein |

### Key Insight
Unsere Tools sind DARK MODE (X-Ray, Advisory Board, Research Engine). Die Landing Page sollte den gleichen Vibe haben — oder bewusst kontrastieren. Drei Strategien:

---

## Option A: "OBSIDIAN" — Full Dark, Linear-Inspired

**Philosophie:** Premium Tool Platform. Alles dunkel. Kein Kompromiss.

**Farben:**
```
Background:     #0a0a0f (fast schwarz)
Surface:        #141418 (Cards)
Surface Hover:  #1c1c22
Border:         rgba(255,255,255,0.08)
Text Primary:   #e8e8ec
Text Secondary: #8b8b95
Accent:         #c8aa50 (Ainary Gold) — EINZIGE Farbe
```

**Vibe:** Linear meets Bloomberg Terminal. Für Leute die $499/mo zahlen.

**Typography:** Inter (clean) + JetBrains Mono (Daten/Metriken)

**Logo:** Geometrisches "A" oder Lightning Bolt in Gold auf Schwarz. Minimal.

**Navigation:** Sidebar links (wie Perplexity/Linear), nicht Top-Nav.

**Pro:**
- Konsistent mit allen Tool-Reports (X-Ray, Research Engine)
- Premium-Gefühl rechtfertigt höhere Preise
- Ein Farbsystem (Gold) = starke Brand-Erkennung
- Sehr differenziert von GAI Insights (die sind generic light mode)

**Contra:**
- Blog/News fühlt sich auf Dark Mode schwerer zu lesen an
- Kann einschüchternd wirken für Mittelstand-Kunden
- Dark mode websites konvertieren statistisch etwas schlechter

**Zielgruppe:** VCs, Tech-Executives, Startups, AI-Savvy Leaders

---

## Option B: "SANDSTONE" — Warm Light, Anthropic-Inspired

**Philosophie:** Intellektuell, warm, vertrauenswürdig. Thinking Partner, nicht Tool.

**Farben:**
```
Background:     #faf8f5 (warmes Off-White)
Surface:        #ffffff
Surface Hover:  #f5f2ed
Border:         #e5e0d8
Text Primary:   #1a1816 (warmes Schwarz)
Text Secondary: #6b6560
Accent:         #c8aa50 (Ainary Gold)
Accent Muted:   rgba(200,170,80,0.12)
```

**Vibe:** Anthropic meets Notion. Für Leute die nachdenken bevor sie handeln.

**Typography:** 
- Headlines: Instrument Serif (editorial, sophisticated) ODER Inter Display (clean)
- Body: Inter (readable)
- Data: JetBrains Mono

**Logo:** Wordmark "Ainary" in Serif + Gold Punkt. Oder handschriftliches "A".

**Navigation:** Top-Nav (klassisch), sticky.

**Pro:**
- Vertrauenswürdiger für Consulting-Kunden und Mittelstand
- Blog/News liest sich besser auf Light Mode
- Warm = approachable, nicht einschüchternd
- Editorial Vibe passt zu "Thought Leadership"

**Contra:**
- Kontrast zu den Dark Mode Tool-Reports (User Experience Bruch)
- Weniger "wow" beim ersten Besuch
- Kann "generic" wirken wenn nicht gut gemacht

**Zielgruppe:** Consulting-Kunden, Mittelstand, C-Suite, Content-Leser

---

## Option C: "DUALITY" — Adaptiver Mode, Perplexity-Inspired

**Philosophie:** Best of both worlds. Landing Page = Light. Tools = Dark. Auto-Switch.

**Farben:**
```
LIGHT (Landing, Blog, News):
  Background:   #fafafa
  Surface:      #ffffff
  Text:         #111111
  Accent:       #c8aa50

DARK (Tools, Advisory Board, Reports):
  Background:   #0a0a0f
  Surface:      #141418
  Text:         #e8e8ec
  Accent:       #c8aa50
  
SHARED:
  Gold:         #c8aa50 (überall gleich = Marken-Anker)
  Font:         Inter (überall gleich = Konsistenz)
  Radius:       12px (überall gleich)
```

**Vibe:** Perplexity-Klarheit im Light Mode, Linear-Power im Dark Mode.

**Typography:** Inter überall. Keine Serif. Clean = erkennbar.

**Logo:** Abstraktes Prisma-"A" (teilt Licht in Spektrum — Light/Dark Duality). Gold.

**Navigation:** 
- Landing: Top-Nav (klassisch, einladend)
- App/Tools: Sidebar (power-user, wie Perplexity)

**Transition:** Wenn User von Landing → Tool klickt, smooth Dark Mode Transition.

**Pro:**
- Jeder Kontext bekommt sein optimales Design
- Blog lesbar (Light), Tools impressive (Dark)
- Gold als Konstante hält alles zusammen
- Flexibelste Option für verschiedene Zielgruppen

**Contra:**
- Mehr CSS zu maintainen
- Risk: Kann inkonsistent wirken wenn Übergang nicht smooth ist
- Komplexer zu bauen

**Zielgruppe:** Alle — anpassbar je nach Kontext

---

## Mein Vote

**Option C (Duality)** mit einer Einschränkung: 

Für v1 starten wir mit **Dark Mode everywhere** (Option A) weil:
1. Unsere Tools sind bereits dark → Konsistenz
2. Schneller zu bauen (ein System statt zwei)
3. Differenziert uns sofort von GAI Insights und jeder anderen Consulting-Site
4. Premium-Pricing wird glaubwürdiger

Dann in v2 (nach Launch, nach erstem Feedback): Blog/News auf Light Mode umstellen → Option C.

**Aber das ist MEIN Vote. Du entscheidest.**

---

## Was alle 3 Optionen gemeinsam haben

- **Gold (#c8aa50)** als einzige Akzentfarbe
- **Inter** als Hauptfont
- **JetBrains Mono** für Daten/Metriken
- **12px Border Radius**
- **Keine Emoji** — nur SVG Icons
- **Keine Stock Photos** — nur Screenshots, Daten, UI
- **"Florian Ziesche" Branding** (nicht Ainary) für DE-Markt

---

*Nächster Schritt: Florian wählt A, B, oder C. Dann baue ich das komplette Platform-Konzept darauf auf.*
