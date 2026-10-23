# ---------------------------------------------
#  Užitečné metody řetězců
# ---------------------------------------------
# Spusť soubor a porovnej výsledky.

veta = "Ahoj PyLadies!"

print(veta.upper())                      # AHOJ PYLADIES!
print(veta.lower())                      # ahoj pyladies!
print(veta.count("a"))                   # 1
print(veta.replace("Ahoj", "Nazdar"))    # Nazdar PyLadies!

# count("a") našlo jedno "a" – to v PyLadies. Velké "A" ze slova Ahoj
# je pro Python jiný znak.

print("anna nováková".title())           # Anna Nováková


# Metoda strip() odstraní mezery na krajích. Ve výpisu nejsou mezery
# vidět, hranaté závorky je ukážou:
odpoved = "  ano  "
print(f"[{odpoved}]")                    # [  ano  ]
print(f"[{odpoved.strip()}]")            # [ano]


# Metod je mnohem víc. Ve VS Code napiš tečku za řetězec nebo za proměnnou
# a editor ti nabídne seznam. Pamatovat si je nemusíš.
