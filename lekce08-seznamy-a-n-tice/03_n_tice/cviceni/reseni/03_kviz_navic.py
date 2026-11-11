# Řešení cvičení 3 – N-tice
# Tvoje řešení může vypadat jinak, a to je v pořádku.

# Rozšiř kvíz z výkladu:
#    - přidej dvě vlastní otázky,
#    - před každou otázkou vypiš, kolikátá je, třeba "Otázka 2/5"
#      (pomůže ti enumerate),
#    - na konci vypiš skóre v procentech a seznam otázek, na které
#      hráčka odpověděla špatně.
#
#      Otázka 1/5
#      Kolik je 7 * 8? 54
#      ...
#      Skóre: 60 %
#      Špatně: ['Kolik je 7 * 8? ', 'Hlavní město Česka? ']

kviz = [
    ("Kolik je 7 * 8? ", "56"),
    ("Hlavní město Česka? ", "Praha"),
    ("Jak se jmenuje cyklus, co běží, dokud platí podmínka? ", "while"),
    ("Jakou metodou přidáš položku na konec seznamu? ", "append"),
    ("Kolik hodnot má dvojice? ", "2"),
]
body = 0
spatne = []

for cislo, polozka in enumerate(kviz, start=1):
    otazka, spravna = polozka
    print(f"Otázka {cislo}/{len(kviz)}")
    odpoved = input(otazka).strip()
    if odpoved == spravna:
        body = body + 1
    else:
        spatne.append(otazka)

print(f"Skóre: {body / len(kviz) * 100:.0f} %")
print(f"Špatně: {spatne}")
