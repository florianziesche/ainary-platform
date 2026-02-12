/**
 * Demo Data Generator
 * Provides realistic mock data when no OpenAI key is available
 */

const operator = require('./advisors/operator');
const investor = require('./advisors/investor');
const contrarian = require('./advisors/contrarian');
const technologist = require('./advisors/technologist');
const strategist = require('./advisors/strategist');
const customer = require('./advisors/customer');

function generateDemoData(question) {
  const advisors = [operator, investor, contrarian, technologist, strategist, customer];

  const responses = [
    // Operator
    `Launch in Germany NOW. Here's why: You're already there, you know the market, and waiting 6 months means 6 months of lost revenue and network building.

Execution plan: Week 1-2: Set up Gewerbeschein + business bank account. Week 3-4: Close first 3 pilot clients (offer 50% discount for case studies). Month 2-3: Deliver pilots, get testimonials, raise rates.

The "perfect setup" fallacy kills more businesses than bad timing. NYC will always be there. The question is: can you afford NOT to start learning now? Research shows 78% of successful consultants started in "non-optimal" conditions.`,

    // Investor
    `Germany-first approach is strategically sound for 3 reasons:

1) Market timing: EU AI regulation is creating massive compliance demand. Companies need implementation help NOW. NYC will follow in 12-18 months - you'll have case studies by then.

2) Capital efficiency: Cost of customer acquisition in Germany is 40-60% lower than US. Burn less cash building initial traction.

3) Optionality: Launch in Germany, keep US option open. Can't do the reverse while living there. Recent data shows 67% of B2B SaaS companies now start in EU due to GDPR/AI Act creating built-in moat.

Recommendation: 6-month Germany sprint, then evaluate NYC expansion with revenue + case studies.`,

    // Contrarian
    `Everyone's saying "just start" - but that's lazy advice. The real question: Why consulting at all?

Consulting scales linearly (your time). You're building a job, not a business. And Germany has 19% VAT, complex employment law, and slower decision cycles than US.

The contrarian move: Build in public for 3 months BEFORE launching. Create content showing your AI implementation process. Build audience first, then productize later. Skip consulting entirely - go straight to AI implementation software.

Or if you must consult: Start remote-first from Germany, target US clients, charge in dollars. Best of both worlds. Recent GitHub data shows most successful AI tools came from creators who shared their process first, monetized second.`,

    // Technologist
    `Technical infrastructure perspective: Germany has better data privacy frameworks and more mature B2B SaaS ecosystem than people think. 

Key advantages: GDPR compliance is already baked in (huge selling point for enterprise). AI Act early-mover advantage. Tech stack can be location-agnostic (Stripe Atlas, remote tools).

NYC advantage: Better access to cutting-edge AI companies, faster feedback loops, higher willingness to pay.

My take: Use Germany time to build your implementation playbook + automation tools. Treat first 5 clients as product research, not revenue. By the time you're in NYC, you'll have a system, not just services.

Pro tip: Most AI consultants fail because they're selling hours, not outcomes. Build measurement frameworks first. ArXiv research shows outcome-based pricing gets 2.3x higher retention.`,

    // Strategist
    `This isn't a location question - it's a positioning question.

Germany play: "AI Compliance & Implementation Specialist" - ride the EU AI Act wave. Become THE expert in AI governance for German/EU companies. Charge premium for regulatory expertise.

NYC play: "AI Product Strategy Consultant" - help startups build AI features. Higher velocity, more risk-taking clients, better for learning cutting-edge applications.

The strategic error would be trying to be everything to everyone. Pick ONE positioning, own it completely, then expand.

My recommendation: Germany with CLEAR positioning. Specialize in "AI Implementation for Industrial/Manufacturing" (massive untapped market, lower competition than SaaS). Build case studies. NYC expansion becomes easier with proven vertical expertise.

Counter-signal: If you want to work with early-stage startups, Germany will frustrate you. Go to NYC.`,

    // Customer
    `From a customer perspective: Where are your DREAM clients?

I've seen consultants succeed in unlikely markets because they deeply understood their customer's pain. And I've seen them fail in "optimal" markets because they were solving their own problems, not customer problems.

Questions to ask:
- Who gets promoted/rewarded for hiring you?
- Where is the pain so acute they'll pay to fix it NOW?
- Can you reach decision-makers easily?

Germany advantage: Less competition, more trust-based relationships, longer sales cycles but higher retention. Customers value thoroughness over speed.

NYC advantage: Faster decision-making, higher risk tolerance, more willing to try new vendors.

My take: Interview 10 potential customers in Germany THIS WEEK. If 3+ are ready to pay, start there. If not, you're building a solution looking for a problem. Recent Reddit discussions show most consulting failures come from selling to the wrong customer segment, not wrong location.`
  ];

  const confidenceLevels = [4, 4, 3, 5, 4, 3]; // ●●●●○, ●●●●○, ●●●○○, etc.

  const researchData = {
    keywords: ['AI', 'consulting', 'Germany', 'NYC', 'business', 'launch'],
    sources: {
      arxiv: [
        {
          source: 'arxiv',
          title: 'AI Adoption Patterns in European SMEs: A Comparative Study',
          url: 'http://arxiv.org/abs/2402.12345',
          abstract: 'Analysis of AI implementation across 500 European companies shows 67% adoption rate in Germany vs 54% EU average. Key barriers: skill gaps, regulatory uncertainty.',
          published: '2024-02-10T08:00:00Z'
        },
        {
          source: 'arxiv',
          title: 'Economic Impact of EU AI Act on Consulting Services Market',
          url: 'http://arxiv.org/abs/2402.11234',
          abstract: 'Estimated €2.8B consulting market opportunity from AI Act compliance. Germany leads with €780M projected spend in 2024-2025.',
          published: '2024-02-09T14:30:00Z'
        }
      ],
      hackernews: [
        {
          source: 'hackernews',
          title: 'Show HN: Launched AI consulting in Berlin, $50k MRR in 4 months',
          url: 'https://news.ycombinator.com/item?id=39234567',
          score: 342,
          published: '2024-02-11T10:20:00Z'
        },
        {
          source: 'hackernews',
          title: 'EU AI Act creates massive opportunity for implementation consultants',
          url: 'https://news.ycombinator.com/item?id=39123456',
          score: 287,
          published: '2024-02-10T16:45:00Z'
        },
        {
          source: 'hackernews',
          title: 'Why I chose Munich over San Francisco for my AI startup',
          url: 'https://news.ycombinator.com/item?id=39012345',
          score: 198,
          published: '2024-02-09T09:15:00Z'
        }
      ],
      reddit: [
        {
          source: 'reddit',
          title: 'Germany vs US for B2B SaaS: 6 months in, here\'s what I learned',
          url: 'https://reddit.com/r/startups/comments/abc123',
          score: 156,
          published: '2024-02-11T12:00:00Z'
        },
        {
          source: 'reddit',
          title: 'AI consulting rates in Europe vs US - data from 50+ consultants',
          url: 'https://reddit.com/r/entrepreneur/comments/xyz789',
          score: 203,
          published: '2024-02-10T14:30:00Z'
        }
      ],
      github: [
        {
          source: 'github',
          title: 'awesome-ai-consulting',
          url: 'https://github.com/ai-consulting/awesome-resources',
          description: 'Curated list of AI consulting frameworks, pricing templates, and case studies. 2.3k stars.',
          published: '2024-02-11T08:00:00Z'
        }
      ]
    },
    totalItems: 10,
    timestamp: new Date().toISOString()
  };

  const knowledgeStructure = {
    keyFacts: [
      'EU AI Act creates estimated €2.8B consulting market opportunity, with Germany leading at €780M projected spend',
      'German companies have 67% AI adoption rate vs 54% EU average, indicating mature market',
      'B2B customer acquisition costs in Germany are 40-60% lower than US markets',
      'Average AI consulting rates: Germany €150-250/hr, NYC $200-400/hr'
    ],
    recentDevelopments: [
      'Multiple HN posts report successful AI consulting launches in Germany with $30-50k MRR within 3-6 months',
      'EU AI Act compliance deadline driving immediate demand for implementation expertise',
      'Trend toward remote-first consulting with US clients from EU base for arbitrage'
    ],
    openQuestions: [
      'Long-term sustainability of AI Act compliance wave vs building evergreen consulting practice',
      'Optimal pricing model: hourly vs value-based vs retainer for AI implementations',
      'Market saturation timeline - how long before competition intensifies in Germany?'
    ],
    counterArguments: [
      'Germany\'s slower decision cycles and risk-averse culture may frustrate execution-focused consultants',
      'NYC offers 3-5x faster feedback loops and higher willingness to experiment with new vendors',
      'Consulting scales linearly - may be building a job rather than a business regardless of location'
    ],
    confidence: 'high'
  };

  const synthesis = {
    consensus: [
      'Start NOW rather than waiting - 5/6 advisors agree that delaying 6 months has higher opportunity cost than imperfect timing',
      'Germany offers structural advantages: lower CAC, regulatory tailwinds (EU AI Act), less competition in B2B space',
      'Build systems/playbooks early rather than just selling hours - productize learnings for future scale',
      'Choose clear positioning (compliance/implementation/strategy) rather than generalist approach'
    ],
    dissent: [
      'Location strategy: Operator/Investor favor Germany-first vs Contrarian suggests remote-first with US clients',
      'Business model: Strategist/Technologist push for specialized positioning vs Customer emphasizes testing market demand first',
      'Speed vs planning: Operator wants immediate execution vs Contrarian advocates 3-month build-in-public period'
    ],
    actionItems: [
      'Interview 10 potential clients in Germany THIS WEEK to validate demand and positioning (Recommended by: Customer, Strategist, Operator)',
      'Set up legal/business infrastructure in Germany (Gewerbeschein, business bank) while running validation interviews (Recommended by: Operator, Investor)',
      'Define ONE clear positioning (AI compliance/implementation for specific vertical) before any marketing (Recommended by: Strategist, Investor, Technologist)'
    ]
  };

  return {
    advisors,
    responses,
    confidenceLevels,
    researchData,
    knowledgeStructure,
    synthesis
  };
}

module.exports = { generateDemoData };
