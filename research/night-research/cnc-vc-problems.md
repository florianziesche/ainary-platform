# Deep Dive: Problems & Opportunities in CNC Manufacturing Planning and Venture Capital

**Date:** 2026-02-05  
**Research Type:** Night Research — Industry Pain Points & Market Analysis

---

## PART 1: CNC Arbeitsvorbereitung (Work Planning) — Problems & Opportunities

### 1.1 Fachkräftemangel (Skilled Worker Shortage) — The Numbers

The skilled worker crisis in German manufacturing is severe and worsening:

- **1.98 million** skilled workers missing in Germany overall (IAB, 2024)
  - Source: https://jus-spanntechnik.de/blog/fachkraeftemangel-statistik/
- **530,000+** qualified workers missing as of October 2024 (IW Köln study)
  - Source: https://iqb.de/karrieremagazin/mint/fachkraeftemangel-in-deutschland/
- **~2/3 of CNC machining SMEs** reported increasing and acute skilled worker shortage in Spring 2024 survey
  - Source: https://www.werkzeug-einsatz-optimierung.de/fachkraeftemangel-in-der-branche-der-cnc-zerspanung-lohnfertigung-strategie-gewinn-erfolg-hpw-hagelberg/
- VDMA survey (500+ members): Fachkräftemangel for MINT jobs in Maschinenbau described as "increasingly dramatic"
  - Source: https://de.statista.com/statistik/daten/studie/1347252/umfrage/mitarbeiternachfrage-im-maschinenbau-in-deutschland/
- German Werkzeugmaschinenindustrie: **~405 companies**, **99,900 employees** — revenue fell ~6% in 2024
  - Source: https://de.statista.com/themen/1079/werkzeugmaschinenindustrie/
- Manufacturing contributed **19.7%** to Germany's gross value added in 2024
  - Source: https://www.nextmsc.com/report/europe-erp-software-market-ic3595

**Root causes:**
- Demographic shift (aging population, low birth rate)
- Young people not entering trades (Ausbildung zum Zerspanungsmechaniker declining)
- Competition from IT/tech sector for MINT talent
- Rural areas hit hardest — urban-rural divide
- Experienced workers retiring, knowledge leaving with them

**What this means for software:** Every tool that can reduce dependency on scarce experienced workers has massive pull. If software can encode expert knowledge (Erfahrungswissen) into automated planning, the TAM isn't just "software spend" — it's "avoided labor cost."

---

### 1.2 Arbeitsvorbereitung Today: How Long, What's the Bottleneck?

**Key insight from Bechtle PLM (2026):**
> "Die Auftragsbücher sind voll, aber die CNC-Fertigung kommt nicht hinterher. Maschinen stehen still, weil Material fehlt. Konstruktion und Arbeitsvorbereitung arbeiten mit unterschiedlichen Daten. Die Softwarelandschaft ist ein Flickenteppich. Daten werden doppelt erfasst. Fehler schleichen sich ein – und kurzfristige Änderungen kosten Stunden."
- Source: https://www.bechtle-plm.com/wissen/blog/cnc-fertigung-optimieren-6-schritte/

**Siemens / NC-Fertigung analysis:**
> "Etwa 15% der Werkzeuge in Unternehmen liegen nicht dokumentiert herum."
> Workers spend **~20% of their time searching for the right tools**. ~20% of tool costs are wasted due to lack of transparency.
- Source: https://www.nc-fertigung.de/digitale-loesungen-beschleunigen-die-cnc-fertigung
- Source: https://de.dmgmori.com/produkte/digitalisierung/arbeitsvorbereitung/digitale-werkzeugverwaltung

**Typical Arbeitsvorbereitung bottlenecks:**
1. **Kalkulation / Quoting** — Estimating machining time for new parts takes 30–120 min per part manually. Experienced Arbeitsvorbereiter needed; juniors can't do it.
2. **Arbeitsplanerstellung** — Creating the work plan (sequence of operations, tools, fixtures, machines) is manual, knowledge-intensive
3. **NC-Programm-Bereitstellung** — Finding/loading the right NC program, version control chaos (USB sticks, network folders, "welche Datei ist die richtige?")
4. **Werkzeugbereitstellung** — Finding tools, checking condition, loading tool magazines. 15% of tools undocumented.
5. **Rüsten (Setup)** — Setup time dominates for small batches. Forum users consistently say "setup takes the longest."
6. **Data silos** — CAD, CAM, ERP, tool management all disconnected. Different data in each system.

