# Řešení bonusu 1 – Indexování a výřezy
# Tvoje řešení může vypadat jinak, a to je v pořádku.

# Vypiš číslo karty tak, aby byly vidět jen poslední čtyři číslice.
#    Zbytek nahraď hvězdičkami, ať jich je přesně tolik jako
#    skrytých číslic.

cislo = "4539112233447788"

print("*" * (len(cislo) - 4) + cislo[-4:])
