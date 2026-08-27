---
target: de Zoute Grand Prix partnershippagina
total_score: 21
max_score: 32
na_heuristics: 7,10
p0_count: 0
p1_count: 3
timestamp: 2026-08-27T12-22-29Z
slug: zoute-grand-prix-index-html
---
# Design Critique — Zoute Grand Prix 2026 partnershippagina

**Method:** dual-agent (A: design review · B: detector + browser evidence).

## Design Health Score

| # | Heuristic | Score | Key issue |
|---|-----------|-------|-----------|
| 1 | Visibility of System Status | 3 | 18MB videoblok laadt poster-loos als zwart vlak; taalwissel geeft geen "je bent hier" |
| 2 | Match System / Real World | 3 | Betekenis van de driehoek ("één geïntegreerde partner") staat nergens als tekst |
| 3 | User Control and Freedom | 2 | Autoplay-loop + eeuwig lopende lijn-animatie zonder stopknop; taalwissel enkel via volledige scroll |
| 4 | Consistency and Standards | 3 | Linkdoelen verschillen (_blank vs zelfde tab); medaillons tonen twee "waarheden" (ghost desktop / vol mobiel) |
| 5 | Error Prevention | 3 | Lage foutkans; CTA navigeert weg met alleen browser-back terug |
| 6 | Recognition Rather Than Recall | 2 | Kernprobleem — op desktop ghost-logo's + 13px vage namen; elk medaillon apart hoveren nodig |
| 7 | Flexibility and Efficiency | n/a | Eénmalige persuade-pagina; geen power-user-pad verwacht |
| 8 | Aesthetic and Minimalist Design | 3 | Elegant en ingetogen; verliest punt door dichte hero-paragraaf + desktop-leegte |
| 9 | Error Recovery | 2 | .reveal-secties (driehoek + CTA) starten op opacity:0, enkel via JS; script-hapering verbergt alles stil, geen noscript |
| 10 | Help and Documentation | n/a | Zelf-verklarende pagina met één doel |
| **Totaal** | | **21/32 (66%)** | **Acceptabel** |

na_heuristics: 7, 10.

## Design Specificity Verdict

