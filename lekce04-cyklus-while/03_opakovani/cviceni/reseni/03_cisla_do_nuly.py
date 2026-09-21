# Řešení cvičení 3 – Opakování
# Tvoje řešení může vypadat jinak, a to je v pořádku.

# Uživatel zadává čísla tak dlouho, dokud nezadá 0. Nakonec vypiš
#    jejich součet, kolik jich bylo a jejich průměr zaokrouhlený
#    na jedno desetinné místo. (Nápověda: round(cislo, 1))

soucet = 0
pocet = 0
cislo = int(input("Zadej číslo (0 = konec): "))
while cislo != 0:
    soucet = soucet + cislo
    pocet = pocet + 1
    cislo = int(input("Zadej číslo (0 = konec): "))

if pocet == 0:
    print("Nezadala jsi žádné číslo.")
else:
    print("Součet:", soucet)
    print("Počet:", pocet)
    print("Průměr:", round(soucet / pocet, 1))
