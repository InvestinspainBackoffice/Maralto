/**
 * /api/match - zoekt bij de antwoorden op /selectie/ de best passende
 * projecten, en geeft ze terug als kant-en-klare kaartjesdata.
 *
 * Zelfde regel als api/project-cards.js in de chatwidget: de browser stuurt
 * alleen critèria door, nooit projectdata. Naam, locatie, prijs, foto en URL
 * komen hier uit api/_projects.json - de enige bron. Zo kan een kaartje
 * nooit een verzonnen prijs of een dode foto tonen, ook niet als iemand met
 * de query-string knoeit.
 *
 * De endpoint wordt tijdens de flow bij elke stap aangeroepen voor de teller
 * ("nog 23 projecten"), en op het eind nog eens voor de kaartjes zelf. Dat is
 * bewust dezelfde endpoint: de teller moet exact hetzelfde tellen als wat de
 * bezoeker daarna te zien krijgt, anders klopt de belofte niet.
 *
 * Query-string wordt zelf geparsed (geen req.query) zodat dit zowel op Vercel
 * als op de lokale devserver werkt.
 */
const { URL } = require('url');
const DATA = require('./_projects.json');

// Ruimer dan bij /api/lead (8): deze endpoint wordt bij élke beantwoorde
// vraag aangeroepen voor de meelopende teller, dus één bezoeker komt in een
// normale doorloop al aan een stuk of twaalf verzoeken. De limiet is er
// tegen iemand die de hele catalogus wil uitlezen, niet tegen de flow zelf.
const RATE_MAX = 60;
const RATE_WINDOW_MS = 60000;
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

/* ── Regio's ──────────────────────────────────────────────────────────────
 * De drie keuzes op stap 1 zijn kuststroken, geen gemeentes, en ze overlappen
 * elkaar bewust ("Marbella" hoort bij A én B). De Costa del Sol loopt
 * praktisch oost-west, dus de lengtegraad uit de coördinaten van elk project
 * is hier een betrouwbaardere indeling dan de plaatsnaam: die staat als vrije
 * tekst in de projectbestanden ("SAN PEDRO, MARBELLA", "OOST-MARBELLA", ...)
 * en zou een lijst uitzonderingen vragen die bij elk nieuw project weer
 * bijgewerkt moet worden. Met deze banden valt elk van de 128 projecten in
 * minstens één regio.
 */
const REGIONS = {
  A: [-4.92, -3.70], // Málaga – Marbella
  B: [-5.18, -4.85], // Marbella – Estepona
  C: [-5.42, -5.10], // Estepona – Sotogrande
};

/* Onder- en bovengrens per budgetcategorie, in euro.
 *
 * De sleutel is een URL-veilige code, niet de Salesforce-code zelf. Die
 * laatste bevat '<', '+' en spaties ('<200k', '3m+', '1m - 3m') en overleeft
 * een query-string niet: '3m+' komt aan de overkant binnen als '3m ', wat de
 * budgetfilter stilzwijgend uitschakelt in plaats van luid te falen. De
 * Salesforce-code staat hiernaast in `sf` en gaat ongewijzigd mee met de
 * lead (in de JSON-body van /api/lead, waar hij géén encoding hoeft te
 * overleven). Spiegelt BUDGET_BUCKETS in _build/generate.py. */
const BUDGET_RANGE = {
  lt200k: { range: [0, 200000], sf: '<200k' },
  '200-400': { range: [200000, 400000], sf: '200k-400k' },
  '400-600': { range: [400000, 600000], sf: '400k-600k' },
  '600-1m': { range: [600000, 1000000], sf: '600k-1m' },
  '1m-3m': { range: [1000000, 3000000], sf: '1m - 3m' },
  '3m-plus': { range: [3000000, Infinity], sf: '3m+' },
};
// Een vanaf-prijs is een vanaf-prijs: een project dat net buiten de gekozen
// categorie begint is nog steeds een reële optie. Boven de grens 10%
// speling, zodat iemand met "400k-600k" een project van €610.000 wél ziet.
// Naar beneden ruimer (60% van de ondergrens, dus ongeveer één categorie
// lager): goedkoper dan gevraagd is zelden een bezwaar, véél goedkoper wel -
// wie €3m opgeeft en een project van €464.000 bovenaan krijgt, ziet een
// selectie die zijn belangrijkste antwoord negeert.
const BUDGET_TOLERANCE_HIGH = 1.1;
const BUDGET_TOLERANCE_LOW = 0.6;

