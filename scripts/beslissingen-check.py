#!/usr/bin/env python3
"""Controleert projecten/beslissingen.md. Gebruik: python3 scripts/beslissingen-check.py"""
import re, sys
rows = []
for l in open("projecten/beslissingen.md", encoding="utf-8"):
    c = [x.strip() for x in l.strip().strip("|").split("|")]
    if len(c) == 7 and re.match(r"\d{4}-\d{2}-\d{2}_[A-Za-z]+\d+$", c[0]):
        rows.append(c)
codes = [r[0] for r in rows]
err = [f"dubbele code: {c}" for c in set(codes) if codes.count(c) > 1]
for r in rows:
    if r[3] not in ("geldt", "vervangen", "voorlopig", "open"): err.append(f"{r[0]}: onbekende status '{r[3]}'")
    if r[5] not in ("ja", "nee"): err.append(f"{r[0]}: kolom In BESLISSINGEN.md moet ja of nee zijn")
    if r[4] and r[4] not in codes: err.append(f"{r[0]}: vervangt onbekende code {r[4]}")
for r in rows:
    if r[5] == "nee": print("Nog niet in BESLISSINGEN.md:", r[0], "-", r[1])
print(len(rows), "beslissingen;", "fouten:" if err else "geen fouten")
print("\n".join(err)); sys.exit(1 if err else 0)
