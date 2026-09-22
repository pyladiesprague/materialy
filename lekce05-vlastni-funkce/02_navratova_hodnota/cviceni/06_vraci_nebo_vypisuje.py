# Cvičení 6 – Návratová hodnota
# Oprav kód a soubor spusť (Run).

# V téhle funkci je chyba. Spusť soubor, přečti si hlášku a funkci
#    oprav. Zbytek programu nech tak, jak je.

def cena_s_dph(cena):
    print(cena * 1.21)


celkem = cena_s_dph(100) + cena_s_dph(250)
print("Dohromady:", celkem)
