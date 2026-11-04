---
title: Postershop
---
# Peapickers Postershop

Site: <https://peapickers.github.io/postershoppeapickers/> · Repo: [peapickers/postershoppeapickers](https://github.com/peapickers/postershoppeapickers) · Regels: [werkwijze](werkwijze.html)

> Nieuwste item bovenaan in elke sectie. Niets verwijderen: voeg een nieuw item toe.

## Kern

### 2026-11-04 · Kern · Twee vormen, kanaal en planning

Vervangt: 2026-11-02 (Oplage)

- Bron: ondernemingsplan postershop 2027-2029, versie 1 (zie [ondernemingsplan](ondernemingsplan.html)).
- **Fine-art:** unieke reproductie, 1 tot 3 exemplaren per werk, genummerd, gesigneerd en met echtheidscertificaat. Ten hoogste 3 tot 5 werken per auteur tegelijk.
- **Poster:** A3 met vaste passe-partout, Epson Enhanced Matte, print on demand zonder oplagegrens. Breder assortiment per auteur toegelaten. Posterlicentie 1 jaar, telkens verlengbaar na schriftelijke bevestiging.
- Gebruik altijd het woord "auteur", niet maker of kunstenaar.
- Kanaal 2027: alleen de webshop. Winkels zijn een uithangbord (poster of kaartje met QR-code), zonder voorraad of commissie. Verkoop in winkels pas later, met een nieuwe licentie per werk.
- Geen verkoop op beurzen of markten. Nooit cash.
- Eerste verkoop pas als de webshop af is, tussen januari en maart 2027, na de oprichting van de vzw.
- Start met 3 auteurs en 15 tot 30 werken. Printer: Epson P900, ongeveer 300 A3 per maand.
- Losse poster blijft te koop. In de mand kan de klant een "wachtronde" aanvinken: gratis levering in Gent in de eerstvolgende gezamenlijke leverronde.

### 2026-11-02 · Kern · Oplage

- Per kunstenaar 3 tot 5 werken in de Postershop.
- Per werk 1 tot 3 afdrukken.
- Elke afdruk wordt genummerd en gesigneerd door de kunstenaar.

### 2026-11-02 · Kern · Stand van zaken

- "Licensed reproductions": elke poster is een archiefstuk uit het Archief.
- In preview: alleen fictieve placeholders, er wordt niets verkocht.

## Boekhouder

### 2026-11-04 · Boekhouder · Prijs per vorm

Vervangt: 2026-11-02 (Prijs en Public Ledger), voor wat de verdeling betreft.

- **Fine-art:** prijs excl. btw = 7 × M, verdeling 1 materiaal / 3 auteur (bruto) / 3 vzw. M verschilt per werk. Voorstel minimum: M = € 5,00, dus ten minste € 42 incl. btw.
- **Poster:** € 6 los, € 15 voor drie (mixen mag), btw inbegrepen. M = € 1,25. Eerst M eraf, de rest 50/50 tussen auteur en vzw: los € 1,85 auteur / € 1,86 vzw, in bundel € 1,44 elk (excl. btw).
- Btw altijd 21 %. 15 % roerende voorheffing, uitbetaling per kwartaal. Voorstel: de boekhouder controleert bedragen en rekeningnummers, de vzw betaalt uit.
- Voorstel verzendschuif Gent: onder € 15 → € 3; € 15 tot 34,99 → € 1,50; vanaf € 35 of met wachtronde → gratis. Bpost-tarieven nog open.
- Vaste kosten ongeveer € 2.500 per jaar en break-even (80 fine-art, 400 bundels, 300 losse posters) volgens het [dossier voor de boekhouder](boekhouder/dossier-voor-de-boekhouder.html); nog te controleren.
- Financiering alleen met een renteloze lening van de oprichter, zonder vaste termijn, kwijt te schelden. Geen krediet. Printer, inkt en papier als gift.

### 2026-11-02 · Boekhouder · Prijs en Public Ledger

- Prijs = 7 × M. M is de materiaalkost plus 20% voor misdruk. De prijs wordt verdeeld in zeven delen.
- De maker wordt betaald in auteursrechten via een exploitatieovereenkomst.
- Betalen via de mand met EPC-QR en gestructureerde mededeling. Geen betaalprovider.
- De Public Ledger staat in `_data/register.csv`. De bedragen daarin zijn nu nog fictief.

## Technieker

### 2026-11-02 · Technieker · Opbouw

- Zelfde CollectionBuilder-basis als het Archief (Jekyll, Ruby 3.3). GitHub Actions bouwt bij elke push naar main (`.github/workflows/pages.yml`).
- Gebruikt hetzelfde metadatamodel: `metadata: peapickers-archief` in `_config.yml`. Een wijziging aan de basis kijk je ook in het Archief na.
- Volg `AGENTS.md`: configureer via `_config.yml`, `_data/theme.yml` en `config-*.csv`. Eigen CSS alleen in `_sass/_custom.scss`.
