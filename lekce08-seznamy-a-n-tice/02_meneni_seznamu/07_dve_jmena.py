# ---------------------------------------------
#  Dvě jména pro jeden seznam
# ---------------------------------------------
# Spusť soubor a porovnej výsledky.

# Chceš poslat kopii seznamu hostů do cateringu. Přiřazení ale seznam
# nezkopíruje. Obě proměnné pak ukazují na stejný seznam:
#
#        hoste    ──╮
#                   ├──▶  ["Anna", "Petra"]
#        catering ──╯

hoste = ["Anna", "Petra"]
catering = hoste

catering.append("Šéfkuchař")

print(catering)     # ['Anna', 'Petra', 'Šéfkuchař']
print(hoste)        # ['Anna', 'Petra', 'Šéfkuchař']


# Samostatný seznam dostaneš metodou copy:
#
#        hoste    ──▶  ["Anna", "Petra"]
#        catering ──▶  ["Anna", "Petra"]
#
# (Oba případy pod sebou ukazuje obrázek dve_jmena.png.)

hoste = ["Anna", "Petra"]
catering = hoste.copy()

catering.append("Šéfkuchař")

print(catering)     # ['Anna', 'Petra', 'Šéfkuchař']
print(hoste)        # ['Anna', 'Petra']


# Stejně je to u funkcí. Funkce dostane ten samý seznam, a když ho změní,
# je to vidět i venku:
def pozvi_evu(seznam):
    seznam.append("Eva")


pozvi_evu(hoste)
print(hoste)        # ['Anna', 'Petra', 'Eva']


# Výřez z první sekce taky vrací nový seznam. Je samostatný stejně jako
# kopie, takže když ho změníš, původní seznam zůstane, jak byl:
hoste = ["Anna", "Petra", "Jana", "Eva"]
prvni_dva = hoste[:2]

prvni_dva.append("Šéfkuchař")

print(prvni_dva)    # ['Anna', 'Petra', 'Šéfkuchař']
print(hoste)        # ['Anna', 'Petra', 'Jana', 'Eva']
