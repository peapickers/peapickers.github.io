---
title: Techniek
---
# Project Techniek

Claude-project: Techniek · Repo: [peapickers/peapickers.github.io](https://github.com/peapickers/peapickers.github.io) · Regels: [werkwijze](werkwijze.html)

> Nieuwste item bovenaan in elke sectie. Niets verwijderen: voeg een nieuw item toe.

## Opdracht

### 2026-11-03 · Technieker · Eerste versie

- Code, hosting en automatische taken van alle peapickers-sites.
- Repos: [peapickers.github.io](https://github.com/peapickers/peapickers.github.io), [peapickersarchief](https://github.com/peapickers/peapickersarchief), [postershoppeapickers](https://github.com/peapickers/postershoppeapickers), [printshoppeapickers](https://github.com/peapickers/printshoppeapickers), [peapickersfeed](https://github.com/peapickers/peapickersfeed) en [peapickers](https://github.com/peapickers/peapickers).
- Leest de secties Technieker op de merkpagina's: [Archief](archief.html#technieker), [Printshop](printshop.html#technieker), [Postershop](postershop.html#technieker) en [Feed](feed.html#technieker).

## Stand van zaken

### 2026-11-07 · Technieker · Beslissingen van 7 november voor de techniek

Aanvulling op: 2026-11-07 (Herroepingsknop, Boekhouder). Op de site is nog niets veranderd; de code komt later.

- Jonas koos voor elk voorstel in de [vragenlijst techniek](techniek/vragenlijst-2026-11-07.html) (VT1 tot VT14). De sectie Site van [BESLISSINGEN.md](https://github.com/peapickers/postershoppeapickers/blob/main/BESLISSINGEN.md) is bijgewerkt.
- **Herroepingsknop**: link "Hier de overeenkomst herroepen" in elke footer, pagina Herroepen met formulier in 2 stappen. Tot de webshop opent doet het formulier niets en toont het enkel de voorbeeldmail. Echt versturen: Cloudflare Workers ontvangt en Brevo mailt (€ 0 per maand, EU-servers), met een eigen domeinnaam als afzender; accounts op naam van de vzw na de oprichting (VT1, VT5, VT6). Zo hoeft er geen nieuwe betalende dienst bij en komen er geen persoonsgegevens op de site.
- **Bewaren**: kopie naar de mailbox van de vzw, maandelijkse export naar Administratie en de versleutelde schijven, 10 jaar (VT2). Uitvoering van ZB09 (T24).
- **Export voor de boekhouder**: CODA, CSV van Mollie en een eigen maandelijkse CSV; Auteursrechten per auteur via een lokaal script en een privébestand (VT3, VT4; T26, T27).
- **Public Ledger**: betaaldag de 15de van januari, april, juli en oktober, eerst 15 juli 2027; rubriek "lening oprichter" per maand; bruikleen als lijn zonder bedrag; Auteursrechten tellen in het kwartaal waarin de herroepingstermijn afloopt (VT9, VT10; T28).
- **Tweede kans**: groep in de filter op Producten met het label "teruggestuurd", prijs 80 %, 50/50 (VT11; T29). **Limited** verborgen tot de eerste Limited gepland is (VT12; T30).
- Actiepunten T22 tot T33 staan in de vragenlijst. De tussenstand van de code (voorbeeldmodus van de knop, Tweede kans, schakelaar Limited) bleef buiten de repo.


### 2026-11-07 · Boekhouder · Herroepingsknop

- Beslist: de webshop krijgt een herroepingsknop (verplicht sinds 19 juni 2026): goed zichtbaar, 2 stappen (formulier met naam, bestelnummer en e-mail; knop "Herroeping bevestigen") en meteen een ontvangstbevestiging per e-mail. Herroeping geldt voor Poster en Limited. Zie [BESLISSINGEN.md](https://github.com/peapickers/postershoppeapickers/blob/main/BESLISSINGEN.md).
- Verzoeken en bevestigingen moeten 10 jaar bewaard kunnen worden. Actiepunten ZB08 en ZB09 in de [beslissingen van 7 november 2026](boekhouder/beslissingen-2026-11-07.html).

### 2026-11-05 · Technieker · BESLISSINGEN.md gaat voor

- Voor de postershop geldt [BESLISSINGEN.md](https://github.com/peapickers/postershoppeapickers/blob/main/BESLISSINGEN.md) boven alles wat ouder is: maten Klein / Medium / Groot, M = papier + inkt zonder btw-opslag, prijs 7 × M zonder btw op de verkoop, verdeling 1 · 3 · 3, Limited in plaats van fine-art.
- Correctie bovenaan gezet in het dossier en de stukken voor de boekhouder, stappenplan v4, plan v3 en v2, de stappenplannen en de feedback van jurist en techniek. Niets verwijderd. Zie ook [Postershop](postershop.html), 2026-11-05.
- Printshop en de oude site `peapickers` hebben eigen formaten en blijven ongewijzigd: BESLISSINGEN.md gaat alleen over de postershop.

### 2026-11-04 · Technieker · Open punten van 3 november afgehandeld

Vervangt: 2026-11-03 (Start)

- Kader, latten en ophangsysteem zijn geschrapt (zie [Postershop](postershop.html), Kern 2026-11-04).
- Bestandsnamen van originelen: één map per auteur, namen zoals `K003-02_titel.tif`. Vervangt de vorm `PP-2026-maker-01_titel.tif` uit [stappenplan v4](jurist/stappenplan-workflow-extended-v4.html), stap 1.3.
- Originelen worden nooit in een cloud bewaard. Proton Drive dient als doorgeefluik voor originelen en als extra back-up van wat online verschijnt.
- De technische nota over de bewaring is bijgewerkt naar versie 2 (twee externe schijven van 500 GB). Ze blijft in het Claude-project, omdat ze details over opslag bevat.

### 2026-11-03 · Technieker · Start

- Nog geen items. Het eerste nieuwe feit komt bovenaan in deze sectie.
