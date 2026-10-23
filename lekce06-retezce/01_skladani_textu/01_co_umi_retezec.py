# ---------------------------------------------
#  Co už s textem umíme
# ---------------------------------------------
# Spusť soubor a porovnej výsledky.
#
# Textu se v Pythonu odborně říká řetězec (anglicky string) – řetěz znaků
# navázaných za sebou. Pracuješ s ním od první lekce. Tohle už znáš:

print("Ahoj" + " " + "PyLadies!")   # spojení plusem    (lekce 1)
print("=" * 20)                     # opakování         (lekce 1)
print(len("Ahoj"))                  # délka – 4         (lekce 3)
print("o" in "Ahoj")                # hledání – True    (lekce 3)

for pismeno in "Ahoj":              # průchod po znacích    (lekce 3)
    print(pismeno)


# Z lekce 1 taky víš, že input() vrací text a int() z něj udělá číslo.
# Opačný směr má na starosti funkce str():
vek = 30
print("Je mi " + str(vek) + " let")     # Je mi 30 let

# Plus spojuje text s textem. Bez str() by ten řádek spadl na TypeError.


# Čím víc kousků, tím hůř se taková věta píše i čte – uhlídat je potřeba
# každou mezeru a kolem každého čísla str():
jmeno = "Anna"
print("Ahoj " + jmeno + ", je ti " + str(vek) + " let.")
