# ---------------------------------------------
#  Výřez: víc znaků najednou
# ---------------------------------------------
# Spusť soubor a porovnej výsledky.

slovo = "PyLadies"


# U výřezu se stejná čísla čtou jinak. Ukazují na značky mezi znaky,
# tedy na místa, kde se text přestřihne:
#
#        ╭───┬───┬───┬───┬───┬───┬───┬───╮
#        │ P │ y │ L │ a │ d │ i │ e │ s │
#        ╰───┴───┴───┴───┴───┴───┴───┴───╯
#        0   1   2   3   4   5   6   7   8
#       -8  -7  -6  -5  -4  -3  -2  -1
#
# Výřez vezme všechno mezi dvěma značkami.


# Dvojtečka mezi dvěma indexy vybere část textu. Druhé číslo se do výřezu
# nepočítá – stejné pravidlo jako u range:
print(slovo[0:2])       # Py
print(slovo[2:8])       # Ladies


# Když první číslo chybí, bere se od začátku:
print(slovo[:2])        # Py

# Když chybí druhé, jede se až do konce:
print(slovo[2:])        # Ladies


# Záporné indexy fungují i tady. Poslední tři znaky a všechno kromě nich:
print(slovo[-3:])       # ies
print(slovo[:-3])       # PyLad


# Za druhou dvojtečkou se dá přidat krok – o kolik znaků se pokaždé
# posunout:
print(slovo[::2])       # PLde

# Krok -1 jde pozpátku a otočí celý text:
print(slovo[::-1])      # seidaLyP


# Původní text zůstává, jak byl – výřez je nový řetězec:
print(slovo)            # PyLadies
