# Řešení bonusu 2 – Vstup od uživatelky
# Tvoje řešení může vypadat jinak, a to je v pořádku.

# Zeptej se na částku a na počet lidí.
#     Vypiš, kolik zaplatí každý a kolik korun zbyde.

castka = int(input("Kolik je účet? "))
lidi = int(input("Kolik vás je? "))
print("Každý zaplatí:", castka // lidi)
print("Zbyde:", castka % lidi)