**Time estimates from industry:**
- Spanflug claims their software reduces Angebotserstellung effort by **up to 90%**
  - Source: https://www.nc-fertigung.de/erweiterte-kalkulationssoftware-fuer-die-zerspanung
- Digital twin / simulation can reduce Einrichtezeiten (setup time) by **up to 20%**
  - Source: https://www.nc-fertigung.de/digitale-loesungen-beschleunigen-die-cnc-fertigung
- With Spanflug MAKE: automated calculation "innerhalb von wenigen Sekunden" vs. 30-120 min manually
  - Source: https://spanflug.de/make/

---

### 1.3 What Tools Do Small/Medium CNC Shops Use?

**The universal truth: Excel + Paper + Experience**

- **99% of machine shop supervisors use Excel** for daily planning and scheduling (JITbase survey)
  - Source: https://www.jitbase.com/blog/the-ubiquity-and-limitations-of-excel-in-machine-shop-daily-planning
- **100% of surveyed VC/PE funds also use Excel** for LP reporting (interesting parallel!)
- **95% of GPs (in the Riskrate VC survey) use Excel** to collect data — same pattern in manufacturing

**Real forum quotes (Practical Machinist):**
> "I use a big white board now... You can use an Excel spread sheet and make it someone's job to update it twice a day."
- Source: https://www.practicalmachinist.com/forum/threads/machine-scheduling.393367/

> "He did however have a nice Excel template he used for quoting."
- Source: https://www.practicalmachinist.com/forum/threads/how-do-you-calculate-time.322355/

> "With how many machines I have (25 CNC's) it is really easy to lose track if we are making money or not."
- Source: https://www.practicalmachinist.com/forum/threads/quotes.145735/

**Excel limitations in CNC planning (from JITbase):**
1. Manual data entry → errors
2. No real-time updates (static snapshots)
3. Scalability issues with growing operations
4. Limited collaboration (version control nightmares)
5. No advanced analytics or optimization
6. Hard copies immediately outdated
7. Security risks

**Typical tool stack of a German KMU Zerspanungsbetrieb:**
- ERP: Often basic (proAlpha, abas, SAP B1, or none at all)
- CAD/CAM: SolidWorks + CAMWorks, Siemens NX, or Mastercam
- Planning: Excel, paper Laufzettel, whiteboards
- Tool management: Physical tool cabinets, maybe TDM or Zoller
- Communication: Phone calls across the shop floor, shouting

---

### 1.4 Competitors & Existing Solutions

#### A) Kalkulation / Quoting Software
| Company | Focus | Notes |
|---------|-------|-------|
| **Spanflug MAKE** | CNC part quoting & Arbeitsvorbereitung | Munich startup, SaaS, AI-based analysis of CAD models. Claims 90% reduction in quoting effort. Strong DACH focus. Closest competitor to an "AV automation" tool. |
| **Costimator** (MTI Systems) | Manufacturing cost estimation | US-based, legacy desktop software. Process-model based. Machinists on Reddit: "I told them I was probably more accurate/fast without software." |
| **FACTON** | Product cost management | Potsdam-based, enterprise-grade. For OEMs, not job shops. |
| **Calcmaster** | CNC time calculation | Swiss, focused on calculation accuracy |

Source: https://spanflug.de/make/  
Source: https://www.capterra.com/p/10010618/Costimator-Cost-Estimating-Software/

#### B) CAM Software (Toolpath generation, not planning)
Major players: Mastercam, Siemens NX CAM, SolidCAM, CAMWorks, hyperMILL, GibbsCAM, Fusion 360 (Autodesk), TopSolid, SprutCAM
- Global CAM software market: **$2.9–3.4 billion** (2024), growing to **$5.4–5.7 billion by 2030** (~9% CAGR)
  - Source: https://www.prnewswire.com/news-releases/cam-software-market-worth-usd-5-69-billion-by-2030--exclusive-report-by-marketsandmarkets-302319412.html

