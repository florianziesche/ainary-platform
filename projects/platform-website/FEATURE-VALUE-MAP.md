# Feature & User-Value Map

*Jedes Feature muss einen klaren User-Value haben. Kein Feature ohne "So what?".*
*Sortiert nach: Compound-Wirkung (wie stark wird es mit der Zeit?)*

---

## Tier 1: Core (Launch)

| Feature | User Value | Business Value | Credits |
|---------|-----------|---------------|---------|
| **Company X-Ray** | "Verstehe jedes Unternehmen in 3 Min" | Kern-Produkt | 3 Cr |
| **Report Update** | "Bleib aktuell, günstiger als neu" | Retention, wiederkehrende Revenue | 1 Cr |
| **Daily Brief** | "Jeden Morgen die Signale die zählen" | Täglicher Touchpoint, Habit | Free / 1 Cr für Deep Analysis |
| **Personalized Insights (Wartezeit)** | "Relevante News WÄHREND du wartest" | Cross-Sell, Engagement | Free |

**User-Aufwand:** Minimal. Login → Analyze → Fertig.

---

## Tier 2: Compound (Monat 1-3)

| Feature | User Value | Business Value | Compound-Effekt |
|---------|-----------|---------------|-----------------|
| **Company Tracker** | "News zu deinen Companies → Alert" | Upsell ("Track this company?") | Portfolio wächst → mehr Alerts → mehr Value |
| **Topic Preferences** | "Wähle: AI, Agents, FinTech, Automotive..." | User Analytics + bessere Personalisierung | Empfehlungen werden besser mit der Zeit |
| **Article Like / Bookmark** | "Speichere was wichtig ist" | Engagement Signal + Content Analytics | Private Wissensdatenbank wächst |
| **Cross-Report Patterns** | "Trend über deine Analysen hinweg erkannt" | Unique Insight, nur durch Nutzung möglich | Mehr Reports → mehr Patterns → mehr Value |

**User-Aufwand:** Gering. Ein Klick: Track / Like / Preference setzen.

---

## Tier 3: Moat (Monat 3-12)

| Feature | User Value | Business Value | Compound-Effekt |
|---------|-----------|---------------|-----------------|
| **Custom Sources** | "Deine eigenen RSS Feeds im System" | Can't-Live-Without, Pro Upgrade | Je mehr Quellen → besser personalisiert → kann nicht wechseln |
| **Historical Delta** | "Was hat sich seit deiner letzten Analyse geändert?" | Report Updates verkaufen sich von selbst | Zeitreihe wächst → einzigartige Perspektive |
| **Report Update Notifications** | "Neue Daten verfügbar — 1 Cr für Update" | Passive Revenue, User kommt zurück | Tracker + neue Daten → automatische Benachrichtigung |
| **Crowd Intelligence** | "47 Analysten tracken BMW. Top Concern: X" | Netzwerkeffekt, mehr User = mehr Value | Exponentiell mit Nutzerzahl |

**User-Aufwand:** Mittel. Custom Sources einrichten = 10 Min. Danach automatisch.

---

## Credit-Ökonomie

| Aktion | Credits | Warum dieser Preis |
|--------|---------|-------------------|
| Neuer Report | 3 | Volle 5-Agent Analyse, teuerste Aktion |
| Report Update | 1 | Nur Delta-Analyse, günstiger → incentiviert Tracking |
| Daily Brief (Basic) | Free | Täglicher Hook, bringt User zurück |
| Daily Brief (Deep) | 1 | Volle Analyse eines Signals |
| Company Tracker Setup | Free | Je mehr Tracker → mehr Update-Notifications → mehr 1-Cr Updates |
| Custom Source hinzufügen | Free (Pro only) | Lock-in Feature, der Zugang ist der Wert |

**Das Pricing-Flywheel:**
```
Neuer Report (3 Cr) 
  → "Track this company?" (Free)
    → Neue Daten verfügbar (Notification)
      → "Update für 1 Cr?" 
        → User bleibt → Nächster Report (3 Cr)
```

---

## User Journey mit Compound-Effekt

```
Woche 1:   Sign up → 1. Report (3 Cr) → "Wow"
Woche 2:   Daily Brief liest er jeden Morgen → Habit
Woche 3:   Tracked 3 Companies → bekommt Alerts
Monat 2:   5 Reports → Cross-Pattern: "Trend in deinem Sektor"
Monat 2:   "Update verfügbar für BMW" → 1 Cr → Historical Delta
Monat 3:   Eigene Sources hinzufügen (Pro) → Daily Brief wird SEINE
Monat 6:   15 Reports, 8 Tracker, 12 Custom Sources
           → Switching Cost: UNMÖGLICH
Monat 12:  Private Intelligence Network
           → "Mein Bloomberg Terminal für €29/mo"
```

---

## Was wir NICHT bauen (Komplexität vermeiden)

- ❌ Social Features (Kommentare, Sharing zwischen Usern)
- ❌ Team/Collaboration (erst wenn Enterprise-Kunden kommen)
- ❌ Eigene Dashboards/Charts bauen
- ❌ API für Dritte (erst Phase 5)
- ❌ Eigene AI-Modelle trainieren auf User-Daten

---

## Interaktions-Übersicht (Simple)

```
User kann:
├── Analyze    → Neuer Report (3 Cr) oder Update (1 Cr)
├── Track      → Company auf Watchlist (Free)
├── Read       → Daily Brief + Artikel (Free / 1 Cr Deep)
├── Customize  → Preferences (Free) + Custom Sources (Pro)
├── Save       → Like / Bookmark Artikel + Insights (Free)
└── Discover   → Cross-Patterns + Crowd Signals (automatisch)
```

**6 Verben. Nicht mehr.** Jedes hat klaren Wert. Keines ist überflüssig.

---

*Erstellt: 2026-02-12, 15:20*
*Status: Konzept — nicht gebaut. Review mit Florian.*
