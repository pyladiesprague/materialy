# Tahák – Lekce 5: Vlastní funkce

Rychlý přehled toho, co jsme se naučili. Klidně si ho vytiskni na A4.

## Vlastní funkce

```python
def cena_s_dph(cena):        # def, jméno, parametr, dvojtečka
    return cena * 1.21       # return = co funkce pošle ven

print(cena_s_dph(100))       # volání – teprve teď se funkce spustí
```

Samotné `def` nic neudělá. Funkce se spustí, až když ji zavoláš.

## Parametry a argumenty

```python
def zkontroluj_heslo(heslo, min_delka):    # parametry = jména v definici
    return len(heslo) >= min_delka

zkontroluj_heslo("pyladies", 8)            # argumenty = hodnoty při volání
```

Záleží na pořadí. Když funkce nic zvenku nepotřebuje: `def vylosuj_cislo():`

## Co s návratovou hodnotou

```python
vysledek = cena_s_dph(100)                  # ulož si ji

if zkontroluj_heslo(heslo, 8):              # rozhodni se podle ní
    print("Heslo přijato.")

print(cena_s_dph(100) + cena_s_dph(250))    # počítej s ní
```

Volání funkce se chová jako hodnota, kterou funkce vrátila.

## return funkci ukončí

```python
def ohodnot_znamku(znamka):
    if znamka == 1:
        return "Výborně"
    elif znamka == 2:
        return "Chvalitebně"
    else:
        return "Ještě zabereme"
```

Řádky pod provedeným `return` se neprovedou. Returnů může být ve funkci víc.

## Funkce volá funkci

```python
def zaregistruj(jmeno, heslo):
    if je_heslo_dost_dlouhe(heslo):
        ramecek("Vítej, " + jmeno)
```

## Proměnné uvnitř funkce

```python
def cena_s_dph(cena):
    dan = cena * 0.21
    return cena + dan

print(dan)      # NameError – dan existuje jenom uvnitř funkce
```
