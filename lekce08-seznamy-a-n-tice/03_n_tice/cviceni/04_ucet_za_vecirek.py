# Cvičení 4 – N-tice
# Jsou tu tři chyby a každá je jiného druhu. Jednu ti ukáže chybová
# hláška, další dvě najdeš debuggerem. Oprav je po jedné a po každé
# opravě program spusť.

# Program spočítá útratu za večírek. V nákupu je zboží, počet kusů
# a cena za kus. Celkovou útratu si šest hostů rozdělí rovným dílem.
# Vypsat má:
#
#   Celkem: 1230 Kč
#   Na hosta: 205 Kč
#   Největší položka: víno (450 Kč)

nakup = [("víno", 3, 150), ("dort", 1, 420), ("chlebíčky", 20, 18)]
hostu = 6


def celkova_utrata(nakup):
    celkem = 0
    for zbozi, kusy in nakup:
        celkem = celkem + kusy * cena
        return celkem


def nejvetsi_polozka(nakup):
    nejvetsi = ""
    nejvic = 0
    for zbozi, kusy, cena in nakup:
        if cena > nejvic:
            nejvetsi = zbozi
            nejvic = cena
    return nejvetsi, nejvic


celkem = celkova_utrata(nakup)
zbozi, castka = nejvetsi_polozka(nakup)

print(f"Celkem: {celkem} Kč")
print(f"Na hosta: {celkem / hostu:.0f} Kč")
print(f"Největší položka: {zbozi} ({castka} Kč)")
