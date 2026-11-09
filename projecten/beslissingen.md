---
title: Beslissingenregister
---
# Beslissingenregister

Eén plek met alle beslissingen, in gewone woorden. Elke regel heeft een code `JJJJ-MM-DD_Project<nr>`, een korte titel en wat er geldt. Cijfers en uitwerking staan in [BESLISSINGEN.md](https://github.com/peapickers/postershoppeapickers/blob/main/BESLISSINGEN.md) (postershop). Dit register is de index, geen kopie.

## Werkwijze

1. Een project dat iets beslist, voegt **één regel** toe onderaan de tabel hieronder. Geen aparte momentopname meer.
2. Code = datum van de beslissing + naam van het project + volgnummer van dat project (`2026-11-07_Jurist4`). Eén nummer per beslissing, niet per vragenlijst.
3. De titel zegt in gewone woorden wat beslist is. In tekst nooit de kale code gebruiken, altijd de titel (code hooguit tussen haakjes).
4. Vervangt de beslissing een oudere, zet dan die code in "Vervangt" en zet bij de oude regel de status op "vervangen". Nooit regels verwijderen.
5. Status: `geldt`, `vervangen`, `voorlopig` of `open`. Kolom "In BESLISSINGEN.md": ja of nee.
6. Controle zonder Claude: `python3 scripts/beslissingen-check.py` (dubbele of ontbrekende codes, verwijzingen naar bestaande codes, lijst van wat nog niet in BESLISSINGEN.md staat).
7. De oude momentopnames blijven als archief en hoeven niet meer gelezen te worden: [boekhouder 7-11](boekhouder/beslissingen-2026-11-07.html), [ondernemingsplan 7-11 avond](ondernemingsplan/beslissingen-2026-11-07-avond.html), [ondernemingsplan 8-11](ondernemingsplan/beslissingen-2026-11-08.html). De oude codes (D1, V1, ...) staan in de laatste kolom.

## Register

| Code | Titel | Wat geldt | Status | Vervangt | In BESLISSINGEN.md | Oude code |
| --- | --- | --- | --- | --- | --- | --- |
| 2026-11-07_Boekhouder1 | Boekhouding in zelfbeheer | De oprichter boekt en doet alle aangiftes zelf. | geldt | | ja | D1 |
| 2026-11-07_Boekhouder2 | ITAA-boekhouder controleert | Vaste maandvergoeding, minstens 1 controle per jaar (vóór 31 december en vóór de neerlegging). | geldt | | ja | D2 |
| 2026-11-07_Boekhouder3 | Software van de boekhouder | Niet Accountable; de software die de boekhouder gebruikt. | geldt | | ja | D3 |
| 2026-11-07_Boekhouder4 | Vereenvoudigde boekhouding | Tenzij de boekhouder dubbel aanraadt. | geldt | | ja | D4 |
| 2026-11-07_Boekhouder5 | Productieplek max. € 150 per maand | Een paar m² bij een bestaand bedrijf. | vervangen | | ja | D5 |
| 2026-11-07_Boekhouder6 | Zetel op productieplek of bij familie | Liefst op de productieplek. | vervangen | | ja | D6 |
| 2026-11-07_Boekhouder7 | Extern gedeeld pand | Zetel daar, geen zetel bij familie. | vervangen | | ja | D7 |
| 2026-11-07_Boekhouder8 | Lening niet nodig bij extern pand | Lening en overname van materiaal niet nodig. | vervangen | | ja | D8 |
| 2026-11-07_Boekhouder9 | Medebestuurder blijft nodig | Minstens 2 bestuurders, geen "niet-uitvoerend" bestuurder. | geldt | | ja | D9 |
| 2026-11-07_Boekhouder10 | 14 dagen herroepingsrecht met herroepingsknop | Voor Poster en Limited; bewaren 10 jaar. | geldt | | ja | D10 |
| 2026-11-07_Boekhouder11 | Auteurs enkel uit België | Tot de boekhouder anders adviseert. | geldt | | ja | D11 |
| 2026-11-07_Compiler1 | Oprichter drukt zelf, kosteloos | Als particulier, buiten de vzw; geen productieplek. | geldt | 2026-11-07_Boekhouder5 | ja | V1 |
| 2026-11-07_Compiler2 | Dienst en vzw gescheiden | Oprichter krijgt nooit geld of voordeel; geen kosten, post of klanten op het adres van de productie. | geldt | | ja | V2 |
| 2026-11-07_Compiler3 | Zetel bij de medebestuurder | Zetel, administratie, post en back-up daar. | vervangen | 2026-11-07_Boekhouder6 | ja | V3 |
| 2026-11-07_Compiler4 | Verdeling 50/50 | Auteursrechten (bruto) 50 %, vzw 50 %; papier en inkt zijn een uitgave per aankoop. | geldt | | ja | V4 |
| 2026-11-07_Compiler5 | Printer is van de oprichter | Geen bruikleen; vzw koopt papier en inkt. | geldt | | ja | V5 |
| 2026-11-07_Compiler6 | Public Ledger toont "gratis dienst" | Zonder naam en bedrag; geen wettelijke boekhouding. | geldt | | ja | V6 |
| 2026-11-07_Compiler7 | Lening van de oprichter | Per uitgave, renteloos, geen termijn. | geldt | 2026-11-07_Boekhouder8 | ja | V7 |
| 2026-11-07_Compiler8 | Eigen pand vanaf 2029 | Uitwerken in 2028. | geldt | | ja | V8 |
| 2026-11-07_Compiler9 | Consumentenprijs onderzoeken | Marktgemiddelde min 30 tot 40 %. | voorlopig | | ja | V9 |
| 2026-11-08_Jurist1 | Verdeling 50/50 geldt nu al | Prijs blijft 7 × M tot marketing het onderzoek bevestigt. | geldt | | ja | |
| 2026-11-08_Jurist2 | Lening is een echte lening | Gestort per uitgave, met register. | geldt | | ja | |
| 2026-11-08_Jurist3 | Aansprakelijkheid | De vzw is aansprakelijk, behalve bij opzet of grove fout van de oprichter. | geldt | | ja | |
| 2026-11-08_Jurist4 | Open punten naar Cultuurloket | Zij zeggen welke expert antwoordt. | vervangen | | ja | |
| 2026-11-08_Techniek1 | Locatie aankopen vanaf 2029 | Aanvulling op Eigen pand vanaf 2029 (2026-11-07_Compiler8). De opbouw van liquide middelen dient om, ten vroegste in 2029, een locatie aan te kopen voor expo's, tentoonstellingen en workshops die passen bij de sociaal-culturele doelen. Enkel met eigen middelen, nooit met krediet. Op de sites uitleggen bij Over en Prijsopbouw; details (kopen of ook huren, hoe het 7M-verhaal erbij past) zijn nog open bij de oprichter. | vervangen |  | nee |  |
| 2026-11-08_Techniek2 | Pand aankopen vanaf 2029, krediet alleen op de particulier | Voor de werking van postershop en printshop blijft gelden: geen krediet, alleen renteloze leningen van de oprichter. Voor een pand (ten vroegste 2029) zet de oprichter geleend geld in, met hulp van naasten en waarschijnlijk een banklening (zo weinig mogelijk). Dat krediet staat op naam van de oprichter als particulier, nooit op de vzw. Bank en subsidies worden zoveel mogelijk vermeden; de bank wordt niet bij naam genoemd. Uitleg op Over en Prijsopbouw in het kader over geldreserves. Open bij Cultuurloket (C14). | geldt | 2026-11-08_Techniek1 | ja |  |
| 2026-11-08_Techniek3 | Gedeelde leverronde voor beide shops | In Gent en deelgemeenten kan de klant van postershop én printshop kiezen voor een eigen moment (€ 3,50 postershop, € 3 printshop, kalender) of de gedeelde leverronde: € 1,00 per deelnemer, bij het afrekenen betaald. Een ronde vertrekt bij 10 deelnemers of na 14 dagen met wie er dan is. Eén bestelling is één deelnemer, ook als ze uit beide shops komt. De klant weet dat de levering laat kan komen; wie niet kan wachten, kiest zo snel mogelijk. Buiten Gent en deelgemeenten: bpost, geen leverronde. Wie rijdt en wat er met de € 10 gebeurt, staat op de sites als: in afwachting van bevestiging Cultuurloket (C15). Tot de vzw bestaat is alles voorbeeld, met één gedeeld gegevensbestand dat beide sites lezen. | geldt |  | ja |  |
| 2026-11-08_Techniek4 | Geen bestelminimum | Er is nergens een bestelminimum, in geen enkele shop of leverwijze. | geldt |  | ja |  |
| 2026-11-08_Techniek5 | Printshop als preview in de stijl van de postershop | Gewone HTML-pagina's in de stijl van de postershop, met voorbeeldmand, betaling vooraf als QR-overschrijving (voorbeeld) en Snipcart-klare velden. Foto uploaden na betaling met het bestelnummer. Prijs 3 × materiaalkost, afgerond op € 0,50, alles naar de vzw. Betaal aan de deur, cash en Payconiq vervallen. Boven de bestelknop en op de bon: Geen herroepingsrecht (maatwerk), met uitleg in een tooltip; vraag bij Cultuurloket (C13). Claims: persoonlijk geleverd zonder te zeggen door wie, geen merknamen, geen vergelijkingen, wel meetbare feiten. | geldt |  | ja |  |
| 2026-11-08_Postershop1 | Tagline met curatielijnen en particulierkunstenaars | De tagline van de postershop wordt "curatielijn(en) uit de archieven van onafhankelijke particulierkunstenaars - tijdelijke naam", met een aparte link op "curatielijn(en)" en op "onafhankelijke particulierkunstenaars" (voorlopig leeg). Vervangt "uit de archieven van onafhankelijke kunstenaars". | geldt |  | ja |  |
| 2026-11-08_Postershop2 | Archiefstukken achter de taglinelinks | Achter de twee links van de tagline komen de archiefstukken die tonen hoe de definities van "curatielijn" en "onafhankelijke particulierkunstenaar" tot stand kwamen. Uit te voeren zodra Jonas de stukken levert. | open |  | ja |  |
| 2026-11-09_Compiler10 | Zetel bij de boekhouder (betaalde domiciliëring) | Maatschappelijke zetel op het adres van de boekhouder, als betaalde dienst (richtprijs € 25 tot € 75 per maand excl. btw). De medebestuurder levert geen adres en krijgt geen officiële post. Offerte met aparte lijn domiciliëring, minstens twee offertes, afspraken in een opdrachtbrief. | geldt | 2026-11-07_Compiler3 | nee | |
| 2026-11-09_Compiler11 | Tweede bestuurder is artistiek curator | Volwaardig bestuurder en medeoprichter. Doet selectie, curatie, beschrijvingen, kwaliteit, ethiek en artistiek netwerk; tekent mee (jaarrekening, begroting, UBO). De oprichter doet dagelijks bestuur, productie, webshop, licentiebeheer, roerende voorheffing en boekhouding. Webshop kan naar de medebestuurder als die dat aantoonbaar kan en wil. Taakverdeling in de statuten. | geldt | | nee | |
| 2026-11-09_Compiler12 | Harde limieten bij selectie | 18 of ouder, auteur van het werk, werk minstens 12 maanden oud, licentieovereenkomst verplicht, leverbaar als reproduceerbaar digitaal bestand, nooit met commerciële intentie gemaakt. Niet onderhandelbaar. | geldt | | nee | |
| 2026-11-09_Compiler13 | Curatiekader en co-description | Zes criteria: technische reproduceerbaarheid, formele integriteit, conceptuele dichtheid, poëtische resonantie, contextuele kracht, ethische geschiktheid. Curator en kunstenaar schrijven elk een notitie; beide naast elkaar gepubliceerd met wederzijdse toestemming. | geldt | | nee | |
| 2026-11-09_Compiler14 | Watermerk of Glaze alleen op webshopbeeld | Enkel met aparte, geparafeerde en intrekbare toestemming van de kunstenaar; niet op de poster; geen bijsnijden, kleuraanpassing of vervorming. | geldt | | nee | |
| 2026-11-09_Compiler15 | Kunst gratis, infrastructuur betaald | Kunstwerken gratis te bekijken, geen paywall, geen pay-to-participate, geen sponsorinvloed op selectie. Te verzoenen met de verkoop van Posters (Verdeling 50/50, 2026-11-07_Compiler4): voorlopig tot de licentie dit regelt. | voorlopig | | nee | |
| 2026-11-09_Compiler16 | Bestuurdersverzekering vóór eerste licentie | Bestuurdersaansprakelijkheidsverzekering met nazorgdekking; de oprichter beheert de polis, de medebestuurder krijgt de gegevens. | geldt | | nee | |
| 2026-11-09_Compiler17 | Belangenconflict oprichter | Bij lening en materiaalgebruik meldt de oprichter het conflict, stemt niet mee en beslist de medebestuurder op basis van de stukken; alles in de notulen. | geldt | | nee | |
| 2026-11-09_Compiler18 | Afspraken tussen de bestuurders | Leesrecht medebestuurder op bank, boekhouding, kwartaaloverzichten, Public Ledger en wachtwoordkluis; elk kwartaal een gesprek; afwijkende meningen in de notulen; jaarlijks gezamenlijk verslag zonder persoonsgegevens; exitafspraken nu vastleggen. | geldt | | nee | |
| 2026-11-09_Compiler19 | Open vragen naar jurist en boekhouder | De herschreven vragenlijst voor de tweede bestuurder vervangt de oude vragenlijst voor Cultuurloket. Open zakelijke vragen (F1 tot F13) gaan rechtstreeks naar jurist of boekhouder; open vragen tussen de bestuurders (G6 tot G8) beslissen beide bestuurders. | geldt | 2026-11-08_Jurist4 | nee | |
