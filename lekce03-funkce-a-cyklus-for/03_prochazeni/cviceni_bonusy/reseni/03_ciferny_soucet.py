# Řešení bonusu 3 – Procházení textu
# Tvoje řešení může vypadat jinak, a to je v pořádku.

# Ciferný součet. Uživatel zadá číslo. Sečti jeho jednotlivé číslice
#     a součet vypiš (třeba z 253 vyjde 2 + 5 + 3 = 10).

cislo = input("Zadej číslo: ")           # necháme jako text, ať projdeme číslice
soucet = 0
for znak in cislo:
    soucet = soucet + int(znak)          # každou číslici převedeme na číslo
print("Ciferný součet:", soucet)
