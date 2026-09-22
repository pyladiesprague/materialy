# Řešení cvičení 5 – Funkce dohromady
# Tvoje řešení může vypadat jinak, a to je v pořádku.

from random import randrange

# Napiš program s nabídkou: hodit kostkou, pozdravit, konec.
#    V cyklu while True nabídku zobraz, zeptej se na volbu a podle ní
#    zavolej funkci. Po volbě "konec" cyklus ukonči.
#    Každá volba i samotné zobrazení nabídky ať je vlastní funkce.

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
