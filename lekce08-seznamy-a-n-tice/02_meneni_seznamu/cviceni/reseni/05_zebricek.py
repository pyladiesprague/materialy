# Řešení cvičení 5 – Měnění seznamů
# Tvoje řešení může vypadat jinak, a to je v pořádku.

# Máš body ze soutěže na večírku. Seřaď je od nejvyšších a vypiš tři
#    nejlepší výsledky jako výřez.
#
#    Vyjít má:  [18, 15, 12]

body = [12, 7, 18, 9, 15]

body.sort(reverse=True)
print(body[:3])
