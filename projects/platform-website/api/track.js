// In-memory event store (persists during warm function instances)
// For production: replace with Vercel KV, Redis, or database
let events = [];
const MAX_EVENTS = 500;

export default function handler(req, res) {
  // CORS
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'GET, POST, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type');
  if (req.method === 'OPTIONS') return res.status(200).end();

  const ip = req.headers['x-forwarded-for'] || req.headers['x-real-ip'] || 'unknown';
  const ua = req.headers['user-agent'] || '';

  // GET: return stored events (for analytics dashboard)
  if (req.method === 'GET') {
    return res.status(200).json({ events: events });
  }

  // POST: store + log event
  let payload;
  try {
    payload = typeof req.body === 'string' ? JSON.parse(req.body) : req.body;
  } catch(e) {
    payload = { raw: req.body };
  }

  const ts = Date.now();
  const event = {
    e: payload.e || 'unknown',
    t: ts,
    ts: ts,
    s: payload.s || '',
    u: payload.u || 'unknown',
    tk: payload.tk || '',
    tn: payload.tn || 'unknown',
    ip: ip.split(',')[0].trim(),
    ua: ua.substring(0, 120),
    d: payload.d || {}
  };

  events.push(event);
  if (events.length > MAX_EVENTS) events = events.slice(-MAX_EVENTS);

  // Also log to Vercel logs
  console.log(JSON.stringify(event));

  res.status(200).json({ ok: true });
}
