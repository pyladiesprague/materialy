# Tahák – Lekce 9: Slovníky

Rychlý přehled toho, co jsme se naučili. Klidně si ho vytiskni na A4.

## Slovník

```python
darky = {"Anna": "dort", "Petra": "víno"}   # klíč: hodnota
prazdny = {}

darky["Petra"]              # víno     čtení podle klíče
len(darky)                  # 2        počet dvojic
f"{darky['Petra']}"         # v f-stringu klíč do apostrofů
```

Klíč bývá text nebo číslo, hodnota může být cokoli, i seznam nebo další
slovník. Každý klíč je ve slovníku jen jednou.

## Když klíč chybí

```python
darky["Karel"]              # KeyError: 'Karel'

"Karel" in darky            # False    in hledá mezi klíči, ne hodnotami
darky.get("Karel")          # None     nespadne
darky.get("Karel", "nic")   # nic      vlastní výchozí hodnota

if darky.get("Karel") is None:
    print("Karel nic nepřinese.")
```

Klíče rozlišují velká a malá písmena: `"petra"` není `"Petra"`.

## Měnění

| Zápis | Co dělá |
|---|---|
| `darky["Jana"] = "chlebíčky"` | přidá dvojici, nebo přepíše hodnotu, když klíč už je |
| `darky["Anna"] = darky["Anna"] + 1` | změní hodnotu výpočtem (klíč už musí být ve slovníku) |
| `darky.pop("Jana")` | odebere dvojici a **vrátí její hodnotu** |
| `darky.copy()` | samostatná kopie |

Slovník nemá `append`.

## Procházení

```python
for klic in darky:                      # jen klíče
for hodnota in darky.values():          # jen hodnoty
for klic, hodnota in darky.items():     # obojí – nejčastější

sum(utrata.values())                    # součet hodnot, stejně min a max
```

## Stavění slovníku v cyklu

```python
delky = {}                      # začni prázdným
for jmeno in hoste:
    delky[jmeno] = len(jmeno)   # přiřazuj pod klíč
```

## Počítadlo

```python
pocty = {}
for pisnicka in hlasy:
    if pisnicka in pocty:
        pocty[pisnicka] = pocty[pisnicka] + 1
    else:
        pocty[pisnicka] = 1

# kratší zápis téhož:
#     pocty[pisnicka] = pocty.get(pisnicka, 0) + 1
```

## Kdo vyhrál

```python
vitez = None
nejvic = 0
for pisnicka, pocet in pocty.items():
    if pocet > nejvic:
        vitez = pisnicka
        nejvic = pocet
```

`max(pocty.values())` řekne jen nejvyšší počet, ne klíč.

## Skupiny

```python
podle_darku = {}
for jmeno, darek in prinesou:
    if darek not in podle_darku:
        podle_darku[darek] = []         # seznam založ při prvním potkání
    podle_darku[darek].append(jmeno)

skupiny[(1, "víno")]                    # klíčem může být n-tice, seznam ne
```

## Záznamy a tabulky

```python
anna = {"jmeno": "Anna", "vek": 34}     # záznam: klíče jsou názvy údajů

hoste = [                               # seznam slovníků = tabulka
    {"jmeno": "Anna", "vek": 34},
    {"jmeno": "Petra", "vek": 25},
]
hoste[0]["jmeno"]                       # Anna – čte se zleva doprava

vecirek["rozpocet"]["piti"]             # data v datech, po krocích
```

## Seznam, nebo slovník?

- **seznam:** záleží na pořadí, hodnoty nemají jméno (fronta, playlist, teploty)
- **slovník:** hledáš podle jména nebo kódu (ceník, telefonní seznam, překlady)

## Slovník ve funkci

Funkce dostane ten samý slovník. Když ho změní, je to vidět i venku.
Když to nechceš, pracuj s kopií:

```python
novy = host.copy()
druhy = host                # NEkopíruje – dvě jména pro jeden slovník
```

## Časté chyby

| Hláška | Co se většinou stalo |
|---|---|
| `KeyError: 'Karel'` | klíč ve slovníku není, nebo se liší velkými písmeny |
| `KeyError` u `d[k] = d[k] + 1` | první přičtení ke klíči, který ještě neexistuje |
| `TypeError: unhashable type: 'list'` | seznam jako klíč – použij n-tici |
| prázdný nebo jen poslední výsledek | `pocty = {}` je uvnitř cyklu místo před ním |
| změnil se i původní slovník | `b = a` místo `b = a.copy()` |
