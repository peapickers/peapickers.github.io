---
title: Postershop
---
# Peapickers Postershop

Site: <https://peapickers.github.io/postershoppeapickers/> · Repo: [peapickers/postershoppeapickers](https://github.com/peapickers/postershoppeapickers) · Regels: [werkwijze](werkwijze.html)

> Nieuwste item bovenaan in elke sectie. Niets verwijderen: voeg een nieuw item toe.

## Kern

### 2026-11-03 · Kern · Geen kader of ophangsysteem

Vervangt: 2026-11-03 (kader en latten in het dossier voor de boekhouder en in stappenplan v4)

- Peapickers levert nooit een kader of ophangsysteem. Het idee van houten latten met touw is geschrapt.
- Dat geldt ook voor wat er nog over kader en latten staat in het [dossier voor de boekhouder](boekhouder/dossier-voor-de-boekhouder.html) en in [stappenplan v4](jurist/stappenplan-workflow-extended-v4.html). Die momentopnames blijven ongewijzigd staan.

### 2026-11-03 · Kern · Oplage per reproductievorm

Vervangt: 2026-11-02 (Oplage), voor posters

- Fine-art: per werk 1 tot 3 exemplaren, genummerd en gesigneerd.
- Poster: print on demand met een vaste verkooptermijn, zonder beperking van de oplage.
- Details: [dossier voor de boekhouder](boekhouder/dossier-voor-de-boekhouder.html), hoofdstuk 1 en 3.

### 2026-11-02 · Kern · Oplage

- Per kunstenaar 3 tot 5 werken in de Postershop.
- Per werk 1 tot 3 afdrukken.
- Elke afdruk wordt genummerd en gesigneerd door de kunstenaar.

### 2026-11-02 · Kern · Stand van zaken

- "Licensed reproductions": elke poster is een archiefstuk uit het Archief.
- In preview: alleen fictieve placeholders, er wordt niets verkocht.

## Boekhouder

### 2026-11-03 · Boekhouder · M en betalen

Vervangt: 2026-11-02 (Prijs en Public Ledger), voor M en de betaalwijze

- M is alleen inkt en papier, op het grootste formaat. Misdruk en alle andere kosten komen uit de commissie van de vzw. Prijsmodel per reproductievorm: [dossier](boekhouder/dossier-voor-de-boekhouder.html), hoofdstuk 3.
- Betalen met Bancontact of een gratis optie. Welke betaaldienst, ligt nog niet vast.

### 2026-11-02 · Boekhouder · Prijs en Public Ledger

- Prijs = 7 × M. M is de materiaalkost plus 20% voor misdruk. De prijs wordt verdeeld in zeven delen.
- De maker wordt betaald in auteursrechten via een exploitatieovereenkomst.
- Betalen via de mand met EPC-QR en gestructureerde mededeling. Geen betaalprovider.
- De Public Ledger staat in `_data/register.csv`. De bedragen daarin zijn nu nog fictief.

## Technieker

### 2026-11-03 · Technieker · Wat de webshop moet krijgen

- Per werk de keuze fine-art of poster, met de volledige prijsopbouw (materiaal, kunstenaar, vzw, afronding, verzending, btw).
- Schuifregelaars voor de passe-partout, enkel bij fine-art.
- Een filter voor naaktheid en een pagina "Meepikken?" met de curatielijn.
- Geen keuze voor een kader of ophangsysteem.
- Bron: [stappenplan v4](jurist/stappenplan-workflow-extended-v4.html), stap 1.6. De site zelf is nog niet aangepast.

### 2026-11-02 · Technieker · Opbouw

- Zelfde CollectionBuilder-basis als het Archief (Jekyll, Ruby 3.3). GitHub Actions bouwt bij elke push naar main (`.github/workflows/pages.yml`).
- Gebruikt hetzelfde metadatamodel: `metadata: peapickers-archief` in `_config.yml`. Een wijziging aan de basis kijk je ook in het Archief na.
- Volg `AGENTS.md`: configureer via `_config.yml`, `_data/theme.yml` en `config-*.csv`. Eigen CSS alleen in `_sass/_custom.scss`.