#### C) Production Planning / MES
| Company | Focus |
|---------|-------|
| **JITbase** | Shop floor scheduling, drag-and-drop, connected to machines |
| **CIMCO / SolidShop** | CNC data management + scheduling |
| **Vectotax** | ERP for Fertigungsunternehmen, focused on KMU |
| **FORCAM / ENISCO** | MES, Werkzeugverwaltung |
| **TDM Systems** (Sandvik) | Tool data management |

Source: https://www.mmsonline.com/articles/the-smarter-way-to-take-full-control-of-your-cnc-machine-shop  
Source: https://www.vectotax.de/  
Source: https://forcam-enisco.net/blog/werkzeugverwaltung-software-vorteile/

#### D) The Gap
**Nobody fully solves "Arbeitsvorbereitung" end-to-end for KMUs:**
- Spanflug focuses on quoting/Kalkulation but doesn't manage shop floor execution
- CAM software generates toolpaths but doesn't plan operations sequences
- ERP handles orders but not detailed manufacturing steps
- MES tracks execution but doesn't plan intelligently
- Tool management is a standalone silo

The **Arbeitsvorbereitung gap** = the space between "we received a customer order" and "the machine is running." This involves: reading drawings, deciding operations, selecting machines/tools, estimating times, creating work plans, preparing NC programs, organizing fixtures. This is still **mostly done in the head of an experienced Meister** — the single biggest knowledge bottleneck.

---

### 1.5 What CNC Machinists Complain About (Forums)

**From Reddit r/Machinists & r/CNC:**
- Programmers without machining experience creating bad programs: "When the CNC Programmer has 0 machining experience"
  - Source: https://www.reddit.com/r/Machinists/comments/1e9fwhb/when_the_cnc_programmer_has_0_machining_experience/
- Declining skills: "It makes me sad to see CNC machinists who have no understanding about concepts like surface speed or chip load"
  - Source: https://www.reddit.com/r/CNC/comments/16iv5us/is_a_career_in_cnc_worth_it/
- Quoting frustration: "To me I see something that is a pain in the ass to make, time consuming, and I will not profit practically at all"
  - Source: https://www.reddit.com/r/CNC/comments/10y5s3v/is_this_quote_i_received_reasonable/
- Career dissatisfaction: "Honestly if I could do it again I would not be a CNC machinist"
  - Source: https://www.reddit.com/r/CNC/comments/1bn5vcf/what_is_it_like_being_a_cnc_machinist/

**From Practical Machinist:**
- Setup time is the #1 pain: "Setup is going to take the longest"
  - Source: https://www.practicalmachinist.com/forum/threads/single-part-quotes-need-advice.120948/
- Quoting accuracy: "There is a hell of a difference between planning the tooling/fixtures and building the program than dealing with setup time"
  - Source: https://www.practicalmachinist.com/forum/threads/setup-time.183866/
- Shop scheduling with whiteboards and Excel
  - Source: https://www.practicalmachinist.com/forum/threads/machine-scheduling.393367/

**Key German forums:** zerspanungsbude.net, CNC-Area.de (recently shut down)

---

### 1.6 ISO Standards for CNC Planning

**ISO 13399** — Cutting Tool Data Representation and Exchange
- International standard enabling cutting tool manufacturers to describe products in a unified digital format
- Simplifies data exchange between CAM, simulation, tool management
- Supported by major tool manufacturers (Sandvik, Kennametal, etc.)
- Source: https://en.wikipedia.org/wiki/ISO_13399
- Source: https://www.mmsonline.com/articles/iso-13399a-key-step-toward-data-driven-manufacturing

**ISO 14649 (STEP-NC)**
- Machine tool control language extending ISO 10303 STEP
- Adds machining model, geometric dimension and tolerance data for inspection
- Vision: Replace G-code with feature-based machining descriptions
- Slow adoption in practice despite technical superiority
- Source: https://en.wikipedia.org/wiki/STEP-NC

