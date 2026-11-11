# Řešení bonusu 1 – Záznamy
# Tvoje řešení může vypadat jinak, a to je v pořádku.

# Recept je na 4 porce. Zeptej se, pro kolik lidí vaříš, a vypiš
#    suroviny přepočítané na tolik porcí. Množství zaokrouhli na celé
#    číslo (funkce round z lekce 3).
#
#    Když uživatel nezadá kladné celé číslo, vypiš "Zadej kladné celé
#    číslo." a nic nepočítej.
#
#      Pro kolik lidí? 6
#      mouka: 750 g
#      mléko: 450 ml
#      vejce: 3 ks
#      cukr: 150 g

recept = {
    "porce": 4,
    "suroviny": {
        "mouka": (500, "g"),
        "mléko": (300, "ml"),
        "vejce": (2, "ks"),
        "cukr": (100, "g"),
    },
}

odpoved = input("Pro kolik lidí? ").strip()

if not odpoved.isdigit() or int(odpoved) == 0:
    print("Zadej kladné celé číslo.")
else:
    pomer = int(odpoved) / recept["porce"]

    for surovina, udaj in recept["suroviny"].items():
        mnozstvi, jednotka = udaj
        print(f"{surovina}: {round(mnozstvi * pomer)} {jednotka}")

# Metodu isdigit znáš z lekce 6. Ohlídá, že int nespadne na textu jako
# "šest" nebo "-2". Nulu je potřeba vyloučit zvlášť.
