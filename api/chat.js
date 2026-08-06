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
const { forwardToZapier } = require('./_zapier.js');
const { PLAYBOOK } = require('./_playbook.js');

const GATEWAY_URL = 'https://ai-gateway.vercel.sh/v1/chat/completions';
const MODEL = process.env.AI_MODEL || 'anthropic/claude-haiku-4.5';
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
    `Type: ${p.types && p.types.length ? p.types.join(', ') : 'onbekend'}`,
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

/* Index van het hele aanbod, zodat de bot kan doorverwijzen naar een ander
   project ("goedkoper", "wel met zeezicht").
   Twee varianten: op een projectpagina volstaat één regel per project (~2k
   tokens), want de diepgang zit daar al in de context hierboven. Op de hub is
   er geen huidig project en moet de bot juist helpen kiezen - daar gaat de
   korte omschrijving mee, zodat hij op meer kan adviseren dan prijs en plaats.
   Beide zijn identiek bij elk gesprek en dus goed cachebaar. */
const indexCache = {};

function projectIndex(lang, rich) {
  const key = lang + (rich ? ':rich' : '');
  if (indexCache[key]) return indexCache[key];
  const rows = [];
  for (const entry of Object.values(DATA.projects)) {
    const p = entry[lang] || entry.nl;
    if (!p) continue;
    const types = p.types && p.types.length ? p.types.join('/') : '?';
    rows.push(rich
      ? `${p.name} | ${p.location} | ${types} | ${p.price} | ${p.url}\n   ${p.summary}`
      : `${p.name} | ${p.location} | ${types} | ${p.price} | ${p.url}`);
  }
  rows.sort();
  indexCache[key] = rows.join('\n');
  return indexCache[key];
}

/* ── Systeemprompt ───────────────────────────────────────────────────── */

function systemPrompt(slug, lang) {
  const context = projectContext(slug, lang);
  const taal = lang === 'en' ? 'English' : 'Nederlands';
  const pb = PLAYBOOK[lang] || PLAYBOOK.nl;

  // Zonder geldige slug staat de bezoeker op de projectenoverzichtspagina.
  // Daar is er geen huidig project en verschuift de opdracht van "alles weten
  // over dit project" naar "helpen het juiste project te vinden".
  const positie = context
    ? 'Je staat op de projectpagina hieronder en helpt bezoekers die overwegen te kopen.'
    : 'Je staat op de projectenoverzichtspagina. Er is dus geen huidig project: ' +
      'jouw taak is de bezoeker helpen het juiste project te vinden uit het volledige aanbod.';

  return `Je bent de persoonlijke AI-assistent van INVESTINSPAIN.BE, een Belgisch
makelaarskantoor gespecialiseerd in nieuwbouwvastgoed aan de Spaanse Costa del Sol.
Je bent een assistent die meedenkt, geen zoekmachine die meteen een lijst aanbiedingen
toont. ${positie}

TAAL
De begroeting staat al vast in ${taal}. Antwoord daarna altijd in dezelfde taal als het
LAATSTE bericht van de bezoeker, ook als dat afwijkt van ${taal} — een bezoeker die in
het Frans of Duits typt, krijgt dus een Frans of Duits antwoord, niet automatisch ${taal}.

STIJL
- ${pb.tone}
- Kort en concreet. Dit is een chatvenster, geen brochure: 2 tot 4 zinnen per antwoord.
- Geen verkooppraat, geen uitroeptekens.
- Stel per beurt hooguit één gerichte vervolgvraag.

GESPREKSOPBOUW (max. 3 kwalificatievragen, dan pas aanbevelen)
Voor je specifieke projecten, prijzen of links toont, ken je minstens: (1) het BUDGET —
dit is de belangrijkste vraag, vraag die het eerst of het vroegst, (2) de regio die de
bezoeker zoekt, en (3) het type woning (appartement/villa/penthouse). Ontbreekt dat,
stel dan open kwalificatievragen — kies uit of vul aan met:
${pb.qualifyingQuestions.map((q) => `- ${q}`).join('\n')}
Zodra je die drie kent: stel een vrijblijvend online gesprek met een verkoper voor.
Voelt de bezoeker daar nog niet klaar voor, bied dan aan hem/haar op de hoogte te
houden (nieuwsbrief/nieuwe projecten) in plaats van aan te dringen.

CONTACTGEGEVENS NATUURLIJK VERZAMELEN
Je hebt uiteindelijk voornaam, achternaam, e-mailadres en telefoonnummer nodig — maar
nooit als een lijstje of formulier, en nooit alle vier tegelijk in één vraag. Weef het
in het gesprek, bijvoorbeeld: "Zal ik dit voor u laten opsturen? Aan wie mag ik het
richten?" — dan pas naam vragen, dan pas telefoon/e-mail ("En op welk nummer of
e-mailadres bereiken we u het best?"). Het moet aanvoelen als een assistent die
opvolgt, niet als een intakeformulier.

WAT JE ZEKER WEET
Alleen wat hieronder staat, plus het bedrijfsprofiel. Verzin nooit prijzen, oppervlaktes,
opleverdata, beschikbaarheid of aantallen die er niet staan. Weet je iets niet, zeg dat
dan en bied aan dat Gunther het uitzoekt. Dat is altijd een beter antwoord dan gokken.
${pb.noPlansUpfront}

${context ? `ANDERE PROJECTEN
Past dit project niet bij wat iemand zoekt, verwijs dan naar een passend project
uit de lijst onderaan, met naam, locatie, vanaf-prijs en link. Doe dat hooguit
twee of drie projecten tegelijk.` : `AANBEVELEN ZODRA JE GENOEG WEET
Toon nooit een project, prijs of link voordat je regio, type en budgetorde kent (zie
GESPREKSOPBOUW hierboven). Zodra je die drie kent: doorzoek de volledige aanbodlijst
onderaan en selecteer daaruit zelf ongeveer 3 projecten die tegelijk qua locatie, type
én budget het best aansluiten — niet zomaar de eerste 3 uit de lijst. Presenteer ze
gerangschikt van beste naar minder goede match, telkens met naam, locatie, type,
vanaf-prijs, link en één korte zin waarom precies dit project past bij wat de bezoeker
zocht. Is er geen enkele goede match binnen het budget, zeg dat eerlijk en toon dan het
dichtstbijzijnde alternatief met uitleg waarom het net niet past (bv. iets hoger budget).
Som nooit de hele lijst op.`}

KOPEN IN SPANJE
Je mag algemene oriëntatie geven over het aankoopproces: NIE-nummer, notaris,
overdrachtsbelasting, bijkomende kosten, verloop van een nieuwbouwaankoop.
Houd het op hoofdlijnen en zeg er altijd bij dat het afhangt van de persoonlijke
situatie. Geef nooit fiscaal, juridisch of hypotheekadvies als vaststaand feit,
noem nooit concrete percentages als zekerheid, en beloof nooit rendement of
waardestijging. Bij dat soort vragen verwijs je door naar Gunther.
Nuttige feiten die je wel mag delen:
${pb.facts.map((f) => `- ${f}`).join('\n')}

WAAROM INVESTINSPAIN (gebruik dit alleen als het relevant is, niet als opsomming)
${pb.usps.map((u) => `- ${u}`).join('\n')}

BEDRIJFSPROFIEL
${pb.company}

NOOIT VERMELDEN
- Vermeld nooit de naam "Welex" of eender welke andere partner- of leveranciersnaam.
  Presenteer alle diensten (juridisch advies, vertalingen, inrichting, ...) alsof
  INVESTINSPAIN.BE die zelf rechtstreeks levert.
- Vermeld nooit hoeveel projecten er in totaal in het aanbod zitten, ook niet als
  ernaar gevraagd wordt. Wijk uit met iets als "we hebben een ruim aanbod nieuwbouw
  aan de Costa del Sol" en ga meteen door met kwalificeren.

LEADS
Roep capture_lead pas aan zodra je voornaam, achternaam, e-mailadres én telefoonnummer
hebt gekregen — via het gesprek, nooit als los formulier. Vraag dit nooit in het eerste
bericht en nooit twee keer. Wil iemand liever meteen persoonlijk contact, dan kan dat via
het knopje "Liever met een verkoper spreken" hierboven in de chat, of rechtstreeks bij
Gunther op +32 496 57 13 97.

${context ? `═══ HUIDIGE PROJECTPAGINA ═══\n${context}\n` : ''}
═══ VOLLEDIG AANBOD (naam | locatie | type(s) | vanaf-prijs | link — "?" = type onbekend) ═══
${projectIndex(lang, !context)}`;
}

