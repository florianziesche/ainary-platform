#!/usr/bin/env node
/**
 * ♔ Mia Mission Control — Live WebSocket Server
 * 
 * Reads OpenClaw session logs, cost data, and system health in real-time.
 * Pushes updates to the dashboard via WebSocket.
 * 
 * Usage: node server.js [--port 3333]
 */

const http = require('http');
const fs = require('fs');
const path = require('path');
const { execSync, spawn } = require('child_process');
const crypto = require('crypto');
const os = require('os');

const PORT = parseInt(process.argv.find((a,i) => process.argv[i-1] === '--port') || '3333');
const HOME = os.homedir();
const WORKSPACE = path.join(HOME, '.openclaw/workspace');
const SESSIONS_DIR = path.join(HOME, '.openclaw/agents/main/sessions');
const LOGS_DIR = path.join(HOME, '.openclaw/logs');
const MEMORY_DIR = path.join(WORKSPACE, 'memory');
const INTEL_DIR = path.join(HOME, 'ainary-tools');

// ─── WebSocket Server (raw, no deps) ────────────────────────

const clients = new Set();

function broadcast(data) {
  const msg = JSON.stringify(data);
  for (const ws of clients) {
    try { ws.send(msg); } catch(e) { clients.delete(ws); }
  }
}

class SimpleWS {
  constructor(socket) {
    this.socket = socket;
    this.alive = true;
    socket.on('data', buf => this._onData(buf));
    socket.on('close', () => { this.alive = false; clients.delete(this); });
    socket.on('error', () => { this.alive = false; clients.delete(this); });
  }
  
  send(data) {
    if (!this.alive) return;
    const buf = Buffer.from(data);
    let header;
    if (buf.length < 126) {
      header = Buffer.alloc(2);
      header[0] = 0x81;
      header[1] = buf.length;
    } else if (buf.length < 65536) {
      header = Buffer.alloc(4);
      header[0] = 0x81;
      header[1] = 126;
      header.writeUInt16BE(buf.length, 2);
    } else {
      header = Buffer.alloc(10);
      header[0] = 0x81;
      header[1] = 127;
      header.writeBigUInt64BE(BigInt(buf.length), 2);
    }
    this.socket.write(Buffer.concat([header, buf]));
  }
  
  _onData(buf) {
    // Decode WebSocket frame
    if (buf.length < 2) return;
    const opcode = buf[0] & 0x0f;
    if (opcode === 0x08) { this.alive = false; this.socket.end(); return; }
    if (opcode === 0x0a || opcode === 0x09) return; // pong/ping
    
    const masked = (buf[1] & 0x80) !== 0;
    let len = buf[1] & 0x7f;
    let offset = 2;
    if (len === 126) { len = buf.readUInt16BE(2); offset = 4; }
    else if (len === 127) { len = Number(buf.readBigUInt64BE(2)); offset = 10; }
    
    if (masked) {
      const mask = buf.slice(offset, offset + 4);
      offset += 4;
      const payload = buf.slice(offset, offset + len);
      for (let i = 0; i < payload.length; i++) payload[i] ^= mask[i % 4];
      // Handle incoming messages if needed
      try {
        const msg = JSON.parse(payload.toString());
        this._onMessage(msg);
      } catch(e) {}
    }
  }
  
  _onMessage(msg) {
    // Handle client requests
    if (msg.type === 'refresh') collectAndBroadcast();
  }
}

// ─── Data Collection ─────────────────────────────────────────

function safeExec(cmd, defaultVal = '') {
  try { return execSync(cmd, { timeout: 5000, encoding: 'utf8' }).trim(); } 
  catch(e) { return defaultVal; }
}

function getSessionsData() {
  const sessions = [];
  try {
    // Read from OpenClaw status
    const statusRaw = safeExec('openclaw status --json 2>/dev/null') || '{}';
    // Fallback: scan session files
    const sessionFiles = fs.readdirSync(SESSIONS_DIR).filter(f => f.endsWith('.jsonl') && !f.includes('.deleted') && !f.includes('.reset')).slice(-20);
    
    for (const file of sessionFiles) {
      const fullPath = path.join(SESSIONS_DIR, file);
      const stat = fs.statSync(fullPath);
      const lines = safeExec(`tail -5 "${fullPath}" 2>/dev/null`).split('\n').filter(Boolean);
      
      let lastMsg = '';
      let model = 'unknown';
      let role = 'unknown';
      for (const line of lines.reverse()) {
        try {
          const obj = JSON.parse(line);
          if (obj.role === 'assistant' && !lastMsg) {
            lastMsg = (obj.content || '').slice(0, 100);
          }
          if (obj.model) model = obj.model;
          if (obj.metadata?.channel) role = obj.metadata.channel;
        } catch(e) {}
      }
      
      const ageMs = Date.now() - stat.mtimeMs;
      const isActive = ageMs < 300000; // 5 min
      
      sessions.push({
        id: file.replace('.jsonl', '').slice(0, 12),
        file: file,
        lastActivity: stat.mtime.toISOString(),
        ageMs,
        active: isActive,
        model,
        channel: role,
        lastMessage: lastMsg,
        sizeKB: Math.round(stat.size / 1024)
      });
    }
    
    sessions.sort((a, b) => a.ageMs - b.ageMs);
  } catch(e) {}
  return sessions;
}

