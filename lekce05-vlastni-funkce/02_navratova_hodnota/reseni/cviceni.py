# ---------------------------------------------
#  Řešení – návratová hodnota
# ---------------------------------------------


# 1) Cena i s 21% DPH.
def cena_s_dph(cena):
    return cena * 1.21


print("100 Kč s DPH:", cena_s_dph(100))
print("250 Kč s DPH:", cena_s_dph(250))


# 2) Plnoletost.
def je_plnoleta(vek):
    return vek >= 18


vek = int(input("Kolik ti je let? "))
if je_plnoleta(vek):
    print("Můžeš dál.")
else:
    print("Ještě ne.")


# 3) Větší z dvojice.
def vetsi(a, b):
    if a > b:
        return a
    else:
        return b


print(vetsi(3, 8))
print(vetsi(10, 2))


# 4) Průměr tří čísel.
def prumer(a, b, c):
    return round((a + b + c) / 3, 1)


print(prumer(1, 2, 4))


# 5) Hodnocení bodů, dokud uživatel nezadá -1.
def hodnoceni(body):
    if body >= 50:
        return "prošla"
    else:
        return "neprošla"


body = int(input("Zadej body (-1 = konec): "))
while body != -1:
    print(body, "bodů:", hodnoceni(body))
    body = int(input("Zadej body (-1 = konec): "))
