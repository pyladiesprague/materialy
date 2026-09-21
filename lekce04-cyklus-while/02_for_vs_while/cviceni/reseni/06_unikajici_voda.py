# Řešení cvičení 6 – For versus while
# Tvoje řešení může vypadat jinak, a to je v pořádku.

# V nádrži je 45 litrů, každou minutu uteče 3 litry. Po každé minutě
#    vypiš zbytek, nakonec počet minut.
#    Kolikrát se cyklus zopakuje dopředu nevíme -> while.
voda = 45
minuty = 0
while voda > 0:
    voda = voda - 3
    minuty = minuty + 1
    print("Po", minuty, "minutách zbývá", voda, "litrů.")
print("Nádrž je prázdná po", minuty, "minutách.")
