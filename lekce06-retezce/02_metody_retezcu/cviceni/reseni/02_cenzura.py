# Řešení cvičení 2 – Metody řetězců
# Tvoje řešení může vypadat jinak, a to je v pořádku.

# Věta z firemní prezentace je plná frází. Vyměň je za srozumitelná
#    slova a výsledek vypiš:
#
#        proaktivně     -> včas
#        implementovat  -> zařídit
#        synergie       -> spolupráci
#
#    Výměny dělej po krocích, ať se řádky dají přečíst.

veta = "Musíme proaktivně implementovat synergie napříč týmy."

srozumitelne = veta.replace("proaktivně", "včas")
srozumitelne = srozumitelne.replace("implementovat", "zařídit")
srozumitelne = srozumitelne.replace("synergie", "spolupráci")

print(srozumitelne)     # Musíme včas zařídit spolupráci napříč týmy.

# Každý replace() vrací nový řetězec, takže další se volá rovnou na něm.
# Zřetězit se dají i za sebe na jeden řádek, u tří výměn by ale byl
# dlouhý přes celou obrazovku.
