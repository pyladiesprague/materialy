# Řešení cvičení 6 – Počítání a skupiny
# Tvoje řešení může vypadat jinak, a to je v pořádku.

# Jsou tu tři chyby a každá je jiného druhu. Jednu ti ukáže chybová
# hláška, další dvě najdeš debuggerem. Oprav je po jedné a po každé
# opravě program spusť.

# Barman si zapisoval, kdo si co objednal. Píše, jak ho napadne, takže
# víno může být i "Víno". Program má spočítat útratu každého hosta
# a najít, kdo utratil nejvíc. Vypsat má:
#
#   Anna: 105 Kč
#   Petra: 120 Kč
#   Jana: 35 Kč
#   Nejvíc utratila Petra (120 Kč).

cenik = {"pivo": 45, "víno": 60, "džus": 35}
objednavky = [("Anna", "pivo"), ("Petra", "víno"), ("Anna", "Víno"),
              ("Jana", "džus"), ("Petra", "víno")]


def spocitej_utraty(objednavky, cenik):
    utraty = {}
    for jmeno, napoj in objednavky:
        cena = cenik[napoj.lower()]                 # 1. chyba
        if jmeno in utraty:
            utraty[jmeno] = utraty[jmeno] + cena    # 2. chyba
        else:
            utraty[jmeno] = cena
    return utraty


def kdo_nejvic(utraty):
    kdo = ""
    nejvic = 0
    for jmeno, castka in utraty.items():
        if castka > nejvic:
            kdo = jmeno
            nejvic = castka                         # 3. chyba
    return kdo, nejvic


utraty = spocitej_utraty(objednavky, cenik)

for jmeno, castka in utraty.items():
    print(f"{jmeno}: {castka} Kč")

kdo, castka = kdo_nejvic(utraty)
print(f"Nejvíc utratila {kdo} ({castka} Kč).")

# 1. KeyError: 'Víno' – v ceníku jsou nápoje malými písmeny. Ukázala ji
#    chybová hláška.
# 2. Když host už ve slovníku byl, jeho útrata se přepsala cenou
#    posledního nápoje místo toho, aby se k ní přičetla. V debuggeru je
#    vidět, že Anně se z 45 stane 60.
# 3. Proměnná nejvic zůstávala na nule, takže podmínku splnil každý host
#    a vyhrál ten poslední. V debuggeru je vidět, že nejvic se nemění.