Deels geauthored. De hero-reveal (curtain-reveal keyframe + video van een onthuld monument) is echt op maat. Máár de visuele wereld is integraal overgenomen uit het Maralto-systeem zonder één Zoute-specifieke cue (geen motorsport, geen Knokke/kust, geen klassieke auto's). Medaillon-foto's = generieke lifestyle-stock. CTA-kaart = IIS-boilerplate. Haal de zegel + één eyebrow-regel weg en het is een standaard "maak kennis met onze bedrijvengroep"-pagina. De Zoute wordt genoemd, niet gevoeld — geen datums, geen locatie, geen "kom langs".

Deterministische scan: exit 2, 14 findings (7 per taal, spiegelbeeldig).
- low-contrast (2x): .btn:hover 4.4:1 (norm 4.5:1)
- undersized-ui-text (6x): eyebrow 9.3-10.4px, footer 9.6px, taalwissellink 9.6px
- all-caps-body (2x): eyebrow — zwak, decoratieve kicker
- gpt-thin-border-wide-shadow (2x advisory): .video-frame 1px border + 60px blur
- flat-type-hierarchy (2x): FALSE POSITIVE — statische engine kan clamp() niet lezen; browser-overlay flagde het niet

Browser-overlay (3 views: NL desktop, EN desktop, NL mobiel): consistent "4 anti-patterns" / 5 instanties. Geen extra findings op mobiel. Live-server na afloop gestopt, git working tree schoon.

## Overall Impression

Mooi gemaakt maar dun van boodschap. Sterke hero-onthulling, daarna een muur gedempt grijze tekst + op desktop bijna een vol scherm lege charcoal, en een driehoek die in ruststand slechts dimme cirkels met spooklogo's toont. De "aha, het is één groep"-payoff komt nooit hard aan. Grootste kans: driehoek zelfverklarend maken in ruststand + mobiele last verlichten (18MB video, tekstdichtheid).

## What's Working

1. De hero-reveal is geauthored, niet getemplatet — curtain-reveal keyframe gekoppeld aan het video-onderwerp.
2. Reduced-motion-afhandeling is werkelijk grondig — elke ruimtelijke transform geneutraliseerd, betekenisdragende opacity/kleur behouden.
3. Touch-vs-muis-logica op de logo-chips (@media hover:hover) is slim — mobiel krijgt meteen volle logo's.

## Priority Issues

### [P1] Hero-video: 18MB, preload=auto, geen poster — mobiel-eerst WhatsApp-publiek
Wat: introductie.mp4 = 18MB (bevestigd), gretige download, geen poster (zwart vlak tot buffer). B zag autoplay-gating.
Waarom: publiek is "grotendeels op gsm via WhatsApp"; CLAUDE.md dwingt WebP-discipline af; poster-loos zwart vak = lege eerste indruk.
Fix: comprimeer naar 2-4MB (720-1080px, H.264 + WebM source), poster toevoegen, preload=metadata of preload=none + play-on-scroll. video aria-hidden + tabindex=-1.
Command: /impeccable optimize

### [P1] Merken-driehoek communiceert niets in ruststand
Wat: logo's op 40% opacity achter 12%-witte chip; namen ~13px; lijnen 0.4-opacity haarlijntjes; betekenis nergens als tekst. Op desktop zweeft de sectie linksboven met scherm leegte.
Waarom: draagt de kernovertuiging; onleesbaar tot je hovert = boodschap verloren voor scanners.
Fix: logo's leesbaar in rust op desktop (vol/≥70% chip, img-opacity ≥0.85); namen ~1rem/--text zwaarder; lijnen sterker + kop "Drie merken, één partner"; op ≥1100px medaillons+driehoek opschalen en centreren.
Command: /impeccable bolder

### [P1] Geen zichtbare focus-indicator op CTA en tekstlinks
Wat: .btn heeft alleen :hover/:active; hero-inline-links + footer-taalwissel leunen op browser-default. Alleen .brand-node heeft :focus-visible. Detector: knop-hover 4.4:1 contrast.
Waarom: toetsenbord-/switch-gebruikers zien niet waar ze staan op de belangrijkste actie (WCAG 2.4.7/2.4.11).
Fix: .btn:focus-visible outline 2px gold, offset 3px; gedeelde a:focus-visible; knop-hoverachtergrond optillen naar ≥4.5:1.
Command: /impeccable harden

### [P2] Social-share-metadata is stuk — distributie is het hele model
Wat: og:image hotlinkt naar WordPress (CLAUDE.md verbiedt dit) en is enkel een logo. Geen twitter:card, geen og:image dimensions, geen hreflang, geen favicon.
Waarom: distributiemodel = "rechtstreeks gedeeld / op social gepost"; gehotlinkt logo rendert als icoontje of niets op WhatsApp/LinkedIn.
Fix: 1200x630 zelf-gehoste share-card onder images/zoute-grand-prix/ via projects.investinspain.be; twitter:card=summary_large_image, og:image:width/height, hreflang NL/EN.
Command: /impeccable harden

### [P2] Dichte hero-paragraaf + zwakke koppenhiërarchie
Wat: ~75-woord gedempt-grijs blok met 3 inline-links, op mobiel gecentreerd/rafelig. H1 32px/300, overtroffen door video. Payoff begraven midden in de paragraaf.
Waarom: koude WhatsApp-link krijgt ~3 seconden; aandacht splitst tussen bewegende video (met eigen woord-overlays) en dichte tekst.
Fix: one-line vette lead + 3-item merkenlijst die de driehoek spiegelt; links uitlijnen op mobiel; H1 groter/zwaarder.
Command: /impeccable clarify

### [P2] Reveal-secties hebben geen no-JS-fallback
Wat: .brand-triangle en .content (incl. CTA) starten op opacity:0, alleen zichtbaar via JS/IntersectionObserver. Beide agents flagden dit. Geen noscript.
Waarom: overtuiging + enige CTA verdwijnen stil en volledig bij een JS-hapering.
Fix: gate de reveal op een .js-klasse op <html>; zonder JS staat alles standaard zichtbaar.
Command: /impeccable harden

## Persona Red Flags

Jordan (first-timer): stille loop-promovideo zonder titel erboven; 75-woord paragraaf nodig om "Silver Partner" te begrijpen; geen datums/locatie/"wat doet IIS er"; op desktop lezen cirkels als decoratie, niet als links.

Casey (distracted mobile): scrolt voorbij video, botst op grijze muur tekst, bounct; lege gaten lezen als "pagina kapot" en nodigen back-swipe uit vóór de CTA; "English"-link ~38x13px te klein; gloeiende puntjes trekken oog maar leiden nergens.

Riley (stress tester): Tab landt eerst ín een paragraaflink; CTA geen focusring; JS uit = driehoek + CTA faden nooit in; 3G = 18MB preload=auto; landscape-telefoon (~740px) = driehoek stapelt verticaal; reduced-motion correct — geen red flag.

Welgestelde 55+ Belgische prospect: "Silver Partner" nooit als prestigieus geframed; nul bewijs (geen evenementfoto's, auto's, testimonials, "X jaar/X families"); medaillon-foto's ogen als stock, niet eigen werk; kleine typografie overal moeilijk voor verouderende ogen; geen persoon om te contacteren, enkel "Bekijk onze projecten".

## Cognitive Load

4 van 8 items falen, 2 partieel. FAIL: chunking (75-woord run-on), one-thing-at-a-time (hover elk medaillon in sequentie), working memory (groep-claim in je hoofd samenstellen), single focus (bewegende video met woord-overlays + dichte paragraaf). PARTIAL: visual hierarchy (video > H1; namen 13px), progressive disclosure (dump of hover-only). PASS: grouping, minimal choices.

## Emotional Journey

Sterke openingspiek (cinematische curtain-reveal), meteen een dal (muur gedempte tekst + op desktop een scherm lege charcoal die als "kapot" leest). De driehoek zou de "aha"-payoff moeten zijn maar is in rust drie dimme cirkels; de eeuwig gloeiende puntjes voegen laaggradige rusteloosheid toe zonder resolutie. CTA sluit rustig maar generiek. Piek-eind: sterke piek, vlak eind. Voorzichtige 55+-koper vertrekt onder de indruk van productiewaarde maar zonder één bewijspunt.

## Minor Observations

- Undersized functionele tekst (bevestigd): eyebrow 9.3-10.4px, footer 9.6px, namen ~13px.
- Inconsistente linkdoelen: medaillons _blank, CTA zelfde tab.
- Merk-section heeft aria-label maar geen zichtbare kop; diagram-betekenis nergens als DOM-tekst.
- scroll-behavior: smooth globaal, niet uitgezet onder prefers-reduced-motion.
- Hero ::before float reserveert 3rem voor ~110px zegel; check de 900-1100px-band op botsing.
- photo-investinspain.webp = 521KB voor 360px-cirkel grotendeels bedekt door chip — trim naar ~150-200KB.
- background-attachment: fixed op de aurora = bekende jank op mobiel Safari — test op echte iPhone.
- Uitroeptekens in NL+EN slotzin iets informeel voor luxe-register.
- gpt-thin-border-wide-shadow advisory op .video-frame: overweeg shadow-blur naar ~36-40px.
- Console: enkel de twee verwachte Vercel-insights 404's; alle assets 200.
- Run-terzijde: Assessment B installeerde 4 ontbrekende parser-packages in ~/.claude/skills/impeccable/scripts/node_modules/ (zonder die viel de detector terug op regex-only).

## Questions to Consider

1. Als je de Zoute-zegel + eyebrow weghaalt, wat zegt dan nog "partner van een klassieke-autoevenement"? Moet palet/textuur/beeld dat dragen i.p.v. één zin?
2. Partnershippagina of "maak kennis met onze groep"-pagina met een zegel op? Geen datums, locatie, "kom langs", evenementfoto's.
3. Voor wie is dit — koude WhatsApp-ontvanger (context) of warme lead (bewijs + persoon)? Bedient nu geen van beide volledig.
4. "Drie merken, één partner" leeft volledig in hover-states + haarlijn-SVG. Zou het concept een gedrukte one-pager overleven?
5. Is een 18MB autoplay-video het juiste middelpunt voor een "grotendeels op mobiel"-publiek, in een repo met WebP-discipline op elke 100KB-foto?
