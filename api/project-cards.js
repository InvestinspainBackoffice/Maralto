/**
 * /api/project-cards - lichte, dependency-vrije endpoint die kaartjesdata
 * teruggeeft voor de klikbare projectaanbevelingen in de AI-chatwidget.
 *
 * Haalt bewust uit dezelfde _projects.json als /api/chat: het model geeft in
 * zijn antwoord alleen de slug door (via de PROJECTEN:-regel in de
 * systeemprompt), nooit naam/prijs/locatie zelf - die haalt de browser hier
 * rechtstreeks op uit de vertrouwde bron. Zo kan een kaartje nooit een
 * verzonnen prijs tonen, ook niet als het model zich zou vergissen.
 *
 * Query-string wordt zelf geparsed (geen req.query) zodat dit zowel op
 * Vercel als op de lokale devserver werkt.
 */
const { URL } = require('url');
const DATA = require('./_projects.json');

module.exports = (req, res) => {
  if (req.method !== 'GET') {
    res.setHeader('Allow', 'GET');
    return res.status(405).json({ error: 'method_not_allowed' });
  }

  const parsed = new URL(req.url, 'http://localhost');
  const lang = parsed.searchParams.get('lang') === 'en' ? 'en' : 'nl';
  const slugs = (parsed.searchParams.get('slugs') || '')
    .split(',')
    .map((s) => s.trim())
    .filter(Boolean)
    .slice(0, 4); // nooit meer dan 4 kaartjes, ook niet bij een rare invoer

  const cards = [];
  for (const slug of slugs) {
    const entry = DATA.projects[slug];
    if (!entry) continue;
    const p = entry[lang] || entry.nl;
    if (!p) continue;
    cards.push({
      slug,
      name: p.name,
      location: p.location,
      price: p.price,
      types: p.types || [],
      url: p.url,
      image: entry.image || '',
    });
  }

  res.setHeader('Cache-Control', 'public, max-age=300');
  return res.status(200).json({ cards });
};
