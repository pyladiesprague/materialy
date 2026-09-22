# ---------------------------------------------
#  Parametry
# ---------------------------------------------
# Spusť soubor a sleduj, co se vypíše.
#
# V minulém souboru byla hranice 8 napevno v těle funkce. Když si ji
# chceme vybrat až při volání, přidáme druhý parametr:

def zkontroluj_heslo(heslo, min_delka):
    if len(heslo) < min_delka:
        print(heslo, "– moc krátké")
    else:
        print(heslo, "– dost dlouhé")


zkontroluj_heslo("pyladies", 8)
zkontroluj_heslo("pyladies", 20)


# Parametry jsou jména v definici: heslo, min_delka.
# Argumenty jsou hodnoty, které pošleš při volání: "pyladies", 8.


# Záleží na pořadí. Tenhle řádek skončí chybou TypeError, protože
# do heslo se dostane číslo 8 a do min_delka text "pyladies":
#
# zkontroluj_heslo(8, "pyladies")


# Parametrů může být kolik potřebuješ. Jenom je odděl čárkou:
def vypis_ucastnici(jmeno, mesto, vek):
    print(jmeno, "z", mesto, "-", vek, "let")


vypis_ucastnici("Anna", "Prahy", 30)
vypis_ucastnici("Petra", "Brna", 25)
