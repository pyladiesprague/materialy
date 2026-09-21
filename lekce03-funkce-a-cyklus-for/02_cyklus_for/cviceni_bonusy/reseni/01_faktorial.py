# Řešení bonusu 1 – Cyklus for
# Tvoje řešení může vypadat jinak, a to je v pořádku.

# Uživatel zadá číslo N. Spočítej cyklem jeho faktoriál –
#     tedy 1 * 2 * 3 * ... * N – a výsledek vypiš.
#     (Faktoriál z 5 je 120.)

n = int(input("Zadej číslo: "))
faktorial = 1
for cislo in range(1, n + 1):     # +1, aby se počítalo i samotné N
    faktorial = faktorial * cislo
print(faktorial)                  # pro 5 vypíše 120
