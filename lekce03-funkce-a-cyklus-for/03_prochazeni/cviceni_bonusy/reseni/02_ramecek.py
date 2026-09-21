# Řešení bonusu 2 – Procházení textu
# Tvoje řešení může vypadat jinak, a to je v pořádku.

# Rámeček. Uživatel zadá velikost N. Vnořenými cykly nakresli
#     čtverec N x N, kde okraj tvoří X a vnitřek je prázdný. Pro N=4:
#         X X X X
#         X     X
#         X     X
#         X X X X
#     Zamysli se: na kterém řádku a sloupci se kreslí X a kdy mezera?

n = int(input("Jak velký rámeček? "))
for radek in range(n):
    for sloupec in range(n):
        if radek == 0 or radek == n - 1 or sloupec == 0 or sloupec == n - 1:
            print("X", end=" ")
        else:
            print(" ", end=" ")
    print()
