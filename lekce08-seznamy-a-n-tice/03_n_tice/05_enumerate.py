# ---------------------------------------------
#  Enumerate: položka i její pořadí
# ---------------------------------------------
# Spusť soubor a porovnej výsledky.

program = ["přípitek", "večeře", "tombola"]


# Někdy potřebuješ u položky znát i její pořadí. Funkce enumerate ke
# každé položce přidá číslo a vrátí dvojice, které rozbalíš:
for poradi, bod in enumerate(program):
    print(poradi, bod)

# 0 přípitek
# 1 večeře
# 2 tombola


# Pro lidi je lepší číslovat od jedničky. Funkce enumerate má parametr
# start s výchozí hodnotou 0. Nastavíš ho stejně jako reverse u řazení,
# i se jménem:
for poradi, bod in enumerate(program, start=1):
    print(f"{poradi}. {bod}")

# 1. přípitek
# 2. večeře
# 3. tombola
