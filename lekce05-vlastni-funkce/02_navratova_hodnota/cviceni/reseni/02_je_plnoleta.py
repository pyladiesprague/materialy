# Řešení cvičení 2 – Návratová hodnota
# Tvoje řešení může vypadat jinak, a to je v pořádku.

# Napiš funkci je_plnoleta(vek), která vrátí True, nebo False.
#    Zeptej se uživatele na věk a podle výsledku vypiš
#    "Můžeš dál." nebo "Ještě ne.".

def je_plnoleta(vek):
    return vek >= 18


vek = int(input("Kolik ti je let? "))
if je_plnoleta(vek):
    print("Můžeš dál.")
else:
    print("Ještě ne.")
