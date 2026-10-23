# Řešení cvičení 5 – Indexování a výřezy
# Tvoje řešení může vypadat jinak, a to je v pořádku.

# Zeptej se na slovo a vypiš, jestli se čte stejně zepředu i pozpátku.
#    Na velikosti písmen ať nezáleží, takže "Oko" projde taky.

slovo = input("Napiš slovo: ").strip().lower()

if slovo == slovo[::-1]:
    print(f"{slovo} je palindrom.")
else:
    print(f"{slovo} palindrom není.")

# Výřez s krokem -1 vrátí otočený text. Když se otočený rovná
# původnímu, je to palindrom.