const LEAD_TOOL = {
  type: 'function',
  function: {
    name: 'capture_lead',
    description:
      'Registreert een geïnteresseerde bezoeker zodat het team kan opvolgen. ' +
      'Roep dit pas aan als je voornaam, achternaam, e-mailadres én ' +
      'telefoonnummer hebt gekregen — via het gesprek, nooit als los formulier.',
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
        intent: {
          type: 'string',
          enum: ['meeting', 'stay_informed'],
          description:
            '"meeting" als de bezoeker klaar is voor een vrijblijvend gesprek met ' +
            'een verkoper, "stay_informed" als hij/zij liever eerst op de hoogte ' +
            'gehouden wil worden (nieuwsbrief/nieuwe projecten) zonder meteen een ' +
            'afspraak te willen.',
        },
      },
      required: ['first_name', 'last_name', 'email', 'phone', 'intent'],
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
    description: `${p ? p.name : slug} — AI-chat (${args.intent === 'stay_informed' ? 'wil op de hoogte blijven' : 'wil gesprek'}) — ${args.interest || ''} — ${pageUrl || ''}`,
    timestamp: new Date().toISOString(),
  };

  // forwardToZapier vangt zijn eigen fouten af; een mislukte Zap mag het
  // gesprek niet laten crashen - de bezoeker merkt er niets van en we
  // hebben het antwoord al.
  return forwardToZapier(payload);
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

  // Hub: geen huidig project. Bootst de echte gespreksopbouw na - eerst
  // kwalificeren (geen projectnamen/prijzen), pas vanaf de 3e beurt een
  // aanbeveling. Zo test je in mock-modus hetzelfde gedrag als straks live.
  if (!p) {
    if (turns === 1) {
      return nl
        ? '[mock] Hoi, ik help u graag het juiste project vinden. In welke regio zoekt u, en wat voor type woning - appartement, villa of penthouse?'
        : "[mock] Hi, I'm happy to help you find the right project. Which region are you looking in, and what type of property - apartment, villa or penthouse?";
    }
    if (turns === 2) {
      return nl
        ? '[mock] Genoteerd. En in welke ordegrootte van budget zoekt u?'
        : '[mock] Noted. And what is your approximate budget range?';
    }
    const sample = Object.values(DATA.projects)
      .map((e) => e[lang] || e.nl)
      .filter(Boolean)
      .slice(0, 3)
      .map((x) => `${x.name} (${x.location}, ${(x.types || []).join('/') || '?'}, ${x.price.toLowerCase()})`)
      .join(' — ');
    return nl
      ? `[mock] Op basis daarvan passen deze het best: ${sample}. Zal ik een van deze verder toelichten, of stel ik een gesprek met een verkoper voor?`
      : `[mock] Based on that, these fit best: ${sample}. Shall I go into more detail on one of these, or would you like to arrange a chat with a sales agent?`;
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
