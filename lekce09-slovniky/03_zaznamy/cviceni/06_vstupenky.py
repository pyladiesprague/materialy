# Cvičení 6 – Záznamy

# Jsou tu tři chyby a každá je jiného druhu. Jednu ti ukáže chybová
# hláška, další dvě najdeš debuggerem. Oprav je po jedné a po každé
# opravě program spusť.

# Program prodává vstupenky na večírek. Děti do 15 let platí 100 Kč,
# ostatní 250 Kč. Funkce s_cenou má vrátit kopii hosta s cenou, původní
# seznam hostů se nemá změnit. Vypsat má:
#
#   Anna: 250 Kč
#   Tom: 100 Kč
#   Petra: 250 Kč
#   Ema: 100 Kč
#   Celkem: 700 Kč
#   Původní záznam: {'jmeno': 'Anna', 'vek': 34}

hoste = [
    {"jmeno": "Anna", "vek": 34},
    {"jmeno": "Tom", "vek": 9},
    {"jmeno": "Petra", "vek": 25},
    {"jmeno": "Ema", "vek": 12},
]


def s_cenou(host):
    novy = host
    if host["vek"] < 15:
        novy["cena"] = 100
    else:
        novy["cena"] = 250
    return novy


def celkem(vstupenky):
    soucet = 0
    for vstupenka in vstupenky:
        soucet = soucet + vstupenka["cena"]
        return soucet


vstupenky = []
for host in hoste:
    vstupenky.append(s_cenou(host))

for vstupenka in vstupenky:
    print(f"{vstupenka['jmneo']}: {vstupenka['cena']} Kč")

print(f"Celkem: {celkem(vstupenky)} Kč")
print(f"Původní záznam: {hoste[0]}")
