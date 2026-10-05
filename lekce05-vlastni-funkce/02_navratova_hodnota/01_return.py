# ---------------------------------------------
#  Návratová hodnota – return
# ---------------------------------------------
# Spusť soubor a sleduj, co se vypíše.
#
# Funkce z minulé složky uměla jenom vypsat, jak na tom heslo je:

def zkontroluj_heslo(heslo):
    if len(heslo) < 8:
        print(heslo, "– moc krátké")
    else:
        print(heslo, "– dost dlouhé")


zkontroluj_heslo("kolo")


# Výsledek se ale jenom vypíše a tím to končí. Program s ním dál nic
# neudělá – kdybychom chtěli krátké heslo odmítnout a dlouhé pustit dál,
# musí nám funkce tu informaci předat zpátky. Od toho je return:
def je_heslo_dost_dlouhe(heslo):
    return len(heslo) >= 8


# Funkce teď vrací True nebo False – hodnoty, které znáš z lekce 2.
# Můžeme si je uložit do proměnné:
vysledek = je_heslo_dost_dlouhe("kolo")
print("kolo:", vysledek)

vysledek = je_heslo_dost_dlouhe("pyladies2026")
print("pyladies2026:", vysledek)


# A hlavně se podle výsledku můžeme rozhodnout:
heslo = input("Zvol si heslo: ")
if je_heslo_dost_dlouhe(heslo):
    print("Heslo přijato.")
else:
    print("Moc krátké, zkus delší.")


# Volání funkce se chová jako hodnota, kterou funkce vrátila.
# Klidně ho můžeš rovnou dosadit do výpočtu:
def cena_s_dph(cena):
    return cena * 1.21


print("Celkem:", cena_s_dph(100) + cena_s_dph(250), "Kč")
