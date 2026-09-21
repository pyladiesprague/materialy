# Řešení cvičení 5 – Cyklus for
# Tvoje řešení může vypadat jinak, a to je v pořádku.

# Uživatel zadá číslo. Cyklem vypiš jeho malou násobilku –
#    tedy cislo * 1 až cislo * 10, každý řádek třeba "7 * 3 = 21".

cislo = int(input("Zadej číslo: "))
for nasobek in range(1, 11):
    print(cislo, "*", nasobek, "=", cislo * nasobek)