**Relevance:** Any planning software that properly leverages ISO 13399 tool data and ISO 14649 feature-based machining has a standards-based differentiation story.

---

### 1.7 Market Size: Fertigungsplanung Software in DACH

**Germany ERP market:**
- **~$2.7 billion** by 2029 (Statista), growing at 3.25% CAGR
  - Source: https://www.statista.com/outlook/tmo/software/enterprise-software/enterprise-resource-planning-software/germany
- Germany captures **22.3%** of Europe's ERP software market
  - Source: https://www.marketdataforecast.com/market-reports/europe-enterprise-resource-planning-software-market

**Global manufacturing operations management software:**
- **$17.46 billion** (2024), expected $18.96B in 2025
  - Source: https://www.grandviewresearch.com/industry-analysis/manufacturing-operations-management-software-market-report

**Smart manufacturing software:**
- **$139.5 billion** globally (2025), growing to $359B by 2032 (14.5% CAGR)
  - Source: https://www.fortunebusinessinsights.com/software-for-smart-manufacturing-market-110142

**DACH-specific estimate for Fertigungsplanung:**
- Germany has ~405 Werkzeugmaschinen producers + **thousands of Lohnfertiger** (contract manufacturers)
- Estimated 5,000–15,000 CNC machining shops in DACH region (based on directory listings)
- At €200–2,000/month SaaS pricing = **€12M–360M annual TAM** for a focused Arbeitsvorbereitung tool in DACH alone
- With manufacturing contributing 19.7% of Germany's GDP, the digitalization wave is politically backed

---

## PART 2: Venture Capital Industry Problems

### 2.1 Emerging Manager Struggles

**The fundraising crisis is real:**

- VC fundraising hit **$76.1 billion** in 2024 — lowest since 2019
- Only **508 new funds** launched — second-lowest count since 2014
- **Top 30 funds captured 75%** of all capital ($57B); just 9 funds raised 46% (~$35B)
- **Andreessen Horowitz alone captured ~10%** of the year's total
- Emerging managers raised only **20% of capital** ($15B) across 245 funds
  - Source: https://www.junipersquare.com/blog/vc-q4-2024
  - Source: https://pitchbook.com/news/articles/us-vc-fundraising-concentration-andreessen-horowitz

**Deloitte confirms:** "Established funds are still raising capital while emerging managers struggle"
- Source: https://www.deloitte.com/us/en/services/audit-assurance/articles/trends-in-venture-capital.html

**SEC held specific hearing** on challenges facing emerging fund managers (Nov 2024)
- Source: https://www.sec.gov/newsroom/press-releases/2024-175

**Key emerging manager pain points:**
1. **Fundraising** — Can't get meetings with institutional LPs; "flight to quality" means capital flows to established brands
2. **Lack of exits** — Without distributions from Fund I, can't raise Fund II
3. **Operations overhead** — Legal, compliance, fund admin, LP reporting consume time meant for deal sourcing
4. **Capital call logistics** — Complex waterfall calculations done in... Excel
5. **LP relationship management** — Small team, many LPs, each wanting custom reporting

**UBS Global Family Office Report 2024:** Liquidity risk is #1 fear among family offices allocating to private markets
- Source: https://www.goingvc.com/post/winning-family-offices-in-2025-the-vc-fundraising-playbook

---

### 2.2 LP Complaints

**Transparency & reporting are the core issues:**

- **LP satisfaction correlates 0.72 with quality of reporting** — poor reporting causes **35% of LP relationships to deteriorate** (Preqin LP survey)
  - Source: https://www.peony.ink/blog/venture-capital-lp-reporting-guide-2025

- **70% of LPs** in North America and Europe incorporate ESG criteria — but data quality is poor
  - Source: https://www.apiday.com/blog-posts/limited-partners-reporting-what-it-is-how-to-do-it-and-best-practices-for-private-equity

- **100% of surveyed GPs use Excel** for LP reporting (Riskrate survey, April 2025)
  - Source: https://www.riskrate.io/post/survey-lp-reporting-and-automation-in-venture-capital-and-private-equity-funds

