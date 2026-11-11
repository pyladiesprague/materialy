# Řešení cvičení 1 – Slovníky
# Tvoje řešení může vypadat jinak, a to je v pořádku.

# Na večírku je bar a tohle je jeho ceník. Postupně:
#    - vypiš, kolik stojí víno,
#    - přidej limonádu za 40 Kč,
#    - zdraž pivo o 5 Kč,
#    - vodu odeber, došla,
#    - vypiš celý ceník a kolik položek v něm je.
#
#      Víno stojí 60 Kč.
#      {'pivo': 50, 'víno': 60, 'džus': 35, 'limonáda': 40}
#      Položek: 4

cenik = {"pivo": 45, "víno": 60, "džus": 35, "voda": 20}

# Klíč v apostrofech – proč, najdeš v 01_proc_slovnik.py.
print(f"Víno stojí {cenik['víno']} Kč.")

cenik["limonáda"] = 40
cenik["pivo"] = cenik["pivo"] + 5
cenik.pop("voda")

print(cenik)
print(f"Položek: {len(cenik)}")
