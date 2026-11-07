# Řešení cvičení 1 – Seznamy
# Tvoje řešení může vypadat jinak, a to je v pořádku.

# Vytvoř seznam pěti svých oblíbených filmů. Vypiš:
#    - první film,
#    - poslední film,
#    - první tři filmy jako výřez,
#    - všechny filmy, každý na vlastní řádek s pomlčkou na začátku,
#    - kolik filmů v seznamu je.

filmy = ["Pelíšky", "Amélie z Montmartru", "Vetřelec", "Ratatouille", "Matrix"]

print(filmy[0])
print(filmy[-1])
print(filmy[:3])

for film in filmy:
    print(f"- {film}")

print(f"Celkem: {len(filmy)}")
