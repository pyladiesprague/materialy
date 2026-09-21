# Řešení cvičení 2 – Opakování
# Tvoje řešení může vypadat jinak, a to je v pořádku.

# Uživatel zadá slovo. Spočítej, kolikrát se v něm objeví
#    písmeno "a", a výsledek vypiš.

slovo = input("Zadej slovo: ")
pocet = 0
for pismeno in slovo:
    if pismeno == "a":
        pocet = pocet + 1
print("Písmeno 'a' je ve slově", pocet, "krát")
