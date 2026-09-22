# Řešení bonusu 2 – Definice funkce
# Tvoje řešení může vypadat jinak, a to je v pořádku.

# Napiš funkci ucet(cena, pocet), která vypíše řádek účtenky:
#     kolik kusů, cena za kus a celková cena.
#     Například ucet(25, 4) vypíše: 4 x 25 Kč = 100 Kč

def ucet(cena, pocet):
    print(pocet, "x", cena, "Kč =", cena * pocet, "Kč")


ucet(25, 4)
ucet(199, 2)
