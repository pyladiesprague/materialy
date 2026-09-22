# Řešení cvičení 1 – Funkce dohromady
# Tvoje řešení může vypadat jinak, a to je v pořádku.

# Napiš funkci nadpis(text), která vypíše text a pod něj čáru
#    z pomlček dlouhou přesně jako ten text.
#    Vyzkoušej ji na dvou různě dlouhých nadpisech.

def nadpis(text):
    print(text)
    print("-" * len(text))


nadpis("Lekce 5")
nadpis("Vlastní funkce a návratové hodnoty")
