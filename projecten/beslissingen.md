---
title: Beslissingenregister
---
# Beslissingenregister

Eén plek met alle beslissingen, in gewone woorden. Elke regel heeft een code `JJJJ-MM-DD_Project<nr>`, een korte titel en wat er geldt. Cijfers en uitwerking staan in [BESLISSINGEN.md](https://github.com/peapickers/postershoppeapickers/blob/main/BESLISSINGEN.md) (postershop). Dit register is de index, geen kopie.

## Werkwijze

1. Een project dat iets beslist, voegt **één regel** toe onderaan de tabel hieronder. Geen aparte momentopname meer.
2. Code = datum van de beslissing + naam van het project + volgnummer van dat project (`2026-11-07_Jurist4`). Eén nummer per beslissing, niet per vragenlijst.
3. De titel zegt in gewone woorden wat beslist is. In tekst nooit de kale code gebruiken, altijd de titel (code hooguit tussen haakjes).
4. Vervangt de beslissing een oudere, zet dan die code in "Vervangt" en zet bij de oude regel de status op "vervangen". Nooit regels verwijderen.
5. Status: `geldt`, `vervangen`, `voorlopig` of `open`. Kolom "In BESLISSINGEN.md": ja of nee.
6. Controle zonder Claude: `python3 scripts/beslissingen-check.py` (dubbele of ontbrekende codes, verwijzingen naar bestaande codes, lijst van wat nog niet in BESLISSINGEN.md staat).
7. De oude momentopnames blijven als archief en hoeven niet meer gelezen te worden: [boekhouder 7-11](boekhouder/beslissingen-2026-11-07.html), [ondernemingsplan 7-11 avond](ondernemingsplan/beslissingen-2026-11-07-avond.html), [ondernemingsplan 8-11](ondernemingsplan/beslissingen-2026-11-08.html). De oude codes (D1, V1, ...) staan in de laatste kolom.

## Register

| Code | Titel | Wat geldt | Status | Vervangt | In BESLISSINGEN.md | Oude code |
| --- | --- | --- | --- | --- | --- | --- |
| 2026-11-07_Boekhouder1 | Boekhouding in zelfbeheer | De oprichter boekt en doet alle aangiftes zelf. | geldt | | ja | D1 |
| 2026-11-07_Boekhouder2 | ITAA-boekhouder controleert | Vaste maandvergoeding, minstens 1 controle per jaar (vóór 31 december en vóór de neerlegging). | geldt | | ja | D2 |
| 2026-11-07_Boekhouder3 | Software van de boekhouder | Niet Accountable; de software die de boekhouder gebruikt. | geldt | | ja | D3 |
| 2026-11-07_Boekhouder4 | Vereenvoudigde boekhouding | Tenzij de boekhouder dubbel aanraadt. | geldt | | ja | D4 |
| 2026-11-07_Boekhouder5 | Productieplek max. € 150 per maand | Een paar m² bij een bestaand bedrijf. | vervangen | | ja | D5 |
| 2026-11-07_Boekhouder6 | Zetel op productieplek of bij familie | Liefst op de productieplek. | vervangen | | ja | D6 |
| 2026-11-07_Boekhouder7 | Extern gedeeld pand | Zetel daar, geen zetel bij familie. | vervangen | | ja | D7 |
| 2026-11-07_Boekhouder8 | Lening niet nodig bij extern pand | Lening en overname van materiaal niet nodig. | vervangen | | ja | D8 |
| 2026-11-07_Boekhouder9 | Medebestuurder blijft nodig | Minstens 2 bestuurders, geen "niet-uitvoerend" bestuurder. | geldt | | ja | D9 |
| 2026-11-07_Boekhouder10 | 14 dagen herroepingsrecht met herroepingsknop | Voor Poster en Limited; bewaren 10 jaar. | geldt | | ja | D10 |
| 2026-11-07_Boekhouder11 | Auteurs enkel uit België | Tot de boekhouder anders adviseert. | geldt | | ja | D11 |
| 2026-11-07_Compiler1 | Oprichter drukt zelf, kosteloos | Als particulier, buiten de vzw; geen productieplek. | geldt | 2026-11-07_Boekhouder5 | ja | V1 |
| 2026-11-07_Compiler2 | Dienst en vzw gescheiden | Oprichter krijgt nooit geld of voordeel; geen kosten, post of klanten op het adres van de productie. | geldt | | ja | V2 |
| 2026-11-07_Compiler3 | Zetel bij de medebestuurder | Zetel, administratie, post en back-up daar. | geldt | 2026-11-07_Boekhouder6 | ja | V3 |
| 2026-11-07_Compiler4 | Verdeling 50/50 | Auteursrechten (bruto) 50 %, vzw 50 %; papier en inkt zijn een uitgave per aankoop. | geldt | | ja | V4 |
| 2026-11-07_Compiler5 | Printer is van de oprichter | Geen bruikleen; vzw koopt papier en inkt. | geldt | | ja | V5 |
| 2026-11-07_Compiler6 | Public Ledger toont "gratis dienst" | Zonder naam en bedrag; geen wettelijke boekhouding. | geldt | | ja | V6 |
| 2026-11-07_Compiler7 | Lening van de oprichter | Per uitgave, renteloos, geen termijn. | geldt | 2026-11-07_Boekhouder8 | ja | V7 |
| 2026-11-07_Compiler8 | Eigen pand vanaf 2029 | Uitwerken in 2028. | geldt | | ja | V8 |
| 2026-11-07_Compiler9 | Consumentenprijs onderzoeken | Marktgemiddelde min 30 tot 40 %. | voorlopig | | ja | V9 |
| 2026-11-08_Jurist1 | Verdeling 50/50 geldt nu al | Prijs blijft 7 × M tot marketing het onderzoek bevestigt. | geldt | | ja | |
| 2026-11-08_Jurist2 | Lening is een echte lening | Gestort per uitgave, met register. | geldt | | ja | |
| 2026-11-08_Jurist3 | Aansprakelijkheid | De vzw is aansprakelijk, behalve bij opzet of grove fout van de oprichter. | geldt | | ja | |
| 2026-11-08_Jurist4 | Open punten naar Cultuurloket | Zij zeggen welke expert antwoordt. | open | | ja | |
