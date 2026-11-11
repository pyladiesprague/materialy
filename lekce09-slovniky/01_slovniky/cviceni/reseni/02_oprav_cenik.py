# Řešení cvičení 2 – Slovníky
# Tvoje řešení může vypadat jinak, a to je v pořádku.

# Program se zeptá na nápoj a vypíše jeho cenu. Když ale napíšeš
#    "Pivo" nebo " pivo", spadne. Spadne i na "rum". Spusť ho, přečti si
#    hlášku a oprav ho tak, aby:
#    - prošlo i velké písmeno a mezery navíc,
#    - na nápoj, který není v ceníku, vypsal "Tohle nemáme.".

cenik = {"pivo": 45, "víno": 60, "džus": 35}

napoj = input("Co si dáš? ").strip().lower()

if napoj in cenik:
    print(f"{napoj} stojí {cenik[napoj]} Kč.")
else:
    print("Tohle nemáme.")
