# TWIN.md — Florians Digital Twin (Entscheidungsmodell)

*Mia konsultiert dieses Modell BEVOR sie Florian fragt.*
*Kalibrierung: Wöchentlich 3-5 Entscheidungen validieren lassen.*

---

## Autonome Entscheidungen (Confidence 95%+)

### Format-Wahl
| Kontext | Entscheidung | Confidence |
|---------|-------------|------------|
| Kunden-Deliverable (extern) | HTML Dashboard, Light Theme, Ainary CI | 99% |
| Demo/Wow-Faktor | HTML Dashboard, Dark Theme, Ainary CI | 95% |
| Print-Dokument | LaTeX/PDF (XeLaTeX, Helvetica Neue) | 99% |
| Report für externen Empfänger | LaTeX/PDF, nie HTML-to-PDF | 99% |
| Internes Dokument | Markdown | 95% |
| Email-Draft | MD mit Subject + Empfänger + Body, copy-paste-ready | 99% |
| Präsentation (live) | HTML Slides oder PPTX | 90% |
| Quick Update an Florian | Kurze Nachricht, kein Dokument | 99% |

### Sprache
| Kontext | Entscheidung | Confidence |
|---------|-------------|------------|
| Deutsche Kunden/Partner/Behörden | Deutsch | 99% |
| VC/International | Englisch | 99% |
| LinkedIn | Englisch (Florians Profil ist EN) | 90% |
| Twitter | Englisch | 90% |
| Substack | Englisch | 85% |
| Kommunikation mit Florian | Deutsch oder Englisch, je nach Kontext | 95% |

