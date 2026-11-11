# ---------------------------------------------
#  Procházení seznamu cyklem for
# ---------------------------------------------
# Spusť soubor a porovnej výsledky.

hoste = ["Anna", "Petra", "Jana", "Adéla"]


# Cyklus for prochází seznam stejně jako řetězec. Místo znaků dostaneš
# po jedné položce seznamu. Pozvánky jsou hotové na dva řádky:
for host in hoste:
    print(f"Milá {host}, přijď v sobotu na večírek!")

# Milá Anna, přijď v sobotu na večírek!
# Milá Petra, přijď v sobotu na večírek!
# Milá Jana, přijď v sobotu na večírek!
# Milá Adéla, přijď v sobotu na večírek!


# Kolik hostů má jméno na A? V lekci 3 jsi počítala sudá čísla
# v range: proměnná začne na nule a v cyklu se jí přičte jednička
# pokaždé, když platí podmínka. Takové proměnné se říká počítadlo.
# U seznamu to funguje stejně, jen místo čísel procházíš jména:
pocet_na_a = 0

for host in hoste:
    if host[0] == "A":
        pocet_na_a = pocet_na_a + 1

print(f"Jmen na A: {pocet_na_a}")     # Jmen na A: 2
