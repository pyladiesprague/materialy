# Řešení cvičení 2 – Procházení textu
# Tvoje řešení může vypadat jinak, a to je v pořádku.

# Bum-Bác. Tuhle úlohu znáš z minula pro jedno číslo – teď ji necháme
#    proběhnout cyklem. Vypiš čísla od 1 do 30, ale:
#    - za dělitelné třemi i pěti zároveň vypiš "BumBác",
#    - za dělitelné jen třemi vypiš "Bum",
#    - za dělitelné jen pěti vypiš "Bác",
#    - jinak vypiš samotné číslo.

for cislo in range(1, 31):
    if cislo % 15 == 0:                 # dělitelné 3 i 5 = dělitelné 15, musí být první
        print("BumBác")
    elif cislo % 3 == 0:
        print("Bum")
    elif cislo % 5 == 0:
        print("Bác")
    else:
        print(cislo)
