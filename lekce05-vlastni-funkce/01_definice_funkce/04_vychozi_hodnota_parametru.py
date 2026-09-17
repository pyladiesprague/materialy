# ---------------------------------------------
#  Výchozí hodnota parametru
# ---------------------------------------------
# Spusť soubor a sleduj, co se vypíše.
#
# round(3.14159, 2) zaokrouhlí na dvě desetinná místa, round(3.14159)
# na celé číslo. Druhý parametr se dá vynechat, protože má připravenou
# výchozí hodnotu. Ve vlastní funkci se zapisuje rovnítkem v definici:

def zkontroluj_heslo(heslo, min_delka=8):
    if len(heslo) < min_delka:
        print(heslo, "– moc krátké")
    else:
        print(heslo, "– dost dlouhé")


zkontroluj_heslo("pyladies")          # min_delka zůstane 8
zkontroluj_heslo("pyladies", 20)      # 20 přebije výchozí hodnotu


# Hodí se to tam, kde skoro vždycky platí jedna hodnota a jenom občas
# potřebuješ jinou:
def pozdrav(jmeno, osloveni="Ahoj"):
    print(osloveni + ",", jmeno)


pozdrav("Anno")
pozdrav("Anno", "Dobrý den")


# Parametry s výchozí hodnotou patří až za ty bez ní.
# Tahle definice by skončila chybou SyntaxError:
#
# def zkontroluj_heslo(min_delka=8, heslo):
