# Řešení cvičení 2 – Definice funkce
# Tvoje řešení může vypadat jinak, a to je v pořádku.

# Napiš funkci ramecek(text), která vypíše řádek hvězdiček,
#    pod něj text a pod něj další řádek hvězdiček.
#    Zavolej ji pro dva různé texty.

def ramecek(text):
    print("*" * 30)
    print(text)
    print("*" * 30)


ramecek("Vítej v kurzu!")
ramecek("Dneska nás čekají funkce.")
