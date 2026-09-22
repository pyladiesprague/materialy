# Řešení cvičení 4 – Funkce dohromady
# Tvoje řešení může vypadat jinak, a to je v pořádku.

# Napiš funkci zeptej_se_na_slovo(), která se ptá tak dlouho,
#    dokud uživatel nezadá slovo aspoň o třech písmenech, a slovo vrátí.
#    Zavolej ji a výsledek pošli do funkce nadpis z úkolu 1.

def zeptej_se_na_slovo():
    slovo = input("Zadej slovo (aspoň 3 písmena): ")
    while len(slovo) < 3:
        print("Moc krátké.")
        slovo = input("Zadej slovo (aspoň 3 písmena): ")
    return slovo


nadpis(zeptej_se_na_slovo())
