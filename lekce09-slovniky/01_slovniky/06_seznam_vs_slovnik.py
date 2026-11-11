# ---------------------------------------------
#  Seznam vs slovník – kdy použít který
# ---------------------------------------------
# Spusť soubor a porovnej výsledky.
#
# Oba drží víc hodnot. Liší se tím, jak se k nim dostaneš:
#   seznam   – hodnoty stojí v pořadí a sahá se na ně indexem 0, 1, 2…
#   slovník  – každá hodnota má klíč, který si zvolíš, a sahá se podle něj


# Stejná data oběma způsoby. Kolik let je Petře?

# Seznamem: musíš vědět, že Petra je druhá, tedy index 1. Ze seznamu
# samotného to nepoznáš:
veky_seznam = [34, 25, 41]
print(veky_seznam[1])   # 25

# Slovníkem: zeptáš se rovnou na Petru:
veky = {"Anna": 34, "Petra": 25, "Jana": 41}
print(veky["Petra"])    # 25


# Index se navíc posouvá. Když Anna odejde, Petra je najednou první:
veky_seznam.pop(0)
print(veky_seznam[1])   # 41 – to už je Jana

# Klíč zůstává, ať se ve slovníku děje cokoli:
veky.pop("Anna")
print(veky["Petra"])    # 25

# (Oba způsoby vedle sebe ukazuje obrázek seznam_vs_slovnik.png.)


# Kdy co:
#   seznam   – záleží na pořadí, nebo hodnoty nemají jméno:
#              fronta, playlist, naměřené teploty, žebříček
#   slovník  – hledáš podle jména nebo kódu:
#              ceník, telefonní seznam, překlady, kdo co přinese
#
# N-tice z lekce 8 se dál hodí na pevnou skupinu hodnot, které patří
# k sobě, třeba jméno a dárek.
