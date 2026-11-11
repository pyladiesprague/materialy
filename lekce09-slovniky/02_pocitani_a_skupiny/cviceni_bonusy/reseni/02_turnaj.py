# Řešení bonusu 2 – Počítání a skupiny
# Tvoje řešení může vypadat jinak, a to je v pořádku.

# Na večírku se hraje turnaj v ping-pongu. Každý zápas je dvojice
#    (vítěz, poražený). Spočítej, kolik zápasů kdo vyhrál. Ve výsledku
#    musí být každý hráč, i ten, kdo nevyhrál nic.
#
#      Anna: 2
#      Petra: 1
#      Jana: 0

zapasy = [("Anna", "Petra"), ("Petra", "Jana"), ("Anna", "Jana")]

vyhry = {}
for vitez, porazeny in zapasy:
    if vitez in vyhry:
        vyhry[vitez] = vyhry[vitez] + 1
    else:
        vyhry[vitez] = 1
    if porazeny not in vyhry:
        vyhry[porazeny] = 0

for hrac, pocet in vyhry.items():
    print(f"{hrac}: {pocet}")
