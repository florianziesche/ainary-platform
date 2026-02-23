// Vercel Serverless — Event Tracker with GitHub Gist persistence
// POST /api/track — appends event to Gist
// GET /api/track?key=SECRET — reads all events from Gist

const GIST_ID = '71ddbcd93985b7c1961b12a5800f16c9';
const GIST_FILE = 'events.jsonl';
const SECRET = process.env.TRACK_SECRET || 'ainary2026';
const GH_TOKEN = process.env.GH_TOKEN;

async function getGist() {
  const res = await fetch(`https://api.github.com/gists/${GIST_ID}`, {
    headers: { 'Authorization': `token ${GH_TOKEN}`, 'Accept': 'application/vnd.github.v3+json' }
  });
  const data = await res.json();
  return (data.files && data.files[GIST_FILE]) ? data.files[GIST_FILE].content : '';
}

async function appendToGist(line) {
  const current = await getGist();
  const updated = current + line + '\n';
  await fetch(`https://api.github.com/gists/${GIST_ID}`, {
    method: 'PATCH',
    headers: { 'Authorization': `token ${GH_TOKEN}`, 'Accept': 'application/vnd.github.v3+json', 'Content-Type': 'application/json' },
    body: JSON.stringify({ files: { [GIST_FILE]: { content: updated } } })
  });
}

module.exports = async (req, res) => {
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'GET, POST, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type');

  if (req.method === 'OPTIONS') return res.status(200).end();

  if (req.method === 'POST') {
    try {
      const body = typeof req.body === 'string' ? JSON.parse(req.body) : req.body;
      const enriched = {
        ...body,
        ip: (req.headers['x-forwarded-for'] || '').split(',')[0].trim(),
        ua: req.headers['user-agent'] || '',
        ts: Date.now()
      };
      await appendToGist(JSON.stringify(enriched));
      return res.status(200).json({ ok: true });
    } catch (e) {
      return res.status(400).json({ error: e.message });
    }
  }

  if (req.method === 'GET') {
    if (req.query.key !== SECRET) return res.status(401).json({ error: 'unauthorized' });
    try {
      const raw = await getGist();
      const lines = raw.trim().split('\n').filter(Boolean);
      const events = lines.map(l => { try { return JSON.parse(l); } catch(e) { return null; } }).filter(Boolean);
      
      // Build sessions
      const sessions = {};
      for (const evt of events) {
        const sid = evt.s || 'unknown';
        if (!sessions[sid]) sessions[sid] = { user: evt.u, tenant: evt.tn, start: evt.ts || evt.t, ip: evt.ip, ua: evt.ua, events: [], tabs: {}, entities: [], copies: 0 };
        sessions[sid].events.push(evt);
        if (evt.e === 'tab_enter') sessions[sid].tabs[evt.d?.tab] = (sessions[sid].tabs[evt.d?.tab] || 0) + 1;
        if (evt.e === 'entity_view') sessions[sid].entities.push(evt.d?.name || evt.d?.entity);
        if (evt.e === 'copy_talking_point') sessions[sid].copies++;
        if (evt.e === 'session_end') sessions[sid].duration_ms = evt.d?.duration_ms;
      }

      const summary = Object.entries(sessions).map(([sid, s]) => ({
        session: sid,
        user: s.user,
        tenant: s.tenant,
        started: new Date(s.start).toISOString(),
        duration: s.duration_ms ? Math.round(s.duration_ms / 1000) + 's' : 'active',
        event_count: s.events.length,
        tabs: s.tabs,
        entities_viewed: [...new Set(s.entities)],
        talking_points_copied: s.copies,
        ip: s.ip
      }));

      if (req.query.format === 'raw') return res.status(200).json({ total: events.length, events });
      return res.status(200).json({ total_events: events.length, total_sessions: Object.keys(sessions).length, sessions: summary });
    } catch (e) {
      return res.status(500).json({ error: e.message });
    }
  }

  return res.status(405).json({ error: 'method not allowed' });
};
