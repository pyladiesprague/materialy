# Řešení bonusu 1 – N-tice
# Tvoje řešení může vypadat jinak, a to je v pořádku.

# Napiš funkci nejlepsi_a_nejhorsi, která má na vstupu seznam dvojic
#    (jméno, body). Vrátí jméno s nejvíc body a jméno s nejméně body.
#
#    Vyjít má:  Petra, Jana

vysledky = [("Anna", 12), ("Petra", 15), ("Jana", 9)]

def nejlepsi_a_nejhorsi(vysledky):
    nejlepsi, nejvic = vysledky[0]
    nejhorsi, nejmene = vysledky[0]

    for jmeno, body in vysledky:
        if body > nejvic:
            nejlepsi, nejvic = jmeno, body
        if body < nejmene:
            nejhorsi, nejmene = jmeno, body

    return nejlepsi, nejhorsi


prvni, posledni = nejlepsi_a_nejhorsi(vysledky)
print(f"{prvni}, {posledni}")
