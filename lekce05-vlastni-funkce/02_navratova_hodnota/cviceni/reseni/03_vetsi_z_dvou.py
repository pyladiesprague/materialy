# Řešení cvičení 3 – Návratová hodnota
# Tvoje řešení může vypadat jinak, a to je v pořádku.

# Napiš funkci vetsi(a, b), která vrátí větší z obou čísel.
#    Funkci max nepoužívej.

def vetsi(a, b):
    if a > b:
        return a
    else:
        return b


print(vetsi(3, 8))
print(vetsi(10, 2))
