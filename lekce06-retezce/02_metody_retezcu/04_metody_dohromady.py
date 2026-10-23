# ---------------------------------------------
#  Metody za sebou
# ---------------------------------------------
# Spusť soubor a zkus různé odpovědi: ano, ANO, nebo ano s mezerou.
#
# V lekci 2 jsi odpověď porovnávala přímo:
#   if odpoved == "ano":
# Taková podmínka projde jen u přesně napsaného "ano". "ANO" ani " ano "
# už neprojdou, i když uživatelka myslela to samé.

odpoved = input("Chceš pokračovat? (ano/ne) ")

upravena = odpoved.strip().lower()
print(f"[{upravena}]")

if upravena == "ano":
    print("Pokračujeme.")
else:
    print("Končíme.")


# Dvě metody se dají napsat za sebe na jeden řádek. Vyhodnocuje se to
# zleva doprava:
#   odpoved.strip()    nejdřív zmizí mezery na krajích
#   .lower()           z toho výsledku pak vzniknou malá písmena
#
# Kdyby byly dva kroky přehlednější, jde to i takhle:
#   bez_mezer = odpoved.strip()
#   upravena = bez_mezer.lower()
