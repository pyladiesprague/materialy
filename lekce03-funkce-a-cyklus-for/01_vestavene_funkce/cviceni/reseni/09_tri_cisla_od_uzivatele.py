# Řešení cvičení 9 – Vestavěné funkce
# Tvoje řešení může vypadat jinak, a to je v pořádku.

# Zeptej se uživatele na tři čísla (klidně i záporná) a vypiš,
#    jak velké je to největší z nich bez ohledu na znaménko.
#    Např. z čísel -20, 5 a 12 je největší velikost 20.

a = int(input("Zadej první číslo: "))
b = int(input("Zadej druhé číslo: "))
c = int(input("Zadej třetí číslo: "))
print(max(abs(a), abs(b), abs(c)))     # abs zahodí znaménko, max vybere největší
