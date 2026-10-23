# Řešení bonusu 2 – Indexování a výřezy
# Tvoje řešení může vypadat jinak, a to je v pořádku.

# Napiš funkci zamen, která má na vstupu text, pozici a znak. Vrátí text,
#    který má na té pozici daný znak a jinak zůstane stejný.
#    zamen("palec", 0, "v") vrátí "valec"
#    zamen("valec", 2, "j") vrátí "vajec"

def zamen(text, pozice, znak):
    return text[:pozice] + znak + text[pozice + 1:]


print(zamen("palec", 0, "v"))
print(zamen("valec", 2, "j"))

# Výřez před pozicí, nový znak, a výřez od dalšího znaku dál.
