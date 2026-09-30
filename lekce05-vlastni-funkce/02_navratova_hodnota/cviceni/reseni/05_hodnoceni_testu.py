# Řešení cvičení 5 – Návratová hodnota
# Tvoje řešení může vypadat jinak, a to je v pořádku.

# Napiš funkci hodnoceni(body), která vrátí "prošla" pro 50 a víc bodů
#    a "neprošla" pro méně. Pak se v cyklu while ptej na body tak dlouho,
#    dokud uživatel nezadá -1, a u každého zadání vypiš hodnocení.

def hodnoceni(body):
    if body >= 50:
        return "prošla"
    else:
        return "neprošla"


body = int(input("Zadej body (-1 = konec): "))
while body != -1:
    print(body, "bodů:", hodnoceni(body))
    body = int(input("Zadej body (-1 = konec): "))
