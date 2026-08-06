/**
 * Gedeelde helper om een lead server-side door te sturen naar Zapier.
 *
 * Gebruikt door api/lead.js (de gewone formulieren) en api/chat.js (leads
 * die de AI-chat vastlegt), zodat de Zapier-URL nergens in code die naar de
 * browser gaat voorkomt - alleen hier, server-side.
 *
 * Bewust nooit een fout laten doorwerken naar de aanroeper: een haperende
 * Zap mag het gesprek of de formulierflow niet breken. De aanroeper krijgt
 * gewoon true/false terug.
 */
const ZAPIER_LEAD_URL = 'https://hooks.zapier.com/hooks/catch/8344712/44ei8hj/';

// Veiligheidsklep voor lokaal/handmatig testen: met ZAPIER_DRY_RUN=1 wordt
// nooit echt gepost, enkel gelogd. _build/devserver.js zet dit standaard aan
// zodat lokaal testen nooit ongemerkt een echte lead in de sheet zet - dat
// was precies wat er tijdens het bouwen van deze functie zelf fout ging.
async function forwardToZapier(payload) {
  if (process.env.ZAPIER_DRY_RUN === '1') {
    console.log('[zapier:dry-run] zou versturen:', JSON.stringify(payload));
    return true;
  }
  try {
    await fetch(ZAPIER_LEAD_URL, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(payload),
    });
    return true;
  } catch (e) {
    return false;
  }
}

module.exports = { forwardToZapier };
