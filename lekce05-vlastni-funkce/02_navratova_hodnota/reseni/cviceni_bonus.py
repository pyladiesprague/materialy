# ---------------------------------------------
#  Řešení – bonusová cvičení: návratová hodnota
# ---------------------------------------------


# B1) Tři pokusy na PIN.
def zkontroluj_pin(spravny_pin):
    pokusy = 0
    while pokusy < 3:
        zadany = input("Zadej PIN: ")
        pokusy = pokusy + 1
        if zadany == spravny_pin:
            return True
        print("Špatný PIN.")
    return False


if zkontroluj_pin("1234"):
    print("Odemčeno.")
else:
    print("Karta zablokována.")


# B2) Ptá se na heslo, dokud není dost dlouhé, a vrátí ho.
def je_heslo_dost_dlouhe(heslo):
    return len(heslo) >= 8


def zeptej_se_na_heslo():
    heslo = input("Zvol si heslo: ")
    while not je_heslo_dost_dlouhe(heslo):
        print("Moc krátké, aspoň 8 znaků.")
        heslo = input("Zvol si heslo: ")
    return heslo


nove_heslo = zeptej_se_na_heslo()
print("Heslo nastaveno:", nove_heslo)


# B3) Kolikrát se písmeno objeví ve slově.
def spocitej_pismeno(slovo, pismeno):
    pocet = 0
    for znak in slovo:
        if znak == pismeno:
            pocet = pocet + 1
    return pocet


slovo = input("Zadej slovo: ")
pismeno = input("Které písmeno mám počítat? ")
print("Počet:", spocitej_pismeno(slovo, pismeno))
