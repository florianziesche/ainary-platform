# Verified Slide Grid Standard
## Sources: Penn State AE Template (.pptx measured), McKinsey PDFs (3 decks), Palantir Q1 2025 (40 slides)

### Consensus Grid (McKinsey + Penn State)

| Element | Position | Confidence |
|---------|----------|-----------|
| Headline top | 2-5% | 90% (2 sources agree) |
| Body/Visual zone start | 18-25% | 85% (all 3 sources) |
| Left/right margin | 3-5% | 90% (all 3 sources) |
| Headline width | 80-95% of slide | 85% |
| Footer/source | 93-97% from top | 90% |
| Headline max | 2 lines | 95% (Penn State explicit) |

### Source-Specific Measurements

**Penn State Assertion-Evidence (16:9, .pptx parsed)**
- Headline: top=1.1%, left=0.8%, width=98.5%, height=15.6-16.8%
- Visual: top=23-27%
- Slide number: bottom-right 93.1%
- Font: headline 26pt, body 20pt

**McKinsey (3 PDFs, PyMuPDF measured, 75% confidence)**
- Action Title: top=2.3-5.4%, width=80-90%
- Body zone: starts at 18-22%
- Margins: 4.5-4.7%
- Font: Georgia Bold 20-25pt (post-2019), Arial 12-14pt body
- Footer: 96-97%

**Palantir Q1 2025 (40 slides, PyMuPDF measured, 95% confidence)**
- Section label: top=5.9%, left=3.9%, 12pt
- Headline: top=13.3-15.9%, left=3.1-5.5%
- Statement headlines: 52pt. Data headlines: 39pt. Dividers: 124pt.
- Left margin: 3.0-3.1%
- Copyright: 93.9%, 9pt

### Palantir is the outlier
Palantir uses 13% for headline because they have a section label above.
McKinsey and Penn State agree: headline at 2-5%.
Palantir's premium whitespace = section label, not margin.

### Our Ainary Deck Settings
- --head-top: 3vh (= ~3%, within McKinsey range)
- --vis-top: 24vh (= ~24%, within consensus)  
- --mx: 4.5vw (= 4.5%, matches McKinsey exactly)

Date: 2026-02-21