const TYPE_PATTERNS = {
  apartment: /appartement|apartment/,
  penthouse: /penthouse/,
  villa: /villa/,
  townhouse: /townhouse|rijwoning|geschakelde woning|semi-?detached/,
};

const LOCATION_PATTERNS = {
  quiet: /rustig|serene|sereen|beslote|privacy|oase|luwte|quiet|secluded|tranquil/,
  city: /centrum|stadskern|oude stad|city cent|town cent|old town/,
  golf: /golf/,
  beach: /strand|beachfront|eerstelijns|zeefront|beach|seafront/,
  countryside: /natuur|platteland|groene omgeving|heuvel|bergen|landelijk|countryside|nature|hillside/,
};

const VIEW_PATTERNS = {
  sea: /zeezicht|zicht op zee|uitzicht op zee|zeezijde|sea view|ocean view/,
  mountain: /bergzicht|bergen|la concha|sierra|mountain view/,
};

function textOf(entry, lang) {
  const p = entry[lang] || entry.nl;
  if (!p) return { strong: '', weak: '' };
  const sections = p.sections || [];
  // Twee tekstlagen, want ze zeggen iets heel verschillends. "Golf" in de
  // samenvatting of een kop betekent dat het project óver golf gaat; "Golf"
  // in de afstandenlijst betekent alleen dat er een baan in de buurt ligt -
  // en dat geldt aan de Costa del Sol voor bijna alles. Zonder dit
  // onderscheid scoort elk project even hoog op elke voorkeur.
  const strong = [p.name, p.summary, ...sections.map((s) => s.heading)]
    .join(' ')
    .toLowerCase();
  const weak = [
    strong,
    ...sections.map((s) => s.text),
    ...(p.stats || []),
    ...(p.amenities || []),
    ...(p.location_facts || []),
  ]
    .join(' ')
    .toLowerCase();
  return { strong, weak };
}

function parseRange(text, unitPattern) {
  // Vangt zowel "3 slaapkamers" als "1 – 4 slaapkamers" en "70-175 m²".
  const re = new RegExp(
    `(\\d{1,4})\\s*(?:[\\u2013\\u2014\\-]|tot|to)?\\s*(\\d{1,4})?\\s*${unitPattern}`,
    'g'
  );
  let min = null;
  let max = null;
  let m;
  while ((m = re.exec(text)) !== null) {
    const lo = parseInt(m[1], 10);
    const hi = m[2] ? parseInt(m[2], 10) : lo;
    if (min === null || lo < min) min = lo;
    if (max === null || hi > max) max = hi;
  }
  return min === null ? null : { min, max };
}

/* De facetten worden één keer per cold start berekend en daarna hergebruikt.
 * Ze staan bewust niet in _projects.json: dat bestand wordt ook door de
 * chatwidget gebruikt, en deze afleidingen zijn alleen voor /selectie/. */
let FACETS = null;

function buildFacets() {
  const out = {};
  for (const [slug, entry] of Object.entries(DATA.projects)) {
    const lon = entry.coords ? parseFloat(entry.coords.split(',')[1]) : NaN;
    const regions = [];
    if (!Number.isNaN(lon)) {
      for (const [code, [lo, hi]] of Object.entries(REGIONS)) {
        if (lon >= lo && lon <= hi) regions.push(code);
      }
    }

    const perLang = {};
    for (const lang of ['nl', 'en']) {
      if (!entry[lang]) continue;
      const { strong, weak } = textOf(entry, lang);
      const types = [];
      for (const [name, re] of Object.entries(TYPE_PATTERNS)) {
        if (re.test(weak)) types.push(name);
      }
      perLang[lang] = {
        strong,
        weak,
        types,
        bedrooms: parseRange(weak, '(?:-|\\s)?(?:slaapkamer|bedroom)'),
        indoor: parseRange(weak, 'm\\u00b2'),
      };
    }

    out[slug] = { regions, lang: perLang };
  }
  return out;
}

