export default function handler(req, res) {
  // CORS
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'POST, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type');
  if (req.method === 'OPTIONS') return res.status(200).end();

  // Accept both sendBeacon (text body) and JSON
  let payload;
  try {
    payload = typeof req.body === 'string' ? JSON.parse(req.body) : req.body;
  } catch(e) {
    payload = { raw: req.body };
  }

  // Log with timestamp — visible in `vercel logs`
  const ts = new Date().toISOString();
  const ip = req.headers['x-forwarded-for'] || req.headers['x-real-ip'] || 'unknown';
  const ua = req.headers['user-agent'] || '';

  console.log(JSON.stringify({
    ts,
    ip,
    ua: ua.substring(0, 100),
    event: payload.e || 'unknown',
    user: payload.u || 'unknown',
    tenant: payload.tn || 'unknown',
    token: payload.tk || '',
    session: payload.s || '',
    data: payload.d || {}
  }));

  res.status(200).json({ ok: true });
}
