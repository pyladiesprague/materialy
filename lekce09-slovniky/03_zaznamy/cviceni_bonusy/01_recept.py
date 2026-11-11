# Bonus 1 – Záznamy
# Doplň kód pod zadání a soubor spusť (Run).

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
