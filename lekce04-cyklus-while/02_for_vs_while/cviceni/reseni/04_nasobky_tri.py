# Řešení cvičení 4 – For versus while
# Tvoje řešení může vypadat jinak, a to je v pořádku.

# Vypiš prvních deset násobků čísla 3 (3, 6, 9, ... 30).
#    Deset opakování, počet známe -> for.
for cislo in range(3, 31, 3):
    print(cislo)

# Jde to i bez kroku – vynásobit si to v cyklu sama:
for cislo in range(1, 11):
    print(cislo * 3)
