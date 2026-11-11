# Řešení cvičení 7 – Měnění seznamů
# Tvoje řešení může vypadat jinak, a to je v pořádku.

# Funkce má vrátit jména seřazená podle abecedy, ale program vypíše
#    None. Najdi chybu a oprav ji.

def podle_abecedy(jmena):
    jmena.sort()
    return jmena


print(podle_abecedy(["Petra", "Anna", "Jana"]))

# Metoda sort seznam seřadí, ale sama vrací None. Funkce tak vracela
# výsledek metody, ne seznam. Nejdřív seřaď, pak vrať seznam.
