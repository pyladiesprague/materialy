# Řešení bonusu 2 – Vestavěné funkce
# Tvoje řešení může vypadat jinak, a to je v pořádku.

# Průměr od 1 do N. Uživatel zadá číslo N. Vypiš průměr všech čísel
#     od 1 do N (součet čísel vyděl jejich počtem).

n = int(input("Zadej N: "))
prumer = sum(range(1, n + 1)) / n       # +1, aby se počítalo i samotné N
print(prumer)                           # pro 10 vypíše 5.5
