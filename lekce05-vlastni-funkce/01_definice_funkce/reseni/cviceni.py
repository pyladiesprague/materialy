# ---------------------------------------------
#  Řešení – vlastní funkce
# ---------------------------------------------


# 1) Funkce oddelovac() vypíše řádek z 30 hvězdiček.
def oddelovac():
    print("*" * 30)


oddelovac()
oddelovac()
oddelovac()


# 2) Funkce ramecek(text) vypíše text mezi dvěma řádky hvězdiček.
def ramecek(text):
    print("*" * 30)
    print(text)
    print("*" * 30)


ramecek("Vítej v kurzu!")
ramecek("Dneska nás čekají funkce.")


# 3) Funkce ohodnot_znamku(znamka).
def ohodnot_znamku(znamka):
    if znamka == 1:
        print("Výborně")
    elif znamka == 2:
        print("Chvalitebně")
    elif znamka == 3:
        print("Dobře")
    else:
        print("Ještě zabereme")


ohodnot_znamku(1)
ohodnot_znamku(3)
ohodnot_znamku(5)


# 4) Funkce odpocet(od) odpočítá dolů k 1.
#    Počet opakování známe, jakmile funkci zavoláme -> for.
#    range(od, 0, -1) začne na od a jde po jedné dolů. Druhé číslo se
#    do range nepočítá, takže poslední vypsané je 1.
def odpocet(od):
    for cislo in range(od, 0, -1):
        print(cislo)
    print("Teď!")


odpocet(3)
odpocet(5)


# 5) Volání funkce z úkolu 3 v cyklu.
for znamka in range(1, 6):
    ohodnot_znamku(znamka)
