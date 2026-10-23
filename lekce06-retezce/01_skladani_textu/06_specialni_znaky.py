# ---------------------------------------------
#  Speciální znaky v textu
# ---------------------------------------------
# Spusť soubor a porovnej, co se vypsalo, s tím, co je v uvozovkách.


# Zpětné lomítko a n (\n) uvnitř textu znamená nový řádek.
# Tenhle jeden print vypíše tři řádky:
print("Anna Nováková\nDlouhá 5\nPraha")


# Uvozovka text ukončuje. Když ji chceš mít uvnitř, označíš ji lomítkem:
print("Řekla \"ahoj\" a odešla.")

# Nebo použiješ druhý druh uvozovek, jednoduché:
print('Řekla "ahoj" a odešla.')


# Když má lomítko zůstat lomítkem, píše se dvakrát. Cesta k souboru:
print("C:\\Users\\Anna\\dokumenty")

# S jedním lomítkem by Python u "\U" hlásil chybu, protože by ho četl
# jako začátek speciálního znaku. Cesty k souborům budeš psát v lekci 13.


# Delší text se píše mezi tři uvozovky a řádkuje se, jak potřebuješ.
# Tenhle zápis jsi viděla v lekci 5 u popisu funkce:
print("""Milá Anno,

kurz pokračuje v úterý od šesti.
Těšíme se!""")


# I před tři uvozovky patří f, když chceš doplňovat hodnoty:
jmeno = "Anna Nováková"
den = "úterý"
hodina = 18
print(f"""Přihláška přijata

Jméno:  {jmeno}
Termín: {den} od {hodina} hodin""")
