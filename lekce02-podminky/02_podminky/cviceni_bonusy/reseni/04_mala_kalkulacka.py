# Řešení bonusu 4 – Podmínky
# Tvoje řešení může vypadat jinak, a to je v pořádku.

# Malá kalkulačka.
#     Zeptej se na dvě čísla a na znaménko (+, -, *, /).
#     Podle znaménka vypiš výsledek správné operace.
#     Bonus v bonusu: ošetři dělení nulou vlastní hláškou.

a = float(input("První číslo: "))
b = float(input("Druhé číslo: "))
znamenko = input("Znaménko (+, -, *, /): ")

if znamenko == "+":
    print(a + b)
elif znamenko == "-":
    print(a - b)
elif znamenko == "*":
    print(a * b)
elif znamenko == "/":
    if b == 0:
        print("Nulou dělit nelze.")
    else:
        print(a / b)
else:
    print("Neznámé znaménko.")
