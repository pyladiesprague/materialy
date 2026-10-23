# ---------------------------------------------
#  Hledání v textu
# ---------------------------------------------
# Spusť soubor a porovnej výsledky.

slovo = "PyLadies"


# Zápis in znáš z cyklů, kde hledal jedno písmeno. Zvládne i delší kus:
print("Ladies" in slovo)        # True
print("ladies" in slovo)        # False

# A opačná otázka, jestli tam něco není:
print("Gentlemen" not in slovo)     # True

# Velikost písmen rozhoduje. Když ti nemá vadit, pomůže lower()
# z minulé složky:
print("ladies" in slovo.lower())    # True


# Na začátek a konec textu jsou metody:
soubor = "prezentace.pdf"

print(soubor.endswith(".pdf"))      # True
print(soubor.startswith("prez"))    # True


# Hodí se to v podmínce:
if soubor.endswith(".pdf"):
    print("Tohle je PDF.")
