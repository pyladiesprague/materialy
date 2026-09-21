# Řešení cvičení 2 – And, or a not
# Tvoje řešení může vypadat jinak, a to je v pořádku.

# Přestupný rok. Rok je přestupný, když je dělitelný čtyřmi,
#    ale ne stovkou – NEBO když je dělitelný čtyřmi sty.
#    Zeptej se na rok a vypiš "Přestupný." / "Nepřestupný.".
#    (Vyzkoušej 2024, 1900, 2000.)

rok = int(input("Zadej rok: "))
if (rok % 4 == 0 and rok % 100 != 0) or rok % 400 == 0:
    print("Přestupný.")
else:
    print("Nepřestupný.")