function scoreProject(entry, facet, f, q) {
  let score = 0;

  // Het type is een harde filter (zie collect()); wat hier overblijft is óf
  // van het gevraagde type, óf een project dat zijn type nergens benoemt.
  // De punten zetten die eerste groep bovenaan.
  if (q.type) {
    if (q.type === 'turnkey') {
      // "Turnkey Modern Property" is geen bouwvorm maar een oplevermoment,
      // en dus geen reden om iets uit te sluiten - alleen om het te tonen.
      if (/sleutelklaar|instapklaar|turnkey|opgeleverd|key-?ready|move-?in ready/.test(f.weak)) {
        score += 24;
      }
    } else if (f.types.includes(q.type)) {
      score += 30;
    }
  }

  // Slaapkamers, woonoppervlak: alleen belonen wat we zéker weten. Deze
  // getallen staan in vrije tekst en zijn maar voor een deel van de projecten
  // af te leiden (slaapkamers ~71/128, m² ~21/128). Een onbekende waarde
  // telt daarom neutraal - anders zou de helft van de catalogus wegvallen op
  // ontbrekende data in plaats van op een echte mismatch.
  if (q.bedrooms && f.bedrooms) {
    const want = q.bedrooms;
    const fits = q.bedroomsOpen
      ? f.bedrooms.max >= want
      : want >= f.bedrooms.min && want <= f.bedrooms.max;
    score += fits ? 12 : -8;
  }
  if (q.indoor && f.indoor) {
    const [lo, hi] = q.indoor;
    score += f.indoor.max >= lo && f.indoor.min <= hi ? 8 : -5;
  }

  if (q.location) {
    const re = LOCATION_PATTERNS[q.location];
    if (re) {
      if (re.test(f.strong)) score += 18;
      else if (re.test(f.weak)) score += 6;
    }
  }

  if (q.view && q.view !== 'none') {
    const re = VIEW_PATTERNS[q.view];
    if (re) {
      if (re.test(f.strong)) score += 14;
      else if (re.test(f.weak)) score += 5;
    }
  }

  // Budget weegt zwaar, en bewust zwaarder dan elke tekstuele voorkeur.
  // Iemand die "1m - 3m" antwoordt en bovenaan een project van €464.000
  // krijgt omdat dat toevallig "zeezicht" in zijn samenvatting heeft, ziet
  // een selectie die zijn belangrijkste antwoord negeert. De prijs telt
  // volledig mee vanaf ~70% van de bovengrens en zakt daaronder af.
  if (entry.price_num && q.budget) {
    const [lo, hi] = BUDGET_RANGE[q.budget].range;
    // Binnen de gekozen categorie: volle punten. Erbuiten (maar binnen de
    // tolerantie die de harde filter nog doorlaat): afgezwakt.
    const inside = entry.price_num >= lo && entry.price_num <= hi;
    score += inside ? 25 : 10;
  }

  return score;
}

function parseQuery(params) {
  const regions = (params.get('regions') || '')
    .split(',')
    .map((s) => s.trim().toUpperCase())
    .filter((s) => REGIONS[s]);

  const INDOOR = { lt100: [0, 100], '100-150': [100, 150], '150plus': [150, 100000] };

  const budget = params.get('budget') || '';
  const type = params.get('type') || '';
  const location = params.get('location') || '';
  const view = params.get('view') || '';
  const bedroomsRaw = params.get('bedrooms') || '';
  const bedroomsMatch = bedroomsRaw.match(/^(\d)(plus)?$/);

  return {
    regions,
    type: TYPE_PATTERNS[type] || type === 'turnkey' ? type : '',
    budget: BUDGET_RANGE[budget] ? budget : '',
    bedrooms: bedroomsMatch ? parseInt(bedroomsMatch[1], 10) : 0,
    bedroomsOpen: Boolean(bedroomsMatch && bedroomsMatch[2]),
    indoor: INDOOR[params.get('indoor')] || null,
    location: LOCATION_PATTERNS[location] ? location : '',
    view: VIEW_PATTERNS[view] ? view : '',
  };
}

