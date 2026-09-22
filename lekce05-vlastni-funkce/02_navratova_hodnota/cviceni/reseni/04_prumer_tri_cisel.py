# Řešení cvičení 4 – Návratová hodnota
# Tvoje řešení může vypadat jinak, a to je v pořádku.

# Napiš funkci prumer(a, b, c), která vrátí průměr tří čísel
#    zaokrouhlený na jedno desetinné místo.

def prumer(a, b, c):
    return round((a + b + c) / 3, 1)


print(prumer(1, 2, 4))
