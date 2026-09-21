# Řešení cvičení 1 – Opakování
# Tvoje řešení může vypadat jinak, a to je v pořádku.

# Projdi cyklem for čísla od 1 do 30. Vypiš jen ta, která jsou
#    dělitelná třemi nebo pěti. (Nápověda: cislo % 3 == 0)

for cislo in range(1, 31):
    if cislo % 3 == 0 or cislo % 5 == 0:
        print(cislo)
