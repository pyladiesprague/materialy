# Řešení bonusu 1 – Funkce dohromady
# Tvoje řešení může vypadat jinak, a to je v pořádku.

# Malý kvíz. Napiš funkci otazka(text, spravna_odpoved), která
#     otázku položí, odpověď načte a vrátí True, když je správná.
#     Polož tři otázky, počítej správné odpovědi a nakonec vypiš skóre.

def otazka(text, spravna_odpoved):
    odpoved = input(text)
    return odpoved == spravna_odpoved


body = 0
if otazka("Hlavní město Česka? ", "Praha"):
    body = body + 1
if otazka("Kolik je 7 * 8? ", "56"):
    body = body + 1
if otazka("Jak se jmenuje cyklus, co běží dokud platí podmínka? ", "while"):
    body = body + 1

print("Skóre:", body, "ze 3")
