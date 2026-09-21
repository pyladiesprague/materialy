# Řešení bonusu 3 – And, or a not
# Tvoje řešení může vypadat jinak, a to je v pořádku.

# Kámen, nůžky, papír. Zeptej se obou hráčů na tah – ať zadají
#     "kamen", "nuzky" nebo "papir". Vypiš, kdo vyhrál:
#       - "Remíza.", když mají oba stejně,
#       - jinak urči vítěze podle pravidel:
#           kámen tupí nůžky, nůžky stříhají papír, papír balí kámen.
#     Vypiš "Vyhrál hráč 1." / "Vyhrál hráč 2.".

hrac1 = input("Hráč 1 (kamen/nuzky/papir): ")
hrac2 = input("Hráč 2 (kamen/nuzky/papir): ")
if hrac1 == hrac2:
    print("Remíza.")
elif (hrac1 == "kamen" and hrac2 == "nuzky") or (hrac1 == "nuzky" and hrac2 == "papir") or (hrac1 == "papir" and hrac2 == "kamen"):
    print("Vyhrál hráč 1.")
else:
    print("Vyhrál hráč 2.")
