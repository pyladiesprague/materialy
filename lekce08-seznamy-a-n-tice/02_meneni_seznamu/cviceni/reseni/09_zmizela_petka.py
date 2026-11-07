# Řešení cvičení 9 – Měnění seznamů
# Tvoje řešení může vypadat jinak, a to je v pořádku.

# Program má ze seznamu odebrat všechny pětky, ale jedna zůstane.
# Dej breakpoint na řádek s if a krokuj. V panelu Variables sleduj
# znamka a znamky. Pak program oprav.

znamky = [5, 5, 1, 2]
bez_petek = []

for znamka in znamky:
    if znamka != 5:
        bez_petek.append(znamka)

print(bez_petek)


# V prvním průchodu cyklus stojí na indexu 0 a remove pětku odebere.
# Ostatní položky se posunou o jedno doleva, takže druhá pětka je teď
# na indexu 0. Cyklus jde dál na index 1 a tu pětku přeskočí.
#
# Seznam, který procházíš, proto neměň. Postav si nový.
