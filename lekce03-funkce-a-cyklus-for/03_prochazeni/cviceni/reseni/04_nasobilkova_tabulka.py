# Řešení cvičení 4 – Procházení textu
# Tvoje řešení může vypadat jinak, a to je v pořádku.

# Násobilková tabulka. Pomocí vnořených cyklů vypiš tabulku 4x4,
#    kde na řádku R a sloupci S je jejich součin:
#        1 2 3 4
#        2 4 6 8
#        3 6 9 12
#        4 8 12 16
#    Jak pojmenuješ obě proměnné cyklu? Zamysli se, ať dávají smysl.

for radek in range(1, 5):
    for sloupec in range(1, 5):
        print(radek * sloupec, end=" ")
    print()                             # po každém řádku skoč na nový řádek
