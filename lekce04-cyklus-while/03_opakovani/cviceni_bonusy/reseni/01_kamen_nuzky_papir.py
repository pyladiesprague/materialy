# Řešení bonusu 1 – Opakování
# Tvoje řešení může vypadat jinak, a to je v pořádku.

from random import randrange

# Kámen, nůžky, papír – znáš z bonusu v lekci 2, kde hráli
#     dva lidé. Teď to rozšíříme: hraješ proti počítači a na víc kol.
#     - Zeptej se na svůj tah: "kamen", "nuzky" nebo "papir".
#     - Počítač si tah vylosuje: randrange(1, 4) vrátí 1, 2 nebo 3,
#       tak si to číslo přelož na tah (1 = kamen, 2 = nuzky, 3 = papir).
#     - Vypiš, co hrál počítač, a kdo kolo vyhrál.
#     - Pak se zeptej "Hrát znovu? (ano/ne) " a podle odpovědi
#       buď pokračuj, nebo skonči.
#     Kdo koho poráží: kámen tupí nůžky, nůžky stříhají papír,
#     papír balí kámen.
#     Nahoru na první řádek nezapomeň:  from random import randrange

while True:
    tvuj_tah = input("Tvůj tah (kamen/nuzky/papir): ")

    # Počítač umí vylosovat jen číslo, tak si ho přeložíme na tah.
    cislo = randrange(1, 4)
    if cislo == 1:
        pocitac = "kamen"
    elif cislo == 2:
        pocitac = "nuzky"
    else:
        pocitac = "papir"
    print("Počítač hrál:", pocitac)

    # Kdo vyhrál: kámen tupí nůžky, nůžky stříhají papír, papír balí kámen.
    vyhrala_kamenem = tvuj_tah == "kamen" and pocitac == "nuzky"
    vyhrala_nuzkami = tvuj_tah == "nuzky" and pocitac == "papir"
    vyhrala_papirem = tvuj_tah == "papir" and pocitac == "kamen"

    if tvuj_tah == pocitac:
        print("Remíza.")
    elif vyhrala_kamenem or vyhrala_nuzkami or vyhrala_papirem:
        print("Vyhrála jsi!")
    else:
        print("Prohrála jsi.")

    znovu = input("Hrát znovu? (ano/ne) ")
    if znovu == "ne":
        break

print("Díky za hru!")
