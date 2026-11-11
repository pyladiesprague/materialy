# ---------------------------------------------
#  Rozdělení do skupin
# ---------------------------------------------
# Spusť soubor a porovnej výsledky.

prinesou = [("Anna", "dort"), ("Petra", "víno"), ("Jana", "chlebíčky"),
            ("Eva", "víno"), ("Marie", "dort")]


# Kdo přinese který dárek? Klíč je dárek a hodnota seznam jmen. Seznam
# pro dárek založíš, když na dárek narazíš poprvé. Pak do něj přidáváš:
podle_darku = {}

for jmeno, darek in prinesou:
    if darek not in podle_darku:
        podle_darku[darek] = []
    podle_darku[darek].append(jmeno)

print(podle_darku)
# {'dort': ['Anna', 'Marie'], 'víno': ['Petra', 'Eva'], 'chlebíčky': ['Jana']}


# Řádek s append čti po krocích. Dělá totéž co tyhle dva řádky:
#
#     jmena = podle_darku[darek]      seznam, který patří k dárku
#     jmena.append(jmeno)             přidá do něj jméno
#
# Seznam ve slovníku se tím změní. Proměnná jmena a podle_darku[darek]
# jsou dvě jména pro jeden seznam, jako v lekci 8.


# Skupiny pak projdeš jako každý slovník. Seznam jmen spojíš metodou join:
for darek, jmena in podle_darku.items():
    print(f"{darek}: {', '.join(jmena)}")

# dort: Anna, Marie
# víno: Petra, Eva
# chlebíčky: Jana


# Klíčem může být i n-tice. Tak rozdělíš hosty podle dvou věcí najednou,
# třeba podle stolu a nápoje:
hoste = [("Anna", 1, "víno"), ("Petra", 1, "džus"), ("Jana", 2, "víno"),
         ("Eva", 1, "víno")]

skupiny = {}

for jmeno, stul, napoj in hoste:
    klic = (stul, napoj)
    if klic not in skupiny:
        skupiny[klic] = []
    skupiny[klic].append(jmeno)

print(skupiny)
# {(1, 'víno'): ['Anna', 'Eva'], (1, 'džus'): ['Petra'], (2, 'víno'): ['Jana']}

print(skupiny[(1, "víno")])     # ['Anna', 'Eva']

# Seznam klíčem být nemůže, protože se dá měnit. Python by spadl
# s hláškou TypeError: unhashable type: 'list'. N-tice se měnit nedá
# (lekce 8), proto klíčem být může.
