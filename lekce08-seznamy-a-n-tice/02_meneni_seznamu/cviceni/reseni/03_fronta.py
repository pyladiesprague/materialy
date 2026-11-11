# Řešení cvičení 3 – Měnění seznamů
# Tvoje řešení může vypadat jinak, a to je v pořádku.

# U fotokoutku na večírku stojí fronta. Dokud v ní někdo je, vezmi
#    první na řadě a vypiš "Fotí se: ...". Na konci vypiš
#    "Fronta je prázdná.".

fronta = ["Anna", "Petra", "Jana"]

while len(fronta) > 0:
    host = fronta.pop(0)
    print(f"Fotí se: {host}")

print("Fronta je prázdná.")
