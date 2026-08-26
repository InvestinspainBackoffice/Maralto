/**
 * Bekende referentiepunten aan de Costa del Sol.
 * Coördinaten: [lat, lon]
 * Aliassen: hoe een bezoeker dit punt kan noemen in de chat
 * (hoofdletterloos, accenten weggelaten voor matching).
 *
 * Worden gebruikt in chat.js om per project de afstand tot het
 * dichtstbijzijnde relevante punt te berekenen en toe te voegen
 * aan de projectindex — zodat de bot kan antwoorden op vragen als
 * "ik wil op 5 minuten van de haven van Estepona wonen".
 */

const LANDMARKS = [
  /* ── Havens / jachthavens ── */
  {
    id: 'haven-estepona',
    label: 'haven van Estepona',
    coords: [36.4274, -5.1477],
    aliases: ['haven estepona', 'puerto estepona', 'jachthaven estepona', 'marina estepona', 'port estepona'],
  },
  {
    id: 'puerto-banus',
    label: 'Puerto Banús',
    coords: [36.4876, -4.9567],
    aliases: ['puerto banus', 'puerto banus', 'banus', 'puerto de banus'],
  },
  {
    id: 'haven-marbella',
    label: 'haven van Marbella',
    coords: [36.5082, -4.8876],
    aliases: ['haven marbella', 'puerto marbella', 'jachthaven marbella', 'marina marbella'],
  },
  {
    id: 'sotogrande-marina',
    label: 'Marina Sotogrande',
    coords: [36.2890, -5.2882],
    aliases: ['marina sotogrande', 'haven sotogrande', 'puerto sotogrande'],
  },
  {
    id: 'fuengirola-haven',
    label: 'haven van Fuengirola',
    coords: [36.5384, -4.6259],
    aliases: ['haven fuengirola', 'puerto fuengirola', 'marina fuengirola'],
  },

  /* ── Stranden ── */
  {
    id: 'strand-estepona',
    label: 'strand Estepona',
    coords: [36.4239, -5.1440],
    aliases: ['strand estepona', 'playa estepona', 'beach estepona', 'zee estepona'],
  },
  {
    id: 'strand-marbella',
    label: 'strand Marbella',
    coords: [36.5012, -4.8843],
    aliases: ['strand marbella', 'playa marbella', 'beach marbella', 'zee marbella'],
  },
  {
    id: 'strand-san-pedro',
    label: 'strand San Pedro',
    coords: [36.4840, -5.0720],
    aliases: ['strand san pedro', 'playa san pedro', 'beach san pedro'],
  },
  {
    id: 'strand-fuengirola',
    label: 'strand Fuengirola',
    coords: [36.5381, -4.6279],
    aliases: ['strand fuengirola', 'playa fuengirola', 'beach fuengirola'],
  },
  {
    id: 'strand-la-cala',
    label: 'strand La Cala de Mijas',
    coords: [36.5003, -4.7209],
    aliases: ['strand la cala', 'playa la cala', 'la cala strand', 'beach la cala'],
  },

  /* ── Luchthavens ── */
  {
    id: 'malaga-airport',
    label: 'luchthaven Málaga',
    coords: [36.6749, -4.4991],
    aliases: ['malaga airport', 'luchthaven malaga', 'vliegveld malaga', 'airport malaga', 'agp'],
  },
  {
    id: 'gibraltar-airport',
    label: 'luchthaven Gibraltar',
    coords: [36.1502, -5.3495],
    aliases: ['gibraltar airport', 'luchthaven gibraltar', 'vliegveld gibraltar'],
  },

  /* ── Stadscentra ── */
  {
    id: 'centrum-marbella',
    label: 'centrum Marbella',
    coords: [36.5093, -4.8843],
    aliases: ['centrum marbella', 'center marbella', 'casco antiguo marbella', 'old town marbella', 'marbella centrum', 'stad marbella'],
  },
  {
    id: 'centrum-estepona',
    label: 'centrum Estepona',
    coords: [36.4274, -5.1467],
    aliases: ['centrum estepona', 'center estepona', 'casco antiguo estepona', 'old town estepona', 'estepona centrum', 'stad estepona'],
  },
  {
    id: 'centrum-fuengirola',
    label: 'centrum Fuengirola',
    coords: [36.5399, -4.6249],
    aliases: ['centrum fuengirola', 'center fuengirola', 'fuengirola centrum'],
  },
  {
    id: 'centrum-benahavis',
    label: 'centrum Benahavís',
    coords: [36.5224, -5.0478],
    aliases: ['centrum benahavis', 'center benahavis', 'benahavis centrum', 'benahavis dorp'],
  },

  /* ── Golf ── */
  {
    id: 'la-quinta-golf',
    label: 'La Quinta Golf',
    coords: [36.5080, -4.9878],
    aliases: ['la quinta golf', 'la quinta'],
  },
  {
    id: 'valderrama',
    label: 'Valderrama Golf',
    coords: [36.2842, -5.2951],
    aliases: ['valderrama', 'valderrama golf', 'real club valderrama'],
  },
  {
    id: 'atalaya-golf',
    label: 'Atalaya Golf',
    coords: [36.4801, -5.0292],
    aliases: ['atalaya golf', 'atalaya golf country club'],
  },
  {
    id: 'flamingos-golf',
    label: 'Flamingos Golf',
    coords: [36.4836, -5.0519],
    aliases: ['flamingos golf', 'villa padierna golf', 'flamingos'],
  },
  {
    id: 'la-cala-golf',
    label: 'La Cala Golf Resort',
    coords: [36.5219, -4.7363],
    aliases: ['la cala golf', 'la cala resort', 'cala golf'],
  },

  /* ── Winkels / voorzieningen ── */
  {
    id: 'la-canada',
    label: 'La Cañada Shopping',
    coords: [36.5303, -4.9397],
    aliases: ['la canada', 'la cañada', 'canada shopping', 'winkelcentrum marbella'],
  },
  {
    id: 'centro-comercial-estepona',
    label: 'winkelcentrum Estepona',
    coords: [36.4248, -5.1567],
    aliases: ['winkelcentrum estepona', 'centro comercial estepona', 'estepona shopping'],
  },

  /* ── Ziekenhuizen ── */
  {
    id: 'hospital-costa-del-sol',
    label: 'Hospital Costa del Sol',
    coords: [36.5031, -4.8691],
    aliases: ['ziekenhuis marbella', 'hospital costa del sol', 'hospital marbella', 'ziekenhuis costa del sol'],
  },
  {
    id: 'hospital-quiron',
    label: 'Hospital Quirónsalud Marbella',
    coords: [36.5141, -4.9101],
    aliases: ['quiron', 'quironsalud', 'ziekenhuis quiron', 'hospital quiron'],
  },
];

