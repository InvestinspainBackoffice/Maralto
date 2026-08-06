/**
 * /api/chat - gespreksendpoint voor de AI-chatwidget.
 *
 * Vercel pikt deze map zero-config op als serverless functie, ook in een repo
 * zonder build-pipeline. Bewust dependency-vrij (native fetch, CommonJS), zodat
 * er geen package.json en npm-install bijkomen.
 *
 * Twee dingen die hier bewust server-side gebeuren:
 *  - De projectkennis komt uit _projects.json, niet uit de pagina. De browser
 *    stuurt alleen een slug mee, dus een bezoeker kan de context niet
 *    herschrijven om de bot iets te laten beweren.
 *  - De lead gaat rechtstreeks naar Zapier vanaf de server. Het GA4-event
 *    blijft client-side, want dat hangt aan de bestaande cookie-consent.
 *
 * Zonder AI_GATEWAY_API_KEY draait alles in mock-modus: dan antwoordt de
 * functie met echte projectdata maar zonder model, zodat de widget gratis
 * te bouwen en te beoordelen is.
 */
const DATA = require('./_projects.json');

const GATEWAY_URL = 'https://ai-gateway.vercel.sh/v1/chat/completions';
const MODEL = process.env.AI_MODEL || 'anthropic/claude-haiku-4.5';
const ZAPIER_LEAD_URL = 'https://hooks.zapier.com/hooks/catch/8344712/44ei8hj/';
// Optioneel: aparte Zap voor gesprekslogging. Niet gezet = geen logging.
const ZAPIER_CHATLOG_URL = process.env.ZAPIER_CHATLOG_URL || '';

const MAX_MESSAGES = 24;      // ~12 beurten, daarna vriendelijk afronden
const MAX_CHARS = 1500;       // per bericht
const MAX_TOKENS = 400;       // kort houden: het is een chatvenster
const RATE_MAX = 12;          // verzoeken
const RATE_WINDOW_MS = 60000; // per minuut per IP

/* ── Rate limiting ────────────────────────────────────────────────────────
   Bewust in-memory: geen extra dienst, geen key, geen kosten. Instances zijn
   kortlevend en er draaien er meerdere, dus dit is een drempel tegen
   toevallig misbruik - niet de echte bescherming. Dat is de spend limit op
   de Gateway-key; die is een hard plafond dat hoe dan ook standhoudt. */
const hits = new Map();

function rateLimited(ip) {
  const now = Date.now();
  if (hits.size > 5000) hits.clear(); // noodrem tegen geheugengroei
  const record = hits.get(ip);
  if (!record || now - record.start > RATE_WINDOW_MS) {
    hits.set(ip, { start: now, count: 1 });
    return false;
  }
  record.count += 1;
  return record.count > RATE_MAX;
}

/* ── Kennisbasis ─────────────────────────────────────────────────────── */

function projectContext(slug, lang) {
  const entry = DATA.projects[slug];
  if (!entry) return null;
  const p = entry[lang] || entry.nl;
  if (!p) return null;

  const lines = [
    `Project: ${p.name}`,
    `Locatie: ${p.location}`,
    `Prijs: ${p.price}`,
    `Pagina: ${p.url}`,
  ];
  if (p.stats.length) lines.push(`Kerncijfers: ${p.stats.join(' | ')}`);
  if (p.amenities.length) lines.push(`Faciliteiten: ${p.amenities.join(', ')}`);
  if (p.location_facts.length) lines.push(`Afstanden: ${p.location_facts.join(' | ')}`);
  for (const s of p.sections) {
    lines.push(`\n## ${s.heading}\n${s.text}`);
  }
  return lines.join('\n');
}

/* Compacte index van het hele aanbod, zodat de bot kan doorverwijzen naar een
   ander project ("goedkoper", "wel met zeezicht"). Eén regel per project houdt
   dit rond de 2k tokens - klein genoeg om bij elk gesprek mee te sturen. */
let indexCache = null;

function projectIndex(lang) {
  if (indexCache && indexCache.lang === lang) return indexCache.text;
  const rows = [];
  for (const entry of Object.values(DATA.projects)) {
    const p = entry[lang] || entry.nl;
    if (p) rows.push(`${p.name} | ${p.location} | ${p.price} | ${p.url}`);
  }
  rows.sort();
  const text = rows.join('\n');
  indexCache = { lang, text };
  return text;
}

/* ── Systeemprompt ───────────────────────────────────────────────────── */

