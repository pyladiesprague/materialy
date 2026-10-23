# ---------------------------------------------
#  Proč f-string
# ---------------------------------------------
# Spusť soubor a porovnej výsledky.

jmeno = "Anna"
vek = 30


# Před uvozovky napiš f a proměnnou dej do složených závorek:
print(f"Je mi {vek} let")       # Je mi 30 let
print(f"Ahoj {jmeno}")          # Ahoj Anna

# Python si hodnotu ze závorek doplní do textu. Číslo si převede sám
# a mezery jsou tam, kde je napíšeš.


# Závorek může být v jedné větě, kolik potřebuješ. Tohle je ta věta,
# na které minulý soubor skončil:
print(f"Ahoj {jmeno}, je ti {vek} let.")    # Ahoj Anna, je ti 30 let.

# Žádné str(), žádné hlídání mezer kolem plusů.
