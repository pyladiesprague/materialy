# Řešení cvičení 2 – Měnění seznamů
# Tvoje řešení může vypadat jinak, a to je v pořádku.

# Kamarádka ti poslala tajnou zprávu: skrývá se v prvních písmenech
#    slov. Postav seznam prvních písmen a pak je spoj do jednoho slova.
#
#    Vyjít má:  DORT

slova = ["Dům", "Okno", "Ryba", "Tužka"]

pismena = []

for slovo in slova:
    pismena.append(slovo[0])

print("".join(pismena))
