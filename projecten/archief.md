---
title: Archief
---
# Peapickers Archief

Site: <https://peapickers.github.io/peapickersarchief/> · Repo: [peapickers/peapickersarchief](https://github.com/peapickers/peapickersarchief) · Regels: [werkwijze](werkwijze.html)

> Nieuwste item bovenaan in elke sectie. Niets verwijderen: voeg een nieuw item toe.

## Kern

### 2026-11-02 · Kern · Stand van zaken

- Niet-commercieel archief van kunstpraktijken van makers buiten de kunstindustrie. Verkoopt niets.
- In preview: online staan alleen fictieve placeholders.
- Elk archiefstuk heeft een vaste code `ARCHIEFSTUKJJJJ-NNN-NN` die nooit verandert.

## Boekhouder

### 2026-11-02 · Boekhouder · Public Ledger

- De Public Ledger staat in `_data/ledger.csv`, met de pdf's in `ledger/`. Online: <https://peapickers.github.io/peapickersarchief/ledger.html>.
- Eerste echte stukken (30-10-2026): het stappenplan voor de archivaris en het ondernemingsplan (versie 3.1).

## Technieker

### 2026-11-02 · Technieker · Opbouw

- CollectionBuilder-CSV (Jekyll, Ruby 3.3). GitHub Actions bouwt de site bij elke push naar main (`.github/workflows/pages.yml`).
- Data: `_data/peapickers-archief.csv` (één rij per archiefstuk) en `_data/archiefvormers.csv`.
- Volg `AGENTS.md`: configureer via `_config.yml`, `_data/theme.yml` en `config-*.csv`. Eigen CSS alleen in `_sass/_custom.scss`.
- Online staan alleen afgeleiden (max. 1200 px, watermerk, Glaze) via `_hulpscripts/afgeleiden.py`, nooit originelen.
- `noindex` en `robots.txt` weren zoekmachines en AI-crawlers.
