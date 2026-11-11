# Řešení cvičení 3 – Záznamy
# Tvoje řešení může vypadat jinak, a to je v pořádku.

# Na večírek je potřeba spoustu věcí zařídit. Vypiš:
#    - kolik úkolů je hotových,
#    - kdo má co ještě udělat. Nehotové úkoly rozděl podle lidí.
#
#      Hotovo: 2 z 5
#      Anna: upéct dort
#      Petra: nafouknout balonky, připravit playlist

ukoly = [
    {"ukol": "koupit víno", "kdo": "Petra", "hotovo": True},
    {"ukol": "upéct dort", "kdo": "Anna", "hotovo": False},
    {"ukol": "nafouknout balonky", "kdo": "Petra", "hotovo": False},
    {"ukol": "poslat pozvánky", "kdo": "Jana", "hotovo": True},
    {"ukol": "připravit playlist", "kdo": "Petra", "hotovo": False},
]

hotovych = 0
zbyva = {}

for ukol in ukoly:
    if ukol["hotovo"]:
        hotovych = hotovych + 1
    else:
        kdo = ukol["kdo"]
        if kdo not in zbyva:
            zbyva[kdo] = []
        zbyva[kdo].append(ukol["ukol"])

print(f"Hotovo: {hotovych} z {len(ukoly)}")

for kdo, jeho_ukoly in zbyva.items():
    print(f"{kdo}: {', '.join(jeho_ukoly)}")
