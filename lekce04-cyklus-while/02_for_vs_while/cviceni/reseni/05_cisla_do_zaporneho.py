# Řešení cvičení 5 – For versus while
# Tvoje řešení může vypadat jinak, a to je v pořádku.

# Načítej od uživatele čísla tak dlouho, dokud nezadá záporné číslo.
#    Pak vypiš, kolik čísel stihl zadat.
#    Kolik čísel zadá dopředu nevíme -> while.
kolik = 0
cislo = int(input("Zadej číslo: "))
while cislo >= 0:
    kolik = kolik + 1
    cislo = int(input("Zadej číslo: "))
print("Počet zadaných čísel před tím záporným:", kolik)
