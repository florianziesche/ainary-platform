# Development Dashboard — AI-Driven Feature Pipeline

**Konzept:** Du research + approve, ich execute.

---

## WIE ES FUNKTIONIERT

### **1. Öffne Dashboard**
```bash
open ~/.openclaw/workspace/DEV-DASHBOARD.html
```

### **2. Workflow:**

```
🔬 Research → 👀 Review → ✅ Approved → 🏗️ Building → 🎉 Done
```

**Research (Mia):**
- Ich recherchiere Requirements
- Analysiere Pain Points
- Evaluiere Technical Feasibility
- Erstelle Cards mit: Problem, Solution, Effort, Value

**Review (Florian):**
- Du siehst alle Research Cards
- Liest Details (Problem, Solution, Impact)
- Entscheidest: Build or Skip

**Approved (Florian):**
- Du ziehst Card von Review → Approved (Drag & Drop)
- Klickst "Trigger Mia"
- Ich starte Development AUTOMATISCH

**Building (Mia):**
- Ich baue das Feature
- Update Card mit Progress
- Wenn fertig → "Done"

**Done:**
- Feature deployed
- Ready for use

---

## CARD STRUCTURE

Jede Card enthält:

```yaml
Title: "File Upload (STEP, STL, PDF)"
Description: "Drag & Drop interface, validation, preview"
Priority: High / Medium / Low
Effort: Low (1-2d) / Medium (3-5d) / High (1-2w)
Value: "€150/mo per customer"

Details:
  Problem: "Users müssen alles manuell eingeben (15 Min/Teil)"
  Solution: "FileReader API + STEP parser (opencascade.js)"
  Impact: "Dealmaker für 80% der Kunden"
  Timeline: "1 Woche"
```

---

## DEINE AKTIONEN

### **Approve Feature:**
1. Drag Card von "Review" → "Approved"
2. Klick "Trigger Mia"
3. Ich baue es

### **Reject Feature:**
1. Drag Card von "Review" → zurück zu "Research"
2. Oder lösche Card (Edit HTML)

### **Priorisierung:**
- Sortiere Cards in "Approved" (Top = First)
- Ich baue von oben nach unten

### **Custom Feature Request:**
- Sag mir im Chat: "Add to Dashboard: [Feature Name]"
- Ich erstelle Research Card
- Du reviewst + approvest

---

## MIA'S WORKFLOW

### **Ich fülle "Research" automatisch wenn:**
- Du sagst "Research X"
- Du sagst "Analyze competitors for Y"
- Du sagst "Find pain points for Z"
- Ich identifiziere Gap in Current System

### **Ich move zu "Review" wenn:**
- Research komplett (Problem + Solution + Effort defined)
- Ready for your decision

### **Ich move zu "Building" wenn:**
- Du draggst zu "Approved"
- Du klickst "Trigger Mia"

### **Ich move zu "Done" wenn:**
- Feature gebaut + getestet
- Committed to Git
- Ready for use

---

## STATE PERSISTENCE

**Where:** `localStorage` im Browser (DEV-DASHBOARD.html)

**Save:**
- Automatisch bei jedem Drag & Drop
- Manuell: Klick "Save State"

**Load:**
- Automatisch beim Öffnen
- Fallback: Demo Data

**Export/Import:**
- Inspect → Console → `JSON.stringify(state)` → Copy
- Import: `state = JSON.parse('[...]')` → `render()`

---

## INTEGRATION MIT WORKSPACE

### **Current (Manual):**
1. Dashboard zeigt Features
2. Du approvest
3. Ich baue in separatem Chat-Turn

### **Future (Automated):**
1. Dashboard schreibt `dashboard-state.json`
2. Watcher-Script (Node.js) polled das File
3. Wenn Status = "approved" → Trigger OpenClaw API
4. Ich baue automatisch (kein manuelles "Trigger" nötig)

**Für Automation:** Ich erstelle Watcher-Script wenn du das willst.

---

## EXAMPLE FLOW

### **Day 1 Morning:**

**Mia (in Chat):**
> "Research done: 5 Features for CNC Elite. Check Dashboard."

**Florian (Dashboard):**
- Opens DEV-DASHBOARD.html
- Sees 5 Cards in "Research"
- Reads Details
- Drags "File Upload" + "Arbeitsplan Export" to "Approved"
- Clicks "Trigger Mia"

