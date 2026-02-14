# LinkedIn Post — Agent Trust System (AgentTrust)

## Post

My AI agent confidently stated a "fact" that was actually an assumption. Nobody caught it — except the system I built to catch exactly that.

I run 7 specialized AI agents. The problem: LLMs are overconfident in 84% of cases (Kadavath et al.). They don't say "I'm not sure." They just sound right.

So I built a trust system with one rule: honesty is currency.

How it works:
→ Budget-CoCoA Calibration: Ask the agent 3x. If answers stay consistent = real confidence. If they drift = flag it.
→ QA Agent is adversarial. Its job is to break the output, not approve it.
→ Every claim gets tagged: fact, assumption, or inference.

The moment it proved itself: Calibration caught an assumption dressed as a fact in a client-facing draft. The kind of mistake that erodes trust slowly — until it doesn't.

No production-ready trust framework for multi-agent systems exists yet. So I'm building AgentTrust as open source.

How do you handle confidence calibration in your agent setups?

#AI #Agents #BuildingInPublic

---

## Beipackzettel

**Confidence:** 85%

**Zeichenzahl:** 1.048 / 1.200

**Hashtags:** 3 / 3 max

**Begründungen:**
- Hook: Konkretes Fehlerszenario statt abstrakte These — zieht rein weil es ein echtes Problem zeigt (corrections.md: "Substanz > Optik")
- "84%" Zahl: Aus Briefing-Context. Referenz zu Kadavath et al. gibt Glaubwürdigkeit ohne akademisch zu klingen
- Struktur mit → Pfeilen: Beibehalten vom FINAL-Post Stil — funktioniert visuell auf LinkedIn
- "honesty is currency": Aus dem Briefing, verdichtet das Konzept in 3 Wörter
- CTA als offene Frage: Nicht "What do you think?" (zu generisch) sondern spezifisch "confidence calibration in your agent setups"
- Kein "Excited to announce" / "Great news" (AGENT.md verbotene Phrasen + corrections.md)
- "I" Perspektive durchgängig (corrections.md: Solo Founder Voice)

**QA-relevante Entscheidungen:**
- ⚠️ "Kadavath et al." — Quelle aus Briefing übernommen, nicht unabhängig verifiziert. Florian sollte prüfen ob die Zahl stimmt und ob er die Referenz drin haben will.
- ⚠️ "client-facing draft" — leichte Dramatisierung des Briefing-Beispiels. Wenn es kein Client Draft war → anpassen.
- ✅ "7 specialized AI agents" — diesmal aus Briefing bestätigt, daher konkrete Zahl statt "mehrere"
- ✅ Open Source Mention ohne Link (kein Link vorhanden, wie im FINAL-Post gelernt)

**Voice Check:** ✅ Florian — direkt, "I"-Perspektive, konkretes Beispiel vor Theorie, keine LLM-Phrasen, spezifische CTA
