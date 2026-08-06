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
 *           ALLOW_REAL_ZAPIER=1 node _build/devserver.js   (zie hieronder)
 */
const http = require('http');
const fs = require('fs');
const path = require('path');

const ROOT = path.join(__dirname, '..');
const PORT = process.env.PORT || 4321;

// Standaard NOOIT een echte Zapier-post vanaf de dev-server, ook niet als
// een formulier volledig wordt doorlopen en verstuurd - anders belandt elke
// handmatige test in Gunthers echte leadsheet. Alleen met expliciete
// ALLOW_REAL_ZAPIER=1 wordt dat toegelaten (bv. één laatste live-check vlak
// voor een merge).
if (process.env.ALLOW_REAL_ZAPIER !== '1') {
  process.env.ZAPIER_DRY_RUN = '1';
}

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

  // Elke /api/<naam> (niet beginnend met _) wordt automatisch naar
  // api/<naam>.js geroute - zo hoeft dit bestand niet aangepast te worden
  // wanneer er een nieuwe functie bijkomt.
  var apiMatch = url.pathname.match(/^\/api\/([a-z][a-z0-9-]*)$/);
  if (apiMatch) {
    var fnPath = path.join(ROOT, 'api', apiMatch[1] + '.js');
    if (!fs.existsSync(fnPath)) {
      res.writeHead(404, { 'Content-Type': 'application/json' });
      return res.end(JSON.stringify({ error: 'not_found' }));
    }
    // Elke keer opnieuw inladen, zodat wijzigingen meteen meetellen zonder
    // de server te herstarten. Ook de gedeelde helpers en datasets wissen we
    // uit de cache, anders blijft een oude versie hangen.
    Object.keys(require.cache)
      .filter((k) => k.startsWith(path.join(ROOT, 'api')))
      .forEach((k) => { delete require.cache[k]; });
    const handler = require(fnPath);
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
  const zapier = process.env.ZAPIER_DRY_RUN === '1'
    ? 'DRY-RUN (geen enkele lead verlaat deze machine)'
    : 'LIVE — stuurt écht naar Zapier';
  console.log(`Dev-server op http://localhost:${PORT}  —  chat: ${mode}  —  leads: ${zapier}`);
});
