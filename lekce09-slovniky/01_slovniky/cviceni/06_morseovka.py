# Cvičení 6 – Slovníky
# Doplň kód pod zadání a soubor spusť (Run).

# Napiš funkci do_morseovky, která má na vstupu text a vrátí ho
#    v Morseově abecedě:
#    - písmena oddělí mezerou,
#    - mezeru mezi slovy zapíše jako "/",
#    - znak, který ve slovníku není (třeba "č"), zapíše jako "?",
#    - velikost písmen nehraje roli.
#
#    Pak se zeptej na text a vypiš ho v morseovce.
#
#      Text: Ahoj Petro
#      .- .... --- .--- / .--. . - .-. ---

MORSE = {
    "a": ".-", "b": "-...", "c": "-.-.", "d": "-..", "e": ".",
    "f": "..-.", "g": "--.", "h": "....", "i": "..", "j": ".---",
    "k": "-.-", "l": ".-..", "m": "--", "n": "-.", "o": "---",
    "p": ".--.", "q": "--.-", "r": ".-.", "s": "...", "t": "-",
    "u": "..-", "v": "...-", "w": ".--", "x": "-..-", "y": "-.--",
    "z": "--..",
}
