# ---------------------------------------------
#  Hledání v seznamu a počítání s čísly
# ---------------------------------------------
# Spusť soubor a porovnej výsledky.

hoste = ["Anna", "Petra", "Jana"]


# Zápis in znáš z lekce 3 a 6, kde hledal písmeno v textu. Stejně
# zjistí, jestli je hodnota v seznamu, a vrátí True nebo False:
print("Petra" in hoste)             # True
print("Karel" in hoste)             # False

# Opačnou otázku položíš zápisem not in:
print("Karel" not in hoste)         # True

# Pozor, tohle in není to samé jako in v cyklu for. Ve for in prochází
# seznam po jedné položce, tady se jen ptá, jestli v něm hodnota je.

if "Anna" in hoste:
    print("Anna je pozvaná.")       # Anna je pozvaná.


# U řetězce in hledá i kus textu. U seznamu porovnává celé položky:
print("Pet" in "Petra")             # True
print("Pet" in hoste)               # False


# V lekci 6 sis u velikosti trička psala tři porovnání:
velikost = "M"

if velikost == "S" or velikost == "M" or velikost == "L":
    print("Tuhle velikost máme.")   # Tuhle velikost máme.

# Se seznamem stačí jedno:
if velikost in ["S", "M", "L"]:
    print("Tuhle velikost máme.")   # Tuhle velikost máme.


# Na seznam čísel fungují vestavěné funkce z lekce 3:
veky = [28, 34, 25, 41]

print(sum(veky))                    # 128
print(min(veky))                    # 25
print(max(veky))                    # 41


# Průměr je součet vydělený počtem:
prumer = sum(veky) / len(veky)
print(f"Průměrný věk: {prumer:.1f}")    # Průměrný věk: 32.0


# Metodu count znáš z řetězců. Spočítá, kolikrát v seznamu položka je:
napoje = ["víno", "džus", "víno", "pivo"]
print(napoje.count("víno"))         # 2
