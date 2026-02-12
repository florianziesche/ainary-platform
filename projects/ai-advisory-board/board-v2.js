#!/usr/bin/env node

/**
 * AI Advisory Board v2 - Research-Backed Advisors
 * Flow: Research → Knowledge Structure → Advisors (informed) → Synthesis → Report
 */

const OpenAI = require('openai');
const fs = require('fs');
const path = require('path');
const slugify = require('slugify');
const { runResearch, buildKnowledgeStructure } = require('./research');
const { synthesizeAdvisorResponses, calculateAdvisorConfidence } = require('./synthesis');
const { renderHTML } = require('./renderer-v2');
const { generateDemoData } = require('./demo-data');

// Load advisors
const operator = require('./advisors/operator');
const investor = require('./advisors/investor');
const contrarian = require('./advisors/contrarian');
const technologist = require('./advisors/technologist');
const strategist = require('./advisors/strategist');
const customer = require('./advisors/customer');

const advisors = [operator, investor, contrarian, technologist, strategist, customer];

// Parse CLI arguments
const args = process.argv.slice(2);
const questionParts = args.filter(arg => !arg.startsWith('--'));
const question = questionParts.join(' ');

const mode = args.find(a => a.startsWith('--mode='))?.split('=')[1] || 'research';
const researchDays = parseInt(args.find(a => a.startsWith('--research-days='))?.split('=')[1]) || 2;

// Check for valid OpenAI key
const hasValidKey = process.env.OPENAI_API_KEY && process.env.OPENAI_API_KEY.startsWith('sk-');

async function getAdvisorResponse(advisor, question, knowledgeStructure, openai) {
  try {
    console.log(`   📊 ${advisor.name}...`);
    
    // Enhance system prompt with research context
    const enhancedPrompt = knowledgeStructure && knowledgeStructure.keyFacts.length > 0
      ? `${advisor.systemPrompt}

RESEARCH CONTEXT (recent data):
Key Facts: ${knowledgeStructure.keyFacts.join(' • ')}
Recent Developments: ${knowledgeStructure.recentDevelopments.join(' • ')}
Open Questions: ${knowledgeStructure.openQuestions.join(' • ')}

When relevant, reference this research in your response. If you cite research findings, note it briefly.`
      : advisor.systemPrompt;

    const completion = await openai.chat.completions.create({
      model: 'gpt-4o',
      messages: [
        { role: 'system', content: enhancedPrompt },
        { role: 'user', content: question }
      ],
      temperature: 0.8,
      max_tokens: 500
    });

    return completion.choices[0].message.content;
  } catch (error) {
    console.error(`   ❌ ${advisor.name} error:`, error.message);
    return `Unable to get response from ${advisor.name}`;
  }
}

