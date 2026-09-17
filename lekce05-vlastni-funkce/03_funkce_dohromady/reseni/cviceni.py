# ---------------------------------------------
#  Řešení – funkce dohromady
# ---------------------------------------------
from random import randrange


# 1) Nadpis s podtržením.
def nadpis(text):
    print(text)
    print("-" * len(text))


nadpis("Lekce 5")
nadpis("Vlastní funkce a návratové hodnoty")


# 2) Sudá čísla od 1 do 20.
def je_sude(cislo):
    return cislo % 2 == 0


for cislo in range(1, 21):
    if je_sude(cislo):
        print(cislo)


# 3) Součet čísel od 1 do n.
def soucet_do(n):
    soucet = 0
    for cislo in range(1, n + 1):
        soucet = soucet + cislo
    return soucet


print("Součet do 5:", soucet_do(5))


# 4) Slovo aspoň o třech písmenech, poslané rovnou do nadpisu.
def zeptej_se_na_slovo():
    slovo = input("Zadej slovo (aspoň 3 písmena): ")
    while len(slovo) < 3:
        print("Moc krátké.")
        slovo = input("Zadej slovo (aspoň 3 písmena): ")
    return slovo


nadpis(zeptej_se_na_slovo())


# 5) Nabídka, kde každá volba je funkce.
def zobraz_menu():
    print("1 - hodit kostkou")
    print("2 - pozdravit")
    print("3 - konec")


def hod_kostkou():
    print("Padlo:", randrange(1, 7))


def pozdrav(jmeno):
    print("Ahoj,", jmeno)


while True:
    zobraz_menu()
    volba = input("Co chceš dělat? ")
    if volba == "1":
        hod_kostkou()
    elif volba == "2":
        jmeno = input("Koho pozdravit? ")
        pozdrav(jmeno)
    elif volba == "3":
        break
    else:
        print("Takovou volbu neznám.")
print("Nashledanou!")
