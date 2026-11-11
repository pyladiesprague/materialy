# ---------------------------------------------
#  Index a výřez: jako u řetězců
# ---------------------------------------------
# Spusť soubor. Na konci schválně spadne – tu chybu si přečti.

hoste = ["Anna", "Petra", "Jana", "Eva", "Marie", "Lucie"]


# Index a výřez fungují stejně jako u řetězců z lekce 6. Index počítá
# od nuly, záporný index od konce:
#
# (Index i výřez v seznamu ukazuje obrázek seznam_index_a_vyrez.png.)

print(hoste[0])         # Anna
print(hoste[2])         # Jana
print(hoste[-1])        # Lucie


# Výřez vrátí nový seznam. Číslo před dvojtečkou se do něj počítá,
# číslo za dvojtečkou už ne:
prvni_dva = hoste[0:2]
print(prvni_dva)        # ['Anna', 'Petra']

# Původní seznam přitom zůstane celý:
print(hoste)    # ['Anna', 'Petra', 'Jana', 'Eva', 'Marie', 'Lucie']

# Začátek a konec můžeš vynechat. Fungují i záporná čísla:
print(hoste[:2])        # ['Anna', 'Petra']
print(hoste[4:])        # ['Marie', 'Lucie']
print(hoste[-2:])       # ['Marie', 'Lucie']


# Index je hodnota jako každá jiná, takže ho můžeš uložit do proměnné:
posledni = len(hoste) - 1
print(hoste[posledni])  # Lucie


# Šest hostů má indexy 0 až 5. Index 6 už v seznamu není:
print(hoste[6])         # IndexError: list index out of range
