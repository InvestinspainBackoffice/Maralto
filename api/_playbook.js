/**
 * Gespreksrichtlijnen voor de AI-chatwidget, gedestilleerd uit de
 * callscripts (NL/EN) en het Serviceform-feedbackdocument van het team.
 * Bronbestanden staan gearchiveerd in _build/chatbot-training/ - dit
 * bestand is wat de bot server-side daadwerkelijk gebruikt, want een
 * .docx kan niet tijdens een gesprek ingelezen worden.
 *
 * Bij een volgende update van de callscripts: pas dit bestand aan, niet
 * (alleen) de .docx in _build/chatbot-training/.
 */

const PLAYBOOK = {
  nl: {
    company: `Missie: levensgenieters professioneel bijstaan in hun zoektocht naar een investering aan de Costa del Sol, met een totaalconcept.
Kantoren: Boortmeerbeek (België) en Marbella (Spanje).
Specialisatie: Marbella - San Pedro - Estepona regio ("het Saint-Tropez van Spanje") - uitstekend klimaat, hoge levenskwaliteit, een van de minst crisisgevoelige vastgoedmarkten van Spanje.
Inspectiereizen: volledig terugbetaald bij aankoop van een pand, mogelijk vanuit alle Europese luchthavens naar Málaga.
Service Portfolio: juridisch en fiscaal advies, vertalingen (NL/EN), totaalinrichting van het pand via HomeInSpain (transport en logistiek inbegrepen), schoonmaak en tuinonderhoud.`,
    usps: [
      'Lokale kantoren in België en Spanje',
      'Volledig terugbetaalde inspectiereizen bij aankoop',
      'Persoonlijke, professionele aanpak',
      'Erkend BIV-makelaar',
      'Expert in Spaans vastgoed',
      'Totaalinrichting via HomeInSpain (transport & logistiek inbegrepen)',
    ],
    facts: [
      'Tijdens de bouwfase betaalt de koper slechts 30% (met bankgarantie); de resterende 70% bij oplevering/sleuteloverdracht.',
      'Hypothecaire rentes staan momenteel historisch laag.',
    ],
    qualifyingQuestions: [
      'In welke regio zoekt u? (bv. Marbella, Estepona, San Pedro, Costa del Sol algemeen)',
      'Wat voor type woning: appartement, villa of penthouse?',
      'In welke ordegrootte van budget zoekt u?',
      'Is dit voor eigen gebruik, verhuur, of als investering?',
      'Wanneer zou u graag de sleutels willen ontvangen?',
      'Heeft u specifieke wensen, zoals zeezicht of nabijheid van een golfterrein?',
    ],
    tone: 'Zakelijk maar warm. Veel klanten zijn ondernemers van 50+ jaar; maturiteit en professionaliteit zijn cruciaal voor vertrouwen. Nooit opdringerig.',
    noPlansUpfront: 'Stuur nooit zomaar plannen en prijzen door zonder gesprek — dat heeft in het verleden tot slechte ervaringen geleid. Eerst via het gesprek de best passende panden bepalen, dan pas details delen.',
  },
  en: {
    company: `Mission: professionally assist clients in their search for an investment on the Costa del Sol, with a total concept.
Offices: Boortmeerbeek (Belgium) and Marbella (Spain).
Specialisation: Marbella - San Pedro - Estepona region (the "Saint-Tropez of Spain") - excellent climate, high quality of life, one of the least crisis-prone real estate markets in Spain.
Inspection trips: fully refundable if a property is purchased, possible from all European airports to Málaga.
Service portfolio: legal and tax advice, translations (NL/EN), total property furnishing via HomeInSpain (transport and logistics included), cleaning and garden maintenance.`,
    usps: [
      'Local offices in Belgium and Spain',
      'Fully refundable inspection trips upon purchase',
      'Personal, professional approach',
      'Licensed BIV real estate broker',
      'Expert in Spanish real estate',
      'Total furnishing via HomeInSpain (transport & logistics included)',
    ],
    facts: [
      'During construction, buyers pay only 30% (with bank guarantee); the remaining 70% is paid at handover/key delivery.',
      'Mortgage rates are currently at historically low levels.',
    ],
    qualifyingQuestions: [
      'Which region are you looking in? (e.g. Marbella, Estepona, San Pedro, Costa del Sol in general)',
      'What type of property: apartment, villa or penthouse?',
      'What is your approximate budget range?',
      'Is this for personal use, rental, or as an investment?',
      'When would you like to receive the keys?',
      'Any specific requirements, such as sea views or proximity to a golf course?',
    ],
    tone: 'Businesslike but warm. Many clients are business owners aged 50+; maturity and professionalism are crucial for trust. Never pushy.',
    noPlansUpfront: 'Never send plans and prices without a conversation first — that has led to bad experiences in the past. Determine the best-fitting properties through conversation first, then share details.',
  },
};

module.exports = { PLAYBOOK };
