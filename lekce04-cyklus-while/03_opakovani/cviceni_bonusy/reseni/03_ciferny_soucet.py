# Řešení bonusu 3 – Opakování
# Tvoje řešení může vypadat jinak, a to je v pořádku.

# Uživatel zadá celé číslo. Sečti jeho číslice a součet vypiš.
#     Například z 253 vyjde 10, protože 2 + 5 + 3 = 10.
#     (Nápověda: cislo % 10 dá poslední číslici, cislo // 10 ji utrhne.)
#     Zkus i záporné číslo. Aby to fungovalo, hodí se abs(cislo) –
#     ta funkce zahodí minus.
#     Postupně utrháváme poslední číslici, dokud něco zbývá.

cislo = int(input("Zadej celé číslo: "))
cislo = abs(cislo)                   # u záporného čísla zahodíme minus
soucet = 0
while cislo > 0:
    soucet = soucet + cislo % 10     # poslední číslice
    cislo = cislo // 10              # utrhneme ji
print("Součet číslic je", soucet)