**Riskrate survey key findings:**
- 95% of GPs use Excel to collect data from ALL portfolio companies
- Manual reporting becomes burdensome with **30+ portfolio companies**
- Waterfall calculations require time-consuming data consolidation and verification
- Calculating investor-specific performance metrics requires special focus and time
- 80% of GPs noted visual branding/layout of LP reports is important

**What LPs want:**
1. Timely, consistent quarterly reports
2. Standardized metrics (TVPI, IRR, DPI, RVPI)
3. Transparent explanations of methodology
4. ESG data
5. Quick responses to ad-hoc questions

**What they get:**
- Late reports
- Inconsistent formatting across funds
- Excel-generated PDFs
- Missing context on portfolio company performance
- Radio silence between quarters

**ILPA (Institutional Limited Partners Association)** created a standardized reporting template to address this — adoption is growing but not universal
- Source: https://ilpa.org/industry-guidance/templates-standards-model-documents/reporting-template/

---

### 2.3 What Founders Hate About VCs

**Sifted survey (59 founders):**
- **>75% faced arrogant VCs and were ghosted**
- **39% faced discrimination** (conscious or unconscious)
- VCs string founders along for weeks, then disappear
- After signing term sheets, some VCs delay to run down cash position then renegotiate
- "If many VCs treated LPs the way they treated founders they'd never raise another fund"
  - Source: https://sifted.eu/articles/founders-vc-horror-stories

**Common complaints:**

1. **Ghosting** — "Ghosting is extremely prevalent with VCs... lack of respect for a founder's time"
   - Source: https://techcrunch.com/2025/03/06/why-vcs-ghost-founders-or-reject-deals-and-never-speak-to-the-founder-again/

2. **Slow decisions** — Median time between Seed and Series A **increased >30% in 2024**. Multi-step processes that could be resolved in meeting 1 drag on for months.
   - Source: https://www.spectup.com/resource-hub/vc-expectations-in-2025

3. **Bad advice / no value add** — Serial founder: "Best advice I ever received was 'reduce your expectations of VCs to zero, then you will be pleasantly surprised from time to time'"
   - Source: https://sifted.eu/articles/founders-vc-horror-stories

4. **Discrimination** — Only 10% of senior investment roles in European VC held by women. 0.24% of UK VC went to Black entrepreneur teams (2009-2019)
   - Source: https://sifted.eu/articles/founders-vc-horror-stories

5. **Structural information asymmetry** — VCs see thousands of deals, founders raise once every 18-24 months. Power imbalance creates "reality distortion field" for investors.
   - Source: https://www.nfx.com/post/how-vcs-become-assholes

**NFX (VC firm) self-reflection on "How VCs Become Assholes":**
- Overwhelmed by negativity (saying no 99% of the time)
- Heartbreak fatigue (invested companies failing)
- Reality distortion field (everyone stops telling you the truth when you have money)
- Constantly on defense (triple-booked calendars, email overload)
  - Source: https://www.nfx.com/post/how-vcs-become-assholes

---

### 2.4 What's Broken in VC That Technology Could Fix

#### A) LP Reporting & Fund Operations
**Problem:** 100% use Excel. Manual, error-prone, time-consuming.  
**Solutions emerging:**
- Juniper Square (GP/LP management platform)
- Visible.vc (portfolio monitoring, 540+ VC funds)
- Carta (fund administration + cap table)
- Allvue Systems (fund management software)
- Rundit (LP reporting)
- Standard Metrics (fund management)
- Papermark (LP reporting)
- Decile Hub / VC Lab (emerging manager tools)

Source: https://standardmetrics.io/vc-fund-management-software-in-2025-the-complete-buyers-guide/  
Source: https://visible.vc/reporting/

#### B) Deal Sourcing & CRM
**Problem:** Relationships are everything but tracked in spreadsheets/emails.  
**Solutions:**
- 4Degrees (relationship intelligence CRM)
- Affinity (relationship CRM for VC)
- PitchBook / Crunchbase / CB Insights (market intelligence)

Source: https://www.4degrees.ai/blog/setting-up-your-venture-capital-fund-essential-services-and-technologies

