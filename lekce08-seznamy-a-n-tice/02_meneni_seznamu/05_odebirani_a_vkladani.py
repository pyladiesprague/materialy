# ---------------------------------------------
#  Odebírání a vkládání
# ---------------------------------------------
# Spusť soubor. Na konci schválně spadne – tu chybu si přečti.

hoste = ["Anna", "Petra", "Jana", "Eva"]


# Jana se omluvila. Metoda remove odebere položku podle hodnoty:
hoste.remove("Jana")
print(hoste)        # ['Anna', 'Petra', 'Eva']


# Hosté přicházejí ke dveřím. Metoda pop odebere položku podle indexu
# a vrátí ji. Bez indexu vezme poslední:
prvni = hoste.pop(0)
print(prvni)        # Anna
print(hoste)        # ['Petra', 'Eva']

posledni = hoste.pop()
print(posledni)     # Eva
print(hoste)        # ['Petra']


# Metoda insert vloží položku na daný index. Ostatní se posunou:
hoste.insert(0, "Marie")
print(hoste)        # ['Marie', 'Petra']


# Když hodnota v seznamu není, remove spadne:
hoste.remove("Karel")       # ValueError: list.remove(x): x not in list
