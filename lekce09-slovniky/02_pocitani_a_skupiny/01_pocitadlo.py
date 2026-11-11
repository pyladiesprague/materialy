# ---------------------------------------------
#  Slovník jako počítadlo
# ---------------------------------------------
# Spusť soubor a porovnej výsledky.

# Hosté hlasovali, která písnička na večírku zazní jako první:
hlasy = ["Trezor", "Jožin z bažin", "Trezor", "Holky z naší školky",
         "Trezor", "Jožin z bažin"]


# Metodou count z lekce 8 spočítáš hlasy pro jednu písničku:
print(hlasy.count("Trezor"))    # 3

# Na všechny písničky bys ale musela předem vědět, které to jsou,
# a zavolat count pro každou zvlášť. Slovník spočítá všechny najednou,
# za jeden průchod cyklem. Klíč je písnička a hodnota počet hlasů.
#
# V první sekci jsi přičítala sklenky řádkem
# sklenky["Anna"] = sklenky["Anna"] + 1. Tady by stejný řádek spadl hned
# u prvního hlasu:
#
#     pocty = {}
#     pocty["Trezor"] = pocty["Trezor"] + 1     KeyError: 'Trezor'
#
# Pravá strana čte klíč, který ve slovníku ještě není. Proto se nejdřív
# zeptáš, jestli tam písnička už je:
pocty = {}

for pisnicka in hlasy:
    if pisnicka in pocty:
        pocty[pisnicka] = pocty[pisnicka] + 1
    else:
        pocty[pisnicka] = 1

print(pocty)    # {'Trezor': 3, 'Jožin z bažin': 2, 'Holky z naší školky': 1}

# Když písnička ve slovníku ještě není, dostane první hlas. Když už tam
# je, přičte se jí jednička. Je to počítadlo z lekce 3, jen jich máš
# tolik, kolik je různých písniček.


# Totéž jde napsat kratší cestou, metodou get. Vrátí dosavadní počet
# hlasů, nebo 0, když písnička ještě žádný nemá:
pocty = {}

for pisnicka in hlasy:
    pocty[pisnicka] = pocty.get(pisnicka, 0) + 1

print(pocty)    # {'Trezor': 3, 'Jožin z bažin': 2, 'Holky z naší školky': 1}

# Oba zápisy dělají totéž. Používej ten, kterému rozumíš líp.


# Text se prochází po znacích (lekce 3), takže stejně spočítáš písmena:
pismena = {}

for pismeno in "ananas":
    if pismeno in pismena:
        pismena[pismeno] = pismena[pismeno] + 1
    else:
        pismena[pismeno] = 1

print(pismena)  # {'a': 3, 'n': 2, 's': 1}
