# ---------------------------------------------
#  Funkce volá funkci
# ---------------------------------------------
# Spusť soubor a zkus se zaregistrovat.
#
# V těle funkce můžeš volat další funkce – klidně i ty svoje.
# Poskládáme dohromady tři, které už z téhle lekce znáš.

def ramecek(text):
    print("*" * 30)
    print(text)
    print("*" * 30)


def je_heslo_dost_dlouhe(heslo):
    return len(heslo) >= 8


def zaregistruj(jmeno, heslo):
    if je_heslo_dost_dlouhe(heslo):
        ramecek("Vítej, " + jmeno)
    else:
        print("Heslo je moc krátké, zkus jiné.")


zaregistruj("Anna", "kolo")
zaregistruj("Petra", "pyladies2026")


# Každá funkce má na starosti jednu věc: ramecek vypisuje,
# je_heslo_dost_dlouhe rozhoduje a zaregistruj obojí řídí.
# Až budeš chtít jiný rámeček, opravíš ho na jednom místě
# a změní se všude, kde se volá.


jmeno = input("Jméno: ")
heslo = input("Heslo: ")
zaregistruj(jmeno, heslo)