async function runAdvisoryBoardV2(question, mode, researchDays) {
  console.log('\n🎯 AI Advisory Board v2 — Research-Backed');
  console.log('━'.repeat(60));
  console.log(`Question: "${question}"`);
  console.log(`Mode: ${mode} | Research days: ${researchDays}\n`);

  const startTime = Date.now();
  let researchData = null;
  let knowledgeStructure = null;
  let synthesis = null;

  // Initialize OpenAI
  const openai = new OpenAI({
    apiKey: process.env.OPENAI_API_KEY
  });

  // Phase 1: Research (only in research mode)
  if (mode === 'research') {
    researchData = await runResearch(question, researchDays);
    knowledgeStructure = await buildKnowledgeStructure(question, researchData, openai);
  } else {
    console.log('🔥 Quick mode - skipping research phase\n');
  }

  // Phase 2: Consult Advisors
  console.log('\n👥 Phase 2: Consulting Advisors...');
  
  const responsePromises = advisors.map(advisor => 
    getAdvisorResponse(advisor, question, knowledgeStructure, openai)
  );

  const responses = await Promise.all(responsePromises);
  
  console.log('   ✓ All advisors consulted');

  // Calculate confidence for each advisor
  const confidenceLevels = responses.map(response => 
    calculateAdvisorConfidence(response, knowledgeStructure || { confidence: 'medium' })
  );

  // Phase 3: Synthesis (only in research mode)
  if (mode === 'research' && knowledgeStructure) {
    synthesis = await synthesizeAdvisorResponses(
      question, 
      advisors, 
      responses, 
      knowledgeStructure, 
      openai
    );
  }

  const duration = ((Date.now() - startTime) / 1000).toFixed(1);
  console.log(`\n✅ Advisory session complete in ${duration}s`);

  // Generate HTML
  const html = renderHTML(
    question,
    advisors,
    responses,
    confidenceLevels,
    researchData,
    knowledgeStructure,
    synthesis,
    mode
  );

  // Save output
  const slug = slugify(question, {
    lower: true,
    strict: true,
    remove: /[*+~.()'"!:@]/g
  }).substring(0, 50);

  const outputPath = path.join(__dirname, 'output', `${slug}-v2.html`);
  
  if (!fs.existsSync(path.join(__dirname, 'output'))) {
    fs.mkdirSync(path.join(__dirname, 'output'));
  }

  fs.writeFileSync(outputPath, html);

  console.log('\n━'.repeat(60));
  console.log(`📄 Report: ${outputPath}`);
  console.log('━'.repeat(60));

  // Open in browser (macOS)
  if (process.platform === 'darwin') {
    console.log('🌐 Opening in browser...\n');
    const { exec } = require('child_process');
    exec(`open "${outputPath}"`);
  }

  return outputPath;
}

async function runDemo() {
  console.log('\n🎭 DEMO MODE — No OpenAI key detected');
  console.log('━'.repeat(60));
  console.log('Generating sample report with mock data...\n');

  const demoQuestion = "Should I launch my AI consulting business in Germany or wait until I'm back in NYC?";
  const demoData = generateDemoData(demoQuestion);

  const html = renderHTML(
    demoQuestion,
    demoData.advisors,
    demoData.responses,
    demoData.confidenceLevels,
    demoData.researchData,
    demoData.knowledgeStructure,
    demoData.synthesis,
    'research'
  );

  const outputPath = path.join(__dirname, 'output', 'demo-advisory-board.html');
  
  if (!fs.existsSync(path.join(__dirname, 'output'))) {
    fs.mkdirSync(path.join(__dirname, 'output'));
  }

  fs.writeFileSync(outputPath, html);

  console.log('✅ Demo report generated');
  console.log(`📄 Report: ${outputPath}`);
  console.log('\n💡 To use real AI analysis, set your OpenAI API key:');
  console.log('   export OPENAI_API_KEY=sk-your-key-here\n');

  // Open in browser
  if (process.platform === 'darwin') {
    const { exec } = require('child_process');
    exec(`open "${outputPath}"`);
  }
}

// Main execution
if (!question) {
  console.error('❌ Usage: node board-v2.js "Your question here" [--mode=quick] [--research-days=7]');
  console.error('\nExamples:');
  console.error('  node board-v2.js "Should we raise a Series A or bootstrap?"');
  console.error('  node board-v2.js "Launch in EU or US?" --mode=quick');
  console.error('  node board-v2.js "AI strategy for 2024?" --research-days=7');
  console.error('\n💡 No API key? Run without question for demo mode.');
  
  if (!hasValidKey) {
    console.error('\n🎭 Starting demo mode...');
    runDemo().catch(error => {
      console.error('❌ Demo failed:', error);
      process.exit(1);
    });
  } else {
    process.exit(1);
  }
} else if (!hasValidKey) {
  console.error('❌ Error: OPENAI_API_KEY not set or invalid');
  console.error('Set it with: export OPENAI_API_KEY=sk-your-key-here');
  console.error('\n💡 Or run without question for demo mode.');
  process.exit(1);
} else {
  runAdvisoryBoardV2(question, mode, researchDays).catch(error => {
    console.error('❌ Fatal error:', error);
    process.exit(1);
  });
}
