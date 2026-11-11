# Bonus 1 – Slovníky
# Doplň kód pod zadání a soubor spusť (Run).

# V naší verzi Scrabblu má každé písmeno svoji hodnotu. Napiš funkci
#    body_za_slovo, která má na vstupu slovo a vrátí součet bodů za jeho
#    písmena.
#    Písmena, která ve slovníku nejsou, mají 0 bodů.
#
#    Pak se zeptej na dvě slova a vypiš, které má víc bodů.
#
#      První slovo: pes
#      Druhé slovo: kočka
#      pes: 3 b.
#      kočka: 8 b.
#      Vyhrává kočka.

BODY = {
    "a": 1, "e": 1, "i": 1, "o": 1, "n": 1, "s": 1, "t": 1, "v": 1,
    "d": 1, "k": 1, "l": 1, "p": 1, "r": 1, "m": 2, "u": 2, "y": 2,
    "b": 3, "c": 3, "j": 2, "z": 2, "h": 2, "č": 4, "ž": 4, "š": 4,
    "f": 5, "g": 5, "x": 10,
}
