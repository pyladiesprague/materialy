# Řešení bonusu 3 – Indexování a výřezy
# Tvoje řešení může vypadat jinak, a to je v pořádku.

# Napiš program, který se pořád dokola ptá, co má dělat:
#
#      kostka     zeptá se, kolikrát hodit, a tolikrát hodí kostkou
#      pozpatku   zeptá se na slovo a vypíše ho pozpátku
#      konec      program skončí
#
#    Odpověď uprav tak, aby prošlo i "KOSTKA" nebo "  konec  ".
#    Ošetři prázdný vstup i počet hodů, který není číslo.
#    Na cokoli jiného vypiš, že takovou volbu neznáš, a zeptej se znovu.
#    Na první řádek patří:  from random import randrange

from random import randrange

while True:
    volba = input("Co chceš dělat? (kostka / pozpatku / konec) ")
    volba = volba.strip().lower()

    if volba == "":
        print("Nic jsi nenapsala, zkus to znovu.")
    elif volba == "konec":
        break
    elif volba == "kostka":
        pocet = input("Kolikrát hodit? ").strip()
        if pocet.isdigit():
            for hod in range(int(pocet)):
                print(f"Padlo: {randrange(1, 7)}")
        else:
            print("To není číslo.")
    elif volba == "pozpatku":
        slovo = input("Jaké slovo? ").strip()
        if slovo == "":
            print("Nemám co otočit.")
        else:
            print(f"{slovo} pozpátku je {slovo[::-1]}")
    else:
        print(f"Volbu {volba} neznám.")

print("Nashledanou!")

# Nabídka, kterou jsi psala u vlastních funkcí, se ovládala čísly – text
# se dal moc snadno napsat jinak, než program čekal. Se strip() a lower()
# už na tom nezáleží a isdigit() ohlídá, co pustíš do int().
