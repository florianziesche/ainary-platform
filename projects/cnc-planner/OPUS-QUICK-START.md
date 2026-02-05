# Opus 4.6 Quick Start — CNC Planner Build

**So startest du das Projekt mit Claude Opus 4.6.**

---

## SCHRITT 1: Öffne Claude.ai

1. Gehe zu https://claude.ai
2. Wähle **Opus 4.6** Model (oben rechts)
3. Starte neuen Chat

---

## SCHRITT 2: System-Prompt laden

**Copy-Paste in Chat:**

```
Lies diese Datei als System Context:
```

**Dann upload:** `OPUS-SYSTEM-PROMPT.md`

**Claude liest es, sagt:** "Verstanden, ich bin bereit."

---

## SCHRITT 3: Project Brief geben

**Copy-Paste:**

```
Lies jetzt die vollständige Projekt-Spezifikation:
```

**Dann upload:** `OPUS-PROJECT-BRIEF.md`

**Claude liest 20KB Spec, versteht:**
- Was gebaut werden soll
- Tech Stack
- Database Schema
- 3-Wochen-Plan
- Alle Requirements

---

## SCHRITT 4: Referenz-Code geben

**Copy-Paste:**

```
Hier ist der aktuelle Prototype (v16), dessen Logic du portieren musst:
```

**Dann upload:** `demo-v16-complete.html`

**Claude analysiert:**
- `calculate()` Funktion
- Formeln
- UI Struktur
- NC-Code Templates

---

## SCHRITT 5: Fragen beantworten

**Claude wird fragen:**
- "Wo soll das GitHub Repo erstellt werden?"
- "Welche Supabase Region? (EU für GDPR)"
- "Soll ich Test-Stripe-Keys nutzen oder Production?"
- "Welche Domain? (cnc-planner.com?)"

**Antworte:**
```
- GitHub Repo: Erstelle unter deinem Account (ich gebe dir später Access)
- Supabase Region: EU (Frankfurt)
- Stripe: Test Keys zuerst (ich gebe dir die Keys)
- Domain: cnc-planner.com (später)
```

---

## SCHRITT 6: Start Development

**Sag zu Claude:**

```
Starte mit Phase 1, Day 1: Setup.

Erstelle:
1. Supabase Project
2. React + TypeScript + Vite Projekt
3. TailwindCSS + shadcn/ui
4. GitHub Repo
5. Vercel Deploy

Zeige mir jeden Schritt bevor du weitergehst.
```

**Claude wird:**
- Schritt für Schritt vorgehen
- Dir Code zeigen
- Fragen wenn unsicher
- Commiten nach jedem Feature

---

## SCHRITT 7: Daily Check-ins

**Jeden Abend fragt Claude:**

```
## Day 1 Progress

**Completed:**
- [x] Supabase project created
- [x] React app initialized
- [x] Deployed to Vercel (empty app)

**Tomorrow:**
- Build Login page
- Integrate Supabase Auth

**Blockers:**
- None

**Questions:**
- Soll ich deutsche oder englische UI-Texte nutzen?
```

**Du antwortest, Claude macht weiter.**

---

## SCHRITT 8: Testing

**Regelmäßig sagen:**

```
Zeige mir einen Live-Link zum aktuellen Stand.
Ich teste Feature X.
```

**Claude gibt dir Vercel URL:**
```
https://cnc-planner-xyz.vercel.app
```

**Du testest, gibst Feedback:**
```
- Login funktioniert ✅
- Aber: Nach Signup fehlt Redirect zur Dashboard
- Fix: Redirect nach erfolgreicher Signup
```

**Claude fixt, committed, deployed.**

---

## SCHRITT 9: Milestones

**Nach jeder Woche:**

**Week 1 Ende:**
```
Zeige mir:
- Live Demo (Vercel URL)
- GitHub Repo
- Was funktioniert, was noch fehlt
```

**Week 2 Ende:**
```
Demo: Upload File → Calculate → Save to Archive
```

