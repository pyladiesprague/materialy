# Řešení cvičení 2 – N-tice
# Tvoje řešení může vypadat jinak, a to je v pořádku.

# Napiš funkci samohlasky_a_souhlasky, která má na vstupu slovo a vrátí
#    dvě hodnoty: počet samohlásek a počet souhlásek. Výsledek rozbal
#    a vypiš:
#
#      večírek: 3 samohlásky, 4 souhlásky

def samohlasky_a_souhlasky(slovo):
    samohlasky = 0
    souhlasky = 0

    for pismeno in slovo.lower():
        if pismeno in "aáeéěiíoóuúůyý":
            samohlasky = samohlasky + 1
        else:
            souhlasky = souhlasky + 1

    return samohlasky, souhlasky


slovo = "večírek"
pocet_samohlasek, pocet_souhlasek = samohlasky_a_souhlasky(slovo)

print(f"{slovo}: {pocet_samohlasek} samohlásky, {pocet_souhlasek} souhlásky")
