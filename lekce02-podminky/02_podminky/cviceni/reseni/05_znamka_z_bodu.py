# Řešení cvičení 5 – Podmínky
# Tvoje řešení může vypadat jinak, a to je v pořádku.

# Zeptej se na počet bodů z testu (0 až 100) a vypiš známku:
#    90 a víc → 1, 75 a víc → 2, 60 a víc → 3, 40 a víc → 4,
#    jinak → 5.

body = int(input("Kolik bodů? "))
if body >= 90:
    print(1)
elif body >= 75:
    print(2)
elif body >= 60:
    print(3)
elif body >= 40:
    print(4)
else:
    print(5)
