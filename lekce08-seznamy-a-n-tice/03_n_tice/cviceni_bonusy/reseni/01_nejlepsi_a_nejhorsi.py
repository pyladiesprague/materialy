# Řešení bonusu 1 – N-tice
# Tvoje řešení může vypadat jinak, a to je v pořádku.

# Napiš funkci nejlepsi_a_nejhorsi, která má na vstupu seznam dvojic
#    (jméno, body). Vrátí jméno s nejvíc body a jméno s nejméně body.
#    Když je seznam prázdný, vrátí None, None.
#
#    Vyjít má:  Petra, Jana
#               None, None   (pro prázdný seznam)

vysledky = [("Anna", 12), ("Petra", 15), ("Jana", 9)]


def nejlepsi_a_nejhorsi(vysledky):
    if len(vysledky) == 0:
        return None, None

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

prvni, posledni = nejlepsi_a_nejhorsi([])
print(f"{prvni}, {posledni}")

# Kontrola prázdného seznamu musí být první. Jinak by vysledky[0]
# spadlo na IndexError, protože v prázdném seznamu žádná první položka
# není.
