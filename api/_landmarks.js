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

  /* ══════════════════════════════════════════════════════
     HAVENS / JACHTHAVENS
     ══════════════════════════════════════════════════════ */
  {
    id: 'haven-estepona',
    label: 'haven van Estepona',
    coords: [36.4274, -5.1477],
    aliases: ['haven estepona', 'puerto estepona', 'jachthaven estepona', 'marina estepona', 'port estepona', 'puerto deportivo estepona'],
  },
  {
    id: 'puerto-banus',
    label: 'Puerto Banús',
    coords: [36.4876, -4.9567],
    aliases: ['puerto banus', 'banus', 'puerto de banus', 'haven banus', 'puerto jose banus'],
  },
  {
    id: 'haven-marbella',
    label: 'haven van Marbella',
    coords: [36.5082, -4.8876],
    aliases: ['haven marbella', 'puerto marbella', 'jachthaven marbella', 'marina marbella', 'puerto deportivo marbella'],
  },
  {
    id: 'haven-duquesa',
    label: 'Puerto de La Duquesa',
    coords: [36.3375, -5.2397],
    aliases: ['duquesa', 'puerto duquesa', 'haven duquesa', 'la duquesa', 'marina duquesa', 'manilva haven'],
  },
  {
    id: 'haven-cabopino',
    label: 'haven van Cabopino',
    coords: [36.4957, -4.7638],
    aliases: ['cabopino', 'haven cabopino', 'puerto cabopino', 'marina cabopino', 'jachthaven cabopino'],
  },
  {
    id: 'haven-benalamadena',
    label: 'haven van Benalmádena',
    coords: [36.5981, -4.5186],
    aliases: ['haven benalamadena', 'puerto benalamadena', 'puerto marina benalamadena', 'marina benalamadena', 'benalmadena marina'],
  },
  {
    id: 'haven-fuengirola',
    label: 'haven van Fuengirola',
    coords: [36.5384, -4.6259],
    aliases: ['haven fuengirola', 'puerto fuengirola', 'marina fuengirola', 'jachthaven fuengirola'],
  },
  {
    id: 'sotogrande-marina',
    label: 'Marina Sotogrande',
    coords: [36.2890, -5.2882],
    aliases: ['marina sotogrande', 'haven sotogrande', 'puerto sotogrande', 'sotogrande haven'],
  },

  /* ══════════════════════════════════════════════════════
     STRANDEN
     ══════════════════════════════════════════════════════ */
  {
    id: 'strand-estepona',
    label: 'strand Estepona',
    coords: [36.4239, -5.1440],
    aliases: ['strand estepona', 'playa estepona', 'beach estepona', 'zee estepona', 'paseo maritimo estepona'],
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
    aliases: ['strand san pedro', 'playa san pedro', 'beach san pedro', 'playa linda vista'],
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
  {
    id: 'strand-cabopino',
    label: 'strand Cabopino',
    coords: [36.4929, -4.7618],
    aliases: ['strand cabopino', 'playa cabopino', 'beach cabopino', 'artola duinen', 'dunas artola'],
  },
  {
    id: 'strand-elviria',
    label: 'strand Elviria',
    coords: [36.4992, -4.8051],
    aliases: ['strand elviria', 'playa elviria', 'beach elviria', 'las chapas strand', 'playa las chapas'],
  },
  {
    id: 'strand-benalamadena',
    label: 'strand Benalmádena',
    coords: [36.5978, -4.5209],
    aliases: ['strand benalamadena', 'playa benalamadena', 'beach benalamadena'],
  },
  {
    id: 'strand-torremolinos',
    label: 'strand Torremolinos',
    coords: [36.6121, -4.5090],
    aliases: ['strand torremolinos', 'playa torremolinos', 'la carihuela', 'beach torremolinos'],
  },
  {
    id: 'strand-manilva',
    label: 'strand Manilva',
    coords: [36.3526, -5.2508],
    aliases: ['strand manilva', 'playa manilva', 'beach manilva', 'playa duquesa manilva'],
  },
  {
    id: 'strand-casares',
    label: 'strand Casares Costa',
    coords: [36.3682, -5.2418],
    aliases: ['strand casares', 'playa casares', 'beach casares', 'casares costa strand'],
  },

  /* ══════════════════════════════════════════════════════
     LUCHTHAVENS
     ══════════════════════════════════════════════════════ */
  {
    id: 'malaga-airport',
    label: 'luchthaven Málaga',
    coords: [36.6749, -4.4991],
    aliases: ['malaga airport', 'luchthaven malaga', 'vliegveld malaga', 'airport malaga', 'agp', 'aeropuerto malaga'],
  },
  {
    id: 'gibraltar-airport',
    label: 'luchthaven Gibraltar',
    coords: [36.1502, -5.3495],
    aliases: ['gibraltar airport', 'luchthaven gibraltar', 'vliegveld gibraltar', 'aeropuerto gibraltar'],
  },

  /* ══════════════════════════════════════════════════════
     STADSCENTRA
     ══════════════════════════════════════════════════════ */
  {
    id: 'centrum-marbella',
    label: 'centrum Marbella',
    coords: [36.5093, -4.8843],
    aliases: ['centrum marbella', 'center marbella', 'casco antiguo marbella', 'old town marbella', 'marbella centrum', 'stad marbella', 'marbella stad'],
  },
  {
    id: 'centrum-estepona',
    label: 'centrum Estepona',
    coords: [36.4274, -5.1467],
    aliases: ['centrum estepona', 'center estepona', 'casco antiguo estepona', 'old town estepona', 'estepona centrum', 'stad estepona', 'estepona stad'],
  },
  {
    id: 'centrum-san-pedro',
    label: 'centrum San Pedro',
    coords: [36.4850, -5.0700],
    aliases: ['centrum san pedro', 'san pedro centrum', 'center san pedro', 'san pedro stad'],
  },
  {
    id: 'centrum-fuengirola',
    label: 'centrum Fuengirola',
    coords: [36.5399, -4.6249],
    aliases: ['centrum fuengirola', 'center fuengirola', 'fuengirola centrum', 'fuengirola stad'],
  },
  {
    id: 'centrum-benahavis',
    label: 'centrum Benahavís',
    coords: [36.5224, -5.0478],
    aliases: ['centrum benahavis', 'center benahavis', 'benahavis centrum', 'benahavis dorp', 'dorp benahavis'],
  },
  {
    id: 'centrum-mijas-pueblo',
    label: 'Mijas Pueblo',
    coords: [36.5977, -4.6380],
    aliases: ['mijas pueblo', 'centrum mijas', 'mijas dorp', 'white village mijas', 'wit dorp mijas'],
  },
  {
    id: 'centrum-casares',
    label: 'centrum Casares',
    coords: [36.4336, -5.2762],
    aliases: ['centrum casares', 'casares centrum', 'casares dorp', 'casares pueblo'],
  },
  {
    id: 'centrum-manilva',
    label: 'centrum Manilva',
    coords: [36.3772, -5.2460],
    aliases: ['centrum manilva', 'manilva centrum', 'manilva dorp', 'manilva pueblo'],
  },
  {
    id: 'centrum-benalamadena',
    label: 'Benalmádena Pueblo',
    coords: [36.5935, -4.5183],
    aliases: ['centrum benalamadena', 'benalamadena centrum', 'benalamadena pueblo', 'benalamadena dorp'],
  },
  {
    id: 'centrum-sotogrande',
    label: 'centrum Sotogrande',
    coords: [36.2970, -5.2853],
    aliases: ['centrum sotogrande', 'sotogrande centrum', 'sotogrande dorp'],
  },
  {
    id: 'la-linea',
    label: 'La Línea de la Concepción',
    coords: [36.1724, -5.3480],
    aliases: ['la linea', 'la linea concepcion', 'la linea gibraltar'],
  },

  /* ══════════════════════════════════════════════════════
     GOLFBANEN
     ══════════════════════════════════════════════════════ */
  {
    id: 'estepona-golf',
    label: 'Estepona Golf',
    coords: [36.4213, -5.1912],
    aliases: ['estepona golf', 'club estepona golf'],
  },
  {
    id: 'el-paraiso-golf',
    label: 'El Paraíso Golf',
    coords: [36.4667, -5.0892],
    aliases: ['el paraiso golf', 'paraiso golf', 'villa padierna paraiso'],
  },
  {
    id: 'flamingos-golf',
    label: 'Los Flamingos Golf',
    coords: [36.4836, -5.0519],
    aliases: ['flamingos golf', 'los flamingos golf', 'villa padierna golf', 'flamingos'],
  },
  {
    id: 'atalaya-golf',
    label: 'Atalaya Golf',
    coords: [36.4801, -5.0292],
    aliases: ['atalaya golf', 'atalaya golf country club', 'atalaya'],
  },
  {
    id: 'guadalmina-golf',
    label: 'Guadalmina Golf',
    coords: [36.4730, -5.0580],
    aliases: ['guadalmina golf', 'real club guadalmina', 'guadalmina sur', 'guadalmina norte'],
  },
  {
    id: 'la-quinta-golf',
    label: 'La Quinta Golf',
    coords: [36.5080, -4.9878],
    aliases: ['la quinta golf', 'la quinta'],
  },
  {
    id: 'los-arqueros-golf',
    label: 'Los Arqueros Golf',
    coords: [36.5100, -5.0378],
    aliases: ['los arqueros golf', 'arqueros golf', 'los arqueros'],
  },
  {
    id: 'los-naranjos-golf',
    label: 'Los Naranjos Golf',
    coords: [36.5062, -4.9472],
    aliases: ['los naranjos golf', 'naranjos golf', 'los naranjos'],
  },
  {
    id: 'marbella-golf-cc',
    label: 'Marbella Golf & Country Club',
    coords: [36.5052, -4.9234],
    aliases: ['marbella golf country club', 'marbella golf club', 'marbella gcc'],
  },
  {
    id: 'santa-clara-golf',
    label: 'Santa Clara Golf',
    coords: [36.5174, -4.9037],
    aliases: ['santa clara golf', 'santa clara golf marbella'],
  },
  {
    id: 'rio-real-golf',
    label: 'Río Real Golf',
    coords: [36.5181, -4.8396],
    aliases: ['rio real golf', 'rio real', 'real golf rio real'],
  },
  {
    id: 'cabopino-golf',
    label: 'Cabopino Golf',
    coords: [36.5021, -4.7753],
    aliases: ['cabopino golf', 'golf cabopino'],
  },
  {
    id: 'la-cala-golf',
    label: 'La Cala Golf Resort',
    coords: [36.5219, -4.7363],
    aliases: ['la cala golf', 'la cala resort', 'cala golf'],
  },
  {
    id: 'mijas-golf',
    label: 'Mijas Golf',
    coords: [36.5419, -4.7128],
    aliases: ['mijas golf', 'mijas golf international', 'golf mijas', 'los lagos golf', 'los olivos golf'],
  },
  {
    id: 'torrequebrada-golf',
    label: 'Torrequebrada Golf',
    coords: [36.5948, -4.5391],
    aliases: ['torrequebrada golf', 'golf torrequebrada', 'real torrequebrada'],
  },
  {
    id: 'la-duquesa-golf',
    label: 'La Duquesa Golf',
    coords: [36.3692, -5.2387],
    aliases: ['la duquesa golf', 'duquesa golf', 'golf duquesa'],
  },
  {
    id: 'finca-cortesin-golf',
    label: 'Finca Cortesín Golf',
    coords: [36.3753, -5.2397],
    aliases: ['finca cortesin', 'finca cortesin golf', 'cortesin golf', 'cortesín'],
  },
  {
    id: 'valderrama',
    label: 'Valderrama Golf',
    coords: [36.2842, -5.2951],
    aliases: ['valderrama', 'valderrama golf', 'real club valderrama', 'ryder cup'],
  },
  {
    id: 'almenara-golf',
    label: 'Almenara Golf',
    coords: [36.2920, -5.2970],
    aliases: ['almenara golf', 'golf almenara', 'sotogrande almenara'],
  },
  {
    id: 'san-roque-golf',
    label: 'San Roque Golf',
    coords: [36.2483, -5.3147],
    aliases: ['san roque golf', 'club san roque', 'golf san roque'],
  },
  {
    id: 'alcaidesa-golf',
    label: 'Alcaidesa Golf',
    coords: [36.1900, -5.3617],
    aliases: ['alcaidesa golf', 'golf alcaidesa', 'la alcaidesa golf'],
  },
  {
    id: 'lauro-golf',
    label: 'Lauro Golf',
    coords: [36.6267, -4.6791],
    aliases: ['lauro golf', 'golf lauro', 'alhaurin golf'],
  },

  /* ══════════════════════════════════════════════════════
     INTERNATIONALE SCHOLEN
     ══════════════════════════════════════════════════════ */
  {
    id: 'aloha-college',
    label: 'Aloha College',
    coords: [36.5062, -4.9432],
    aliases: ['aloha college', 'aloha school', 'college aloha', 'school aloha marbella'],
  },
  {
    id: 'swans-school',
    label: 'Swans International School',
    coords: [36.4935, -5.0447],
    aliases: ['swans school', 'swans international', 'swans san pedro', 'internationale school san pedro'],
  },
  {
    id: 'laude-san-pedro',
    label: 'Laude San Pedro International College',
    coords: [36.4870, -5.0540],
    aliases: ['laude san pedro', 'laude school', 'laude college', 'san pedro international school'],
  },
  {
    id: 'sotogrande-international-school',
    label: 'Sotogrande International School',
    coords: [36.2756, -5.2935],
    aliases: ['sotogrande international school', 'sis sotogrande', 'internationale school sotogrande'],
  },
  {
    id: 'ise-estepona',
    label: 'International School Estepona',
    coords: [36.4320, -5.1560],
    aliases: ['ise estepona', 'international school estepona', 'internationale school estepona'],
  },
  {
    id: 'eic-marbella',
    label: 'English International College',
    coords: [36.5251, -4.7381],
    aliases: ['eic', 'english international college', 'english college marbella', 'english school marbella'],
  },
  {
    id: 'british-school-marbella',
    label: 'The British School of Marbella',
    coords: [36.5180, -4.8720],
    aliases: ['british school marbella', 'british school', 'british college marbella'],
  },
  {
    id: 'mayfair-academy',
    label: 'Mayfair International Academy',
    coords: [36.5251, -4.7381],
    aliases: ['mayfair academy', 'mayfair international', 'mayfair school mijas'],
  },

  /* ══════════════════════════════════════════════════════
     ZIEKENHUIZEN / KLINIEKEN
     ══════════════════════════════════════════════════════ */
  {
    id: 'hospital-costa-del-sol',
    label: 'Hospital Costa del Sol',
    coords: [36.5031, -4.8691],
    aliases: ['ziekenhuis marbella', 'hospital costa del sol', 'hospital marbella', 'ziekenhuis costa del sol', 'hcos'],
  },
  {
    id: 'hospital-quiron',
    label: 'Hospital Quirónsalud Marbella',
    coords: [36.5141, -4.9101],
    aliases: ['quiron', 'quironsalud', 'ziekenhuis quiron', 'hospital quiron', 'clinica quiron'],
  },
  {
    id: 'hospital-xanit',
    label: 'Hospital Vithas Xanit',
    coords: [36.5940, -4.5448],
    aliases: ['xanit', 'vithas xanit', 'hospital xanit', 'ziekenhuis benalamadena', 'xanit benalamadena'],
  },
  {
    id: 'hospital-estepona',
    label: 'Hospital de Estepona',
    coords: [36.4248, -5.1467],
    aliases: ['ziekenhuis estepona', 'hospital estepona', 'clinica estepona'],
  },

  /* ══════════════════════════════════════════════════════
     WINKELCENTRA / LIFESTYLE
     ══════════════════════════════════════════════════════ */
  {
    id: 'la-canada',
    label: 'La Cañada Shopping',
    coords: [36.5303, -4.9397],
    aliases: ['la canada', 'la cañada', 'canada shopping', 'winkelcentrum marbella', 'parque comercial canada'],
  },
  {
    id: 'laguna-village',
    label: 'Laguna Village Estepona',
    coords: [36.4443, -5.1248],
    aliases: ['laguna village', 'laguna village estepona', 'laguna estepona'],
  },
  {
    id: 'miramar-fuengirola',
    label: 'Centro Comercial Miramar',
    coords: [36.5394, -4.6285],
    aliases: ['miramar', 'centro comercial miramar', 'winkelcentrum fuengirola', 'miramar fuengirola'],
  },
  {
    id: 'el-corte-ingles-marbella',
    label: 'El Corte Inglés Marbella',
    coords: [36.5172, -4.9178],
    aliases: ['el corte ingles marbella', 'corte ingles marbella', 'corte ingles'],
  },
  {
    id: 'higueron-west',
    label: 'Centro Higueron',
    coords: [36.5822, -4.5734],
    aliases: ['higueron', 'centro higueron', 'higueron west', 'higueron resort shopping'],
  },
  {
    id: 'nikki-beach',
    label: 'Nikki Beach Marbella',
    coords: [36.5022, -4.8849],
    aliases: ['nikki beach', 'nikki beach marbella', 'nikki'],
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
 * Geeft voor een project (met coords string "lat,lon") een beknopte string
 * met de dichtstbijzijnde landmarks per categorie — als extra regels in
 * de projectindex zodat de bot kan redeneren over afstanden.
 *
 * Alleen landmarks binnen 30 km worden getoond; per categorie hooguit één.
 */
const CATEGORIES = {
  haven:   ['haven-estepona','puerto-banus','haven-marbella','haven-duquesa','haven-cabopino','haven-benalamadena','haven-fuengirola','sotogrande-marina'],
  strand:  ['strand-estepona','strand-marbella','strand-san-pedro','strand-fuengirola','strand-la-cala','strand-cabopino','strand-elviria','strand-benalamadena','strand-torremolinos','strand-manilva','strand-casares'],
  golf:    ['estepona-golf','el-paraiso-golf','flamingos-golf','atalaya-golf','guadalmina-golf','la-quinta-golf','los-arqueros-golf','los-naranjos-golf','marbella-golf-cc','santa-clara-golf','rio-real-golf','cabopino-golf','la-cala-golf','mijas-golf','torrequebrada-golf','la-duquesa-golf','finca-cortesin-golf','valderrama','almenara-golf','san-roque-golf','alcaidesa-golf','lauro-golf'],
  airport: ['malaga-airport','gibraltar-airport'],
  centrum: ['centrum-marbella','centrum-estepona','centrum-san-pedro','centrum-fuengirola','centrum-benahavis','centrum-mijas-pueblo','centrum-casares','centrum-manilva','centrum-benalamadena','centrum-sotogrande'],
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
 * Stopwoorden verwijderen voor robuuste alias-matching.
 */
function normalise(text) {
  return (text || '').toLowerCase()
    .normalize('NFD').replace(/[̀-ͯ]/g, '') // accenten weg
    .replace(/\b(van|de|het|der|den|du|le|la|el|los|las|the|of|in|bij|naar|aan)\b/g, ' ')
    .replace(/[^a-z0-9 ]/g, ' ')
    .replace(/\s+/g, ' ')
    .trim();
}

/**
 * Zoekt een landmark op basis van een stukje tekst (alias-matching).
 * Geeft { id, label, coords, aliases } terug of null.
 */
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