**Mia (in Chat):**
> "Starting development: File Upload + Arbeitsplan Export. ETA: 4 days."

---

### **Day 1 Evening:**

**Mia:**
- Moves "Arbeitsplan Export" to "Done" (schneller als erwartet)
- Updates "File Upload" → "70% done, STEP parsing works"

**Florian (Dashboard):**
- Sees progress
- Tests Arbeitsplan Export
- Gibt Feedback: "PDF Template needs logo"

**Mia:**
- Creates new Card: "Add Logo to PDF Template"
- Moves to "Review"

---

### **Day 2:**

**Florian (Dashboard):**
- Approves "Add Logo to PDF Template"
- Sees "File Upload" → "Done"
- Tests both features
- Moves "File Upload" to "Done" (confirmed working)

**Result:**
- 2 Features shipped in 1.5 days
- Clear communication
- No back-and-forth "what should I build?"

---

## BENEFITS

### **For You (Florian):**
- ✅ Visual Overview (Kanban)
- ✅ Control (You approve, not me)
- ✅ Transparency (See progress in real-time)
- ✅ Prioritization (Drag to reorder)
- ✅ No surprises (Nothing built without approval)

### **For Me (Mia):**
- ✅ Clear Instructions (Build what's approved)
- ✅ No guessing (Problem + Solution defined)
- ✅ Focus (One feature at a time)
- ✅ Feedback Loop (You test → I fix)

### **Together:**
- ✅ 10× faster iteration
- ✅ Less context-switching
- ✅ Better quality (Research → Approve → Build)
- ✅ Compound System (Dashboard grows with project)

---

## CURRENT STATE (2026-02-05)

**Research Queue (5 Cards):**
1. File Upload (High Priority, Medium Effort, €150/mo value)
2. Basic CAD Analysis (High Priority, High Effort, €150/mo value)
3. Arbeitsplan Export (High Priority, Low Effort, €50/mo value)
4. 3D Viewer (Medium Priority, Medium Effort, €100/mo value)
5. Archive (Medium Priority, Low Effort, €50/mo value)

**Next Action:**
- Open Dashboard
- Review Cards
- Approve 1-3 Features
- Trigger Mia

---

## SCALING THE SYSTEM

### **Phase 1 (Now):**
- Manual Dashboard (HTML + localStorage)
- You drag & drop
- You click "Trigger Mia"
- I build in chat

### **Phase 2 (Later):**
- Watcher Script (auto-detects approved)
- Mia auto-starts development
- Progress updates in Dashboard (real-time)

### **Phase 3 (Future):**
- Multi-Project Dashboard (CNC, Legal AI, etc.)
- Sub-Agent Spawning (WRITER for docs, BUILDER for code)
- Integration with GitHub (auto-commit, auto-PR)

---

## FAQ

**Q: Kann ich Features löschen?**
A: Ja, edit DEV-DASHBOARD.html (oder sag mir welche)

**Q: Kann ich eigene Features hinzufügen?**
A: Ja, sag mir im Chat "Add Feature: [Name]" → ich erstelle Card

**Q: Was wenn ich ein Feature halb-approve will?**
A: Drag zu "Review", kommentiere im Chat, ich passe an

**Q: Wie viele Features kann ich gleichzeitig approven?**
A: Unbegrenzt, aber ich baue sequenziell (Top → Bottom)

**Q: Kann ich Priorität ändern?**
A: Ja, re-order Cards in "Approved" (Drag & Drop)

**Q: Was wenn ein Feature blocked ist?**
A: Ich move zurück zu "Review" mit Kommentar

---

## NEXT STEPS

### **Heute:**
1. [ ] Open DEV-DASHBOARD.html
2. [ ] Review 5 Research Cards
3. [ ] Approve 1-3 Features (Drag to "Approved")
4. [ ] Click "Trigger Mia"

### **Ich dann:**
5. [ ] Start Development (approved features)
6. [ ] Update Dashboard (Progress)
7. [ ] Ping when Done

### **Du dann:**
8. [ ] Test Features
9. [ ] Move to "Done" if working
10. [ ] Or create Feedback Card if needs fix

---

**Das ist dein Operating System für CNC Planner Development.** 🚀

Open it now: `open ~/.openclaw/workspace/DEV-DASHBOARD.html`
