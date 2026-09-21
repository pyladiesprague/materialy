# Řešení bonusu 2 – Opakování
# Tvoje řešení může vypadat jinak, a to je v pořádku.

# Uživatel zadá číslo N. Vypiš z hvězdiček trojúhelník vysoký N –
#     první řádek "*", druhý "**", ... N-tý má N hvězdiček.
#     (Nápověda: text se dá opakovat: "*" * 3 je "***")

n = int(input("Zadej N: "))
for radek in range(1, n + 1):
    print("*" * radek)
