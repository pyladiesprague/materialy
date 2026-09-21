# Řešení bonusu 3 – Podmínky
# Tvoje řešení může vypadat jinak, a to je v pořádku.

# Bum-Bác pro jedno číslo.
#     Zeptej se na číslo a vypiš:
#       - "BumBác", když je dělitelné třemi i pěti zároveň,
#       - "Bum", když je dělitelné jen třemi,
#       - "Bác", když je dělitelné jen pěti,
#       - jinak samotné číslo.
#     Dělitelnost třemi i pěti = dělitelnost patnácti. Musí se testovat
#     jako první – jinak by číslo spadlo hned do větve "Bum" nebo "Bác"
#     a na "BumBác" by nikdy nedošlo.

cislo = int(input("Zadej číslo: "))
if cislo % 15 == 0:
    print("BumBác")
elif cislo % 3 == 0:
    print("Bum")
elif cislo % 5 == 0:
    print("Bác")
else:
    print(cislo)
