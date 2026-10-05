# ---------------------------------------------
#  Funkce bez parametru
# ---------------------------------------------
# Spusť soubor víckrát – pokaždé to dopadne jinak.
#
# Někdy funkce nic zvenku nepotřebuje. Závorky pak zůstanou prázdné –
# v definici i při volání.

from random import randrange


def hod_minci():
    if randrange(1, 3) == 1:
        print("Panna")
    else:
        print("Orel")


hod_minci()
hod_minci()
hod_minci()