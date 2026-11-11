# Řešení cvičení 5 – Počítání a skupiny
# Tvoje řešení může vypadat jinak, a to je v pořádku.

# Program má spočítat, kolikrát si hosté objednali který nápoj. Vypíše
# ale jen {'pivo': 1}. Dej breakpoint na řádek s if a krokuj. V panelu
# Variables sleduj napoj a pocty. Pak program oprav.
#
#   Vyjít má:  {'víno': 1, 'pivo': 3, 'džus': 1}

objednavky = ["víno", "pivo", "džus", "pivo", "pivo"]

pocty = {}
for napoj in objednavky:
    if napoj in pocty:
        pocty[napoj] = pocty[napoj] + 1
    else:
        pocty[napoj] = 1

print(pocty)

# Řádek pocty = {} byl uvnitř cyklu. V každém průchodu tak vznikl nový
# prázdný slovník a do něj se zapsal jen aktuální nápoj. Prázdný slovník
# se musí založit jednou, před cyklem.
