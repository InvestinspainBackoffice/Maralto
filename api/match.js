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

/* ── Gemeentes ────────────────────────────────────────────────────────────
 * De tien keuzes op stap 1 zijn gemeentes/wijken langs de Costa del Sol.
 * We matchen op de `location`-tekst van elk project (HERO_LOCATION uit het
 * projectbestand), niet op lengtegraad. Die tekst is betrouwbaarder: "SAN
 * PEDRO, MARBELLA" is duidelijk San Pedro, terwijl dezelfde lengtegraad ook
 * net in Cancelada of Benahavís kan vallen. Een project kan in meerdere
 * gemeentes vallen als de locatietekst meerdere patronen treft.
 */
const MUNICIPALITIES = {
  sotogrande:  /sotogrande|alcaidesa/i,
  manilva:     /manilva|casares/i,
  estepona:    /estepona/i,
  sanpedro:    /san pedro|cancelada/i,
  puertobanus: /nueva andal|la quinta|real de la quinta|ist[aá]n|oj[eé]n|puerto ban/i,
  marbella:    /\bmarbella\b|benahav[ií]s|elviria/i,
  mijascosta:  /mijas costa|la cala de mijas/i,
  mijas:       /\bmijas\b(?!\s*costa)/i,
  fuengirola:  /fuengirola|mijas pueblo/i,
  malaga:      /benalm[aá]dena|torremolinos|m[aá]laga|torre del mar/i,
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
  lt200k:   { range: [0, 200000],         sf: '<200k' },
  '200-400':{ range: [200000, 400000],    sf: '200k-400k' },
  '400-600':{ range: [400000, 600000],    sf: '400k-600k' },
  '600-1m': { range: [600000, 1000000],   sf: '600k-1m' },
  '1m-3m':  { range: [1000000, 3000000],  sf: '1m - 3m' },
  '3m-plus':{ range: [3000000, Infinity], sf: '3m+' },
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
    // Gemeente-matching op locatietekst: betrouwbaarder dan lengtegraad
    // omdat de HERO_LOCATION in elk projectbestand de echte gemeentenaam
    // bevat (bv. "SAN PEDRO, MARBELLA"), terwijl lengtegraad-banden altijd
    // een arbitraire drempel vereisen die bij elk nieuw project gecontroleerd
    // moet worden.
    const locationText = (entry.nl && entry.nl.location) || '';
    const municipalities = [];
    for (const [code, re] of Object.entries(MUNICIPALITIES)) {
      if (re.test(locationText)) municipalities.push(code);
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

    out[slug] = { municipalities, lang: perLang };
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
      if (/sleutelklaar|instapklaar|turnkey|opgeleverd|key-?ready|move-?in ready/.test(f.weak)) {
        score += 24;
      }
    } else if (f.types.includes(q.type)) {
      score += 30;
    }
  }

  // Slaapkamers, woonoppervlak: alleen belonen wat we zéker weten.
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
  if (entry.price_num && q.budget) {
    const [lo, hi] = BUDGET_RANGE[q.budget].range;
    const inside = entry.price_num >= lo && entry.price_num <= hi;
    score += inside ? 25 : 10;
  }

  return score;
}

function parseQuery(params) {
  const regions = (params.get('regions') || '')
    .split(',')
    .map((s) => s.trim().toLowerCase())
    .filter((s) => MUNICIPALITIES[s]);

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
      // "Binnenkort beschikbaar" - 4 van de 128) vallen af.
      if (!entry.price_num) continue;

      // Harde gemeente-filter: alleen als de bezoeker minstens één gemeente
      // heeft gekozen én het project in geen enkele gekozen gemeente valt.
      if (q.regions.length && !q.regions.some((r) => facet.municipalities.includes(r))) continue;

      // Wie om een villa vraagt hoort niet meegeteld te worden in een lijst
      // vol appartementen. Projecten die hun type nergens benoemen (6 van de
      // 128) blijven wél staan. 'turnkey' filtert niet.
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
  // tweede fase of een aparte duplex-selectie), met dezelfde naam.
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
    budget_sf: q.budget ? BUDGET_RANGE[q.budget].sf : '',
    cards,
  });
};
