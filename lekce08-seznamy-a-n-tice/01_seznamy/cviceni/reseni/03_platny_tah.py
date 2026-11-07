# Řešení cvičení 3 – Seznamy
# Tvoje řešení může vypadat jinak, a to je v pořádku.

# Tuhle funkci znáš z hry v lekci 7. Přepiš ji tak, aby místo tří
#    porovnání používala seznam TAHY a zápis in.

KAMEN = "kamen"
NUZKY = "nuzky"
PAPIR = "papir"
TAHY = [KAMEN, NUZKY, PAPIR]


def je_platny(tah):
    return tah in TAHY


print(je_platny("nuzky"))       # True
print(je_platny("pes"))         # False
