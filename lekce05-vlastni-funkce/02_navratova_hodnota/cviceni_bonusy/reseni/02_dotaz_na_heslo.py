# Řešení bonusu 2 – Návratová hodnota
# Tvoje řešení může vypadat jinak, a to je v pořádku.

# Napiš funkci zeptej_se_na_heslo(), která se ptá tak dlouho,
#     dokud uživatel nezadá heslo aspoň o 8 znacích, a to heslo vrátí.
#     Uvnitř použij funkci je_heslo_dost_dlouhe z výkladu –
#     zkopíruj si její definici sem nahoru, soubory se navzájem nevidí.

def je_heslo_dost_dlouhe(heslo):
    return len(heslo) >= 8


def zeptej_se_na_heslo():
    heslo = input("Zvol si heslo: ")
    while not je_heslo_dost_dlouhe(heslo):
        print("Moc krátké, aspoň 8 znaků.")
        heslo = input("Zvol si heslo: ")
    return heslo


nove_heslo = zeptej_se_na_heslo()
print("Heslo nastaveno:", nove_heslo)