function getCostData() {
  // Parse gateway log for today's model usage to estimate costs
  const today = new Date().toISOString().slice(5, 10); // MM-DD
  const todayShort = new Date().toLocaleDateString('de-DE', { day: '2-digit', month: '2-digit' });
  
  try {
    // Count model calls from gateway log
    const logLines = safeExec(`grep "agent model" ${HOME}/.openclaw/logs/gateway.log 2>/dev/null | tail -50`);
    const modelCounts = {};
    let todayCalls = 0;
    for (const line of logLines.split('\n')) {
      if (!line) continue;
      const modelMatch = line.match(/agent model: (.+)/);
      if (modelMatch) {
        const model = modelMatch[1];
        modelCounts[model] = (modelCounts[model] || 0) + 1;
        todayCalls++;
      }
    }
    
    // Rough cost estimate (based on typical Opus session costs)
    // Opus 4: ~$0.15 per 1K input tokens, ~$0.60 per 1K output tokens
    // Average session: ~20K input + 5K output ≈ $6 per session
    const activeSessions = getSessionsData().filter(s => s.active).length;
    const estimatedDailyCost = todayCalls * 0.5; // rough per-call estimate
    
    return {
      today: { 
        total: Math.round(estimatedDailyCost * 100) / 100,
        calls: todayCalls,
        byModel: modelCounts
      },
      source: 'gateway-log-estimate'
    };
  } catch(e) {}
  
  return { today: { total: 0, calls: 0, byModel: {} }, source: 'unavailable' };
}

function getMemoryFiles() {
  const files = [];
  const scanDir = (dir, prefix = '') => {
    try {
      for (const f of fs.readdirSync(dir)) {
        const full = path.join(dir, f);
        const stat = fs.statSync(full);
        if (stat.isFile() && f.endsWith('.md')) {
          files.push({
            name: prefix + f,
            path: full,
            modified: stat.mtime.toISOString(),
            ageMs: Date.now() - stat.mtimeMs,
            sizeKB: Math.round(stat.size / 1024)
          });
        } else if (stat.isDirectory() && !f.startsWith('.')) {
          scanDir(full, prefix + f + '/');
        }
      }
    } catch(e) {}
  };
  
  // Core files
  for (const f of ['SOUL.md', 'USER.md', 'AGENTS.md', 'MEMORY.md']) {
    const full = path.join(WORKSPACE, f);
    try {
      const stat = fs.statSync(full);
      files.push({ name: f, path: full, modified: stat.mtime.toISOString(), ageMs: Date.now() - stat.mtimeMs, sizeKB: Math.round(stat.size / 1024), core: true });
    } catch(e) {}
  }
  
  scanDir(MEMORY_DIR, 'memory/');
  files.sort((a, b) => a.ageMs - b.ageMs);
  return files;
}

let _intelCache = null;
let _intelCacheTime = 0;

