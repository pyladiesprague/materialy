# Řešení bonusu 2 – Funkce dohromady
# Tvoje řešení může vypadat jinak, a to je v pořádku.

# Napiš funkci nejvetsi_ze_tri(a, b, c), která vrátí největší
#     ze tří čísel. Uvnitř použij funkci vetsi(a, b) z minulé složky –
#     zkopíruj si její definici sem nahoru, soubory se navzájem nevidí.

def vetsi(a, b):
    if a > b:
        return a
    else:
        return b


def nejvetsi_ze_tri(a, b, c):
    return vetsi(vetsi(a, b), c)


print(nejvetsi_ze_tri(3, 9, 5))
