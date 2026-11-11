# Řešení bonusu 2 – Záznamy
# Tvoje řešení může vypadat jinak, a to je v pořádku.

# Tři kamarádky platily za večírek každá něco. Náklady se mají rozdělit
#    rovným dílem.
#    - Napiš funkci kolik_kdo_zaplatil, která má na vstupu seznam plateb
#      a vrátí slovník: jméno a kolik ta osoba zaplatila celkem.
#    - Spočítej, kolik vychází na jednu.
#    - Vypiš, kdo má kolik doplatit nebo dostat zpátky.
#
#      Anna zaplatila 510 Kč
#      Petra zaplatila 480 Kč
#      Jana zaplatila 360 Kč
#      Na jednu: 450 Kč
#      Anna dostane zpátky 60 Kč
#      Petra dostane zpátky 30 Kč
#      Jana doplatí 90 Kč

platby = [
    {"kdo": "Anna", "za_co": "dort", "castka": 420},
    {"kdo": "Petra", "za_co": "víno", "castka": 450},
    {"kdo": "Anna", "za_co": "balonky", "castka": 90},
    {"kdo": "Jana", "za_co": "chlebíčky", "castka": 360},
    {"kdo": "Petra", "za_co": "led", "castka": 30},
]


def kolik_kdo_zaplatil(platby):
    zaplatila = {}
    for platba in platby:
        kdo = platba["kdo"]
        zaplatila[kdo] = zaplatila.get(kdo, 0) + platba["castka"]
    return zaplatila


zaplatila = kolik_kdo_zaplatil(platby)

if len(zaplatila) == 0:
    print("Nikdo nic neplatil.")
else:
    for kdo, castka in zaplatila.items():
        print(f"{kdo} zaplatila {castka} Kč")

    na_jednu = sum(zaplatila.values()) / len(zaplatila)
    print(f"Na jednu: {na_jednu:.0f} Kč")

    for kdo, castka in zaplatila.items():
        rozdil = castka - na_jednu
        if rozdil > 0:
            print(f"{kdo} dostane zpátky {rozdil:.0f} Kč")
        elif rozdil < 0:
            print(f"{kdo} doplatí {-rozdil:.0f} Kč")
        else:
            print(f"{kdo} je vyrovnaná")
