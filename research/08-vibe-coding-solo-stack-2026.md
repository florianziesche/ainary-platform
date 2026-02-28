# Research Report #8: Vibe Coding & One-Person SaaS — Der optimale Stack 2026
*Mia ♔ | 2026-02-23 | [INTERN]*

---

## THE ANSWER
Der optimale Stack für Florian (technisch, solo, speed-first) ist: **Claude Code für Backend/Logic + Lovable für UI-Prototypen + Cursor für Refinement + Vercel für Deploy**. Das ist nahezu identisch mit dem, was wir BEREITS NUTZEN. Kein Stack-Wechsel nötig. Der größte Hebel ist nicht das Tool, sondern der **Workflow**: Prototype fast (Lovable) → Refine (Cursor/Claude) → Deploy (Vercel) → Ship.

## CONFIDENCE: Likely (80%)

---

## KEY EVIDENCE

### Die Vibe-Coding-Landschaft Feb 2026
| Tool | Stärke | Schwäche | Für wen |
|------|--------|----------|---------|
| **Cursor** | Multi-file editing, Rules files, Codebase-Kontext | Lernkurve | Developer mit bestehendem Repo ✅ |
| **Claude Code** | Raw power, Benchmark leader, Terminal-native | Kein GUI-Editor | Power user ✅ |
| **Lovable** | Bestes UI-Polish, schnellster Prototyp | Skaliert schlecht für große Codebases | Non-technical Validation |
| **Bolt.new** | Framework-Flexibilität | Weniger polished als Lovable | Full-Stack Prototypen |
| **Replit Agent** | Most autonomous, 30+ Integrations | Vendor Lock-in | Anfänger |
| **Windsurf** | Cascade Agent, bester Kontext für große Codebases | Neue Company | Large codebases |
| **v0 (Vercel)** | UI Components, React | Nur Frontend | Designer |

### Unser aktueller Stack vs Optimal
| Bereich | Aktuell | Optimal | Änderung? |
|---------|---------|---------|-----------|
| Coding | Claude Code (OpenClaw) | Claude Code + Cursor für Refinement | 🟡 Cursor als Ergänzung |
| Prototyping | Manuell in HTML | Lovable → Export → Cursor | ✅ **Lovable testen** |
| Deploy | Vercel | Vercel | ✅ Perfekt |
| Backend | Static HTML + Gist API | Static HTML + Gist API | ✅ Reicht für Phase 1 |
| DB | Keine (JSON in Gist) | Supabase wenn nötig | 🟡 Erst bei >10 Kunden |
| Auth | Custom JS Hash | Custom JS Hash | ✅ Reicht für Phase 1 |
| Analytics | Custom API (Gist) | Custom API | ✅ Funktioniert |

### Der ideale Workflow für Ainary
```
1. IDEA → Claude Code (Mia) → Konzept + Architektur
2. UI → Lovable → Schneller Prototyp (wenn neues UI nötig)
3. CODE → Claude Code + Cursor → Implementation
4. DEPLOY → Vercel (git push) → Live in 14s
5. TEST → Browser → Screenshot → Done
```

### Empfehlung
**Kein großer Stack-Wechsel.** Einzige Ergänzung: **Lovable für neue UI-Prototypen** (nicht für gotham.html — das ist zu komplex). Für neue Produkte (z.B. Koalitionsnavigator-UI) wäre Lovable der schnellste Weg zu einem klickbaren Prototyp.

---

## SOURCES
```
[B1] Best Vibe Coding Tools 2026, vibecoding.app → vibecoding.app/blog/...
[B1] Best AI App Builder 2026, Mocha → getmocha.com/blog/...
[B1] Choosing AI Prototyping Stack, Medium, Jan 2026 → annaarteeva.medium.com/...
[B2] Top 10 Vibe-Coding Platforms, Noca → noca.ai/top-10-...
[B2] Vibe Coding Tools Guide, Replit → replit.com/discover/...
```

---

*Report 8/10 complete. ♔*
