# Řešení bonusu 2 – Skládání textu
# Tvoje řešení může vypadat jinak, a to je v pořádku.

# V lekci 3 jsi vnořenými cykly vypsala násobilkovou tabulku. Sloupce
#    se v ní rozjely, protože dvojciferná čísla jsou širší:
#
#        1 2 3 4
#        2 4 6 8
#        3 6 9 12
#        4 8 12 16
#
#    Napiš ji znovu tak, aby čísla byla pod sebou. Tabulku rovnou
#    zvětši na 10x10, ať je rozdíl pořádně vidět.
#
#    Vnořené cykly i print s end znáš z lekce 3. Nové je jen to,
#    kolik místa každému číslu dáš.

for radek in range(1, 11):
    for sloupec in range(1, 11):
        print(f"{radek * sloupec:4}", end="")
    print()

# Každé číslo dostane čtyři místa a zarovná se doprava, takže jednotky
# skončí pod jednotkami. Největší číslo v tabulce je 100 a na to stačí
# tři místa – čtvrté dělá mezeru mezi sloupci.
#
# V lekci 3 bylo v printu end=" ", tedy mezera. Tady je end="" prázdné,
# protože mezeru už obstarává ta šířka.
