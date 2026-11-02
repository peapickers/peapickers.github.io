---
title: Postershop
---
# Peapickers Postershop

Site: <https://peapickers.github.io/postershoppeapickers/> · Repo: [peapickers/postershoppeapickers](https://github.com/peapickers/postershoppeapickers) · Regels: [werkwijze](werkwijze.html)

> Nieuwste item bovenaan in elke sectie. Niets verwijderen: voeg een nieuw item toe.

## Kern

### 2026-11-02 · Kern · Oplage

- Per kunstenaar 3 tot 5 werken in de Postershop.
- Per werk 1 tot 3 afdrukken.
- Elke afdruk wordt genummerd en gesigneerd door de kunstenaar.

### 2026-11-02 · Kern · Stand van zaken

- "Licensed reproductions": elke poster is een archiefstuk uit het Archief.
- In preview: alleen fictieve placeholders, er wordt niets verkocht.

## Boekhouder

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
