# Řešení cvičení 2 – Funkce dohromady
# Tvoje řešení může vypadat jinak, a to je v pořádku.

# Napiš funkci je_sude(cislo), která vrátí True, nebo False.
#    Pak v cyklu for projdi čísla od 1 do 20 a vypiš jen sudá.

def je_sude(cislo):
    return cislo % 2 == 0


for cislo in range(1, 21):
    if je_sude(cislo):
        print(cislo)
