# Řešení cvičení 5 – Cyklus while
# Tvoje řešení může vypadat jinak, a to je v pořádku.

# Pořád dokola se ptej "Napiš slovo: " a to slovo vypiš.
#    Když uživatel napíše "konec", ukonči cyklus příkazem break.
#    Použij while True.

while True:
    slovo = input("Napiš slovo: ")
    if slovo == "konec":
        break
    print(slovo)
print("Konec.")