#### C) Decision-Making Process
**Problem:** Harvard/NBER survey of 900 VCs found decisions are heavily subjective, focused on founders (team) over everything else. Process varies wildly between firms.  
Source: https://corpgov.law.harvard.edu/2019/08/20/how-do-venture-capitalists-make-decisions/

#### D) Communication / Founder Experience
**Problem:** Ghosting, slow feedback, no transparency on process or timeline.  
**Potential fix:** Structured deal pipelines with automated status updates, templated pass reasons, SLA commitments.  
No dominant solution exists yet.

#### E) Emerging Manager Back Office
**Problem:** New GPs cobble together fund admin, legal, compliance, reporting from scratch.  
**Solutions emerging:**
- VC Lab "Fund in a Box" (turnkey fund launch)
- AngelList (fund infrastructure)
- Decile Group (emerging manager platform)

Source: https://govclab.com/2025/08/14/vc-back-office-solutions/  
Source: https://fi.co/insight/vc-back-office-solutions

---

### 2.5 The Biggest VC Industry Structural Problems

1. **Exit market frozen** — Distributions depressed, LPs won't recommit, fundraising suffers. Circular problem with no easy fix.
   - $149.2B exit value in 2024 (improvement but still weak)
   - 21 exits >$1B contributed 42% of total — small number of outsized events
   - Source: https://www.junipersquare.com/blog/vc-q4-2024

2. **Concentration intensifying** — Capital flowing to fewer, larger funds. 30% of deals were flat or down rounds. The "barbell" is growing.
   - Source: https://carta.com/data/vc-concentration-2024/

3. **AI distortion** — AI companies account for 29% of deals and 46% of deal value. Non-AI startups starved of capital.
   - Source: https://www.junipersquare.com/blog/vc-q4-2024

4. **Regulatory challenges** — Large exits blocked by antitrust scrutiny. Companies staying private longer.

5. **McKinsey Global Private Markets Report 2025:** "Infrastructure fundraising down 15% YoY to lowest in a decade"
   - Source: https://www.mckinsey.com/industries/private-capital/our-insights/global-private-markets-report

---

## Cross-Cutting Themes (CNC × VC)

| Pattern | CNC Manufacturing | Venture Capital |
|---------|-------------------|-----------------|
| **Excel dependency** | 99% use Excel for planning | 100% use Excel for LP reporting |
| **Knowledge in heads** | Experienced Meister holds the planning knowledge | Senior partners hold deal/relationship knowledge |
| **Skilled worker shortage** | Can't find Zerspanungsmechaniker | Can't find experienced fund operations people |
| **Fragmented tools** | CAD + CAM + ERP + Tool mgmt = silos | CRM + Fund admin + LP portal + Cap table = silos |
| **Paper/manual processes** | Laufzettel, whiteboards, printouts | PDF reports, email-based updates |
| **Setup time dominates** | Small batch = setup > cutting | New fund = legal/ops setup > investing |
| **Standards exist but ignored** | ISO 13399/14649 poorly adopted | ILPA templates exist but optional |

---

## Key Takeaways for Opportunity Assessment

### CNC Arbeitsvorbereitung:
1. **Massive pain, low digitalization** — The gap between "CAD model arrives" and "machine runs" is still filled by human expertise and Excel
2. **Spanflug is the closest competitor** but focuses on quoting, not full AV automation
3. **The knowledge encoding problem** is the real opportunity — turning Meister-knowledge into software
4. **Market is ready** — Fachkräftemangel creates urgency, Industry 4.0 creates political/funding tailwind
5. **DACH TAM conservative estimate:** €12-360M/year depending on pricing and penetration

### Venture Capital:
1. **Emerging managers are underserved** — squeezed between expensive enterprise tools and Excel
2. **LP reporting is the most automatable pain point** — already seeing multiple startups attack it
3. **Founder experience is terrible** but hard to monetize (founders aren't the paying customer)
4. **The exit freeze creates opportunity** for secondary market tools, valuation tools, portfolio analytics
5. **Back-office-as-a-service** is a growing category for emerging managers

---

*Research compiled from 25+ sources, February 2026*
