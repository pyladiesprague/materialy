# Řešení bonusu 1 – Počítání a skupiny
# Tvoje řešení může vypadat jinak, a to je v pořádku.

# Anagramy jsou slova ze stejných písmen, jen jinak poskládaných, třeba
#    "rak" a "kra". Rozděl slova do skupin anagramů a vypiš skupiny,
#    ve kterých je víc než jedno slovo.
#
#    Tip: dvě slova jsou anagramy, když mají po seřazení písmen stejný
#    text. Slovo převedeš na seznam písmen funkcí list (lekce 8), seznam
#    seřadíš metodou sort a zpátky spojíš metodou join.
#
#      rak, kra
#      kos, sok
#      loket, kotel
#      lak, kal

slova = ["rak", "kos", "loket", "kra", "les", "sok", "kotel", "lak", "kal"]


def serazena_pismena(slovo):
    pismena = list(slovo)
    pismena.sort()
    return "".join(pismena)


skupiny = {}
for slovo in slova:
    klic = serazena_pismena(slovo)
    if klic not in skupiny:
        skupiny[klic] = []
    skupiny[klic].append(slovo)

for slova_ve_skupine in skupiny.values():
    if len(slova_ve_skupine) > 1:
        print(", ".join(slova_ve_skupine))
