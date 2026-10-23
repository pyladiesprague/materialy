# Řešení cvičení 3 – Indexování a výřezy
# Tvoje řešení může vypadat jinak, a to je v pořádku.

# V proměnné datum je text ve tvaru rok-měsíc-den. Vypiš ho česky,
#    tedy ve tvaru:  17. 10. 2026

datum = "2026-10-17"

rok = datum[:4]
mesic = datum[5:7]
den = datum[8:10]

print(f"{den}. {mesic}. {rok}")

# Pomlčky jsou na indexech 4 a 7, proto ty mezery v číslech.
