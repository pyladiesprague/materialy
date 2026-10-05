# Řešení bonusu 3 – Návratová hodnota
# Tvoje řešení může vypadat jinak, a to je v pořádku.

# Napiš funkci spocitej_pismeno(slovo, pismeno), která vrátí,
#     kolikrát se písmeno ve slově objeví.
#     spocitej_pismeno("kolotoč", "o") vrátí 3.
#     Nechej si zadat slovo i písmeno od uživatele a výsledek vypiš.

def spocitej_pismeno(slovo, pismeno):
    pocet = 0
    for znak in slovo:
        if znak == pismeno:
            pocet = pocet + 1
    return pocet


slovo = input("Zadej slovo: ")
pismeno = input("Které písmeno mám počítat? ")
print("Počet:", spocitej_pismeno(slovo, pismeno))