function systemPrompt(slug, lang) {
  const context = projectContext(slug, lang);
  const taal = lang === 'en' ? 'English' : 'Nederlands';

  return `Je bent de digitale assistent van INVESTINSPAIN.BE, een Belgisch
makelaarskantoor gespecialiseerd in nieuwbouwvastgoed aan de Spaanse Costa del Sol.
Je staat op de projectpagina hieronder en helpt bezoekers die overwegen te kopen.

ANTWOORD ALTIJD IN HET ${taal.toUpperCase()}.

STIJL
- Kort en concreet. Dit is een chatvenster, geen brochure: 2 tot 4 zinnen per antwoord.
- Warm en professioneel, zoals een ervaren makelaar. Geen verkooppraat, geen uitroeptekens.
- Stel één vervolgvraag als dat het gesprek vooruithelpt.

WAT JE ZEKER WEET
Alleen wat hieronder staat. Verzin nooit prijzen, oppervlaktes, opleverdata,
beschikbaarheid of aantallen die er niet staan. Weet je iets niet, zeg dat dan
en bied aan dat Gunther het uitzoekt. Dat is altijd een beter antwoord dan gokken.

ANDERE PROJECTEN
Past dit project niet bij wat iemand zoekt, verwijs dan naar een passend project
uit de lijst onderaan, met naam, locatie, vanaf-prijs en link. Doe dat hooguit
twee of drie projecten tegelijk.

KOPEN IN SPANJE
Je mag algemene oriëntatie geven over het aankoopproces: NIE-nummer, notaris,
overdrachtsbelasting, bijkomende kosten, verloop van een nieuwbouwaankoop.
Houd het op hoofdlijnen en zeg er altijd bij dat het afhangt van de persoonlijke
situatie. Geef nooit fiscaal, juridisch of hypotheekadvies als vaststaand feit,
noem nooit concrete percentages als zekerheid, en beloof nooit rendement of
waardestijging. Bij dat soort vragen verwijs je door naar Gunther.

LEADS
Zodra iemand echte interesse toont - vraagt naar plattegronden, prijslijst,
beschikbaarheid, een bezoek - bied dan aan de volledige informatie te laten
opsturen. Vraag voornaam, achternaam, e-mailadres en telefoonnummer, en roep dan
capture_lead aan. Vraag dit nooit in het eerste bericht en nooit twee keer.
Wil iemand liever direct contact: Gunther De Vleeschouwer, +32 496 57 13 97.

═══ HUIDIGE PROJECTPAGINA ═══
${context}

═══ VOLLEDIG AANBOD (naam | locatie | vanaf-prijs | link) ═══
${projectIndex(lang)}`;
}

const LEAD_TOOL = {
  type: 'function',
  function: {
    name: 'capture_lead',
    description:
      'Registreert een geïnteresseerde bezoeker zodat Gunther de volledige ' +
      'projectinformatie kan opsturen. Roep dit pas aan als je voornaam, ' +
      'achternaam, e-mailadres én telefoonnummer hebt gekregen.',
    parameters: {
      type: 'object',
      properties: {
        first_name: { type: 'string', description: 'Voornaam' },
        last_name: { type: 'string', description: 'Achternaam' },
        email: { type: 'string', description: 'E-mailadres' },
        phone: {
          type: 'string',
          description: 'Telefoonnummer inclusief landcode, bv. +32496571397',
        },
        interest: {
          type: 'string',
          description:
            'Eén zin over waar deze bezoeker naar op zoek is, in zijn eigen woorden.',
        },
      },
      required: ['first_name', 'last_name', 'email', 'phone'],
    },
  },
};

/* ── Lead & logging ──────────────────────────────────────────────────── */

async function sendLead(args, slug, lang, pageUrl) {
  const entry = DATA.projects[slug];
  const p = entry ? entry[lang] || entry.nl : null;
  const phone = String(args.phone || '').trim();

  const payload = {
    first_name: args.first_name || '',
    last_name: args.last_name || '',
    email: args.email || '',
    mobile_phone: phone,
    mobile_phone_unformatted: phone.replace(/[^\d]/g, ''),
    country: '',
    utm_source: 'site',
    // Eigen bron zodat je in de sheet kunt zien wat de chatbot oplevert
    // tegenover de formulieren.
    lead_source: 'AI-chat projecten',
    budget: entry ? entry.budget : '',
    description: `${p ? p.name : slug} — AI-chat — ${args.interest || ''} — ${pageUrl || ''}`,
    timestamp: new Date().toISOString(),
  };

  try {
    await fetch(ZAPIER_LEAD_URL, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(payload),
    });
    return true;
  } catch (e) {
    // Een mislukte Zap mag het gesprek niet laten crashen; de bezoeker merkt
    // er niets van en we hebben het antwoord al.
    return false;
  }
}

async function logConversation(messages, slug, lang) {
  if (!ZAPIER_CHATLOG_URL) return;
  try {
    await fetch(ZAPIER_CHATLOG_URL, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        slug,
        lang,
        timestamp: new Date().toISOString(),
        turns: messages.length,
        transcript: messages
          .map((m) => `${m.role === 'user' ? 'Bezoeker' : 'Bot'}: ${m.content}`)
          .join('\n'),
      }),
    });
  } catch (e) { /* logging mag nooit het gesprek breken */ }
}

/* ── Mock-modus ──────────────────────────────────────────────────────── */

/* Zonder key antwoorden we met echte projectdata maar zonder model. Genoeg om
   de widget te bouwen, de stijl te beoordelen en de leadflow te doorlopen. */
