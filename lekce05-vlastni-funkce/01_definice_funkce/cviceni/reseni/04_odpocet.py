# Řešení cvičení 4 – Definice funkce
# Tvoje řešení může vypadat jinak, a to je v pořádku.

# Napiš funkci odpocet(od), která odpočítá od zadaného čísla
#    dolů k 1 a nakonec vypíše "Teď!".
#    Zavolej ji pro 3 a pro 5.
#    Počet opakování známe, jakmile funkci zavoláme -> for.
#    range(od, 0, -1) začne na od a jde po jedné dolů. Druhé číslo se
#    do range nepočítá, takže poslední vypsané je 1.

def odpocet(od):
    for cislo in range(od, 0, -1):
        print(cislo)
    print("Teď!")


odpocet(3)
odpocet(5)
