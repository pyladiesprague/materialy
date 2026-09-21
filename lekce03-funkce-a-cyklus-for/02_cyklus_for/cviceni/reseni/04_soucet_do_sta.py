# Řešení cvičení 4 – Cyklus for
# Tvoje řešení může vypadat jinak, a to je v pořádku.

# Spočítej součet všech čísel od 1 do 100 pomocí cyklu for
#    (ne funkcí sum) a výsledek vypiš.

soucet = 0
for cislo in range(1, 101):
    soucet = soucet + cislo
print(soucet)                 # 5050
