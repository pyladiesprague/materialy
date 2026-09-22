# Řešení cvičení 1 – Návratová hodnota
# Tvoje řešení může vypadat jinak, a to je v pořádku.

# Napiš funkci cena_s_dph(cena), která vrátí cenu i s 21% DPH.
#    Vypiš cenu za 100 Kč a za 250 Kč.

def cena_s_dph(cena):
    return cena * 1.21


print("100 Kč s DPH:", cena_s_dph(100))
print("250 Kč s DPH:", cena_s_dph(250))
