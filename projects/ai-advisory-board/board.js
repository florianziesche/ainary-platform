#!/usr/bin/env node

/**
 * AI Advisory Board
 * Get 6 expert perspectives on any decision
 */

const OpenAI = require('openai');
const fs = require('fs');
const path = require('path');
const slugify = require('slugify');
const { renderHTML } = require('./renderer');

// Load advisors
const operator = require('./advisors/operator');
const investor = require('./advisors/investor');
const contrarian = require('./advisors/contrarian');
const technologist = require('./advisors/technologist');
const strategist = require('./advisors/strategist');
const customer = require('./advisors/customer');

const advisors = [operator, investor, contrarian, technologist, strategist, customer];

// Initialize OpenAI
const openai = new OpenAI({
  apiKey: process.env.OPENAI_API_KEY
});

async function getAdvisorResponse(advisor, question) {
  try {
    console.log(`📊 Consulting ${advisor.name}...`);
    
    const completion = await openai.chat.completions.create({
      model: 'gpt-4o',
      messages: [
        { role: 'system', content: advisor.systemPrompt },
        { role: 'user', content: question }
      ],
      temperature: 0.8,
      max_tokens: 500
    });

    return completion.choices[0].message.content;
  } catch (error) {
    console.error(`❌ Error consulting ${advisor.name}:`, error.message);
    return `Error: Unable to get response from ${advisor.name}`;
  }
}

async function runAdvisoryBoard(question) {
  console.log('\n🎯 AI Advisory Board');
  console.log('━'.repeat(60));
  console.log(`Question: "${question}"\n`);
  console.log('Consulting 6 advisors in parallel...\n');

  const startTime = Date.now();

  // Run all advisor consultations in parallel
  const responsePromises = advisors.map(advisor => 
    getAdvisorResponse(advisor, question)
  );

  const responses = await Promise.all(responsePromises);

  const duration = ((Date.now() - startTime) / 1000).toFixed(2);
  console.log(`\n✅ All advisors consulted in ${duration}s\n`);

  // Generate HTML output
  const html = renderHTML(question, advisors, responses);
  
  // Create slug for filename
  const slug = slugify(question, {
    lower: true,
    strict: true,
    remove: /[*+~.()'"!:@]/g
  }).substring(0, 50);

  const outputPath = path.join(__dirname, 'output', `${slug}.html`);
  
  // Ensure output directory exists
  if (!fs.existsSync(path.join(__dirname, 'output'))) {
    fs.mkdirSync(path.join(__dirname, 'output'));
  }

  fs.writeFileSync(outputPath, html);

  console.log('━'.repeat(60));
  console.log(`📄 Report generated: ${outputPath}`);
  console.log('━'.repeat(60));
  console.log('\nAdvisor Summary:');
  advisors.forEach((advisor, i) => {
    console.log(`\n${advisor.name} (${advisor.role}):`);
    console.log(responses[i].substring(0, 150) + '...');
  });
  console.log('\n');

  return outputPath;
}

// CLI Usage
const question = process.argv.slice(2).join(' ');

if (!question) {
  console.error('❌ Usage: node board.js "Your question here"');
  console.error('Example: node board.js "Should we raise a Series A or bootstrap?"');
  process.exit(1);
}

if (!process.env.OPENAI_API_KEY) {
  console.error('❌ Error: OPENAI_API_KEY environment variable not set');
  console.error('Set it with: export OPENAI_API_KEY=your-key-here');
  process.exit(1);
}

// Run the advisory board
runAdvisoryBoard(question).catch(error => {
  console.error('❌ Fatal error:', error);
  process.exit(1);
});
