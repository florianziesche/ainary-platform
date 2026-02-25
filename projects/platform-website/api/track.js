// Persistent tracking via /tmp file (survives warm instances, lost on cold start)
// + sends copy to Google Sheet via Apps Script for permanent storage
import { readFileSync, writeFileSync, appendFileSync } from 'fs';

const EVENTS_FILE = '/tmp/ai-track-events.json';
const MAX_EVENTS = 2000;

function loadEvents() {
  try {
    return JSON.parse(readFileSync(EVENTS_FILE, 'utf8'));
  } catch(e) {
    return [];
  }
}

function saveEvent(event) {
  try {
    appendFileSync(EVENTS_FILE, JSON.stringify(event) + '\n');
  } catch(e) {}
}

function allEvents() {
  try {
    const raw = readFileSync(EVENTS_FILE, 'utf8').trim();
    if (!raw) return [];
    return raw.split('\n').map(l => { try { return JSON.parse(l); } catch(e) { return null; } }).filter(Boolean);
  } catch(e) {
    return [];
  }
}

export default function handler(req, res) {
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'GET, POST, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type');
  if (req.method === 'OPTIONS') return res.status(200).end();

  const ip = (req.headers['x-forwarded-for'] || req.headers['x-real-ip'] || 'unknown').split(',')[0].trim();
  const ua = (req.headers['user-agent'] || '').substring(0, 120);

  // GET: return all stored events
  if (req.method === 'GET') {
    const events = allEvents();
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

  saveEvent(event);

  // Also log for vercel logs
  console.log(JSON.stringify({ ...event, ua: ua.substring(0, 60) }));

  res.status(200).json({ ok: true });
}
