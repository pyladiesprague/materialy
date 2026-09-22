# Řešení bonusu 3 – Definice funkce
# Tvoje řešení může vypadat jinak, a to je v pořádku.

from random import randrange

# Napiš funkci hod_kostkou(), která hodí kostkou a hod vypíše.
#     Zavolej ji cyklem for pětkrát za sebou.

def hod_kostkou():
    hod = randrange(1, 7)
    print("Padlo:", hod)


for pokus in range(5):
    hod_kostkou()
