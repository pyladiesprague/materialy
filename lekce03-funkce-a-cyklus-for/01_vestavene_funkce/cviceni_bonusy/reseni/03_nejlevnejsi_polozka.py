# Řešení bonusu 3 – Vestavěné funkce
# Tvoje řešení může vypadat jinak, a to je v pořádku.

# Cíl a rozpočet. Uživatel zadá cenu tří položek. Vypiš nejlevnější
#     a nejdražší z nich a jestli se všechny tři vejdou do rozpočtu 1000 Kč.

cena1 = int(input("Cena 1: "))
cena2 = int(input("Cena 2: "))
cena3 = int(input("Cena 3: "))
print("Nejlevnější:", min(cena1, cena2, cena3))
print("Nejdražší:", max(cena1, cena2, cena3))
if cena1 + cena2 + cena3 <= 1000:
    print("Vejdou se do rozpočtu.")
else:
    print("Rozpočet nestačí.")
