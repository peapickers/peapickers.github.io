---
title: Feedback jurist op ondernemingsplan v2
---
> **Correctie 2026-11-05 · Technieker.** Voor de postershop gelden de prijzen, maten en woorden uit [BESLISSINGEN.md](https://github.com/peapickers/postershoppeapickers/blob/main/BESLISSINGEN.md); die gaan voor op deze tekst. M = papier + inkt, zonder btw-opslag. Prijs = 7 × M, afgerond op € 0,10, zonder btw op de verkoop (vzw peapickers is btw-vrijgesteld). Verdeling 1 · 3 · 3: Materiaalkost 1M, Auteursrechten 3M bruto (min 15 % roerende voorheffing), vzw peapickers 3M bruto. Maten Klein 20 × 30, Medium 30 × 45 en Groot 40 × 60 cm, geen A-formaten meer. "Fine-art" heet nu Limited. De tekst hieronder blijft ongewijzigd staan als archief.

# Feedback jurist op ondernemingsplan v2
Datum: 2026-11-04

Gelezen als juridisch voorbereider: het plan en de zes repo's van peapickers, naast licentieovereenkomst concept 5 (2026-11-03). Dit is voorbereiding voor de jurist, geen bindend advies. Elke wetsverwijzing staat als **[te verifiëren]**: ze moet in de geldende versie nagekeken worden. Bij elk punt staat waar mogelijk wat de wet zegt (W), wat gebruikelijk is (G) en wat mijn inschatting is (I).

Kleurcode: **ROOD** = waarschijnlijk ongeldig of groot risico · **ORANJE** = onduidelijk, onevenwichtig of onderhandelbaar · **GROEN** = in orde.

## Wat mist er

1. **ROOD · De AI-bescherming werkt niet (§ 2.2 punt 6).** De robots.txt die AI-crawlers en zoekmachines weert, staat op `/peapickersarchief/robots.txt`. Crawlers lezen alleen `/robots.txt` op de hoofdmap van het domein (RFC 9309), en peapickers.github.io heeft er geen. Site, archief en licentie (art. 5.2) beloven iets wat nu niet gebeurt. W: het voorbehoud tegen tekst- en datamining moet bij online inhoud machineleesbaar zijn [te verifiëren: art. 4.3 richtlijn 2019/790 en de omzetting in Boek XI WER]. I: kleine technische fix, grote juridische waarde.
2. **ROOD · Klantteksten van de webshop (§ 5.1, § 8.3).** Postershop en printshop hebben nog geen algemene voorwaarden, geen informatie over het herroepingsrecht met modelformulier en geen privacyverklaring. Het vinkje in de mand verwijst naar teksten die "nog op te stellen" zijn. W: verplicht bij verkoop op afstand [te verifiëren: art. VI.45 en VI.47 e.v. WER]. I: blokkeert de eerste verkoop, niet de voorbereiding.
3. **ORANJE · Afspraken tussen de oprichter en de vzw (§ 5, § 8.2 stap 6, § 9.4).** De oprichter is stichter, dagelijks bestuurder, geldschieter, schenker van de printer, drukker op het eigen adres en bewaarder van de bestanden. Nodig: een schriftelijke renteloze lening (met kwijtschelding), een schenkingsakte of bruikleen voor printer en voorraad, een afspraak over het gebruik van de ruimte en de verzekering daarvan. Vraag aan de jurist: valt dit onder de regeling voor belangenconflicten van bestuurders [te verifiëren: WVV]?
4. **ORANJE · Statuten (§ 8.2 stap 2).** Er is nog geen ontwerp. Aandachtspunten: een doel waarin verkoop van posters en prints een middel is voor het onbaatzuchtige doel [te verifiëren: art. 1:2 WVV], de bestemming van het vermogen bij ontbinding (§ 8.3), de goedkeuringen door alle bestuurders (§ 8.1) en de regeling voor belangenconflicten.
5. **ORANJE · Herroeping bij posters op maat (§ 4.1, § 8.3).** De klant kiest velgrootte, afbeeldingsgrootte en verhouding per centimeter. Dat kan onder de uitzondering vallen voor goederen die volgens de specificaties van de consument gemaakt zijn [te verifiëren: art. VI.53, 3° WER; arrest Möbel Kraft, C-529/19]. § 8.3 en licentie art. 7.14 gaan nog uit van 14 dagen voor alles. Keuze nodig: de uitzondering inroepen en dat vóór de bestelling melden, of vrijwillig 14 dagen geven.
6. **ORANJE · Voorwaarden printshop.** Klanten mogen foto's van anderen laten drukken ("Kreeg je de foto van iemand anders"). Nodig: de klant garandeert de rechten op het beeld en de toestemming van wie erop staat, peapickers mag weigeren, en de klant vrijwaart peapickers.
7. **ORANJE · Reglement selectiecomité (§ 4.3, § 8.1).** Join peapickers zegt dat elk lid een redenering publiceert, ook over afgewezen werk. Nodig: kort reglement met samenstelling, geheimhouding, belangenconflict en wat er wel en niet gepubliceerd wordt.
8. **ORANJE · Publiek domein.** De oude site (peapickers.io) toont 16 werken uit het publiek domein, en "Hoe het werkt" heeft een prijsmodel van 4 delen voor zulk werk. Niet elk werk is zeker vrij: J.R. Sabiers (1936, sterfjaar onbekend), een Hubble-beeld van NASA en ESA (2017, ESA-beelden vragen volgens mij naamsvermelding onder een open licentie), en Dorothea Lange (1936, overleden 1965: in België waarschijnlijk vrij via de vergelijking van beschermingstermijnen voor werk uit de VS [te verifiëren: art. 7 richtlijn 2006/116]). Een check per werk is nodig vóór verkoop.

## Logisch / onlogisch

**Logisch (GROEN)**

- Niet-exclusieve licentie per werk, geen sublicentie, stoppen kan altijd binnen 7 dagen (§ 7). Dat is evenwichtig voor de auteur en beperkt het risico op herziening van het contract.
- Nooit tekenen tijdens het eerste gesprek en doorverwijzen naar Cultuurloket (§ 7 punt 2).
- Kwartaaloverzicht met inzagerecht voor de auteur (licentie art. 8.7): voldoet aan de transparantieplicht [te verifiëren: art. XI.167/1 e.v. WER].
- Niets verkopen zonder vzw (§ 12).
- De knop "Bestellen met betalingsverplichting" in de mand.

**Onlogisch of in tegenspraak**

- **ROOD · § 2.2 punt 1 en § 7 punt 5: "zonder persoonsgegevens" klopt niet.** De Public Ledger (`register.csv`) toont per werkcode het bedrag voor de auteur. Het middelste deel van de code is het nummer van de archiefvormer, en dat nummer hangt op de archiefvormerspagina aan een naam. Zo wordt het inkomen per auteur publiek. W: gepseudonimiseerde gegevens blijven persoonsgegevens als ze te herleiden zijn [te verifiëren: overweging 26 AVG]. I: kies tussen een aparte, intrekbare toestemming in de licentie of bedragen per kwartaal samenvoegen.
- **ORANJE · § 2.2 punt 6 tegenover licentie art. 7.8.** De licentie zegt dat het werk in geen enkele vorm bewerkt wordt, maar het webshopbeeld krijgt een watermerk schuin over het beeld en gaat door Glaze. Dat raakt het integriteitsrecht van de auteur [te verifiëren: art. XI.165 WER]. Nodig: een specifieke toestemming als uitzondering in de licentie en in de ontsluitingsovereenkomst van het archief.
- **ORANJE · § 2.2 punt 4 tegenover de printshop.** "Nooit cash" geldt voor elk merk, maar de printshop vraagt "cash of Payconiq/overschrijving" aan de deur (`js/config.js`).
- **ORANJE · § 4 tegenover de websites.** Op 4-11 is beslist: 7 × M met 1/3/3, posters op maat, geen kaders, levering € 3,50. Nog niet aangepast:
  - peapickers.github.io, "Hoe het werkt": 1 materiaal / 3 maker / 2 financiers / 1 peapickers;
  - postershop, Join peapickers (punt 5 en 6): poster € 6 of € 15 voor drie, € 1,25 materiaal, 50/50, vast formaat;
  - postershop, "Hoe laat is het?": "als poster te verkopen, in een kleine genummerde en gesigneerde oplage" (mengt poster en fine-art);
  - licentie concept 5: art. 2.4 (levering € 3), 7.10 (kaders), 7.13 (vast A3/A2-formaat), 8.2 (afronden naar beneden), 8.10 (€ 6 / € 15, 50/50).
- **ORANJE · § 2 kernzin: "zonder dat hun statuut moet veranderen".** Ook op "Hoe het werkt" en met het bedrag "tot € 77.220 bruto (VLAIO, 2026)" op de postershop. Of auteursinkomsten als roerend inkomen of als beroepsinkomen gelden, beslist de fiscus, niet peapickers. Voorstel: verwijzen naar Cultuurloket of een boekhouder, en het bedrag laten bevestigen door de boekhouder.
- **ORANJE · Privacyverklaring archief.** De verwerkingsverantwoordelijke is "de archivaris, als particulier", zonder naam of adres [te verifiëren: art. 13.1 a AVG]. De rechtsgrond per verwerking ontbreekt. De netwerkpagina toont lidmaatschap van clubs, collectieven en vzw's, wat soms gevoelige gegevens prijsgeeft [te verifiëren: art. 9 AVG].

## Te veel / te weinig / te sterk benadrukt

- **Te weinig:** het juridische luik in § 12 ("Licentie of herroeping juridisch fout", kans laag). Met de punten hierboven is de kans eerder middel. Voorstel: drie extra risico's, namelijk "Klantteksten ontbreken bij de start", "Persoonsgegevens in de Public Ledger" en "AI-scraping ondanks belofte".
- **Te sterk benadrukt:** "Zoekmachines en AI-crawlers worden geweerd" en "bescherming tegen AI-training" (§ 2.2 punt 6, over-pagina, archief). Pas laten staan als punt 1 van "Wat mist er" opgelost is, en dan formuleren als een poging, geen garantie.
- **Te weinig:** wie de verwerkingsverantwoordelijke is voor klantgegevens (mail, adres, bestelling) in § 5.1 en § 8.3.

## Wat kan gevisualiseerd of vertaald worden

- **Een schema van de documenten:** wie tekent wat met wie (auteur ↔ vzw: licentie; geportretteerde ↔ auteur: modelovereenkomst; klant ↔ vzw: voorwaarden; oprichter ↔ vzw: lening en schenking; bestuurders: statuten). Past bij § 8.
- **Een tabel "wat moet klaar zijn vóór de eerste verkoop"** in § 11: statuten, ondernemingsnummer, voorwaarden, herroeping, privacy, licentie concept 6 nagelezen.
- De footer van de postershop in gewone taal: "© de auteurs. Gereproduceerd onder licentie door vzw peapickers. Tekst- en datamining, ook voor AI, is niet toegestaan." in plaats van "© Alle reproducties zijn gelicentieerd."
- "Meedoen" zegt "Zo bewijs je dat het werk van jou is." Een contract met peapickers bewijst geen auteurschap tegenover derden; het auteursrecht ontstaat vanzelf bij het maken. Voorstel: "Zo leggen we samen vast wat je ons toestaat."

## Top 3 voorstellen

1. **robots.txt op de hoofdmap van peapickers.github.io en een TDM-voorbehoud in elke footer.** Kost een uur, herstelt een belofte uit § 2.2 en uit de licentie.
2. **Licentie concept 6 en de klantteksten van de postershop** (algemene voorwaarden, herroeping met modelformulier, privacyverklaring), vóór de jurist (§ 8.2 stap 2) nagelezen wordt, zodat die alles in één keer ziet. Met de beslissing over herroeping bij posters op maat en over de bedragen per auteur in de Public Ledger.
3. **Statuten en de afspraken tussen oprichter en vzw** (lening, schenking printer, ruimte, verzekering, belangenconflict) als concept 1, zodat § 8.2 stap 2 en 6 samen nagelezen kunnen worden.

## Open vragen voor de jurist

Nieuw ten opzichte van de vragen in licentie concept 5. Zekerheid van mijn inschatting tussen haakjes.

1. Volstaat "poster op bestelling, vel A4 tot 40 × 60 cm, verhouding 4:6 tot 1:1" als uitdrukkelijke exploitatiewijze? (middel: een bandbreedte volstaat waarschijnlijk)
2. Valt een poster op maat onder de uitzondering op het herroepingsrecht? (middel: waarschijnlijk wel bij keuze per centimeter)
3. Is toestemming een geldige rechtsgrond voor bedragen per auteur in de Public Ledger, gezien de afhankelijke positie van de auteur? (middel)
4. Volstaan robots.txt en een tekst in de footer als voorbehoud tegen tekst- en datamining, en kan de vzw dat doen namens de auteur? (middel)
5. Is een watermerk met Glaze een aantasting van het integriteitsrecht, en volstaat een specifieke toestemming? (middel)
6. Is de vzw als drukker aansprakelijk als een klant van de printshop een beschermd beeld laat drukken? (laag tot middel)
7. Is *Destitute pea pickers* van Dorothea Lange in België publiek domein? (middel: waarschijnlijk wel)
8. Zijn J.R. Sabiers, de anonieme foto's en de museumbeelden vrij voor commerciële verkoop? (laag)
9. Valt het Hubble-beeld onder een licentie met naamsvermelding, en mag het verkocht worden? (middel)
10. Valt een lening, schenking of bruikleen tussen oprichter en vzw onder de regeling voor belangenconflicten? (middel)
11. Is lidmaatschap van een groep op de netwerkpagina een bijzondere categorie van persoonsgegevens? (middel)
12. Volstaat "de archivaris, als particulier" als verwerkingsverantwoordelijke? (middel tot hoog: naam en adres zijn waarschijnlijk nodig)
13. Klopt € 77.220 voor 2026, en mag de vzw publiek zeggen dat auteurs hun statuut niet moeten aanpassen? (laag; vraag voor de boekhouder)

Ook nog open: de zeven vragen van licentie concept 5 en de vragen J1 tot J11 over de ondertekening.
