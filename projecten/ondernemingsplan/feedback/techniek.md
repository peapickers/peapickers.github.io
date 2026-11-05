---
title: Feedback techniek op ondernemingsplan v2
---
> **Correctie 2026-11-05 · Technieker.** Voor de postershop gelden de prijzen, maten en woorden uit [BESLISSINGEN.md](https://github.com/peapickers/postershoppeapickers/blob/main/BESLISSINGEN.md); die gaan voor op deze tekst. M = papier + inkt, zonder btw-opslag. Prijs = 7 × M, afgerond op € 0,10, zonder btw op de verkoop (vzw peapickers is btw-vrijgesteld). Verdeling 1 · 3 · 3: Materiaalkost 1M, Auteursrechten 3M bruto (min 15 % roerende voorheffing), vzw peapickers 3M bruto. Maten Klein 20 × 30, Medium 30 × 45 en Groot 40 × 60 cm, geen A-formaten meer. "Fine-art" heet nu Limited. Voor deze feedback: T02 (afronding incl. btw) vervalt, want er is geen btw op de verkoop; de prijs is gewoon 7 × M afgerond op € 0,10. De posterconfigurator in PR #6 werkt nu met Klein, Medium en Groot in plaats van A4 tot 40 × 60 cm. De tekst hieronder blijft ongewijzigd staan als archief.

# Feedback techniek op ondernemingsplan v2
Datum: 2026-11-04

Gelezen als technieker die de webshop en de sites bouwt. Als bewijs van haalbaarheid verwijs ik naar twee openstaande pull requests op `postershoppeapickers`: **PR #6** (posterconfigurator, prijs 7 × M live, fine-art met vaste prijs, Snipcart klaar) en **PR #7** (verzending: afhalen, fietslevering, gebundelde fietsronde, bpost). Alle bedragen voor externe diensten zijn ordegroottes en moeten nagekeken worden op de tarievenpagina's van die diensten.

## Wat mist er

1. **De betaalweg.** § 2.2 punt 4 zegt "geen betaalprovider", maar er staat nergens hoe een klant dan wel betaalt en hoe een bestelling binnenkomt. De gekozen technische weg (Snipcart als mand, Mollie voor Bancontact, PR #6) is een betaalprovider. Het plan moet één van beide kiezen en die keuze uitschrijven (zie "Logisch / onlogisch").
2. **Waar klantgegevens wel staan.** Een levering vraagt naam en adres, een terugstorting na de fietsronde (PR #7) vraagt een rekeningnummer. "Geen klantgegevens op de site" (§ 2.2, § 8.3) klopt technisch voor de statische site zelf, maar de gegevens staan dan bij Snipcart en Mollie, of in de mailbox van de vzw. Er ontbreken: waar ze staan, wie erbij kan, hoe lang ze bewaard worden, een privacyverklaring op de site en een verwerkersovereenkomst met elke dienst.
3. **Hosting en domeinnaam.** Het plan noemt de site nergens als infrastructuur. GitHub Pages is gratis, maar de gebruiksvoorwaarden van GitHub Pages sluiten sites uit die vooral dienen om commerciële transacties mogelijk te maken (docs.github.com, "GitHub Pages limits"). Voor een webshop is dat een risico. Een eigen domeinnaam ontbreekt ook, terwijl § 6 QR-codes op flyers en stickers drukt: die QR-codes moeten naar een eigen domein wijzen, zodat de site later van host kan wisselen zonder dat gedrukt materiaal dode links bevat.
4. **Lopende kosten van de webshop** ontbreken in § 9.4 en bijlage A (zie de tabel bij "Te veel / te weinig").
5. **Hoe de Public Ledger gevuld wordt.** § 2.2 en § 7 zeggen dat elke verkoop erin staat, maar niet wie dat doet, hoe vaak en uit welke bron. Voorstel: zie "Top 3".
6. **Wat er gebeurt als de mand of de betaling uitvalt** (storing bij Snipcart of Mollie, een wijziging van hun voorwaarden of prijzen). Er is geen plan B.
7. **Toegang en sleutels.** Wie heeft de wachtwoorden van GitHub, Snipcart, Mollie, domein en bank? § 10 zegt "bij uitval van de oprichter wordt de webshop stilgezet", maar niemand anders kan dat technisch doen als enkel de oprichter de sleutels heeft. Een verzegelde noodenvelop of een gedeelde kluis (bv. Proton Pass) bij de medebestuurder ontbreekt.
8. **Toegankelijkheid en mobiel.** De configurator met schuivers moet op een telefoon werken, want de QR-codes uit § 6 openen op een telefoon. Dat is nergens een vereiste of een test.
9. **Een testfase.** § 11 zegt "webshop af" in januari tot maart 2027, maar niet wanneer en met wie er proefbestellingen gebeuren. Mollie live gebruiken kan pas met een ondernemingsnummer en een bankrekening van de vzw (januari 2027), dus echte betalingen testen kan pas na de oprichting.

## Logisch / onlogisch

**Posterconfigurator (§ 4.1): haalbaar, en grotendeels al gebouwd.** PR #6 doet wat § 4.1 beschrijft: velgrootte per centimeter van A4 tot 40 × 60 cm, verhouding van 4:6 tot 1:1, staand of liggend, passe-partout per centimeter, aantal, instellingen kopiëren naar de volgende poster, en live de berekening van M (velkost + inktkost) en de prijs met de verdeling 1 / 3 / 3 en de btw. De tarieven staan in één CSV (`_data/config-prijzen.csv`), dus een nieuwe papierprijs is één regel aanpassen. Januari tot maart 2027 volstaat voor wat overblijft: echte beelden, testen op telefoons en de koppeling met de echte betaalaccount. De configurator is dus geen risico voor de planning; de oprichting en de betaalaccount zijn dat wel.

**Prijsafronding (§ 4, § 9.1) botst met de techniek.** Het plan rondt de prijs incl. btw af op € 0,10 (Semimatte A3: € 15,70) en rekent terug naar € 12,98 excl. btw. Maar € 12,98 × 1,21 = € 15,71, niet € 15,70. En een mand zoals Snipcart rekent de btw bovenop de prijs excl. btw: met 7 × M = € 12,95 wordt dat € 15,67. Om overal hetzelfde bedrag te tonen moet het plan kiezen: (a) prijzen ingeven incl. btw (Snipcart kan btw "inbegrepen" rekenen) en het afrondingsverschil bij het deel van de vzw laten vallen, of (b) niet afronden en € 15,67 tonen. Optie (b) past beter bij "ontleed tot op de cent".

**"Geen betaalprovider" (§ 2.2) tegenover de gekozen weg.** Zonder betaalprovider blijft enkel overschrijving: de klant bestelt per mail of formulier, krijgt een EPC-QR-code met gestructureerde mededeling en de bestelling wordt pas gedrukt na ontvangst op de rekening. Dat is goedkoop en privé, maar handwerk (ordegrootte 5 minuten per bestelling om af te stemmen) en trager voor de klant. Met Snipcart en Mollie betaalt de klant meteen met Bancontact, maar dan is er wél een betaalprovider en staan klantgegevens bij twee externe diensten. Beide zijn technisch mogelijk; de voorbeeldmand met EPC-QR bestaat al op de site en Snipcart staat klaar in PR #6. De zin in § 2.2 moet wel overeenkomen met wat er gebouwd wordt, anders belooft het plan iets wat de site niet doet.

**"Geen tracking" is haalbaar,** maar Snipcart en Mollie laden scripts van een externe server en kunnen cookies zetten bij het afrekenen. Dat is functioneel, geen marketingtracking, maar het hoort in de privacyverklaring. Het effect meten van flyers (§ 6, § 13) kan zonder tracking met een aparte QR-link per plek (bv. `?bron=flyer-zaak1`) en tellen hoeveel bestellingen die bron meegeven, of met privacyvriendelijke telling zonder cookies. Nu staat er "we meten of het verkeer stijgt" zonder hoe; dat botst met "geen tracking" als niemand het uitlegt.

**Wachtronde voor gezamenlijke levering (§ 5.1) en PR #7 verschillen.** Het plan zegt: leverkost € 3,50 vast, bestelminimum € 20, en een gratis gedeelde ronde die vertrekt bij 5 aanmeldingen of na hoogstens 14 dagen. PR #7 bouwt iets anders: fietskost per km (voorbeeld € 1 + € 0,25 per km excl. btw), de klant betaalt de volle fietskost en krijgt na de ronde het verschil terug. Een van de twee moet aangepast worden. Technisch is de versie uit het plan eenvoudiger: geen terugstortingen, dus geen rekeningnummers van klanten nodig.

**"De site toont hoeveel mensen wachten en wanneer de ronde sluit" (§ 5.1)** is op een statische site niet vanzelf live. Mogelijkheden, van eenvoudig naar complex:

| Aanpak | Hoe | Nadeel |
|---|---|---|
| Handmatig | Na elke bestelling past de oprichter één getal en een datum aan in een databestand; de site bouwt in 1 à 2 minuten opnieuw | Vergeten kan; werkt enkel als de oprichter het doet |
| Halfautomatisch | Een geplande GitHub Action vraagt elk uur het aantal open rondebestellingen op bij Snipcart en schrijft alleen dat getal weg | API-sleutel als geheim in GitHub; niet tot op de minuut juist |
| Live | Een kleine serverfunctie geeft het getal terug bij elk bezoek | Breekt met de statische site; extra dienst en kosten |

Halfautomatisch is genoeg. Er wordt enkel een aantal gepubliceerd, nooit een naam of adres.

**Bestelminimum € 20 (§ 5.1).** Snipcart heeft voor zover ik weet geen ingebouwd bestelminimum; dat moet met een eigen controle in de mand gebeuren (na te kijken). Bij overschrijving is het gewoon een regel bij het bevestigen.

**Statische site (CollectionBuilder/Jekyll): de juiste keuze.** Geen server en geen database om te hacken, geen klantgegevens in de eigen code, gratis of bijna gratis hosting, en elke wijziging staat in de Git-geschiedenis, wat goed past bij "absolute transparantie". De beperkingen zijn: niets is live (wachtronde, voorraad), en alles wat dynamisch is (mand, betaling) komt van externe diensten. Fine-art in kleine oplage kan Snipcart wel bijhouden als voorraad per werk (PR #6 zet al een maximum per bestelling gelijk aan de oplage).

**Beveiliging van beelden (§ 2.2 punt 6) is maar half technisch afdwingbaar.** Klein beeld, zichtbaar watermerk in het bestand zelf (niet als laag erboven in de browser) en metadata verwijderd: dat werkt, en er is al een hulpscript voor het watermerk op de placeholders. Bescherming tegen AI-training is zwakker: een `robots.txt` die bekende AI-crawlers weigert en "noai"-metatags zijn verzoeken, geen slot. GitHub Pages laat geen eigen serverregels toe, dus crawlers blokkeren op serverniveau kan pas met een eigen domein achter een dienst die dat aanbiedt. Rechtsklik uitzetten heeft geen zin: wat de browser toont, kan gedownload worden. Het plan beloft beter "zo klein en zo gemarkeerd mogelijk" dan "bescherming".

**Public Ledger in Git.** Alles wat ooit in de repository stond, blijft in de geschiedenis staan. Een per vergissing gepubliceerd rekeningnummer of adres wissen vraagt het herschrijven van die geschiedenis en is daarna nog niet zeker weg (kopieën, caches). Daarom moet er altijd een menselijke controle zijn vóór een regel publiek wordt.

## Te veel / te weinig / te sterk benadrukt

**Te weinig: lopende kosten van de webshop.** § 9.4 en § 12 noemen geen enkele technische kost. Ordegroottes, na te kijken:

| Post | Ordegrootte per jaar | Opmerking |
|---|---|---|
| Domeinnaam (.be) | € 10 tot 15 | Nodig voor QR-codes en voor wisselen van host |
| Snipcart | 2 % van de omzet, met een minimum per maand bij lage omzet | Tarief in USD; bij 500 posters per jaar ligt de omzet waarschijnlijk onder de grens, dan geldt het minimum (ordegrootte € 200 tot 250 per jaar) |
| Mollie, Bancontact | vast bedrag per transactie, ordegrootte € 0,25 tot 0,40 | Bij ca. 330 bestellingen (gemiddeld 1,5 poster) ordegrootte € 100 |
| Hosting | € 0 (GitHub Pages) tot € 0 à 60 (andere host) | Zie het risico van GitHub Pages hierboven |
| Mail op eigen domein, wachtwoordkluis | € 0 tot 50 | Afhankelijk van het pakket |
| Onderhoud printer (onderhoudsbox, printkop, reiniging) | € 30 tot 100 | Elke reiniging kost ook inkt; niet in M |

Samen ordegrootte **€ 300 tot 500 per jaar**, dus 10 tot 20 % bovenop de € 2.500 vaste kosten [A1], of ongeveer 60 tot 100 extra posters om break-even te halen (§ 9.2). Per poster van € 15,70 kosten Snipcart en Mollie samen ongeveer € 0,60; het plan moet zeggen dat dit uit het deel van de vzw komt, anders klopt de "ontleding tot op de cent" niet meer.

**Te weinig: technische risico's in § 12.** Voorstel voor extra rijen:

| Risico | Kans | Gevolg | Wat dan |
|---|---|---|---|
| Host weigert de webshop (voorwaarden GitHub Pages) | Laag tot middel | Site offline | Eigen domein; host met toegelaten commercieel gebruik klaarhouden |
| Mand- of betaaldienst valt uit of verhoogt prijzen | Laag | Geen verkoop of hogere kosten | Overschrijving met EPC-QR als plan B, zit al in de site |
| Prijs op de site verschilt van prijs in de mand | Middel | Klant ziet ander bedrag, vertrouwen weg | Eén bron (`config-prijzen.csv`); testbestelling bij elke prijswijziging |
| Persoonsgegevens per vergissing in de Public Ledger | Laag | Datalek, blijft in Git-geschiedenis | Elke regel nagekeken vóór publicatie; geen vrije tekstvelden van klanten |
| Gehackt account (GitHub, Snipcart, Mollie, mail) | Laag | Valse prijzen, omgeleide betalingen | Tweestapsverificatie overal; sleutels in een kluis |
| Beelden geschraapt of gekopieerd | Middel | Werk circuleert zonder toestemming | Klein, watermerk in het bestand; auteur vooraf inlichten dat dit niet te voorkomen is |
| Printer defect | Laag tot middel | Geen productie | Reserve voor herstelling; tijdelijk stilzetten zoals bij uitval |

**Te sterk benadrukt:** "Geen betaalprovider" en "bescherming tegen AI-training" in § 2.2 staan als niet-onderhandelbaar, terwijl het eerste niet overeenkomt met de gekozen bouw en het tweede technisch niet waar te maken is. Beter: wat de vzw wel garandeert (geen marketingtracking, geen eigen klantendatabase, kleine beelden met watermerk) en wat ze niet kan garanderen.

**Te veel:** niets technisch. De tabellen in § 4.1 zijn precies wat de configurator nodig heeft.

## Wat kan gevisualiseerd of vertaald worden

1. **De configurator zelf als figuur in § 4.1.** Een schermafbeelding of schets van één poster: vel, passe-partout, afbeelding, met de drie getallen (velkost, inktkost, M) ernaast. Dat legt "velgrootte en afbeeldingsgrootte" beter uit dan tekst. Kan met een placeholder, zonder werk van een auteur.
2. **De weg van een bestelling als stroomschema in § 5.1:** mand, betaling, bevestiging, drukken, inpakken, wachtronde of bpost, levering, regel in de Public Ledger. Met per stap waar gegevens staan (browser, Snipcart, Mollie, mailbox, bank) en hoe lang. Dat beantwoordt meteen de privacyvraag.
3. **Een tijdlijn van de wachtronde:** dag 0 eerste aanmelding, teller 1 tot 5, vertrek bij 5 of op dag 14.
4. **Waar de klantgegevens staan:** een klein schema "op de site: niets · in de mand: tijdelijk · bij de betaaldienst: betaling · bij de vzw: adres tot levering + X".
5. **De Public Ledger als voorbeeld:** drie fictieve regels (verkoop, uitbetaling, kost) zoals ze op de site verschijnen, zodat lezers zien wat "elke euro staat erin" betekent.
6. **Vertaling naar de site:** § 4.1 en § 5.1 kunnen bijna letterlijk de uitlegpagina's "Hoe werkt de prijs" en "Verzending" worden; PR #6 en PR #7 hebben die pagina's al half. De KPI's uit § 13 kunnen automatisch uit de Public Ledger berekend en op de site getoond worden.

## Top 3 voorstellen

1. **Kies in § 2.2 en § 5.1 tussen Snipcart + Mollie en overschrijving met EPC-QR, en schrijf de gevolgen uit:** wie welke klantgegevens heeft en hoe lang, de transactiekosten per poster (uit het deel van de vzw), en de prijsafronding (prijs incl. btw ingeven of niet afronden). Stem daarna PR #7 af op de leverregels van het plan (vaste € 3,50 en gratis ronde, of fietskost per km met terugstorting).
2. **Neem een eigen domeinnaam en de webshopkosten op in § 9.4 en de technische risico's in § 12**, met de host als apart punt: bekijk vóór de lancering of GitHub Pages voor de webshop mag, en houd een alternatief klaar. De QR-codes uit § 6 wijzen enkel naar het eigen domein.
3. **Vul de Public Ledger halfautomatisch:** een klein script zet de bestelexport van Snipcart (of het bankafschrift) om naar regels in `register.csv` met alleen datum, werkcode, formaat, aantal en bedragen, zonder naam, adres of rekeningnummer. Het script maakt een pull request; de oprichter of de boekhouder keurt elke batch goed vóór publicatie (per maand, en zeker vóór elke kwartaaluitbetaling). Hetzelfde mechanisme kan het aantal wachtenden voor de fietsronde bijwerken.

## Actiepunten voor de compiler

Elk punt hierboven als één taak, klaar om over te nemen in de todo-lijst. Prioriteit: **H** = vóór de webshop live gaat (maart 2027), **M** = vóór de eerste kwartaaluitbetaling (juli 2027), **L** = later. "Rol" is wie het punt beslist of uitvoert, geen persoon.

| ID | § | Actie | Prio | Rol | Hangt af van |
|---|---|---|---|---|---|
| T01 | § 2.2, § 5.1 | Kiezen: Snipcart + Mollie of overschrijving met EPC-QR; § 2.2 punt 4 ("geen betaalprovider") daarop afstemmen | H | oprichter | — |
| T02 | § 4, § 9.1 | Afronding kiezen: prijs incl. btw ingeven en afronding uit het vzw-deel, of niet afronden (€ 15,67 i.p.v. € 15,70); alle voorbeeldprijzen in het plan herrekenen | H | oprichter | T01 |
| T03 | § 2.2, § 8.3 | Uitschrijven waar klantgegevens staan, wie erbij kan en hoe lang; privacyverklaring op de site; verwerkersovereenkomst per externe dienst | H | oprichter, jurist | T01 |
| T04 | § 5.1 | Leverregels gelijktrekken met de site: vaste € 3,50 en gratis ronde (plan) of fietskost per km met terugstorting (postershop PR #7) | H | oprichter, technieker | — |
| T05 | § 5.1 | Wachtronde-teller halfautomatisch bouwen (alleen een aantal en een sluitdatum, nooit gegevens) | M | technieker | T01, T04 |
| T06 | § 5.1 | Bestelminimum € 20 technisch afdwingen of laten vallen | H | technieker | T01 |
| T07 | § 9.4, § 6 | Eigen domeinnaam opnemen (€ 10 tot 15 per jaar); QR-codes enkel naar het eigen domein | H | oprichter | — |
| T08 | § 12 | Nagaan of GitHub Pages een webshop toelaat; alternatieve host klaarhouden | H | technieker | T07 |
| T09 | § 9.4, bijlage A | Lopende webshopkosten opnemen (Snipcart, Mollie, domein, mail, printeronderhoud; ordegrootte € 300 tot 500 per jaar) als nieuwe aanname; tarieven nakijken | H | oprichter, boekhouder | T01 |
| T10 | § 9.2 | Transactiekosten per poster (ca. € 0,60) uit het vzw-deel halen en break-even herrekenen | H | boekhouder | T09 |
| T11 | § 12 | Technische risico's toevoegen (host, uitval betaaldienst, prijsverschil site/mand, persoonsgegevens in de Ledger, gehackt account, geschraapte beelden, printer defect) | H | oprichter | — |
| T12 | § 10, § 12 | Sleutelbeheer: wachtwoorden in een gedeelde kluis of noodenvelop bij de medebestuurder; tweestapsverificatie overal | H | oprichter, medebestuurder | — |
| T13 | § 11 | Testfase plannen: proefbestellingen in testmodus vóór de oprichting, echte betaling na ondernemingsnummer en bankrekening | H | technieker | T01 |
| T14 | § 4.1 | Configurator testen op telefoons en op toegankelijkheid | H | technieker | — |
| T15 | § 2.2 punt 6 | Belofte over beelden herformuleren: klein, watermerk in het bestand, metadata weg; AI-bescherming enkel als verzoek (robots.txt, noai) | M | oprichter | — |
| T16 | § 6, § 13 | Flyereffect meten zonder tracking: aparte QR-link per plek, bestellingen per bron tellen | M | technieker | T07 |
| T17 | § 2.2, § 7 | Public Ledger halfautomatisch vullen: script zet bestelexport of bankafschrift om naar regels zonder persoonsgegevens, als pull request ter goedkeuring | M | technieker, boekhouder | T01 |
| T18 | § 5.1 | Stroomschema van een bestelling toevoegen, met per stap waar gegevens staan | M | oprichter | T03 |
| T19 | § 4.1 | Figuur van de configurator (vel, passe-partout, afbeelding, M) met een placeholder | L | technieker | — |
| T20 | § 5.1 | Tijdlijn van de wachtronde (1 tot 5 aanmeldingen of dag 14) als figuur | L | oprichter | T04 |
| T21 | § 13 | KPI's automatisch uit de Public Ledger berekenen en op de site tonen | L | technieker | T17 |
