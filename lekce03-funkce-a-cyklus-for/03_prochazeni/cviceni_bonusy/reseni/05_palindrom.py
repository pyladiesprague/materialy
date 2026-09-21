# Řešení bonusu 5 – Procházení textu
# Tvoje řešení může vypadat jinak, a to je v pořádku.

# Palindrom. Uživatel zadá slovo. Zjisti, jestli se čte stejně
#     zepředu i zezadu (třeba "kajak" nebo "radar").
#     Zamysli se, jak si slovo poskládáš pozpátku a jak obě verze porovnáš.

slovo = input("Napiš slovo: ")
obracene = ""
for znak in slovo:
    obracene = znak + obracene           # každé písmeno dáme PŘED dosavadní výsledek
if slovo == obracene:
    print("Je to palindrom.")
else:
    print("Není to palindrom.")