module.exports = (req, res) => {
  if (req.method !== 'GET') {
    res.setHeader('Allow', 'GET');
    return res.status(405).json({ error: 'method_not_allowed' });
  }

  const ip =
    ((req.headers && req.headers['x-forwarded-for']) || '').split(',')[0].trim() ||
    'unknown';
  if (rateLimited(ip)) {
    return res.status(429).json({ error: 'rate_limited' });
  }

  if (!FACETS) FACETS = buildFacets();

  const parsed = new URL(req.url, 'http://localhost');
  const params = parsed.searchParams;
  const lang = params.get('lang') === 'en' ? 'en' : 'nl';
  const limit = Math.min(12, Math.max(1, parseInt(params.get('limit'), 10) || 3));
  const q = parseQuery(params);

  function collect(useBudget) {
    const out = [];
    for (const [slug, entry] of Object.entries(DATA.projects)) {
      const facet = FACETS[slug];
      const f = facet.lang[lang] || facet.lang.nl;
      if (!f) continue;

      // Projecten zonder vanaf-prijs ("Uitverkocht", "Prijs op aanvraag",
      // "Binnenkort beschikbaar" - 4 van de 128) vallen af. Ze zijn niet op
      // budget te toetsen, en een uitverkocht project bovenaan een
      // persoonlijke selectie zetten ondermijnt precies het vertrouwen dat
      // deze pagina moet opbouwen.
      if (!entry.price_num) continue;

      // Harde filters: alleen op wat we voor álle projecten zeker weten -
      // de regio (uit de coördinaten) en de vanaf-prijs.
      if (q.regions.length && !q.regions.some((r) => facet.regions.includes(r))) continue;

      // Wie om een villa vraagt hoort niet meegeteld te worden in een lijst
      // vol appartementen. Projecten die hun type nergens benoemen (6 van de
      // 128) blijven wél staan: die vallen weg op ontbrekende data, niet op
      // een echte mismatch. 'turnkey' filtert niet - dat is een
      // oplevermoment, geen bouwvorm.
      if (
        q.type &&
        q.type !== 'turnkey' &&
        f.types.length &&
        !f.types.includes(q.type)
      ) {
        continue;
      }
      if (useBudget && q.budget) {
        const [lo, hi] = BUDGET_RANGE[q.budget].range;
        if (entry.price_num > hi * BUDGET_TOLERANCE_HIGH) continue;
        if (entry.price_num < lo * BUDGET_TOLERANCE_LOW) continue;
      }

      out.push({ slug, entry, score: scoreProject(entry, facet, f, q) });
    }

    // Vaste volgorde bij gelijke score, zodat dezelfde antwoorden altijd
    // dezelfde lijst geven - een resultaat dat per refresh wisselt voelt als
    // een gok in plaats van een selectie.
    out.sort(
      (a, b) =>
        b.score - a.score ||
        a.entry.price_num - b.entry.price_num ||
        a.slug.localeCompare(b.slug)
    );
    return out;
  }

  let scored = collect(true);
  // Onder €200.000 heeft de catalogus vandaag niets. Liever eerlijk het
  // dichtstbijzijnde alternatief tonen (en dat zo labelen) dan een leeg
  // scherm na negen ingevulde vragen.
  const relaxed = scored.length === 0;
  if (relaxed) scored = collect(false);

  // Vier ontwikkelingen staan onder twee slugs in de portefeuille (een
  // tweede fase of een aparte duplex-selectie), met dezelfde naam. Twee
  // kaartjes "Ocean View Marbella" naast elkaar kost een plek in een top drie
  // en leest als een fout. De best scorende van het paar blijft staan.
  const seenNames = new Set();
  const cards = [];
  for (const { slug, entry } of scored) {
    if (cards.length >= limit) break;
    const p = entry[lang] || entry.nl;
    const key = String(p.name || '').toLowerCase().replace(/[^a-z0-9]/g, '');
    if (key && seenNames.has(key)) continue;
    seenNames.add(key);
    cards.push({
      slug,
      name: p.name,
      location: p.location,
      price: p.price,
      url: p.url,
      image: entry.image || '',
    });
  }

  res.setHeader('Cache-Control', 'public, max-age=300');
  return res.status(200).json({
    count: relaxed ? 0 : scored.length,
    relaxed,
    // De Salesforce-code hoort bij de gekozen categorie en wordt hier
    // teruggegeven zodat de pagina hem letterlijk kan doorsturen met de lead,
    // zonder de mapping een tweede keer te moeten kennen.
    budget_sf: q.budget ? BUDGET_RANGE[q.budget].sf : '',
    cards,
  });
};
