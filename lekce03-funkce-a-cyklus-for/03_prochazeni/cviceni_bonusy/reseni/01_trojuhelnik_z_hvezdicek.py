# Řešení bonusu 1 – Procházení textu
# Tvoje řešení může vypadat jinak, a to je v pořádku.

# Trojúhelník z hvězdiček. Uživatel zadá výšku a ty vypiš
#     trojúhelník, kde první řádek má jednu hvězdičku, druhý dvě atd.:
#     *
#     **
#     ***

vyska = int(input("Jak vysoký trojúhelník? "))
for radek in range(1, vyska + 1):
    print("*" * radek)                   # "*" * 3 je "***"
