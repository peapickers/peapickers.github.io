---
title: Werkwijze
---
# Werkwijze voor de projectpagina's

Elk merk van peapickers heeft hier één pagina: [Archief](archief.html), [Printshop](printshop.html), [Postershop](postershop.html) en [Feed](feed.html). Die pagina is de gedeelde bron voor elk Claude-project van dat merk.

## Regels (archiefvorming)

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

### 2026-11-02 · Kern · Huisstijl en samenhang

- peapickers is de paraplunaam voor de projecten van Jonas in Gent. Geen vzw; een vzw kan ten vroegste na februari 2029.
- Huisstijl: Courier Prime, zwarte kaders van 1 px, papierkleur #F7F7F6 (archief: neutraal grijs #EBEBEB).
- Archief en postershop delen het metadatamodel en de CollectionBuilder-code. Een wijziging aan de basis kijk je in beide repos na.
- Alles gratis en privacyvriendelijk: geen server, geen betaalprovider, geen tracking.
