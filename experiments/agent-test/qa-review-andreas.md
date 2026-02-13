# QA Review: Andreas Brand Outreach Email

**Score:** 45/100  
**Verdict:** ❌ **FAIL** — Major violation + tonality mismatch

---

## 🚨 Critical Violations

### 1. **FOLLOW-UP OHNE KONTEXT (-30 Punkte)**
**Source:** `people.md` → "Email 06.02 gesendet, Antwort pending"

**Das Problem:**
- Andreas hat vor 7 Tagen eine Email bekommen (06.02)
- Er hat NICHT geantwortet
- Diese Email ignoriert das komplett
- Das ist unhöflich und sieht aus wie Spam (zwei identische Pitches ohne Acknowledgment)

**Was fehlt:**
- "Ich hatte dir letzte Woche geschrieben..." ODER
- Medium wechseln (WhatsApp statt Email — er ist Familie!) ODER  
- Einfach warten auf Antwort

**Fix:**
Entweder komplett umschreiben als persönliche Nachfrage ("Hey Andreas, hast du meine Email letzte Woche gesehen?") oder Medium wechseln.

---

### 2. **ZU FORMAL FÜR FAMILIE (-15 Punkte)**
**Source:** `people.md` → "Andreas Brand — Onkel"

**Das Problem:**
Der Ton ist B2B-Sales, nicht Familie. Vergleiche:

❌ "ich habe als Proof of Concept einen AI-basierten Corporate X-Ray Report für MBS erstellt"  
✅ "Hey Andreas, ich habe was für MBS gebaut das dir helfen könnte"

❌ "Der Report ist fertig. Ich würde dir gern zeigen"  
✅ "Schau's dir mal an, sag mir was du denkst"

**Was fehlt:**
- Persönlicher Einstieg (Bezug auf Beziehung, letztes Gespräch, etc.)
- Weniger Corporate-Sprache
- Mehr "ich helfe dir" statt "ich verkaufe dir"

---

### 3. **MARKETING-TON STATT SUBSTANZ (-10 Punkte)**
**Source:** `quality-standards.md` → "Florians Stimme: direkt, ehrlich, spezifisch"

**Das Problem:**
- "Corporate X-Ray Report" klingt wie Buzzword-Bingo
- "Proof of Concept" — warum nicht einfach "Report"?
- "intelligente Werkzeugauswahl" — okay, aber ohne Beispiel abstrakt

**Was fehlt:**
- 1-2 konkrete Zahlen ("spart dir 3h/Woche in der AV")
- Screenshot/Beispiel ("Hier, schau dir Seite 4 an")
- Weniger Label, mehr Show

---

## ⚠️ Minor Issues

### 4. **Kein persönlicher Hook (+0 Punkte, aber Chance verpasst)**
**Source:** `quality-standards.md` → "Konkreter Grund warum ICH an DICH schreibe"

Warum MBS? Warum Andreas? Warum jetzt?  
Antwort: Weil er Onkel ist und Florian ihm helfen will. Das steht nicht drin.

Besser: "Ich weiß wie viel Zeit bei euch in die Arbeitsvorbereitung geht — dachte mir das könnte helfen."

---

### 5. **CTA könnte konkreter sein (+0 Punkte)**
"Nächste Woche 20 Minuten" — okay, aber:
- Kein Terminvorschlag (Dienstag 14:00?)
- Kein Cal.com Link
- Bei Familie: Warum nicht Samstag vorbeikommen und zeigen?

---

## ✅ Was funktioniert

- ✅ Länge: 6 Sätze (Quality Standard: 5-7) ✓
- ✅ Keine Preise (Correction) ✓
- ✅ Du-Form korrekt für Familie ✓
- ✅ Konkrete Beispiele (NC-Programm, Werkzeugauswahl, Zeitkalkulation) ✓
- ✅ Klarer CTA (Call) ✓
- ✅ Kein "I hope this email finds you well" ✓

---

## 📊 Calibration Check

**Agent claimed:** 75% Confidence  
**My assessment:** 35% Confidence

**Warum die Differenz?**
Der Agent hat den Kontext (`people.md`: "Email 06.02 pending") gelesen, aber nicht verstanden, dass das ein FOLLOW-UP ist. Das ist kein kleiner Fehler — das ist die Grundlage der gesamten Email.

Uncertainty im Beipackzettel zeigt:
- "ob Andreas bereits technisch affin ist" → irrelevant bei Familie, einfach fragen
- "ob 20 Min Call das richtige Format ist" → RICHTIGE Frage, aber keine Antwort
- "könnte als pushy wahrgenommen werden" → JA, weil Follow-up ohne Kontext!

Der Agent HAT das Problem gesehen ("Known risks: Email vom 06.02 ist noch oben"), aber nicht verstanden wie kritisch das ist.

---

## 🎯 Recommendation

**ZURÜCK AN AGENT MIT SPEZIFISCHEN FIXES:**

### Option A: Follow-up mit Kontext
```
Hey Andreas,

ich hatte dir letzte Woche den AI Report für MBS geschickt — hast du Lust, da mal reinzuschauen?

Wenn du magst, können wir 20 Minuten telefonieren, oder ich komme vorbei und zeige dir, wie das konkret in der AV aussehen könnte.

Sag Bescheid!
Gruß, Florian
```

### Option B: Medium wechseln (WhatsApp/Anruf)
Wenn Andreas eher WhatsApp nutzt oder anrufen besser ist (Familie!), Email skippen und direkt kontaktieren.

### Option C: Warten
Wenn die erste Email noch keine Woche alt ist (06.02 → 13.02 = 7 Tage), einfach noch 3-5 Tage warten. Er ist Familie, kein Lead der wegläuft.

---

## 📝 Lessons Learned

1. **Follow-ups IMMER kennzeichnen** — "Ich hatte dir letzte Woche..." ist Pflicht
2. **Kontext checken:** `people.md` nicht nur lesen, sondern verstehen (Email pending = DO NOT SEND AGAIN)
3. **Audience-Ton anpassen:** Familie ≠ B2B Cold Outreach
4. **Marketing-Sprache bei Familie vermeiden:** "Report für dich gebaut" > "Corporate X-Ray Proof of Concept"

---

**Status:** FAIL — Agent soll neu schreiben oder Strategie wechseln (WhatsApp, Anruf, Warten).
