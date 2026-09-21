# Řešení bonusu 1 – Cyklus while
# Tvoje řešení může vypadat jinak, a to je v pořádku.

from random import randrange

# Hra "Oko bere":
#     - Začínáš s 0 body.
#     - V každém kole se ukáže, kolik máš bodů, a zeptáš se,
#       jestli si chceš líznout kartu.
#     - Když ano, počítač ti dá náhodnou kartu 2 až 10
#       (randrange(2, 11)) a přičte ji k bodům.
#     - Cíl je dostat se přesně na 21. Když přetáhneš přes 21, prohráváš.
#     - Když řekneš, že už nechceš, hra skončí a vypíše se výsledek.
#     Nahoru na první řádek nezapomeň:  from random import randrange

soucet = 0
while soucet < 21:
    print("Máš", soucet, "bodů.")
    odpoved = input("Chceš si líznout? (ano/ne) ")
    if odpoved == "ne":
        break
    karta = randrange(2, 11)
    print("Lízla sis", karta)
    soucet = soucet + karta

if soucet == 21:
    print("Přesně 21, vyhráváš!")
elif soucet > 21:
    print("Přetáhla jsi přes 21, prohráváš. Máš", soucet)
else:
    print("Končíš s", soucet, "body.")
