# Řešení cvičení 5 – Procházení textu
# Tvoje řešení může vypadat jinak, a to je v pořádku.

# Hody dvěma kostkami. Vnořenými cykly vypiš všechny možné hody
#    dvěma kostkami (každá má čísla 1 až 6) a u každého i jejich součet.
#    Každý řádek bude vypadat třeba takhle: 2 + 5 = 7

for kostka1 in range(1, 7):
    for kostka2 in range(1, 7):
        print(kostka1, "+", kostka2, "=", kostka1 + kostka2)
