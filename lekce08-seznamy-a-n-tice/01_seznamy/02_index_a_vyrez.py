# ---------------------------------------------
#  Index a výřez: jako u řetězců
# ---------------------------------------------
# Spusť soubor. Na konci schválně spadne – tu chybu si přečti.

hoste = ["Anna", "Petra", "Jana", "Eva"]


# Index a výřez fungují stejně jako u řetězců z lekce 6. Index počítá
# od nuly, záporný index od konce:
print(hoste[0])         # Anna
print(hoste[2])         # Jana
print(hoste[-1])        # Eva


# Výřez vrátí nový seznam. Číslo před dvojtečkou se do něj počítá,
# číslo za dvojtečkou už ne:
prvni_dva = hoste[0:2]
print(prvni_dva)        # ['Anna', 'Petra']

# Původní seznam přitom zůstane celý:
print(hoste)            # ['Anna', 'Petra', 'Jana', 'Eva']

# Začátek a konec můžeš vynechat:
print(hoste[:2])        # ['Anna', 'Petra']
print(hoste[2:])        # ['Jana', 'Eva']


# Index je hodnota jako každá jiná, takže ho můžeš uložit do proměnné:
posledni = len(hoste) - 1
print(hoste[posledni])  # Eva


# Čtyři hosté mají indexy 0 až 3. Index 4 už v seznamu není:
print(hoste[4])         # IndexError: list index out of range
