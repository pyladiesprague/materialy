# Cvičení 5 – Počítání a skupiny
# Spusť soubor (Run). Výsledek je špatný. Najdi chybu debuggerem.

# Program má spočítat, kolikrát si hosté objednali který nápoj. Vypíše
# ale jen {'pivo': 1}. Dej breakpoint na řádek s if a krokuj. V panelu
# Variables sleduj napoj a pocty. Pak program oprav.
#
#   Vyjít má:  {'víno': 1, 'pivo': 3, 'džus': 1}

objednavky = ["víno", "pivo", "džus", "pivo", "pivo"]

for napoj in objednavky:
    pocty = {}
    if napoj in pocty:
        pocty[napoj] = pocty[napoj] + 1
    else:
        pocty[napoj] = 1

print(pocty)
