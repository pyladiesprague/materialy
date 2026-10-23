# Řešení cvičení 2 – Skládání textu
# Tvoje řešení může vypadat jinak, a to je v pořádku.

# Vypiš účtenku tak, aby ceny byly pod sebou: název zarovnaný doleva
#    na dvanáct míst, cenu doprava na osm míst se dvěma desetinnými
#    místy. Na konec přidej řádek se součtem.
#
#    Když je součet vyšší než 150 Kč, přidej ještě řádek se slevou
#    deset procent a řádek s cenou po slevě.

polozka1 = "káva"
cena1 = 59
polozka2 = "dort"
cena2 = 84.5
polozka3 = "čaj"
cena3 = 45


def radek(nazev, castka):
    print(f"{nazev:12}{castka:8.2f}")


radek(polozka1, cena1)
radek(polozka2, cena2)
radek(polozka3, cena3)

soucet = cena1 + cena2 + cena3
radek("součet", soucet)

if soucet > 150:
    sleva = soucet * 0.1
    radek("sleva", sleva)
    radek("k platbě", soucet - sleva)

# Řádek se opakoval pořád stejně, tak si na něj jde napsat funkci
# z lekce 5 – a pak ji použít i na součet a slevu.
