# ---------------------------------------------
#  Co může být ve složených závorkách
# ---------------------------------------------
# Spusť soubor a porovnej výsledky.

kniha = "Malý princ"
stran_celkem = 320
precteno = 184


# Nejen proměnná. Do závorek jde i výpočet:
print(f"Zbývá {stran_celkem - precteno} stran.")        # Zbývá 136 stran.

# Vestavěná funkce:
print(f"Název má {len(kniha)} znaků.")                  # Název má 10 znaků.

# Porovnání, které vrátí True nebo False:
print(f"Jsem za polovinou? {precteno > stran_celkem / 2}")      # True


# I vlastní funkce z lekce 5:
def procenta(cast, celek):
    return cast / celek * 100


print(f"Přečteno: {procenta(precteno, stran_celkem)} %")
