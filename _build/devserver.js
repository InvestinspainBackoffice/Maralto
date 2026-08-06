/**
 * Lokale dev-server: serveert de statische site én draait /api/chat, zodat de
 * chatwidget te testen is zonder Vercel CLI of deploy.
 *
 * Staat in _build/ en wordt dus door .vercelignore uitgesloten van de deploy.
 * Emuleert alleen wat de functie werkelijk gebruikt (method, headers, body,
 * res.status().json()) - geen poging tot een volledige Vercel-kloon.
 *
 * Gebruik:  node _build/devserver.js        (mock-modus, geen key nodig)
 *           AI_GATEWAY_API_KEY=... node _build/devserver.js
 */
const http = require('http');
const fs = require('fs');
const path = require('path');

const ROOT = path.join(__dirname, '..');
const PORT = process.env.PORT || 4321;

const TYPES = {
  '.html': 'text/html; charset=utf-8',
  '.css': 'text/css; charset=utf-8',
  '.js': 'text/javascript; charset=utf-8',
  '.json': 'application/json; charset=utf-8',
  '.webp': 'image/webp',
  '.jpg': 'image/jpeg',
  '.png': 'image/png',
  '.svg': 'image/svg+xml',
  '.pdf': 'application/pdf',
  '.ico': 'image/x-icon',
};

function readBody(req) {
  return new Promise((resolve) => {
    let raw = '';
    req.on('data', (c) => { raw += c; });
    req.on('end', () => {
      try { resolve(JSON.parse(raw || '{}')); } catch (e) { resolve(null); }
    });
  });
}

// Minimale Vercel-achtige res: alleen status/json/setHeader worden gebruikt.
function wrapRes(res) {
  res.status = (code) => { res.statusCode = code; return res; };
  res.json = (obj) => {
    res.setHeader('Content-Type', 'application/json; charset=utf-8');
    res.end(JSON.stringify(obj));
    return res;
  };
  return res;
}

const server = http.createServer(async (req, res) => {
  const url = new URL(req.url, `http://localhost:${PORT}`);

  if (url.pathname === '/api/chat') {
    // Elke keer opnieuw inladen, zodat wijzigingen aan chat.js meteen
    // meetellen zonder de server te herstarten.
    delete require.cache[require.resolve('../api/chat.js')];
    delete require.cache[require.resolve('../api/_projects.json')];
    const handler = require('../api/chat.js');
    req.body = await readBody(req);
    try {
      await handler(req, wrapRes(res));
    } catch (err) {
      console.error('[devserver]', err);
      wrapRes(res).status(500).json({ error: 'dev_crash', detail: err.message });
    }
    return;
  }

  let filePath = path.join(ROOT, decodeURIComponent(url.pathname));
  if (fs.existsSync(filePath) && fs.statSync(filePath).isDirectory()) {
    filePath = path.join(filePath, 'index.html');
  }
  if (!filePath.startsWith(ROOT) || !fs.existsSync(filePath)) {
    res.writeHead(404, { 'Content-Type': 'text/plain' });
    return res.end('404');
  }
  res.writeHead(200, {
    'Content-Type': TYPES[path.extname(filePath)] || 'application/octet-stream',
  });
  fs.createReadStream(filePath).pipe(res);
});

server.listen(PORT, () => {
  const mode = process.env.AI_GATEWAY_API_KEY ? 'ECHT MODEL' : 'MOCK (geen key)';
  console.log(`Dev-server op http://localhost:${PORT}  —  chat: ${mode}`);
});
