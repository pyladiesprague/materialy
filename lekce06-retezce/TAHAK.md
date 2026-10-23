# Tahák – Lekce 6: Řetězce

Rychlý přehled toho, co jsme se naučili. Klidně si ho vytiskni na A4.

## f-string

```python
jmeno = "Anna"
vek = 30

print(f"Ahoj {jmeno}, je ti {vek} let.")    # f před uvozovkami, hodnota v {}
```

Do složených závorek patří cokoliv, co má hodnotu: proměnná, výpočet,
vestavěná funkce, porovnání i volání vlastní funkce.

```python
print(f"Zbývá {stran_celkem - precteno} stran.")
print(f"Název má {len(kniha)} znaků.")
print(f"Jsem za polovinou? {precteno > stran_celkem / 2}")
print(f"Přečteno: {procenta(precteno, stran_celkem)} %")
```

## Za dvojtečkou se říká, jak to má vypadat

```python
print(f"{cena:.2f}")        # 301.29   dvě desetinná místa
print(f"{mesto:12}")        # text na dvanáct míst, zarovnaný doleva
print(f"{teplota:8.1f}")    # číslo na osm míst, zarovnané doprava
print(f"{mesto:>12}")       # > doprava, < doleva
```

## Speciální znaky

```python
print("první\ndruhý")       # \n   nový řádek
print("Řekla \"ahoj\".")    # \"   uvozovka uvnitř uvozovek
print('Řekla "ahoj".')      #      nebo jednoduché uvozovky zvenku
print("C:\\Users\\Anna")    # \\   zpětné lomítko
```

Delší text se píše mezi tři uvozovky a f před ně patří stejně jako před jedny:

```python
print(f"""Přihláška přijata

Jméno:  {jmeno}
Termín: {den} od {hodina} hodin""")
```

## Metody řetězců

```python
slovo.upper()                     # PYLADIES
slovo.lower()                     # pyladies
slovo.title()                     # Anna Nováková
slovo.strip()                     # mezery na krajích pryč
slovo.count("a")                  # kolikrát tam písmeno je
veta.replace("synergie", "spolupráci")    # vymění všechny výskyty
slovo.isdigit()                   # jsou to samé číslice?
slovo.startswith("Py")
slovo.endswith(".pdf")
```

Metoda původní text nemění, vrací nový:

```python
slovo = "pyladies"
slovo.upper()           # výsledek nikdo nevzal
print(slovo)            # pyladies

slovo = slovo.upper()   # takhle změna zůstane
```

Metody se dají psát za sebe, vyhodnocuje se to zleva doprava:

```python
odpoved = input("ano/ne? ").strip().lower()
```

## Kontrola vstupu

```python
vek = input("Kolik ti je? ").strip()

if vek.isdigit():
    print(int(vek) + 1)
else:
    print("To není číslo.")
```

Bez té kontroly by `int("třicet")` spadlo na `ValueError`.

## Index

Index se počítá od nuly, od konce záporně.

```
         P   y   L   a   d   i   e   s
       ╭───┬───┬───┬───┬───┬───┬───┬───╮
       │ 0 │ 1 │ 2 │ 3 │ 4 │ 5 │ 6 │ 7 │
       │-8 │-7 │-6 │-5 │-4 │-3 │-2 │-1 │
       ╰───┴───┴───┴───┴───┴───┴───┴───╯
```

```python
slovo[0]        # P
slovo[-1]       # s    poslední
slovo[8]        # IndexError – poslední index je o jedna menší než délka
```

## Výřez

U výřezu ukazují čísla na značky mezi znaky:

```
       ╭───┬───┬───┬───┬───┬───┬───┬───╮
       │ P │ y │ L │ a │ d │ i │ e │ s │
       ╰───┴───┴───┴───┴───┴───┴───┴───╯
       0   1   2   3   4   5   6   7   8
      -8  -7  -6  -5  -4  -3  -2  -1
```

```python
slovo[0:2]      # Py         druhé číslo se nepočítá, jako u range
slovo[:2]       # Py         od začátku
slovo[2:]       # Ladies     až do konce
slovo[-3:]      # ies        poslední tři
slovo[::2]      # PLde       krok po dvou
slovo[::-1]     # seidaLyP   otočení
```

## Text se nedá přepsat

Řetězec jednou vznikne a od té chvíle se nemění – je neměnný.

```python
slovo[0] = "v"              # TypeError

novy = "v" + slovo[1:]      # nový řetězec z výřezů
```

## Hledání v textu

```python
"Ladies" in slovo           # True
"Gentlemen" not in slovo    # True
"ladies" in slovo.lower()   # True – když nemá vadit velikost písmen
```
