# Řešení cvičení 5 – Opakování
# Tvoje řešení může vypadat jinak, a to je v pořádku.

from random import randrange

# Hra "hádej číslo":
#    - Počítač si vylosuje číslo od 1 do 20: randrange(1, 21)
#    - Uživatel hádá. Po každém tipu vypiš "Moc velké." nebo "Moc malé.".
#    - Když trefí, vypiš "Trefa!" a skonči.
#    - Když se netrefí ani na pátý pokus, prozraď číslo a skonči.
#    Nahoru na první řádek nezapomeň:  from random import randrange

hadane_cislo = randrange(1, 21)
pokusy = 0
while True:
    odpoved = int(input("Hádej číslo od 1 do 20: "))
    pokusy = pokusy + 1

    if odpoved == hadane_cislo:
        print("Trefa!")
        break

    if pokusy == 5:
        print("Pět pokusů je pryč. Číslo bylo", hadane_cislo)
        break

    if odpoved > hadane_cislo:
        print("Moc velké.")
    else:
        print("Moc malé.")
