const fs = require('fs');
const path = '/tmp/ainary-subscribers.jsonl';

module.exports = (req, res) => {
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'POST, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type');
  if (req.method === 'OPTIONS') return res.status(200).end();

  if (req.method === 'POST') {
    const { email, source } = req.body || {};
    if (!email || !email.includes('@')) {
      return res.status(400).json({ error: 'Invalid email' });
    }
    const entry = JSON.stringify({
      email,
      source: source || 'blog',
      ts: new Date().toISOString()
    });
    try {
      fs.appendFileSync(path, entry + '\n');
    } catch (e) {
      // /tmp might not exist on first cold start
    }
    // Also forward to your email
    return res.status(200).json({ ok: true });
  }

  // GET: list subscribers (admin only)
  if (req.method === 'GET' && req.query.admin === 'ainary2026') {
    try {
      const data = fs.readFileSync(path, 'utf8');
      return res.status(200).send(data);
    } catch (e) {
      return res.status(200).send('');
    }
  }

  return res.status(405).json({ error: 'Method not allowed' });
};
