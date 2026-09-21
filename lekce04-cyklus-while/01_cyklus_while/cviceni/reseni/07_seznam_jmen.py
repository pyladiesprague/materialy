# Řešení cvičení 7 – Cyklus while
# Tvoje řešení může vypadat jinak, a to je v pořádku.

# Ptej se "Jméno: " a každé jméno vypiš. Když uživatel nic nenapíše
#    a jen zmáčkne Enter, přeskoč výpis příkazem continue.
#    Cyklus ukonči, když uživatel napíše "konec".
#    (Prázdná odpověď z inputu je prázdný text: "")

while True:
    jmeno = input("Jméno: ")
    if jmeno == "konec":
        break
    if jmeno == "":
        continue
    print(jmeno)
print("Konec.")
