# ---------------------------------------------
#  Text se nedá přepsat
# ---------------------------------------------
# Spusť soubor. Na konci schválně spadne – tu chybu si přečti.

slovo = "palec"


# Index umí znak přečíst:
print(slovo[0])     # p


# Přepsat ho ale nejde. Řetězec v Pythonu jednou vznikne a od té chvíle
# se nemění – odborně se tomu říká neměnný. Když potřebuješ jiný,
# vyrobíš nový, třeba z výřezů:
novy = "v" + slovo[1:]
print(novy)         # valec

# Původní zůstal, jak byl:
print(slovo)        # palec

# Odtud taky to, co dělá upper() v předchozí složce: vrací nový
# řetězec, protože ten původní přepsat neumí.

# Řetězec není jediná věc, která se dá indexovat a krájet. V lekci 8
# potkáš seznamy – ty se chovají hodně podobně, jen se měnit dají.


# Tenhle řádek skončí chybou TypeError:
slovo[0] = "v"
