# ---------------------------------------------
#  Seznam se dá měnit
# ---------------------------------------------
# Spusť soubor. Na konci schválně spadne – tu chybu si přečti.

hoste = ["Anna", "Petra", "Jana"]


# Petra poslala místo sebe sestru. Položku nahradíš tak, že do jejího
# indexu přiřadíš novou hodnotu:
hoste[1] = "Marie"
print(hoste)        # ['Anna', 'Marie', 'Jana']


# Eva se ozvala, že taky přijde. Metoda append přidá položku na konec:
hoste.append("Eva")
print(hoste)        # ['Anna', 'Marie', 'Jana', 'Eva']


# Metody řetězců z lekce 6 vracely nový text. Metoda append mění rovnou
# seznam, který už máš, proto ji není potřeba nikam ukládat.


# Text změnit nejde. Tuhle chybu znáš z lekce 6:
jmeno = "Petra"
jmeno[0] = "M"      # TypeError: 'str' object does not support item assignment
