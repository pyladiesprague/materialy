# Řešení cvičení 2 – Podmínky
# Tvoje řešení může vypadat jinak, a to je v pořádku.

# Vrať se ke studentce se třemi známkami. Spočítej průměr a vypiš
#    "Máš vyznamenání!", když je průměr menší nebo rovný 2,
#    jinak vypiš "Bez vyznamenání.".

znamka1 = 1
znamka2 = 3
znamka3 = 2
prumer = (znamka1 + znamka2 + znamka3) / 3
if prumer <= 2:
    print("Máš vyznamenání!")
else:
    print("Bez vyznamenání.")
