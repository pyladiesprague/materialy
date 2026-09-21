# Řešení bonusu 4 – Procházení textu
# Tvoje řešení může vypadat jinak, a to je v pořádku.

# Teplotní skok. Uživatel postupně zadá sedm denních teplot
#     (klidně i záporných). Najdi a vypiš největší skok mezi dvěma
#     sousedními dny – tedy největší rozdíl teplot ze dne na den
#     (bez ohledu na to, jestli teplota stoupla, nebo klesla).

predchozi = int(input("Zadej teplotu: "))
nejvetsi_skok = 0
for den in range(6):                     # zbývá dalších šest dní
    teplota = int(input("Zadej teplotu: "))
    skok = abs(teplota - predchozi)      # rozdíl proti včerejšku, bez ohledu na směr
    if skok > nejvetsi_skok:
        nejvetsi_skok = skok
    predchozi = teplota                  # dnešek se stane včerejškem
print("Největší skok:", nejvetsi_skok)
