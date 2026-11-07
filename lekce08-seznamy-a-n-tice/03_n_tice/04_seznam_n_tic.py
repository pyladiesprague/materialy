# ---------------------------------------------
#  Seznam n-tic
# ---------------------------------------------
# Spusť soubor a porovnej výsledky. Na konci si zahraješ kvíz.

# Seznam a n-tice se dobře doplňují. Každá n-tice je jeden host a seznam
# jich drží, kolik potřebuješ:
darky = [("Anna", "dort"), ("Petra", "víno"), ("Jana", "chlebíčky")]

print(darky[0])         # ('Anna', 'dort')
print(len(darky))       # 3


# V cyklu for se dá každá n-tice rovnou rozbalit:
for jmeno, darek in darky:
    print(f"{jmeno} přinese {darek}.")

# Anna přinese dort.
# Petra přinese víno.
# Jana přinese chlebíčky.


# Do seznamu přidáš n-tici stejně jako cokoli jiného. Pozor na dvojí
# závorky: vnitřní patří n-tici, vnější metodě append.
darky.append(("Eva", "víno"))
print(len(darky))       # 4


# Postup se stavěním seznamu funguje i tady:
vino = []

for jmeno, darek in darky:
    if darek == "víno":
        vino.append(jmeno)

print(vino)             # ['Petra', 'Eva']


# Na večírek chceš kvíz. V lekci 5 jsi měla na každou otázku vlastní
# volání a vlastní if. Když jsou otázky s odpověďmi v seznamu dvojic,
# stačí jeden cyklus a další otázku jen dopíšeš:
kviz = [
    ("Kolik je 7 * 8? ", "56"),
    ("Hlavní město Česka? ", "Praha"),
    ("Jak se jmenuje cyklus, co běží, dokud platí podmínka? ", "while"),
]
body = 0

for otazka, spravna in kviz:
    odpoved = input(otazka).strip()
    if odpoved == spravna:
        body = body + 1

print(f"Skóre: {body} z {len(kviz)}")
