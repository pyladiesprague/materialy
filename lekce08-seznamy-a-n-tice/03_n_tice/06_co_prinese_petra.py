# ---------------------------------------------
#  Co přinese Petra?
# ---------------------------------------------
# Spusť soubor a porovnej výsledky.

darky = [("Anna", "dort"), ("Petra", "víno"), ("Jana", "chlebíčky")]


# Chceš zjistit jednu věc: co přinese Petra. Se seznamem dvojic musíš
# projít hosty jednoho po druhém, dokud ji nenajdeš:
def co_prinese(hledane_jmeno, darky):
    for jmeno, darek in darky:
        if jmeno == hledane_jmeno:
            return darek
    return None


print(co_prinese("Petra", darky))   # víno
print(co_prinese("Karel", darky))   # None

# Funguje to, ale na každou otázku tohoto typu je potřeba celý cyklus.
# V lekci 9 potkáš slovníky, kde si hodnotu vytáhneš rovnou podle jména.
