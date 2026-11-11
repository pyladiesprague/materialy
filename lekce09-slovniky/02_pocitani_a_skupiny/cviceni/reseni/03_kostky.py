# Řešení cvičení 3 – Počítání a skupiny
# Tvoje řešení může vypadat jinak, a to je v pořádku.

from random import randrange

# Hoď kostkou 600krát a spočítej, kolikrát padlo které číslo.
#    - Slovník si připrav předem: klíče 1 až 6, hodnoty 0. Tak v něm budou
#      všechna čísla, a to ve správném pořadí.
#    - Vypiš každé číslo s řadou hvězdiček. Jedna hvězdička znamená 10 hodů.
#
#      1: ********* (97)
#      2: ********** (104)
#      ...
#
#    Na první řádek patří:  from random import randrange
#    randrange(1, 7) vrátí náhodné číslo od 1 do 6.

pocty = {}
for cislo in range(1, 7):
    pocty[cislo] = 0

for hod in range(600):
    cislo = randrange(1, 7)
    pocty[cislo] = pocty[cislo] + 1

for cislo, pocet in pocty.items():
    hvezdicky = "*" * (pocet // 10)
    print(f"{cislo}: {hvezdicky} ({pocet})")
