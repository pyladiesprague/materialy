# Řešení bonusu 3 – Funkce dohromady
# Tvoje řešení může vypadat jinak, a to je v pořádku.

from random import randrange

# Hra na hádání čísla, celá poskládaná z funkcí – losování,
#     načtení tipu i vyhodnocení ať má každé svoji.
#     Hlavní cyklus while pak jenom tyhle funkce volá.

def vylosuj_cislo():
    return randrange(1, 21)


def zeptej_se_na_tip():
    return int(input("Hádej číslo od 1 do 20: "))


def je_trefa(tip, hledane):
    return tip == hledane


def napoveda(tip, hledane):
    if tip > hledane:
        return "Moc velké."
    else:
        return "Moc malé."


hledane_cislo = vylosuj_cislo()
while True:
    tip = zeptej_se_na_tip()
    if je_trefa(tip, hledane_cislo):
        print("Trefa!")
        break
    print(napoveda(tip, hledane_cislo))
