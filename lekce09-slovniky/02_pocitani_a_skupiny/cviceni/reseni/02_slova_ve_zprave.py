# Řešení cvičení 2 – Počítání a skupiny
# Tvoje řešení může vypadat jinak, a to je v pořádku.

# Napiš funkci spocitej_slova, která má na vstupu text a vrátí slovník:
#    klíč je slovo a hodnota říká, kolikrát v textu je. Velikost písmen
#    nehraje roli.
#
#    Pak vypiš jen slova, která jsou ve zprávě víc než jednou.
#
#      kdo: 3
#      přinese: 2
#      a: 2

zprava = "Kdo přinese víno a kdo přinese dort a kdo přijde pozdě"


def spocitej_slova(text):
    pocty = {}
    for slovo in text.lower().split():
        if slovo in pocty:
            pocty[slovo] = pocty[slovo] + 1
        else:
            pocty[slovo] = 1
    return pocty


pocty = spocitej_slova(zprava)

for slovo, pocet in pocty.items():
    if pocet > 1:
        print(f"{slovo}: {pocet}")

# Podmínku ve funkci jde zkrátit metodou get:
#
#     pocty[slovo] = pocty.get(slovo, 0) + 1
#
# Pro prázdný text vrátí funkce prázdný slovník:
#
#     print(spocitej_slova(""))       # {}
