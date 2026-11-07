# Řešení bonusu 1 – Měnění seznamů
# Tvoje řešení může vypadat jinak, a to je v pořádku.

from random import choice

# Vylosuj tři výherce tomboly. Každý může vyhrát jen jednou, takže
#    vylosované jméno ze seznamu vždycky odeber.
#
#    Na první řádek patří:  from random import choice
#    choice(seznam) vrátí náhodnou položku seznamu.

hoste = ["Anna", "Petra", "Jana", "Eva", "Marie"]

for poradi in range(1, 4):
    vyherce = choice(hoste)
    hoste.remove(vyherce)
    print(f"{poradi}. cena: {vyherce}")
