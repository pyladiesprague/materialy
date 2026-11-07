# ---------------------------------------------
#  Stavíme seznam v cyklu
# ---------------------------------------------
# Spusť soubor a porovnej výsledky. Na konci se tě zeptá na jména.

hoste = ["Anna", "Petra", "Jana"]


# Tohle je nejčastější práce se seznamem: začneš s prázdným a v cyklu
# do něj přidáváš.
pozvanky = []

for host in hoste:
    pozvanky.append(f"Pozvánka pro: {host}")

print(pozvanky)
# ['Pozvánka pro: Anna', 'Pozvánka pro: Petra', 'Pozvánka pro: Jana']


# Stejně si vybereš jen některé položky. Podmínka rozhodne, co se přidá.
# Tady chceš vědět, které nákupy na večírek stojí přes 100 Kč:
ceny = [120, 45, 300, 80, 150]
drahe = []

for cena in ceny:
    if cena > 100:
        drahe.append(cena)

print(drahe)                # [120, 300, 150]
print(ceny)                 # [120, 45, 300, 80, 150]


# Funkce list převede range na seznam. Hodí se to třeba na čísla stolů:
stoly = list(range(1, 6))
print(stoly)                # [1, 2, 3, 4, 5]


# V lekci 4 jsi v cyklu četla jména a hned je vypisovala. Potom byla
# pryč. Se seznamem ti zůstanou:
prihlaseni = []

while True:
    jmeno = input("Jméno (konec = hotovo): ")
    if jmeno == "konec":
        break
    prihlaseni.append(jmeno)

print(f"Přihlášených: {len(prihlaseni)}")
print(prihlaseni)
