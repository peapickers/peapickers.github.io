---
title: Feed
---
# Peapickers Feed

Site: <https://peapickers.github.io/peapickersfeed/> · Repo: [peapickers/peapickersfeed](https://github.com/peapickers/peapickersfeed) · Regels: [werkwijze](werkwijze.html)

> Nieuwste item bovenaan in elke sectie. Niets verwijderen: voeg een nieuw item toe.

## Kern

### 2026-11-02 · Kern · Stand van zaken

- De Gentse cultuuragenda: film, theater, dans, muziek, lezingen en tentoonstellingen in en rond Gent.
- Prototype. Vroeger heette de repo two-step; het oude adres stuurt niet door.
- Bij elke film een artikel "Funding" over wie de film betaalde, met bronnen.

## Boekhouder

### 2026-11-02 · Boekhouder · Geen inkomsten of kosten

- Verkoopt niets en heeft geen kosten: GitHub Pages en GitHub Actions zijn gratis.

## Technieker

### 2026-11-02 · Technieker · Opbouw

- Statische site: `index.html`, `screenings.json`, `films.json` en `feed.xml` (RSS).
- Een GitHub Action (`.github/workflows/update-listings.yml`) werkt de agenda elke woensdagochtend bij met de scripts in `scripts/`.
- Niet automatisch: Funding-artikels, lezingen en tentoonstellingen. Die gebeuren in een Claude-sessie.
- `igmcp/` bevat bestanden voor de Instagram-server op de Mac van Jonas.
