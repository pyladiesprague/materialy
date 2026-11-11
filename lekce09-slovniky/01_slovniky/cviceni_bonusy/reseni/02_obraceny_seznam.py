# Řešení bonusu 2 – Slovníky
# Tvoje řešení může vypadat jinak, a to je v pořádku.

# Ve slovníku se hledá jen podle klíče. Někdo ti volá z čísla
#    731 333 444 a ty chceš vědět, kdo to je.
#
#    Napiš funkci otoc_slovnik, která má na vstupu slovník a vrátí nový slovník,
#    kde jsou klíče a hodnoty prohozené. Pak v něm číslo najdi.
#
#      Volá: Petra

telefony = {"Anna": "602 111 222", "Petra": "731 333 444", "Jana": "608 999 000"}


def otoc_slovnik(slovnik):
    otoceny = {}
    for klic, hodnota in slovnik.items():
        otoceny[hodnota] = klic
    return otoceny


podle_cisla = otoc_slovnik(telefony)
print(f"Volá: {podle_cisla['731 333 444']}")

# Pozor: kdyby dva lidé měli stejné číslo, v otočeném slovníku zůstane
# jen poslední z nich. Klíč může být ve slovníku jen jednou.
