---
title: Werkwijze
---
# Werkwijze voor de projectpagina's

Elk merk van peapickers heeft hier één pagina: [Archief](archief.html), [Printshop](printshop.html), [Postershop](postershop.html) en [Feed](feed.html). Die pagina is de gedeelde bron voor elk Claude-project van dat merk.

## Regels (archiefvorming)

### 2026-11-03 · Technieker · Pagina's per project

- Naast de merkpagina's is er nu één pagina per Claude-project: [Boekhouder](boekhouder.html), [Marketing](marketing.html), [Techniek](techniek.html) en [Jurist](jurist.html).
- Een feit over één merk komt op de merkpagina, in de sectie van die rol. Een feit over het werk van het project zelf komt op de projectpagina.
- Marketing en Jurist hebben nog geen sectie op de merkpagina's. Hebben ze een feit over één merk, dan voegen ze onderaan die merkpagina een sectie `## Marketing` of `## Jurist` toe.
- Alle regels hieronder gelden ook voor de projectpagina's.

### 2026-11-02 · Technieker · Eerste versie

1. **Nooit verwijderen of overschrijven.** Ook een fout blijft staan. Je verbetert ze met een nieuw item.
2. **Elk nieuw feit is een nieuw item**, bovenaan in de juiste sectie, in de vorm `### JJJJ-MM-DD · Rol · korte titel`.
3. **Het nieuwste item geldt.** Spreekt een nieuw item een ouder tegen, dan schrijf je erbij: `Vervangt: JJJJ-MM-DD`.
4. **De juiste plaats:** over geld bij Boekhouder, over code en hosting bij Technieker, over wat het merk is en hoe ver het staat bij Kern. Gaat het over alle merken, dan komt het op deze pagina.
5. **Samenvatten en verwijzen.** Cijfers en instellingen blijven in hun eigen bestand. Het item zegt wat er veranderde en waar het staat.
6. **Niets privés.** Deze repo is publiek. Geen klantgegevens, geheimen, wachtwoorden of privébedragen.
7. **Eerst lezen, dan schrijven.** Lees de pagina opnieuw voor je iets toevoegt. Wat je het laatst gelezen hebt, is de stand van zaken.

Git bewaart daarnaast elke versie, met datum.

## Instructietekst voor elk Claude-project

### 2026-11-03 · Technieker · Projecten per rol

Voor de projecten Boekhouder, Marketing, Techniek en Jurist. Vervang `<project>` door `boekhouder`, `marketing`, `techniek` of `jurist`. Elk project moet de repo peapickers/peapickers.github.io gekoppeld hebben in de projectinstellingen.

```text
Gedeelde bron peapickers

De gedeelde informatie over dit project staat in de repo peapickers/peapickers.github.io, in projecten/<project>.md. De regels staan in projecten/werkwijze.md. De merkpagina's staan in projecten/archief.md, printshop.md, postershop.md en feed.md. Online: https://peapickers.github.io/projecten/<project>.html

Lees projecten/<project>.md en projecten/werkwijze.md aan het begin van elke taak, en de merkpagina's die over je taak gaan. Wat je het laatst gelezen hebt, is de stand van zaken.

Werk volgens archiefvorming:
- Verwijder of overschrijf nooit bestaande informatie, ook geen fouten.
- Voeg elk nieuw feit toe als nieuw item, bovenaan in de juiste sectie: ### JJJJ-MM-DD · Rol · korte titel
- Over één merk: op de merkpagina, in de sectie van je rol. Over het werk van dit project: op projecten/<project>.md. Over alle merken: werkwijze.md.
- Het nieuwste item geldt. Spreekt het een ouder item tegen, schrijf dan: Vervangt: JJJJ-MM-DD.
- Vat samen en verwijs. Cijfers en instellingen blijven in hun eigen bestand.
- Zet nooit klantgegevens, gegevens van makers, geheimen, wachtwoorden, offertes of privébedragen in de repo. Ze is publiek.
- Een push naar main staat meteen online. Commitbericht: "Projectpagina <project>: wat er veranderde".
```

### 2026-11-02 · Technieker · Eerste versie

Kopieer dit in de projectinstructies. Vervang `<merk>` door `archief`, `printshop`, `postershop` of `feed`.

