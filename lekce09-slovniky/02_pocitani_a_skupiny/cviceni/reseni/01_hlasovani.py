# Řešení cvičení 1 – Počítání a skupiny
# Tvoje řešení může vypadat jinak, a to je v pořádku.

# Hosté vybírají dezert. Ptej se "Hlas: ", dokud někdo nenapíše "konec".
#    - Hlasy počítej ve slovníku.
#    - Velikost písmen a mezery navíc nehrají roli.
#    - Prázdný hlas nepočítej.
#    - Napiš funkci najdi_viteze, která má na vstupu slovník s hlasy
#      a vrátí dezert s nejvíc hlasy. Když nikdo nehlasoval, vrátí None.
#    - Na konci vypiš počet hlasů pro každý dezert a vítěze. Když nikdo
#      nehlasoval, vypiš "Nikdo nehlasoval.".
#
#      Hlas: dort
#      Hlas: Zmrzlina
#      Hlas:  dort
#      Hlas: konec
#      dort: 2
#      zmrzlina: 1
#      Vyhrává dort.


def najdi_viteze(hlasy):
    vitez = None
    nejvic = 0
    for dezert, pocet in hlasy.items():
        if pocet > nejvic:
            vitez = dezert
            nejvic = pocet
    return vitez


hlasy = {}

while True:
    hlas = input("Hlas: ").strip().lower()
    if hlas == "konec":
        break
    if hlas == "":
        continue

    if hlas in hlasy:
        hlasy[hlas] = hlasy[hlas] + 1
    else:
        hlasy[hlas] = 1

for dezert, pocet in hlasy.items():
    print(f"{dezert}: {pocet}")

vitez = najdi_viteze(hlasy)
if vitez is None:
    print("Nikdo nehlasoval.")
else:
    print(f"Vyhrává {vitez}.")

# Když je slovník prázdný, cyklus ve funkci neproběhne ani jednou
# a vitez zůstane None. Zápis is None znáš z první sekce.
