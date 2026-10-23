# Řešení cvičení 4 – Indexování a výřezy
# Tvoje řešení může vypadat jinak, a to je v pořádku.

# Zeptej se na jméno souboru a vypiš, jestli je to obrázek,
#    tedy jestli končí na .png

soubor = input("Jméno souboru: ")

if soubor.lower().endswith(".png"):
    print("Tohle je obrázek.")
else:
    print("Tohle obrázek není.")