function getIntelStatus() {
  // Cache for 60s — pip list is slow
  if (_intelCache && Date.now() - _intelCacheTime < 60000) return _intelCache;
  
  const tools = [];
  const venvPkgs = safeExec(`${INTEL_DIR}/bin/pip list --format=json 2>/dev/null`, '[]');
  let pkgList = [];
  try { pkgList = JSON.parse(venvPkgs); } catch(e) {}
  const pkgNames = new Set(pkgList.map(p => p.name.toLowerCase()));
  
  const checks = [
    { name: 'Bundesanzeiger', pkg: 'deutschland', cmd: null },
    { name: 'Crawl4AI', pkg: 'crawl4ai', cmd: null },
    { name: 'GPT-Researcher', pkg: 'gpt-researcher', cmd: null },
    { name: 'Graphiti', pkg: 'graphiti-core', cmd: null },
    { name: 'Cognee', pkg: 'cognee', cmd: null },
    { name: 'LightRAG', pkg: 'lightrag-hku', cmd: null },
    { name: 'browser-use', pkg: 'browser-use', cmd: null },
    { name: 'Scrapling', pkg: 'scrapling', cmd: null },
    { name: 'Handelsregister', pkg: 'handelsregister', cmd: null },
  ];
  
  for (const c of checks) {
    const installed = pkgNames.has(c.pkg);
    tools.push({ name: c.name, status: installed ? 'ready' : 'missing', pkg: c.pkg });
  }
  
  // Docker services
  const dockerRunning = safeExec('docker ps --format "{{.Names}}" 2>/dev/null');
  tools.push({ 
    name: 'ChangeDetection', 
    status: dockerRunning.includes('changedetection') ? 'ready' : 'docker-pending',
    docker: true
  });
  tools.push({ 
    name: 'Twenty CRM', 
    status: dockerRunning.includes('twenty') ? 'ready' : 'docker-pending',
    docker: true 
  });
  
  // offeneregister data
  const dataFile = path.join(INTEL_DIR, 'data/de_companies.jsonl.bz2');
  let dataSize = 0;
  try { dataSize = fs.statSync(dataFile).size; } catch(e) {}
  tools.push({ name: 'offeneregister', status: dataSize > 0 ? 'partial' : 'missing', sizeMB: Math.round(dataSize / 1048576) });
  
  _intelCache = tools;
  _intelCacheTime = Date.now();
  return tools;
}

function getSystemHealth() {
  const loadAvg = os.loadavg();
  const totalMem = os.totalmem();
  const freeMem = os.freemem();
  const usedPct = Math.round((1 - freeMem / totalMem) * 100);
  
  // Disk space
  const diskInfo = safeExec("df -h / | tail -1 | awk '{print $5}'", '?%');
  
  // Gateway status
  const gwStatus = safeExec('openclaw gateway status 2>/dev/null', 'unknown');
  
  return {
    cpuLoad: loadAvg,
    memoryUsedPct: usedPct,
    memoryFreeGB: Math.round(freeMem / 1073741824 * 10) / 10,
    memoryTotalGB: Math.round(totalMem / 1073741824 * 10) / 10,
    diskUsed: diskInfo,
    gateway: gwStatus.includes('running') ? 'running' : gwStatus.includes('stopped') ? 'stopped' : 'unknown',
    uptime: Math.round(os.uptime() / 3600) + 'h',
    platform: os.platform(),
    hostname: os.hostname()
  };
}

