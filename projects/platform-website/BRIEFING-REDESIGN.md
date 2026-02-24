# Briefing Redesign — Bamberg First, Then Template

## Problem
Current briefing is a data dump. Tiny fonts, cramped layout, no emotional arc, no "wow" moment. 
A candidate opens it and thinks "okay, Daten" not "holy shit, die wissen mehr über meine Wahl als ich."

## Design Principles
1. **Less is more** — 5 sections, nicht 15. Jede Sektion verdient ihren Platz.
2. **Jeder Satz beantwortet "und was bedeutet das?"** — keine nackte Zahl.
3. **Neutral = Glaubwürdig** — Analystensprache, keine Kampagnensprache.
4. **Premium fühlt sich an wie leer** — Whitespace, große Schrift, Luft zum Atmen.
5. **Progressive Disclosure** — Übersicht → Klick → Detail. Nicht alles auf einmal.

## Informationsarchitektur (Kandidat öffnet Link)

### 1. HERO: Lagebeurteilung (above the fold, EINZIGER Inhalt der sofort sichtbar ist)
- Stadtname + Wahltermin + Countdown
- 1 Absatz (3 Sätze max): Lage, Dynamik, Schlüsselfaktor
- 3 KPIs: Stichwahl-Wahrscheinlichkeit | Führender Kandidat | Medien-Dynamik
- Evidenz-Badge: "Basierend auf 42 Quellen, Stand 24.02.2026"
- **KEIN Scrollen nötig um das Wichtigste zu verstehen**

### 2. ENTWICKLUNGEN (was hat sich verändert)
- Max 3 Items (nicht 5)
- Jedes Item: **Was** (1 Zeile) → **Warum relevant** (1 Zeile) → **Quelle** (Link)
- Farbcode: Rot = dringend, Gelb = beobachten, Grau = Hintergrund

### 3. KANDIDATEN-MATRIX (wer steht wo)
- Horizontale Karten, alle gleich groß (Neutralität!)
- Pro Kandidat: Foto-Platzhalter | Name+Partei | 1 Satz Positionierung | Prognose-Range | Stärke | Schwäche
- **Sortierung alphabetisch** (nicht nach Stärke — neutral)
- Klick → Dossier-Tab mit vollem Profil

### 4. THEMEN-KOMPASS (was die Wähler bewegt)
- Radiale oder horizontale Visualisierung
- 5 Themen, sortiert nach Relevanz
- Pro Thema: Name | Relevanz-Balken | 1-Satz Bedeutung | Wer profitiert/verliert
- **Keine Positionierungsempfehlung** — nur Analyse wer wo steht

### 5. SZENARIEN (wie kann es ausgehen)
- 3 Szenarien als Karten nebeneinander
- Pro Szenario: Name | Wahrscheinlichkeit (groß) | 2 Sätze | Bedingungen (collapsed)
- Visuell: Wahrscheinlichkeit als Halbkreis/Gauge

### KEIN Deep Dive auf Briefing-Tab
- Alles was jetzt "Detailanalyse" ist → verschwindet oder geht in andere Tabs
- Briefing = Executive Summary. Fertig. 5 Sektionen, 1 Scroll.

## Visuelle Regeln
- Mindestens 9pt Fließtext (aktuell 6-7pt = unlesbar)
- Max 80ch Zeilenbreite
- 24px Abstand zwischen Sektionen
- Sidebar: BLEIBT, aber wird vereinfacht (nur Kandidaten + Themen, keine Hypothesen/Events)
- Intel Feed rechts: BLEIBT als Quellen-Nachweis
- Fonts: Behalten (Inter + JetBrains Mono)

## Content-Regeln
- Jede Zahl hat Kontext ("55 von 100" nicht "55")
- Jeder Score hat Erklärung ("Risiko-Score: Kombination aus Skandal-Exposition, Medienpräsenz und Wähler-Volatilität")
- Kein Fachbegriff ohne Erklärung beim ersten Auftreten
- Kandidaten-Beschreibungen: Gleiche Struktur für alle (Neutralität)
- Quellen immer sichtbar — Transparenz = Vertrauen

## Was ich NICHT mehr zeige (Kill List)
- KPI-Leiste (5 Dossiers, 30 Quellen) → in Footer als Fußnote
- E/I/J/A Legend → zu komplex, verwirrt
- Risk-Ranking Balken → in Kandidaten-Matrix integriert  
- Momentum Index → in Kandidaten-Matrix als Sub-Info
- Social Media Follower-Bars → in Dossier-Tab
- Google Trends Bars → in Dossier-Tab
- YouTube Intelligence → in Dossier-Tab
- Themen-Radar duplicate → einmal reicht
- "Jetzt relevant" Cards → ersetzt durch Entwicklungen

## Template vs. Daten
Alles in normalizeCity() — Template liest nur normalisierte Felder.
Bamberg-spezifische Texte: NEIN. Alles aus JSON generiert.
Wenn die Daten gut sind, ist das Briefing gut.

## Zeitplan
1. CSS-Variablen anpassen (Schriftgrößen, Abstände) — 10min
2. renderBriefing() komplett neu schreiben — 60min
3. Sidebar vereinfachen — 20min
4. Bamberg-Daten perfektionieren (Lücken füllen) — 30min
5. Screenshot + Review mit Florian — 10min
6. Deploy nur nach Freigabe
