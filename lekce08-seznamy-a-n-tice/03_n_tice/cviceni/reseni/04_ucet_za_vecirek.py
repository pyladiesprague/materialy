# Řešení cvičení 4 – N-tice
# Tvoje řešení může vypadat jinak, a to je v pořádku.

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
    for zbozi, kusy, cena in nakup:
        celkem = celkem + kusy * cena
    return celkem


def nejvetsi_polozka(nakup):
    nejvetsi = ""
    nejvic = 0
    for zbozi, kusy, cena in nakup:
        if kusy * cena > nejvic:
            nejvetsi = zbozi
            nejvic = kusy * cena
    return nejvetsi, nejvic


celkem = celkova_utrata(nakup)
zbozi, castka = nejvetsi_polozka(nakup)

print(f"Celkem: {celkem} Kč")
print(f"Na hosta: {celkem / hostu:.0f} Kč")
print(f"Největší položka: {zbozi} ({castka} Kč)")


# 1. ValueError: too many values to unpack.
#    N-tice v nákupu mají tři hodnoty, ale cyklus rozbaluje jen dvě.
#    Patří tam for zbozi, kusy, cena in nakup.
#
#    Program doběhne, ale vypíše Celkem: 450 Kč.
#
# 2. Breakpoint do celkova_utrata a krokování ukáže, že funkce skončí
#    po prvním průchodu. Řádek return je odsazený uvnitř cyklu. Patří
#    až za něj.
#
#    Celkem i Na hosta už sedí, ale největší položka vyšla dort.
#
# 3. Breakpoint do nejvetsi_polozka ukáže, že se porovnává cena jednoho
#    kusu, takže vyhrává dort za 420 Kč. Víno stojí za kus jen 150 Kč,
#    ale tři kusy dělají 450 Kč. Porovnávat se má kusy * cena.
