# Řešení cvičení 3 – Definice funkce
# Tvoje řešení může vypadat jinak, a to je v pořádku.

# Napiš funkci ohodnot_znamku(znamka), která vypíše:
#    1 → "Výborně", 2 → "Chvalitebně", 3 → "Dobře",
#    cokoliv jiného → "Ještě zabereme".
#    Vyzkoušej ji na známkách 1, 3 a 5.

def ohodnot_znamku(znamka):
    if znamka == 1:
        print("Výborně")
    elif znamka == 2:
        print("Chvalitebně")
    elif znamka == 3:
        print("Dobře")
    else:
        print("Ještě zabereme")


ohodnot_znamku(1)
ohodnot_znamku(3)
ohodnot_znamku(5)