/**
 * Haversine afstand in km tussen twee [lat, lon] punten.
 */
function haversine(lat1, lon1, lat2, lon2) {
  const R = 6371;
  const dLat = (lat2 - lat1) * Math.PI / 180;
  const dLon = (lon2 - lon1) * Math.PI / 180;
  const a = Math.sin(dLat / 2) ** 2 +
    Math.cos(lat1 * Math.PI / 180) * Math.cos(lat2 * Math.PI / 180) *
    Math.sin(dLon / 2) ** 2;
  return R * 2 * Math.asin(Math.sqrt(a));
}

/**
 * Geeft voor een project (met coords [lat, lon]) een beknopte string
 * met de 4 dichtstbijzijnde landmarks — geschikt als extra regels in
 * de projectindex zodat de bot kan redeneren over afstanden.
 *
 * Alleen landmarks binnen 30 km worden getoond; per categorie
 * (haven, strand, golf, luchthaven, centrum) hooguit één.
 */
const CATEGORIES = {
  haven: ['haven-estepona', 'puerto-banus', 'haven-marbella', 'sotogrande-marina', 'fuengirola-haven'],
  strand: ['strand-estepona', 'strand-marbella', 'strand-san-pedro', 'strand-fuengirola', 'strand-la-cala'],
  golf:   ['la-quinta-golf', 'valderrama', 'atalaya-golf', 'flamingos-golf', 'la-cala-golf'],
  airport: ['malaga-airport', 'gibraltar-airport'],
  centrum: ['centrum-marbella', 'centrum-estepona', 'centrum-fuengirola', 'centrum-benahavis'],
};

function landmarkDistances(coords) {
  if (!coords) return '';
  let lat, lon;
  if (typeof coords === 'string') {
    [lat, lon] = coords.split(',').map(Number);
  } else if (Array.isArray(coords)) {
    [lat, lon] = coords;
  } else {
    return '';
  }
  if (!lat || !lon) return '';

  const byId = Object.fromEntries(LANDMARKS.map((l) => [l.id, l]));
  const parts = [];

  for (const [cat, ids] of Object.entries(CATEGORIES)) {
    let best = null;
    let bestDist = Infinity;
    for (const id of ids) {
      const lm = byId[id];
      if (!lm) continue;
      const d = haversine(lat, lon, lm.coords[0], lm.coords[1]);
      if (d < bestDist && d <= 30) {
        bestDist = d;
        best = lm;
      }
    }
    if (best) {
      const distStr = bestDist < 1 ? `${Math.round(bestDist * 1000)}m` : `${bestDist.toFixed(1)}km`;
      parts.push(`${best.label} ${distStr}`);
    }
  }

  return parts.length ? `  Afstanden: ${parts.join(' | ')}` : '';
}

/**
 * Zoekt een landmark op basis van een stukje tekst (alias-matching).
 * Geeft { id, label, coords } terug of null.
 * Stopwoorden (van, de, het, het, der, ...) worden weggehaald voor matching.
 */
function normalise(text) {
  return (text || '').toLowerCase()
    .normalize('NFD').replace(/[̀-ͯ]/g, '') // accenten weg
    .replace(/\b(van|de|het|der|den|du|le|la|el|los|las|the|of|in|bij|naar)\b/g, ' ')
    .replace(/[^a-z0-9 ]/g, ' ')
    .replace(/\s+/g, ' ')
    .trim();
}

function findLandmark(text) {
  const q = normalise(text);
  for (const lm of LANDMARKS) {
    for (const alias of lm.aliases) {
      if (q.includes(normalise(alias))) return lm;
    }
  }
  return null;
}

module.exports = { LANDMARKS, haversine, landmarkDistances, findLandmark };
