/**
 * /api/lead - ontvangt de gewone leadformulieren (hoofdformulier, pop-up,
 * zijpaneel) en stuurt ze pas server-side door naar Zapier.
 *
 * Vervangt de rechtstreekse browser-naar-Zapier POST. Die had twee gevolgen:
 * de Zapier-webhook-URL stond onversleuteld in elke pagina, en er zat geen
 * enkele rate limiting of validatie tussen "wie dit ook post" en de
 * leadsheet. Wie de URL in de paginabron vond, kon rechtstreeks posten en
 * het echte formulier volledig omzeilen.
 *
 * De payload-vorm verandert bewust niet: dezelfde velden, dezelfde Zap.
 * Alleen de bestemming van de fetch() in de browser wijzigt.
 */
const { forwardToZapier } = require('./_zapier.js');

const RATE_MAX = 8;           // verzoeken
const RATE_WINDOW_MS = 60000; // per minuut per IP
// Lager dan bij de chat (12): een bezoeker verstuurt een leadformulier
// hooguit een paar keer per bezoek, nooit tientallen keren per minuut.

const MAX_FIELD_LEN = 200;
const ALLOWED_SOURCES = ['hoofdformulier', 'pop-up', 'zijpaneel', 'projectenoverzicht', 'selectie'];

// UTM-parameters worden alleen doorgegeven als ze er zijn. De projectpagina's
// sturen ze niet mee (die zetten utm_source vast op 'site'); /selectie/ wel,
// want de advertenties die daarheen linken leunen erop.
const UTM_FIELDS = ['utm_source', 'utm_medium', 'utm_campaign', 'utm_term', 'utm_content'];

const hits = new Map();

function rateLimited(ip) {
  const now = Date.now();
  if (hits.size > 5000) hits.clear();
  const record = hits.get(ip);
  if (!record || now - record.start > RATE_WINDOW_MS) {
    hits.set(ip, { start: now, count: 1 });
    return false;
  }
  record.count += 1;
  return record.count > RATE_MAX;
}

function str(value) {
  return String(value || '').slice(0, MAX_FIELD_LEN);
}

module.exports = async (req, res) => {
  if (req.method !== 'POST') {
    res.setHeader('Allow', 'POST');
    return res.status(405).json({ error: 'method_not_allowed' });
  }

  const ip =
    (req.headers['x-forwarded-for'] || '').split(',')[0].trim() || 'unknown';
  if (rateLimited(ip)) {
    return res.status(429).json({ error: 'rate_limited' });
  }

  let body = req.body;
  if (typeof body === 'string') {
    try { body = JSON.parse(body); } catch (e) { body = null; }
  }
  if (!body || typeof body !== 'object') {
    return res.status(400).json({ error: 'bad_request' });
  }

  // Basisvalidatie: geen lege leads doorsturen naar de sheet. Verder houden
  // we dit bewust losjes - het gaat om ruis wegfilteren, niet om een
  // volwaardige formuliervalidatie opnieuw op te bouwen server-side.
  if (!body.email || !body.first_name || !body.last_name) {
    return res.status(400).json({ error: 'missing_fields' });
  }

  const formBron = ALLOWED_SOURCES.includes(body.form_source)
    ? body.form_source
    : 'onbekend';

  const payload = {
    first_name: str(body.first_name),
    last_name: str(body.last_name),
    email: str(body.email),
    mobile_phone: str(body.mobile_phone),
    mobile_phone_unformatted: str(body.mobile_phone_unformatted),
    country: str(body.country),
    utm_source: 'site',
    lead_source: str(body.lead_source) || 'Projectpagina',
    budget: str(body.budget),
    description: `${str(body.project_name)} — ${formBron} — ${str(body.page_url)}`,
    timestamp: new Date().toISOString(),
  };

  // De selectiepagina stuurt de gegeven antwoorden mee. Ze gaan achter de
  // bestaande description aan in plaats van in een nieuw veld, zodat de Zap
  // en de kolommen in de leadsheet ongewijzigd blijven werken.
  const answers = str(body.answers);
  if (answers) payload.description += ` — ${answers}`;
  // description is samengesteld uit meerdere velden en kan zo langer worden
  // dan de limiet die str() per veld bewaakt.
  payload.description = payload.description.slice(0, 600);

  for (const field of UTM_FIELDS) {
    if (body[field]) payload[field] = str(body[field]);
  }

  const ok = await forwardToZapier(payload);
  // Ook bij een mislukte Zap 200 teruggeven: de bezoeker staat al onderweg
  // naar /bedankt/ (keepalive-fetch, geen await in de browser) en moet daar
  // niets van een falende achterliggende integratie merken.
  return res.status(200).json({ ok });
};
