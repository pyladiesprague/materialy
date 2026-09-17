# ---------------------------------------------
#  Řešení – bonusová cvičení: vlastní funkce
# ---------------------------------------------
from random import randrange


# B1) Obdélník z hvězdiček.
def obdelnik(sirka, vyska):
    for radek in range(vyska):
        print("*" * sirka)


obdelnik(5, 3)


# B2) Řádek účtenky.
def ucet(cena, pocet):
    print(pocet, "x", cena, "Kč =", cena * pocet, "Kč")


ucet(25, 4)
ucet(199, 2)


# B3) Hod kostkou pětkrát za sebou.
def hod_kostkou():
    hod = randrange(1, 7)
    print("Padlo:", hod)


for pokus in range(5):
    hod_kostkou()
