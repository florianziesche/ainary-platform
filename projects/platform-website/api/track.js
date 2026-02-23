// Vercel Serverless Function — Event Tracker
// POST /api/track — stores events
// GET /api/track?key=SECRET — retrieves all events

const events = []; // In-memory (resets on cold start, but Vercel KV/Blob would be persistent)
// For persistence, we write to Vercel's /tmp which persists during warm function
const fs = require('fs');
const EVENTS_FILE = '/tmp/ai-events.jsonl';
const SECRET = process.env.TRACK_SECRET || 'ainary2026';

module.exports = async (req, res) => {
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'GET, POST, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type');
  
  if (req.method === 'OPTIONS') {
    return res.status(200).end();
  }

  if (req.method === 'POST') {
    try {
      const body = typeof req.body === 'string' ? req.body : JSON.stringify(req.body);
      const line = JSON.stringify({
        ...JSON.parse(body),
        ip: (req.headers['x-forwarded-for'] || req.socket?.remoteAddress || '').split(',')[0].trim(),
        ua: req.headers['user-agent'] || '',
        ts: Date.now()
      }) + '\n';
      fs.appendFileSync(EVENTS_FILE, line);
      return res.status(200).json({ ok: true });
    } catch (e) {
      return res.status(400).json({ error: e.message });
    }
  }

  if (req.method === 'GET') {
    // Auth check
    if (req.query.key !== SECRET) {
      return res.status(401).json({ error: 'unauthorized' });
    }

    try {
      const raw = fs.existsSync(EVENTS_FILE) ? fs.readFileSync(EVENTS_FILE, 'utf8') : '';
      const lines = raw.trim().split('\n').filter(Boolean);
      const events = lines.map(l => { try { return JSON.parse(l); } catch(e) { return null; } }).filter(Boolean);
      
      // Build summary
      const sessions = {};
      for (const evt of events) {
        const sid = evt.s || 'unknown';
        if (!sessions[sid]) sessions[sid] = { user: evt.u, tenant: evt.tn, start: evt.t, events: [], tabs: {}, entities: [], copies: 0 };
        sessions[sid].events.push(evt);
        if (evt.e === 'tab_enter') sessions[sid].tabs[evt.d?.tab] = (sessions[sid].tabs[evt.d?.tab] || 0) + 1;
        if (evt.e === 'entity_view') sessions[sid].entities.push(evt.d?.name);
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
        talking_points_copied: s.copies
      }));

      const format = req.query.format;
      if (format === 'raw') {
        return res.status(200).json({ total: events.length, events });
      }
      
      return res.status(200).json({
        total_events: events.length,
        total_sessions: Object.keys(sessions).length,
        sessions: summary,
        last_event: events.length > 0 ? events[events.length - 1] : null
      });
    } catch (e) {
      return res.status(500).json({ error: e.message });
    }
  }

  return res.status(405).json({ error: 'method not allowed' });
};
