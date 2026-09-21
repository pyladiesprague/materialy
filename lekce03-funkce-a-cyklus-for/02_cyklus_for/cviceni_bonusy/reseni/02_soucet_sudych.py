# Řešení bonusu 2 – Cyklus for
# Tvoje řešení může vypadat jinak, a to je v pořádku.

# Spočítej cyklem součet všech sudých čísel od 1 do 100 a vypiš ho.

soucet = 0
for cislo in range(2, 101, 2):    # krok 2 = jen sudá čísla
    soucet = soucet + cislo
print(soucet)                     # 2550
