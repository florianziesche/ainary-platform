import OpenAI from 'openai';

const client = new OpenAI();

export async function callOpenAI(systemPrompt, userPrompt, { json = false, model = 'gpt-4o', temperature = 0.7 } = {}) {
  const opts = {
    model,
    temperature,
    messages: [
      { role: 'system', content: systemPrompt },
      { role: 'user', content: userPrompt }
    ]
  };
  if (json) opts.response_format = { type: 'json_object' };

  for (let attempt = 1; attempt <= 3; attempt++) {
    try {
      const res = await client.chat.completions.create(opts);
      const text = res.choices[0].message.content;
      return json ? JSON.parse(text) : text;
    } catch (e) {
      log('API', `Attempt ${attempt} failed: ${e.message}`);
      if (attempt === 3) throw e;
      await new Promise(r => setTimeout(r, 2000 * attempt));
    }
  }
}

export function slugify(name) {
  return name.toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/(^-|-$)/g, '');
}

export function log(phase, message) {
  const time = new Date().toLocaleTimeString('en-US', { hour12: false });
  console.log(`[${time}] ◎ ${phase}: ${message}`);
}