```text
Gedeelde bron peapickers

De gedeelde informatie over dit merk staat in de repo peapickers/peapickers.github.io, in projecten/<merk>.md. De regels voor alle merken staan in projecten/werkwijze.md. Online: https://peapickers.github.io/projecten/<merk>.html

Lees projecten/<merk>.md en projecten/werkwijze.md aan het begin van elke taak. Wat je het laatst gelezen hebt, is de stand van zaken.

Werk volgens archiefvorming:
- Verwijder of overschrijf nooit bestaande informatie, ook geen fouten.
- Voeg elk nieuw feit toe als nieuw item, bovenaan in de juiste sectie: ### JJJJ-MM-DD · Rol · korte titel
- Juiste sectie: Kern (wat het merk is, stand van zaken), Boekhouder (geld, prijzen, Public Ledger), Technieker (code, hosting, automatische taken). Gaat het over alle merken: werkwijze.md.
- Het nieuwste item geldt. Spreekt het een ouder item tegen, schrijf dan: Vervangt: JJJJ-MM-DD.
- Vat samen en verwijs. Cijfers en instellingen blijven in hun eigen bestand.
- Zet nooit klantgegevens, geheimen, wachtwoorden of privébedragen in de repo. Ze is publiek.
- Een push naar main staat meteen online. Commitbericht: "Projectpagina <merk>: wat er veranderde".
```

## Gemeenschappelijk

### 2026-11-07 · Boekhouder · vzw: productieplek, zetel en bestuur

Vervangt: 2026-11-04 (vzw peapickers), de zinnen over de niet-uitvoerend bestuurder en over printer en voorraad op het privéadres.

- Productie en voorraad komen op een paar m² bij een bestaand bedrijf of organisatie, voor maximaal € 150 per maand alles inbegrepen. Niet op het privéadres van de oprichter.
- De zetel komt liefst op het adres van de productieplek, anders bij een familielid met schriftelijke toestemming.
- Een "niet-uitvoerende" bestuurder bestaat niet in een vzw. Er blijven minstens 2 leden en 2 bestuurders nodig.
- Details: [beslissingen van 7 november 2026](boekhouder/beslissingen-2026-11-07.html) en [BESLISSINGEN.md](https://github.com/peapickers/postershoppeapickers/blob/main/BESLISSINGEN.md). Open vragen over geld en materiaal: [vragenlijst boekhouder](boekhouder/vragenlijst-2026-11-07.html).

### 2026-11-04 · Kern · vzw peapickers

Vervangt: 2026-11-02 (Huisstijl en samenhang), alleen de zin over de vzw.

- vzw peapickers wordt opgericht rond januari 2027, zodra een medebestuurder gekozen is. "Ten vroegste na februari 2029" geldt niet meer.
- Oprichting met onderhandse akte, zonder notaris. Twee stichtende leden en twee bestuurders: de oprichter als dagelijks bestuurder, een niet-uitvoerend bestuurder die de zetel en de back-upschijf beheert.
- Printer en voorraad staan op het privéadres van de oprichter, niet op de zetel. Woonkosten worden nooit ingebracht.
- Aparte bankrekening op naam van de vzw, geen cashbetalingen, voor geen enkel merk.
- Uitgaven voor hardware en voor juridische of gespecialiseerde diensten vragen de goedkeuring van beide bestuurders.
- Bij uitval van de oprichter wordt de webshop tijdelijk stilgezet.
- Nog open in het plan: herroepingsrecht bij fine-art, bestemming van het vermogen bij ontbinding, verzekeringen, boekhouder. Zie [ondernemingsplan](ondernemingsplan.html).

### 2026-11-02 · Kern · Huisstijl en samenhang

- peapickers is de paraplunaam voor de projecten van Jonas in Gent. Geen vzw; een vzw kan ten vroegste na februari 2029.
- Huisstijl: Courier Prime, zwarte kaders van 1 px, papierkleur #F7F7F6 (archief: neutraal grijs #EBEBEB).
- Archief en postershop delen het metadatamodel en de CollectionBuilder-code. Een wijziging aan de basis kijk je in beide repos na.
- Alles gratis en privacyvriendelijk: geen server, geen betaalprovider, geen tracking.
