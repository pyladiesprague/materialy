# Řešení cvičení 4 – Cyklus while
# Tvoje řešení může vypadat jinak, a to je v pořádku.

# Uživatel postupně zadává čísla. Sčítej je. Jakmile zadá 0,
#    přestaň se ptát a vypiš celkový součet.

soucet = 0
cislo = int(input("Zadej číslo (0 = konec): "))
while cislo != 0:
    soucet = soucet + cislo
    cislo = int(input("Zadej číslo (0 = konec): "))
print("Součet je", soucet)
