# Řešení cvičení 3 – Procházení textu
# Tvoje řešení může vypadat jinak, a to je v pořádku.

# Statistika čísel. Uživatel zadá, kolik čísel bude zadávat, a pak
#    ta čísla postupně napíše. V jednom průchodu cyklem spočítej a vypiš
#    jejich součet, průměr, největší a nejmenší číslo.
#    Nepoužívej funkce sum, max ani min – spočítej vše sama cyklem.

pocet = int(input("Kolik čísel zadáš? "))
prvni = int(input("Zadej číslo: "))
soucet = prvni
nejvetsi = prvni                        # první číslo je zatím největší i nejmenší
nejmensi = prvni
for i in range(pocet - 1):              # první už máme, zbývá o jedno míň
    cislo = int(input("Zadej číslo: "))
    soucet = soucet + cislo
    if cislo > nejvetsi:
        nejvetsi = cislo
    if cislo < nejmensi:
        nejmensi = cislo
print("Součet:", soucet)
print("Průměr:", soucet / pocet)
print("Největší:", nejvetsi)
print("Nejmenší:", nejmensi)
