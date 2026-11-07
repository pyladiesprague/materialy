# ---------------------------------------------
#  Rozbalování
# ---------------------------------------------
# Spusť soubor. Na konci schválně spadne – tu chybu si přečti.

anna = ("Anna", "dort")


# Hodnoty z n-tice můžeš uložit do proměnných najednou:
jmeno, darek = anna

print(jmeno)        # Anna
print(darek)        # dort


# Je to přehlednější než indexy, které si musíš pamatovat:
print(f"{anna[0]} přinese {anna[1]}.")      # Anna přinese dort.
print(f"{jmeno} přinese {darek}.")          # Anna přinese dort.


# Díky rozbalování prohodíš dvě proměnné na jednom řádku:
vlevo = "Anna"
vpravo = "Petra"
vlevo, vpravo = vpravo, vlevo

print(vlevo)        # Petra
print(vpravo)       # Anna


# Počet proměnných musí sedět s počtem hodnot:
jmeno, darek = ("Petra", "víno", 2)     # ValueError: too many values to unpack
