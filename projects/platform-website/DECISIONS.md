# Platform Decisions Log

*Jede Entscheidung dokumentiert: Was, Warum, Wann, Alternativen.*
*Single Source of Truth für "Warum haben wir das so gemacht?"*

---

## D-001: Pricing-Modell → Credits (Lovable-Style)
**Datum:** 2026-02-12
**Entscheidung:** Credits-basiertes Pricing statt Flat-Fee oder klassische Tiers
**Alternativen:** A) Klassische Tiers — langweilig. B) Flat-Fee — riskant ohne Millionen User. C) ✅ Credits — transparent, skaliert
**Florians Input:** "Credits ist mein Bauchgefühl."

## D-002: Design Benchmark → Linear.app
**Datum:** 2026-02-12
**Entscheidung:** Linear.app als Qualitäts-Benchmark
**Florians Input:** "Das ist der Benchmark. Den musst du erreichen."

## D-003: CI Document vor jedem Build
**Datum:** 2026-02-12
**Entscheidung:** DESIGN-SYSTEM.md als Gesetz — kein Build ohne es zu lesen
**Florians Input:** "Dem muss jeder Build folgen."

## D-004: Farbsystem → Indigo + Gold Dual-Accent
**Datum:** 2026-02-12
**Entscheidung:** Indigo (#6366f1) = Primary (CTAs, Icons, Links). Gold (#c8aa50) = Special (Preise, Badges, Premium).
**Alternativen:** A) Gold only — Finance-Vibe. B) Indigo only — nicht differenziert. C) ✅ Indigo+Gold — unique Combo.
**Florians Input:** "C."

## D-005: Product-Farben als subtile Akzente
**Datum:** 2026-02-12
**Entscheidung:** Website Shell = Indigo+Gold. Product-Farben nur Icons/Badges.
**Florians Input:** "Product-Farben als subtile Akzente ist mein Instinkt."

## D-006: Fonts → Geist + Inter + JetBrains Mono
**Datum:** 2026-02-12
**Entscheidung:** Geist (Headlines), Inter (Body), JetBrains Mono (Data)
**Florians Input:** "Die Fonts schauen gut aus, gute Wahl."

## D-007: Trusted By → entfernt bis Launch
**Datum:** 2026-02-12
**Entscheidung:** Keine Fake-Logos. Social Proof nach Launch.
**Florians Input:** "Trusted by kann warten bis zum Launch."

## D-008: Stats → Kundenwert statt Kosten
**Datum:** 2026-02-12
**Entscheidung:** 90 sec / 243 Sources / 3 Rounds. Keine eigenen Kosten zeigen.
**Florians Input:** "Statt $0.15 eine andere KPI, der Kunde zahlt ja seinen Preis."

## D-009: Daily Brief → 4 Kategorien
**Datum:** 2026-02-12
**Entscheidung:** AI & Tech / Enterprise / Startups & VC / Tools & Products

## D-010: Product-Grafiken → echte Screenshots, keine Kundennamen
**Datum:** 2026-02-12
**Entscheidung:** Screenshots von eigenen Reports, aber KEINE echten Firmennamen. Fiktive Companies für Demos.
**Florians Input:** "Keinen Kundennamen."

## D-011: Build-Reihenfolge
**Datum:** 2026-02-12
**Entscheidung:** Landing → Pricing → Quality → Blog → Tools → Daily Brief

## D-012: Versionen archivieren + Changelog
**Datum:** 2026-02-12
**Entscheidung:** Jede Version in archive/vN/ + CHANGELOG.md mit Learnings
**Florians Input:** "Speichere auch Versionen, daraus lernst du."

## D-013: Do/Don'ts pro Seite
**Datum:** 2026-02-12
**Entscheidung:** pages/[name].md mit Spec + Do/Don'ts + Learnings
**Florians Input:** "Dann vergisst du auch keine custom Symbole."

## D-014: /quality → "How We Build"
**Datum:** 2026-02-12
**Entscheidung:** Eigene Seite für Agent-Architektur (inspiriert von Linear /quality)

## D-015: Website = Produkt
**Datum:** 2026-02-12
**Entscheidung:** Website ist state-of-the-art, Build = Content
**Florians Input:** "Das Produkt ist die Website."

## D-016: SEO-Architektur → Pillar + Cluster
**Datum:** 2026-02-12
**Entscheidung:** Topic Clusters mit Pillar Pages

## D-017: Login + Sign up in Nav
**Datum:** 2026-02-12
**Entscheidung:** Log in (text) + Sign up (Indigo button) rechts in Nav

## D-018: Build = Blog-Artikel
**Datum:** 2026-02-12
**Entscheidung:** Jeder Build-Prozess wird als Content dokumentiert
**Florians Input:** "Alles was wir machen = Blog Post mit Quellen."

## D-019: Tagline → "Human × AI = Compounded Intelligence"
**Datum:** 2026-02-12
**Entscheidung:** "Compounded Intelligence" als Philosophie/Tagline
**Alternativen:** LIMITLESS (zu bold), HAI (belegt: Stanford, HackerOne)
**Florians Input:** "Compounded Intelligence for now."

## D-020: Stats → 3 ungerade KPIs
**Datum:** 2026-02-12
**Entscheidung:** 90 sec / 243 / 3 Rounds. Keine Dopplung.
**Florians Input:** "3 oder 5 sind besser als gerade Zahlen."

## D-021: Logo-Usage → Text nur, keine Logos
**Datum:** 2026-02-12
**Entscheidung:** "Powered by OpenAI · Anthropic · Google Cloud" als Text

## D-022: Alle Outputs visuell (HTML/PDF)
**Datum:** 2026-02-12
**Entscheidung:** Florian bewertet NUR visuell
**Florians Input:** "Ich brauche immer HTML oder PDF."

## D-023: Pricing Subtitle → Value Anchor
**Datum:** 2026-02-12
**Entscheidung:** "Strategic intelligence reports that take weeks and cost thousands. Now starting at zero."

## D-024: "The tool IS the demo"
**Datum:** 2026-02-12
**Entscheidung:** Phase 1: Fiktive Demo-Reports. Phase 2: Live Input → echter Report.
**Florians Input:** "Der Trend ist the tool is the demo."

## D-025: Blog → Executive Mode + Internal Links
**Datum:** 2026-02-12
**Entscheidung:** Toggle "Full Article" / "Executive Summary" + Hyperlinks zu Tools/anderen Artikeln für SEO
**Florians Input:** "Weniger ist mehr. Executive für weniger Text. Hyperlinks für SEO."

## D-026: Entscheidungen dokumentieren
**Datum:** 2026-02-12
**Entscheidung:** Alle Entscheidungen in DECISIONS.md mit Datum, Alternativen, Begründung
**Florians Input:** "Dokumentiere alle unsere Entscheidungen in unsere Architektur."

---

*Nächste Entscheidung: D-027*
*Dieses Dokument wächst mit jedem Build. Nie löschen, nur ergänzen.*

D-032 | 2026-02-12 | Framework → Astro | Before launch, migrate static HTML to Astro. Shared Nav/Footer/Cards, one CSS. Florian approved.
D-033 | 2026-02-12 | Logo → ●Ainary | Gold dot before text. On all pages.
D-034 | 2026-02-12 | Section Anatomy Standard | Every section: Title + Subtitle + Content + Cross-link. Documented in DESIGN-SYSTEM.md.
D-035 | 2026-02-12 | Stats → < 3 min | Consistent with 'minutes' messaging.
