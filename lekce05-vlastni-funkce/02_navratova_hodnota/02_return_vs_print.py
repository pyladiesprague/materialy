# ---------------------------------------------
#  return vs. print
# ---------------------------------------------
# Spusť soubor a sleduj, co se vypíše.
#
# Tyhle dvě funkce vypadají na první pohled skoro stejně:

def vypis_dph(cena):
    print(cena * 1.21)


def spocitej_dph(cena):
    return cena * 1.21


# Když je zavoláš, obě ukážou to samé číslo:
vypis_dph(100)
print(spocitej_dph(100))


# Rozdíl je vidět, až když si výsledek zkusíš uložit:
vysledek_vypisu = vypis_dph(100)
vysledek_vypoctu = spocitej_dph(100)
print("z vypis_dph:", vysledek_vypisu)
print("ze spocitej_dph:", vysledek_vypoctu)


# Proměnná vysledek_vypisu je None. Funkce vypis_dph číslo vypsala,
# ale ven nic nepředala – a když funkce nemá return, vrací Python
# právě None (tedy „nic"). S None se dál počítat nedá:
#
# print(vysledek_vypisu + 50)     # TypeError


# Proto se funkce většinou píšou tak, že spočítají a vrátí,
# a vypisování nechají na tom, kdo je volá:
print("Cena s DPH:", spocitej_dph(100), "Kč")
print("Dohromady:", spocitej_dph(100) + spocitej_dph(250), "Kč")
