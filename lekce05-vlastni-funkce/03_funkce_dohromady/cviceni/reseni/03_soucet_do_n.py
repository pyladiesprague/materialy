# Řešení cvičení 3 – Funkce dohromady
# Tvoje řešení může vypadat jinak, a to je v pořádku.

# Napiš funkci soucet_do(n), která vrátí součet čísel od 1 do n.
#    soucet_do(5) vrátí 15.

def soucet_do(n):
    soucet = 0
    for cislo in range(1, n + 1):
        soucet = soucet + cislo
    return soucet


print("Součet do 5:", soucet_do(5))
