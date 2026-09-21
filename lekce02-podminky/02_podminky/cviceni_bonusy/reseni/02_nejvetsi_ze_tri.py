# Řešení bonusu 2 – Podmínky
# Tvoje řešení může vypadat jinak, a to je v pořádku.

# Největší ze tří.
#     Máš tři čísla. Zjisti a vypiš to největší z nich.
#     Zatím bez and/or – poradíme si vnořenými if.

a = 12
b = 25
c = 8
if a >= b:
    if a >= c:
        print(a)
    else:
        print(c)
else:
    if b >= c:
        print(b)
    else:
        print(c)
