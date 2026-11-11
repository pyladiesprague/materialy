# Řešení cvičení 4 – Počítání a skupiny
# Tvoje řešení může vypadat jinak, a to je v pořádku.

# Napiš funkci rozdel_podle_pismene, která má na vstupu seznam jmen
#    a vrátí slovník: klíč je první písmeno a hodnota seznam jmen, která
#    jím začínají.
#
#    Pak vypiš každé písmeno a za ním jména oddělená čárkou.
#
#      A: Anna, Adéla
#      P: Petra, Pavla
#      J: Jana

hoste = ["Anna", "Petra", "Jana", "Adéla", "Pavla"]


def rozdel_podle_pismene(jmena):
    skupiny = {}
    for jmeno in jmena:
        pismeno = jmeno[0]
        if pismeno not in skupiny:
            skupiny[pismeno] = []
        skupiny[pismeno].append(jmeno)
    return skupiny


podle_pismene = rozdel_podle_pismene(hoste)

for pismeno, jmena in podle_pismene.items():
    print(f"{pismeno}: {', '.join(jmena)}")

# Funkce počítá s tím, že žádné jméno není prázdný text. U prázdného
# textu by jmeno[0] spadlo na IndexError.
