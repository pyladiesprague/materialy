# Řešení cvičení 5 – Skládání textu
# Tvoje řešení může vypadat jinak, a to je v pořádku.

# Slož pozvánku na několik řádků a vypiš ji jedním printem.
#    Použij tři uvozovky a f-string dohromady, hodnoty ber z proměnných.
#    Má vyjít něco jako:
#
#        POZVÁNKA
#        Anna Nováková
#
#        Kurz pokračuje ve čtvrtek od 18 hodin.
#        Místo: Dlouhá 5

jmeno = "Anna Nováková"
den = "čtvrtek"
hodina = 18
misto = "Dlouhá 5"

print(f"""POZVÁNKA
{jmeno}

Kurz pokračuje ve {den} od {hodina} hodin.
Místo: {misto}""")

# Před tři uvozovky patří f stejně jako před jedny.
