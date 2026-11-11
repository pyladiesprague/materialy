# Řešení cvičení 4 – Měnění seznamů
# Tvoje řešení může vypadat jinak, a to je v pořádku.

# Zeptej se na větu. Vypiš, kolik má slov. Pak ji vypiš se slovy
#    v opačném pořadí.
#
#      Věta: Python je fajn
#      Slov: 3
#      fajn je Python

veta = input("Věta: ")
slova = veta.split()

print(f"Slov: {len(slova)}")
print(" ".join(slova[::-1]))


# Výřez [::-1] z lekce 6 vrátí seznam pozpátku. Kdo si na něj
# nevzpomene, zvládne to i cyklem. Správně jsou obě řešení:
obracene = []

for slovo in slova:
    obracene.insert(0, slovo)

print(" ".join(obracene))
