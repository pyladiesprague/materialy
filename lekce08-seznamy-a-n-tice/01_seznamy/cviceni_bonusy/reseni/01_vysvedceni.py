# Řešení bonusu 1 – Seznamy
# Tvoje řešení může vypadat jinak, a to je v pořádku.

# Napiš funkci vyhodnot_vysvedceni, která má na vstupu seznam známek
#    a vrátí text:
#
#      "bez známek"             když je seznam prázdný
#      "neprospěl/a"            když je mezi známkami pětka
#      "s vyznamenáním"         když je průměr nejvýš 1.5 a žádná známka
#                               není horší než 2
#      "prospěl/a"              jinak
#
#    Vyzkoušej ji na seznamech [1, 2, 1], [1, 3, 2], [1, 5, 1] a [].


def vyhodnot_vysvedceni(znamky):
    if len(znamky) == 0:
        return "bez známek"

    prumer = sum(znamky) / len(znamky)

    if 5 in znamky:
        return "neprospěl/a"
    if prumer <= 1.5 and max(znamky) <= 2:
        return "s vyznamenáním"
    return "prospěl/a"


print(vyhodnot_vysvedceni([1, 2, 1]))       # s vyznamenáním
print(vyhodnot_vysvedceni([1, 3, 2]))       # prospěl/a
print(vyhodnot_vysvedceni([1, 5, 1]))       # neprospěl/a
print(vyhodnot_vysvedceni([]))              # bez známek

# Kontrola prázdného seznamu musí být první. Jinak by funkce spadla
# na dělení nulou dřív, než by se k ní dostala.
