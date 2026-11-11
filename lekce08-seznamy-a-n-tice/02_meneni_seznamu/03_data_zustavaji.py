# ---------------------------------------------
#  Data zůstávají
# ---------------------------------------------
# Spusť soubor. Zeptá se tě na věk hostů.

# V lekci 3 jsi počítala statistiku čísel od uživatele. V cyklu sis
# průběžně hlídala součet, největší a nejmenší číslo:
#
#     soucet = soucet + cislo
#     if cislo > nejvetsi:
#         nejvetsi = cislo
#     if cislo < nejmensi:
#         nejmensi = cislo
#
# Každá nová otázka by znamenala další proměnnou. Se seznamem si čísla
# jen uložíš a počítáš až potom:
pocet = int(input("Kolik hostů? "))
veky = []

for i in range(pocet):
    odpoved = input("Věk: ")
    vek = int(odpoved)
    veky.append(vek)

# Ty tři řádky v cyklu se dají napsat i na jeden. Vyhodnocuje se to
# zevnitř ven: input, pak int, pak append.
#
#     veky.append(int(input("Věk: ")))
#
# Kratší ale neznamená lepší. Piš to tak, jak se ti to líp čte.

print(f"Součet: {sum(veky)}")
print(f"Průměr: {sum(veky) / len(veky):.1f}")
print(f"Nejstarší: {max(veky)}")
print(f"Nejmladší: {min(veky)}")


# Čísla pořád máš, takže můžeš položit otázku, se kterou jsi předtím
# nepočítala:
dospeli = 0

for vek in veky:
    if vek >= 18:
        dospeli = dospeli + 1

print(f"Dospělých: {dospeli}")
