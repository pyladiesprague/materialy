# Řešení bonusu 2 – Měnění seznamů
# Tvoje řešení může vypadat jinak, a to je v pořádku.

# Ze seznamu postav nový seznam, ve kterém se žádná položka neopakuje
#    a pořadí zůstane stejné.
#
#    Vyjít má:  ['pes', 'kočka', 'křeček']

zvirata = ["pes", "kočka", "pes", "křeček", "kočka"]

bez_opakovani = []

for zvire in zvirata:
    if zvire not in bez_opakovani:
        bez_opakovani.append(zvire)

print(bez_opakovani)
