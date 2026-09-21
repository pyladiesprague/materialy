# Řešení cvičení 6 – Cyklus while
# Tvoje řešení může vypadat jinak, a to je v pořádku.

# Ptej se na heslo. Když uživatel zadá "pyladies", vypiš "Vítej!"
#    a skonči. Když se splete třikrát, vypiš "Zablokováno." a skonči taky.
#    Z cyklu se v obou případech dostaneš příkazem break.

pokusy = 0
while True:
    heslo = input("Zadej heslo: ")
    pokusy = pokusy + 1
    if heslo == "pyladies":
        print("Vítej!")
        break
    if pokusy == 3:
        print("Zablokováno.")
        break
    print("Špatně, zkus to znovu.")
