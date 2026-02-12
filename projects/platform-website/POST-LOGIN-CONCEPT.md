# Post-Login Concept — Durchdacht

*Bevor wir bauen: Was soll passieren wenn jemand sich einloggt?*

---

## Was die Besten machen

### Claude.ai
- Login → **sofort ein Input-Feld** ("How can I help you?")
- Sidebar links: Conversation History
- KEIN Dashboard, KEIN Onboarding-Wizard
- **Die EINE Aktion:** Nachricht schreiben → sofort Wert

### Linear.app
- Login → **Workspace mit Issues** (nicht leer!)
- Pre-populated mit Demo-Issues damit es nicht leer aussieht
- Sidebar: Projects, Issues, Views
- **Die EINE Aktion:** Issue erstellen oder bestehendes öffnen

### Lovable.dev
- Login → **ein Prompt-Feld** ("What do you want to build?")
- Darunter: Templates + Recent Projects
- **Die EINE Aktion:** Prompt eingeben → App wird gebaut

### Perplexity.ai
- Login → **Suchfeld** + Trending Topics
- Recent Searches darunter
- **Die EINE Aktion:** Frage stellen → sofort Antwort

---

## Das Pattern

Alle erfolgreichen Tools haben das gleiche Pattern:

```
Login → EINE prominente Aktion → Sofort Wert erleben
        ↑                          ↓
    Kein Onboarding          "Aha-Moment" in < 60 Sekunden
```

**Sekundär** (kleiner, am Rand): History, Settings, Account.

---

## Für Ainary: Die EINE Aktion

**"Welches Unternehmen willst du analysieren?"**

Das ist unser "How can I help you?" / "What do you want to build?"

### Der Flow:

```
1. User loggt sich ein
2. Sieht: Input-Feld + "Corporate" / "Startup" Toggle
3. Gibt ein: "BMW" 
4. Drückt Enter
5. Sieht: Loading-Animation (5 Agents arbeiten)
6. 3 Minuten später: Report ist da
7. "Aha-Moment" ✓
```

---

## Konzept: 2 Zustände

### Zustand A: Neuer User (0 Reports)

```
┌─────────────────────────────────────────────┐
│ ●Ainary           [Daily Brief] [Florian ▾] │
│                                             │
│                                             │
│                                             │
│                                             │
│     What company do you want to analyze?     │
│                                             │
│     ┌─────────────────────────────────┐     │
│     │ Enter company name...            │     │
│     └─────────────────────────────────┘     │
│     [Corporate X-Ray]  [Startup X-Ray]      │
│                                             │
│     3 free credits · No credit card needed   │
│                                             │
│                                             │
│                                             │
└─────────────────────────────────────────────┘
```

**Warum:** Kein Noise. Kein Dashboard. Keine Sidebar. 
Nur die EINE Frage. Wie Claude. Wie Perplexity.

### Zustand B: Returning User (1+ Reports)

```
┌─────────────────────────────────────────────┐
│ ●Ainary           [Daily Brief] [Florian ▾] │
│                                             │
│     What company do you want to analyze?     │
│     ┌─────────────────────────────────┐     │
│     │ Enter company name...            │     │
│     └─────────────────────────────────┘     │
│     [Corporate X-Ray]  [Startup X-Ray]      │
│                                             │
│     ─── Your Reports ───────────────────    │
│                                             │
│     Meridian Automotive    Corporate  Feb 12 │
│     47 pages · Completed                    │
│                                             │
│     Arclight AI            Startup    Feb 11 │
│     32 pages · Completed                    │
│                                             │
│     ─── Today's Intelligence ───────────    │
│                                             │
│     3 signals · 1 high-relevance            │
│     [Read Daily Brief →]                    │
│                                             │
│     ────────────────────────────────────    │
│     2 / 3 credits remaining                 │
│                                             │
└─────────────────────────────────────────────┘
```

**Warum:** Input bleibt prominent. Reports sind da aber sekundär.
Daily Brief als Bonus-Wert (komm jeden Tag zurück).

---

## Was wir NICHT brauchen (jedenfalls nicht jetzt)

1. ~~Sidebar~~ — Zu komplex für Tag 1. Claude hat eine, Linear hat eine, aber die haben tausende Features. Wir haben 2.
2. ~~Settings Page~~ — Email + Password ändern? Nicht für MVP.
3. ~~Onboarding Wizard~~ — "Enter company name" IST das Onboarding.
4. ~~Quick Actions Cards~~ — Wenn du nur 2 Produkte hast, brauchst du keine "Quick Actions".

---

## Bestehende Seiten: Was ändert sich nach Login?

| Seite | Logged Out | Logged In |
|-------|-----------|-----------|
| Landing | Marketing + "Sign up" CTAs | Redirect → Post-Login |
| Products | Showcase + "Sign up to analyze" | "Analyze" Button aktiv |
| Daily Brief | Teaser (3 Signale) | Volle Analyse |
| Blog | Frei zugänglich | Frei zugänglich |
| Pricing | Alle Tiers sichtbar | "Current: Free" Badge |
| Nav | "Log in" + "Sign up" | "Florian ▾" Dropdown |

---

## Empfehlung

**Phase 1 (jetzt bauen):**
- Post-Login Page = Zustand A (Input-Feld only)
- Nav: Replace "Log in/Sign up" mit "Florian ▾" Dropdown (My Reports, Settings, Log out)
- Das gebaute Dashboard als "My Reports" Page recyclen (wenn man auf "View all" klickt)

**Phase 2 (nach ersten Usern):**
- Zustand B (Reports + Daily Brief darunter)
- Daily Brief Content-Unlock für eingeloggte User

**Phase 3 (wenn nötig):**
- Sidebar — nur wenn wir 5+ Features haben
- Settings — nur wenn wir Payments haben

---

## Die Frage an Florian

Zustand A oder gleich Zustand B? 

Mein Vote: **A zuerst.** Weil:
- Simpler zu bauen
- Erzwingt Fokus auf das Kernprodukt
- Wir wissen noch nicht ob Daily Brief im Dashboard Sinn macht
- "Don't let users start from a blank page" (Linear-Prinzip) → der Input IST die Seite

---

*Geschrieben: 2026-02-12, 15:05*
*Nicht gebaut — erst nach Florians Review.*
