# Řešení cvičení 7 – Vestavěné funkce
# Tvoje řešení může vypadat jinak, a to je v pořádku.

# Uživatel zadá počet sekund (třeba 3661). Přepočítej ho na hodiny,
#    minuty a sekundy a vypiš je jako 1:1:1 jediným printem.

sekundy = int(input("Zadej počet sekund: "))
hodiny = sekundy // 3600            # kolik celých hodin
minuty = sekundy % 3600 // 60       # ze zbytku kolik celých minut
zbyle = sekundy % 60                # a co zbyde jsou sekundy
print(hodiny, minuty, zbyle, sep=":")   # pro 3661 vypíše 1:1:1
