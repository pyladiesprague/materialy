# ---------------------------------------------
#  Stavíme slovník v cyklu
# ---------------------------------------------
# Spusť soubor a porovnej výsledky.

# Slovník může být prázdný. Píše se jako prázdné složené závorky:
hlasy = {}
print(hlasy)            # {}
print(len(hlasy))       # 0


# V lekci 8 jsi stavěla seznam: začala jsi prázdným a v cyklu přidávala.
# Se slovníkem je to stejné, jen místo append přiřazuješ pod klíč.
# Tak převedeš seznam dvojic z lekce 8 na slovník:
darky_seznam = [("Anna", "dort"), ("Petra", "víno"), ("Jana", "chlebíčky")]

darky = {}
for jmeno, darek in darky_seznam:
    darky[jmeno] = darek

print(darky)            # {'Anna': 'dort', 'Petra': 'víno', 'Jana': 'chlebíčky'}
print(darky["Petra"])   # víno


# Hodnotu můžeš i spočítat. Kolik písmen má které jméno:
hoste = ["Anna", "Petra", "Jana"]

delky = {}
for jmeno in hoste:
    delky[jmeno] = len(jmeno)

print(delky)            # {'Anna': 4, 'Petra': 5, 'Jana': 4}


# Klíče můžou být i čísla. Na začátku večírku nesedí u žádného ze tří
# stolů nikdo:
u_stolu = {}
for stul in range(1, 4):
    u_stolu[stul] = 0

print(u_stolu)          # {1: 0, 2: 0, 3: 0}


# Slovník postavíš i z textu. Metoda split ti vrátí seznam a ten se dá
# rozbalit stejně jako n-tice:
zprava = "Anna:dort, Petra:víno, Jana:chlebíčky"

darky = {}
for odpoved in zprava.split(", "):
    jmeno, darek = odpoved.split(":")
    darky[jmeno] = darek

print(darky)            # {'Anna': 'dort', 'Petra': 'víno', 'Jana': 'chlebíčky'}
