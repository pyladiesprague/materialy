# ---------------------------------------------
#  Procházení slovníku
# ---------------------------------------------
# Spusť soubor a porovnej výsledky.

darky = {"Anna": "dort", "Petra": "víno", "Jana": "chlebíčky"}


# Cyklus for prochází klíče:
for jmeno in darky:
    print(jmeno)

# Anna
# Petra
# Jana


# Hodnotu si ke klíči přečteš jako obvykle:
for jmeno in darky:
    print(f"{jmeno} přinese {darky[jmeno]}.")

# Anna přinese dort.
# Petra přinese víno.
# Jana přinese chlebíčky.


# Metoda values vrátí jen hodnoty:
for darek in darky.values():
    print(darek)

# dort
# víno
# chlebíčky

# Když hodnoty rovnou vypíšeš, vypadá to zvláštně. V cyklu nebo v sum
# se s nimi ale pracuje jako se seznamem:
print(darky.values())   # dict_values(['dort', 'víno', 'chlebíčky'])


# Metoda items vrátí dvojice klíč–hodnota. Rozbalíš je stejně jako
# seznam n-tic v lekci 8. Je to nejčastější způsob, jak slovník projít:
for jmeno, darek in darky.items():
    print(f"{jmeno} přinese {darek}.")

# Anna přinese dort.
# Petra přinese víno.
# Jana přinese chlebíčky.


# Na čísla ve slovníku fungují sum, min a max. Stačí jim dát hodnoty:
utrata = {"víno": 450, "dort": 420, "chlebíčky": 360}

print(sum(utrata.values()))     # 1230
print(max(utrata.values()))     # 450

# Funkce max vrátí jen nejvyšší částku, ne zboží, ke kterému patří.
# Jak najít i klíč, uvidíš v další sekci.


# Shrnutí:
#
#     for klic in slovnik:                    jen klíče
#     for hodnota in slovnik.values():        jen hodnoty
#     for klic, hodnota in slovnik.items():   obojí
#
# Pamatovat si to nemusíš – všechno ze slovníků najdeš v taháku.
