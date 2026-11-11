# Řešení bonusu 1 – Slovníky
# Tvoje řešení může vypadat jinak, a to je v pořádku.

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


def body_za_slovo(slovo):
    soucet = 0
    for pismeno in slovo.lower():
        soucet = soucet + BODY.get(pismeno, 0)
    return soucet


prvni = input("První slovo: ")
druhe = input("Druhé slovo: ")

body_prvni = body_za_slovo(prvni)
body_druhe = body_za_slovo(druhe)

print(f"{prvni}: {body_prvni} b.")
print(f"{druhe}: {body_druhe} b.")

if body_prvni > body_druhe:
    print(f"Vyhrává {prvni}.")
elif body_druhe > body_prvni:
    print(f"Vyhrává {druhe}.")
else:
    print("Remíza.")
