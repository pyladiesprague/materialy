# Materiály – kurz PyLadies Praha

Výukové materiály kurzu programování v Pythonu pro začátečnice.
Běh **podzim 2026**, 13 lekcí.

## Jak si materiály stáhnout

Nahoře klikni na zelené tlačítko **Code** → **Download ZIP**. Stažený archiv
rozbal a složku otevři ve VS Code (**File → Open Folder**).

Po každé lekci sem přibude nová složka. Stáhni si ZIP znovu – nové lekce se
přidávají, ty starší zůstávají beze změny.

## Lekce

| # | Složka | Téma |
|---|---|---|
| 1 | `lekce01-prvni-program/` | print, aritmetika, proměnné, input |
| 2 | `lekce02-podminky/` | porovnávání, if/elif/else, and/or/not |
| 3 | `lekce03-funkce-a-cyklus-for/` | vestavěné funkce, cyklus for |
| 4 | `lekce04-cyklus-while/` | cyklus while, break, continue, for vs while |
| 5 | `lekce05-vlastni-funkce/` | def, parametry, return |

Další lekce přibývají v průběhu kurzu.

## Co najdeš v každé lekci

```
TAHAK.md                   shrnutí na jednu stránku
01_koncept/                složka na každý koncept
   NN_nazev.py             výklad se spustitelnými ukázkami
   cviceni/                úkoly k procvičení, jeden soubor na úlohu
   cviceni/reseni/         vzorová řešení
   cviceni_bonusy/         bonusy pro rychlíky
   cviceni_bonusy/reseni/  řešení bonusů
```

Obrázky k výkladu leží přímo ve složce konceptu. Ne každý koncept má bonusy a
opakovací koncepty můžou mít jen cvičení.

Soubory s výkladem procházej popořadě podle čísla, spouštěj je tlačítkem
**Run** vpravo nahoře a čti komentáře. Pak se pusť do složky `cviceni/`.

## Pro autory

Z materiálů se automaticky generuje web kurzu
([pyladiesprague/public-pages](https://github.com/pyladiesprague/public-pages)),
proto musí soubory dodržet formát, který převod umí přečíst:

- Výklad `NN_nazev.py` začíná titulkem mezi dvěma řádky `# ---`.
- Úloha v `cviceni/` nebo `cviceni_bonusy/` má jeden soubor na úlohu a první
  řádek `# Cvičení N – …` nebo `# Bonus N – …`, kde N odpovídá číslu `NN_` v názvu.
- Řešení má v `reseni/` stejný název souboru a první řádek
  `# Řešení cvičení N – …` nebo `# Řešení bonusu N – …`.

Podrobný popis formátu je v
[návodu k importu](https://github.com/pyladiesprague/public-pages/blob/main/code/materials/README.md)
(repo je soukromé, vidí ho kouči).

Kontrolu dělá GitHub Action `.github/workflows/web.yml`. U každého PR (kromě PR
z forků, které nemají přístup k tokenu `PUBLIC_PAGES_TOKEN`) a po každém pushi
do `main` zkusí materiály převést na web, nic přitom nezapisuje; chyba formátu
nebo konflikt s redakčními opravami webu kontrolu shodí. Po úspěšném pushi do
`main` pak pošle webu signál `materialy-push` a ten otevře PR s novými stránkami.
