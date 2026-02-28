```json
{
  "real_question": "Can we build a profitable AI calibration service targeting German Mittelstand companies before EU AI Act enforcement creates mandatory demand in August 2026?",
  "why_now": "EU AI Act enforcement starts August 2026 for high-risk systems (CT-023), but calibration standards are undefined (CT-015). CEN/CENELEC standards expected 2027-2028 create a 12-18 month window to establish market position before technical requirements crystallize (CT-016).",
  "sub_questions": [
    {
      "id": "SQ-1",
      "question": "Which German Mittelstand sectors deploy AI systems that fall under EU AI Act high-risk categories (Annex III) or transparency requirements (Art. 50)?",
      "why_it_matters": "Determines addressable market size and urgency of compliance needs by August 2026.",
      "evidence_needed": "Industry reports on AI adoption by German SMEs, EU AI Act applicability analyses for manufacturing/logistics/healthcare, BDI/VDMA position papers on AI regulation impact",
      "search_queries": [
        "\"deutscher mittelstand\" \"KI einsatz\" statistik 2024 manufacturing",
        "EU AI Act Annex III \"german SME\" compliance requirements analysis",
        "BDI VDMA \"künstliche intelligenz\" regulierung mittelstand 2024"
      ]
    },
    {
      "id": "SQ-2",
      "question": "What is the current state of AI calibration awareness and implementation maturity in German Mittelstand companies?",
      "why_it_matters": "Baseline assessment determines education vs. implementation focus and pricing strategy.",
      "evidence_needed": "Surveys on AI governance in German SMEs, case studies of calibration failures in German industry, consultancy reports on AI maturity models for Mittelstand",
      "search_queries": [
        "\"AI governance\" \"german SME\" survey 2024 calibration confidence",
        "mittelstand \"AI maturity\" assessment framework 2024",
        "\"KI Vertrauen\" kalibrierung mittelstand studie 2024"
      ]
    },
    {
      "id": "SQ-3",
      "question": "What are the technical integration requirements and costs for implementing calibration in typical Mittelstand AI deployments (ERP, MES, quality control)?",
      "why_it_matters": "Determines feasibility of <€5000/month target pricing and technical support requirements.",
      "evidence_needed": "Technical architectures of common German industrial AI systems, API documentation for SAP/Siemens/KUKA AI modules, implementation case studies from similar markets",
      "search_queries": [
        "SAP S/4HANA AI calibration integration API documentation",
        "\"Siemens MindSphere\" \"confidence scores\" implementation guide",
        "mittelstand \"AI integration\" costs case study manufacturing 2024"
      ]
    },
    {
      "id": "SQ-4",
      "question": "Which German certification bodies (TÜV, DEKRA) are developing AI assessment frameworks and what calibration requirements do they include?",
      "why_it_matters": "Certification body standards will become de facto requirements regardless of EU harmonized standards timeline.",
      "evidence_needed": "TÜV/DEKRA AI certification frameworks, DIN SPEC documents on AI trustworthiness, interviews with certification body representatives",
      "search_queries": [
        "TÜV Süd \"AI certification\" framework 2024 calibration requirements",
        "DIN SPEC 92001 \"vertrauenswürdige KI\" kalibrierung anforderungen",
        "DEKRA \"künstliche intelligenz\" zertifizierung mittelstand 2024"
      ]
    },
    {
      "id": "SQ-5",
      "question": "What competitive AI compliance solutions exist in the German market and how do they address calibration?",
      "why_it_matters": "Identifies partnership opportunities vs. competitive threats and pricing benchmarks.",
      "evidence_needed": "Competitor analysis of German AI governance vendors, pricing models for compliance software in German B2B market, partnership structures with system integrators",
      "search_queries": [
        "\"AI compliance\" software anbieter deutschland mittelstand 2024",
        "\"KI governance\" lösung preise german market analysis",
        "appliedAI akirio \"ai compliance\" partnership mittelstand"
      ]
    }
  ],
  "blindspots": [
    {
      "question": "Are we underestimating the role of Betriebsrat (works councils) in blocking AI implementations that lack explainability, regardless of calibration quality?",
      "why_its_a_blindspot": "German co-determination law gives workers significant power over AI deployment. Perfect calibration without worker trust may still fail.",
      "confidence": 85,
      "reasoning": "CT-025 shows trust depends on more than technical metrics. German labor relations add unique constraints not captured in our technical focus.",
      "recommendation": "YES — priority 2"
    },
    {
      "question": "Could mandatory calibration create a 'compliance theater' market where companies buy minimal solutions to check boxes rather than improve decision-making?",
      "why_its_a_blindspot": "Regulatory-driven markets often optimize for compliance documentation over actual performance improvement, limiting growth potential.",
      "confidence": 75,
      "reasoning": "ISO 42001 requires process but not outcomes (CT-022). Companies may prefer cheap 'calibration certificates' over real implementation.",
      "recommendation": "YES — priority 2"
    },
    {
      "question": "What if the real barrier isn't technical calibration but German SMEs' fundamental distrust of probabilistic vs. deterministic systems?",
      "why_its_a_blindspot": "German engineering culture values precision and determinism. Calibrated uncertainty may be culturally rejected regardless of regulatory requirements.",
      "confidence": 70,
      "reasoning": "CT-012 notes current UQ practices aren't human-centered. German Mittelstand engineering culture may require different framing than 'confidence scores'.",
      "recommendation": "MAYBE"
    }
  ]
}
```