function getRecentFeed() {
  const feed = [];
  try {
    const allFiles = fs.readdirSync(SESSIONS_DIR)
      .filter(f => f.endsWith('.jsonl') && !f.includes('.deleted') && !f.includes('.reset') && f !== 'sessions.json');
    
    const files = allFiles
      .map(f => { try { return { name: f, mtime: fs.statSync(path.join(SESSIONS_DIR, f)).mtimeMs }; } catch(e) { return null; } })
      .filter(Boolean)
      .sort((a, b) => b.mtime - a.mtime)
      .slice(0, 5);
    
    for (const file of files) {
      // Read last 8KB instead of shelling out
      const fullPath = path.join(SESSIONS_DIR, file.name);
      try {
        const stat = fs.statSync(fullPath);
        const readSize = Math.min(stat.size, 8192);
        const fd = fs.openSync(fullPath, 'r');
        const buf = Buffer.alloc(readSize);
        fs.readSync(fd, buf, 0, readSize, Math.max(0, stat.size - readSize));
        fs.closeSync(fd);
        
        const text = buf.toString('utf8');
        const lines = text.split('\n').filter(Boolean);
        
        for (const line of lines) {
          try {
            // Skip incomplete first line from mid-read
            if (!line.startsWith('{')) continue;
            const obj = JSON.parse(line);
            if (obj.role === 'assistant' && obj.content) {
              let msg = obj.content.replace(/[#*_`\[\]]/g, '').replace(/\n+/g, ' ').trim();
              // Skip tool results and very long outputs
              if (msg.length < 10 || msg.length > 500) continue;
              msg = msg.slice(0, 120);
              
              feed.push({
                time: obj.timestamp || new Date(file.mtime).toISOString(),
                agent: obj.metadata?.agent || '♔ Main',
                message: msg,
                session: file.name.slice(0, 8)
              });
            }
          } catch(e) {}
        }
      } catch(e) {}
    }
    
    feed.sort((a, b) => new Date(b.time) - new Date(a.time));
  } catch(e) {}
  return feed.slice(0, 20);
}

function collectAll() {
  return {
    type: 'state',
    timestamp: new Date().toISOString(),
    sessions: getSessionsData(),
    costs: getCostData(),
    memory: getMemoryFiles(),
    intel: getIntelStatus(),
    health: getSystemHealth(),
    feed: getRecentFeed()
  };
}

function collectAndBroadcast() {
  const state = collectAll();
  broadcast(state);
}

// ─── File Watcher ────────────────────────────────────────────

let watchDebounce = null;
function setupWatchers() {
  const watchDirs = [SESSIONS_DIR, LOGS_DIR].filter(d => { try { fs.accessSync(d); return true; } catch(e) { return false; } });
  
  for (const dir of watchDirs) {
    try {
      fs.watch(dir, { persistent: false }, (eventType, filename) => {
        if (watchDebounce) clearTimeout(watchDebounce);
        watchDebounce = setTimeout(() => {
          collectAndBroadcast();
        }, 1000);
      });
    } catch(e) {}
  }
}

// ─── HTTP + WS Server ────────────────────────────────────────

const DASHBOARD_DIR = __dirname;

const MIME = {
  '.html': 'text/html',
  '.js': 'application/javascript',
  '.css': 'text/css',
  '.json': 'application/json',
  '.png': 'image/png',
  '.jpg': 'image/jpeg',
  '.svg': 'image/svg+xml',
};

const server = http.createServer((req, res) => {
  // API endpoints
  if (req.url === '/api/state') {
    res.writeHead(200, { 'Content-Type': 'application/json', 'Access-Control-Allow-Origin': '*' });
    res.end(JSON.stringify(collectAll()));
    return;
  }
  
  if (req.url === '/api/memory' && req.method === 'GET') {
    const memoryFiles = getMemoryFiles();
    res.writeHead(200, { 'Content-Type': 'application/json', 'Access-Control-Allow-Origin': '*' });
    res.end(JSON.stringify(memoryFiles));
    return;
  }
  
  if (req.url.startsWith('/api/memory/read?')) {
    const filePath = new URL(req.url, 'http://localhost').searchParams.get('path');
    if (filePath && filePath.includes('.md') && !filePath.includes('..')) {
      try {
        const content = fs.readFileSync(filePath, 'utf8');
        res.writeHead(200, { 'Content-Type': 'text/plain', 'Access-Control-Allow-Origin': '*' });
        res.end(content);
        return;
      } catch(e) {}
    }
    res.writeHead(404); res.end('Not found');
    return;
  }
  
  // Static files
  let filePath = req.url === '/' ? '/index.html' : req.url;
  filePath = path.join(DASHBOARD_DIR, filePath);
  
  // Security: no path traversal
  if (!filePath.startsWith(DASHBOARD_DIR)) {
    res.writeHead(403); res.end('Forbidden');
    return;
  }
  
  const ext = path.extname(filePath);
  const contentType = MIME[ext] || 'text/plain';
  
  try {
    const content = fs.readFileSync(filePath);
    res.writeHead(200, { 'Content-Type': contentType });
    res.end(content);
  } catch(e) {
    res.writeHead(404);
    res.end('Not found');
  }
});

// WebSocket upgrade
server.on('upgrade', (req, socket, head) => {
  if (req.url !== '/ws') {
    socket.destroy();
    return;
  }
  
  const key = req.headers['sec-websocket-key'];
  const acceptKey = crypto
    .createHash('sha1')
    .update(key + '258EAFA5-E914-47DA-95CA-5AB5DC11650A')
    .digest('base64');
  
  socket.write(
    'HTTP/1.1 101 Switching Protocols\r\n' +
    'Upgrade: websocket\r\n' +
    'Connection: Upgrade\r\n' +
    `Sec-WebSocket-Accept: ${acceptKey}\r\n` +
    '\r\n'
  );
  
  const ws = new SimpleWS(socket);
  clients.add(ws);
  
  // Send initial state
  ws.send(JSON.stringify(collectAll()));
});

server.listen(PORT, () => {
  console.log(`♔ Mia Mission Control`);
  console.log(`  Dashboard: http://localhost:${PORT}`);
  console.log(`  WebSocket: ws://localhost:${PORT}/ws`);
  console.log(`  API:       http://localhost:${PORT}/api/state`);
  console.log(`  Watching:  ${SESSIONS_DIR}`);
  setupWatchers();
  
  // Periodic broadcast every 30s
  setInterval(collectAndBroadcast, 30000);
});
