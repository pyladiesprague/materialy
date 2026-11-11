# Tahák – Lekce 8: Seznamy a n-tice

Rychlý přehled toho, co jsme se naučili. Klidně si ho vytiskni na A4.

## Seznam

```python
hoste = ["Anna", "Petra", "Jana", "Eva"]
prazdny = []

len(hoste)          # 4
hoste[0]            # Anna      index od nuly
hoste[-1]           # Eva       záporný index od konce
hoste[:2]           # ['Anna', 'Petra']   výřez vrací nový seznam
hoste[4]            # IndexError – poslední index je len(hoste) - 1
```

## Procházení a hledání

```python
for host in hoste:              # položky po jedné
    print(f"Milá {host}, přijď!")

"Petra" in hoste                # True    je v seznamu?
"Karel" not in hoste            # True    není v seznamu?
velikost in ["S", "M", "L"]     # místo tří porovnání s or

napoje.count("víno")            # kolikrát tam položka je
sum(veky), min(veky), max(veky)
sum(veky) / len(veky)           # průměr
```

U řetězce `in` najde i kus textu, u seznamu porovnává celé položky.

## Stavění seznamu v cyklu

```python
drahe = []                      # začni prázdným
for cena in ceny:
    if cena > 100:              # podmínka rozhodne, co se přidá
        drahe.append(cena)

list(range(1, 6))               # [1, 2, 3, 4, 5]
```

## Metody, které seznam mění

| Zápis | Co dělá |
|---|---|
| `hoste[1] = "Marie"` | nahradí položku na indexu |
| `hoste.append("Eva")` | přidá na konec |
| `hoste.insert(0, "Eva")` | vloží na index, ostatní se posunou doprava |
| `hoste.remove("Jana")` | odebere podle hodnoty (když tam není → `ValueError`) |
| `hoste.pop(0)` | odebere podle indexu a vrátí ji |
| `hoste.pop()` | odebere a vrátí poslední |
| `hoste.sort()` | seřadí od nejmenšího, `Č` a další české znaky až za `z` |
| `hoste.sort(reverse=True)` | seřadí obráceně |

Metody `append`, `insert`, `remove` a `sort` mění seznam a vrací `None`.
Jejich výsledek nikam neukládej:

```python
hoste.sort()                # správně
hoste = hoste.sort()        # špatně – v hoste je teď None
```

Výjimka je `pop`: seznam změní a odebranou položku vrátí.

```python
prvni = hoste.pop(0)        # v prvni je odebraná položka
```

## Text a seznam

```python
"Anna, Petra, Jana".split(", ")     # ['Anna', 'Petra', 'Jana']
"Python je fajn".split()            # podle mezer

", ".join(hoste)                    # Anna, Petra, Jana
```

U `join` je tečka za oddělovačem, seznam patří do závorek. Položky musí být
texty.

## Dvě jména, jeden seznam

```python
catering = hoste            # NEkopíruje – obě jména ukazují na jeden seznam
catering = hoste.copy()     # samostatná kopie
catering = hoste[:2]        # výřez je taky nový seznam
```

Funkce, které pošleš seznam, dostane ten samý seznam. Když ho změní, je to
vidět i venku.

## N-tice

```python
anna = ("Anna", "dort")             # dvojice
petra = ("Petra", "víno", 2)        # trojice

anna[0]                             # Anna    čte se jako seznam
anna[1] = "koláč"                   # TypeError – n-tice se nemění
```

- **Seznam:** věci stejného druhu, počet se mění (hosté).
- **N-tice:** pevný počet, každá pozice znamená něco jiného (jméno a dárek).

Anglicky se n-tici říká `tuple`.

## Rozbalování

```python
jmeno, darek = anna                 # počet proměnných = počet hodnot
vlevo, vpravo = vpravo, vlevo       # prohození

def rozsad(hoste, mist):
    return hoste // mist, hoste % mist      # funkce vrátí dvě hodnoty

stoly, zbyva = rozsad(17, 4)

for jmeno, darek in darky:          # seznam n-tic, rozbalí se v cyklu
    print(f"{jmeno} přinese {darek}.")

darky.append(("Eva", "víno"))       # vnitřní závorky n-tice, vnější append
```

## Enumerate

```python
for poradi, bod in enumerate(program, start=1):
    print(f"{poradi}. {bod}")       # 1. přípitek, 2. večeře, ...
```

Bez `start=1` se čísluje od nuly.

## Časté chyby

| Hláška | Co se většinou stalo |
|---|---|
| `IndexError: list index out of range` | index za koncem – poslední je `len(seznam) - 1` |
| `ValueError: list.remove(x): x not in list` | `remove` hodnoty, která v seznamu není |
| `ValueError: too many values to unpack` | víc hodnot než proměnných při rozbalování |
| `TypeError: 'tuple' object does not support item assignment` | změna n-tice |
| `None` místo seznamu | výsledek `sort` nebo `append` uložený do proměnné |
| změnily se oba seznamy | `b = a` místo `b = a.copy()` |