**Week 3 Ende:**
```
Full Flow: Signup → Onboard → Subscribe → Calculate → Download PDF
```

---

## SCHRITT 10: Launch

**Wenn alles done:**

```
Production Deployment Checklist:
- [ ] All tests pass
- [ ] Stripe in production mode
- [ ] Supabase in production tier
- [ ] Domain configured (cnc-planner.com)
- [ ] Monitoring setup (Sentry)
- [ ] First customer can signup
```

**Claude macht Checklist, du gehst durch, dann: LAUNCH.** 🚀

---

## BACKUP PLAN (Falls Claude stuck)

**Wenn Claude nicht weiterkommt:**

### **Option A: Sub-Task**
```
Das ist zu komplex. Teile es in 3 kleinere Tasks:
1. [Specific sub-task]
2. [Specific sub-task]
3. [Specific sub-task]

Starte mit 1.
```

### **Option B: Show Example**
```
Hier ist ein Beispiel wie es funktionieren sollte:
[Paste code example or link]

Implementiere das ähnlich für unser Projekt.
```

### **Option C: Ask Mia**
```
@Mia: Claude ist stuck bei [Feature X]. 
Was ist der beste Approach?
```

**Ich antworte mit:**
- Alternative Lösung
- Simplification
- Library-Empfehlung

---

## TIPPS

### **Für schnelle Iteration:**
- Lass Claude kleine Features bauen (1-2 Stunden)
- Teste sofort
- Gib Feedback
- Nächstes Feature

### **Für komplexe Features:**
- Bitte um "Design Doc" zuerst
- Review Architecture
- Dann: "Build it"

### **Für Debugging:**
- Paste Error Messages
- Claude liest Stack Trace
- Schlägt Fix vor

### **Für Performance:**
- "Run Lighthouse on [URL]"
- Claude analysiert Score
- Optimiert

---

## ERWARTETE TIMELINE

| Week | Milestone | What Works |
|------|-----------|------------|
| 1 | Foundation | Auth, Settings, Deploy |
| 2 | Core Features | Upload, Calculate, Archive |
| 3 | Payment + Polish | Stripe, Onboarding, PDF |

**Total:** 21 Tage = Production-Ready SaaS

---

## COST ESTIMATE

**Claude Opus 4.6 Usage:**
- ~200 prompts à 5K tokens input + 2K output = ~1.4M tokens
- Cost: ~$30-50 für gesamtes Projekt (Anthropic Pricing)

**Infrastructure (während Development):**
- Supabase: Free Tier (ausreichend)
- Vercel: Free Tier (ausreichend)
- Stripe: Test Mode (kostenlos)

**Total Budget:** ~$50 für 3 Wochen Development

---

## SUCCESS METRICS

**Du weißt es ist "done" wenn:**
- ✅ Florian kann Demo einem echten Kunden zeigen
- ✅ Kunde kann signup → pay → calculate
- ✅ Keine critical bugs
- ✅ Tests pass
- ✅ Deployed auf Production

**Dann:** First Customer Onboarding → Revenue → Scale

---

## NEXT STEP

**Jetzt sofort:**
1. Open https://claude.ai
2. Upload `OPUS-SYSTEM-PROMPT.md`
3. Upload `OPUS-PROJECT-BRIEF.md`
4. Upload `demo-v16-complete.html`
5. Say: "Starte mit Phase 1, Day 1"

**Claude antwortet:**
> "Verstanden. Ich erstelle jetzt das Supabase Project und React App. Schritt 1: ..."

**Und los geht's.** 🚀

---

## FRAGEN?

**An mich (Mia):**
- "Was wenn Claude Feature X nicht kann?"
- "Welche Library für Y?"
- "Ist dieser Approach gut?"

**An Claude:**
- Alle Tech-Fragen
- Code-Reviews
- Bug-Fixes
- Architecture-Entscheidungen

**Zusammen:** Wir bauen das in 3 Wochen. **Let's go.** ♔
