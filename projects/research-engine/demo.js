#!/usr/bin/env node
// Demo script — Test renderer without OpenAI API
import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';
import { render } from './renderer.js';

const __dirname = path.dirname(fileURLToPath(import.meta.url));

console.log('\n🎨 Research Engine Demo — Testing HTML Template\n');

// Mock data
const mockRawData = {
  arxiv: [
    { title: 'Efficient Large Language Model Pretraining', category: 'cs.AI' },
    { title: 'Multi-Agent Reinforcement Learning Survey', category: 'cs.MA' }
  ],
  hackernews: [
    { title: 'Show HN: Local LLM runner with quantization', score: 342 },
    { title: 'GPT-4 vs Claude 3 Opus benchmark', score: 256 }
  ],
  reddit: [
    { title: 'New SOTA on ImageNet', subreddit: 'MachineLearning', score: 1203 },
    { title: 'Llama 3 leaked benchmarks', subreddit: 'LocalLLaMA', score: 892 }
  ],
  github: [
    { title: 'microsoft / autogen', language: 'Python', todayStars: 423 },
    { title: 'openai / whisper-v3', language: 'Python', todayStars: 312 }
  ],
  rss: [
    { title: 'The Next Wave of AI Infrastructure', feed: 'a16z' },
    { title: 'Why We Invested in Anthropic', feed: 'Greylock' }
  ],
  source_insights: {
    arxiv: 'ArXiv shows a clear trend: researchers are shifting focus from massive model training to efficient inference. Papers on quantization, distillation, and mixture-of-experts architectures dominate the feed. Multi-agent systems research is accelerating — coordination protocols and planning algorithms are the new frontier. The academic signal suggests we\'re moving from "bigger is better" to "smarter is cheaper".',
    hackernews: 'Hacker News discussions reveal a grassroots revolution: developers are running GPT-3.5-class models on consumer hardware. The quantization tooling (GGUF, GPTQ, AWQ) is maturing fast. There\'s growing skepticism about closed models — the community increasingly believes open source will catch up within 12 months. Voice interfaces (Whisper v3) and local AI agents (AutoGPT clones) are trending hard.',
    reddit: 'Reddit communities (r/MachineLearning, r/LocalLLaMA) are early adopters of bleeding-edge techniques. The Llama 3 hype is real — leaked benchmarks suggest it\'s within 5% of GPT-4. There\'s intense interest in SOTA vision models and multi-modal capabilities. The vibe: open source is winning, and the AI moat is shrinking faster than expected.',
    github: 'GitHub trending repos signal where developers are voting with their time: AutoGen, Whisper v3, and quantization tools dominate. Multi-agent frameworks (LangGraph, CrewAI) are gaining traction. The open-source ecosystem is moving fast — projects go from zero to production-ready in weeks. Key insight: what\'s trending on GitHub today will be a YC batch company in 6 months.',
    rss: 'VC blogs reveal capital allocation patterns: AI infrastructure is the consensus bet. Vector databases, orchestration layers, and monitoring tools are getting funded aggressively. Anthropic, Perplexity, and Character.ai are hot topics. The VC narrative: "picks and shovels" for the AI gold rush. But contrarian take: infrastructure is getting crowded — application layer might be undervalued.'
  }
};

