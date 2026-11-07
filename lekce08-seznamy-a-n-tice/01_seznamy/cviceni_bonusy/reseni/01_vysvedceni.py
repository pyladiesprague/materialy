# Řešení bonusu 1 – Seznamy
# Tvoje řešení může vypadat jinak, a to je v pořádku.

# Napiš funkci vyhodnot_vysvedceni, která má na vstupu seznam známek
#    a vrátí text:
#
#      "neprospěl/a"            když je mezi známkami pětka
#      "s vyznamenáním"         když je průměr nejvýš 1.5 a žádná známka
#                               není horší než 2
#      "prospěl/a"              jinak
#
#    Vyzkoušej ji na seznamech [1, 2, 1], [1, 3, 2] a [1, 5, 1].


def vyhodnot_vysvedceni(znamky):
    prumer = sum(znamky) / len(znamky)

    if 5 in znamky:
        return "neprospěl/a"
    if prumer <= 1.5 and max(znamky) <= 2:
        return "s vyznamenáním"
    return "prospěl/a"


print(vyhodnot_vysvedceni([1, 2, 1]))       # s vyznamenáním
print(vyhodnot_vysvedceni([1, 3, 2]))       # prospěl/a
print(vyhodnot_vysvedceni([1, 5, 1]))       # neprospěl/a