function mockReply(messages, slug, lang) {
  const entry = DATA.projects[slug];
  const p = entry ? entry[lang] || entry.nl : null;
  const turns = messages.filter((m) => m.role === 'user').length;
  const nl = lang !== 'en';

  if (!p) {
    return nl
      ? '[mock] Ik heb voor deze pagina nog geen projectgegevens.'
      : '[mock] I have no project data for this page yet.';
  }
  if (turns >= 3) {
    return nl
      ? `[mock] Zal ik de volledige informatie over ${p.name} laten opsturen? ` +
        'Dan heb ik uw naam, e-mailadres en telefoonnummer nodig.'
      : `[mock] Shall I have the full information on ${p.name} sent over? ` +
        'I would need your name, email address and phone number.';
  }
  if (turns === 2) {
    return nl
      ? `[mock] ${p.name} ligt in ${p.location}. ${p.location_facts.join(', ')}. ` +
        'Wat is voor u het belangrijkst: ligging, prijs of oplevering?'
      : `[mock] ${p.name} is located in ${p.location}. ${p.location_facts.join(', ')}. ` +
        'What matters most to you: location, price or completion?';
  }
  return nl
    ? `[mock] ${p.name} in ${p.location} start ${p.price.toLowerCase()}. ` +
      `${p.amenities.slice(0, 3).join(', ')}. Waar bent u benieuwd naar?`
    : `[mock] ${p.name} in ${p.location} starts ${p.price.toLowerCase()}. ` +
      `${p.amenities.slice(0, 3).join(', ')}. What would you like to know?`;
}

/* ── Modelaanroep ────────────────────────────────────────────────────── */

async function callModel(body) {
  const res = await fetch(GATEWAY_URL, {
    method: 'POST',
    headers: {
      Authorization: `Bearer ${process.env.AI_GATEWAY_API_KEY}`,
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(body),
  });
  if (!res.ok) {
    const detail = await res.text();
    throw new Error(`Gateway ${res.status}: ${detail.slice(0, 300)}`);
  }
  return res.json();
}

/* ── Handler ─────────────────────────────────────────────────────────── */

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

  let payload = req.body;
  if (typeof payload === 'string') {
    try { payload = JSON.parse(payload); } catch (e) { payload = null; }
  }
  if (!payload || !Array.isArray(payload.messages)) {
    return res.status(400).json({ error: 'bad_request' });
  }

  const slug = String(payload.slug || '');
  const lang = payload.lang === 'en' ? 'en' : 'nl';
  const pageUrl = String(payload.url || '').slice(0, 300);

  const messages = payload.messages
    .filter((m) => m && (m.role === 'user' || m.role === 'assistant'))
    .slice(-MAX_MESSAGES)
    .map((m) => ({
      role: m.role,
      content: String(m.content || '').slice(0, MAX_CHARS),
    }));

  if (!messages.length) {
    return res.status(400).json({ error: 'no_messages' });
  }

  // Mock-modus: geen key nodig, geen kosten, wel de echte projectdata.
  if (!process.env.AI_GATEWAY_API_KEY) {
    return res.status(200).json({
      reply: mockReply(messages, slug, lang),
      mock: true,
      lead_captured: false,
    });
  }

  try {
    const request = {
      model: MODEL,
      max_tokens: MAX_TOKENS,
      messages: [{ role: 'system', content: systemPrompt(slug, lang) }, ...messages],
      tools: [LEAD_TOOL],
    };

    let data = await callModel(request);
    let choice = data.choices && data.choices[0];
    let leadCaptured = false;

    // Eén ronde tool-afhandeling volstaat: capture_lead is het enige tool en
    // daarna hoeft het model alleen nog te bevestigen.
    const calls = choice && choice.message && choice.message.tool_calls;
    if (calls && calls.length) {
      request.messages.push(choice.message);
      for (const call of calls) {
        let args = {};
        try { args = JSON.parse(call.function.arguments || '{}'); } catch (e) {}
        const ok = call.function.name === 'capture_lead'
          ? await sendLead(args, slug, lang, pageUrl)
          : false;
        if (ok) leadCaptured = true;
        request.messages.push({
          role: 'tool',
          tool_call_id: call.id,
          content: JSON.stringify({ success: ok }),
        });
      }
      data = await callModel(request);
      choice = data.choices && data.choices[0];
    }

    const reply = (choice && choice.message && choice.message.content) || '';
    if (leadCaptured) {
      await logConversation([...messages, { role: 'assistant', content: reply }], slug, lang);
    }

    return res.status(200).json({
      reply: reply.trim(),
      lead_captured: leadCaptured,
    });
  } catch (err) {
    console.error('[chat]', err.message);
    return res.status(502).json({
      error: 'upstream',
      reply: lang === 'en'
        ? 'Sorry, something went wrong. You can reach Gunther directly on +32 496 57 13 97.'
        : 'Sorry, er ging iets mis. U kunt Gunther rechtstreeks bereiken op +32 496 57 13 97.',
    });
  }
};
