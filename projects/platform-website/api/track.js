// Persistent tracking via Upstash Redis (survives cold starts)
const KV_URL = process.env.KV_REST_API_URL;
const KV_TOKEN = process.env.KV_REST_API_TOKEN;
const MAX_EVENTS = 5000;
const LIST_KEY = 'track:events';

async function redisFetch(cmd) {
  const resp = await fetch(`${KV_URL}`, {
    method: 'POST',
    headers: { Authorization: `Bearer ${KV_TOKEN}`, 'Content-Type': 'application/json' },
    body: JSON.stringify(cmd),
  });
  return resp.json();
}

async function pushEvent(event) {
  // RPUSH + LTRIM to cap at MAX_EVENTS
  await redisFetch(['RPUSH', LIST_KEY, JSON.stringify(event)]);
  await redisFetch(['LTRIM', LIST_KEY, -MAX_EVENTS, -1]);
}

async function getEvents(limit = 500) {
  const res = await redisFetch(['LRANGE', LIST_KEY, -limit, -1]);
  return (res.result || []).map(s => { try { return JSON.parse(s); } catch(e) { return null; } }).filter(Boolean);
}

export default async function handler(req, res) {
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'GET, POST, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type');
  if (req.method === 'OPTIONS') return res.status(200).end();

  if (!KV_URL || !KV_TOKEN) {
    return res.status(500).json({ error: 'Redis not configured' });
  }

  const ip = (req.headers['x-forwarded-for'] || req.headers['x-real-ip'] || 'unknown').split(',')[0].trim();
  const ua = (req.headers['user-agent'] || '').substring(0, 120);

  // GET: return stored events
  if (req.method === 'GET') {
    const limit = parseInt(req.query.limit) || 500;
    const events = await getEvents(limit);
    return res.status(200).json({ events, count: events.length });
  }

  // POST: store event
  let payload;
  try {
    payload = typeof req.body === 'string' ? JSON.parse(req.body) : req.body;
  } catch(e) {
    payload = { raw: req.body };
  }

  const event = {
    e: payload.e || 'unknown',
    t: Date.now(),
    ts: Date.now(),
    s: payload.s || '',
    u: payload.u || 'unknown',
    tk: payload.tk || '',
    tn: payload.tn || 'unknown',
    ip,
    ua,
    d: payload.d || {}
  };

  await pushEvent(event);
  console.log(JSON.stringify({ ...event, ua: ua.substring(0, 60) }));

  res.status(200).json({ ok: true });
}
