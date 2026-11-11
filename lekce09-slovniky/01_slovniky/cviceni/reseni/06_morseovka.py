# Řešení cvičení 6 – Slovníky
# Tvoje řešení může vypadat jinak, a to je v pořádku.

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


def do_morseovky(text):
    znacky = []
    for znak in text.lower():
        if znak == " ":
            znacky.append("/")
        elif znak in MORSE:
            znacky.append(MORSE[znak])
        else:
            znacky.append("?")
    return " ".join(znacky)


text = input("Text: ").strip()
print(do_morseovky(text))

# Poslední dvě větve jde zkrátit metodou get:
#
#     else:
#         znacky.append(MORSE.get(znak, "?"))
