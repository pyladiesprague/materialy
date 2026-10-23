# ---------------------------------------------
#  Index: jeden znak z textu
# ---------------------------------------------
# Spusť soubor. Na konci schválně spadne – tu chybu si přečti.

slovo = "PyLadies"


# Cyklus for z lekce 3 ti podal znaky po jednom, od začátku do konce.
# Když chceš jenom jeden konkrétní, sáhneš si na něj rovnou. Každý znak
# má svoje pořadové číslo, kterému se říká index. Počítá se od nuly,
# takže první písmeno má index 0:
#
#          P   y   L   a   d   i   e   s
#        ╭───┬───┬───┬───┬───┬───┬───┬───╮
#        │ 0 │ 1 │ 2 │ 3 │ 4 │ 5 │ 6 │ 7 │   index
#        │-8 │-7 │-6 │-5 │-4 │-3 │-2 │-1 │   index od konce
#        ╰───┴───┴───┴───┴───┴───┴───┴───╯
#
# (Obě čtení čísel ukazuje vedle sebe obrázek index_a_vyrez.png.)

print(slovo[0])     # P
print(slovo[1])     # y
print(slovo[2])     # L


# Poslední index je proto o jedna menší než délka:
print(len(slovo))   # 8
print(slovo[7])     # s


# Od konce se dá počítat záporně a je to kratší:
print(slovo[-1])    # s
print(slovo[-2])    # e


# Index jde dosadit i z proměnné nebo z výpočtu:
pozice = 3
print(slovo[pozice])            # a
print(slovo[len(slovo) - 1])    # s


# Index, který v textu není, skončí chybou IndexError:
print(slovo[8])