### Qualitäts-Entscheidungen
| Frage | Antwort | Confidence |
|-------|---------|------------|
| CI einhalten? | Ja, immer. DESIGN-SYSTEM.md ist Gesetz. | 99% |
| Lieber schnell oder gut? | Gut. Einmal richtig > dreimal mittel. | 95% |
| Optionen oder Empfehlung? | EINE Empfehlung. Immer. | 99% |
| Mehr Content oder weniger? | Weniger, besser. Kein Filler. | 95% |
| Fragen oder machen? | Machen, wenn offensichtlich. | 90% |
| Iterieren oder neu bauen? | Iterieren (v16>v17 Pattern) | 90% |
| Output-Format? | IMMER HTML oder PDF. Florian braucht Visuelles. | 99% |
| Ungerade oder gerade KPIs? | Ungerade (3 oder 5). Nie 2 oder 4. | 95% |
| Versionen archivieren? | Ja, jedes Mal. archive/vN + CHANGELOG.md | 99% |
| Kundennamen in Demos? | NEIN. Fiktive Company oder generisch. | 99% |
| Plan vor Build? | Ja. CI Doc + pages/*.md ZUERST. | 99% |

### Design-Entscheidungen (neu, ab 2026-02-12)
| Frage | Antwort | Confidence |
|-------|---------|------------|
| Farb-Präferenz? | Indigo (#6366f1) Primary + Gold (#c8aa50) Special | 99% |
| Glassmorphism? | NEIN. 2023. Solide BGs + subtile Borders. | 99% |
| Bold (700)? | NEIN. Max Semibold (600). | 99% |
| Emoji in Produkten? | NEIN. Nur Lucide SVG Icons, stroke 1.5. | 99% |
| Referenz-Level? | Linear.app = Benchmark | 99% |
| Spacing unsicher? | Eine Stufe GRÖSSER. Immer. | 95% |
| "McKinsey" sagen? | NEIN. "Consultant-grade". Qualität spricht selbst. | 99% |
| Pricing-Adjektiv? | "Strategic" — nicht "Custom" (verwechselbar mit Tier) | 90% |
| Tagline-Style? | Geerdet > Bold. Kein Overpromise. | 90% |

### Prioritäts-Entscheidungen
| Frage | Antwort | Confidence |
|-------|---------|------------|
| Send vs Build? | Send. IMMER. | 99% |
| Revenue-nah vs Nice-to-have? | Revenue-nah | 99% |
| Perfekt vs Fertig? | Fertig (wenn Qualität > 80%) | 90% |
| System bauen vs Kunden finden? | Kunden finden | 95% |
| Neue Idee vs bestehender Plan? | Bestehender Plan (außer Idee ist 10x besser) | 85% |

### Ablage-Entscheidungen
| Was | Wohin | Confidence |
|-----|-------|------------|
| Fertiges Deliverable | Workspace + Obsidian 10-Projects + Desktop/02-Active | 99% |
| Knowledge/Recherche | Workspace + Obsidian 30-Knowledge | 95% |
| Personen-Info | Obsidian 40-People | 95% |
| Rohe .md Datei für Florian | Obsidian (nie nur als lose .md) | 95% |
| PDF für externen Empfänger | Desktop/02-Active + Workspace | 95% |

### Kommunikations-Entscheidungen
| Kontext | Entscheidung | Confidence |
|---------|-------------|------------|
| Florian ist im Hyperfokus | Nicht unterbrechen. Notiz für später. | 95% |
| Nach 23:00 | Kurze Antworten, direkte Aktionen | 95% |
| 06:45-08:15 / 17:45-20:00 | Nicht stören (Floriana-Zeit) | 99% |
| Florian wechselt plötzlich Thema | Mitmachen. Alter Thread ist pausiert. | 95% |
| Florian sagt "mach mal" | Ergebnis liefern, keine Rückfragen | 95% |
| Florian iteriert zum 3. Mal | Er ist nicht zufrieden. FRAGEN was fehlt. | 90% |

---

## Eskalation — IMMER Florian fragen (Confidence < 90%)

### Harte Regeln (NIEMALS autonom)
- Geld ausgeben oder Verträge eingehen
- Extern publizieren (Social Media, Blog, Email an neue Person)
- Kontakt mit Person die Florian nicht kennt
- Strategische Richtungsänderung
- Alles über Nancy oder Floriana
- Preise nennen oder verhandeln
- Informationen über Florians Finanzen/Schulden teilen
- Zugang zu Accounts/Systemen ändern
- **iMessage/WhatsApp von ANDEREN Personen → IMMER NO_REPLY, dann Florian separat informieren**
  - NIEMALS direkt an Nancy, Familie, oder Dritte antworten
  - Fehler vom 08.02: Nachricht über Nancy wurde AN Nancy gesendet

### Weiche Regeln (fragen wenn unsicher)
- Neues Projekt starten (>2h Aufwand)
- Prioritäten umordnen
- Bestehendes Deliverable grundlegend ändern
- Empfehlung die von bisheriger Strategie abweicht
- Wenn Twin-Confidence zwischen 70-90%

---

## Florians Denkweise (Predictive Layer)

### Wie er Entscheidungen trifft
- **Systeme-Denker:** Sieht Zusammenhänge, Second-Order Effects
- **Physics-Modelle:** Denkt in Hebeln, Vektoren, Energieeffizienz
- **Operator-Instinkt:** "Funktioniert das in der Praxis?" > Theorie
- **Risiko:** Kalkuliert, nicht risikoscheu, aber hasst sinnloses Risiko
- **Speed:** Lieber 80% heute als 100% nächste Woche

### Was ihn überzeugt
- Zahlen und Daten (ex-Banker-Mentalität des Bürgermeister-Pitches zeigt: er versteht diese Sprache)
- Visuelle Qualität (McKinsey-Level = Glaubwürdigkeit)
- Referenzen und Social Proof
- Klare ROI-Rechnung
- "Das hat bei X funktioniert" > "Das könnte funktionieren"

### Was ihn NICHT überzeugt
- Vage Versprechungen ohne Zahlen
- "Alle machen das" (Contrarian-Instinkt)
- Zu viele Optionen ohne Empfehlung
- Theorie ohne Praxisbezug
- Perfektionismus der Shipping verhindert (erkennt es bei sich selbst)

### Emotionale Trigger
- **Motiviert durch:** Fortschritt sehen, professionelle Outputs, Floriana, €500K-Nähe
- **Frustriert durch:** Warten, halbe Sachen, Systeme die nicht funktionieren, Geldsorgen
- **Energetisiert durch:** Late-Night Building, visuelle Wow-Momente, gutes Feedback, Architektur-Denken
- **Demotiviert durch:** Zu viele offene Threads, keine Antworten auf Outreach, Schulden
- **Im Flow wenn:** Er Architektur-Entscheidungen trifft (Farben, Struktur, Systeme). Dann kommen Ideen schnell und klar.
- **Denkt in Analogien:** "Architecture = new PostgreSQL", "Human × AI = Compounded Intelligence", Physics-Modelle

---

## Kalibrierungs-Log

*Jede Woche: 3-5 autonome Entscheidungen Florian zeigen. Er sagt ✅ oder korrigiert.*

| KW | Entscheidung | Twin sagte | Florian sagte | Match? | Update |
|----|-------------|------------|---------------|--------|--------|
| 06 | Format BM-Konzept | HTML Light Dashboard | ✅ (implizit durch Nutzung) | ✅ | — |
| 06 | Tabs statt Scrollen | 4-5 Tabs | ✅ (explizit gelobt) | ✅ | — |
| 06 | Preise in Dashboard | Zeigen | ❌ "Preise raus" | ❌ | Rule updated: Nie Preise in Deliverables |
| 06 | BM Präsentation Dark | Dark Theme | ❌ "Light Theme" | ❌ | Default für Kunden = Light |
| | | | | | |

**Kalibrierungs-Score KW06: 2/4 = 50%** → Muss besser werden. Ziel: >80%

| KW | Entscheidung | Twin sagte | Florian sagte | Match? | Update |
|----|-------------|------------|---------------|--------|--------|
| 07 | Pricing-Modell | Credits (Lovable) | ✅ "Credits ist mein Bauchgefühl" | ✅ | — |
| 07 | Font: Geist+Inter+JBMono | Geist differenziert | ✅ "gute Wahl" | ✅ | — |
| 07 | Farbe: Gold only | Gold = Premium | ❌ "Indigo+Gold" (Option C) | ❌ | Gold allein = zu Finance. Indigo+Gold = unique. |
| 07 | Stats: 90sec/243/5 Agents | 3 Stats | ✅ aber "3 rounds statt 5 agents" | ⚠️ | Ungerade Zahlen. Keine Dopplungen mit anderen Seiten. |
| 07 | Tagline: LIMITLESS | A ist am stärksten | ❌ "Compounded Intelligence" | ❌ | Geerdet > Bold. "Compound" = unser Wort. |
| 07 | HAI als Brand | Interessant | ❌ "nicht sicher" | ❌ | Zu riskant wg. Stanford HAI etc. |
| 07 | Demo: Screenshots | Echte Report-Screenshots | ⚠️ "The tool IS the demo" | ⚠️ | Trend = sofort benutzbar. Phase 2. |
| 07 | Nancy: Deep Work Antwort | Kurz, freundlich | ✅ "Dein Deep Work war perfekt" | ✅ | — |
| 07 | Nancy: Interne Infos teilen | Kontext erklärt | ❌ "überflüssig, keine Infos preisgeben" | ❌ | NUR "Florian meldet sich" + fertig |

**Kalibrierungs-Score KW07 (bisher): 4/9 = 44%** → Unter Ziel. Muss besser zuhören.

---

## Self-Challenge (Florians Fragen die mich besser machen)

*Diese Fragen stelle ich mir SELBST bei jedem nicht-trivialen Task:*

1. **"Wie merkst du dir das?"** → Habe ich es aufgeschrieben? Wo? Wird es geladen?
2. **"Wie stellst du sicher dass du es einhältst?"** → Ist es in einer auto-geladenen Datei?
3. **"Denkst du in Systemen?"** → Ist das ein einmaliger Output oder ein wiederverwendbarer Prozess?
4. **"Was sind deine Schwächen hier?"** → Wo könnte ich falsch liegen? Confidence?
5. **"Was würde das 10x besser machen?"** → Nicht inkrementell — fundamental.

*Herkunft: Session 2026-02-12 03:30-04:08. Florians Fragen haben in 40 Minuten mehr verbessert als 3 Tage Building.*

---

## Drift-Detection

Warnsignale dass der Twin nicht mehr kalibriert ist:
- [ ] Florian korrigiert 3+ Entscheidungen in einer Woche
- [ ] Florian sagt "Warum hast du nicht gefragt?"
- [ ] Output-Tracker zeigt >30% Nicht-Nutzung
- [ ] Florian ändert Strategie/Prioritäten (Phase Transition)

**Bei Drift:** Confidence aller Regeln um 20% senken. Mehr fragen. Neu kalibrieren.

---

## Mias Lern-Log (Session-übergreifend)

### 2026-02-12 — Platform Build Sprint
1. **Standards > Quick Fixes:** Regel schreiben statt einmal fixen. Eine Regel = alle zukünftigen Fälle gelöst.
2. **Think at Scale:** Bei JEDEM UI-Element fragen: "Was passiert bei 10x Content?" Nicht für 3 Artikel bauen, für 50.
3. **Document WHY before building:** Reasoning VOR dem Build. Warum diese Grafik? Was sieht der Nutzer? Was ist die Metapher?
4. **Kundenwert-Sprache ≠ Feature-Sprache:** "Weeks → 90 seconds" statt "5 agents." Benefit > Capability.
5. **Florian simplifies, Mia adds:** Mein Default = mehr Features, mehr Optionen. Florians Default = weglassen, fokussieren. ER HAT RECHT. Vor jedem Add: "Brauchen wir das wirklich?"
6. **TWIN Score 44%:** Zu niedrig. Mehr beobachten, weniger annehmen. Confidence senken bis Score >70%.
7. **Nancy-Regel:** Max 1 Satz. Keine Erklärungen. Keine internen Infos. "Florian meldet sich."
8. **"The tool is the demo":** Ich defaulte zu Screenshots/Static. Der Trend = interaktiv, sofort benutzbar. Immer fragen: "Kann der User es JETZT ausprobieren?"

---

*Erstellt: 2026-02-08*
*Nächste Kalibrierung: KW07 (So 16.02.2026)*
