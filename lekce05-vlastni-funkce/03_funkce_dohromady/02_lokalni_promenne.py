# ---------------------------------------------
#  Proměnné uvnitř funkce
# ---------------------------------------------
# Spusť soubor. Na konci schválně spadne – tu chybu si přečti.
#
# Proměnná, která vznikne uvnitř funkce, patří jenom té funkci.
# Venku o ní Python neví.

def cena_s_dph(cena):
    print("Uvnitř funkce je cena:", cena)
    dan = cena * 0.21
    return cena + dan


# Parametr je na tom stejně. Tady je proměnná cena i venku,
# a přesto si funkce žije se svou vlastní:
cena = 500

print("Výsledek:", cena_s_dph(100))
print("Venku je cena:", cena)


# Kdyby to tak nebylo, každá funkce by nám přepisovala proměnné
# v celém programu a nikdo by se v tom nevyznal.


# A teď ta chyba. Proměnná dan vznikla uvnitř funkce cena_s_dph,
# takže tenhle řádek skončí hláškou NameError: name 'dan' is not defined
print(dan)
