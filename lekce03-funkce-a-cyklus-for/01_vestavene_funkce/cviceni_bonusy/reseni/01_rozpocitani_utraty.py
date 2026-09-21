# Řešení bonusu 1 – Vestavěné funkce
# Tvoje řešení může vypadat jinak, a to je v pořádku.

# Uživatel zadá celkovou cenu útraty a počet lidí. Vypiš, kolik
#     zaplatí každý, zaokrouhleno na dvě desetinná místa.

cena = int(input("Kolik jste utratili? "))
lidi = int(input("Kolik vás bylo? "))
print(round(cena / lidi, 2))        # pro 1000 a 3 vypíše 333.33
