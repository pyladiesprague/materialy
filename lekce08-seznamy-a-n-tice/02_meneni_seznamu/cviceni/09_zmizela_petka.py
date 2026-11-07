# Cvičení 9 – Měnění seznamů
# Spusť soubor (Run). Výsledek je špatný. Najdi chybu debuggerem.

# Program má ze seznamu odebrat všechny pětky, ale jedna zůstane.
# Dej breakpoint na řádek s if a krokuj. V panelu Variables sleduj
# znamka a znamky. Pak program oprav.

znamky = [5, 5, 1, 2]

for znamka in znamky:
    if znamka == 5:
        znamky.remove(znamka)

print(znamky)
