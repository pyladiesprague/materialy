# Cvičení 3 – Seznamy
# Oprav kód a soubor spusť (Run).

# Tuhle funkci znáš z hry v lekci 7. Přepiš ji tak, aby místo tří
#    porovnání používala seznam TAHY a zápis in.

KAMEN = "kamen"
NUZKY = "nuzky"
PAPIR = "papir"
TAHY = [KAMEN, NUZKY, PAPIR]


def je_platny(tah):
    return tah == KAMEN or tah == NUZKY or tah == PAPIR


print(je_platny("nuzky"))       # True
print(je_platny("pes"))         # False
