---
title: Printshop
---
# Peapickers Printshop

Site: <https://peapickers.github.io/printshoppeapickers/> · Repo: [peapickers/printshoppeapickers](https://github.com/peapickers/printshoppeapickers) · Regels: [werkwijze](werkwijze.html)

> Nieuwste item bovenaan in elke sectie. Niets verwijderen: voeg een nieuw item toe.

## Kern

### 2026-11-02 · Kern · Stand van zaken

- Fotoprints op bestelling. Levering in Gent en deelgemeenten, betalen aan de deur.
- In preview.

## Boekhouder

### 2026-11-02 · Boekhouder · Prijs en betalen

- Prijs = 3 × M. M is de materiaalkost van één print (papier en inkt) plus 20% voor misdruk. Geen auteursrechten of voorschotten.
- De materiaalkosten in `js/config.js` zijn nog voorbeeldbedragen.
- Betalen aan de deur: cash of Payconiq/overschrijving. Leverkost staat in `js/config.js`.

## Technieker

### 2026-11-02 · Technieker · Opbouw

- Statische HTML/JS zonder build. Alle instellingen staan in `js/config.js`: prijzen, leveruren, postcodes, links.
- Bestellingen gaan via een ntfy-pushmelding (alleen het bestelnummer, nooit klantgegevens) en een mail naar het Proton-adres van de printshop.
- Een GitHub Action (`.github/workflows/beschikbaarheid.yml`) zet de Proton-agenda elk uur om naar `beschikbaarheid.json`. Het geheim heet `AGENDA_ICS_URL`.
