---
title: Vragenlijst techniek (7 november 2026)
---
> Momentopname van 2026-11-07, Claude-project Techniek. Terug naar [Techniek](../techniek.html). [BESLISSINGEN.md](https://github.com/peapickers/postershoppeapickers/blob/main/BESLISSINGEN.md), de [beslissingen van 7 november 2026](../boekhouder/beslissingen-2026-11-07.html) en de vragenlijsten van de [boekhouder](../boekhouder/vragenlijst-2026-11-07.html), de [jurist](../jurist/vragenlijst-2026-11-07.html) en [marketing](../marketing/vragenlijst-2026-11-07.html) gaan voor. Geen juridisch of fiscaal advies. Alle bedragen van diensten zijn ordegroottes van hun tarievenpagina's (november 2026), na te kijken vóór de keuze.

# Vragenlijst techniek voor de oprichter

Datum: 2026-11-07 · Rol: Techniek · Codes: VT1 tot VT14 (vragen), T22 en verder (actiepunten)

**Kort.** De site kan de herroepingsknop zelf tonen (formulier in 2 stappen), maar een statische site kan geen e-mail versturen en niets bewaren. Daarvoor is een kleine dienst nodig. Dat kan gratis (VT1), maar vraagt een eigen domeinnaam (T07). Verder: waar we 10 jaar bewaren (VT2), in welk formaat de boekhouding inleest (VT3, VT4), en hoe de Public Ledger de lening, de betaaldagen en Tweede kans toont (VT8 tot VT10). Het bouwen staat stil tot je antwoordt.

Wat al beantwoord is, vragen we niet opnieuw: betaaldag de 15de, weekend de werkdag ervoor (VB8); lening als bedrag per maand zonder naam, bruikleen zonder bedrag (VB13); 0 Limited bij de start (VB7, VM6); klant betaalt het terugsturen (VJ3); terugbetaling na ontvangst of verzendbewijs (VJ4); Tweede kans 80 % en 50/50 als filtergroep (VJ19, VM3); geen gratis teruggave in Gent (VM2); geen gastheer, zetel of adres online (VM4, VM10); oproep medebestuurder nog niet online (VM5); printshop alleen "Geen herroepingsrecht" (VM14, wacht op J22).

★ = houdt de webshop (maart 2027) tegen.

## Vragen

| # | Vraag of onzekerheid | Waarom het ertoe doet | Onze veronderstelling of voorstel | Antwoord Jonas |
| --- | --- | --- | --- | --- |
| VT1 ★ | **Welke dienst verstuurt de ontvangstbevestiging** na "Herroeping bevestigen", en wat mag dat kosten? (ZB08) | De bevestiging moet meteen vertrekken, met inhoud, datum en uur. GitHub Pages kan geen mail sturen. Een mailto-link of een automatisch antwoord van Proton bevat de inhoud niet of komt niet "meteen" (veronderstelling). | **Cloudflare Workers** (gratis tot 100.000 oproepen per dag) ontvangt het formulier, **Brevo** (gratis tot 300 mails per dag, gegevens in Frankrijk en Duitsland) verstuurt de mail. Kost: € 0 per maand, plus een eigen domeinnaam (ca. € 10 tot 15 per jaar, T07) als afzender. Alternatieven: Formspree (gratis tot 50 inzendingen per maand; automatisch antwoord wellicht betalend, na te kijken), Resend (gratis 3.000 mails per maand, 100 per dag; gegevensregio niet duidelijk). | |
| VT2 ★ | **Waar bewaren we** herroepingsverzoeken en bevestigingen **10 jaar**? (ZB09) | Fiscale bewaartermijn bij elke terugbetaling (BESLISSINGEN.md, te bevestigen door de boekhouder). Brevo en Cloudflare zijn geen archief. Het moet ook leesbaar blijven na een wissel van dienst. | Elke bevestiging gaat ook als kopie naar de mailbox van de vzw (Proton). Elke maand een export (pdf of eml) naar de map Administratie en naar de versleutelde schijven, met een lijn in het logboek. Nooit in de repo of de Public Ledger. Wissen na 10 jaar, in de halfjaarlijkse controle. | |
| VT3 ★ | **Welk exportformaat** voor de transacties, zolang de software van de boekhouder niet gekozen is (ZB03)? | Je boekt zelf (D1). Wat je niet kunt inlezen, tik je over. Snipcart, Mollie en de bank leveren elk een eigen bestand. | Bank: **CODA**, het Belgische standaardformaat dat boekhoudsoftware inleest (KBC, Odoo). Mollie: het uitbetalingsrapport als CSV. Daarbovenop één eigen CSV per maand (datum, soort, werkcode, ontvangen, betaald, Materiaalkost, Auteursrechten bruto, vzw peapickers, lening), afgeleid van de Public Ledger. Scheidingsteken en kolommen pas vastleggen na de keuze van de software. | |
| VT4 ★ | **Export Auteursrechten per auteur** (273S, fiche 281.45): waar staat de koppeling werkcode ↔ auteur? | De Public Ledger toont nooit wie welk bedrag krijgt. Toch heb je per auteur per kwartaal bruto, voorheffing en netto nodig. | Een klein script op je eigen computer leest de Public Ledger en een privébestand "werkcode → auteurcode". Het maakt per kwartaal een tabel per auteur. Het privébestand staat alleen op de versleutelde schijven (zoals de originelen), niet in een cloud en niet in de repo. Rijksregisternummers blijven in de software van de boekhouder. | |
| VT5 ★ | **Wanneer en op wiens naam** maken we de accounts (Cloudflare, Brevo, domein)? | Een account op je eigen naam vóór de oprichting bindt jou persoonlijk (VB9: geen kosten van vóór de oprichting). Wie de sleutels heeft, moet ook bij uitval kunnen stilzetten (T12, ZB21). | Nu bouwen en testen met de voorbeeldmodus (niets versturen). Echte accounts op naam van vzw peapickers, met het vzw-mailadres, na de oprichting (januari 2027). Tweestapsverificatie, sleutels in een kluis die de medebestuurder kan openen. | |
| VT6 ★ | **Wat toont de knop nu**, zolang de webshop niet open is? | BESLISSINGEN.md: op elke pagina. Maar nu wordt niets verkocht, dus er valt niets te herroepen. | De link "Hier de overeenkomst herroepen" staat nu al in de footer. Het formulier werkt, maar verstuurt en bewaart niets: het toont alleen de mail die de klant zou krijgen. Eén schakelaar in `_config.yml` zet het echte versturen aan. | |
| VT7 ★ | **Welk bestelnummer** vult de klant in? | Snipcart geeft een eigen nummer. Plan B (overschrijving) maakt een nummer PP-… Het formulier en de mail moeten hetzelfde nummer tonen als de bevestiging van de bestelling en het kassabonkaartje. | Het Snipcart-nummer, ook op het kassabonkaartje. Bij overschrijving het PP-nummer. Het formulier aanvaardt beide en controleert niets automatisch: de oprichter zoekt de bestelling op. | |
| VT8 ★ | **Klantteksten van de jurist** (J15) zijn er nog niet. Mag de pagina Herroepen nu online met de tekst van marketing (tekst 2) en een duidelijke melding "Ontwerptekst"? | Zonder pagina is er geen knop op elke pagina. Met een pagina staat er een tekst online die nog niet nagekeken is. | Ja: online met de melding "Ontwerptekst, nog na te kijken door de jurist en de advocaat". Wat tussen vierkante haken staat (adres, terugbetaling van de standaardleverkost), laten we weg of tonen we als "[volgt]". | |
| VT9 | **In welk kwartaal** tellen de Auteursrechten van een verkoop vlak voor het einde van een kwartaal? | Auteursrechten tellen pas na de herroepingstermijn (J19, stappenplan v4, 4.3). Een Poster geleverd op 25 juni is pas op 9 juli definitief. | Ze tellen in het kwartaal waarin de 14 dagen na de levering aflopen. Die van 25 juni gaan dus mee op 15 oktober, niet op 15 juli. "Nog uit te betalen" in de Public Ledger toont beide apart: "na de herroepingstermijn" en "nog in de termijn". | |
| VT10 | **Voorbeeldcijfers in de Public Ledger**: mogen we de fictieve handelingen herschrijven? | De voorbeelden tonen nog oude prijzen (€ 15,70), een gift van materiaal, een Limited in april en een uitbetaling op 5 juli. Dat klopt niet meer met VB4, VB7, VB8 en BESLISSINGEN.md. | Ja: nieuwe fictieve reeks voor 2027 met de prijzen van nu, een lijn "bruikleen" zonder bedrag, elke maand "lening oprichter", 0 Limited, 2 herroepingen waarvan 1 doorverkocht in Tweede kans, uitbetaling op 15 juli. De oude reeks blijft in de Git-geschiedenis. Bovenaan de Public Ledger een tabel "Lening oprichter per maand" (gestort, terugbetaald, openstaand). | |
| VT11 | **Tweede kans in de webshop**: hoe ziet één teruggestuurde Poster eruit? | Elke teruggestuurde Poster is uniek (maat en papier liggen vast), maar hoort bij een werk dat ook als gewone Poster te koop is. | Een eigen kaart in de filtergroep Tweede kans, met het label "teruggestuurd" en de prijs ("€ 12,10, was € 15,10"). De kaart opent de productpagina van het werk, met een derde keuze "Tweede kans" naast Poster. Maximaal 1 in de mand. Na de verkoop zet de oprichter de regel in `_data/tweede-kans.csv` op "verkocht". | |
| VT12 | **Limited verbergen**: alleen de keuze en de filter, of ook de uitleg? | VM6 verbergt de keuze en de filtergroep. Prijsopbouw en Deelnemen? leggen Limited nog uit. | Eén schakelaar `limited-actief: false` in `_config.yml` verbergt de keuze en de filtergroep. De uitleg op Prijsopbouw en Deelnemen? blijft, met de zin "Limited volgt later". Zet je de schakelaar op true, dan is alles terug. | |
| VT13 | **Download van de Public Ledger** als CSV, voor iedereen? | Absolute transparantie (kenmerk 1). Een bestand is ook handig om zelf in te lezen (VT3). | Ja: een knop "Download (CSV)" op de Public Ledger, met dezelfde kolommen als op de site, zonder persoonsgegevens. | |
| VT14 | **Publiek domein**: nu al een pagina bouwen of later? | BESLISSINGEN.md wil een aparte pagina bij Posters. De site zegt nog "worden niet verkocht". Er is nog geen werk nagekeken als "zeker vrij in België". | Nu alleen de zin aanpassen: "krijgen later een eigen pagina bij Posters, aan 4 × M, zonder Auteursrechten". De pagina bouwen zodra het eerste werk nagekeken is (M40). | |

## Todo voor Jonas

- [ ] VT1 tot VT8 beantwoorden (★), daarna de rest.
- [ ] Een domeinnaam kiezen (T07): nodig als afzender van de bevestiging (VT1) en voor de QR-codes.
- [ ] Bij de keuze van de boekhouder vragen welk importformaat de software leest (VT3), en of hij de bewaring van herroepingen 10 jaar bevestigt (VT2).

## Actiepunten voor de compiler

| ID | § | Actie | Prio | Rol | Hangt af van |
| --- | --- | --- | --- | --- | --- |
| T22 | VT1, VT6 | Herroepingspagina en link in de footer van elke pagina (2 stappen, voorbeeldmodus). Uitvoering van ZB08 voor het zichtbare deel. | H | Techniek | VT6, VT8 |
| T23 | VT1, VT5 | Dienst voor de ontvangstbevestiging bouwen en testen (endpoint in `_config.yml`), kopie naar de mailbox van de vzw. Uitvoering van ZB08. | H | Techniek | VT1, VT5, T07 |
| T24 | VT2 | Maandelijkse export van herroepingen naar Administratie en de versleutelde schijven; lijn in het logboek; wissen na 10 jaar. Uitvoering van ZB09. | M | Techniek, Boekhouder | VT2, T23 |
| T25 | VT8 | Klantteksten van de jurist (J15) op de pagina Herroepen, in de mand en in de privacyverklaring zetten; melding "Ontwerptekst" weghalen. | H | Techniek | J15 |
| T26 | VT3 | Maandelijkse CSV-export van transacties, afgeleid van de Public Ledger; kolommen afstemmen op de software van de boekhouder. | H | Techniek, Boekhouder | VT3, ZB03 |
| T27 | VT4 | Script "Auteursrechten per auteur per kwartaal" (lokaal, privébestand werkcode → auteur), voor de 273S en de fiche 281.45. | M | Techniek | VT4, ZB03 |
| T28 | VT9, VT10 | Public Ledger: rubriek "lening oprichter" per maand, lijn bruikleen, betaaldagen de 15de (weekend: werkdag ervoor), "Nog uit te betalen" vanaf 15 juli 2027. Uitvoering van ZB22. | H | Techniek | VT9, VT10 |
| T29 | VT11 | Tweede kans: filtergroep, label "teruggestuurd", keuze in het bestelvak, Prijsopbouw 50/50, tekst bij een lege lijst (M31). | H | Techniek | VT11 |
| T30 | VT12 | Schakelaar Limited (M34); aanzetten zodra de eerste Limited gepland is (J21). | H | Techniek | VT12 |
| T31 | VM4, tekst 5 en 7 | Over, Deelnemen?, Prijsopbouw en Bestellen en leveren bijwerken met de teksten van marketing (M32, M35). | H | Techniek | |
| T32 | VT14 | Pagina publiek domein bij Posters (M40). | M | Techniek, Marketing | VT14 |
| T33 | VM14 | Melding "Geen herroepingsrecht" in de printshop, alleen waar de jurist zegt dat het moet (M42). | M | Techniek | J22 |

ZB08 (herroepingsknop) en ZB09 (10 jaar bewaren) uit de [beslissingen van 7 november](../boekhouder/beslissingen-2026-11-07.html) komen terug in VT1, VT2, T22 tot T24.

## Bronnen

- Cloudflare Workers, gratis tot 100.000 oproepen per dag: [Cloudflare, Workers pricing](https://developers.cloudflare.com/workers/platform/pricing/); [DEV Community, Cloudflare Workers free tier](https://dev.to/0012303/cloudflare-workers-has-a-free-tier-100k-requestsday-at-the-edge-with-kv-r2-and-d1-52k9).
- Brevo, gratis 300 mails per dag, gegevens in Frankrijk en Duitsland: [Brevo, email API](https://www.brevo.com/en/features/email-api/); [CaptainDNS, Brevo technical guide](https://www.captaindns.com/en/blog/brevo-transactional-email-technical-guide).
- Resend, gratis 3.000 mails per maand en 100 per dag: [Resend, pricing](https://resend.com/pricing); [Automation Atlas, Resend free tier 2026](https://automationatlas.io/answers/resend-free-tier-explained-2026/).
- Formspree, gratis 50 inzendingen per maand: [Formspree, account limits](https://help.formspree.io/articles/account-management/account-limits); [splitforms, Formspree free plan limits](https://splitforms.com/formspree-free-plan-limits). Of het automatisch antwoord betalend is: veronderstelling, na te kijken.
- CODA als standaard voor bankafschriften in Belgische boekhoudsoftware: [KBC, CODA](https://www.kbc.be/ondernemen/nl/product/betalen-en-betaald-worden/rekeninginformatie/coda.html); [Odoo, CODA](https://www.odoo.com/documentation/user/9.0/nl/accounting/bank/feeds/coda.html).
- Herroepingsknop en ontvangstbevestiging: zie de bronnen in de [vragenlijst jurist](../jurist/vragenlijst-2026-11-07.html).
