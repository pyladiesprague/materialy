# Řešení bonusu 1 – Skládání textu
# Tvoje řešení může vypadat jinak, a to je v pořádku.

# Vypiš diplom v rámečku z hvězdiček:
#
#    **************************
#    * Anna Nováková          *
#    * Python pro začátečnice *
#    **************************
#
#    Rámeček musí být přesně tak široký, jak je potřeba. Když jméno
#    nebo název kurzu vyměníš za delší, musí se přizpůsobit sám –
#    šířku tedy spočítej, nepiš ji natvrdo.

jmeno = "Anna Nováková"
kurz = "Python pro začátečnice"

# Nejdelší z obou řádků určuje šířku vnitřku. Ke každému řádku patří
# ještě hvězdička a mezera z obou stran, tedy čtyři znaky navíc.
vnitrek = max(len(jmeno), len(kurz))
sirka = vnitrek + 4

print("*" * sirka)
print(f"* {jmeno:{vnitrek}} *")
print(f"* {kurz:{vnitrek}} *")
print("*" * sirka)

# Šířka se dá do složených závorek dosadit z proměnné – proto
# {jmeno:{vnitrek}}.
#
# Bez toho zápisu to jde taky, jen delším plusem:
#
#     print("* " + jmeno + " " * (vnitrek - len(jmeno)) + " *")
