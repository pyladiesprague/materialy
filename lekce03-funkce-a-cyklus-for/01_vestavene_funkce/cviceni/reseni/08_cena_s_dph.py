# Řešení cvičení 8 – Vestavěné funkce
# Tvoje řešení může vypadat jinak, a to je v pořádku.

# Zboží stojí 1000 Kč bez DPH. Na jeden řádek vypiš cenu bez DPH
#    i s DPH (21 %). Použij dva printy – první nech řádek pokračovat,
#    druhý ho dokonči.

cena = 1000
print("bez DPH:", cena, "Kč,", end=" ")     # end=" " – řádek pokračuje
print("s DPH:", round(cena * 1.21), "Kč")   # bez DPH: 1000 Kč, s DPH: 1210 Kč