const mockAnalysis = {
  emerging_signals: [
    {
      title: 'Local LLM Quantization Going Mainstream',
      why_it_matters: 'Developers are running GPT-3.5 level models on consumer hardware. This democratizes AI access and reduces cloud dependency.',
      signal_strength: 5,
      sources: ['hackernews', 'reddit', 'github']
    },
    {
      title: 'Multi-Agent Systems Research Accelerating',
      why_it_matters: 'ArXiv shows 3x increase in multi-agent RL papers. AutoGPT-style agents moving from demos to production.',
      signal_strength: 4,
      sources: ['arxiv', 'github']
    },
    {
      title: 'Open Source Catching Up to Closed Models',
      why_it_matters: 'Llama 3 leaked benchmarks show performance within 5% of GPT-4. The moat is shrinking.',
      signal_strength: 5,
      sources: ['reddit', 'hackernews', 'arxiv']
    },
    {
      title: 'VCs Doubling Down on AI Infrastructure',
      why_it_matters: 'Multiple funds announcing AI infra-focused vehicles. The picks-and-shovels play is getting crowded.',
      signal_strength: 3,
      sources: ['rss']
    },
    {
      title: 'Whisper v3 Driving Voice Interface Adoption',
      why_it_matters: 'OpenAI\'s latest speech model enables near-perfect transcription. Voice-first apps becoming viable.',
      signal_strength: 4,
      sources: ['github', 'hackernews']
    }
  ],
  deep_dives: [
    {
      title: 'The Quantization Revolution',
      summary: 'GGUF, GPTQ, AWQ — multiple quantization methods now allow 70B parameter models to run on 24GB VRAM. This changes the economics of AI deployment.',
      why_investigate: 'If cloud costs aren\'t a moat, what is? Companies betting on proprietary models need to rethink strategy.',
      sources: ['github', 'reddit', 'hackernews']
    },
    {
      title: 'Multi-Agent Coordination Breakthroughs',
      summary: 'New papers show agents can negotiate, plan, and execute complex tasks with minimal human intervention. AutoGen, LangGraph, CrewAI all trending.',
      why_investigate: 'This could be the next platform shift — from "chatbot" to "team of agents". Early movers will win.',
      sources: ['arxiv', 'github']
    },
    {
      title: 'AI Infrastructure Gold Rush',
      summary: 'VCs are pouring money into vector databases, orchestration layers, monitoring tools. The middleware layer is getting crowded.',
      why_investigate: 'Which categories are over-funded? Where are the gaps? Understanding the infrastructure map is critical.',
      sources: ['rss', 'hackernews']
    }
  ],
  contrarian_corner: [
    {
      idea: 'Open source will NOT kill proprietary models',
      why_ignored: 'Everyone assumes Llama/Mistral will commoditize LLMs. The narrative is seductive.',
      why_might_matter: 'Proprietary models still lead by 12-18 months. Distribution + trust + reliability matter more than raw capability. OpenAI/Anthropic have moats that aren\'t technical.'
    },
    {
      idea: 'Most AI agent startups will fail',
      why_ignored: 'Hype cycle is at peak. Everyone building AutoGPT clones.',
      why_might_matter: 'Agents are demo-ware. Reliability, error handling, and user trust are unsolved. 90% of current startups won\'t survive contact with production.'
    },
    {
      idea: 'Voice interfaces won\'t replace text',
      why_ignored: 'Whisper v3 hype suggests voice is "the future".',
      why_might_matter: 'Privacy, social context, and precision favor text. Voice is great for cars/kitchens, terrible for offices/public spaces. The "voice-first" bet is overplayed.'
    }
  ],
  cross_source_patterns: [
    {
      pattern: 'Academic Research → GitHub → Product (6-month cycle)',
      sources: ['arxiv', 'github', 'hackernews'],
      significance: 'What\'s in ArXiv today is in GitHub trending in 3 months, and in YC batch announcements in 6 months. Track this pipeline to predict startup ideas.'
    },
    {
      pattern: 'VC interest follows Reddit hype (with 2-week lag)',
      sources: ['reddit', 'rss'],
      significance: 'When r/LocalLLaMA goes crazy about a technique, VCs start writing about it 2 weeks later. Reddit is the leading indicator.'
    },
    {
      pattern: 'Open source stars predict commercial viability',
      sources: ['github', 'hackernews'],
      significance: 'Repos gaining >500 stars/day often become venture-backed companies within 6 months. Early GitHub traction = product-market fit signal.'
    }
  ],
  meta: {
    total_items_analyzed: 243,
    timeframe: 'last 48 hours',
    confidence: 'high'
  }
};

// Render HTML
const reportDate = new Date().toISOString().split('T')[0];
const html = render(mockAnalysis, mockRawData, reportDate);

// Save
const outputDir = path.join(__dirname, 'output');
if (!fs.existsSync(outputDir)) {
  fs.mkdirSync(outputDir, { recursive: true });
}

const outputPath = path.join(outputDir, `research-demo-${reportDate}.html`);
fs.writeFileSync(outputPath, html, 'utf-8');

console.log(`✅ Demo report generated!`);
console.log(`📄 HTML: ${outputPath}`);
console.log('');

// Open in browser (macOS)
if (process.platform === 'darwin') {
  console.log('🌐 Opening in browser...\n');
  const { exec } = await import('child_process');
  exec(`open "${outputPath}"`);
}
