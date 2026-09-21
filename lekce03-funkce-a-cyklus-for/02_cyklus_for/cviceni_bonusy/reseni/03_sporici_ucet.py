# Řešení bonusu 3 – Cyklus for
# Tvoje řešení může vypadat jinak, a to je v pořádku.

# Uživatel zadá počáteční částku na spořicím účtu. Úrok je 5 % ročně.
#     Spočítej cyklem, kolik na účtu bude po deseti letech
#     (každý rok se částka vynásobí 1.05), a výsledek vypiš.

castka = int(input("Kolik si ukládáš? "))
for rok in range(10):
    castka = castka * 1.05
print(round(castka, 2))           # pro 1000 vypíše 1628.89
